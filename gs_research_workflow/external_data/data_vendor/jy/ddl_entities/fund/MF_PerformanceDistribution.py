# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_PerformanceDistribution(SQLTableEntity):
    name: str = 'MF_PerformanceDistribution'
    
    chn_name: str = '公募基金经营业绩与收益分配'
    
    business_unique: str = 'InnerCode,ReportDate'
    
    refresh_freq: str = """半年更新"""
    
    comment: str = """1.本表记录基金公司披露的定报中基金收入、基金费用、净收益、经营业绩、收益分配等数据。
2.历史数据：1998年12月起-至今。
3.数据来源：基金公司披露的定期报告。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    InvestmentIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='InvestmentIncome', column_type='decimal(19,4)', nullable=False, chn_name='投资收益(元)')
    """投资收益(元):"""

    BondInterestIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='BondInterestIncome', column_type='decimal(19,4)', nullable=False, chn_name='债券利息收入(元)')
    """债券利息收入(元):"""

    ConvertibleInterestIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='ConvertibleInterestIncome', column_type='decimal(19,4)', nullable=False, chn_name='可转换债券利息收入(元)')
    """可转换债券利息收入(元):"""

    DepositInterestIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='DepositInterestIncome', column_type='decimal(19,4)', nullable=False, chn_name='存款利息收入(元)')
    """存款利息收入(元):"""

    DividendIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='DividendIncome', column_type='decimal(19,4)', nullable=False, chn_name='股利收入(元)')
    """股利收入(元):"""

    BoughtSellbackSecuIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='BoughtSellbackSecuIncome', column_type='decimal(19,4)', nullable=False, chn_name='买入返售证券收入(元)')
    """买入返售证券收入(元):"""

    OtherInvestmentIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='OtherInvestmentIncome', column_type='decimal(19,4)', nullable=False, chn_name='其他投资收益(元)')
    """其他投资收益(元):"""

    OtherIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='OtherIncome', column_type='decimal(19,4)', nullable=False, chn_name='其他收入(元)')
    """其他收入(元):"""

    IssuanceFareBalance: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='IssuanceFareBalance', column_type='decimal(19,4)', nullable=False, chn_name='额定发行费用余额(元)')
    """额定发行费用余额(元):"""

    TotalIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='TotalIncome', column_type='decimal(19,4)', nullable=False, chn_name='收入合计(元)')
    """收入合计(元):"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='InnerCode', column_type='int', nullable=True, chn_name='基金内部编码')
    """基金内部编码:基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    MangementFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='MangementFee', column_type='decimal(19,4)', nullable=False, chn_name='基金管理人报酬(元)')
    """基金管理人报酬(元):"""

    PerformanceFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='PerformanceFee', column_type='decimal(19,4)', nullable=False, chn_name='业绩报酬(元)')
    """业绩报酬(元):"""

    TrustFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='TrustFee', column_type='decimal(19,4)', nullable=False, chn_name='基金托管费(元)')
    """基金托管费(元):"""

    SoldRepoSecuExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='SoldRepoSecuExpense', column_type='decimal(19,4)', nullable=False, chn_name='卖出回购证券支出(元)')
    """卖出回购证券支出(元):"""

    InterestExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='InterestExpense', column_type='decimal(19,4)', nullable=False, chn_name='利息支出(元)')
    """利息支出(元):"""

    SaleExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='SaleExpense', column_type='decimal(19,4)', nullable=False, chn_name='销售费用(元)')
    """销售费用(元):"""

    OtherExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='OtherExpense', column_type='decimal(19,4)', nullable=False, chn_name='其他费用(元)')
    """其他费用(元):"""

    AnnualListingFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='AnnualListingFee', column_type='decimal(19,4)', nullable=False, chn_name='上市年费(元)')
    """上市年费(元):"""

    InfoDisclosureFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='InfoDisclosureFee', column_type='decimal(19,4)', nullable=False, chn_name='信息披露费(元)')
    """信息披露费(元):"""

    AuditFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='AuditFee', column_type='decimal(19,4)', nullable=False, chn_name='审计费用(元)')
    """审计费用(元):"""

    ReportDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='ReportDate', column_type='datetime', nullable=True, chn_name='报告期')
    """报告期:"""

    TotalExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='TotalExpense', column_type='decimal(19,4)', nullable=False, chn_name='费用合计(元)')
    """费用合计(元):"""

    PastProfitAndLoss: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='PastProfitAndLoss', column_type='decimal(19,4)', nullable=False, chn_name='(净收益)以前年度损益调整')
    """(净收益)以前年度损益调整:"""

    NetProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='NetProfit', column_type='decimal(19,4)', nullable=False, chn_name='基金净收益(元)')
    """基金净收益(元):"""

    UnrealizedProfitChange: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='UnrealizedProfitChange', column_type='decimal(19,4)', nullable=False, chn_name='未实现估值增值变动数(元)')
    """未实现估值增值变动数(元):"""

    Performance: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='Performance', column_type='decimal(19,4)', nullable=False, chn_name='基金经营业绩(元)')
    """基金经营业绩(元):"""

    RetainedNetProfitAtBegin: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='RetainedNetProfitAtBegin', column_type='decimal(19,4)', nullable=False, chn_name='期初未分配净收益(元)')
    """期初未分配净收益(元):"""

    RetainedProfitBeforeTrans: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='RetainedProfitBeforeTrans', column_type='decimal(19,4)', nullable=False, chn_name='资产移交基准日前未分配收益(元)')
    """资产移交基准日前未分配收益(元):"""

    RetainedProfitAtBegin: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='RetainedProfitAtBegin', column_type='decimal(19,4)', nullable=False, chn_name='期初未分配收益(元)')
    """期初未分配收益(元):"""

    ApplyingBufferMoney: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='ApplyingBufferMoney', column_type='decimal(19,4)', nullable=False, chn_name='本期申购基金单位的损益平准金(元)')
    """本期申购基金单位的损益平准金(元):"""

    ProfitAndLossBufferMoney: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='ProfitAndLossBufferMoney', column_type='decimal(19,4)', nullable=False, chn_name='本期损益平准金(元)')
    """本期损益平准金(元):"""

    SecurityApreadIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='SecurityApreadIncome', column_type='decimal(19,4)', nullable=False, chn_name='证券买卖价差收入(元)')
    """证券买卖价差收入(元):"""

    RedemptionBufferMoney: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='RedemptionBufferMoney', column_type='decimal(19,4)', nullable=False, chn_name='本期赎回基金单位的损益平准金(元)')
    """本期赎回基金单位的损益平准金(元):"""

    DistributableNetProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='DistributableNetProfit', column_type='decimal(19,4)', nullable=False, chn_name='可供分配基金净收益(元)')
    """可供分配基金净收益(元):"""

    DistributedNetProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='DistributedNetProfit', column_type='decimal(19,4)', nullable=False, chn_name='本期已分配基金净收益(元)')
    """本期已分配基金净收益(元):"""

    Others: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='Others', column_type='decimal(19,4)', nullable=False, chn_name='其他(元)')
    """其他(元):"""

    ProfitDistribution: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='ProfitDistribution', column_type='decimal(19,4)', nullable=False, chn_name='收益分配(元)')
    """收益分配(元):"""

    RetainedProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='RetainedProfit', column_type='decimal(19,4)', nullable=False, chn_name='期末基金未分配净收益(元)')
    """期末基金未分配净收益(元):"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新日期')
    """更新日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    StockSpreadIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='StockSpreadIncome', column_type='decimal(19,4)', nullable=False, chn_name='股票差价收入(元)')
    """股票差价收入(元):"""

    BondSpreadIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='BondSpreadIncome', column_type='decimal(19,4)', nullable=False, chn_name='债券差价收入(元)')
    """债券差价收入(元):"""

    ConvertibleSpreadIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='ConvertibleSpreadIncome', column_type='decimal(19,4)', nullable=False, chn_name='可转换债券买卖价差收入(元)')
    """可转换债券买卖价差收入(元):"""

    WarrantSpreadIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='WarrantSpreadIncome', column_type='decimal(19,4)', nullable=False, chn_name='权证买卖价差收入(元)')
    """权证买卖价差收入(元):"""

    OtherSpreadIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PerformanceDistribution', column_name='OtherSpreadIncome', column_type='decimal(19,4)', nullable=False, chn_name='其他价差收入(元)')
    """其他价差收入(元):"""

