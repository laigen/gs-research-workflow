# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_IssueAndListing(SQLTableEntity):
    name: str = 'MF_IssueAndListing'
    
    chn_name: str = '公募基金发行与上市'
    
    business_unique: str = 'InnerCode'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.本表记录基金发行与上市相关信息，包括发行上市的日期、发行状态、发起人认购情况等相关信息。
2.历史数据：1998年3月起-至今。
3.信息来源：基金公司官网披露的产品说明书及相关临时公告。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    IssueStartDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='IssueStartDate', column_type='datetime', nullable=False, chn_name='发行起始日')
    """发行起始日:"""

    IssueEndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='IssueEndDate', column_type='datetime', nullable=False, chn_name='发行截止日')
    """发行截止日:"""

    OrgIssueStartDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='OrgIssueStartDate', column_type='datetime', nullable=False, chn_name='机构发行起始日')
    """机构发行起始日:"""

    OrgIssueEndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='OrgIssueEndDate', column_type='datetime', nullable=False, chn_name='机构发行截止日')
    """机构发行截止日:"""

    IssueState: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='IssueState', column_type='int', nullable=False, chn_name='发行状态')
    """发行状态:发行状态(IssueState)与(CT_SystemConst)表中的DM字段关联，令LB = 1939，得到发行状态的具体描述：1-待募集，2-取消募集，3-募集中，4-募集结束，5-募集成功，6-募集失败。"""

    IssueCancelDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='IssueCancelDate', column_type='datetime', nullable=False, chn_name='取消发行时间')
    """取消发行时间:"""

    CurrencyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='CurrencyCode', column_type='int', nullable=False, chn_name='发行币种')
    """发行币种:发行币种(CurrencyCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1068，得到发行币种的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，1170-约旦第纳尔，1180-科..."""

    CurrencyStyle: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='CurrencyStyle', column_type='int', nullable=False, chn_name='货币样式')
    """货币样式:货币样式(CurrencyStyle)与(CT_SystemConst)表中的DM字段关联，令LB = 1741，得到货币样式的具体描述：1-现汇，2-现钞。"""

    InitialParValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='InitialParValue', column_type='decimal(19,4)', nullable=False, chn_name='基金初始单位面值(元)')
    """基金初始单位面值(元):"""

    ParValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='ParValue', column_type='decimal(19,4)', nullable=False, chn_name='基金单位面值(元)')
    """基金单位面值(元):"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='InnerCode', column_type='int', nullable=True, chn_name='基金内部编码')
    """基金内部编码:基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    UnitIssuePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='UnitIssuePrice', column_type='decimal(19,4)', nullable=False, chn_name='单位基金发行价格(元)')
    """单位基金发行价格(元):"""

    UnitIssueFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='UnitIssueFee', column_type='decimal(19,4)', nullable=False, chn_name='单位基金发行费用(元)')
    """单位基金发行费用(元):"""

    ShareIssued: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='ShareIssued', column_type='decimal(18,4)', nullable=False, chn_name='基金单位发行总份额(份)')
    """基金单位发行总份额(份):"""

    InitiatorSubscribeVolume: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='InitiatorSubscribeVolume', column_type='decimal(18,0)', nullable=False, chn_name='发起人认购份额(份)')
    """发起人认购份额(份):"""

    InitiatorHoldFloatShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='InitiatorHoldFloatShares', column_type='decimal(18,0)', nullable=False, chn_name='发起人持有可流通份额数量(份)')
    """发起人持有可流通份额数量(份):"""

    InitiatorHoldTerm: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='InitiatorHoldTerm', column_type='decimal(18,4)', nullable=False, chn_name='发起人可流通份额持有期限(月)')
    """发起人可流通份额持有期限(月):"""

    MiniInitiatorHoldingRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='MiniInitiatorHoldingRatio', column_type='decimal(18,6)', nullable=False, chn_name='存续期发起人最低持有份额比例')
    """存续期发起人最低持有份额比例:"""

    FInstitutionQuota: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='FInstitutionQuota', column_type='decimal(18,0)', nullable=False, chn_name='保险公司等机构配售份额(份)')
    """保险公司等机构配售份额(份):"""

    PublicOfferShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='PublicOfferShares', column_type='decimal(18,0)', nullable=False, chn_name='上网公开发行份额(份)')
    """上网公开发行份额(份):"""

    GeneralLegalPersonQuota: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='GeneralLegalPersonQuota', column_type='decimal(18,0)', nullable=False, chn_name='一般法人网下配售份额(份)')
    """一般法人网下配售份额(份):"""

    InitialInfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='InitialInfoPublDate', column_type='datetime', nullable=False, chn_name='首次信息发布日期')
    """首次信息发布日期:"""

    AbbrNameForApplying: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='AbbrNameForApplying', column_type='varchar(20)', nullable=False, chn_name='申购简称')
    """申购简称:"""

    ApplyingCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='ApplyingCode', column_type='varchar(10)', nullable=False, chn_name='申购代码')
    """申购代码:"""

    ApplyingUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='ApplyingUnit', column_type='int', nullable=False, chn_name='申购单位(份)')
    """申购单位(份):"""

    MinimumApplying: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='MinimumApplying', column_type='int', nullable=False, chn_name='单一帐户申购下限(份)')
    """单一帐户申购下限(份):"""

    MaximumApplying: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='MaximumApplying', column_type='int', nullable=False, chn_name='单一帐户申购上限(份)')
    """单一帐户申购上限(份):"""

    ApplyingTimes: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='ApplyingTimes', column_type='int', nullable=False, chn_name='单一帐户申购次数')
    """单一帐户申购次数:单一帐户申购次数(ApplyingTimes)与(CT_SystemConst)表中的DM字段关联，令LB = 1191，得到单一帐户申购次数的具体描述：1-一次，2-多次。"""

    ValidlApplyingAccounts: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='ValidlApplyingAccounts', column_type='int', nullable=False, chn_name='发行有效申购总户数(户)')
    """发行有效申购总户数(户):"""

    ValidApplyingVol: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='ValidApplyingVol', column_type='decimal(18,0)', nullable=False, chn_name='发行有效申购总量(份)')
    """发行有效申购总量(份):"""

    OverApplyingMultiples: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='OverApplyingMultiples', column_type='decimal(18,4)', nullable=False, chn_name='发行超额认购倍数(倍)')
    """发行超额认购倍数(倍):"""

    FreezeFunds: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='FreezeFunds', column_type='decimal(18,4)', nullable=False, chn_name='发行冻结资金(元)')
    """发行冻结资金(元):"""

    ProspectusIssuedDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='ProspectusIssuedDate', column_type='datetime', nullable=False, chn_name='招募说明书发布日期')
    """招募说明书发布日期:"""

    HitRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='HitRatio', column_type='decimal(18,9)', nullable=False, chn_name='发行中签率')
    """发行中签率:"""

    ListedDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='ListedDate', column_type='datetime', nullable=False, chn_name='基金上市日期')
    """基金上市日期:"""

    ListedPlace: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='ListedPlace', column_type='int', nullable=False, chn_name='基金上市地点')
    """基金上市地点:基金上市地点(ListedPlace)与(CT_SystemConst)表中的DM字段关联，令LB = 201 AND DM IN (83,90)，得到基金上市地点的具体描述：83-上海证券交易所，90-深圳证券交易所。"""

    OutstandingShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='OutstandingShares', column_type='decimal(18,0)', nullable=False, chn_name='本次可流通份额(份)')
    """本次可流通份额(份):"""

    FirstDayOpenPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='FirstDayOpenPrice', column_type='decimal(18,3)', nullable=False, chn_name='上市首日开盘价(元)')
    """上市首日开盘价(元):"""

    FirstDayColsePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='FirstDayColsePrice', column_type='decimal(18,3)', nullable=False, chn_name='上市首日收盘价(元)')
    """上市首日收盘价(元):"""

    FirstDayTurnoverRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='FirstDayTurnoverRatio', column_type='decimal(18,6)', nullable=False, chn_name='上市首日换手率')
    """上市首日换手率:"""

    EstablishmentDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='EstablishmentDate', column_type='datetime', nullable=False, chn_name='成立日期')
    """成立日期:"""

    ApplyOpeningDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='ApplyOpeningDate', column_type='datetime', nullable=False, chn_name='申购开放起始日')
    """申购开放起始日:"""

    RedeemOpeningDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='RedeemOpeningDate', column_type='datetime', nullable=False, chn_name='赎回开放起始日')
    """赎回开放起始日:"""

    ListAnnouncementIssueDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='ListAnnouncementIssueDate', column_type='datetime', nullable=False, chn_name='上市公告书发布日期')
    """上市公告书发布日期:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新日期')
    """更新日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    FundRaisingMethod: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='FundRaisingMethod', column_type='int', nullable=False, chn_name='募资方式')
    """募资方式:募资方式(FundRaisingMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1211，得到募资方式的具体描述：1-基金发行，2-改制上市，3-封转开，4-基金转型，5-新增份额。"""

    FundType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='FundType', column_type='int', nullable=False, chn_name='发行基金类型')
    """发行基金类型:发行基金类型(FundType)与(CT_SystemConst)表中的DM字段关联，令LB = 1210，得到发行基金类型的具体描述：1-契约型封闭式，2-开放式，3-LOF，4-ETF，5-FOF，6-创新型封闭式，7-开放式(带固定封闭期)，8-ETF联接基金，9-半开放式。"""

    IssueObject: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='IssueObject', column_type='varchar(100)', nullable=False, chn_name='发行对象')
    """发行对象:"""

    IssueWay: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IssueAndListing', column_name='IssueWay', column_type='int', nullable=False, chn_name='发行方式')
    """发行方式:"""

