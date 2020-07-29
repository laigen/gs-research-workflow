# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_MainDataNew(SQLTableEntity):
    name: str = 'LC_MainDataNew'
    
    chn_name: str = '公司报告期主要会计数据_新会计准则'
    
    business_unique: str = 'CompanyCode,EndDate,Mark'
    
    refresh_freq: str = """季更新"""
    
    comment: str = """1.反映上市公司的主要指标。
2.该表收录报告期未调整和调整的数据。若某个报告期的数据有多次调整，则该表展示最新调整数据；若某报告期暂未披露调整后数据，则已调整类别下的数据与调整前的数据一致。
3.该表中各财务科目的单位均为人民币元。
4.数据范围：1989-12-31至今
5.信息来源：招股说明书、定报、审计报告等"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    DilutedEPS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='DilutedEPS', column_type='decimal(19,4)', nullable=False, chn_name='稀释每股收益(元)')
    """稀释每股收益(元):"""

    BasicEPSCut: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='BasicEPSCut', column_type='decimal(19,4)', nullable=False, chn_name='基本每股收益(扣除)(元)')
    """基本每股收益(扣除)(元):"""

    DilutedEPSCut: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='DilutedEPSCut', column_type='decimal(19,4)', nullable=False, chn_name='稀释每股收益(扣除)(元)')
    """稀释每股收益(扣除)(元):"""

    EPS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='EPS', column_type='decimal(19,4)', nullable=False, chn_name='每股收益(摊薄)(元)')
    """每股收益(摊薄)(元):每股收益（摊薄）（EPS）：由归属于母公司所有者的净利润与最新总股本相除得来。"""

    ROEByReport: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='ROEByReport', column_type='decimal(18,4)', nullable=False, chn_name='##净资产收益率(摊薄)-原始披露(%)')
    """##净资产收益率(摊薄)-原始披露(%):"""

    ROE: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='ROE', column_type='decimal(18,4)', nullable=False, chn_name='净资产收益率(摊薄)(%)')
    """净资产收益率(摊薄)(%):净资产收益率（摊薄）（ROE）：由归属于母公司所有者的净利润与归属母公司的股东权益相除得来。"""

    ROECut: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='ROECut', column_type='decimal(18,4)', nullable=False, chn_name='净资产收益率(摊薄-扣除)(%)')
    """净资产收益率(摊薄-扣除)(%):"""

    WROE: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='WROE', column_type='decimal(18,4)', nullable=False, chn_name='净资产收益率(加权)(%)')
    """净资产收益率(加权)(%):"""

    WROECut: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='WROECut', column_type='decimal(18,4)', nullable=False, chn_name='净资产收益率(加权-扣除)(%)')
    """净资产收益率(加权-扣除)(%):"""

    OperatingReenue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='OperatingReenue', column_type='decimal(19,4)', nullable=False, chn_name='营业收入(元)')
    """营业收入(元):"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。"""

    InvestIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='InvestIncome', column_type='decimal(19,4)', nullable=False, chn_name='投资净收益(元)')
    """投资净收益(元):"""

    FinancialExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='FinancialExpense', column_type='decimal(19,4)', nullable=False, chn_name='财务费用(元)')
    """财务费用(元):财务费用（FinancialExpense）：非金融类指标。"""

    FairValueChangeIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='FairValueChangeIncome', column_type='decimal(19,4)', nullable=False, chn_name='公允价值变动净收益(元)')
    """公允价值变动净收益(元):"""

    OperatingProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='OperatingProfit', column_type='decimal(19,4)', nullable=False, chn_name='营业利润(元)')
    """营业利润(元):"""

    NonoperatingIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='NonoperatingIncome', column_type='decimal(19,4)', nullable=False, chn_name='营业外收入(元)')
    """营业外收入(元):"""

    NonoperatingExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='NonoperatingExpense', column_type='decimal(19,4)', nullable=False, chn_name='营业外支出(元)')
    """营业外支出(元):"""

    TotalProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='TotalProfit', column_type='decimal(19,4)', nullable=False, chn_name='利润总额(元)')
    """利润总额(元):"""

    IncomeTaxCost: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='IncomeTaxCost', column_type='decimal(19,4)', nullable=False, chn_name='所得税(元)')
    """所得税(元):"""

    UncertainedInvestmentLosses: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='UncertainedInvestmentLosses', column_type='decimal(19,4)', nullable=False, chn_name='未确认的投资损失(元)')
    """未确认的投资损失(元):"""

    NPFromParentCompanyOwners: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='NPFromParentCompanyOwners', column_type='decimal(19,4)', nullable=False, chn_name='净利润(不含少数损益)(元)')
    """净利润(不含少数损益)(元):"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    MinorityProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='MinorityProfit', column_type='decimal(19,4)', nullable=False, chn_name='少数股东损益(元)')
    """少数股东损益(元):"""

    NetProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='NetProfit', column_type='decimal(19,4)', nullable=False, chn_name='净利润(元)')
    """净利润(元):"""

    NonRecurringProfitLoss: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='NonRecurringProfitLoss', column_type='decimal(19,4)', nullable=False, chn_name='非经常性损益(元)')
    """非经常性损益(元):"""

    NetProfitCut: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='NetProfitCut', column_type='decimal(19,4)', nullable=False, chn_name='扣除非经常性损益后净利润(元)')
    """扣除非经常性损益后净利润(元):"""

    ProfitatISA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='ProfitatISA', column_type='decimal(19,4)', nullable=False, chn_name='国际会计准则净利润(元)')
    """国际会计准则净利润(元):"""

    MarginIntoOutStatement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='MarginIntoOutStatement', column_type='text', nullable=False, chn_name='境内外审计净利润差异说明')
    """境内外审计净利润差异说明:"""

    NetOperateCashFlow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='NetOperateCashFlow', column_type='decimal(19,4)', nullable=False, chn_name='经营活动产生的现金流量净额(元)')
    """经营活动产生的现金流量净额(元):"""

    NetOperateCashFlowPS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='NetOperateCashFlowPS', column_type='decimal(19,4)', nullable=False, chn_name='每股经营活动现金流量净额(元)')
    """每股经营活动现金流量净额(元):"""

    NetInvestCashFlow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='NetInvestCashFlow', column_type='decimal(19,4)', nullable=False, chn_name='投资活动产生的现金流量净额(元)')
    """投资活动产生的现金流量净额(元):"""

    NetFinanceCashFlow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='NetFinanceCashFlow', column_type='decimal(19,4)', nullable=False, chn_name='筹资活动产生的现金流量净额(元)')
    """筹资活动产生的现金流量净额(元):"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='InfoSource', column_type='varchar(50)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    CashEquialentIncrease: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='CashEquialentIncrease', column_type='decimal(19,4)', nullable=False, chn_name='现金及现金等价物净增加额(元)')
    """现金及现金等价物净增加额(元):"""

    ExchanRateChangeEffect: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='ExchanRateChangeEffect', column_type='decimal(19,4)', nullable=False, chn_name='汇率变动对现金及现金等价物的影响')
    """汇率变动对现金及现金等价物的影响:"""

    EndPeriodCashEquivalent: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='EndPeriodCashEquivalent', column_type='decimal(19,4)', nullable=False, chn_name='期末现金及现金等价物余额')
    """期末现金及现金等价物余额:"""

    CashEquialents: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='CashEquialents', column_type='decimal(19,4)', nullable=False, chn_name='货币资金(元)')
    """货币资金(元):"""

    TradingAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='TradingAssets', column_type='decimal(19,4)', nullable=False, chn_name='交易性金融资产(元)')
    """交易性金融资产(元):"""

    InterestReceivables: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='InterestReceivables', column_type='decimal(19,4)', nullable=False, chn_name='应收利息(元)')
    """应收利息(元):"""

    DividendReceivables: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='DividendReceivables', column_type='decimal(19,4)', nullable=False, chn_name='应收股利(元)')
    """应收股利(元):"""

    AccountReceivables: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='AccountReceivables', column_type='decimal(19,4)', nullable=False, chn_name='应收账款(元)')
    """应收账款(元):"""

    OtherReceivable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='OtherReceivable', column_type='decimal(19,4)', nullable=False, chn_name='其他应收款(元)')
    """其他应收款(元):"""

    Inventories: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='Inventories', column_type='decimal(19,4)', nullable=False, chn_name='存货(元)')
    """存货(元):"""

    BulletinType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='BulletinType', column_type='varchar(30)', nullable=False, chn_name='公告类别')
    """公告类别:"""

    TotalCurrentAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='TotalCurrentAssets', column_type='decimal(19,4)', nullable=False, chn_name='流动资产合计(元)')
    """流动资产合计(元):"""

    HoldForSaleAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='HoldForSaleAssets', column_type='decimal(19,4)', nullable=False, chn_name='可供出售金融资产(元)')
    """可供出售金融资产(元):"""

    HoldToMaturityInvestments: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='HoldToMaturityInvestments', column_type='decimal(19,4)', nullable=False, chn_name='持有至到期投资(元)')
    """持有至到期投资(元):"""

    InvestmentProperty: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='InvestmentProperty', column_type='decimal(19,4)', nullable=False, chn_name='投资性房地产(元)')
    """投资性房地产(元):"""

    LongtermEquityInvest: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='LongtermEquityInvest', column_type='decimal(19,4)', nullable=False, chn_name='长期股权投资(元)')
    """长期股权投资(元):"""

    IntangibleAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='IntangibleAssets', column_type='decimal(19,4)', nullable=False, chn_name='无形资产(元)')
    """无形资产(元):"""

    TotalNonCurrentAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='TotalNonCurrentAssets', column_type='decimal(19,4)', nullable=False, chn_name='非流动资产合计(元)')
    """非流动资产合计(元):"""

    TotalAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='TotalAssets', column_type='decimal(19,4)', nullable=False, chn_name='资产总计(元)')
    """资产总计(元):"""

    ShortTermLoan: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='ShortTermLoan', column_type='decimal(19,4)', nullable=False, chn_name='短期借款(元)')
    """短期借款(元):"""

    TradingLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='TradingLiability', column_type='decimal(19,4)', nullable=False, chn_name='交易性金融负债(元)')
    """交易性金融负债(元):"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    SalariesPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='SalariesPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付职工薪酬(元)')
    """应付职工薪酬(元):"""

    DividendPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='DividendPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付股利(元)')
    """应付股利(元):"""

    TaxsPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='TaxsPayable', column_type='decimal(19,4)', nullable=False, chn_name='应交税费(元)')
    """应交税费(元):"""

    InterestPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='InterestPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付利息(元)')
    """应付利息(元):"""

    OtherPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='OtherPayable', column_type='decimal(19,4)', nullable=False, chn_name='其他应付款(元)')
    """其他应付款(元):"""

    NonCurrentLiabilityIn1Year: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='NonCurrentLiabilityIn1Year', column_type='decimal(19,4)', nullable=False, chn_name='一年内到期的非流动负债(元)')
    """一年内到期的非流动负债(元):"""

    TotalCurrentLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='TotalCurrentLiability', column_type='decimal(19,4)', nullable=False, chn_name='流动负债合计(元)')
    """流动负债合计(元):"""

    TotalNonCurrentLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='TotalNonCurrentLiability', column_type='decimal(19,4)', nullable=False, chn_name='非流动负债合计(元)')
    """非流动负债合计(元):"""

    TotalLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='TotalLiability', column_type='decimal(19,4)', nullable=False, chn_name='负债合计(元)')
    """负债合计(元):"""

    PaidInCapital: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='PaidInCapital', column_type='decimal(19,4)', nullable=False, chn_name='实收资本(或股本)(元)')
    """实收资本(或股本)(元):"""

    AccountingStandards: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='AccountingStandards', column_type='int', nullable=False, chn_name='会计准则')
    """会计准则:会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 1455，得到会计准则的具体描述：1-新会计准则(2007)，9-旧会计准则。"""

    CapitalResereFund: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='CapitalResereFund', column_type='decimal(19,4)', nullable=False, chn_name='资本公积(元)')
    """资本公积(元):"""

    SurplusReserveFund: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='SurplusReserveFund', column_type='decimal(19,4)', nullable=False, chn_name='盈余公积(元)')
    """盈余公积(元):"""

    RetainedProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='RetainedProfit', column_type='decimal(19,4)', nullable=False, chn_name='未分配利润(元)')
    """未分配利润(元):"""

    SEWithoutMI: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='SEWithoutMI', column_type='decimal(19,4)', nullable=False, chn_name='股东权益(不含少数权益)(元)')
    """股东权益(不含少数权益)(元):"""

    MinorityInterests: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='MinorityInterests', column_type='decimal(19,4)', nullable=False, chn_name='少数股东权益(元)')
    """少数股东权益(元):"""

    TotalShareholderEquity: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='TotalShareholderEquity', column_type='decimal(19,4)', nullable=False, chn_name='所有者权益合计(元)')
    """所有者权益合计(元):"""

    TotalLiabilityAndEquity: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='TotalLiabilityAndEquity', column_type='decimal(19,4)', nullable=False, chn_name='负债和所有者权益总计(元)')
    """负债和所有者权益总计(元):"""

    NetAssetISA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='NetAssetISA', column_type='decimal(19,4)', nullable=False, chn_name='国际会计准则净资产/股东权益(元)')
    """国际会计准则净资产/股东权益(元):"""

    NAPSByReport: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='NAPSByReport', column_type='decimal(19,4)', nullable=False, chn_name='##每股净资产-原始披露(元)')
    """##每股净资产-原始披露(元):"""

    NAPS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='NAPS', column_type='decimal(19,4)', nullable=False, chn_name='每股净资产(元)')
    """每股净资产(元):"""

    Mark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='Mark', column_type='int', nullable=False, chn_name='合并标志')
    """合并标志:合并调整标志（Mark）：1-最新（合并调整，暂未披露调整数据取未调整数据），2-合并未调整"""

    NAPSAdjusted: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='NAPSAdjusted', column_type='decimal(19,4)', nullable=False, chn_name='调整后每股净资产(元)')
    """调整后每股净资产(元):"""

    TotalShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='TotalShares', column_type='decimal(18,0)', nullable=False, chn_name='总股本(股)')
    """总股本(股):"""

    DiidendFinancing: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='DiidendFinancing', column_type='varchar(200)', nullable=False, chn_name='分配融资方案说明')
    """分配融资方案说明:"""

    TotalRecompense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='TotalRecompense', column_type='decimal(19,4)', nullable=False, chn_name='领导人报酬总额(元)')
    """领导人报酬总额(元):"""

    FeeForAccountantOffice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='FeeForAccountantOffice', column_type='decimal(19,4)', nullable=False, chn_name='会计师事务所费用(元)')
    """会计师事务所费用(元):"""

    ModifiedAuditOpinion: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='ModifiedAuditOpinion', column_type='varchar(100)', nullable=False, chn_name='非标准审计意见描述')
    """非标准审计意见描述:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='UpdateTime', column_type='datetime', nullable=False, chn_name='更新日期')
    """更新日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    BasicEPS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainDataNew', column_name='BasicEPS', column_type='decimal(19,4)', nullable=False, chn_name='基本每股收益(元)')
    """基本每股收益(元):基本每股收益（BasicEPS）：新会计准则下，取公司的实际披露数；旧会计准则下，取公司披露的每股收益（加权）。"""

