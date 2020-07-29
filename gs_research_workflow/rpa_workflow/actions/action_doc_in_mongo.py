# -*- coding: UTF-8 -*-

"""
在 Mongo 中有关 Action 的定义

有关 Mongo Engine 的 documents : https://mongoengine-odm.readthedocs.io/guide/defining-documents.html
"""
from mongoengine import Document, StringField, DateTimeField, BinaryField, IntField, ListField, ReferenceField, CASCADE, \
    LazyReferenceField, BooleanField
from enum import Enum


class ActionStatusFlag(Enum):
    WaitingForRun = 1
    """等待分配队列"""

    Running = 2
    """已分配（发送），等待应答"""

    RunningTimeout = 3
    """超时未返回"""
    Finished = 4
    """已完成"""


class RPAActionDoc(Document):
    # ----- 这部分是 action 的基本信息 --------
    act_id = StringField(primary_key=True)
    """action id"""

    creator_uuid = StringField()
    """创建者的 pk uuid"""

    act_ctime = DateTimeField()
    act_description = StringField()
    act = BinaryField()
    """act参数的 pickle 的 binary """

    result_process_function = StringField()
    """ action 结果的解析函数， 
        function 的 signature 为 ： (rlt_path: str, batch_action_uuid: str, action_uuid: str, save_doc: bool = True)
    """

    finished_triggered_function = StringField()
    """ action 在 完成以后， Process 完成之后， 需要调用的 function , signature 为 (batch_action_uuid:str , action_uuid:str) 
        具体的相关数据内容，需要到 mongo 中自行查询，一般用来做 NLP 或者 生成新的关联的 action 内容
    """

    # ---- 这部分是 action 的 runtime 信息 -----
    status_flag = IntField()
    """ 状态标记： see ActionStatusFlag"""

    add_to_exec_queue_t = DateTimeField()
    """ 加到 execute queue 的时间点 """

    target_pc_id = StringField()
    """ 指派到终端 machine 的 id 编号 """

    response_t = DateTimeField()
    """ 完成后应答的时间点 """

    batch_id = StringField()
    """ batch的 gid 内容 """

    idx_in_batch = IntField()
    """ 在 batch 内的序号 """

    meta = {
        "indexes": [
            "#creator_uuid",
            "#status_flag",
            "#batch_id",
            "act_ctime",
            "add_to_exec_queue_t",
        ]
    }


class RPABatchAction(Document):
    batch_id = StringField(primary_key=True)

    is_dynamic_batch = BooleanField()
    """ 允许是一个 dynamic batch , 即 关联的 action 是可以动态增加的 """

    from_function = StringField()

    function_paras = BinaryField()
    """ function 参数的 parameters 的 dictionary 的 pickle """

    extract_parser_func = StringField()
    """parse用到的 function 类
        一般不再填入，改为每个 Action 自己设定相关的 extract count 
    """

    real_actions = ListField(LazyReferenceField(RPAActionDoc, reverse_delete_rule=CASCADE), default=None)
    """
        NOTE: 允许不再填入该数据，因为考虑到有些 batch 是动态增加的
    """

    real_action_count = IntField()
    """
        NOTE: 允许不再填入该数据，因为考虑到有些 batch 是动态增加的
    """

    finished_action_count = IntField()
    """
        NOTE: 这里可能不再查询了，因为有多少 action 可能是动态增加的
    """

    ctime = DateTimeField()

    status = IntField()
    """ see ActionStatusFlag
        NOTE : 这个 status 可能不再准确，因为 batch action 下有多少 action 可能是动态增加的
    """

    meta = {
        "indexes": [
            "#from_function",
            "#extract_parser_func",
            "#status",
            "ctime",
        ]
    }


# RPABatchAction.register_delete_rule(RPABatchAction, "real_actions", CASCADE)
