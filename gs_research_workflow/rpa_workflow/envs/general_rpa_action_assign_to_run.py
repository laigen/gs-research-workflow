# -*- coding: UTF-8 -*-

"""
一个通用的基于 mongo 中已经保存的 rpa action 的调度 environment，主要提供的功能有：
1) 收集执行环境的信息，有空闲的时候，从 db 中的队列找到下一个需要 assign 的 action push 到 kafka 进行执行
2) action 执行完成后，调用相应的函数，进行数据的入库工作
3) 做一个最简单的容错机制，action 30min 之后没有返回结果，则认为超时失败。提交下一个 action 加入到执行队列中

NOTE：以后考虑增加的复杂功能
1) 多机并行执行 action，多机状态信息的维护
2) 出错 action 的 retry
3) 根据 remote pc 的资源情况进行调整
"""
import asyncio
from datetime import datetime
from typing import Dict, Any, Callable, Optional, List
import logging

from gs_framework import Env, ObjectStateStream, StateVariable, state_var_change_handler, pick_one_change, \
    StatefulObjectAndCommitStream, create_stateful_object, timer
from gs_research_workflow.rpa_workflow.kw_search_srvs import topic_kw_search

from gs_research_workflow.common.serialization_utilities import str_to_cls, cls_to_str

from gs_research_workflow.rpa_workflow.act_msg_data import WinRPAAction, RPAActionOrigResult, ActionResultBinary, \
    RPAAction, topic_uipath_actions

from gs_research_workflow.common.mongo_resource import db_nlp, used_db_position, mongo_db_conn
from gs_research_workflow.rpa_workflow.actions.action_doc_in_mongo import RPAActionDoc, RPABatchAction, ActionStatusFlag
import pickle

from gs_research_workflow.rpa_workflow.result_extraction.utilities import upsert_document

logger = logging.getLogger(__name__)


mongo_db_conn(used_db_position, db_nlp)

TIMEOUT_IN_SECS: int = 60 * 30


