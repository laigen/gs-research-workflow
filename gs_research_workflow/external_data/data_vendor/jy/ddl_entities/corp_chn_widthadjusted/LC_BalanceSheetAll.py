# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_BalanceSheetAll(SQLTableEntity):
    name: str = 'LC_BalanceSheetAll'
    
    chn_name: str = '资产负债表_新会计准则'
    
    business_unique: str = 'InfoPublDate,CompanyCode,EndDate,IfAdjusted,IfMerged'
    
    refresh_freq: str = """季更新"""
    
    comment: str = """1.反映上市公司依据2007年新会计准则在年报、中报、季报中披露的资产负债表数据；并依据新旧会计准则的科目对应关系，收录主要科目的历史对应数据。
2.收录同一公司在报告期末的四种财务报告，即未调整的合并报表、未调整的母公司报表、调整后的合并报表以及调整后的母公司报表。
3.若某个报告期的数据有多次调整，则该表展示历次调整数据。
4.该表中各财务科目的单位均为人民币元。
5.带“##”的特殊项目为单个公司披露的非标准化的科目，对应的“特殊字段说明”字段将对其作出说明；带“##”的调整项目是为了让报表的各个小项借贷平衡而设置的，便于客户对报表的遗漏和差错进行判断。
6.数据范围：1989-12-31至今
7.信息来源：招股说明书、定报、审计报告等"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    EnterpriseType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='EnterpriseType', column_type='int', nullable=True, chn_name='企业性质')
    """企业性质:企业性质(EnterpriseType)与(CT_SystemConst)表中的DM字段关联，令LB = 1414 AND DM IN (13,31,33,35,39,99)，得到企业性质的具体描述：13-商业银行，31-证券公司，33-信托公司，35-保险公司，39-其他非银行金融机构，99-一般企业。"""

    OtherCurrentLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='OtherCurrentLiability', column_type='decimal(19,4)', nullable=False, chn_name='其他流动负债')
    """其他流动负债:"""

    CLExceptionalItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='CLExceptionalItems', column_type='decimal(19,4)', nullable=False, chn_name='##流动负债特殊项目')
    """##流动负债特殊项目:"""

    CLAdjustmentItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='CLAdjustmentItems', column_type='decimal(19,4)', nullable=False, chn_name='##流动负债调整项目')
    """##流动负债调整项目:"""

    TotalCurrentLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='TotalCurrentLiability', column_type='decimal(19,4)', nullable=False, chn_name='流动负债合计')
    """流动负债合计:"""

    LongtermLoan: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='LongtermLoan', column_type='decimal(19,4)', nullable=False, chn_name='长期借款')
    """长期借款:"""

    BondsPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='BondsPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付债券')
    """应付债券:"""

    LPreferStock: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='LPreferStock', column_type='decimal(19,4)', nullable=False, chn_name='#优先股')
    """#优先股:"""

    LPerpetualDebt: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='LPerpetualDebt', column_type='decimal(19,4)', nullable=False, chn_name='#永续债')
    """#永续债:"""

    LongtermAccountPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='LongtermAccountPayable', column_type='decimal(19,4)', nullable=False, chn_name='长期应付款')
    """长期应付款:"""

    LongSalariesPay: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='LongSalariesPay', column_type='decimal(19,4)', nullable=False, chn_name='长期应付职工薪酬')
    """长期应付职工薪酬:"""

    IfComplete: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='IfComplete', column_type='int', nullable=False, chn_name='完整标志')
    """完整标志:完整标志(IfComplete)与(CT_SystemConst)表中的DM字段关联，令LB = 1444，得到完整标志的具体描述：1-完整报表，2-简表，3-个别字段修正报表。"""

    SpecificAccountPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='SpecificAccountPayable', column_type='decimal(19,4)', nullable=False, chn_name='专项应付款')
    """专项应付款:"""

    EstimateLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='EstimateLiability', column_type='decimal(19,4)', nullable=False, chn_name='预计负债')
    """预计负债:"""

    DeferredTaxLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='DeferredTaxLiability', column_type='decimal(19,4)', nullable=False, chn_name='递延所得税负债')
    """递延所得税负债:"""

    LongDeferIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='LongDeferIncome', column_type='decimal(19,4)', nullable=False, chn_name='长期递延收益')
    """长期递延收益:"""

    OtherNonCurrentLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='OtherNonCurrentLiability', column_type='decimal(19,4)', nullable=False, chn_name='其他非流动负债')
    """其他非流动负债:"""

    NCLExceptionalItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='NCLExceptionalItems', column_type='decimal(19,4)', nullable=False, chn_name='##非流动负债特殊项目')
    """##非流动负债特殊项目:"""

    NCLAdjustmentItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='NCLAdjustmentItems', column_type='decimal(19,4)', nullable=False, chn_name='##非流动负债调整项目')
    """##非流动负债调整项目:"""

    TotalNonCurrentLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='TotalNonCurrentLiability', column_type='decimal(19,4)', nullable=False, chn_name='非流动负债合计')
    """非流动负债合计:"""

    BorrowingFromCentralBank: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='BorrowingFromCentralBank', column_type='decimal(19,4)', nullable=False, chn_name='向中央银行借款')
    """向中央银行借款:"""

    DepositOfInterbank: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='DepositOfInterbank', column_type='decimal(19,4)', nullable=False, chn_name='同业及其他金融机构存放款项')
    """同业及其他金融机构存放款项:"""

    CashEquivalents: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='CashEquivalents', column_type='decimal(19,4)', nullable=False, chn_name='货币资金')
    """货币资金:"""

    BorrowingCapital: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='BorrowingCapital', column_type='decimal(19,4)', nullable=False, chn_name='拆入资金')
    """拆入资金:"""

    DerivativeLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='DerivativeLiability', column_type='decimal(19,4)', nullable=False, chn_name='衍生金融负债')
    """衍生金融负债:"""

    SoldBuybackSecuProceeds: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='SoldBuybackSecuProceeds', column_type='decimal(19,4)', nullable=False, chn_name='卖出回购金融资产款')
    """卖出回购金融资产款:"""

    Deposit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='Deposit', column_type='decimal(19,4)', nullable=False, chn_name='吸收存款')
    """吸收存款:"""

    ProxySecuProceeds: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='ProxySecuProceeds', column_type='decimal(19,4)', nullable=False, chn_name='代理买卖证券款')
    """代理买卖证券款:"""

    SubIssueSecuProceeds: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='SubIssueSecuProceeds', column_type='decimal(19,4)', nullable=False, chn_name='代理承销证券款')
    """代理承销证券款:"""

    DepositsReceived: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='DepositsReceived', column_type='decimal(19,4)', nullable=False, chn_name='存入保证金')
    """存入保证金:"""

    AdvanceInsurance: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='AdvanceInsurance', column_type='decimal(19,4)', nullable=False, chn_name='预收保费')
    """预收保费:"""

    CommissionPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='CommissionPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付手续费及佣金')
    """应付手续费及佣金:"""

    ReinsurancePayables: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='ReinsurancePayables', column_type='decimal(19,4)', nullable=False, chn_name='应付分保账款')
    """应付分保账款:"""

    ClientDeposit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='ClientDeposit', column_type='decimal(19,4)', nullable=False, chn_name='其中:客户资金存款')
    """其中:客户资金存款:"""

    CompensationPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='CompensationPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付赔付款')
    """应付赔付款:"""

    PolicyDividendPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='PolicyDividendPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付保单红利')
    """应付保单红利:"""

    InsurerDepositInvestment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='InsurerDepositInvestment', column_type='decimal(19,4)', nullable=False, chn_name='保户储金及投资款')
    """保户储金及投资款:"""

    UnearnedPremiumReserve: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='UnearnedPremiumReserve', column_type='decimal(19,4)', nullable=False, chn_name='未到期责任准备金')
    """未到期责任准备金:"""

    OutstandingClaimReserve: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='OutstandingClaimReserve', column_type='decimal(19,4)', nullable=False, chn_name='未决赔款准备金')
    """未决赔款准备金:"""

    LifeInsuranceReserve: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='LifeInsuranceReserve', column_type='decimal(19,4)', nullable=False, chn_name='寿险责任准备金')
    """寿险责任准备金:"""

    LTHealthInsuranceLR: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='LTHealthInsuranceLR', column_type='decimal(19,4)', nullable=False, chn_name='长期健康险责任准备金')
    """长期健康险责任准备金:"""

    IndependenceLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='IndependenceLiability', column_type='decimal(19,4)', nullable=False, chn_name='独立账户负债')
    """独立账户负债:"""

    OtherLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='OtherLiability', column_type='decimal(19,4)', nullable=False, chn_name='其他负债')
    """其他负债:"""

    LExceptionalItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='LExceptionalItems', column_type='decimal(19,4)', nullable=False, chn_name='##负债特殊项目')
    """##负债特殊项目:"""

    TradingAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='TradingAssets', column_type='decimal(19,4)', nullable=False, chn_name='交易性金融资产')
    """交易性金融资产:"""

    LAdjustmentItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='LAdjustmentItems', column_type='decimal(19,4)', nullable=False, chn_name='##负债调整项目')
    """##负债调整项目:"""

    TotalLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='TotalLiability', column_type='decimal(19,4)', nullable=False, chn_name='负债合计')
    """负债合计:"""

    PaidInCapital: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='PaidInCapital', column_type='decimal(19,4)', nullable=False, chn_name='实收资本(或股本)')
    """实收资本(或股本):"""

    OtherEquityinstruments: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='OtherEquityinstruments', column_type='decimal(19,4)', nullable=False, chn_name='其他权益工具')
    """其他权益工具:"""

    EPreferStock: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='EPreferStock', column_type='decimal(19,4)', nullable=False, chn_name='#优先股')
    """#优先股:"""

    EPerpetualDebt: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='EPerpetualDebt', column_type='decimal(19,4)', nullable=False, chn_name='#永续债')
    """#永续债:"""

    CapitalReserveFund: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='CapitalReserveFund', column_type='decimal(19,4)', nullable=False, chn_name='资本公积')
    """资本公积:"""

    SurplusReserveFund: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='SurplusReserveFund', column_type='decimal(19,4)', nullable=False, chn_name='盈余公积')
    """盈余公积:"""

    RetainedProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='RetainedProfit', column_type='decimal(19,4)', nullable=False, chn_name='未分配利润')
    """未分配利润:"""

    TreasuryStock: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='TreasuryStock', column_type='decimal(19,4)', nullable=False, chn_name='减:库存股')
    """减:库存股:"""

    BillReceivable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='BillReceivable', column_type='decimal(19,4)', nullable=False, chn_name='应收票据')
    """应收票据:"""

    OtherCompositeIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='OtherCompositeIncome', column_type='decimal(19,4)', nullable=False, chn_name='其他综合收益')
    """其他综合收益:"""

    OrdinaryRiskReserveFund: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='OrdinaryRiskReserveFund', column_type='decimal(19,4)', nullable=False, chn_name='一般风险准备')
    """一般风险准备:"""

    ForeignCurrencyReportConvDiff: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='ForeignCurrencyReportConvDiff', column_type='decimal(19,4)', nullable=False, chn_name='外币报表折算差额')
    """外币报表折算差额:"""

    UncertainedInvestmentLoss: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='UncertainedInvestmentLoss', column_type='decimal(19,4)', nullable=False, chn_name='未确认投资损失')
    """未确认投资损失:"""

    OtherReserves: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='OtherReserves', column_type='decimal(19,4)', nullable=False, chn_name='其他储备(公允价值变动储备)')
    """其他储备(公允价值变动储备):"""

    SpecificReserves: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='SpecificReserves', column_type='decimal(19,4)', nullable=False, chn_name='专项储备')
    """专项储备:"""

    SEExceptionalItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='SEExceptionalItems', column_type='decimal(19,4)', nullable=False, chn_name='##归属母公司所有者权益特殊项目')
    """##归属母公司所有者权益特殊项目:"""

    SEAdjustmentItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='SEAdjustmentItems', column_type='decimal(19,4)', nullable=False, chn_name='##归属母公司所有者权益调整项目')
    """##归属母公司所有者权益调整项目:"""

    SEWithoutMI: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='SEWithoutMI', column_type='decimal(19,4)', nullable=False, chn_name='归属母公司股东权益合计')
    """归属母公司股东权益合计:"""

    MinorityInterests: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='MinorityInterests', column_type='decimal(19,4)', nullable=False, chn_name='少数股东权益')
    """少数股东权益:"""

    DividendReceivable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='DividendReceivable', column_type='decimal(19,4)', nullable=False, chn_name='应收股利')
    """应收股利:"""

    OtherItemsEffectingSE: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='OtherItemsEffectingSE', column_type='decimal(19,4)', nullable=False, chn_name='##所有者权益调整项目')
    """##所有者权益调整项目:"""

    TotalShareholderEquity: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='TotalShareholderEquity', column_type='decimal(19,4)', nullable=False, chn_name='所有者权益(或股东权益)合计')
    """所有者权益(或股东权益)合计:"""

    LEExceptionalItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='LEExceptionalItems', column_type='decimal(19,4)', nullable=False, chn_name='##负债和权益特殊项目')
    """##负债和权益特殊项目:"""

    LEAdjustmentItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='LEAdjustmentItems', column_type='decimal(19,4)', nullable=False, chn_name='##负债和权益调整项目')
    """##负债和权益调整项目:"""

    TotalLiabilityAndEquity: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='TotalLiabilityAndEquity', column_type='decimal(19,4)', nullable=False, chn_name='负债和所有者权益(或股东权益)总计')
    """负债和所有者权益(或股东权益)总计:"""

    SpecialFieldRemark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='SpecialFieldRemark', column_type='varchar(1000)', nullable=False, chn_name='特殊字段说明')
    """特殊字段说明:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    TradeRiskRSRVFd: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='TradeRiskRSRVFd', column_type='decimal(19,4)', nullable=False, chn_name='交易风险准备')
    """交易风险准备:"""

    BillAccReceivable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='BillAccReceivable', column_type='decimal(19,4)', nullable=False, chn_name='应收票据及应收账款')
    """应收票据及应收账款:"""

    InterestReceivable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='InterestReceivable', column_type='decimal(19,4)', nullable=False, chn_name='应收利息')
    """应收利息:"""

    AccountReceivable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='AccountReceivable', column_type='decimal(19,4)', nullable=False, chn_name='应收账款')
    """应收账款:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='InfoPublDate', column_type='datetime', nullable=True, chn_name='信息发布日期')
    """信息发布日期:"""

    ContractualAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='ContractualAssets', column_type='decimal(19,4)', nullable=False, chn_name='合同资产')
    """合同资产:"""

    OtherReceivable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='OtherReceivable', column_type='decimal(19,4)', nullable=False, chn_name='其他应收款')
    """其他应收款:"""

    AdvancePayment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='AdvancePayment', column_type='decimal(19,4)', nullable=False, chn_name='预付款项')
    """预付款项:"""

    Inventories: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='Inventories', column_type='decimal(19,4)', nullable=False, chn_name='存货')
    """存货:"""

    BearerBiologicalAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='BearerBiologicalAssets', column_type='decimal(19,4)', nullable=False, chn_name='其中:消耗性生物资产')
    """其中:消耗性生物资产:"""

    DeferredExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='DeferredExpense', column_type='decimal(19,4)', nullable=False, chn_name='待摊费用')
    """待摊费用:"""

    HoldAndFSAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='HoldAndFSAssets', column_type='decimal(19,4)', nullable=False, chn_name='划分为持有待售的资产')
    """划分为持有待售的资产:"""

    NonCurrentAssetIn1Year: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='NonCurrentAssetIn1Year', column_type='decimal(19,4)', nullable=False, chn_name='一年内到期的非流动资产')
    """一年内到期的非流动资产:"""

    OtherCurrentAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='OtherCurrentAssets', column_type='decimal(19,4)', nullable=False, chn_name='其他流动资产')
    """其他流动资产:"""

    CAExceptionalItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='CAExceptionalItems', column_type='decimal(19,4)', nullable=False, chn_name='##流动资产特殊项目')
    """##流动资产特殊项目:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='InfoSource', column_type='varchar(100)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    CAAdjustmentItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='CAAdjustmentItems', column_type='decimal(19,4)', nullable=False, chn_name='##流动资产调整项目')
    """##流动资产调整项目:"""

    TotalCurrentAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='TotalCurrentAssets', column_type='decimal(19,4)', nullable=False, chn_name='流动资产合计')
    """流动资产合计:"""

    DebtInvestment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='DebtInvestment', column_type='decimal(19,4)', nullable=False, chn_name='债权投资')
    """债权投资:"""

    OthDebtInvestment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='OthDebtInvestment', column_type='decimal(19,4)', nullable=False, chn_name='其他债权投资')
    """其他债权投资:"""

    HoldToMaturityInvestments: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='HoldToMaturityInvestments', column_type='decimal(19,4)', nullable=False, chn_name='持有至到期投资')
    """持有至到期投资:"""

    HoldForSaleAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='HoldForSaleAssets', column_type='decimal(19,4)', nullable=False, chn_name='可供出售金融资产')
    """可供出售金融资产:"""

    OthEquityInstrument: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='OthEquityInstrument', column_type='decimal(19,4)', nullable=False, chn_name='其他权益工具投资')
    """其他权益工具投资:"""

    OthNonCurFinAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='OthNonCurFinAssets', column_type='decimal(19,4)', nullable=False, chn_name='其他非流动金融资产')
    """其他非流动金融资产:"""

    InvestmentProperty: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='InvestmentProperty', column_type='decimal(19,4)', nullable=False, chn_name='投资性房地产')
    """投资性房地产:"""

    LongtermEquityInvest: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='LongtermEquityInvest', column_type='decimal(19,4)', nullable=False, chn_name='长期股权投资')
    """长期股权投资:"""

    BulletinType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='BulletinType', column_type='int', nullable=False, chn_name='公告类别')
    """公告类别:公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311，得到公告类别的具体描述：10-发行上市书，20-定期报告，30-业绩快报，50-章程制度，70-临时公告，90-交易所通报，91-交易所临时停(复)牌公告，99-其他。"""

    LongtermReceivableAccount: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='LongtermReceivableAccount', column_type='decimal(19,4)', nullable=False, chn_name='长期应收款')
    """长期应收款:"""

    FixedAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='FixedAssets', column_type='decimal(19,4)', nullable=False, chn_name='固定资产')
    """固定资产:"""

    ConstructionMaterials: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='ConstructionMaterials', column_type='decimal(19,4)', nullable=False, chn_name='工程物资')
    """工程物资:"""

    ConstruInProcess: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='ConstruInProcess', column_type='decimal(19,4)', nullable=False, chn_name='在建工程')
    """在建工程:"""

    FixedAssetsLiquidation: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='FixedAssetsLiquidation', column_type='decimal(19,4)', nullable=False, chn_name='固定资产清理')
    """固定资产清理:"""

    BiologicalAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='BiologicalAssets', column_type='decimal(19,4)', nullable=False, chn_name='生产性生物资产')
    """生产性生物资产:"""

    OilGasAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='OilGasAssets', column_type='decimal(19,4)', nullable=False, chn_name='油气资产')
    """油气资产:"""

    IntangibleAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='IntangibleAssets', column_type='decimal(19,4)', nullable=False, chn_name='无形资产')
    """无形资产:"""

    SeatCosts: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='SeatCosts', column_type='decimal(19,4)', nullable=False, chn_name='其中:交易席位费')
    """其中:交易席位费:"""

    DevelopmentExpenditure: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='DevelopmentExpenditure', column_type='decimal(19,4)', nullable=False, chn_name='开发支出')
    """开发支出:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。"""

    GoodWill: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='GoodWill', column_type='decimal(19,4)', nullable=False, chn_name='商誉')
    """商誉:"""

    LongDeferredExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='LongDeferredExpense', column_type='decimal(19,4)', nullable=False, chn_name='长期待摊费用')
    """长期待摊费用:"""

    DeferredTaxAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='DeferredTaxAssets', column_type='decimal(19,4)', nullable=False, chn_name='递延所得税资产')
    """递延所得税资产:"""

    OtherNonCurrentAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='OtherNonCurrentAssets', column_type='decimal(19,4)', nullable=False, chn_name='其他非流动资产')
    """其他非流动资产:"""

    NCAExceptionalItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='NCAExceptionalItems', column_type='decimal(19,4)', nullable=False, chn_name='##非流动资产特殊项目')
    """##非流动资产特殊项目:"""

    NCAAdjustmentItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='NCAAdjustmentItems', column_type='decimal(19,4)', nullable=False, chn_name='##非流动资产调整项目')
    """##非流动资产调整项目:"""

    TotalNonCurrentAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='TotalNonCurrentAssets', column_type='decimal(19,4)', nullable=False, chn_name='非流动资产合计')
    """非流动资产合计:"""

    LoanAndAccountReceivables: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='LoanAndAccountReceivables', column_type='decimal(19,4)', nullable=False, chn_name='投资-贷款及应收款项(应收款项类投资)')
    """投资-贷款及应收款项(应收款项类投资):"""

    SettlementProvi: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='SettlementProvi', column_type='decimal(19,4)', nullable=False, chn_name='结算备付金')
    """结算备付金:"""

    ClientProvi: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='ClientProvi', column_type='decimal(19,4)', nullable=False, chn_name='其中:客户备付金')
    """其中:客户备付金:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    DepositInInterbank: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='DepositInInterbank', column_type='decimal(19,4)', nullable=False, chn_name='存放同业款项')
    """存放同业款项:"""

    RMetal: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='RMetal', column_type='decimal(19,4)', nullable=False, chn_name='贵金属')
    """贵金属:"""

    LendCapital: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='LendCapital', column_type='decimal(19,4)', nullable=False, chn_name='拆出资金')
    """拆出资金:"""

    DerivativeAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='DerivativeAssets', column_type='decimal(19,4)', nullable=False, chn_name='衍生金融资产')
    """衍生金融资产:"""

    BoughtSellbackAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='BoughtSellbackAssets', column_type='decimal(19,4)', nullable=False, chn_name='买入返售金融资产')
    """买入返售金融资产:"""

    LoanAndAdvance: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='LoanAndAdvance', column_type='decimal(19,4)', nullable=False, chn_name='发放贷款和垫款')
    """发放贷款和垫款:"""

    InsuranceReceivables: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='InsuranceReceivables', column_type='decimal(19,4)', nullable=False, chn_name='应收保费')
    """应收保费:"""

    ReceivableSubrogationFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='ReceivableSubrogationFee', column_type='decimal(19,4)', nullable=False, chn_name='应收代位追偿款')
    """应收代位追偿款:"""

    ReinsuranceReceivables: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='ReinsuranceReceivables', column_type='decimal(19,4)', nullable=False, chn_name='应收分保账款')
    """应收分保账款:"""

    ReceivableUnearnedR: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='ReceivableUnearnedR', column_type='decimal(19,4)', nullable=False, chn_name='应收分保未到期责任准备金')
    """应收分保未到期责任准备金:"""

    IfAdjusted: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='IfAdjusted', column_type='int', nullable=True, chn_name='是否调整')
    """是否调整:是否调整(IfAdjusted)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM IN (1,2,6,7,8)，得到是否调整的具体描述：1-是，2-否，6-一季末调整，7-二季末调整，8-三季末调整。"""

    ReceivableClaimsR: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='ReceivableClaimsR', column_type='decimal(19,4)', nullable=False, chn_name='应收分保未决赔款准备金')
    """应收分保未决赔款准备金:"""

    ReceivableLifeR: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='ReceivableLifeR', column_type='decimal(19,4)', nullable=False, chn_name='应收分保寿险责任准备金')
    """应收分保寿险责任准备金:"""

    ReceivableLTHealthR: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='ReceivableLTHealthR', column_type='decimal(19,4)', nullable=False, chn_name='应收分保长期健康险责任准备金')
    """应收分保长期健康险责任准备金:"""

    InsurerImpawnLoan: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='InsurerImpawnLoan', column_type='decimal(19,4)', nullable=False, chn_name='保户质押贷款')
    """保户质押贷款:"""

    FixedDeposit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='FixedDeposit', column_type='decimal(19,4)', nullable=False, chn_name='定期存款')
    """定期存款:"""

    RefundableDeposit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='RefundableDeposit', column_type='decimal(19,4)', nullable=False, chn_name='存出保证金')
    """存出保证金:"""

    RefundableCapitalDeposit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='RefundableCapitalDeposit', column_type='decimal(19,4)', nullable=False, chn_name='存出资本保证金')
    """存出资本保证金:"""

    IndependenceAccountAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='IndependenceAccountAssets', column_type='decimal(19,4)', nullable=False, chn_name='独立账户资产')
    """独立账户资产:"""

    OtherAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='OtherAssets', column_type='decimal(19,4)', nullable=False, chn_name='其他资产')
    """其他资产:"""

    AExceptionalItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='AExceptionalItems', column_type='decimal(19,4)', nullable=False, chn_name='##资产特殊项目')
    """##资产特殊项目:"""

    IfMerged: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='IfMerged', column_type='int', nullable=True, chn_name='是否合并')
    """是否合并:是否合并(IfMerged)与(CT_SystemConst)表中的DM字段关联，令LB = 1189 AND DM IN (1,2)，得到是否合并的具体描述：1-合并，2-母公司。"""

    AAdjustmentItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='AAdjustmentItems', column_type='decimal(19,4)', nullable=False, chn_name='##资产调整项目')
    """##资产调整项目:"""

    TotalAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='TotalAssets', column_type='decimal(19,4)', nullable=False, chn_name='资产总计')
    """资产总计:"""

    ShortTermLoan: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='ShortTermLoan', column_type='decimal(19,4)', nullable=False, chn_name='短期借款')
    """短期借款:"""

    ImpawnedLoan: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='ImpawnedLoan', column_type='decimal(19,4)', nullable=False, chn_name='其中:质押借款')
    """其中:质押借款:"""

    TradingLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='TradingLiability', column_type='decimal(19,4)', nullable=False, chn_name='交易性金融负债')
    """交易性金融负债:"""

    NotesPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='NotesPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付票据')
    """应付票据:"""

    AccountsPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='AccountsPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付账款')
    """应付账款:"""

    NotAccountsPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='NotAccountsPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付票据及应付账款')
    """应付票据及应付账款:"""

    ContractLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='ContractLiability', column_type='decimal(19,4)', nullable=False, chn_name='合同负债')
    """合同负债:"""

    STBondsPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='STBondsPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付短期债券')
    """应付短期债券:"""

    AccountingStandards: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='AccountingStandards', column_type='int', nullable=True, chn_name='会计准则')
    """会计准则:会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 1455，得到会计准则的具体描述：1-新会计准则(2007)，9-旧会计准则。"""

    AdvanceReceipts: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='AdvanceReceipts', column_type='decimal(19,4)', nullable=False, chn_name='预收款项')
    """预收款项:"""

    SalariesPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='SalariesPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付职工薪酬')
    """应付职工薪酬:"""

    DividendPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='DividendPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付股利')
    """应付股利:"""

    TaxsPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='TaxsPayable', column_type='decimal(19,4)', nullable=False, chn_name='应交税费')
    """应交税费:"""

    InterestPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='InterestPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付利息')
    """应付利息:"""

    OtherPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='OtherPayable', column_type='decimal(19,4)', nullable=False, chn_name='其他应付款')
    """其他应付款:"""

    AccruedExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='AccruedExpense', column_type='decimal(19,4)', nullable=False, chn_name='预提费用')
    """预提费用:"""

    DeferredProceeds: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='DeferredProceeds', column_type='decimal(19,4)', nullable=False, chn_name='递延收益')
    """递延收益:"""

    HoldAndFSLi: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='HoldAndFSLi', column_type='decimal(19,4)', nullable=False, chn_name='划分为持有待售的负债')
    """划分为持有待售的负债:"""

    NonCurrentLiabilityIn1Year: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetAll', column_name='NonCurrentLiabilityIn1Year', column_type='decimal(19,4)', nullable=False, chn_name='一年内到期的非流动负债')
    """一年内到期的非流动负债:"""

