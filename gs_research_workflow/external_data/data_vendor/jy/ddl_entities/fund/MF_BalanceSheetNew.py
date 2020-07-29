# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_BalanceSheetNew(SQLTableEntity):
    name: str = 'MF_BalanceSheetNew'
    
    chn_name: str = '公募基金资产负债表_新会计准则'
    
    business_unique: str = 'InnerCode,EndDate,Mark'
    
    refresh_freq: str = """半年更新"""
    
    comment: str = """1.包含依据2007年新会计准则披露的基金资产负债表数据；并跟据新旧会计准则的科目对应关系，收录了主要科目的历史对应数据。
2.收录同一基金在报告期末的两种财务报告，即未调整报表和调整后报表。若某个报告期的数据有多次调整，则该表展示最新调整数据；若某报告期暂未披露调整后数据，则已调整类别下的数据与调整前的数据一致。
3.带“##”的特殊项目为单个基金披露的非标准化的科目，对应的“特殊字段说明”字段将对其作出说明；带“##”的调整项目是为了让报表的各个小项借贷平衡而设置的，便于客户对报表的遗漏和差错进行判断。
4.该表中各财务科目下数据对应的货币单位均为人民币元。
5.历史数据：1998年12月起-至今。
6.信息来源：基金公司披露的定期报告。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    Deposit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='Deposit', column_type='decimal(19,4)', nullable=False, chn_name='银行存款')
    """银行存款:"""

    SettlementProvi: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='SettlementProvi', column_type='decimal(19,4)', nullable=False, chn_name='结算备付金')
    """结算备付金:"""

    RefundableDeposit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='RefundableDeposit', column_type='decimal(19,4)', nullable=False, chn_name='存出保证金')
    """存出保证金:"""

    TradingAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='TradingAssets', column_type='decimal(19,4)', nullable=False, chn_name='交易性金融资产')
    """交易性金融资产:"""

    StockInvestment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='StockInvestment', column_type='decimal(19,4)', nullable=False, chn_name='其中：股票投资')
    """其中：股票投资:"""

    BondInvestment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='BondInvestment', column_type='decimal(19,4)', nullable=False, chn_name='债券投资')
    """债券投资:"""

    ABSInvestment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='ABSInvestment', column_type='decimal(19,4)', nullable=False, chn_name='资产支持证券投资')
    """资产支持证券投资:"""

    FundInvestment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='FundInvestment', column_type='decimal(19,4)', nullable=False, chn_name='基金投资')
    """基金投资:"""

    WarrentInvestment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='WarrentInvestment', column_type='decimal(19,4)', nullable=False, chn_name='权证投资')
    """权证投资:"""

    DerivativeAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='DerivativeAssets', column_type='decimal(19,4)', nullable=False, chn_name='衍生金融资产')
    """衍生金融资产:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    BoughtSellbackAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='BoughtSellbackAssets', column_type='decimal(19,4)', nullable=False, chn_name='买入返售金融资产')
    """买入返售金融资产:"""

    SecuSettlementReceivables: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='SecuSettlementReceivables', column_type='decimal(19,4)', nullable=False, chn_name='应收证券清算款')
    """应收证券清算款:"""

    InterestReceivables: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='InterestReceivables', column_type='decimal(19,4)', nullable=False, chn_name='应收利息')
    """应收利息:"""

    DividendReceivables: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='DividendReceivables', column_type='decimal(19,4)', nullable=False, chn_name='应收股利')
    """应收股利:"""

    ApplyingReceivables: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='ApplyingReceivables', column_type='decimal(19,4)', nullable=False, chn_name='应收申购款')
    """应收申购款:"""

    DeferredTaxAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='DeferredTaxAssets', column_type='decimal(19,4)', nullable=False, chn_name='递延所得税资产')
    """递延所得税资产:"""

    AccountReceivables: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='AccountReceivables', column_type='decimal(19,4)', nullable=False, chn_name='应收帐款')
    """应收帐款:"""

    OtherReceivables: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='OtherReceivables', column_type='decimal(19,4)', nullable=False, chn_name='其他应收款')
    """其他应收款:"""

    DeferrredExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='DeferrredExpense', column_type='decimal(19,4)', nullable=False, chn_name='待摊费用')
    """待摊费用:"""

    OtherAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='OtherAssets', column_type='decimal(19,4)', nullable=False, chn_name='其他资产')
    """其他资产:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='InfoSource', column_type='varchar(100)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    AExceptionalItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='AExceptionalItems', column_type='decimal(19,4)', nullable=False, chn_name='##资产特殊项目')
    """##资产特殊项目:"""

    AAdjustmentItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='AAdjustmentItems', column_type='decimal(19,4)', nullable=False, chn_name='##资产调整项目')
    """##资产调整项目:"""

    TotalAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='TotalAssets', column_type='decimal(19,4)', nullable=False, chn_name='资产总计')
    """资产总计:"""

    ShortTermLoan: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='ShortTermLoan', column_type='decimal(19,4)', nullable=False, chn_name='短期借款')
    """短期借款:"""

    TradingLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='TradingLiability', column_type='decimal(19,4)', nullable=False, chn_name='交易性金融负债')
    """交易性金融负债:"""

    DerivativeLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='DerivativeLiability', column_type='decimal(19,4)', nullable=False, chn_name='衍生金融负债')
    """衍生金融负债:"""

    SoldBuybackSecuProceeds: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='SoldBuybackSecuProceeds', column_type='decimal(19,4)', nullable=False, chn_name='卖出回购金融资产款')
    """卖出回购金融资产款:"""

    SecuSettlementPayables: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='SecuSettlementPayables', column_type='decimal(19,4)', nullable=False, chn_name='应付证券清算款')
    """应付证券清算款:"""

    RedemptionMoneyPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='RedemptionMoneyPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付赎回款')
    """应付赎回款:"""

    RedemptionFeePayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='RedemptionFeePayable', column_type='decimal(19,4)', nullable=False, chn_name='应付赎回费')
    """应付赎回费:"""

    BulletinType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='BulletinType', column_type='int', nullable=False, chn_name='公告类别')
    """公告类别:公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311，得到公告类别的具体描述：10-发行上市书，20-定期报告，30-业绩快报，50-章程制度，70-临时公告，90-交易所通报，91-交易所临时停(复)牌公告，99-其他。"""

    ManagementFeePayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='ManagementFeePayable', column_type='decimal(19,4)', nullable=False, chn_name='应付管理人报酬')
    """应付管理人报酬:"""

    TrustFeePayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='TrustFeePayable', column_type='decimal(19,4)', nullable=False, chn_name='应付托管费')
    """应付托管费:"""

    SalesFeePayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='SalesFeePayable', column_type='decimal(19,4)', nullable=False, chn_name='应付销售服务费')
    """应付销售服务费:"""

    TransactionFeePayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='TransactionFeePayable', column_type='decimal(19,4)', nullable=False, chn_name='应付交易费用')
    """应付交易费用:"""

    TaxsPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='TaxsPayable', column_type='decimal(19,4)', nullable=False, chn_name='应交税费')
    """应交税费:"""

    InterestPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='InterestPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付利息')
    """应付利息:"""

    ProfitPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='ProfitPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付利润')
    """应付利润:"""

    DeferredTaxLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='DeferredTaxLiability', column_type='decimal(19,4)', nullable=False, chn_name='递延所得税负债')
    """递延所得税负债:"""

    AccountPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='AccountPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付帐款')
    """应付帐款:"""

    OtherPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='OtherPayable', column_type='decimal(19,4)', nullable=False, chn_name='其他应付款')
    """其他应付款:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='InnerCode', column_type='int', nullable=True, chn_name='基金内部编码')
    """基金内部编码:基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    AccruedExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='AccruedExpense', column_type='decimal(19,4)', nullable=False, chn_name='预提费用')
    """预提费用:"""

    OtherLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='OtherLiability', column_type='decimal(19,4)', nullable=False, chn_name='其他负债')
    """其他负债:"""

    LExceptionalItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='LExceptionalItems', column_type='decimal(19,4)', nullable=False, chn_name='##负债特殊项目')
    """##负债特殊项目:"""

    LAdjustmentItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='LAdjustmentItems', column_type='decimal(19,4)', nullable=False, chn_name='##负债调整项目')
    """##负债调整项目:"""

    TotalLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='TotalLiability', column_type='decimal(19,4)', nullable=False, chn_name='负债合计')
    """负债合计:"""

    PaidInCapital: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='PaidInCapital', column_type='decimal(19,4)', nullable=False, chn_name='实收基金')
    """实收基金:"""

    RetainedProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='RetainedProfit', column_type='decimal(19,4)', nullable=False, chn_name='未分配利润')
    """未分配利润:"""

    OtherEquity: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='OtherEquity', column_type='decimal(19,4)', nullable=False, chn_name='其他权益')
    """其他权益:"""

    SEExceptionalItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='SEExceptionalItems', column_type='decimal(19,4)', nullable=False, chn_name='##权益特殊项目')
    """##权益特殊项目:"""

    SEAdjustmentItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='SEAdjustmentItems', column_type='decimal(19,4)', nullable=False, chn_name='##权益调整项目')
    """##权益调整项目:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到基金公司的交易代码、简称等。"""

    TotalShareholderEquity: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='TotalShareholderEquity', column_type='decimal(19,4)', nullable=False, chn_name='所有者权益合计')
    """所有者权益合计:"""

    LEExceptionalItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='LEExceptionalItems', column_type='decimal(19,4)', nullable=False, chn_name='##负债和权益特殊项目')
    """##负债和权益特殊项目:"""

    LEAdjustmentItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='LEAdjustmentItems', column_type='decimal(19,4)', nullable=False, chn_name='##负债和权益调整项目')
    """##负债和权益调整项目:"""

    TotalLiabilityAndEquity: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='TotalLiabilityAndEquity', column_type='decimal(19,4)', nullable=False, chn_name='负债和所有者权益总计')
    """负债和所有者权益总计:"""

    TotalFundShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='TotalFundShares', column_type='decimal(19,4)', nullable=False, chn_name='基金份额总额(份)')
    """基金份额总额(份):"""

    UnitNV: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='UnitNV', column_type='decimal(19,4)', nullable=False, chn_name='基金份额净值')
    """基金份额净值:"""

    SpecialFieldRemark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='SpecialFieldRemark', column_type='varchar(1000)', nullable=False, chn_name='特殊字段说明')
    """特殊字段说明:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新日期')
    """更新日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    Mark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='Mark', column_type='int', nullable=True, chn_name='调整标志')
    """调整标志:调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM IN (1,2)，得到调整标志的具体描述：1-是，2-否。"""

    AccountingStandards: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BalanceSheetNew', column_name='AccountingStandards', column_type='int', nullable=False, chn_name='会计准则')
    """会计准则:会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 1455，得到会计准则的具体描述：1-新会计准则(2007)，9-旧会计准则。"""

