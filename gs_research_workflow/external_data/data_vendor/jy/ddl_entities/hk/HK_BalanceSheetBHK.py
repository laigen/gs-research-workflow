# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_BalanceSheetBHK(SQLTableEntity):
    name: str = 'HK_BalanceSheetBHK'
    
    chn_name: str = '港股资产负债表__银行(香港会计准则)'
    
    business_unique: str = 'CompanyCode,EndDate,PeriodMark,Mark,CurrencyUnit'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.介绍按香港会计准则、国际会计准则等披露的港股银行资产负债表中各项标准化会计指标。该表为港股资产负债表的横表。
2.数据范围：1998年至今。
3.数据来源：港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    AccountingStandards: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='AccountingStandards', column_type='int', nullable=True, chn_name='会计准则')
    """会计准则:会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB=1357，得到会计准则的具体描述：7-国际会计准则，110-香港会计准则，502-美国会计准则，503-新加坡会计准则，510-国际会计准则及香港会计准则，520-中国会计准则。"""

    CurrencyUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='CurrencyUnit', column_type='int', nullable=True, chn_name='货币单位')
    """货币单位:货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB=1068，得到货币单位的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，1170-约旦第纳尔，1180-科威特..."""

    CashHoldings: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='CashHoldings', column_type='decimal(19,4)', nullable=False, chn_name='库存现金及短期资金(元)')
    """库存现金及短期资金(元):"""

    FinancialOrgDeposits: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='FinancialOrgDeposits', column_type='decimal(19,4)', nullable=False, chn_name='银行同业及其他金融机构存款(元)')
    """银行同业及其他金融机构存款(元):"""

    DepositCard: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='DepositCard', column_type='decimal(19,4)', nullable=False, chn_name='所持存款证(元)')
    """所持存款证(元):"""

    OwesCertiOfGovHK: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='OwesCertiOfGovHK', column_type='decimal(19,4)', nullable=False, chn_name='香港特区政府负债证明书(元)')
    """香港特区政府负债证明书(元):"""

    RMetal: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='RMetal', column_type='decimal(19,4)', nullable=False, chn_name='贵金属(元)')
    """贵金属(元):"""

    LendCapital: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='LendCapital', column_type='decimal(19,4)', nullable=False, chn_name='拆出资金(元)')
    """拆出资金(元):"""

    TradeBill: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='TradeBill', column_type='decimal(19,4)', nullable=False, chn_name='贸易票据(元)')
    """贸易票据(元):"""

    InterestReceivables: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='InterestReceivables', column_type='decimal(19,4)', nullable=False, chn_name='应收利息(元)')
    """应收利息(元):"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到所属公司股票的交易代码、简称等。"""

    InvestInRece: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='InvestInRece', column_type='decimal(19,4)', nullable=False, chn_name='应收款项类投资(元)')
    """应收款项类投资(元):"""

    LoansAndOtherPayment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='LoansAndOtherPayment', column_type='decimal(19,4)', nullable=False, chn_name='客户贷款及其他款项(元)')
    """客户贷款及其他款项(元):"""

    LoansOtherRece: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='LoansOtherRece', column_type='decimal(19,4)', nullable=False, chn_name='贷款及其他账项(元)')
    """贷款及其他账项(元):"""

    FinAetAtFValTPL: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='FinAetAtFValTPL', column_type='decimal(19,4)', nullable=False, chn_name='按公平值入损益金融资产(元)')
    """按公平值入损益金融资产(元):"""

    HoldForSaleAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='HoldForSaleAssets', column_type='decimal(19,4)', nullable=False, chn_name='可供出售金融资产(元)')
    """可供出售金融资产(元):"""

    HeldToMatuInv: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='HeldToMatuInv', column_type='decimal(19,4)', nullable=False, chn_name='持至到期投资(元)')
    """持至到期投资(元):"""

    AssetToSold: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='AssetToSold', column_type='decimal(19,4)', nullable=False, chn_name='待出售之资产(元)')
    """待出售之资产(元):"""

    BoughtSellbackAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='BoughtSellbackAssets', column_type='decimal(19,4)', nullable=False, chn_name='买入返售金融资产(元)')
    """买入返售金融资产(元):"""

    TradingAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='TradingAssets', column_type='decimal(19,4)', nullable=False, chn_name='交易性金融资产(元)')
    """交易性金融资产(元):"""

    DeriFinAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='DeriFinAssets', column_type='decimal(19,4)', nullable=False, chn_name='衍生性金融资产(元)')
    """衍生性金融资产(元):"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    InvestInJointVen: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='InvestInJointVen', column_type='decimal(19,4)', nullable=False, chn_name='对合营企业的投资(元)')
    """对合营企业的投资(元):"""

    SecuInvestment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='SecuInvestment', column_type='decimal(19,4)', nullable=False, chn_name='证券投资(元)')
    """证券投资(元):"""

    OSecuInvestment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='OSecuInvestment', column_type='decimal(19,4)', nullable=False, chn_name='其他证券投资(元)')
    """其他证券投资(元):"""

    SubCompanyEquity: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='SubCompanyEquity', column_type='decimal(19,4)', nullable=False, chn_name='联营公司权益(元)')
    """联营公司权益(元):"""

    SubsAndOtherEquity: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='SubsAndOtherEquity', column_type='decimal(19,4)', nullable=False, chn_name='附属公司及其他权益(元)')
    """附属公司及其他权益(元):"""

    FixedAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='FixedAssets', column_type='decimal(19,4)', nullable=False, chn_name='固定资产(元)')
    """固定资产(元):"""

    InvestProperty: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='InvestProperty', column_type='decimal(19,4)', nullable=False, chn_name='投资物业(元)')
    """投资物业(元):"""

    IntangibleAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='IntangibleAssets', column_type='decimal(19,4)', nullable=False, chn_name='无形资产(元)')
    """无形资产(元):"""

    GoodWill: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='GoodWill', column_type='decimal(19,4)', nullable=False, chn_name='商誉(元)')
    """商誉(元):"""

    DeferredTaxAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='DeferredTaxAssets', column_type='decimal(19,4)', nullable=False, chn_name='递延税项资产(元)')
    """递延税项资产(元):"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='InfoSource', column_type='varchar(100)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    OtherAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='OtherAssets', column_type='decimal(19,4)', nullable=False, chn_name='其他资产(元)')
    """其他资产(元):"""

    AExcepItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='AExcepItems', column_type='decimal(19,4)', nullable=False, chn_name='资产特殊项目(元)')
    """资产特殊项目(元):"""

    AAdjItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='AAdjItems', column_type='decimal(19,4)', nullable=False, chn_name='资产调整项目(元)')
    """资产调整项目(元):"""

    TotalAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='TotalAssets', column_type='decimal(19,4)', nullable=False, chn_name='总资产(元)')
    """总资产(元):"""

    HongkongDollar: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='HongkongDollar', column_type='decimal(19,4)', nullable=False, chn_name='香港特区政府流通纸币(元)')
    """香港特区政府流通纸币(元):"""

    BorFromCentralBank: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='BorFromCentralBank', column_type='decimal(19,4)', nullable=False, chn_name='向中央银行借款(元)')
    """向中央银行借款(元):"""

    FOrganizationDepposit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='FOrganizationDepposit', column_type='decimal(19,4)', nullable=False, chn_name='银行同业及其他金融机构存款(负债)(元)')
    """银行同业及其他金融机构存款(负债)(元):"""

    CustomerDeposits: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='CustomerDeposits', column_type='decimal(19,4)', nullable=False, chn_name='客户存款(元)')
    """客户存款(元):"""

    IssuedDepositCard: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='IssuedDepositCard', column_type='decimal(19,4)', nullable=False, chn_name='已发行存款证(元)')
    """已发行存款证(元):"""

    BorrowingCapital: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='BorrowingCapital', column_type='decimal(19,4)', nullable=False, chn_name='拆入资金(元)')
    """拆入资金(元):"""

    BeginDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='BeginDate', column_type='datetime', nullable=False, chn_name='开始日期')
    """开始日期:"""

    TaxPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='TaxPayable', column_type='decimal(19,4)', nullable=False, chn_name='应交税项(元)')
    """应交税项(元):"""

    InterestPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='InterestPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付利息(元)')
    """应付利息(元):"""

    SalariesPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='SalariesPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付职工薪酬(元)')
    """应付职工薪酬(元):"""

    LendingCapital: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='LendingCapital', column_type='decimal(19,4)', nullable=False, chn_name='借贷资本(元)')
    """借贷资本(元):"""

    SubordDebt: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='SubordDebt', column_type='decimal(19,4)', nullable=False, chn_name='后偿负债(元)')
    """后偿负债(元):"""

    Issuedbond: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='Issuedbond', column_type='decimal(19,4)', nullable=False, chn_name='已发行债券(元)')
    """已发行债券(元):"""

    DebtInstruIssued: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='DebtInstruIssued', column_type='decimal(19,4)', nullable=False, chn_name='已发行债务工具(元)')
    """已发行债务工具(元):"""

    DerivativeLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='DerivativeLiability', column_type='decimal(19,4)', nullable=False, chn_name='衍生金融负债(元)')
    """衍生金融负债(元):"""

    SBbSecuProceeds: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='SBbSecuProceeds', column_type='decimal(19,4)', nullable=False, chn_name='卖出回购金融资产款(元)')
    """卖出回购金融资产款(元):"""

    DeferredTaxLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='DeferredTaxLiability', column_type='decimal(19,4)', nullable=False, chn_name='递延税项负债(元)')
    """递延税项负债(元):"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    OtherAccountAndPrepare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='OtherAccountAndPrepare', column_type='decimal(19,4)', nullable=False, chn_name='其他帐项及准备(元)')
    """其他帐项及准备(元):"""

    LExcepItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='LExcepItems', column_type='decimal(19,4)', nullable=False, chn_name='负债特殊项目(元)')
    """负债特殊项目(元):"""

    LAdjuItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='LAdjuItems', column_type='decimal(19,4)', nullable=False, chn_name='负债调整项目(元)')
    """负债调整项目(元):"""

    TotalLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='TotalLiability', column_type='decimal(19,4)', nullable=False, chn_name='总负债(元)')
    """总负债(元):"""

    AssetLessTLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='AssetLessTLiability', column_type='decimal(19,4)', nullable=False, chn_name='总资产减总负债(元)')
    """总资产减总负债(元):"""

    ShareCapital: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='ShareCapital', column_type='decimal(19,4)', nullable=False, chn_name='股本(元)')
    """股本(元):"""

    OtherEquityinstruments: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='OtherEquityinstruments', column_type='decimal(19,4)', nullable=False, chn_name='其他权益工具(元)')
    """其他权益工具(元):"""

    Reserve: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='Reserve', column_type='decimal(19,4)', nullable=False, chn_name='储备(元)')
    """储备(元):"""

    StockPremium: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='StockPremium', column_type='decimal(19,4)', nullable=False, chn_name='股本溢价(元)')
    """股本溢价(元):"""

    ReserveFund: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='ReserveFund', column_type='decimal(19,4)', nullable=False, chn_name='法定储备(元)')
    """法定储备(元):"""

    PeriodMark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='PeriodMark', column_type='int', nullable=True, chn_name='日期标志')
    """日期标志:日期标志(PeriodMark)与(CT_SystemConst)表中的DM字段关联，令LB=1314，得到日期标志的具体描述：1-1个月，2-2个月，3-3个月，4-4个月，5-5个月，6-半年度，7-7个月，8-8个月，9-9个月，10-10个月，11-11个月，12-年度，13-13个月，14-14个月，15-15个月，16-16个月，17-17个月，..."""

    CapitalReserveFund: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='CapitalReserveFund', column_type='decimal(19,4)', nullable=False, chn_name='资本公积(元)')
    """资本公积(元):"""

    RevaluationReserve: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='RevaluationReserve', column_type='decimal(19,4)', nullable=False, chn_name='重估储备(元)')
    """重估储备(元):"""

    ExchangeReserve: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='ExchangeReserve', column_type='decimal(19,4)', nullable=False, chn_name='汇兑储备(元)')
    """汇兑储备(元):"""

    OtherReserve: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='OtherReserve', column_type='decimal(19,4)', nullable=False, chn_name='其他储备(元)')
    """其他储备(元):"""

    HoldProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='HoldProfit', column_type='decimal(19,4)', nullable=False, chn_name='保留溢利(元)')
    """保留溢利(元):"""

    SimulantAllotDividend: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='SimulantAllotDividend', column_type='decimal(19,4)', nullable=False, chn_name='拟派股息(元)')
    """拟派股息(元):"""

    RetainedProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='RetainedProfit', column_type='decimal(19,4)', nullable=False, chn_name='未分配利润(元)')
    """未分配利润(元):"""

    SEExcepItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='SEExcepItems', column_type='decimal(19,4)', nullable=False, chn_name='股东权益特殊项目(元)')
    """股东权益特殊项目(元):"""

    SEAdjItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='SEAdjItems', column_type='decimal(19,4)', nullable=False, chn_name='股东权益调整项目(元)')
    """股东权益调整项目(元):"""

    ShareholderEquity: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='ShareholderEquity', column_type='decimal(19,4)', nullable=False, chn_name='股东权益(元)')
    """股东权益(元):"""

    CompanyNature: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='CompanyNature', column_type='int', nullable=False, chn_name='公司性质')
    """公司性质:公司性质(CompanyNature)与(CT_SystemConst)表中的DM字段关联，令令LB=1356，得到公司性质的具体描述："""

    MinorityInterests: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='MinorityInterests', column_type='decimal(19,4)', nullable=False, chn_name='非控股权益(元)')
    """非控股权益(元):"""

    AddEquityInstruments: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='AddEquityInstruments', column_type='decimal(19,4)', nullable=False, chn_name='额外股本工具(元)')
    """额外股本工具(元):"""

    TotalInterests: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='TotalInterests', column_type='decimal(19,4)', nullable=False, chn_name='总权益(元)')
    """总权益(元):"""

    TotalIntATotalLiab: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='TotalIntATotalLiab', column_type='decimal(19,4)', nullable=False, chn_name='总权益及总负债(元)')
    """总权益及总负债(元):"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    FiscalYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='FiscalYear', column_type='datetime', nullable=False, chn_name='财政年度')
    """财政年度:"""

    InsertTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='InsertTime', column_type='datetime', nullable=False, chn_name='发布时间')
    """发布时间:"""

    Mark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetBHK', column_name='Mark', column_type='int', nullable=True, chn_name='合并调整标志')
    """合并调整标志:合并调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB=1511，得到合并调整标志的具体描述：1-合并调整，2-合并未调整，3-母公司调整，4-母公司未调整，5-专项合并调整，6-专项合并未调整。"""

