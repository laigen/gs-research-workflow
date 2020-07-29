# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_AShareIPO(SQLTableEntity):
    name: str = 'LC_AShareIPO'
    
    chn_name: str = 'A股发行与上市'
    
    business_unique: str = 'InnerCode'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.该表包括A股首次发行上市的明细情况。
2.中文名称带*的，表示该字段表述的信息当前已不再披露。
3.2016年1月1日起实行新股发行与上市新规。新规实行前，新股发行的招股说明书发布日期与发行公告日为同一天，新规实行后，出现不同日期的情况。
4.数据范围：1990-12-10至今
5.信息来源：招股意向书、招股说明书、上市公告书等"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    IssueEndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='IssueEndDate', column_type='datetime', nullable=False, chn_name='发行日期下限')
    """发行日期下限:"""

    AbandonSubsMOL: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='AbandonSubsMOL', column_type='decimal(19,4)', nullable=False, chn_name='投资者放弃认购金额(网上)')
    """投资者放弃认购金额(网上):"""

    UnderwritSOL: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='UnderwritSOL', column_type='decimal(19,2)', nullable=False, chn_name='包销股数(网上放弃)')
    """包销股数(网上放弃):"""

    UnderwritMOL: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='UnderwritMOL', column_type='decimal(19,4)', nullable=False, chn_name='包销金额(网上放弃)')
    """包销金额(网上放弃):"""

    UnderwritPOL: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='UnderwritPOL', column_type='decimal(19,4)', nullable=False, chn_name='包销比例(网上放弃)')
    """包销比例(网上放弃):"""

    BidderNumberLP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='BidderNumberLP', column_type='decimal(16,0)', nullable=False, chn_name='配售投标询价对象家数(家)')
    """配售投标询价对象家数(家):"""

    PlacingNumberLP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='PlacingNumberLP', column_type='int', nullable=False, chn_name='配售对象家数(家)')
    """配售对象家数(家):"""

    ApplyVolLP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ApplyVolLP', column_type='decimal(16,0)', nullable=False, chn_name='配售申购总量(股)')
    """配售申购总量(股):"""

    ValidApplyVolLP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ValidApplyVolLP', column_type='decimal(16,0)', nullable=False, chn_name='配售有效申购总量(股)')
    """配售有效申购总量(股):"""

    ValidApplyNumLP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ValidApplyNumLP', column_type='int', nullable=False, chn_name='配售有效申购户数(户)')
    """配售有效申购户数(户):"""

    OverSubsTimesLP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='OverSubsTimesLP', column_type='decimal(9,4)', nullable=False, chn_name='配售超额认购倍数(倍)')
    """配售超额认购倍数(倍):"""

    OnlineStartDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='OnlineStartDate', column_type='datetime', nullable=False, chn_name='网上申购日期上限')
    """网上申购日期上限:"""

    ApplyMoneyLP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ApplyMoneyLP', column_type='decimal(19,4)', nullable=False, chn_name='配售申购资金(元)')
    """配售申购资金(元):"""

    LotRateLP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='LotRateLP', column_type='decimal(18,15)', nullable=False, chn_name='配售中签率')
    """配售中签率:"""

    ALotRateLP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ALotRateLP', column_type='decimal(12,10)', nullable=False, chn_name='其中:A类投资者配售中签率')
    """其中:A类投资者配售中签率:其中:A类投资者配售中签率(ALotRateLP)：A类投资者代表公募基金和社保基金"""

    BLotRateLP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='BLotRateLP', column_type='decimal(12,10)', nullable=False, chn_name='其中:B类投资者配售中签率')
    """其中:B类投资者配售中签率:其中:B类投资者配售中签率(BLotRateLP)：B类投资者代表年金、保险资金"""

    CLotRateLP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='CLotRateLP', column_type='decimal(12,10)', nullable=False, chn_name='其中:C类投资者配售中签率')
    """其中:C类投资者配售中签率:其中:C类投资者配售中签率(CLotRateLP)：C类投资者代表除A类、B类以外的其他网下投资者"""

    PlacingSharesLP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='PlacingSharesLP', column_type='decimal(16,0)', nullable=False, chn_name='网下实际配售股数(股)')
    """网下实际配售股数(股):"""

    NormalLegalPersonShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='NormalLegalPersonShare', column_type='decimal(16,0)', nullable=False, chn_name='其中:向一般法人配售数量(股)')
    """其中:向一般法人配售数量(股):"""

    StrategicInvestorShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='StrategicInvestorShare', column_type='decimal(16,0)', nullable=False, chn_name='向战略投资者配售数量(股)')
    """向战略投资者配售数量(股):"""

    OtherPlacingShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='OtherPlacingShare', column_type='decimal(16,0)', nullable=False, chn_name='其他发行数量(股)')
    """其他发行数量(股):"""

    PlacingShareProportion: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='PlacingShareProportion', column_type='decimal(18,6)', nullable=False, chn_name='网下申购配售比例(%)')
    """网下申购配售比例(%):"""

    OnlineEndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='OnlineEndDate', column_type='datetime', nullable=False, chn_name='网上申购日期下限')
    """网上申购日期下限:"""

    SubsShareFL: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='SubsShareFL', column_type='decimal(19,4)', nullable=False, chn_name='投资者缴款认购股数(股)(网下)')
    """投资者缴款认购股数(股)(网下):"""

    SubsMoneyFL: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='SubsMoneyFL', column_type='decimal(19,4)', nullable=False, chn_name='投资者缴款认购金额(网下)')
    """投资者缴款认购金额(网下):"""

    AbandonSubsSFL: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='AbandonSubsSFL', column_type='decimal(19,2)', nullable=False, chn_name='投资者放弃认购股数(股)(网下)')
    """投资者放弃认购股数(股)(网下):"""

    AbandonSubsMFL: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='AbandonSubsMFL', column_type='decimal(19,4)', nullable=False, chn_name='投资者放弃认购金额(网下)')
    """投资者放弃认购金额(网下):"""

    UnderwritSFL: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='UnderwritSFL', column_type='decimal(19,2)', nullable=False, chn_name='包销股数(网下放弃)')
    """包销股数(网下放弃):"""

    UnderwritMFL: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='UnderwritMFL', column_type='decimal(19,4)', nullable=False, chn_name='包销金额(网下放弃)')
    """包销金额(网下放弃):"""

    UnderwritPFL: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='UnderwritPFL', column_type='decimal(19,4)', nullable=False, chn_name='包销比例(网下放弃)')
    """包销比例(网下放弃):"""

    TailoredPlaVolLP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='TailoredPlaVolLP', column_type='decimal(16,0)', nullable=False, chn_name='法人定向配售股数/战略定向配售(股)')
    """法人定向配售股数/战略定向配售(股):"""

    STAQNETAllotment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='STAQNETAllotment', column_type='decimal(16,0)', nullable=False, chn_name='STAQ/NET拟定向配售股数(股)')
    """STAQ/NET拟定向配售股数(股):"""

    STAQNETSubscription: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='STAQNETSubscription', column_type='decimal(16,0)', nullable=False, chn_name='STAQ/NET定向配售实际认购数(股)')
    """STAQ/NET定向配售实际认购数(股):"""

    RefundmentDate_Online: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='RefundmentDate_Online', column_type='datetime', nullable=False, chn_name='网上申购资金解冻日')
    """网上申购资金解冻日:"""

    StaffAllotment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='StaffAllotment', column_type='decimal(16,0)', nullable=False, chn_name='公司职工配售股数(股)')
    """公司职工配售股数(股):"""

    UnderwriterBoughtVol: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='UnderwriterBoughtVol', column_type='decimal(16,0)', nullable=False, chn_name='余股包销数量(股)')
    """余股包销数量(股):"""

    OverSubSum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='OverSubSum', column_type='decimal(19,2)', nullable=False, chn_name='发行时超额配售股数(股)')
    """发行时超额配售股数(股):"""

    ExGSOptionPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ExGSOptionPublDate', column_type='datetime', nullable=False, chn_name='绿鞋行使情况公告日')
    """绿鞋行使情况公告日:"""

    ExGSOptionEndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ExGSOptionEndDate', column_type='datetime', nullable=False, chn_name='绿鞋行使截止日')
    """绿鞋行使截止日:"""

    SLBuySum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='SLBuySum', column_type='decimal(19,2)', nullable=False, chn_name='二级买入股数(股)')
    """二级买入股数(股):"""

    ExGsOptionOverSubSum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ExGsOptionOverSubSum', column_type='decimal(19,2)', nullable=False, chn_name='绿鞋行使超额配售股数(股)')
    """绿鞋行使超额配售股数(股):"""

    FunPrefAllotmentShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='FunPrefAllotmentShares', column_type='decimal(16,0)', nullable=False, chn_name='*投资基金优先配售股数(股)')
    """*投资基金优先配售股数(股):"""

    FunPrefAllotmentHoldTerm: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='FunPrefAllotmentHoldTerm', column_type='decimal(9,4)', nullable=False, chn_name='*投资基金优先配售持股期限(月)')
    """*投资基金优先配售持股期限(月):"""

    ValidApplyVolSM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ValidApplyVolSM', column_type='decimal(16,0)', nullable=False, chn_name='*二级市场配售有效申购总量(股)')
    """*二级市场配售有效申购总量(股):"""

    PayDateOnline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='PayDateOnline', column_type='datetime', nullable=False, chn_name='网上申购缴款日期')
    """网上申购缴款日期:"""

    ValidApplyNumSM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ValidApplyNumSM', column_type='int', nullable=False, chn_name='*二级市场配售有效申购户数(户)')
    """*二级市场配售有效申购户数(户):"""

    OverSubsTimesSM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='OverSubsTimesSM', column_type='decimal(9,4)', nullable=False, chn_name='*二级市场配售超额认购倍数(倍)')
    """*二级市场配售超额认购倍数(倍):"""

    NumAllotedSM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='NumAllotedSM', column_type='int', nullable=False, chn_name='*二级市场配售配号总数(个)')
    """*二级市场配售配号总数(个):"""

    LotRateSM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='LotRateSM', column_type='decimal(18,15)', nullable=False, chn_name='*二级市场配售中签率')
    """*二级市场配售中签率:"""

    PlacingSharesSM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='PlacingSharesSM', column_type='decimal(16,0)', nullable=False, chn_name='*二级市场实际配售股数(股)')
    """*二级市场实际配售股数(股):"""

    ParValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ParValue', column_type='decimal(19,4)', nullable=False, chn_name='每股面值(元)')
    """每股面值(元):"""

    IssuePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='IssuePrice', column_type='decimal(19,4)', nullable=False, chn_name='每股发行价(元)')
    """每股发行价(元):"""

    IssueVol: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='IssueVol', column_type='decimal(16,0)', nullable=False, chn_name='发行量(股)')
    """发行量(股):"""

    OriginalVol: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='OriginalVol', column_type='decimal(16,0)', nullable=False, chn_name='其中老股转让发行量(股)')
    """其中老股转让发行量(股):"""

    TotalSharesListDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='TotalSharesListDate', column_type='decimal(16,0)', nullable=False, chn_name='首发后总股本_上市日(股)')
    """首发后总股本_上市日(股):"""

    BookingStartDateLP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='BookingStartDateLP', column_type='datetime', nullable=False, chn_name='网下申购日期上限')
    """网下申购日期上限:"""

    TotalSharesBeforeIssue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='TotalSharesBeforeIssue', column_type='decimal(16,0)', nullable=False, chn_name='首发前总股本(股)')
    """首发前总股本(股):"""

    TotalIssueMV: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='TotalIssueMV', column_type='decimal(19,4)', nullable=False, chn_name='发行总市值(元)')
    """发行总市值(元):"""

    EstiPERatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='EstiPERatio', column_type='decimal(19,8)', nullable=False, chn_name='预估市盈率(倍)')
    """预估市盈率(倍):预估市盈率(倍)(EstiPERatio)=预估发行价/(上年净利润/发行后总股本(预披露))"""

    WeightedPERatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='WeightedPERatio', column_type='decimal(19,8)', nullable=False, chn_name='发行市盈率(加权平均)(倍)')
    """发行市盈率(加权平均)(倍):"""

    DilutedPERatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='DilutedPERatio', column_type='decimal(19,8)', nullable=False, chn_name='发行市盈率(全面摊薄)(倍)')
    """发行市盈率(全面摊薄)(倍):"""

    PERatioBeforeIssue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='PERatioBeforeIssue', column_type='decimal(19,8)', nullable=False, chn_name='发行市盈率(按发行前总股本)(倍)')
    """发行市盈率(按发行前总股本)(倍):"""

    PERatioAfterIssue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='PERatioAfterIssue', column_type='decimal(19,8)', nullable=False, chn_name='发行市盈率(按发行后总股本预测利润)(倍)')
    """发行市盈率(按发行后总股本预测利润)(倍):"""

    StateSharesIssuePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='StateSharesIssuePrice', column_type='decimal(19,4)', nullable=False, chn_name='*国有股存量发行每股发行价(元)')
    """*国有股存量发行每股发行价(元):"""

    StateSharesIssued: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='StateSharesIssued', column_type='decimal(16,0)', nullable=False, chn_name='*国有股存量发行股数(股)')
    """*国有股存量发行股数(股):"""

    IPOProceeds: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='IPOProceeds', column_type='decimal(19,4)', nullable=False, chn_name='募集资金总额(元)')
    """募集资金总额(元):"""

    BookingEndDateLP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='BookingEndDateLP', column_type='datetime', nullable=False, chn_name='网下申购日期下限')
    """网下申购日期下限:"""

    IPONetProceeds: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='IPONetProceeds', column_type='decimal(19,4)', nullable=False, chn_name='募集资金净额(元)')
    """募集资金净额(元):"""

    MoneyToAccount: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='MoneyToAccount', column_type='decimal(19,4)', nullable=False, chn_name='募集资金到帐金额(元)')
    """募集资金到帐金额(元):"""

    DateToAccount: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='DateToAccount', column_type='datetime', nullable=False, chn_name='募集资金到帐时间')
    """募集资金到帐时间:"""

    StateSharesProceeds: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='StateSharesProceeds', column_type='decimal(19,4)', nullable=False, chn_name='*国有股存量发行收入总额(元)')
    """*国有股存量发行收入总额(元):"""

    StateSharesNetProceeds: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='StateSharesNetProceeds', column_type='decimal(19,4)', nullable=False, chn_name='*国有股存量发行收入净额(元)')
    """*国有股存量发行收入净额(元):"""

    IssueCost: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='IssueCost', column_type='decimal(19,4)', nullable=False, chn_name='发行费用总额(元)')
    """发行费用总额(元):"""

    UnderwritingFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='UnderwritingFee', column_type='decimal(19,4)', nullable=False, chn_name='承销费用(元)')
    """承销费用(元):"""

    CPAFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='CPAFee', column_type='decimal(19,4)', nullable=False, chn_name='注册会计师费用(元)')
    """注册会计师费用(元):"""

    AssetAppraisalFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='AssetAppraisalFee', column_type='decimal(19,4)', nullable=False, chn_name='资产评估费用(元)')
    """资产评估费用(元):"""

    LandEvaluationFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='LandEvaluationFee', column_type='decimal(19,4)', nullable=False, chn_name='土地评估费用(元)')
    """土地评估费用(元):"""

    RefundmentDate_Offline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='RefundmentDate_Offline', column_type='datetime', nullable=False, chn_name='网下申购资金退款日')
    """网下申购资金退款日:"""

    AttorneyFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='AttorneyFee', column_type='decimal(19,4)', nullable=False, chn_name='律师费用(元)')
    """律师费用(元):"""

    TotalAgentFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='TotalAgentFee', column_type='decimal(19,4)', nullable=False, chn_name='中介机构费合计(元)')
    """中介机构费合计(元):"""

    OnlineIssueFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='OnlineIssueFee', column_type='decimal(19,4)', nullable=False, chn_name='上网发行费用(元)')
    """上网发行费用(元):"""

    ScripFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ScripFee', column_type='decimal(19,4)', nullable=False, chn_name='股票登记费用(元)')
    """股票登记费用(元):"""

    SponsorFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='SponsorFee', column_type='decimal(19,4)', nullable=False, chn_name='上市推荐费用(元)')
    """上市推荐费用(元):"""

    OtherFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='OtherFee', column_type='decimal(19,4)', nullable=False, chn_name='其他费用(元)')
    """其他费用(元):"""

    IssueCostPerShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='IssueCostPerShare', column_type='decimal(18,6)', nullable=False, chn_name='每股发行费用(元/股)')
    """每股发行费用(元/股):"""

    PreparedListExchange: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='PreparedListExchange', column_type='int', nullable=False, chn_name='上市地')
    """上市地:上市地(PreparedListExchange)与(CT_SystemConst)表中的DM字段关联，令LB = 201，得到上市地的具体描述：10-上海期货交易所，11-上海国际能源交易中心，12-中国银行间外汇市场，13-大连商品交易所，14-上海黄金交易所，15-郑州商品交易所，49-澳大利亚证券交易所，50-新西兰证券交易所，51-中国金融期货交易..."""

    OutstandingShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='OutstandingShares', column_type='decimal(16,0)', nullable=False, chn_name='本次上市流通股数(股)')
    """本次上市流通股数(股):"""

    NumOver1000Shares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='NumOver1000Shares', column_type='int', nullable=False, chn_name='持1000股以上股东户数(户)')
    """持1000股以上股东户数(户):"""

    PayDateOffline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='PayDateOffline', column_type='datetime', nullable=False, chn_name='网下申购缴款日期')
    """网下申购缴款日期:"""

    FirstOpenPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='FirstOpenPrice', column_type='decimal(19,4)', nullable=False, chn_name='上市首日开盘价(元)')
    """上市首日开盘价(元):"""

    FirstHighPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='FirstHighPrice', column_type='decimal(19,4)', nullable=False, chn_name='上市首日最高价(元)')
    """上市首日最高价(元):"""

    FirstLowPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='FirstLowPrice', column_type='decimal(19,4)', nullable=False, chn_name='上市首日最低价(元)')
    """上市首日最低价(元):"""

    FirstClosePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='FirstClosePrice', column_type='decimal(19,4)', nullable=False, chn_name='上市首日收盘价(元)')
    """上市首日收盘价(元):"""

    FirstAvgPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='FirstAvgPrice', column_type='decimal(19,4)', nullable=False, chn_name='上市首日成交均价(元)')
    """上市首日成交均价(元):"""

    FirstTurnoverVolume: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='FirstTurnoverVolume', column_type='decimal(16,0)', nullable=False, chn_name='上市首日成交量(股)')
    """上市首日成交量(股):"""

    FirstTurnoverValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='FirstTurnoverValue', column_type='decimal(19,4)', nullable=False, chn_name='上市首日成交额(元)')
    """上市首日成交额(元):"""

    FirstChangePCT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='FirstChangePCT', column_type='decimal(18,6)', nullable=False, chn_name='上市首日涨跌幅(%)')
    """上市首日涨跌幅(%):"""

    FirstTurnover: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='FirstTurnover', column_type='decimal(18,6)', nullable=False, chn_name='上市首日换手率(%)')
    """上市首日换手率(%):"""

    SecuCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='SecuCode', column_type='varchar(20)', nullable=False, chn_name='交易代码(正股代码)')
    """交易代码(正股代码):"""

    IssueResultPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='IssueResultPublDate', column_type='datetime', nullable=False, chn_name='中签率公告日')
    """中签率公告日:"""

    SecurityAbbr: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='SecurityAbbr', column_type='varchar(100)', nullable=False, chn_name='证券简称(正股交易简称)')
    """证券简称(正股交易简称):"""

    IssueProcessCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='IssueProcessCode', column_type='int', nullable=False, chn_name='发行进程')
    """发行进程:发行进程(IssueProcessCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1722，得到发行进程的具体描述：10-待发行，20-发行待上市，30-上市，35-发行前中止，40-发行后中止，45-暂缓发行。"""

    NAPSBeforeIssue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='NAPSBeforeIssue', column_type='decimal(19,4)', nullable=False, chn_name='发行前每股净资产')
    """发行前每股净资产:"""

    NAPSAfterIssue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='NAPSAfterIssue', column_type='decimal(19,4)', nullable=False, chn_name='发行后每股净资产')
    """发行后每股净资产:"""

    EarningForecastYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='EarningForecastYear', column_type='datetime', nullable=False, chn_name='盈利预测年度')
    """盈利预测年度:"""

    MainIncomeForecast: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='MainIncomeForecast', column_type='decimal(19,4)', nullable=False, chn_name='主营业务收入预测(元)')
    """主营业务收入预测(元):"""

    NetProfitForecast: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='NetProfitForecast', column_type='decimal(19,4)', nullable=False, chn_name='净利润预测(元)')
    """净利润预测(元):"""

    DilutedEPSForecast: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='DilutedEPSForecast', column_type='decimal(19,4)', nullable=False, chn_name='全面摊薄每股盈利预测(元)')
    """全面摊薄每股盈利预测(元):"""

    DividendPolicy: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='DividendPolicy', column_type='varchar(255)', nullable=False, chn_name='股利分配政策')
    """股利分配政策:"""

    EstimatedFirstDiviDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='EstimatedFirstDiviDate', column_type='varchar(100)', nullable=False, chn_name='预计首次分配时间')
    """预计首次分配时间:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='InnerCode', column_type='int', nullable=True, chn_name='证券内部编码')
    """证券内部编码:"""

    ResultPulbDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ResultPulbDate', column_type='datetime', nullable=False, chn_name='发行结果公告日')
    """发行结果公告日:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新日期')
    """更新日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    PayStartDateLP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='PayStartDateLP', column_type='datetime', nullable=False, chn_name='*法人配售缴款期上限')
    """*法人配售缴款期上限:"""

    PayEndDateLP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='PayEndDateLP', column_type='datetime', nullable=False, chn_name='*法人配售缴款期下限')
    """*法人配售缴款期下限:"""

    ApplyStartDateF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ApplyStartDateF', column_type='datetime', nullable=False, chn_name='*基金优先配售申购日期上限')
    """*基金优先配售申购日期上限:"""

    ApplyEndDateF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ApplyEndDateF', column_type='datetime', nullable=False, chn_name='*基金优先配售申购日期下限')
    """*基金优先配售申购日期下限:"""

    PayStartDateF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='PayStartDateF', column_type='datetime', nullable=False, chn_name='*基金优先配售缴款期下限')
    """*基金优先配售缴款期下限:"""

    PayEndDateF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='PayEndDateF', column_type='datetime', nullable=False, chn_name='*基金优先配售缴款期上限')
    """*基金优先配售缴款期上限:"""

    SecMarketPlacingDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='SecMarketPlacingDate', column_type='datetime', nullable=False, chn_name='*二级市场配售日期')
    """*二级市场配售日期:"""

    PayStartDateSM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='PayStartDateSM', column_type='datetime', nullable=False, chn_name='*二级市场配售缴款日上限')
    """*二级市场配售缴款日上限:"""

    PayEndDateSM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='PayEndDateSM', column_type='datetime', nullable=False, chn_name='*二级市场配售缴款日下限')
    """*二级市场配售缴款日下限:"""

    InitialInfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='InitialInfoPublDate', column_type='datetime', nullable=True, chn_name='首次信息发布日期')
    """首次信息发布日期:"""

    ListAnnouncementDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ListAnnouncementDate', column_type='datetime', nullable=False, chn_name='上市公告日(上市公告书发布日期)')
    """上市公告日(上市公告书发布日期):"""

    ListDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ListDate', column_type='datetime', nullable=False, chn_name='上市日期')
    """上市日期:"""

    OffLineLockPeriod: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='OffLineLockPeriod', column_type='int', nullable=False, chn_name='网下配售股票锁定期(月)')
    """网下配售股票锁定期(月):"""

    NormalLegalPersonShareLD: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='NormalLegalPersonShareLD', column_type='datetime', nullable=False, chn_name='向一般法人配售部分上市日期')
    """向一般法人配售部分上市日期:"""

    StrategicInvestorShareLD: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='StrategicInvestorShareLD', column_type='datetime', nullable=False, chn_name='向战略投资者配售部分上市日期')
    """向战略投资者配售部分上市日期:"""

    StaffSharesListDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='StaffSharesListDate', column_type='datetime', nullable=False, chn_name='内部职工股上市日期')
    """内部职工股上市日期:"""

    StaffSharesListTerm: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='StaffSharesListTerm', column_type='decimal(9,4)', nullable=False, chn_name='内部职工股上市期限(年)')
    """内部职工股上市期限(年):"""

    IssueMethod: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='IssueMethod', column_type='int', nullable=False, chn_name='发行方式')
    """发行方式:"""

    RaisingMethod: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='RaisingMethod', column_type='int', nullable=False, chn_name='募资方式')
    """募资方式:募资方式(RaisingMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1021 AND DM IN (1,2,10)，得到募资方式的具体描述：1-新股发行，2-历史遗留，10-吸收合并。"""

    StockType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='StockType', column_type='int', nullable=False, chn_name='发行股票类型')
    """发行股票类型:发行股票类型(StockType)与(CT_SystemConst)表中的DM字段关联，令LB = 1177 AND DM IN (1)，得到发行股票类型的具体描述：1-A股。"""

    IntentLetterPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='IntentLetterPublDate', column_type='datetime', nullable=False, chn_name='招股公告日(招股意向书发布日期)')
    """招股公告日(招股意向书发布日期):"""

    PricingModel: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='PricingModel', column_type='int', nullable=False, chn_name='发行价定价方式')
    """发行价定价方式:"""

    RationModel: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='RationModel', column_type='int', nullable=False, chn_name='发行量定量方式')
    """发行量定量方式:"""

    IssueObject: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='IssueObject', column_type='varchar(255)', nullable=False, chn_name='发行对象')
    """发行对象:"""

    UnderwritingMode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='UnderwritingMode', column_type='int', nullable=False, chn_name='承销方式')
    """承销方式:承销方式(UnderwritingMode)与(CT_SystemConst)表中的DM字段关联，令LB = 1017，得到承销方式的具体描述：1-全额包销，2-余额包销，3-代销，4-自销，5-限额包销，8-非包销。"""

    LeadUnderwriter: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='LeadUnderwriter', column_type='varchar(500)', nullable=False, chn_name='主承销商')
    """主承销商:"""

    ColeadUnderwriter: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ColeadUnderwriter', column_type='varchar(500)', nullable=False, chn_name='副主承销商')
    """副主承销商:"""

    ListingSponsor: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ListingSponsor', column_type='varchar(500)', nullable=False, chn_name='上市推荐人')
    """上市推荐人:"""

    Distributor: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='Distributor', column_type='varchar(500)', nullable=False, chn_name='分销商')
    """分销商:"""

    InternationalCoordinator: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='InternationalCoordinator', column_type='varchar(500)', nullable=False, chn_name='国际协调人')
    """国际协调人:"""

    UnderwritingSignDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='UnderwritingSignDate', column_type='datetime', nullable=False, chn_name='*承销协议签署日')
    """*承销协议签署日:"""

    IntentLetterSignDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='IntentLetterSignDate', column_type='datetime', nullable=False, chn_name='招股意向书签署日期')
    """招股意向书签署日期:"""

    UnderwritingStartDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='UnderwritingStartDate', column_type='datetime', nullable=False, chn_name='*承销期上限')
    """*承销期上限:"""

    UnderwritingEndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='UnderwritingEndDate', column_type='datetime', nullable=False, chn_name='*承销期下限')
    """*承销期下限:"""

    IssuePriceCeiling: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='IssuePriceCeiling', column_type='decimal(19,4)', nullable=False, chn_name='发行价上限(最高价)(元)')
    """发行价上限(最高价)(元):"""

    IssuePriceFloor: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='IssuePriceFloor', column_type='decimal(19,4)', nullable=False, chn_name='发行价下限(最低价)(元)')
    """发行价下限(最低价)(元):"""

    EstiIssuePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='EstiIssuePrice', column_type='decimal(19,4)', nullable=False, chn_name='预估发行价(元)')
    """预估发行价(元):预估发行价(元)(EstiIssuePrice)：新股发行拟募集资金总额/ 发行量上限（不多于）"""

    EstiApMaxOnline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='EstiApMaxOnline', column_type='decimal(16,0)', nullable=False, chn_name='预估上网发行申购上限(最多股)')
    """预估上网发行申购上限(最多股):预估上网发行申购上限(最多股)(EstiApMaxOnline)=网上发行计划（万股）/ 1000 取整（沪市）；网上发行计划（万股）/ 500 取整（深市）"""

    IssueVolCeiling: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='IssueVolCeiling', column_type='decimal(16,0)', nullable=False, chn_name='发行量上限(不多于)(股)')
    """发行量上限(不多于)(股):"""

    OriginalVolCeiling: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='OriginalVolCeiling', column_type='decimal(16,0)', nullable=False, chn_name='老股转让发行量上限(股)')
    """老股转让发行量上限(股):"""

    IssueVolFloor: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='IssueVolFloor', column_type='decimal(16,0)', nullable=False, chn_name='发行量下限(不少于)(股)')
    """发行量下限(不少于)(股):"""

    PlannedProceeds: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='PlannedProceeds', column_type='decimal(19,4)', nullable=False, chn_name='拟募集资金总额(元)')
    """拟募集资金总额(元):"""

    ProspectusPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ProspectusPublDate', column_type='datetime', nullable=False, chn_name='招股说明书发布日期')
    """招股说明书发布日期:"""

    OnlineIssuePlan: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='OnlineIssuePlan', column_type='decimal(19,2)', nullable=False, chn_name='网上发行计划(股)')
    """网上发行计划(股):"""

    OfflineApplyPlan: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='OfflineApplyPlan', column_type='decimal(19,2)', nullable=False, chn_name='网下配售计划(股)')
    """网下配售计划(股):"""

    StrategyApplyPlan: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='StrategyApplyPlan', column_type='decimal(19,2)', nullable=False, chn_name='战略配售计划(股)')
    """战略配售计划(股):"""

    OverAllotmentOption: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='OverAllotmentOption', column_type='decimal(16,0)', nullable=False, chn_name='超额配售权(股)')
    """超额配售权(股):"""

    ApplyCodeOnline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ApplyCodeOnline', column_type='varchar(10)', nullable=False, chn_name='上网发行申购代码')
    """上网发行申购代码:"""

    IssueNameAbbr_Online: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='IssueNameAbbr_Online', column_type='varchar(20)', nullable=False, chn_name='上网发行申购简称')
    """上网发行申购简称:"""

    ApplyUnitOnline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ApplyUnitOnline', column_type='int', nullable=False, chn_name='上网发行认购单位(股)')
    """上网发行认购单位(股):"""

    ApplyMaxOnline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ApplyMaxOnline', column_type='decimal(16,0)', nullable=False, chn_name='上网发行申购上限(股)')
    """上网发行申购上限(股):"""

    ApplyFloor_Online: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ApplyFloor_Online', column_type='int', nullable=False, chn_name='上网发行申购下限(至少)(股)')
    """上网发行申购下限(至少)(股):"""

    LOAccuApplyCeiling: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='LOAccuApplyCeiling', column_type='decimal(19,2)', nullable=False, chn_name='法定机构帐户累计申购上限(股)')
    """法定机构帐户累计申购上限(股):"""

    IssuePublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='IssuePublDate', column_type='datetime', nullable=False, chn_name='发行公告日')
    """发行公告日:"""

    ApplyUnitLP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ApplyUnitLP', column_type='int', nullable=False, chn_name='法人配售认购单位(股)')
    """法人配售认购单位(股):"""

    ApplyMaxLP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ApplyMaxLP', column_type='decimal(16,0)', nullable=False, chn_name='法人配售申购上限(股)')
    """法人配售申购上限(股):"""

    ApplyMinLP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ApplyMinLP', column_type='decimal(16,0)', nullable=False, chn_name='法人配售申购下限(股)')
    """法人配售申购下限(股):"""

    OLBefPutBack: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='OLBefPutBack', column_type='decimal(19,4)', nullable=False, chn_name='网上发行量(回拨前)(万股)')
    """网上发行量(回拨前)(万股):"""

    OffLBefPutBack: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='OffLBefPutBack', column_type='decimal(19,4)', nullable=False, chn_name='网下发行量(回拨前)(万股)')
    """网下发行量(回拨前)(万股):"""

    FundPrefAllotment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='FundPrefAllotment', column_type='decimal(18,6)', nullable=False, chn_name='*投资基金优先配售限额(占发行量)')
    """*投资基金优先配售限额(占发行量):"""

    SingleFundPrefAllotment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='SingleFundPrefAllotment', column_type='decimal(18,6)', nullable=False, chn_name='*单个基金优先配售限额(占发行量)')
    """*单个基金优先配售限额(占发行量):"""

    ApplyCodeSM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ApplyCodeSM', column_type='int', nullable=False, chn_name='*二级市场配售申购代码')
    """*二级市场配售申购代码:"""

    ApplyMaxSM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ApplyMaxSM', column_type='decimal(16,0)', nullable=False, chn_name='*二级市场配售申购上限(股)')
    """*二级市场配售申购上限(股):"""

    ApplyUnitSM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ApplyUnitSM', column_type='int', nullable=False, chn_name='*二级市场配售认购单位(股)')
    """*二级市场配售认购单位(股):"""

    ProspectusSignDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ProspectusSignDate', column_type='datetime', nullable=False, chn_name='招股说明书签署日期')
    """招股说明书签署日期:"""

    MarkValueFloor: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='MarkValueFloor', column_type='decimal(19,8)', nullable=False, chn_name='网下发行询价资格所需持有市值下限(元)')
    """网下发行询价资格所需持有市值下限(元):"""

    MarkValueStatmt: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='MarkValueStatmt', column_type='varchar(500)', nullable=False, chn_name='网下发行询价资格所需持有市值说明')
    """网下发行询价资格所需持有市值说明:"""

    PriceNumberPI: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='PriceNumberPI', column_type='int', nullable=False, chn_name='初步询价价位个数')
    """初步询价价位个数:"""

    MinProgressivePricePI: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='MinProgressivePricePI', column_type='decimal(9,4)', nullable=False, chn_name='初步询价最小累进价格')
    """初步询价最小累进价格:"""

    MinApplyingPricePI: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='MinApplyingPricePI', column_type='decimal(9,4)', nullable=False, chn_name='初步询价最低申购价格')
    """初步询价最低申购价格:"""

    PriceNumberBB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='PriceNumberBB', column_type='int', nullable=False, chn_name='累计询价价位个数')
    """累计询价价位个数:"""

    MinProgressivePriceBB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='MinProgressivePriceBB', column_type='decimal(9,4)', nullable=False, chn_name='累计询价最小累进价格')
    """累计询价最小累进价格:"""

    MaxApplyingRatioBB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='MaxApplyingRatioBB', column_type='decimal(9,6)', nullable=False, chn_name='累计询价申购数量上限比例(%)')
    """累计询价申购数量上限比例(%):"""

    TimesBB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='TimesBB', column_type='decimal(19,8)', nullable=False, chn_name='询价累积报价倍数')
    """询价累积报价倍数:"""

    ValidApplyVolOnline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ValidApplyVolOnline', column_type='decimal(16,0)', nullable=False, chn_name='网上发行有效申购总量(股)')
    """网上发行有效申购总量(股):"""

    IssueStartDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='IssueStartDate', column_type='datetime', nullable=False, chn_name='发行日期上限')
    """发行日期上限:"""

    ValidApplyNumOnline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='ValidApplyNumOnline', column_type='int', nullable=False, chn_name='网上发行有效申购户数(户)')
    """网上发行有效申购户数(户):"""

    OverSubsTimesOnline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='OverSubsTimesOnline', column_type='decimal(18,6)', nullable=False, chn_name='网上发行超额认购倍数(倍)')
    """网上发行超额认购倍数(倍):"""

    NumAllotedOnline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='NumAllotedOnline', column_type='int', nullable=False, chn_name='网上发行配号总数(个)')
    """网上发行配号总数(个):"""

    FreezedMoneyOnline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='FreezedMoneyOnline', column_type='decimal(19,4)', nullable=False, chn_name='网上发行冻结资金(元)')
    """网上发行冻结资金(元):"""

    LotRateOnline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='LotRateOnline', column_type='decimal(18,15)', nullable=False, chn_name='网上发行中签率')
    """网上发行中签率:"""

    LotNumOnline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='LotNumOnline', column_type='varchar(2000)', nullable=False, chn_name='网上发行中签号')
    """网上发行中签号:"""

    SharesOnline: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='SharesOnline', column_type='decimal(16,0)', nullable=False, chn_name='网上实际发行股数(股)')
    """网上实际发行股数(股):"""

    SubsShareOL: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='SubsShareOL', column_type='decimal(19,4)', nullable=False, chn_name='投资者缴款认购股数(股)(网上)')
    """投资者缴款认购股数(股)(网上):"""

    SubsMoneyOL: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='SubsMoneyOL', column_type='decimal(19,4)', nullable=False, chn_name='投资者缴款认购金额(网上)')
    """投资者缴款认购金额(网上):"""

    AbandonSubsSOL: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AShareIPO', column_name='AbandonSubsSOL', column_type='decimal(19,2)', nullable=False, chn_name='投资者放弃认购股数(股)(网上)')
    """投资者放弃认购股数(股)(网上):"""

