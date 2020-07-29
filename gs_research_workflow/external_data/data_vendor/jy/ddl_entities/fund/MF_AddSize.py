# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_AddSize(SQLTableEntity):
    name: str = 'MF_AddSize'
    
    chn_name: str = '公募基金扩募'
    
    business_unique: str = '2005年以后无数据更新，已经不存在基金扩募的操作，故表单退役。'
    
    refresh_freq: str = """停止更新"""
    
    comment: str = """1.本表记录封闭式基金扩募信息，都是比较早期的历史数据，现阶段基本上不会有新的数据产生。
2.历史数据：1999年11月起-2005年。
3.信息来源：基金公司官网披露的相关临时公告。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    AddShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='AddShares', column_type='decimal(18,0)', nullable=False, chn_name='扩募份额(份)')
    """扩募份额(份):"""

    UnitIsuueFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='UnitIsuueFee', column_type='decimal(19,4)', nullable=False, chn_name='单位发行费用(元)')
    """单位发行费用(元):"""

    InitiatorQuota: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='InitiatorQuota', column_type='decimal(18,0)', nullable=False, chn_name='发起人配售数量(份)')
    """发起人配售数量(份):"""

    PublicQuota: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='PublicQuota', column_type='decimal(18,0)', nullable=False, chn_name='公众持有人可配售数量(份)')
    """公众持有人可配售数量(份):"""

    PublicQuotaRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='PublicQuotaRatio', column_type='decimal(18,4)', nullable=False, chn_name='公众持有人配售比例(10配X)')
    """公众持有人配售比例(10配X):"""

    RegisterDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='RegisterDate', column_type='datetime', nullable=False, chn_name='权益登记日')
    """权益登记日:"""

    ExRightDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='ExRightDate', column_type='datetime', nullable=False, chn_name='除权基准日')
    """除权基准日:"""

    AbbrNameForApplying: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='AbbrNameForApplying', column_type='varchar(20)', nullable=False, chn_name='认购简称')
    """认购简称:"""

    ApplyingCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='ApplyingCode', column_type='varchar(20)', nullable=False, chn_name='认购代码')
    """认购代码:"""

    PayStartDateForPublic: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='PayStartDateForPublic', column_type='datetime', nullable=False, chn_name='公众持有人配售缴款起始日')
    """公众持有人配售缴款起始日:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='InnerCode', column_type='int', nullable=True, chn_name='基金内部编码')
    """基金内部编码:基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    PayEndDateForPublic: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='PayEndDateForPublic', column_type='datetime', nullable=False, chn_name='公众持有人配售缴款截止日')
    """公众持有人配售缴款截止日:"""

    PayDateForInitiator: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='PayDateForInitiator', column_type='datetime', nullable=False, chn_name='发起人配售缴款日')
    """发起人配售缴款日:"""

    PayDateForBuyRest: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='PayDateForBuyRest', column_type='datetime', nullable=False, chn_name='发起人认购剩余部分缴款日')
    """发起人认购剩余部分缴款日:"""

    PayStartDateForFI: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='PayStartDateForFI', column_type='datetime', nullable=False, chn_name='保险公司等机构认购缴款起始日')
    """保险公司等机构认购缴款起始日:"""

    PayEndDateForFI: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='PayEndDateForFI', column_type='datetime', nullable=False, chn_name='保险公司等机构认购缴款截止日')
    """保险公司等机构认购缴款截止日:"""

    ListedDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='ListedDate', column_type='datetime', nullable=False, chn_name='扩募可流通部分上市日期')
    """扩募可流通部分上市日期:"""

    OutstandingShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='OutstandingShares', column_type='decimal(18,0)', nullable=False, chn_name='本次可流通份额(份)')
    """本次可流通份额(份):"""

    PublicActualBuyShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='PublicActualBuyShares', column_type='decimal(18,0)', nullable=False, chn_name='公众持有人实际认购份额(份)')
    """公众持有人实际认购份额(份):"""

    FIActualBuyShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='FIActualBuyShares', column_type='decimal(18,0)', nullable=False, chn_name='保险公司等机构认购份额(份)')
    """保险公司等机构认购份额(份):"""

    InitiatorHoldFloatShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='InitiatorHoldFloatShares', column_type='decimal(18,0)', nullable=False, chn_name='发起人持有可流通份额数量(份)')
    """发起人持有可流通份额数量(份):"""

    InitialInfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='InitialInfoPublDate', column_type='datetime', nullable=False, chn_name='首次信息发布日期')
    """首次信息发布日期:"""

    InitiatorHoldTerm: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='InitiatorHoldTerm', column_type='decimal(18,4)', nullable=False, chn_name='发起人可流通份额最低持有期限(月)')
    """发起人可流通份额最低持有期限(月):"""

    MiniInitiatorHoldingRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='MiniInitiatorHoldingRatio', column_type='decimal(18,6)', nullable=False, chn_name='存续期发起人最低持有份额比例')
    """存续期发起人最低持有份额比例:"""

    SharesAfterAdded: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='SharesAfterAdded', column_type='decimal(18,0)', nullable=False, chn_name='扩募后基金规模(份)')
    """扩募后基金规模(份):"""

    DurationExtended: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='DurationExtended', column_type='int', nullable=False, chn_name='扩募后基金延长年限(年)')
    """扩募后基金延长年限(年):"""

    DurationAfterAdded: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='DurationAfterAdded', column_type='int', nullable=False, chn_name='扩募后基金存续年限(年)')
    """扩募后基金存续年限(年):"""

    StartDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='StartDate', column_type='datetime', nullable=False, chn_name='存续期开始日')
    """存续期开始日:"""

    ExpireDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='ExpireDate', column_type='datetime', nullable=False, chn_name='存续期截止日')
    """存续期截止日:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新日期')
    """更新日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    ProspectusIssueDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='ProspectusIssueDate', column_type='datetime', nullable=False, chn_name='扩募说明书发布日期')
    """扩募说明书发布日期:"""

    FundRaisingMethod: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='FundRaisingMethod', column_type='int', nullable=False, chn_name='扩募方式')
    """扩募方式:"""

    IssueObject: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='IssueObject', column_type='varchar(250)', nullable=False, chn_name='扩募对象')
    """扩募对象:"""

    ParValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='ParValue', column_type='decimal(19,4)', nullable=False, chn_name='基金单位面值(元)')
    """基金单位面值(元):"""

    UnitPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='UnitPrice', column_type='decimal(19,4)', nullable=False, chn_name='基金单位配售价格(元)')
    """基金单位配售价格(元):"""

    InitiatorQuotaPriceNotes: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AddSize', column_name='InitiatorQuotaPriceNotes', column_type='varchar(250)', nullable=False, chn_name='基金发起人配售价格说明')
    """基金发起人配售价格说明:"""

