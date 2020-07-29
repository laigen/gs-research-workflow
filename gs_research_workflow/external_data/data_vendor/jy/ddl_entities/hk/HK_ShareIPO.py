# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_ShareIPO(SQLTableEntity):
    name: str = 'HK_ShareIPO'
    
    chn_name: str = '港股发行与上市'
    
    business_unique: str = 'InnerCode,InitialInfoPublDate,IssueType'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.记录港股的进程、发行方式、通用属性以及其他发行情况，包含主要字段有：事件进程、发行类别、发行方式、发行对象、定价日、发行基准、实际发行数量等信息内容。
2.数据范围：1994年至今。
3.数据来源：港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    AbortPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='AbortPublDate', column_type='datetime', nullable=False, chn_name='终止实施公告日')
    """终止实施公告日:"""

    RelativeAllotment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='RelativeAllotment', column_type='decimal(18,2)', nullable=False, chn_name='关联人士配售股数(股)')
    """关联人士配售股数(股):"""

    MidPricePShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='MidPricePShare', column_type='decimal(18,2)', nullable=False, chn_name='每股中位价(元)')
    """每股中位价(元):"""

    TotalSubShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='TotalSubShares', column_type='decimal(18,2)', nullable=False, chn_name='实际认购股数(股)')
    """实际认购股数(股):"""

    TotalNumSubCeiling: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='TotalNumSubCeiling', column_type='decimal(18,2)', nullable=False, chn_name='认购总股数上限(股)')
    """认购总股数上限(股):"""

    TotalNumSubMedian: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='TotalNumSubMedian', column_type='decimal(18,2)', nullable=False, chn_name='认购总股数中位数(股)')
    """认购总股数中位数(股):"""

    TotalNumSubFloor: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='TotalNumSubFloor', column_type='decimal(18,2)', nullable=False, chn_name='认购总股数下限(股)')
    """认购总股数下限(股):"""

    GlobalSalesRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='GlobalSalesRatio', column_type='decimal(18,8)', nullable=False, chn_name='占全球发售比例(%)')
    """占全球发售比例(%):"""

    IssuedCapitalRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='IssuedCapitalRatio', column_type='decimal(18,8)', nullable=False, chn_name='占已发行股本比例(%)')
    """占已发行股本比例(%):"""

    Stetement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='Stetement', column_type='varchar(500)', nullable=False, chn_name='备注')
    """备注:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='修改日期')
    """修改日期:"""

    IssueType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='IssueType', column_type='int', nullable=False, chn_name='发行类别')
    """发行类别:发行类别(IssueType)与(CT_SystemConst)表中的DM字段关联，令LB = 1329，得到发行类别的具体描述：1-首发，3-增发，9-股东转让配售，10-基金营销。"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    IssueMethod: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='IssueMethod', column_type='int', nullable=False, chn_name='发行方式')
    """发行方式:"""

    IssueObject: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='IssueObject', column_type='int', nullable=False, chn_name='发行对象')
    """发行对象:发行对象(IssueObject)与(CT_SystemConst)表中的DM字段关联，令LB = 1331，得到发行对象的具体描述：10-全球，13-香港，21-公司股东，31-独立第三者。"""

    CurrencyUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='CurrencyUnit', column_type='int', nullable=False, chn_name='面值单位')
    """面值单位:面值单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068，得到面值单位的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，1170-约旦第纳尔，1180-科..."""

    ParValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='ParValue', column_type='decimal(19,10)', nullable=False, chn_name='每股面值(元)')
    """每股面值(元):"""

    TradeUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='TradeUnit', column_type='int', nullable=False, chn_name='买卖单位(股/手)')
    """买卖单位(股/手):"""

    IssuePriceCurrencyUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='IssuePriceCurrencyUnit', column_type='int', nullable=False, chn_name='发行价单位')
    """发行价单位:发行价单位(IssuePriceCurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068，得到发行价单位的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，1170-..."""

    UnderwritingMode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='UnderwritingMode', column_type='int', nullable=False, chn_name='承销方式')
    """承销方式:承销方式(UnderwritingMode)与(CT_SystemConst)表中的DM字段关联，令LB = 1017，得到承销方式的具体描述：1-全额包销，2-余额包销，3-代销，4-自销，5-限额包销，8-非包销。"""

    RationModel: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='RationModel', column_type='int', nullable=False, chn_name='定量方式')
    """定量方式:定量方式(RationModel)与(CT_SystemConst)表中的DM字段关联，令LB = 1020，得到定量方式的具体描述：1-发行额度，2-设定上限，3-设定下限，4-设定区间。"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='InnerCode', column_type='int', nullable=True, chn_name='内部代码')
    """内部代码:内部代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。"""

    IssueVolPlanned: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='IssueVolPlanned', column_type='decimal(18,2)', nullable=False, chn_name='1)计划发行总股数(股)')
    """1)计划发行总股数(股):"""

    NewShareVolPlanned: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='NewShareVolPlanned', column_type='decimal(18,2)', nullable=False, chn_name='nan')
    """nan:"""

    StoreShareVolPlanned: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='StoreShareVolPlanned', column_type='decimal(18,2)', nullable=False, chn_name='nan')
    """nan:"""

    QualifiedSHAllotmentPlanned: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='QualifiedSHAllotmentPlanned', column_type='decimal(18,2)', nullable=False, chn_name='-##合资格股东优先配售股数(股)')
    """-##合资格股东优先配售股数(股):"""

    PublicNewSharePlanned: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='PublicNewSharePlanned', column_type='decimal(18,2)', nullable=False, chn_name='公开发售新股股数(股)')
    """公开发售新股股数(股):"""

    PublicStoreSharePlanned: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='PublicStoreSharePlanned', column_type='decimal(18,2)', nullable=False, chn_name='公开发售存量股数(股)')
    """公开发售存量股数(股):"""

    StaffPriorAllotmentPlanned: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='StaffPriorAllotmentPlanned', column_type='decimal(18,2)', nullable=False, chn_name='-##全职职员优先发售股数(股)')
    """-##全职职员优先发售股数(股):"""

    OverAllotmentOptionPlanned: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='OverAllotmentOptionPlanned', column_type='decimal(18,2)', nullable=False, chn_name='预计超额配售权股数(股)')
    """预计超额配售权股数(股):"""

    IssuePriceCeiling: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='IssuePriceCeiling', column_type='decimal(18,8)', nullable=False, chn_name='每股最低价(元)')
    """每股最低价(元):"""

    IssuePriceFloor: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='IssuePriceFloor', column_type='decimal(18,8)', nullable=False, chn_name='每股最高价(元)')
    """每股最高价(元):"""

    InitialInfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='InitialInfoPublDate', column_type='datetime', nullable=False, chn_name='首次信息发布日期')
    """首次信息发布日期:"""

    TradeUnitPriceAtCeiling: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='TradeUnitPriceAtCeiling', column_type='decimal(19,4)', nullable=False, chn_name='按最高价每手支付价格(元)')
    """按最高价每手支付价格(元):"""

    ReferrencePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='ReferrencePrice', column_type='int', nullable=False, chn_name='预期参考价位')
    """预期参考价位:预期参考价位(ReferrencePrice)与(CT_SystemConst)表中的DM字段关联，令LB = 1332，得到预期参考价位的具体描述：1-最高价，3-中位数，5-最低价，9-厘定价。"""

    ProceedsPlanned: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='ProceedsPlanned', column_type='decimal(19,4)', nullable=False, chn_name='预计募资总额(元)')
    """预计募资总额(元):"""

    NetProceedsPlanned: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='NetProceedsPlanned', column_type='decimal(19,4)', nullable=False, chn_name='预计所得款净额(元)')
    """预计所得款净额(元):"""

    OverAllotmentProceedsPlanned: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='OverAllotmentProceedsPlanned', column_type='decimal(19,4)', nullable=False, chn_name='预计超额配售所得款净额(元)')
    """预计超额配售所得款净额(元):"""

    IssueCostPlanned: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='IssueCostPlanned', column_type='decimal(19,4)', nullable=False, chn_name='预计发行总费用(元)')
    """预计发行总费用(元):"""

    CommisionRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='CommisionRatio', column_type='decimal(18,8)', nullable=False, chn_name='佣金比例')
    """佣金比例:"""

    ApplyStartDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='ApplyStartDate', column_type='datetime', nullable=False, chn_name='申购起始日')
    """申购起始日:"""

    IssueExpireDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='IssueExpireDate', column_type='datetime', nullable=False, chn_name='发行有效期截止日')
    """发行有效期截止日:"""

    LastTradeDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='LastTradeDate', column_type='datetime', nullable=False, chn_name='最后交易日')
    """最后交易日:"""

    Process: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='Process', column_type='int', nullable=False, chn_name='事件进程')
    """事件进程:事件进程(Process)与(CT_SystemConst)表中的DM字段关联，令LB = 1059，得到事件进程的具体描述：1000-意向，1001-预案，1004-决案，1007-否决，1010-申请，1013-批准，1016-未实施终止，1019-实施中，1022-实施完成，1025-解除，1028-到期，1041-续签，1043-部分续签，1051-..."""

    ExDiviDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='ExDiviDate', column_type='datetime', nullable=False, chn_name='除权日')
    """除权日:"""

    RightRegDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='RightRegDate', column_type='datetime', nullable=False, chn_name='股权登记日')
    """股权登记日:"""

    TransferEndFirstDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='TransferEndFirstDate', column_type='datetime', nullable=False, chn_name='截止过户首日')
    """截止过户首日:"""

    TransferEndLastDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='TransferEndLastDate', column_type='datetime', nullable=False, chn_name='截止过户末日')
    """截止过户末日:"""

    PayEndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='PayEndDate', column_type='datetime', nullable=False, chn_name='缴款截止日')
    """缴款截止日:"""

    IssueEndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='IssueEndDate', column_type='datetime', nullable=False, chn_name='发行截止日')
    """发行截止日:发行截止日(IssueEndDate):在有些场景下也称为申购截止日。"""

    PricingDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='PricingDate', column_type='datetime', nullable=False, chn_name='定价日')
    """定价日:"""

    DateToAccount: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='DateToAccount', column_type='datetime', nullable=False, chn_name='股票发放日')
    """股票发放日:"""

    RefundmentOutDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='RefundmentOutDate', column_type='datetime', nullable=False, chn_name='退款寄发日')
    """退款寄发日:"""

    IssueComplishmentDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='IssueComplishmentDate', column_type='datetime', nullable=False, chn_name='发行完成日')
    """发行完成日:"""

    BDDecisionPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='BDDecisionPublDate', column_type='datetime', nullable=False, chn_name='董事会公告日')
    """董事会公告日:"""

    ProposedListDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='ProposedListDate', column_type='datetime', nullable=False, chn_name='预计上市日')
    """预计上市日:"""

    OverAllotmentProposedListDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='OverAllotmentProposedListDate', column_type='datetime', nullable=False, chn_name='超额配售股份预计上市日')
    """超额配售股份预计上市日:"""

    IssueResultPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='IssueResultPublDate', column_type='datetime', nullable=False, chn_name='发行结果公告日')
    """发行结果公告日:"""

    OverAllotmentOptionExpireDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='OverAllotmentOptionExpireDate', column_type='datetime', nullable=False, chn_name='超额配售权行使完成日')
    """超额配售权行使完成日:"""

    OfferRatioX: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='OfferRatioX', column_type='int', nullable=False, chn_name='供股比例(X:Y)-X')
    """供股比例(X:Y)-X:"""

    OfferRatioY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='OfferRatioY', column_type='int', nullable=False, chn_name='供股比例(X:Y)-Y')
    """供股比例(X:Y)-Y:"""

    IssueBase: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='IssueBase', column_type='int', nullable=False, chn_name='发行基准')
    """发行基准:发行基准(IssueBase)与(CT_SystemConst)表中的DM字段关联，令LB = 1333，得到发行基准的具体描述：10-已发行股份，20-拆细后之新股份，23-合并后之新股份，30-公开发售之新股份，31-供股之新股份。"""

    IssueBaseShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='IssueBaseShares', column_type='decimal(18,2)', nullable=False, chn_name='发行基准股数(股)')
    """发行基准股数(股):"""

    IssueVol: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='IssueVol', column_type='decimal(18,2)', nullable=False, chn_name='1)实际发行总股数(股)')
    """1)实际发行总股数(股):"""

    RatioInPriShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='RatioInPriShare', column_type='decimal(18,8)', nullable=False, chn_name='占原来股份比例')
    """占原来股份比例:"""

    BDDecisionSignDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='BDDecisionSignDate', column_type='datetime', nullable=False, chn_name='董事会公告签署日')
    """董事会公告签署日:"""

    RatioInPostShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='RatioInPostShare', column_type='decimal(18,8)', nullable=False, chn_name='占扩大后股份比例')
    """占扩大后股份比例:"""

    NewShareVol: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='NewShareVol', column_type='decimal(18,2)', nullable=False, chn_name='nan')
    """nan:"""

    StoreShareAllotment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='StoreShareAllotment', column_type='decimal(18,2)', nullable=False, chn_name='nan')
    """nan:"""

    QualifiedSHPriorAllotment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='QualifiedSHPriorAllotment', column_type='decimal(18,2)', nullable=False, chn_name='-##合资格股东优先配售股数(股)')
    """-##合资格股东优先配售股数(股):"""

    PublicOfferedNewShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='PublicOfferedNewShare', column_type='decimal(18,2)', nullable=False, chn_name='nan')
    """nan:"""

    PublicOfferedStoreShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='PublicOfferedStoreShare', column_type='decimal(18,2)', nullable=False, chn_name='nan')
    """nan:"""

    StaffPriorAllotment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='StaffPriorAllotment', column_type='decimal(18,2)', nullable=False, chn_name='-##全职职员优先发售股数(股)')
    """-##全职职员优先发售股数(股):"""

    OverAllotmentOption: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='OverAllotmentOption', column_type='decimal(18,2)', nullable=False, chn_name='2)超额配售权股数(股)')
    """2)超额配售权股数(股):"""

    OverAllotmentNewShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='OverAllotmentNewShare', column_type='decimal(18,2)', nullable=False, chn_name='nan')
    """nan:"""

    OverAllotmentStoreShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='OverAllotmentStoreShare', column_type='decimal(18,2)', nullable=False, chn_name='nan')
    """nan:"""

    SMDeciPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='SMDeciPublDate', column_type='datetime', nullable=False, chn_name='股东大会公告日')
    """股东大会公告日:"""

    IssuePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='IssuePrice', column_type='decimal(18,8)', nullable=False, chn_name='每股发行价(元)')
    """每股发行价(元):"""

    TotalProceeds: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='TotalProceeds', column_type='decimal(19,4)', nullable=False, chn_name='募资总额(元)')
    """募资总额(元):"""

    NetProceeds: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='NetProceeds', column_type='decimal(19,4)', nullable=False, chn_name='所得款净额(元)')
    """所得款净额(元):"""

    OverAllotmentProceeds: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='OverAllotmentProceeds', column_type='decimal(19,4)', nullable=False, chn_name='超额配售募资总额(元)')
    """超额配售募资总额(元):"""

    OverAllotmentNetProceeds: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='OverAllotmentNetProceeds', column_type='decimal(19,4)', nullable=False, chn_name='超额配售所得款净额(元)')
    """超额配售所得款净额(元):"""

    PubApplyUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='PubApplyUnit', column_type='decimal(18,2)', nullable=False, chn_name='1)公众股认购有效申请份数(白/黄/电子)')
    """1)公众股认购有效申请份数(白/黄/电子):"""

    PubApplyShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='PubApplyShares', column_type='decimal(18,2)', nullable=False, chn_name='nan')
    """nan:"""

    PubApplyMultiple: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='PubApplyMultiple', column_type='decimal(18,8)', nullable=False, chn_name='nan')
    """nan:"""

    StaffApplyUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='StaffApplyUnit', column_type='decimal(18,2)', nullable=False, chn_name='2)全职职员优先配售有效申请份数(粉红色)')
    """2)全职职员优先配售有效申请份数(粉红色):"""

    StaffApplyShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='StaffApplyShares', column_type='decimal(18,2)', nullable=False, chn_name='nan')
    """nan:"""

    ProspectusPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='ProspectusPublDate', column_type='datetime', nullable=False, chn_name='招股章程发布日')
    """招股章程发布日:"""

    StaffApplyMultiple: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='StaffApplyMultiple', column_type='decimal(18,8)', nullable=False, chn_name='nan')
    """nan:"""

    AllotmentApplyUnits: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='AllotmentApplyUnits', column_type='decimal(18,2)', nullable=False, chn_name='3)配售申请份数')
    """3)配售申请份数:"""

    AllotmentApplyShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='AllotmentApplyShares', column_type='decimal(18,2)', nullable=False, chn_name='nan')
    """nan:"""

    AllotmentApplyMultiple: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='AllotmentApplyMultiple', column_type='decimal(18,8)', nullable=False, chn_name='nan')
    """nan:"""

    QualifiedSHApplyUnits: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='QualifiedSHApplyUnits', column_type='decimal(18,2)', nullable=False, chn_name='#合资格股东优先配售有效申请份数(蓝色)')
    """#合资格股东优先配售有效申请份数(蓝色):"""

    QualifiedSHApplyShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='QualifiedSHApplyShares', column_type='decimal(18,2)', nullable=False, chn_name='nan')
    """nan:"""

    QualifiedSHApplyMultiple: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='QualifiedSHApplyMultiple', column_type='decimal(18,8)', nullable=False, chn_name='nan')
    """nan:"""

    ValidApplyShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='ValidApplyShares', column_type='decimal(18,2)', nullable=False, chn_name='4)有效申请总股数(股)')
    """4)有效申请总股数(股):"""

    ValidApplyAllotmentShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='ValidApplyAllotmentShares', column_type='decimal(18,2)', nullable=False, chn_name='有效申请暂定配额股数(股)')
    """有效申请暂定配额股数(股):"""

    ValidApplyOverAllotmentShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='ValidApplyOverAllotmentShares', column_type='decimal(18,2)', nullable=False, chn_name='有效申请额外发行股数(股)')
    """有效申请额外发行股数(股):"""

    ContractSignDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='ContractSignDate', column_type='datetime', nullable=False, chn_name='协议签署日')
    """协议签署日:"""

    IrrevocableUndertakingShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='IrrevocableUndertakingShares', column_type='decimal(18,2)', nullable=False, chn_name='5)不可撤回承诺股数(股)')
    """5)不可撤回承诺股数(股):"""

    SubscribeRemainShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='SubscribeRemainShares', column_type='decimal(18,2)', nullable=False, chn_name='认购不足股数(股)')
    """认购不足股数(股):"""

    UnderwriterBoughtVol: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='UnderwriterBoughtVol', column_type='decimal(18,2)', nullable=False, chn_name='包销未认购股数(股)')
    """包销未认购股数(股):"""

    UnderwriterNumber: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='UnderwriterNumber', column_type='int', nullable=False, chn_name='承配人总数')
    """承配人总数:"""

    FirstUnderwriterAllotment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='FirstUnderwriterAllotment', column_type='decimal(18,2)', nullable=False, chn_name='最大承配人配售股数(股)')
    """最大承配人配售股数(股):"""

    First5UnderwritersAllotment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='First5UnderwritersAllotment', column_type='decimal(18,2)', nullable=False, chn_name='前5大承配人配售股数(股)')
    """前5大承配人配售股数(股):"""

    First10UnderwritersAllotment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='First10UnderwritersAllotment', column_type='decimal(18,2)', nullable=False, chn_name='前10大承配人配售股数(股)')
    """前10大承配人配售股数(股):"""

    First15UnderwritersAllotment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='First15UnderwritersAllotment', column_type='decimal(18,2)', nullable=False, chn_name='前15大承配人配售股数(股)')
    """前15大承配人配售股数(股):"""

    First20UnderwritersAllotment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='First20UnderwritersAllotment', column_type='decimal(18,2)', nullable=False, chn_name='前20大承配人配售股数(股)')
    """前20大承配人配售股数(股):"""

    First25UnderwritersAllotment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareIPO', column_name='First25UnderwritersAllotment', column_type='decimal(18,2)', nullable=False, chn_name='前25大承配人配售股数(股)')
    """前25大承配人配售股数(股):"""

