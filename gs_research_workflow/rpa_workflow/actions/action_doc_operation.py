# -*- coding: UTF-8 -*-

"""
提供 action 的  mongo db 的一些操作内容
"""
import pickle
from datetime import datetime
from typing import List, Tuple

from gs_research_workflow.rpa_workflow.result_extraction.utilities import upsert_document

from gs_research_workflow.rpa_workflow.actions.action_doc_in_mongo import RPABatchAction, RPAActionDoc, ActionStatusFlag

from gs_research_workflow.rpa_workflow.act_msg_data import RPAAction


def append_actions_into_dynamic_batch_action(batch_action_uuid: str, extract_parser_func: str,
                                             finished_triggered_func:str,
                                             actions: List[Tuple[RPAAction, str, str]]) -> str:
    """
    actions 的定义： Tuple[action,uuid,description] , uuid 由外部指派，以便于进行映射处理
    """
    for i, (action, uuid, action_description) in enumerate(actions):
        action_doc = RPAActionDoc(act_id=uuid)
        action_doc.act_ctime = datetime.now()
        action_doc.act_description = action_description
        action.description = action_doc.act_description
        action_doc.result_process_function = extract_parser_func
        action_doc.status_flag = ActionStatusFlag.WaitingForRun.value
        action_doc.batch_id = batch_action_uuid
        action_doc.act = pickle.dumps(action, protocol=4)
        action_doc.finished_triggered_function = finished_triggered_func
        upsert_document(action_doc, False)
