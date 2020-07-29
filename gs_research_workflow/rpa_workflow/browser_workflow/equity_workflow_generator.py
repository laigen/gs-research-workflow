# -*- coding: UTF-8 -*-

"""
生成 股票相关的 workflow 的内容
"""
import pickle
from enum import Enum
from typing import Optional, Dict, List, Callable
import logging

from gs_framework.utilities import md5_str

from gs_research_workflow.common.serialization_utilities import cls_to_str
from gs_research_workflow.rpa_workflow.actions.action_doc_in_mongo import RPABatchAction, ActionStatusFlag

from gs_research_workflow.rpa_workflow.browser_workflow.equity_sentiment_workflow import add_equity_sentiment_actions
from gs_research_workflow.rpa_workflow.result_extraction.utilities import upsert_document

from gs_research_workflow.nlp.data.general_browser_workflow_docs import TriggeredWebPagesCrawlWorkflow, \
    PredefinedWorkflow, WorkflowSubmitType, WorkflowStatusFlag, EntityType
from mongoengine import Q

from gs_research_workflow.common.datetime_utilities import local_now
from gs_research_workflow.common.mongo_resource import mongo_db_conn, used_db_position, db_nlp

from gs_research_workflow.nlp.data.docs_in_mongo import FinancialInstrumentSymbol
from gs_research_workflow.rpa_workflow.act_msg_data import WorkflowRequest
from datetime import datetime

logger = logging.getLogger(__name__)


class GSPredefinedWorkflow(Enum):
    EquityNewsAndSentiment = "equity_news_and_sentiment"

# region workflow name to actions generator functions


TPActionGeneratorCallable = Callable[[FinancialInstrumentSymbol, str], List[str]]

WORKFLOW_NAME_TO_ACTION_GENERATORS: Dict[str, List[TPActionGeneratorCallable]] = {
    GSPredefinedWorkflow.EquityNewsAndSentiment.value: [add_equity_sentiment_actions]
}
""" 预定义的 workflow action 生成函数定义 """

# endregion


def find_equity(symbol_or_name: str) -> Optional[FinancialInstrumentSymbol]:
    """ 使用 symbol or name 在 FinancialInstrumentSymbol 中查询匹配的 symbol
        前提是该 symbol 已经填入过 yahoo 的基本信息内容（前置的环境准备）
    """
    ls_symbol_guess = [f"{symbol_or_name}{suffix}" for suffix in ["", ".SS", ".SZ", ".HK"]]
    raw_query = {"_id": {"$in": ls_symbol_guess}, "$or": [{"chn_name": symbol_or_name}, {"eng_name": symbol_or_name}],
                 "info_from_yahoo": {"$exists": True}}

    symbol_obj = FinancialInstrumentSymbol.objects(
        (Q(symbol__in=ls_symbol_guess) | Q(chn_name=symbol_or_name) | Q(eng_name=symbol_or_name) | Q(
            full_name=symbol_or_name)) & Q(
            info_from_yahoo__exists=True)).first()
    if symbol_obj is not None:
        return symbol_obj
    else:
        return None


def is_same_period(t1: datetime, t2: datetime, pd_freq: str) -> bool:
    import pandas as pd
    return len(pd.period_range(t1 if t1 < t2 else t2, t2 if t1 < t2 else t1, freq=pd_freq)) == 1


