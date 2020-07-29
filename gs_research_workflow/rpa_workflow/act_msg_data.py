# -*- coding: UTF-8 -*-

"""
与 RPA workflow 有关的 topic message 的定义
"""
from datetime import datetime
from typing import Union, List, Optional

from dataclasses import dataclass

from gs_framework import StateVariable
from gs_framework import State


import faust
from mongoengine import Document, StringField, BinaryField, DateTimeField

topic_uipath_actions = faust.types.TP("uipath-actions-v001", 1)
topic_uipath_machine = faust.types.TP("uipath-machine-v001", 1)
topic_uipath_account = faust.types.TP("uipath-account-v001", 1)


# region action related

class ActionResultBinary(Document):
    uuid = StringField(primary_key=True)
    action_uuid = StringField()
    bin = BinaryField()
    ctime = DateTimeField()


@dataclass
class AtomAction:
    workflow_name: str
    """对应于 UIPath 中的一个 xaml 文件，需要有目录的数据信息, 
        eg: browser_kw_search_actions/act_batch_google_news_search"""

    para: Optional[Union[List[object], object]]
    """需要传入 workflow 的参数内容"""


@dataclass
class RPAAction:
    creator_cls: str = None
    """Action 创建者的 Class 定义"""

    creator_uuid: str = None
    """创建者 env 的 uuid"""

    action_executor_required_tags: List[str] = None
    """ 执行 action 的 executor 环境必须要有的 Tag 内容， 格式为： TagCategory:TagValue
        如果指定了多项 tag 内容，则必须都满足才允许执行该 action
    
    eg: 'feature:google_news_search'  支持 google news search 的功能
        'g_account:laigen.soso@gmail.com' laigen 的 google 账号
        
        'feature:twitter_search'  支持 twitter search 的功能
        'twitter_account:laigen3'  laigen3 的 twitter 账号
    """

    ctime: datetime = None
    """Action 的创建时间"""

    description: str = None
    """便于 debug 的 action  的描述信息 """

    action: List[AtomAction] = None
    """具体的 action 内容"""

    result_save_mongo: bool = True
    """ 生成者可以决定，action 是否要保存到 mongo 中 ， 缺省始终是需要保存到 Mongo 中的
    Added by laigen , 2020.06.04
    """

    no_output: bool = False
    """没有输出内容，Added by laigen , 2020.06.05"""


@dataclass
class RPAActionOrigResult:
    """uipath 执行完 action """
    creator_uuid: str
    """ 为了不需要将所有的内容都先存放在 localstorage , 这里将 creator_uuid 的信息重复一次 """

    success_flag: bool
    """RPA是否"""

    terminal_id: Optional[str] = None
    """执行该 action 的终端 id"""

    rlt_data: Optional[bytes] = None
    # ALERT: kafka 不推荐传递超过 1MB 的 message ， 所以超过 1M 只能通过 mongo 来传递 binary 的数据
    # binary 的数据依然保留，在几种情况下会用到
    #   1) action 的生成者明确知道结果内容不大，并且 desktop 不在能够访问到 Mongo 的环境中
    # 结果内容，是放入 Mongo 还是直接放在 msg 中，有 action instance 的生成者确定

    rlt_bin_data_uuid: Optional[str] = None
    """在 通过 mongo 传递 binary 的数据内容"""

    err_msg: Optional[str] = None
    """如果执行出错，这里保留出错的信息内容"""


@dataclass
class RPAActionOrigResultProcessInfo:
    """ 处理 action 结果的环境 """
    processor_cls: str
    """处理 action 结果进程的类定义"""

    finished_ts: Optional[datetime]
    """处理完成的时间点"""


class WinRPAAction(State):
    """一项在 uipath(win-side) 中执行的 action 内容 """
    action_uuid = StateVariable(dtype=str, default_val=None, help="uuid for an action")
    action = StateVariable(dtype=RPAAction, default_val=None, help="action to run by uipath")
    action_orig_result = StateVariable(dtype=RPAActionOrigResult, default_val=None, help="action result to analyse")
    action_orig_result_process = StateVariable(dtype=RPAActionOrigResultProcessInfo, default_val=None,
                                               help="action result to analyse")

# endregion

# region workflow related


@dataclass
class WorkflowRequest:
    """请求发起一次 workflow """
    request_from_account: str = None
    """ 发起请求的账户 """
    request_from_pc_id: str = None
    """ 请求从哪一台 pc 发起的 """


    entity_str: str = None
    """string 类型的 entity 定义，后续通过查询 Mongo DB 确定 entity 的类型(股票/named_entity/text_paragraph)"""
    workflow_name: str = None
    """需要执行的 workflow name , 有一个 dictionary 将完成 string 2 function 的映射 ， cls_to_str 对象"""

    para_begin: Optional[datetime] = None
    """workflow para begin"""
    para_end: Optional[datetime] = None
    """workflow para end time"""

    ctime:Optional[datetime] = None
    """请求的时间，取发出请求的 local time"""


# endregion
