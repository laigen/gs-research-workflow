# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_AShareSeasonedNewIssue(SQLTableEntity):
    name: str = 'LC_AShareSeasonedNewIssue'
    
    chn_name: str = 'A股增发'
    
    business_unique: str = 'InnerCode,InitialInfoPublDate'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.收录A股增发A股、B股增发A股、H股增发A股等的明细情况，包括历次增发预案、进程日期、预案有效期、发行属性、发行价区间、发行量区间、发行日期、上网发行情况、网下配售申购情况和募集资金与费用等内容。
2.数据范围：1991-08-17至今"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    SASACApprovalPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='SASACApprovalPublDate', column_type='datetime', nullable=False, chn_name='国资委通过公告日')
    """国资委通过公告日:"""

    ListAnnounceDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ListAnnounceDate', column_type='datetime', nullable=False, chn_name='增发新股上市公告日期')
    """增发新股上市公告日期:"""

    NewShareListDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='NewShareListDate', column_type='datetime', nullable=False, chn_name='增发股份上市日期')
    """增发股份上市日期:"""

    OutstandingShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='OutstandingShares', column_type='decimal(16,0)', nullable=False, chn_name='本次上市流通股数(股)')
    """本次上市流通股数(股):"""

    PutBackVol: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='PutBackVol', column_type='decimal(16,0)', nullable=False, chn_name='网上网下回拨股数(股)')
    """网上网下回拨股数(股):"""

    PrefPlaVolHMax: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='PrefPlaVolHMax', column_type='decimal(16,0)', nullable=False, chn_name='原股东可配售股数(最多)(股)')
    """原股东可配售股数(最多)(股):"""

    PrefPlaVolH: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='PrefPlaVolH', column_type='decimal(16,0)', nullable=False, chn_name='原股东优先配售股数(股)')
    """原股东优先配售股数(股):"""

    PrefPlaVolHOnline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='PrefPlaVolHOnline', column_type='decimal(16,0)', nullable=False, chn_name='原股东网上认购优先配售(股)')
    """原股东网上认购优先配售(股):"""

    PrefPlaVolHOffline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='PrefPlaVolHOffline', column_type='decimal(16,0)', nullable=False, chn_name='原股东网下认购优先配售(股)')
    """原股东网下认购优先配售(股):"""

    ValidApplyHNum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ValidApplyHNum', column_type='int', nullable=False, chn_name='原股东有效申购户数(户)')
    """原股东有效申购户数(户):"""

    ValidApplyNumHOnline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ValidApplyNumHOnline', column_type='int', nullable=False, chn_name='原股东网上认购有效申购户数(户)')
    """原股东网上认购有效申购户数(户):"""

    CSRCApprovalPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='CSRCApprovalPublDate', column_type='datetime', nullable=False, chn_name='证监会批准公告日')
    """证监会批准公告日:"""

    ValidApplyNumHOffline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ValidApplyNumHOffline', column_type='int', nullable=False, chn_name='原股东网下认购有效申购户数(户)')
    """原股东网下认购有效申购户数(户):"""

    PublicOfferVolOnline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='PublicOfferVolOnline', column_type='decimal(16,0)', nullable=False, chn_name='上网公开发行股数(股)')
    """上网公开发行股数(股):"""

    ValidApplyVolOnline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ValidApplyVolOnline', column_type='decimal(16,0)', nullable=False, chn_name='上网有效申购总量(股)')
    """上网有效申购总量(股):"""

    ValidApplyNumOnline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ValidApplyNumOnline', column_type='int', nullable=False, chn_name='上网有效申购户数(户)')
    """上网有效申购户数(户):"""

    OverSubsTimesOnline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='OverSubsTimesOnline', column_type='decimal(9,4)', nullable=False, chn_name='上网超额认购倍数(倍)')
    """上网超额认购倍数(倍):"""

    LotRateOnline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='LotRateOnline', column_type='decimal(18,15)', nullable=False, chn_name='上网中签率')
    """上网中签率:"""

    PlaVolLPOffline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='PlaVolLPOffline', column_type='decimal(16,0)', nullable=False, chn_name='法人网下配售股数(股)')
    """法人网下配售股数(股):"""

    ValidApplyVolLPOffline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ValidApplyVolLPOffline', column_type='decimal(16,0)', nullable=False, chn_name='法人网下配售有效申购总量(股)')
    """法人网下配售有效申购总量(股):"""

    ValidApplyNumLPOffline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ValidApplyNumLPOffline', column_type='int', nullable=False, chn_name='法人网下配售有效申购户数(户)')
    """法人网下配售有效申购户数(户):"""

    OverSubsTimesLPOffline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='OverSubsTimesLPOffline', column_type='decimal(9,4)', nullable=False, chn_name='法人网下配售超额认购倍数(倍)')
    """法人网下配售超额认购倍数(倍):"""

    EventProcedureCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='EventProcedureCode', column_type='int', nullable=False, chn_name='事件进程')
    """事件进程:事件进程(EventProcedureCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1640，得到事件进程的具体描述：10-董事会预案，20-股东大会通过，21-国资委通过，22-发审委通过，23-证监会通过，29-实施中，30-实施完成，40-国资委否决，41-股东大会否决，42-证监会否决，43-发审委否决，50-延期实施，..."""

    LotRateLPOffline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='LotRateLPOffline', column_type='decimal(18,15)', nullable=False, chn_name='法人网下配售中签率')
    """法人网下配售中签率:"""

    APlaVolLPOffline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='APlaVolLPOffline', column_type='decimal(16,0)', nullable=False, chn_name='A类法人网下配售股数(股)')
    """A类法人网下配售股数(股):"""

    AValidApplyVolLPOffline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='AValidApplyVolLPOffline', column_type='decimal(16,0)', nullable=False, chn_name='A类法人网下配售有效申购总量(股)')
    """A类法人网下配售有效申购总量(股):"""

    AValidApplyNumLPOffline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='AValidApplyNumLPOffline', column_type='int', nullable=False, chn_name='A类法人网下配售有效申购户数(户)')
    """A类法人网下配售有效申购户数(户):"""

    ALotRateLPOffline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ALotRateLPOffline', column_type='decimal(18,15)', nullable=False, chn_name='A类法人网下配售中签率')
    """A类法人网下配售中签率:"""

    BPlaVolLPOffline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='BPlaVolLPOffline', column_type='decimal(16,0)', nullable=False, chn_name='B类法人网下配售股数(股)')
    """B类法人网下配售股数(股):"""

    BValidApplyVolLPOffline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='BValidApplyVolLPOffline', column_type='decimal(16,0)', nullable=False, chn_name='B类法人网下配售有效申购总量(股)')
    """B类法人网下配售有效申购总量(股):"""

    BValidApplyNumLPOffline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='BValidApplyNumLPOffline', column_type='decimal(16,0)', nullable=False, chn_name='B类法人网下配售有效申购户数(户)')
    """B类法人网下配售有效申购户数(户):"""

    BLotRateLPOffline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='BLotRateLPOffline', column_type='decimal(18,15)', nullable=False, chn_name='B类法人网下配售中签率')
    """B类法人网下配售中签率:"""

    PlaVolHOffline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='PlaVolHOffline', column_type='decimal(16,0)', nullable=False, chn_name='原股东网下配售股数(股)')
    """原股东网下配售股数(股):"""

    AdvanceValidStartDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='AdvanceValidStartDate', column_type='datetime', nullable=False, chn_name='预案有效期起始日')
    """预案有效期起始日:"""

    ValidPlaVolHOffline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ValidPlaVolHOffline', column_type='decimal(16,0)', nullable=False, chn_name='原股东网下配售有效申购总量(股)')
    """原股东网下配售有效申购总量(股):"""

    ValidPlaNumHOffline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ValidPlaNumHOffline', column_type='int', nullable=False, chn_name='原股东网下配售有效申购户数(户)')
    """原股东网下配售有效申购户数(户):"""

    LotRateHOffline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='LotRateHOffline', column_type='decimal(18,15)', nullable=False, chn_name='原股东网下配售中签率')
    """原股东网下配售中签率:"""

    PlaVolF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='PlaVolF', column_type='decimal(16,0)', nullable=False, chn_name='投资基金配售股数(股)')
    """投资基金配售股数(股):"""

    PlaVolSTAQNET: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='PlaVolSTAQNET', column_type='decimal(16,0)', nullable=False, chn_name='STAQ/NET定向配售股数(股)')
    """STAQ/NET定向配售股数(股):"""

    TailoredPlaVolLP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='TailoredPlaVolLP', column_type='decimal(16,0)', nullable=False, chn_name='法人定向配售股数(股)')
    """法人定向配售股数(股):"""

    EarningForecastYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='EarningForecastYear', column_type='datetime', nullable=False, chn_name='盈利预测年度')
    """盈利预测年度:"""

    MainIncomeForecast: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='MainIncomeForecast', column_type='decimal(19,4)', nullable=False, chn_name='主营业务收入预测(元)')
    """主营业务收入预测(元):"""

    NetProfitForecast: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='NetProfitForecast', column_type='decimal(19,4)', nullable=False, chn_name='净利润预测(元)')
    """净利润预测(元):"""

    DilutedEPSForecast: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='DilutedEPSForecast', column_type='decimal(19,4)', nullable=False, chn_name='全面摊薄每股盈利预测(元)')
    """全面摊薄每股盈利预测(元):"""

    AdvanceValidEndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='AdvanceValidEndDate', column_type='datetime', nullable=False, chn_name='预案有效期截止日')
    """预案有效期截止日:"""

    UnderwritingMode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='UnderwritingMode', column_type='int', nullable=False, chn_name='承销方式')
    """承销方式:承销方式(UnderwritingMode)与(CT_SystemConst)表中的DM字段关联，令LB = 1017，得到承销方式的具体描述：1-全额包销，2-余额包销，3-代销，4-自销，5-限额包销，8-非包销。"""

    UnderwriterBoughtVol: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='UnderwriterBoughtVol', column_type='decimal(16,0)', nullable=False, chn_name='余股包销数量(股)')
    """余股包销数量(股):"""

    SchemeChangePublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='SchemeChangePublDate', column_type='datetime', nullable=False, chn_name='方案变动公告日')
    """方案变动公告日:"""

    ChangeStatement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ChangeStatement', column_type='varchar(1000)', nullable=False, chn_name='方案变动说明')
    """方案变动说明:"""

    ChangeType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ChangeType', column_type='int', nullable=False, chn_name='方案变动类型')
    """方案变动类型:方案变动类型(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1194，得到方案变动类型的具体描述：1-否，2-是，3-放弃或股东大会否决，4-可转债改增发，5-可转债改配股，6-增发改配股，7-增发改可转债，8-配股改可转债，9-配股改增发，10-未核准，11-更改发行规模，12-延长有效期，13-其他，14-回拨后..."""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    StockType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='StockType', column_type='int', nullable=False, chn_name='增发A股类型')
    """增发A股类型:增发A股类型(StockType)与(CT_SystemConst)表中的DM字段关联，令LB = 1239 AND DM IN (1,2)，得到增发A股类型的具体描述：1-A股增发A股，2-B股增发A股。"""

    PriceIntervalStatement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='PriceIntervalStatement', column_type='varchar(255)', nullable=False, chn_name='发行价区间确定方式说明')
    """发行价区间确定方式说明:"""

    PricingModel: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='PricingModel', column_type='int', nullable=False, chn_name='发行价定价方式')
    """发行价定价方式:"""

    RationModel: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='RationModel', column_type='int', nullable=False, chn_name='发行量定量方式')
    """发行量定量方式:"""

    IssueMethod: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='IssueMethod', column_type='int', nullable=False, chn_name='发行方式')
    """发行方式:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='InnerCode', column_type='int', nullable=True, chn_name='证券内部编码')
    """证券内部编码:"""

    IssuePurpose: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='IssuePurpose', column_type='varchar(255)', nullable=False, chn_name='增发目的')
    """增发目的:"""

    ISOBTypeCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ISOBTypeCode', column_type='int', nullable=False, chn_name='发行对象类型')
    """发行对象类型:"""

    IssueObject: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='IssueObject', column_type='varchar(255)', nullable=False, chn_name='发行对象')
    """发行对象:"""

    IssuePriceCeiling: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='IssuePriceCeiling', column_type='decimal(19,4)', nullable=False, chn_name='发行价上限(最高价)(元)')
    """发行价上限(最高价)(元):"""

    IssuePriceFloor: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='IssuePriceFloor', column_type='decimal(19,4)', nullable=False, chn_name='发行价下限(最低价)(元)')
    """发行价下限(最低价)(元):"""

    AdjustedIssuePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='AdjustedIssuePrice', column_type='decimal(19,4)', nullable=False, chn_name='最新发行价下限(元)')
    """最新发行价下限(元):"""

    PriceAdjustedDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='PriceAdjustedDate', column_type='datetime', nullable=False, chn_name='最新发行价调整日')
    """最新发行价调整日:"""

    ReferringPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ReferringPrice', column_type='decimal(19,4)', nullable=False, chn_name='承销商指导价格(元)')
    """承销商指导价格(元):"""

    IssueVolCeiling: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='IssueVolCeiling', column_type='decimal(16,0)', nullable=False, chn_name='发行量上限(不超过)(股)')
    """发行量上限(不超过)(股):"""

    IssueVolFloor: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='IssueVolFloor', column_type='decimal(16,0)', nullable=False, chn_name='发行量下限(不少于)(股)')
    """发行量下限(不少于)(股):"""

    InitialInfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='InitialInfoPublDate', column_type='datetime', nullable=False, chn_name='首次信息发布日期')
    """首次信息发布日期:"""

    AdjustedIssueVol: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='AdjustedIssueVol', column_type='decimal(16,0)', nullable=False, chn_name='最新发行量上限(股)')
    """最新发行量上限(股):"""

    PriceVolAdjustedDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='PriceVolAdjustedDate', column_type='datetime', nullable=False, chn_name='最新发行价及发行量调整日')
    """最新发行价及发行量调整日:"""

    OverAllotmentOption: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='OverAllotmentOption', column_type='decimal(16,0)', nullable=False, chn_name='超额配售权(股)')
    """超额配售权(股):"""

    IssueStartDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='IssueStartDate', column_type='datetime', nullable=False, chn_name='发行日期起始日')
    """发行日期起始日:"""

    IssueEndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='IssueEndDate', column_type='datetime', nullable=False, chn_name='发行日期截止日')
    """发行日期截止日:"""

    UnderwritingStartDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='UnderwritingStartDate', column_type='datetime', nullable=False, chn_name='承销期起始日')
    """承销期起始日:"""

    UnderwritingEndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='UnderwritingEndDate', column_type='datetime', nullable=False, chn_name='承销期截止日')
    """承销期截止日:"""

    IfExRightAShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='IfExRightAShare', column_type='int', nullable=False, chn_name='A股除权与否')
    """A股除权与否:A股除权与否（IfExRightAShare）：固定常量：1->是0->否"""

    RightRegDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='RightRegDate', column_type='datetime', nullable=False, chn_name='股权登记日')
    """股权登记日:"""

    ExRightDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ExRightDate', column_type='datetime', nullable=False, chn_name='除权日')
    """除权日:"""

    ProjInfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ProjInfoSource', column_type='varchar(200)', nullable=False, chn_name='预案信息来源')
    """预案信息来源:"""

    SuspendStartDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='SuspendStartDate', column_type='datetime', nullable=False, chn_name='停牌时间起始日')
    """停牌时间起始日:"""

    SuspendEndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='SuspendEndDate', column_type='datetime', nullable=False, chn_name='停牌时间截止日')
    """停牌时间截止日:"""

    PrefPlaDateH: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='PrefPlaDateH', column_type='datetime', nullable=False, chn_name='老股东优先配售日期')
    """老股东优先配售日期:"""

    PrefPlaRatioH: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='PrefPlaRatioH', column_type='decimal(9,4)', nullable=False, chn_name='老股东优先配售比例(10配X)')
    """老股东优先配售比例(10配X):"""

    PrefPlaApplyCodeH: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='PrefPlaApplyCodeH', column_type='varchar(10)', nullable=False, chn_name='老股东优先配售申购代码')
    """老股东优先配售申购代码:"""

    PrefPlaApplyAbbrNameH: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='PrefPlaApplyAbbrNameH', column_type='varchar(20)', nullable=False, chn_name='老股东优先配售申购简称')
    """老股东优先配售申购简称:"""

    IssueDateOnline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='IssueDateOnline', column_type='datetime', nullable=False, chn_name='上网公开发行日期')
    """上网公开发行日期:"""

    ApplyCodeOnline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ApplyCodeOnline', column_type='varchar(10)', nullable=False, chn_name='上网发行申购代码')
    """上网发行申购代码:"""

    ApplyAbbrNameOnline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ApplyAbbrNameOnline', column_type='varchar(20)', nullable=False, chn_name='上网发行申购简称')
    """上网发行申购简称:"""

    ApplyUnitOnline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ApplyUnitOnline', column_type='int', nullable=False, chn_name='上网发行申购单位(股)')
    """上网发行申购单位(股):"""

    IssueResultInfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='IssueResultInfoSource', column_type='varchar(200)', nullable=False, chn_name='发行结果信息来源')
    """发行结果信息来源:"""

    ApplyMaxOnline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ApplyMaxOnline', column_type='decimal(16,0)', nullable=False, chn_name='上网发行申购上限(股)')
    """上网发行申购上限(股):"""

    ApplyStartDateLPOffline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ApplyStartDateLPOffline', column_type='datetime', nullable=False, chn_name='法人网下配售申购日期起始日')
    """法人网下配售申购日期起始日:"""

    ApplyEndDateLPOffline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ApplyEndDateLPOffline', column_type='datetime', nullable=False, chn_name='法人网下配售申购日期截止日')
    """法人网下配售申购日期截止日:"""

    PayStartDateLPOffline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='PayStartDateLPOffline', column_type='datetime', nullable=False, chn_name='法人网下申购缴款开始日')
    """法人网下申购缴款开始日:"""

    PlaPayEndDateLPOffline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='PlaPayEndDateLPOffline', column_type='datetime', nullable=False, chn_name='法人网下申购缴款截止日')
    """法人网下申购缴款截止日:"""

    ApplyUnitLPOffline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ApplyUnitLPOffline', column_type='int', nullable=False, chn_name='法人网下配售认购单位(股)')
    """法人网下配售认购单位(股):"""

    ApplyMinLPOffline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ApplyMinLPOffline', column_type='int', nullable=False, chn_name='法人网下配售申购下限(股)')
    """法人网下配售申购下限(股):"""

    ApplyMaxLPOffline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ApplyMaxLPOffline', column_type='decimal(16,0)', nullable=False, chn_name='法人网下配售申购上限(股)')
    """法人网下配售申购上限(股):"""

    ValidApplyTimesLPOffline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ValidApplyTimesLPOffline', column_type='int', nullable=False, chn_name='法人网下配售有效申购次数限定')
    """法人网下配售有效申购次数限定:法人网下配售有效申购次数限定(ValidApplyTimesLPOffline)与(CT_SystemConst)表中的DM字段关联，令LB = 1195，得到法人网下配售有效申购次数限定的具体描述：1-多次申购，2-一次申购。"""

    ApplyStartDateF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ApplyStartDateF', column_type='datetime', nullable=False, chn_name='基金配售申购日期起始日')
    """基金配售申购日期起始日:"""

    AdvanceDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='AdvanceDate', column_type='datetime', nullable=False, chn_name='预案公布日期')
    """预案公布日期:"""

    ApplyEndDateF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ApplyEndDateF', column_type='datetime', nullable=False, chn_name='基金配售申购日期截止日')
    """基金配售申购日期截止日:"""

    PayStartDateF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='PayStartDateF', column_type='datetime', nullable=False, chn_name='基金配售缴款开始日')
    """基金配售缴款开始日:"""

    PayEndDateF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='PayEndDateF', column_type='datetime', nullable=False, chn_name='基金配售缴款截止日')
    """基金配售缴款截止日:"""

    PrefAllotmentF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='PrefAllotmentF', column_type='decimal(16,0)', nullable=False, chn_name='投资基金配售限额(股)')
    """投资基金配售限额(股):"""

    PrefAllotmentSingleF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='PrefAllotmentSingleF', column_type='decimal(16,0)', nullable=False, chn_name='单个基金配售限额(股)')
    """单个基金配售限额(股):"""

    STAQNETPlaStartDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='STAQNETPlaStartDate', column_type='datetime', nullable=False, chn_name='STAQ/NET定向配售时间起始日')
    """STAQ/NET定向配售时间起始日:"""

    STAQNETPlaEndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='STAQNETPlaEndDate', column_type='datetime', nullable=False, chn_name='STAQ/NET定向配售时间截止日')
    """STAQ/NET定向配售时间截止日:"""

    STAQNETPlaRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='STAQNETPlaRatio', column_type='decimal(9,4)', nullable=False, chn_name='STAQ/NET定向配售比例(10配X)')
    """STAQ/NET定向配售比例(10配X):"""

    QuotationUnitOnline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='QuotationUnitOnline', column_type='decimal(19,4)', nullable=False, chn_name='网上申购报价单位(元)')
    """网上申购报价单位(元):"""

    QuotationUnitOffline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='QuotationUnitOffline', column_type='decimal(19,4)', nullable=False, chn_name='网下申购报价单位(元)')
    """网下申购报价单位(元):"""

    SMDeciPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='SMDeciPublDate', column_type='datetime', nullable=False, chn_name='股东大会决议公告日期')
    """股东大会决议公告日期:"""

    OddLotsTreatment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='OddLotsTreatment', column_type='varchar(255)', nullable=False, chn_name='零股处理方式')
    """零股处理方式:"""

    ParValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ParValue', column_type='decimal(19,4)', nullable=False, chn_name='每股面值(元)')
    """每股面值(元):"""

    IssuePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='IssuePrice', column_type='decimal(19,4)', nullable=False, chn_name='每股发行价(元)')
    """每股发行价(元):"""

    StateSharesIssuePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='StateSharesIssuePrice', column_type='decimal(19,4)', nullable=False, chn_name='国有股存量发行每股发行价(元)')
    """国有股存量发行每股发行价(元):"""

    WeightedPERatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='WeightedPERatio', column_type='real', nullable=False, chn_name='加权平均发行市盈率(倍)')
    """加权平均发行市盈率(倍):"""

    DilutedPERatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='DilutedPERatio', column_type='real', nullable=False, chn_name='全面摊薄发行市盈率(倍)')
    """全面摊薄发行市盈率(倍):"""

    PERatioBeforeIssue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='PERatioBeforeIssue', column_type='real', nullable=False, chn_name='发行市盈率(按发行前总股本)(倍)')
    """发行市盈率(按发行前总股本)(倍):"""

    PERatioAfterIssue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='PERatioAfterIssue', column_type='real', nullable=False, chn_name='发行市盈率(按发行后总股本预测利润)(倍)')
    """发行市盈率(按发行后总股本预测利润)(倍):"""

    IssueVol: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='IssueVol', column_type='decimal(16,0)', nullable=False, chn_name='发行量(股)')
    """发行量(股):"""

    StateSharesIssued: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='StateSharesIssued', column_type='decimal(16,0)', nullable=False, chn_name='其中：国有股存量发行股数(股)')
    """其中：国有股存量发行股数(股):"""

    IntentLetterPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='IntentLetterPublDate', column_type='datetime', nullable=False, chn_name='增发新股意向书发布日期')
    """增发新股意向书发布日期:"""

    TotalIssueMV: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='TotalIssueMV', column_type='decimal(19,4)', nullable=False, chn_name='发行总市值(元)')
    """发行总市值(元):"""

    IssueCost: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='IssueCost', column_type='decimal(19,4)', nullable=False, chn_name='发行费用总额(元)')
    """发行费用总额(元):"""

    UnderwritingFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='UnderwritingFee', column_type='decimal(19,4)', nullable=False, chn_name='承销费用(元)')
    """承销费用(元):"""

    CPAFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='CPAFee', column_type='decimal(19,4)', nullable=False, chn_name='注册会计师费用(元)')
    """注册会计师费用(元):"""

    AssetAppraisalFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='AssetAppraisalFee', column_type='decimal(19,4)', nullable=False, chn_name='资产评估费用(元)')
    """资产评估费用(元):"""

    LandEvaluationFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='LandEvaluationFee', column_type='decimal(19,4)', nullable=False, chn_name='土地评估费用(元)')
    """土地评估费用(元):"""

    AttorneyFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='AttorneyFee', column_type='decimal(19,4)', nullable=False, chn_name='律师费用(元)')
    """律师费用(元):"""

    TotalAgentFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='TotalAgentFee', column_type='decimal(19,4)', nullable=False, chn_name='中介机构费合计(元)')
    """中介机构费合计(元):"""

    OnlineIssueFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='OnlineIssueFee', column_type='decimal(19,4)', nullable=False, chn_name='上网发行费用(元)')
    """上网发行费用(元):"""

    ScripFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ScripFee', column_type='decimal(19,4)', nullable=False, chn_name='股票登记费用(元)')
    """股票登记费用(元):"""

    ProspectusPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='ProspectusPublDate', column_type='datetime', nullable=False, chn_name='增发新股说明书发布日期')
    """增发新股说明书发布日期:"""

    SponsorFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='SponsorFee', column_type='decimal(19,4)', nullable=False, chn_name='上市推荐费用(元)')
    """上市推荐费用(元):"""

    OtherFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='OtherFee', column_type='decimal(19,4)', nullable=False, chn_name='其他费用(元)')
    """其他费用(元):"""

    IssueCostPerShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='IssueCostPerShare', column_type='decimal(19,4)', nullable=False, chn_name='每股发行费用(元)')
    """每股发行费用(元):"""

    FreezedMoney: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='FreezedMoney', column_type='decimal(19,4)', nullable=False, chn_name='冻结资金(元)')
    """冻结资金(元):"""

    SNIProceeds: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='SNIProceeds', column_type='decimal(19,4)', nullable=False, chn_name='增发新股募集资金总额(元)')
    """增发新股募集资金总额(元):"""

    SNINetProceeds: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='SNINetProceeds', column_type='decimal(19,4)', nullable=False, chn_name='增发新股募集资金净额(元)')
    """增发新股募集资金净额(元):"""

    StateSharesProceeds: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='StateSharesProceeds', column_type='decimal(19,4)', nullable=False, chn_name='国有股存量发行收入总额(元)')
    """国有股存量发行收入总额(元):"""

    StateSharesNetProceeds: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='StateSharesNetProceeds', column_type='decimal(19,4)', nullable=False, chn_name='国有股存量发行收入净额(元)')
    """国有股存量发行收入净额(元):"""

    MoneyToAccount: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='MoneyToAccount', column_type='decimal(19,4)', nullable=False, chn_name='募集资金到帐金额(元)')
    """募集资金到帐金额(元):"""

    DateToAccount: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareSeasonedNewIssue', column_name='DateToAccount', column_type='datetime', nullable=False, chn_name='募集资金到帐时间')
    """募集资金到帐时间:"""

