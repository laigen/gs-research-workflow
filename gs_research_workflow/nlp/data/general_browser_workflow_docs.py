# -*- coding: UTF-8 -*-

"""
定义一组较为通用（即可以通过 cfg file）方式定义的 browser workflow 的内容，这里保存有关该类 workflow 中的 data serialization 的相关内容

序列化的内容需要达到的目标：
1) 能够方便从各个角度去生成 report 。 比如： 按照一个 workflow ， 按照多个 workflow 中的某一个相同的 unit
2) 能够抽取一部分结构化数据，进入到 workflow 的二次迭代。 比如： 读取到高管数据以后，用高管名字 + symbol 进行第二轮的搜索


有关 Mongo Engine 的 documents : https://mongoengine-odm.readthedocs.io/guide/defining-documents.html

"""
from enum import Enum

from gs_research_workflow.rpa_workflow.actions.action_doc_in_mongo import RPAActionDoc, RPABatchAction

from gs_research_workflow.nlp.data.docs_in_mongo import FinancialInstrumentSymbol, GlobalEntity, Article
from mongoengine import Document, StringField, DateTimeField, ListField, EmbeddedDocument, IntField, \
    FloatField, EmbeddedDocumentField, EmbeddedDocumentListField, LazyReferenceField, BooleanField, BinaryField


class PredefinedWorkflow(Document):
    workflow_name = StringField(primary_key=True)
    refresh_freq = StringField()
    """刷新的频度定义"""


class BinaryAttachment(Document):
    """ pdf 或者 png 格式的各种附件内容
        这里只提供 binary 的基于 uuid 的 key-value query
    """

    uuid = StringField(primary_key=True)
    """ 暂定 uuid 为 bin_data 解压后的 MD5 hashcode
        ALERT： gzip 的 binary 文件可能存在有随机性，相同的文件多次压缩得到的 binary 并不完全相同，所以这里的 uuid 是原始 binary 的 md5 hash
    """

    bin_data = BinaryField()
    """文件内容"""

    file_ext = StringField()
    """文件的后缀，通常为 pdf / png 等"""

    ctime = DateTimeField()
    """文件的创建时间"""

    is_gzip = BooleanField()
    """是否经过了 gzip 压缩"""

    bin_length = IntField()
    """binary 的 length"""

    action_uuid = StringField()
    """由哪个 action 获得的"""

    meta = {
        "indexes": [
            "#action_uuid",
        ]
    }


class EntityType(Enum):
    Equity = 1
    """ reffer from FinancialInstrumentSymbol """
    NamedEntity = 2
    """  reffer from GlobalEntity """
    Paragraph = 3
    """for a paragraph text"""


class WorkflowSubmitType(Enum):
    HotKey = 1
    ScheduleTask = 2


class WorkflowStatusFlag(Enum):
    WaitToRun = 0
    SuccessFinished = 1
    WithError = 2


class TriggeredWebPagesCrawlWorkflow(Document):
    """ Trigger 的一次抓取数据的 workflow 的内容
    eg : 在 2020/06/21 时， laigen 触发了一次获取  AAPL 的相关舆情数据的一次 workflow  (一个 document )
         在 2020/06/22 时，laigen 又触发了一次获取 AAPL  的相关舆情数据的 workflow （另一个 document）
     """
    uuid = StringField(primary_key=True)
    """ uuid 由 HASH[ ( fin_instrument | named_entity | txt_paragraph ) + workflow_name + (para_begin|para_end) + submit_account + ctime ] 构成  """

    main_entity_type = IntField()
    """value is EntityType"""

    fin_instrument = LazyReferenceField(FinancialInstrumentSymbol, default=None)
    """ 适用于 main_entity_type == EntityType.Equity 的情况 """
    named_entity = LazyReferenceField(GlobalEntity, default=None)
    """ 适用于 main_entity_type == EntityType.NamedEntity 的情况"""

    txt_paragraph = StringField()
    """ 适用于  main_entity_type == EntityType.Paragraph 的情况"""

    workflow = LazyReferenceField(PredefinedWorkflow, default=None)
    """ 执行哪一项预定义的 workflow 内容 """

    para_begin = DateTimeField()
    para_end = DateTimeField()

    # ---- 以下是一些与  workflow 溯源相关的信息 ----
    submit_account = StringField()
    """由哪个账号提交的workflow"""
    submit_type = IntField()
    """提交方式， see WorkflowSubmitType """
    submit_time = DateTimeField()
    """提交任务的时间"""

    # ---- some result -------
    finish_or_error_flag = IntField()
    """ see : WorkflowStatusFlag """
    error_msg = StringField()

    # ---- relate batch action ---------
    action_batch = LazyReferenceField(RPABatchAction, default=None)


class GeneralBrowserActionInstance(Document):
    """ 一个通用的 action inst 结果保存，这里与 action instance 是一对一的关系 """
    # 这里包含了 action instance 的信息，以及 action instance result 的内容

    uuid = StringField(primary_key=True)
    """ UUID 这里直接使用  action instance 的 uuid  """

    from_workflow = LazyReferenceField(TriggeredWebPagesCrawlWorkflow, default=None)
    """ 有哪个workflow 所创建的内容 """

    # ---- action inst 所具体描述的 entity 情况 ------
    main_entity_type = IntField()
    """value is EntityType"""

    fin_instrument = LazyReferenceField(FinancialInstrumentSymbol, default=None)
    """ 适用于 main_entity_type == EntityType.Equity 的情况 """
    named_entity = LazyReferenceField(GlobalEntity, default=None)
    """ 适用于 main_entity_type == EntityType.NamedEntity 的情况"""

    txt_paragraph = StringField()
    """ 适用于  main_entity_type == EntityType.Paragraph 的情况"""

    # ----- action inst 的定义 -------------
    action_gen_func = StringField()
    """"生成 action 的 function """
    ctime = DateTimeField()
    """创建时间"""

    # ----- 这里是 general_web_app_backend 的一些入参 , GWA = General Web App
    gwa_cfg_name = StringField()
    gwa_kw = StringField()
    gwa_additional_kw = StringField()
    gwa_begin = DateTimeField()
    gwa_end = DateTimeField()

    # ----- action 的一些描述信息，用于出 report 时，提供一些分组或者给人消费的信息
    action_category = StringField()
    """ Action 的类别分组，比如： positioning / sentiment 等 """
    action_sub_category = StringField()
    """ 比如：new institution / raise rating 等"""
    action_description = StringField()
    """ 比如： 评级进行了调升，之前与之后发生了什么。  股价掉了30%，之前与之后发生了什么? """

    # ----- 这里是一些执行情况的信息 ---------
    no_data_flag = BooleanField()
    """是否检测到没有数据的标记"""
    no_new_data_flag = BooleanField()
    """是否检测到没有新数据的标记"""

    related_articles = ListField(LazyReferenceField(Article), default=None)
    """ action instance 关联的 articles ， 所有 article """
    new_found_articles = ListField(LazyReferenceField(Article), default=None)
    """ 新发现的文章内容列表 """

    img_page_snapshot = LazyReferenceField(BinaryAttachment, default=None)
    pdf_page_snapshot = LazyReferenceField(BinaryAttachment, default=None)

    meta = {
        "indexes": [
            "#main_entity_type",
            "#fin_instrument",
            "#named_entity",
            "#gwa_kw",
            "#gwa_additional_kw",
            "-ctime",
            "-gwa_begin",
            "-gwa_end"
        ]
    }
