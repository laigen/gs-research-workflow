# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_IncomeStatementNew(SQLTableEntity):
    name: str = 'MF_IncomeStatementNew'
    
    chn_name: str = '公募基金利润表_新会计准则'
    
    business_unique: str = 'InnerCode,EndDate,Mark'
    
    refresh_freq: str = """半年更新"""
    
    comment: str = """1.包含依据2007年新会计准则披露的基金利润表数据；并跟据新旧会计准则的科目对应关系，收录了主要科目的历史对应数据。
2.收录同一基金在报告期末的两种财务报告，即未调整报表和调整后报表。若某个报告期的数据有多次调整，则该表展示最新调整数据；若某报告期暂未披露调整后数据，则已调整类别下的数据与调整前的数据一致。
3.带“##”的特殊项目为单个基金披露的非标准化的科目，对应的“特殊字段说明”字段将对其作出说明；带“##”的调整项目是为了让报表的各个小项借贷平衡而设置的，便于客户对报表的遗漏和差错进行判断。
4.该表中各财务科目下数据对应的货币单位均为人民币元。
5.历史数据：1998年12月起-至今。
6.信息来源：基金公司披露的定期报告。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    AccountingStandards: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='AccountingStandards', column_type='int', nullable=False, chn_name='会计准则')
    """会计准则:会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 1455，得到会计准则的具体描述：1-新会计准则(2007)，9-旧会计准则。"""

    InterestIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='InterestIncome', column_type='decimal(19,4)', nullable=False, chn_name='1.利息收入')
    """1.利息收入:"""

    DepositInterestIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='DepositInterestIncome', column_type='decimal(19,4)', nullable=False, chn_name='其中:存款利息收入')
    """其中:存款利息收入:"""

    BondInterestIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='BondInterestIncome', column_type='decimal(19,4)', nullable=False, chn_name='债券利息收入')
    """债券利息收入:"""

    ABSInterestIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='ABSInterestIncome', column_type='decimal(19,4)', nullable=False, chn_name='资产支持证券利息收入')
    """资产支持证券利息收入:"""

    SellbackAssetsIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='SellbackAssetsIncome', column_type='decimal(19,4)', nullable=False, chn_name='买入返售金融资产收入')
    """买入返售金融资产收入:"""

    OtherInterestIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='OtherInterestIncome', column_type='decimal(19,4)', nullable=False, chn_name='其他利息收入')
    """其他利息收入:"""

    InvestmentIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='InvestmentIncome', column_type='decimal(19,4)', nullable=False, chn_name='2.投资收益')
    """2.投资收益:"""

    StockInvestmentIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='StockInvestmentIncome', column_type='decimal(19,4)', nullable=False, chn_name='其中:股票投资收益')
    """其中:股票投资收益:"""

    BondInvestmentIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='BondInvestmentIncome', column_type='decimal(19,4)', nullable=False, chn_name='债券投资收益')
    """债券投资收益:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    ABSInvestmentIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='ABSInvestmentIncome', column_type='decimal(19,4)', nullable=False, chn_name='资产支持证券投资收益')
    """资产支持证券投资收益:"""

    FundInvestIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='FundInvestIncome', column_type='decimal(19,4)', nullable=False, chn_name='基金投资收益')
    """基金投资收益:"""

    DerivativeInvestIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='DerivativeInvestIncome', column_type='decimal(19,4)', nullable=False, chn_name='衍生工具收益')
    """衍生工具收益:"""

    DividendIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='DividendIncome', column_type='decimal(19,4)', nullable=False, chn_name='股利收益')
    """股利收益:"""

    OtherInvestmentIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='OtherInvestmentIncome', column_type='decimal(19,4)', nullable=False, chn_name='其他投资收益')
    """其他投资收益:"""

    FairValueChangeIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='FairValueChangeIncome', column_type='decimal(19,4)', nullable=False, chn_name='3.公允价值变动收益')
    """3.公允价值变动收益:"""

    ExchangeIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='ExchangeIncome', column_type='decimal(19,4)', nullable=False, chn_name='4.汇兑收益')
    """4.汇兑收益:"""

    OtherIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='OtherIncome', column_type='decimal(19,4)', nullable=False, chn_name='5.其他收入')
    """5.其他收入:"""

    IncomeExceptionalItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='IncomeExceptionalItems', column_type='decimal(19,4)', nullable=False, chn_name='##收入特殊项目')
    """##收入特殊项目:"""

    IncomeAdjustmentItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='IncomeAdjustmentItems', column_type='decimal(19,4)', nullable=False, chn_name='##收入调整项目')
    """##收入调整项目:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='InfoSource', column_type='varchar(100)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    TotalRevenue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='TotalRevenue', column_type='decimal(19,4)', nullable=False, chn_name='收入合计')
    """收入合计:"""

    MangementExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='MangementExpense', column_type='decimal(19,4)', nullable=False, chn_name='1.管理人报酬')
    """1.管理人报酬:"""

    TrusteeExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='TrusteeExpense', column_type='decimal(19,4)', nullable=False, chn_name='2.托管费')
    """2.托管费:"""

    SaleExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='SaleExpense', column_type='decimal(19,4)', nullable=False, chn_name='3.销售服务费')
    """3.销售服务费:"""

    TransactionExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='TransactionExpense', column_type='decimal(19,4)', nullable=False, chn_name='4.交易费用')
    """4.交易费用:"""

    InterestExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='InterestExpense', column_type='decimal(19,4)', nullable=False, chn_name='5.利息支出')
    """5.利息支出:"""

    SoldRepoSecuExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='SoldRepoSecuExpense', column_type='decimal(19,4)', nullable=False, chn_name='其中:卖出回购金融资产支出')
    """其中:卖出回购金融资产支出:"""

    OtherExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='OtherExpense', column_type='decimal(19,4)', nullable=False, chn_name='6.其他费用')
    """6.其他费用:"""

    ExpenseExceptionalItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='ExpenseExceptionalItems', column_type='decimal(19,4)', nullable=False, chn_name='##费用特殊项目')
    """##费用特殊项目:"""

    ExpenseAdjustmentItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='ExpenseAdjustmentItems', column_type='decimal(19,4)', nullable=False, chn_name='##费用调整项目')
    """##费用调整项目:"""

    BulletinType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='BulletinType', column_type='int', nullable=False, chn_name='公告类别')
    """公告类别:公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311，得到公告类别的具体描述：10-发行上市书，20-定期报告，30-业绩快报，50-章程制度，70-临时公告，90-交易所通报，91-交易所临时停(复)牌公告，99-其他。"""

    TotalExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='TotalExpense', column_type='decimal(19,4)', nullable=False, chn_name='费用合计')
    """费用合计:"""

    PastProfitAndLoss: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='PastProfitAndLoss', column_type='decimal(19,4)', nullable=False, chn_name='以前年度损益调整')
    """以前年度损益调整:"""

    ProfitExceptionalItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='ProfitExceptionalItems', column_type='decimal(19,4)', nullable=False, chn_name='##利润特殊项目')
    """##利润特殊项目:"""

    ProfitAdjustmentItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='ProfitAdjustmentItems', column_type='decimal(19,4)', nullable=False, chn_name='##利润调整项目')
    """##利润调整项目:"""

    TotalProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='TotalProfit', column_type='decimal(19,4)', nullable=False, chn_name='利润总额')
    """利润总额:"""

    SpecialFieldRemark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='SpecialFieldRemark', column_type='varchar(1000)', nullable=False, chn_name='特殊字段说明')
    """特殊字段说明:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新日期')
    """更新日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='InnerCode', column_type='int', nullable=True, chn_name='基金内部编码')
    """基金内部编码:基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到基金公司的交易代码、简称等。"""

    StartDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='StartDate', column_type='datetime', nullable=False, chn_name='开始日期')
    """开始日期:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    Mark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_IncomeStatementNew', column_name='Mark', column_type='int', nullable=True, chn_name='调整标志')
    """调整标志:调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM IN (1,2)，得到调整标志的具体描述：1-是，2-否。"""

