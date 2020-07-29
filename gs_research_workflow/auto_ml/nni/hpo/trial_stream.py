# -*- coding: UTF-8 -*-
import os

import faust
import nni
from gs_framework.activatable_stateful_service import Env, Activatable
from gs_framework.object_reference import ObjectRef
from gs_framework.state_var_change_dispatcher import state_var_change_handler, pick_one_change
from gs_framework.state_variable import StateVariable
from typing import Mapping, Any, Callable, Union
import logging

from gs_framework.stateful_object import State

logger = logging.getLogger(__name__)

topic_gs_nni_trial = faust.types.TP(f"GS_NNI_TRIAL", 1)
ENV_KEY_TRIAL_IN_NNI = "trial_in_nni"


# ---- [laigen 2020.02.29] colab train 不再通过 kafka 进行，这里先去掉。  ----
# class TrialColabSideEnv(Env):
#     """Colab Side Env 用于更新 state 信息"""
#
#     intermediate_metrics = StateVariable(dtype=Mapping[str, Any], default_val=None, help="intermediate_metrics")
#     final_metrics = StateVariable(dtype=Union[Mapping[str, Any], float], default_val=None, help="final_metrics")
#
#     def __init__(self, trial_cfg_hash_gid: str, one_trial_spec_val: str):
#         """Note: 允许避免相同的 trial 的多次数据之间的干扰，增加一个 one_trial_spec_val 可以让 msg 的 pk 进行区分"""
#         super().__init__()
#         self.trial_hash_gid = trial_cfg_hash_gid
# ----


class LocalRunGSWorkflowEnv(Env):
    """作为colab的替代，允许在local环境运行train"""

    need_to_run_flag = StateVariable(dtype=int, default_val=0, help="set state to run")

    def __init__(self, trial_hash_id: str, experiment_name: str, experiment_uuid: str, trial_uuid: str):
        super().__init__()
        self._trial_hash_id = trial_hash_id
        self.trial_uuid = trial_uuid
        self.experiment_name = experiment_name
        self.experiment_uuid = experiment_uuid

    # ---- [laigen 2020.02.29] colab train 不再通过 kafka 进行，这里先去掉。  ----
    # def set_workflow_data(self, cfg_file: str, metrics_topic: faust.types.TP):
    # ---- end ----
    def set_workflow_data(self, cfg_file: str):
        self._cfg_file = cfg_file
        # ---- [laigen 2020.02.29] colab train 不再通过 kafka 进行，这里先去掉。  ----
        # self._metric_topic = metrics_topic
        # ---- end ----

    async def exec_train_workflow(self):
        from gs_research_workflow.common.serialization_utilities import load_mapping_from_file
        from gs_research_workflow.core.gs_step import create_step_by_dict
        from gs_research_workflow.auto_ml.nni.hpo.trial_stream import topic_gs_nni_trial

        workflow_cfg, workflow_context = load_mapping_from_file(self._cfg_file)
        workflow_inst = create_step_by_dict(workflow_cfg, workflow_context)
        workflow_inst.prepare_metrics_recorder(self.experiment_name, self.experiment_uuid, self.trial_uuid)
        # 这里假定一定是 TFTrainStep 这个对象
        # ---- [laigen 2020.02.29] colab train 不再通过 kafka 进行，这里先去掉。  ----
        # await workflow_inst.prepare_metrics_callback(self._trial_hash_id, self.trial_uuid, topic_gs_nni_trial)
        # ---- end ----
        await workflow_inst.fit()
        await workflow_inst.eval_model()
        await workflow_inst.stop_env()

    # 无法trigger 的写法 ：
    # @state_var_change_handler(state_vars="need_to_run_flag")
    @state_var_change_handler(state_vars=need_to_run_flag)
    @pick_one_change
    async def on_need_to_run_flag_change(self, state_var_owner_pk: Any, state_var_name: str, need_to_run_flag: int):
        logger.info(f"in on_need_to_run_flag_change {need_to_run_flag}")
        if need_to_run_flag:
            await self.exec_train_workflow()
