# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_FinancialIndex(SQLTableEntity):
    name: str = 'MF_FinancialIndex'
    
    chn_name: str = '公募基金财务指标'
    
    business_unique: str = 'InnerCode,ReportDate'
    
    refresh_freq: str = """半年更新"""
    
    comment: str = """1.本表记录基金各类财务指标，包括基金单位指标、资产状况指标、收益分析指标、费用分析指标、盈利能力指标。
2.历史数据：1998年12月起-至今。
3.信息来源：基金公司披露的定期报告。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    TotalAsset: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='TotalAsset', column_type='decimal(19,4)', nullable=False, chn_name='基金资产总额(元)')
    """基金资产总额(元):"""

    TotalLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='TotalLiability', column_type='decimal(19,4)', nullable=False, chn_name='基金负债总额(元)')
    """基金负债总额(元):"""

    UnrealizedProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='UnrealizedProfit', column_type='decimal(19,4)', nullable=False, chn_name='基金未实现估值增值(元)')
    """基金未实现估值增值(元):"""

    TotalNetAsset: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='TotalNetAsset', column_type='decimal(19,4)', nullable=False, chn_name='基金净资产值(元)')
    """基金净资产值(元):"""

    TotalShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='TotalShares', column_type='decimal(18,4)', nullable=False, chn_name='基金单位总额(元)')
    """基金单位总额(元):"""

    TotalIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='TotalIncome', column_type='decimal(19,4)', nullable=False, chn_name='基金总收入(元)')
    """基金总收入(元):"""

    SecuSpreadIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='SecuSpreadIncome', column_type='decimal(19,4)', nullable=False, chn_name='证券买卖价差收入(元)')
    """证券买卖价差收入(元):证券买卖价差收入＝股票差价收入＋债券差价收入"""

    InvestIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='InvestIncome', column_type='decimal(19,4)', nullable=False, chn_name='投资收益(元)')
    """投资收益(元):投资收益＝债券利息收入＋股利收入"""

    NetProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='NetProfit', column_type='decimal(19,4)', nullable=False, chn_name='本期净收益(元)')
    """本期净收益(元):"""

    RetainedProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='RetainedProfit', column_type='decimal(19,4)', nullable=False, chn_name='期末未分配收益(元)')
    """期末未分配收益(元):"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='InnerCode', column_type='int', nullable=True, chn_name='基金内部编码')
    """基金内部编码:基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    Performance: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='Performance', column_type='decimal(19,4)', nullable=False, chn_name='基金经营业绩(元)')
    """基金经营业绩(元):"""

    RealizedProfitRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='RealizedProfitRatio', column_type='decimal(18,4)', nullable=False, chn_name='已实现收入比率')
    """已实现收入比率:已实现收入比率＝[1－未实现估值增值/（经营业绩＋费用）]×100%"""

    MainIncomeRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='MainIncomeRatio', column_type='decimal(18,4)', nullable=False, chn_name='主营收入比率')
    """主营收入比率:主营收入比率＝（证券买卖价差收入＋投资收益＋未实现利得）/（经营业绩＋费用）×100%"""

    StockInvestIncomeRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='StockInvestIncomeRatio', column_type='decimal(18,6)', nullable=False, chn_name='股票收入比率')
    """股票收入比率:股票收入比率＝（股票差价收入+股息收入＋股票投资估值增值）/（经营业绩＋费用）×100%，其中股票投资估值增值＝（本期股票投资市值－本期股票投资成本）－（上期股票投资市值－上期股票投资成本）"""

    BondInvestIncomeRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='BondInvestIncomeRatio', column_type='decimal(18,6)', nullable=False, chn_name='债券收入比率')
    """债券收入比率:债券收入比率＝（债券差价收入+债券利息收入+债券投资估值增值）/（经营业绩＋费用）×100%,其中债券投资估值增值＝（本期债券投资市值－本期债券投资成本）－（上期债券投资市值－上期债券投资成本）"""

    ManagementFeeProportion: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='ManagementFeeProportion', column_type='decimal(18,6)', nullable=False, chn_name='管理费占总费用的比例')
    """管理费占总费用的比例:"""

    TrustFeeProportion: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='TrustFeeProportion', column_type='decimal(18,6)', nullable=False, chn_name='托管费占总费用的比例')
    """托管费占总费用的比例:"""

    TradeExpenseProportion: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='TradeExpenseProportion', column_type='decimal(18,6)', nullable=False, chn_name='交易费占总费用的比例')
    """交易费占总费用的比例:"""

    OtherExpenseProportion: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='OtherExpenseProportion', column_type='decimal(18,6)', nullable=False, chn_name='其他费用占总费用的比例')
    """其他费用占总费用的比例:"""

    ManagementFeeProfitRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='ManagementFeeProfitRatio', column_type='decimal(18,6)', nullable=False, chn_name='管理费用收益比')
    """管理费用收益比:管理费用收益比=总收益/管理费用＝（经营业绩＋费用）/管理费用"""

    ReportDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='ReportDate', column_type='datetime', nullable=True, chn_name='报告期')
    """报告期:"""

    TrustFeeProfitRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='TrustFeeProfitRatio', column_type='decimal(18,6)', nullable=False, chn_name='托管费用收益比')
    """托管费用收益比:托管费用收益比=总收益/托管费用=（经营业绩＋费用）/托管费用"""

    TradeExpenseProfitRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='TradeExpenseProfitRatio', column_type='decimal(18,6)', nullable=False, chn_name='交易费用收益比')
    """交易费用收益比:交易费用收益比=总收益/交易费用=（经营业绩＋费用）/交易费用"""

    OtherExpenseProfitRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='OtherExpenseProfitRatio', column_type='decimal(18,6)', nullable=False, chn_name='其他费用收益比')
    """其他费用收益比:其他费用收益比=总收益/其他费用=（经营业绩＋费用）/其他费用"""

    TotalExpenseProfitRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='TotalExpenseProfitRatio', column_type='decimal(18,6)', nullable=False, chn_name='总费用收益比')
    """总费用收益比:总费用收益比=总收益/费用=（经营业绩＋费用）/费用"""

    NVYield: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='NVYield', column_type='decimal(18,6)', nullable=False, chn_name='净值收益率')
    """净值收益率:"""

    PerformanceGrowthRate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='PerformanceGrowthRate', column_type='decimal(18,6)', nullable=False, chn_name='经营业绩同比增长率')
    """经营业绩同比增长率:"""

    NVGrowthRate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='NVGrowthRate', column_type='decimal(18,6)', nullable=False, chn_name='本期净值增长率')
    """本期净值增长率:"""

    AccumulatedNVGrowthRate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='AccumulatedNVGrowthRate', column_type='decimal(18,6)', nullable=False, chn_name='累计净值增长率')
    """累计净值增长率:"""

    TotalAssetGrowthRate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='TotalAssetGrowthRate', column_type='decimal(18,6)', nullable=False, chn_name='总资产增长率')
    """总资产增长率:总资产增长率＝（本期总资产/上期总资产－1）×100%"""

    UnrealizedProfitRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='UnrealizedProfitRatio', column_type='decimal(18,6)', nullable=False, chn_name='未实现估值增值收入比率')
    """未实现估值增值收入比率:未实现估值增值收入比率＝（未实现估值增值/基金本期净收益）×100%"""

    UnitNetProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='UnitNetProfit', column_type='decimal(19,4)', nullable=False, chn_name='单位基金净收益(元)')
    """单位基金净收益(元):"""

    StockTradeYield: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='StockTradeYield', column_type='decimal(18,6)', nullable=False, chn_name='股票交易收益率')
    """股票交易收益率:股票交易收益率＝{股票差价收入/[(期初净值＋期末净值)/2]×0.8}×100%"""

    DividendRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='DividendRatio', column_type='decimal(18,6)', nullable=False, chn_name='分红率')
    """分红率:分红率＝（收益分配金额/本期可分配收益）×100%"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新日期')
    """更新日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    UnitDistributableProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='UnitDistributableProfit', column_type='decimal(19,4)', nullable=False, chn_name='单位基金可分配净收益(元)')
    """单位基金可分配净收益(元):"""

    UnitRetainedProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='UnitRetainedProfit', column_type='decimal(19,4)', nullable=False, chn_name='单位基金未分配收益(元)')
    """单位基金未分配收益(元):"""

    UnitNV: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='UnitNV', column_type='decimal(19,4)', nullable=False, chn_name='单位基金净值(元)')
    """单位基金净值(元):"""

    UnitAccumulatedNV: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='UnitAccumulatedNV', column_type='decimal(19,4)', nullable=False, chn_name='单位基金累计净值(元)')
    """单位基金累计净值(元):"""

    DiscountRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FinancialIndex', column_name='DiscountRatio', column_type='decimal(18,4)', nullable=False, chn_name='基金升贴水率')
    """基金升贴水率:"""

