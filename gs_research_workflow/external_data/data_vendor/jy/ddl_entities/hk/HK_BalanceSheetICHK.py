# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_BalanceSheetICHK(SQLTableEntity):
    name: str = 'HK_BalanceSheetICHK'
    
    chn_name: str = '港股资产负债表__保险(香港会计准则)'
    
    business_unique: str = 'EndDate,CompanyCode,PeriodMark,Mark,CurrencyUnit'
    
    refresh_freq: str = """滚动更新"""
    
    comment: str = """1.介绍按香港会计准则、国际会计准则等披露的港股保险公司资产负债表中各项标准化会计指标。该表为港股资产负债表的横表。
2.数据范围：2000年至今。
3.数据来源：港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    AccountingStandards: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='AccountingStandards', column_type='int', nullable=True, chn_name='会计准则')
    """会计准则:会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB=1357，得到会计准则的具体描述：7-国际会计准则，110-香港会计准则，502-美国会计准则，503-新加坡会计准则，510-国际会计准则及香港会计准则，520-中国会计准则。"""

    CurrencyUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='CurrencyUnit', column_type='int', nullable=True, chn_name='货币单位')
    """货币单位:货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB=1068，得到货币单位的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，1170-约旦第纳尔，1180-科威特..."""

    DepositCardIA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='DepositCardIA', column_type='decimal(19,4)', nullable=False, chn_name='存款证(元)')
    """存款证(元):"""

    FixedDeposit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='FixedDeposit', column_type='decimal(19,4)', nullable=False, chn_name='定期存款(元)')
    """定期存款(元):"""

    ReserveDeposits: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='ReserveDeposits', column_type='decimal(19,4)', nullable=False, chn_name='法定存款(元)')
    """法定存款(元):"""

    Cash: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='Cash', column_type='decimal(19,4)', nullable=False, chn_name='现金及等价物(元)')
    """现金及等价物(元):"""

    ReinsAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='ReinsAssets', column_type='decimal(19,4)', nullable=False, chn_name='再保险资产(元)')
    """再保险资产(元):"""

    RefCapDeposit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='RefCapDeposit', column_type='decimal(19,4)', nullable=False, chn_name='存出资本保证金(元)')
    """存出资本保证金(元):"""

    PrepaidLeasePays: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='PrepaidLeasePays', column_type='decimal(19,4)', nullable=False, chn_name='预付租赁付款(元)')
    """预付租赁付款(元):"""

    InvestIncRece: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='InvestIncRece', column_type='decimal(19,4)', nullable=False, chn_name='应收投资收益(元)')
    """应收投资收益(元):"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到所属公司股票的交易代码、简称等。"""

    InsuranceReceivables: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='InsuranceReceivables', column_type='decimal(19,4)', nullable=False, chn_name='应收保费(元)')
    """应收保费(元):"""

    ReinsuranceReceivables: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='ReinsuranceReceivables', column_type='decimal(19,4)', nullable=False, chn_name='应收分保账款(元)')
    """应收分保账款(元):"""

    InsAndOthRece: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='InsAndOthRece', column_type='decimal(19,4)', nullable=False, chn_name='保险及其他应收款项(元)')
    """保险及其他应收款项(元):"""

    InvestInLoansAndRece: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='InvestInLoansAndRece', column_type='decimal(19,4)', nullable=False, chn_name='归入贷款及应收款的投资(元)')
    """归入贷款及应收款的投资(元):"""

    SecuInvestment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='SecuInvestment', column_type='decimal(19,4)', nullable=False, chn_name='证券投资(元)')
    """证券投资(元):"""

    FinAetAtFValTPL: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='FinAetAtFValTPL', column_type='decimal(19,4)', nullable=False, chn_name='按公平值入损益金融资产(元)')
    """按公平值入损益金融资产(元):"""

    HoldForSaleAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='HoldForSaleAssets', column_type='decimal(19,4)', nullable=False, chn_name='可供出售金融资产(元)')
    """可供出售金融资产(元):"""

    BoughtSellbackSecu: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='BoughtSellbackSecu', column_type='decimal(19,4)', nullable=False, chn_name='买入返售证券(元)')
    """买入返售证券(元):"""

    EquUTFundInvPort: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='EquUTFundInvPort', column_type='decimal(19,4)', nullable=False, chn_name='股本证券及单位信托基金投资组合(元)')
    """股本证券及单位信托基金投资组合(元):"""

    InvInAsJointVen: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='InvInAsJointVen', column_type='decimal(19,4)', nullable=False, chn_name='于联营企业和合营企业的投资(元)')
    """于联营企业和合营企业的投资(元):"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    HoldToMatInv: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='HoldToMatInv', column_type='decimal(19,4)', nullable=False, chn_name='持有至到期投资(元)')
    """持有至到期投资(元):"""

    SubCompanyEquity: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='SubCompanyEquity', column_type='decimal(19,4)', nullable=False, chn_name='联营公司权益(元)')
    """联营公司权益(元):"""

    InvestProperty: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='InvestProperty', column_type='decimal(19,4)', nullable=False, chn_name='投资物业(元)')
    """投资物业(元):"""

    WorkshopAndEquipment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='WorkshopAndEquipment', column_type='decimal(19,4)', nullable=False, chn_name='物业厂房及设备(元)')
    """物业厂房及设备(元):"""

    DeferredTaxAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='DeferredTaxAssets', column_type='decimal(19,4)', nullable=False, chn_name='递延税项资产(元)')
    """递延税项资产(元):"""

    Borrowings: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='Borrowings', column_type='decimal(19,4)', nullable=False, chn_name='贷款(元)')
    """贷款(元):"""

    InsurerImpawnLoan: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='InsurerImpawnLoan', column_type='decimal(19,4)', nullable=False, chn_name='保户质押贷款(元)')
    """保户质押贷款(元):"""

    DebtsSecurities: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='DebtsSecurities', column_type='decimal(19,4)', nullable=False, chn_name='债务证券(元)')
    """债务证券(元):"""

    RecoverTax: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='RecoverTax', column_type='decimal(19,4)', nullable=False, chn_name='可收回税项(元)')
    """可收回税项(元):"""

    AExcepItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='AExcepItems', column_type='decimal(19,4)', nullable=False, chn_name='资产特殊项目(元)')
    """资产特殊项目(元):"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='InfoSource', column_type='varchar(100)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    AAdjItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='AAdjItems', column_type='decimal(19,4)', nullable=False, chn_name='资产调整项目(元)')
    """资产调整项目(元):"""

    TotalAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='TotalAssets', column_type='decimal(19,4)', nullable=False, chn_name='总资产(元)')
    """总资产(元):"""

    DepositOfInsured: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='DepositOfInsured', column_type='decimal(19,4)', nullable=False, chn_name='保户储金(元)')
    """保户储金(元):"""

    InsContract: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='InsContract', column_type='decimal(19,4)', nullable=False, chn_name='保险合同(元)')
    """保险合同(元):"""

    InvestContract: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='InvestContract', column_type='decimal(19,4)', nullable=False, chn_name='投资合同(元)')
    """投资合同(元):"""

    ReinPremPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='ReinPremPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付再保险保费(元)')
    """应付再保险保费(元):"""

    InsurAccPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='InsurAccPayable', column_type='decimal(19,4)', nullable=False, chn_name='保险应付账款(元)')
    """保险应付账款(元):"""

    SubordDebtIL: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='SubordDebtIL', column_type='decimal(19,4)', nullable=False, chn_name='应付次级债(元)')
    """应付次级债(元):"""

    DiviForInsured: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='DiviForInsured', column_type='decimal(19,4)', nullable=False, chn_name='应付保户红利(元)')
    """应付保户红利(元):"""

    BFinInstAmsPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='BFinInstAmsPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付银行及其他金融机构款项(元)')
    """应付银行及其他金融机构款项(元):"""

    BeginDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='BeginDate', column_type='datetime', nullable=False, chn_name='开始日期')
    """开始日期:"""

    TaxesPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='TaxesPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付税项(元)')
    """应付税项(元):"""

    AccountsPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='AccountsPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付帐款(元)')
    """应付帐款(元):"""

    AdvanceInsurance: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='AdvanceInsurance', column_type='decimal(19,4)', nullable=False, chn_name='预收保费(元)')
    """预收保费(元):"""

    NotDecidedReserves: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='NotDecidedReserves', column_type='decimal(19,4)', nullable=False, chn_name='未决赔款准备(元)')
    """未决赔款准备(元):"""

    SoldRepoSecuProceeds: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='SoldRepoSecuProceeds', column_type='decimal(19,4)', nullable=False, chn_name='卖出回购证券(元)')
    """卖出回购证券(元):"""

    FinliabAtFV: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='FinliabAtFV', column_type='decimal(19,4)', nullable=False, chn_name='以公平值计入损益金融负债(元)')
    """以公平值计入损益金融负债(元):"""

    DerivativeLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='DerivativeLiability', column_type='decimal(19,4)', nullable=False, chn_name='衍生金融负债(元)')
    """衍生金融负债(元):"""

    DeferredTaxLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='DeferredTaxLiability', column_type='decimal(19,4)', nullable=False, chn_name='递延税项负债(元)')
    """递延税项负债(元):"""

    CurIncTaxLiab: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='CurIncTaxLiab', column_type='decimal(19,4)', nullable=False, chn_name='当期所得税负债(元)')
    """当期所得税负债(元):"""

    LExcepItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='LExcepItems', column_type='decimal(19,4)', nullable=False, chn_name='负债特殊项目(元)')
    """负债特殊项目(元):"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    LAdjuItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='LAdjuItems', column_type='decimal(19,4)', nullable=False, chn_name='负债调整项目(元)')
    """负债调整项目(元):"""

    TotalLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='TotalLiability', column_type='decimal(19,4)', nullable=False, chn_name='总负债(元)')
    """总负债(元):"""

    AssetLessTLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='AssetLessTLiability', column_type='decimal(19,4)', nullable=False, chn_name='总资产减总负债(元)')
    """总资产减总负债(元):"""

    ShareCapital: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='ShareCapital', column_type='decimal(19,4)', nullable=False, chn_name='股本(元)')
    """股本(元):"""

    OtherEquityinstruments: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='OtherEquityinstruments', column_type='decimal(19,4)', nullable=False, chn_name='其他权益工具(元)')
    """其他权益工具(元):"""

    Reserve: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='Reserve', column_type='decimal(19,4)', nullable=False, chn_name='储备(元)')
    """储备(元):"""

    StockPremium: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='StockPremium', column_type='decimal(19,4)', nullable=False, chn_name='股本溢价(元)')
    """股本溢价(元):"""

    ReserveFund: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='ReserveFund', column_type='decimal(19,4)', nullable=False, chn_name='法定储备(元)')
    """法定储备(元):"""

    CapitalReserveFund: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='CapitalReserveFund', column_type='decimal(19,4)', nullable=False, chn_name='资本公积(元)')
    """资本公积(元):"""

    RevaluationReserve: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='RevaluationReserve', column_type='decimal(19,4)', nullable=False, chn_name='重估储备(元)')
    """重估储备(元):"""

    PeriodMark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='PeriodMark', column_type='int', nullable=True, chn_name='日期标志')
    """日期标志:日期标志(PeriodMark)与(CT_SystemConst)表中的DM字段关联，令LB=1314，得到日期标志的具体描述：1-1个月，2-2个月，3-3个月，4-4个月，5-5个月，6-半年度，7-7个月，8-8个月，9-9个月，10-10个月，11-11个月，12-年度，13-13个月，14-14个月，15-15个月，16-16个月，17-17个月，..."""

    ExchangeReserve: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='ExchangeReserve', column_type='decimal(19,4)', nullable=False, chn_name='汇兑储备(元)')
    """汇兑储备(元):"""

    OtherReserve: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='OtherReserve', column_type='decimal(19,4)', nullable=False, chn_name='其他储备(元)')
    """其他储备(元):"""

    HoldProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='HoldProfit', column_type='decimal(19,4)', nullable=False, chn_name='保留溢利(元)')
    """保留溢利(元):"""

    SimulantAllotDividend: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='SimulantAllotDividend', column_type='decimal(19,4)', nullable=False, chn_name='拟派股息(元)')
    """拟派股息(元):"""

    RetainedProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='RetainedProfit', column_type='decimal(19,4)', nullable=False, chn_name='未分配利润(元)')
    """未分配利润(元):"""

    SEExcepItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='SEExcepItems', column_type='decimal(19,4)', nullable=False, chn_name='股东权益特殊项目(元)')
    """股东权益特殊项目(元):"""

    SEAdjItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='SEAdjItems', column_type='decimal(19,4)', nullable=False, chn_name='股东权益调整项目(元)')
    """股东权益调整项目(元):"""

    ShareholderEquity: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='ShareholderEquity', column_type='decimal(19,4)', nullable=False, chn_name='股东权益(元)')
    """股东权益(元):"""

    MinorityInterests: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='MinorityInterests', column_type='decimal(19,4)', nullable=False, chn_name='非控股权益(元)')
    """非控股权益(元):"""

    TotalInterests: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='TotalInterests', column_type='decimal(19,4)', nullable=False, chn_name='总权益(元)')
    """总权益(元):"""

    CompanyNature: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='CompanyNature', column_type='int', nullable=False, chn_name='公司性质')
    """公司性质:公司性质(CompanyNature)与(CT_SystemConst)表中的DM字段关联，令LB=1356，得到公司性质的具体描述：1-普通，2-金融，3-保险，4-房地产，5-银行。"""

    TotalIntATotalLiab: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='TotalIntATotalLiab', column_type='decimal(19,4)', nullable=False, chn_name='总权益及总负债(元)')
    """总权益及总负债(元):"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    FiscalYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='FiscalYear', column_type='datetime', nullable=False, chn_name='财政年度')
    """财政年度:"""

    InsertTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='InsertTime', column_type='datetime', nullable=False, chn_name='发布时间')
    """发布时间:"""

    Mark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetICHK', column_name='Mark', column_type='int', nullable=True, chn_name='合并调整标志')
    """合并调整标志:合并调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB=1511，得到合并调整标志的具体描述：1-合并调整，2-合并未调整，3-母公司调整，4-母公司未调整，5-专项合并调整，6-专项合并未调整。"""