def create_equity_workflow(req: WorkflowRequest):
    assert req.workflow_name in GSPredefinedWorkflow._value2member_map_

    equity_entity = find_equity(req.entity_str)
    if equity_entity is None:
        wf_batch_uuid = md5_str(f"{req.request_from_account}-{req.ctime.isoformat()}-{req.entity_str}")
        doc_wf = TriggeredWebPagesCrawlWorkflow(uuid=wf_batch_uuid,
                                                workflow=PredefinedWorkflow(workflow_name=req.workflow_name),
                                                para_begin=req.para_begin,
                                                para_end=req.para_begin,
                                                submit_account=req.request_from_account,
                                                submit_type=WorkflowSubmitType.HotKey.value,
                                                submit_time=req.ctime,
                                                finish_or_error_flag=WorkflowStatusFlag.WithError.value,
                                                error_msg=f"Can't find equity symbol or name by '{req.entity_str}'"
                                                )
        upsert_document(doc_wf, False)
        return

    # 找到了 entity， 生成 workflow 的内容
    wf_batch_uuid = md5_str(
        f"{equity_entity.symbol}-{req.workflow_name}-{req.para_begin}-{req.para_end}-{req.request_from_account}-{req.ctime.isoformat()}")

    # 查询 workflow 预设的更新频率
    # wf_freq = "D"
    wf_freq = "1s"
    workflow_def = PredefinedWorkflow.objects(workflow_name=req.workflow_name).first()
    if workflow_def is not None:
        wf_freq = workflow_def.refresh_freq
    # 找一下该 symbol 的 workflow 最近一次的执行时间(假定 Per Symbol + Per Account)
    latest_workflow_inst = TriggeredWebPagesCrawlWorkflow.objects(fin_instrument=equity_entity.symbol,
                                                                  workflow=req.workflow_name,
                                                                  submit_account=req.request_from_account,
                                                                  finish_or_error_flag__in=[
                                                                      WorkflowStatusFlag.WaitToRun.value,
                                                                      WorkflowStatusFlag.SuccessFinished.value]).order_by(
        "-submit_time").first()
    # 如果在同一个周期的，直接记录一条错误的记录内容
    if latest_workflow_inst is not None and is_same_period(latest_workflow_inst.submit_time, req.ctime, wf_freq):
        logger.error(
            f"Workflow(uuid={latest_workflow_inst.uuid},ctime='{latest_workflow_inst.submit_time}') in the same period is existed.")
        doc_wf = TriggeredWebPagesCrawlWorkflow(uuid=wf_batch_uuid,
                                                main_entity_type=EntityType.Equity.value,
                                                fin_instrument=FinancialInstrumentSymbol(symbol=equity_entity.symbol),
                                                workflow=PredefinedWorkflow(workflow_name=req.workflow_name),
                                                para_begin=req.para_begin,
                                                para_end=req.para_begin,
                                                submit_account=req.request_from_account,
                                                submit_type=WorkflowSubmitType.HotKey.value,
                                                submit_time=req.ctime,
                                                finish_or_error_flag=WorkflowStatusFlag.WithError.value,
                                                error_msg=f"workflow '{req.workflow_name}'({equity_entity.symbol}) is executed at {latest_workflow_inst.submit_time} . No need to rerun now."
                                                )
        upsert_document(doc_wf, False)
        return

    # 创建一个workflow
    doc_wf = TriggeredWebPagesCrawlWorkflow(uuid=wf_batch_uuid,
                                            main_entity_type=EntityType.Equity.value,
                                            fin_instrument=FinancialInstrumentSymbol(symbol=equity_entity.symbol),
                                            workflow=PredefinedWorkflow(workflow_name=req.workflow_name),
                                            para_begin=req.para_begin,
                                            para_end=req.para_begin,
                                            submit_account=req.request_from_account,
                                            submit_type=WorkflowSubmitType.HotKey.value,
                                            submit_time=req.ctime,
                                            finish_or_error_flag=WorkflowStatusFlag.WaitToRun.value
                                            )
    upsert_document(doc_wf, False)

    # 创建 batch action
    doc_batch_action = RPABatchAction(batch_id=wf_batch_uuid,
                                      is_dynamic_batch=True,
                                      from_function=cls_to_str(create_equity_workflow),
                                      ctime=req.ctime,
                                      status=ActionStatusFlag.WaitingForRun.value
                                      )
    upsert_document(doc_batch_action, False)

    # 依次调用 action generator 函数
    # NOTE ： 这里是直接访问 diction ， 以后改为调用函数，就可以支持 register 的功能
    for func in WORKFLOW_NAME_TO_ACTION_GENERATORS.get(req.workflow_name, []):
        func(equity_entity, wf_batch_uuid)
    logger.info(f"Batch action '{wf_batch_uuid}' is created.")


if __name__ == "__main__":
    mongo_db_conn(used_db_position, db_nlp)

    # PDD | BABA , USO ， AMZN ， IWM
    # ctime = datetime(2020, 6, 24, 10, 33, 20, 0)
    ctime = datetime.now()
    req = WorkflowRequest(request_from_account="laigen_gs", request_from_pc_id="laigen_gs.DevPC",
                          entity_str="PDD",
                          workflow_name=GSPredefinedWorkflow.EquityNewsAndSentiment.value, ctime=ctime)
    create_equity_workflow(req)
    # new : C407C42E1B8192E6E32E9016B646A484




# TODO 考虑增加 patents 的搜索
# TODO 除了 YouTube 、Twitter 、Facebook 常见的这些，还有 MetaCafe 、Vimeo 、Dailymotion、LiveLeak 等等这些
# TODO 搜狗指数
