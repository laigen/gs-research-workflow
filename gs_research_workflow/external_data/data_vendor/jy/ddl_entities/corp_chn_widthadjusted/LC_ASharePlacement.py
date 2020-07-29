# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_ASharePlacement(SQLTableEntity):
    name: str = 'LC_ASharePlacement'
    
    chn_name: str = 'A股配股'
    
    business_unique: str = 'InnerCode,InitialInfoPublDate'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.收录A股历次配股预案及实施进展明细，包括预案有效期、配股价格区间、配股说明书、募集资金和配股交款日等内容。
2.数据范围：1991-03-06至今"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    AdvanceValidStartDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='AdvanceValidStartDate', column_type='datetime', nullable=False, chn_name='预案有效期起始日')
    """预案有效期起始日:"""

    AdvanceValidEndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='AdvanceValidEndDate', column_type='datetime', nullable=False, chn_name='预案有效期截止日')
    """预案有效期截止日:"""

    PlaRatioPlanned: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='PlaRatioPlanned', column_type='decimal(9,4)', nullable=False, chn_name='计划配股比例(10配X)')
    """计划配股比例(10配X):"""

    PlaPriceCeiling: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='PlaPriceCeiling', column_type='decimal(19,4)', nullable=False, chn_name='配股价格上限(最高价)(元)')
    """配股价格上限(最高价)(元):"""

    PlaPriceFloor: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='PlaPriceFloor', column_type='decimal(19,4)', nullable=False, chn_name='配股价格下限(最低价)(元)')
    """配股价格下限(最低价)(元):"""

    DeciPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='DeciPublDate', column_type='datetime', nullable=False, chn_name='决案公布日')
    """决案公布日:"""

    PlaProspectusPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='PlaProspectusPublDate', column_type='datetime', nullable=False, chn_name='配股说明书刊登日期')
    """配股说明书刊登日期:"""

    PlaAbbrName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='PlaAbbrName', column_type='varchar(20)', nullable=False, chn_name='配股简称')
    """配股简称:"""

    PlaCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='PlaCode', column_type='varchar(10)', nullable=False, chn_name='配股代码')
    """配股代码:"""

    BaseShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='BaseShares', column_type='decimal(16,0)', nullable=False, chn_name='配股股本基数(股)')
    """配股股本基数(股):"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='InnerCode', column_type='int', nullable=True, chn_name='证券内部编码')
    """证券内部编码:"""

    PlannedPlaVol: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='PlannedPlaVol', column_type='decimal(16,0)', nullable=False, chn_name='计划配股数量(股)')
    """计划配股数量(股):"""

    ActualPlaRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='ActualPlaRatio', column_type='decimal(9,4)', nullable=False, chn_name='实际配股比例(10配X)')
    """实际配股比例(10配X):"""

    ActualPlaVol: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='ActualPlaVol', column_type='decimal(16,0)', nullable=False, chn_name='实际配股数量(股)')
    """实际配股数量(股):"""

    PlaObject: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='PlaObject', column_type='varchar(255)', nullable=False, chn_name='配股对象')
    """配股对象:"""

    ParValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='ParValue', column_type='decimal(19,4)', nullable=False, chn_name='每股面值(元)')
    """每股面值(元):"""

    PlaPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='PlaPrice', column_type='decimal(19,4)', nullable=False, chn_name='每股配股价格(元)')
    """每股配股价格(元):"""

    TransferPlaRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='TransferPlaRatio', column_type='decimal(9,4)', nullable=False, chn_name='转配比(10转配X)')
    """转配比(10转配X):"""

    TransferPlaVol: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='TransferPlaVol', column_type='decimal(16,0)', nullable=False, chn_name='转配股(股)')
    """转配股(股):"""

    TransferFeePerShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='TransferFeePerShare', column_type='decimal(19,4)', nullable=False, chn_name='每股转配费(元)')
    """每股转配费(元):"""

    OddLotsTreatment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='OddLotsTreatment', column_type='int', nullable=False, chn_name='零股处理方法')
    """零股处理方法:零股处理方法(OddLotsTreatment)与(CT_SystemConst)表中的DM字段关联，令LB = 1218，得到零股处理方法的具体描述：1-不足一股不予配售，2-不足一股四舍五入，3-不足一股累计后随机配售，4-不足一股依据精确算法处理。"""

    InitialInfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='InitialInfoPublDate', column_type='datetime', nullable=True, chn_name='首次信息发布日期')
    """首次信息发布日期:"""

    PlannedPlaProceeds: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='PlannedPlaProceeds', column_type='decimal(19,4)', nullable=False, chn_name='计划募集资金总额(元)')
    """计划募集资金总额(元):"""

    PlaProceeds: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='PlaProceeds', column_type='decimal(19,4)', nullable=False, chn_name='募集资金总额(元)')
    """募集资金总额(元):"""

    PlaCost: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='PlaCost', column_type='decimal(19,4)', nullable=False, chn_name='发行费用总额(元)')
    """发行费用总额(元):"""

    UnderwritingFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='UnderwritingFee', column_type='decimal(19,4)', nullable=False, chn_name='承销费用(元)')
    """承销费用(元):"""

    CPAFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='CPAFee', column_type='decimal(19,4)', nullable=False, chn_name='注册会计师费用(元)')
    """注册会计师费用(元):"""

    AssetAppraisalFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='AssetAppraisalFee', column_type='decimal(19,4)', nullable=False, chn_name='资产评估费用(元)')
    """资产评估费用(元):"""

    LandEvaluationFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='LandEvaluationFee', column_type='decimal(19,4)', nullable=False, chn_name='土地评估费用(元)')
    """土地评估费用(元):"""

    AttorneyFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='AttorneyFee', column_type='decimal(19,4)', nullable=False, chn_name='律师费用(元)')
    """律师费用(元):"""

    TotalAgentFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='TotalAgentFee', column_type='decimal(19,4)', nullable=False, chn_name='中介机构费合计(元)')
    """中介机构费合计(元):"""

    OnlineIssueFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='OnlineIssueFee', column_type='decimal(19,4)', nullable=False, chn_name='上网发行费用(元)')
    """上网发行费用(元):"""

    PlaYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='PlaYear', column_type='datetime', nullable=False, chn_name='配股年度')
    """配股年度:"""

    ScripFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='ScripFee', column_type='decimal(19,4)', nullable=False, chn_name='股票登记费用(元)')
    """股票登记费用(元):"""

    SponsorFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='SponsorFee', column_type='decimal(19,4)', nullable=False, chn_name='上市推荐费用(元)')
    """上市推荐费用(元):"""

    OtherFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='OtherFee', column_type='decimal(19,4)', nullable=False, chn_name='其他费用(元)')
    """其他费用(元):"""

    PlaNetProceeds: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='PlaNetProceeds', column_type='decimal(19,4)', nullable=False, chn_name='募集资金净额(元)')
    """募集资金净额(元):"""

    RightRegDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='RightRegDate', column_type='datetime', nullable=False, chn_name='股权登记日')
    """股权登记日:"""

    ExRightDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='ExRightDate', column_type='datetime', nullable=False, chn_name='除权日')
    """除权日:"""

    PayStartDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='PayStartDate', column_type='datetime', nullable=False, chn_name='配股交款起始日')
    """配股交款起始日:"""

    PayEndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='PayEndDate', column_type='datetime', nullable=False, chn_name='配股交款截止日')
    """配股交款截止日:"""

    DateToAccount: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='DateToAccount', column_type='datetime', nullable=False, chn_name='资金到帐日')
    """资金到帐日:"""

    MoneyToAccount: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='MoneyToAccount', column_type='decimal(19,4)', nullable=False, chn_name='资金到帐金额(元)')
    """资金到帐金额(元):"""

    StockType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='StockType', column_type='int', nullable=False, chn_name='发行股票类型')
    """发行股票类型:发行股票类型(StockType)与(CT_SystemConst)表中的DM字段关联，令LB = 1177 AND DM IN (1,3)，得到发行股票类型的具体描述：1-A股，3-H股。"""

    PlaListDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='PlaListDate', column_type='datetime', nullable=False, chn_name='配股上市日')
    """配股上市日:"""

    LargeSHSubsStatement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='LargeSHSubsStatement', column_type='text', nullable=False, chn_name='大股东认配说明')
    """大股东认配说明:"""

    SchemeChange: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='SchemeChange', column_type='int', nullable=False, chn_name='方案是否变更')
    """方案是否变更:方案是否变更(SchemeChange)与(CT_SystemConst)表中的DM字段关联，令LB = 1194，得到方案是否变更的具体描述：1-否，2-是，3-放弃或股东大会否决，4-可转债改增发，5-可转债改配股，6-增发改配股，7-增发改可转债，8-配股改可转债，9-配股改增发，10-未核准，11-更改发行规模，12-延长有效期，13-其他，14-回..."""

    ChangeStatement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='ChangeStatement', column_type='varchar(255)', nullable=False, chn_name='方案变动说明')
    """方案变动说明:"""

    UnderwritingMode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='UnderwritingMode', column_type='int', nullable=False, chn_name='承销方式')
    """承销方式:承销方式(UnderwritingMode)与(CT_SystemConst)表中的DM字段关联，令LB = 1017，得到承销方式的具体描述：1-全额包销，2-余额包销，3-代销，4-自销，5-限额包销，8-非包销。"""

    UnderwriterBoughtVol: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='UnderwriterBoughtVol', column_type='decimal(16,0)', nullable=False, chn_name='余股包销数量(股)')
    """余股包销数量(股):"""

    PublicSHSubscriptionEsti: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='PublicSHSubscriptionEsti', column_type='decimal(16,0)', nullable=False, chn_name='公众股东预计认配股数(股)')
    """公众股东预计认配股数(股):"""

    PublicSHSubscriptionActu: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='PublicSHSubscriptionActu', column_type='decimal(16,0)', nullable=False, chn_name='公众股东实际认配股数(股)')
    """公众股东实际认配股数(股):"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    AdvanceDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='AdvanceDate', column_type='datetime', nullable=False, chn_name='预案公布日')
    """预案公布日:"""

    SMDeciPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='SMDeciPublDate', column_type='datetime', nullable=False, chn_name='股东大会决议公告日期')
    """股东大会决议公告日期:"""

    PricingModel: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='PricingModel', column_type='int', nullable=False, chn_name='配股价格确定方式')
    """配股价格确定方式:配股价格确定方式(PricingModel)与(CT_SystemConst)表中的DM字段关联，令LB = 1113，得到配股价格确定方式的具体描述：1-设定区间，2-市价折扣。"""

    PricingDescription: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ASharePlacement', column_name='PricingDescription', column_type='varchar(255)', nullable=False, chn_name='配股价格确定方式说明')
    """配股价格确定方式说明:"""