class GeneralRPAActionExecutionEnv(Env):
    uipath_action_stream = ObjectStateStream.bind_at_runtime()

    _actions_in_running = StateVariable(dtype=dict, default_val=None,
                                        help="key:action_uuid , value:action add to exec")

    def __init__(self):
        super().__init__()

        self.all_managed_pcs: set[str] = {"GS_ROBOT.VPC001"}
        """先 hardcode 所有的 pc 内容，以后在考虑动态管理，多 pc 的处理"""

    @state_var_change_handler(state_vars=WinRPAAction.action_orig_result, state_var_source=uipath_action_stream)
    @pick_one_change
    async def on_act_orig_result(self, state_var_owner_pk: Any, state_var_name: str,
                                 act_orig_result: RPAActionOrigResult):
        # logger.info(f"Search result msg. {act_orig_result.creator_uuid} - {self.pk}")
        if act_orig_result.creator_uuid != self.pk:
            return
        logger.info(f"RPA action result returned. {act_orig_result.creator_uuid} - {act_orig_result.success_flag}")
        # act_orig_result.rlt_data 解包解压后存入 Mongo，同时生成 state 的 dataframe 数据对象
        action_uuid = state_var_owner_pk
        rlt_bin_data = None
        if act_orig_result.rlt_bin_data_uuid:
            rlt_bin_doc = ActionResultBinary.objects.get(uuid=act_orig_result.rlt_bin_data_uuid)
            rlt_bin_data = rlt_bin_doc.bin
            logger.info(f"bin data result length={len(rlt_bin_data)}")
            # KWSearchExternalEnv.upload_search_result_via_tar_binary(state_var_owner_pk, rlt_bin_data)
        GeneralRPAActionExecutionEnv.proc_action_result(action_uuid, rlt_bin_data)
        if self._actions_in_running.VALUE and action_uuid in self._actions_in_running.VALUE:
            del self._actions_in_running.VALUE[action_uuid]
            self._actions_in_running.mark_changed()
        # 还有正在执行的 action ,就先不发送新的出去
        if self._actions_in_running.VALUE is not None and len(self._actions_in_running.VALUE) > 0:
            return
        # query next action to run
        next_act_to_run = self.query_action_to_run()
        if next_act_to_run is None:
            return
        return self.create_action_run_msg(next_act_to_run)

    @staticmethod
    def proc_action_result(action_uuid, action_bin_result: bytes):
        # 得到 action batch uuid
        # 解包 文件，并解析入库
        action_doc: RPAActionDoc = RPAActionDoc.objects(act_id=action_uuid).first()
        if action_doc is None:
            return
        batch_id = action_doc.batch_id
        action_doc.status_flag = ActionStatusFlag.Finished.value
        action_doc.response_t = datetime.now()
        upsert_document(action_doc, False)

        # 数据保存到 db
        def action_result_save_to_mongo(f_save):
            import tarfile
            import os
            import tempfile

            with tempfile.TemporaryDirectory() as tmp_dir:
                tar_file = os.path.join(tmp_dir, "action_result.tar.gz")
                with open(tar_file, "w+b") as tar_f:
                    tar_f.write(action_bin_result)
                    tar_f.flush()
                tar = tarfile.open(tar_file, "r:gz")
                tar.extractall(tmp_dir)
                tar.close()
                try:
                    f_save(os.path.join(tmp_dir, action_doc.act_id), batch_id, action_uuid, True)
                except Exception as ex:
                    logger.error(
                        f"An error occur when extract action '{action_uuid}' ,  proc function '{cls_to_str(f_save)}' ,error_info:'{ex}'")

        action_result_save_to_mongo(str_to_cls(action_doc.result_process_function))

        # NOTE： 暂时先在 action process 里调用，以后可以把这个放到另一个异步过程中进行调用
        if action_doc.finished_triggered_function:
            try:
                f_after_action_finished = str_to_cls(action_doc.finished_triggered_function)
                f_after_action_finished(batch_id, action_uuid)
            except Exception as ex:
                logger.error(
                    f"An error occur when '{action_uuid}' finished trigger function '{action_doc.finished_triggered_function}' ,error_info:'{ex}'")

        batch_action: RPABatchAction = RPABatchAction.objects(batch_id=batch_id).first()
        if batch_action:
            batch_action.finished_action_count = RPAActionDoc.objects(batch_id=batch_id, status_flag__in=[
                ActionStatusFlag.RunningTimeout.value, ActionStatusFlag.Finished.value]).count()
            upsert_document(batch_action, False)

        # 因为有动态的 BatchAction , 这里比较难判定 batch_action 的 status
        # if batch_action.real_action_count <= batch_action.finished_action_count:
        #     batch_action.status = ActionStatusFlag.Finished.value

    def query_action_to_run(self) -> Optional[RPAActionDoc]:
        return RPAActionDoc.objects(status_flag=ActionStatusFlag.WaitingForRun.value).order_by("act_ctime").first()

    def create_action_run_msg(self, action_doc: RPAActionDoc) -> StatefulObjectAndCommitStream:
        act_uuid = action_doc.act_id
        act = create_stateful_object(act_uuid, WinRPAAction)
        act[WinRPAAction.action_uuid].VALUE = act_uuid

        act_obj: RPAAction = pickle.loads(action_doc.act)
        # 需要补充三项内容，创建者的 pk, class 以及 target pc
        act_obj.creator_cls = cls_to_str(self.__class__)
        act_obj.creator_uuid = self.pk
        assigned_pc = next(iter(self.all_managed_pcs))  # NOTE:这里先固定指派机器
        act_obj.action_executor_required_tags.append(f"pc_id:{assigned_pc}")
        act_obj.ctime = datetime.now()
        act[WinRPAAction.action].VALUE = act_obj

        # 同步 mongo 中的信息
        action_doc.status_flag = ActionStatusFlag.Running.value
        action_doc.add_to_exec_queue_t = datetime.now()
        action_doc.target_pc_id = assigned_pc
        upsert_document(action_doc, False)

        # 同步 env 的 state variable
        if self._actions_in_running.VALUE is None:
            self._actions_in_running.VALUE = dict()
        self._actions_in_running.VALUE[act_uuid] = datetime.now()
        self._actions_in_running.mark_changed()

        logger.info(f"start an RPA action {action_doc.act_id} - {action_doc.act_description}")

        return StatefulObjectAndCommitStream(act, self.uipath_action_stream)

    @timer(interval=60)
    async def on_one_minute(self):
        # 检查有没有超时的 action
        timeout_actions: List[str] = list()

        if self._actions_in_running.VALUE is not None:
            for act_uuid, added_t in self._actions_in_running.VALUE.items():
                if (datetime.now() - added_t).total_seconds() >= TIMEOUT_IN_SECS:
                    timeout_actions.append(act_uuid)
        for act_uuid in timeout_actions:
            del self._actions_in_running.VALUE[act_uuid]
        self._actions_in_running.mark_changed()
        # 更新 mongo db 中的内容
        for act_uuid in timeout_actions:
            act_doc: RPAActionDoc = RPAActionDoc.objects(act_id=act_uuid).first()
            if act_doc:
                act_doc.status_flag = ActionStatusFlag.RunningTimeout.value
                upsert_document(act_doc, False)

        if not self._actions_in_running.VALUE:
            next_action = self.query_action_to_run()
            if next_action:
                return self.create_action_run_msg(next_action)


async def start_env():
    logger.info(f"----------- preparing -------------")
    env = GeneralRPAActionExecutionEnv()
    env.bind(topic_define=topic_kw_search)
    env.uipath_action_stream.bind(topic_define=topic_uipath_actions)

    logger.info(f"----------- env start -------------")
    await env.start()


def debug_one_action_result(action_uuid: str):
    rlt_bin_data = None
    rlt_bin_doc = ActionResultBinary.objects.get(action_uuid=action_uuid)
    rlt_bin_data = rlt_bin_doc.bin
    logger.info(f"bin data result length={len(rlt_bin_data)}")
    GeneralRPAActionExecutionEnv.proc_action_result(action_uuid, rlt_bin_data)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_env())
    loop.run_forever()

    # debug_one_action_result("59B689FDAE57458495F0600154FB4108")
