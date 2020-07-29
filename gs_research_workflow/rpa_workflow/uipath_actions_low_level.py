# -*- coding: UTF-8 -*-

"""
Low Level Action ： Action 的最接近原始(Desktop UIPath 接收的 Action)定义
                    如： twitter search 的 Action

!!! ALERT:
    1) Low Level API 返回的 RPAAction 中，以下部分内容是空缺，留在其他层的 Action 处理填入
        [RPAAction.creator_cls] 应该由上层的调用者填入
        [RPAAction.creator_uuid] 由上层的调用者填入
        [RPAAction.action_executor_required_tags] 中仅填入与软件环境有关的信息，具体指定到哪一台服务器，由 env 的资源控制这决定
        [RPAAction.description] 应该由上层的调用者决定怎么填入这一层的描述信息


有关 Low Level Action 的调度：
    1) 所有待执行的 Low Level Action 先全部入 Mongo 库，进入等待队列
    2) 有一个 Env 专职负责 Low Level Action 的调度执行
        2.1) Env PreDefine 调度队列规则， 假定是 先入先出 , 以后可以考虑 action 的 creator 的等级加权等
        2.2) Env 找到超时未应答的 action , resend or 标记为 fail
        2.3) 收集所有的 Desktop Env 的状态信息，向空闲的 resource push action
    3) 分发处理接收到的 action response , 并调用不同的函数入库

"""
from datetime import datetime
from typing import List, Dict

from dataclasses import dataclass

from gs_research_workflow.rpa_workflow.act_msg_data import RPAAction, AtomAction

EXT_ENV_SEEKING_ALPHA: str = "seeking_alpha"
EXT_ENV_TWITTER: str = "twitter"
EXT_ENV_GOOGLE_NEWS: str = "google_news"
EXT_ENV_AZURE_NLP: str = "azure_nlp"


def seeking_alpha_channels(channels: List[str]) -> RPAAction:
    """获取 Seeking Alpha 的某些专栏内容"""
    # TODO: 检测是否都是合法的 channel
    return RPAAction(action_executor_required_tags=[f"ext_envs:{EXT_ENV_SEEKING_ALPHA}"],
                     action=[AtomAction(workflow_name="browser_kw_search_actions/act_multi_nlp_task",
                                        para={"site": "seeking_alpha",
                                              "function": "special_columns",
                                              "ls_paras": channels})])


def seeking_alpha_authors_info(author_ids: List[str]) -> RPAAction:
    """seeking alpha 的某个 Author 的信息"""
    return RPAAction(action_executor_required_tags=[f"ext_envs:{EXT_ENV_SEEKING_ALPHA}"],
                     action=[AtomAction(workflow_name="browser_kw_search_actions/act_multi_nlp_task",
                                        para={"site": "seeking_alpha",
                                              "function": "author_info",
                                              "ls_paras": author_ids})])


def seeking_alpha_symbols_info(symbols: List[str], pages: int = 1) -> RPAAction:
    """ seeking alpha 的有些 symbol 代码信息"""
    return RPAAction(action_executor_required_tags=[f"ext_envs:{EXT_ENV_SEEKING_ALPHA}"],
                     action=[AtomAction(workflow_name="browser_kw_search_actions/act_multi_nlp_task",
                                        para={"site": "seeking_alpha",
                                              "function": "symbol_summary",
                                              "pages": pages,
                                              "ls_paras": symbols})])


def seeking_alpha_kws_search(keywords: List[str], pg_count: int = 1) -> RPAAction:
    """ seeking alpha 的 keywords Search """
    return RPAAction(action_executor_required_tags=[f"ext_envs:{EXT_ENV_SEEKING_ALPHA}"],
                     action=[AtomAction(workflow_name="browser_kw_search_actions/act_multi_nlp_task",
                                        para={"site": "seeking_alpha",
                                              "function": "kw_search",
                                              "pages": pg_count,
                                              "ls_paras": keywords})])


def twitter_kws_search(keywords: List[str], pg_count: int = 1) -> RPAAction:
    """ twitter 的 keyword search """
    return RPAAction(action_executor_required_tags=[f"ext_envs:{EXT_ENV_TWITTER}"],
                     action=[AtomAction(workflow_name="browser_kw_search_actions/act_multi_nlp_task",
                                        para={"site": "twitter",
                                              "function": "kw_search",
                                              "pages": pg_count,
                                              "ls_paras": keywords})])


def twitter_users_following(user_ids: List[str], pg_count: int = 1) -> RPAAction:
    """ twitter 用户的 following 信息 """
    return RPAAction(action_executor_required_tags=[f"ext_envs:{EXT_ENV_TWITTER}"],
                     action=[AtomAction(workflow_name="browser_kw_search_actions/act_multi_nlp_task",
                                        para={"site": "twitter",
                                              "function": "following",
                                              "pages": pg_count,
                                              "ls_paras": user_ids})])


@dataclass
class AzureTxtAnaPara:
    doc: str
    pk_field: str
    pk_val: str
    txt_field: str
    txt_value: str

    def to_dict(self) -> Dict:
        return {"doc": self.doc, "pk_field": self.pk_field, "pk_val": self.pk_val, "txt_field": self.txt_field,
                "txt_value": self.txt_value}


def azure_txt_analysis(paragraphs: List[AzureTxtAnaPara]) -> RPAAction:
    return RPAAction(action_executor_required_tags=[f"ext_envs:{EXT_ENV_AZURE_NLP}"],
                     ctime=datetime.now(),
                     action=[AtomAction(workflow_name="browser_kw_search_actions/act_multi_nlp_task",
                                        para={"site": "azure",
                                              "function": "txt_ana",
                                              "ls_paras": [x.to_dict() for x in paragraphs]})])


def google_news_kws_search(keywords: List[str], pg_count: int = 1) -> RPAAction:
    """ twitter 的 keyword search """
    return RPAAction(action_executor_required_tags=[f"ext_envs:{EXT_ENV_GOOGLE_NEWS}"],
                     ctime=datetime.now(),
                     action=[AtomAction(workflow_name="browser_kw_search_actions/act_multi_nlp_task",
                                        para={"site": "google_news",
                                              "function": "kw_search",
                                              "pages": pg_count,
                                              "ls_paras": keywords})])


def general_desktop_browser_backend_action(cfg_name: str, kw: str, additional_kw: str = "") -> RPAAction:
    """ 较为通用的 desktop env 的内容 """
    if additional_kw is None:
        additional_kw = ""
    return RPAAction(action_executor_required_tags=[],
                     ctime=datetime.now(),
                     action=[AtomAction(workflow_name="DesktopRPA/act_desktop_action_dispatch",
                                        para={"action": "general_desktop_browser_backend_action",
                                              "cfg_name": cfg_name,
                                              "kw": kw,
                                              "additional_kw": additional_kw
                                              })])
