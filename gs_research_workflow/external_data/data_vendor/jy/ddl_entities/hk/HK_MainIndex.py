# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_MainIndex(SQLTableEntity):
    name: str = 'HK_MainIndex'
    
    chn_name: str = '港股主要财务分析指标'
    
    business_unique: str = 'CompanyCode,BeginDate,EndDate,PeriodMark'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.根据报告期公布的财务科目数据衍生而来的每股指标，以及反映公司盈利、偿债、成长、营运、分红、现金流、资本结构等能力的指标。
2.若某个报告期的数据有多次调整，则该表展示最新合并调整数据；若某报告期暂未披露调整后数据，则展示调整前的合并数据。
3.该表中各财务科目的单位均为人民币元。若报告期公布的记帐本位币不是人民币，则按公告截止日期汇率转换为人民币。
4.对于季度报告，上市公司可能只披露了损益表，而未披露资产负债表和现金流量表。这会导致财务指标表中，相应报告期的基本每股收益，毛利率等指标有值，而每股净资产，存货周转率等指标为空值。
5.对于招股说明书，由于上市之前年度公司的总股本数据通常不正常（无股本或股本很小），或导致上市前年度的每股收益，每股净资产等每股指标为空值，或数值畸大。
6.由于公司毛利中可能大部分来自于原材料价值变动等项目，可能会因此导致毛利率指标畸大。
7.数据范围：1998年至今。
8.数据来源：港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    NetAssetPS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='NetAssetPS', column_type='decimal(18,6)', nullable=False, chn_name='每股净资产')
    """每股净资产:每股净资产=归属于母公司股东权益/当期发行在外普通股"""

    OperCashFlowPS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='OperCashFlowPS', column_type='decimal(18,6)', nullable=False, chn_name='每股经营现金净流量')
    """每股经营现金净流量:每股经营现金净流量=经营活动产生的现金流量净额/当期发行在外普通股"""

    CashFlowPS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='CashFlowPS', column_type='decimal(18,6)', nullable=False, chn_name='每股现金流量净额')
    """每股现金流量净额:每股现金净流量=现金及现金等价物净增加额/当期发行在外普通股"""

    MainIncomePS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='MainIncomePS', column_type='decimal(18,6)', nullable=False, chn_name='每股营业收入')
    """每股营业收入:每股营业收入=总收入/当期发行在外普通股"""

    DividendPS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='DividendPS', column_type='decimal(18,6)', nullable=False, chn_name='每股派息')
    """每股派息:每股派利=(每股股息+每股特别股息)"""

    GrossIncomeRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='GrossIncomeRatio', column_type='decimal(18,6)', nullable=False, chn_name='销售毛利率(%)')
    """销售毛利率(%):销售毛利率=（毛利/总收入）*100%；若“总收入”小于等于0或为NULL，则该指标不计算，以NULL列示。"""

    OperatingProfitRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='OperatingProfitRatio', column_type='decimal(18,6)', nullable=False, chn_name='经营利润率(%)')
    """经营利润率(%):经营利润率=（营运溢利/总收入）*100%；若“总收入”小于等于0或为NULL，则该指标不计算，以NULL列示。"""

    NetProfitRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='NetProfitRatio', column_type='decimal(18,6)', nullable=False, chn_name='销售净利率(%)')
    """销售净利率(%):销售净利率=（净利润/总收入）*100%；若“总收入”小于等于0或为NULL，则该指标不计算，以NULL列示。"""

    EarningBeforeTaxRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='EarningBeforeTaxRatio', column_type='decimal(18,6)', nullable=False, chn_name='税前利润率(%)')
    """税前利润率(%):税前利润率=（税前利润/总收入）*100%；若“总收入”小于等于0或为NULL，则该指标不计算，以NULL列示。"""

    ROEWeighted: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='ROEWeighted', column_type='decimal(18,6)', nullable=False, chn_name='净资产收益率(ROE)(%)')
    """净资产收益率(ROE)(%):平均净资产收益率（ROE）=[归属于母公司的净利润*2/（期初归属于母公司的股东权益+期末归属于母公司的股东权益）]*100%；若“（期初归属于母公司的股东权益+期末归属于母公司的股东权益）”小于等于0或为NULL，则该指标不计算，以NULL列示。"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到港股的交易代码、简称等。"""

    ROA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='ROA', column_type='decimal(18,6)', nullable=False, chn_name='总资产净利率(%)')
    """总资产净利率(%):总资产净利率（ROA）=[税后利润——持续经营业务*2/（期初总资产+期末总资产）]*100%"""

    OperProfitToTP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='OperProfitToTP', column_type='decimal(18,6)', nullable=False, chn_name='营业利润／利润总额(%)')
    """营业利润／利润总额(%):营业利润／利润总额=（营业溢利／税前利润）*100%；若“税前利润”小于等于0或为NULL，则该指标不计算，以NULL列示。"""

    TaxToTP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='TaxToTP', column_type='decimal(18,6)', nullable=False, chn_name='税项／利润总额(%)')
    """税项／利润总额(%):税项／利润总额=（税项／税前利润）*100%；若“税前利润”小于等于0或为NULL，则该指标不计算，以NULL列示。"""

    OperCashToTP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='OperCashToTP', column_type='decimal(18,6)', nullable=False, chn_name='经营活动产生的现金流量净额／营业收入(%)')
    """经营活动产生的现金流量净额／营业收入(%):经营活动产生的现金流量净额／营业收入=（经营活动产生的现金净流量／总收入）*100%；若“总收入”小于等于0或为NULL，则该指标不计算，以NULL列示。"""

    DebtAssetsRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='DebtAssetsRatio', column_type='decimal(18,6)', nullable=False, chn_name='资产负债率(%)')
    """资产负债率(%):资产负债率=（负债合计/总资产）*100%"""

    EquityMultipler: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='EquityMultipler', column_type='decimal(18,6)', nullable=False, chn_name='权益乘数')
    """权益乘数:权益乘数=总资产/归属于母公司的权益合计；若“归属于母公司的权益合计”小于等于0或为NULL，则该指标不计算，以NULL列示。"""

    DebtEquityRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='DebtEquityRatio', column_type='decimal(18,6)', nullable=False, chn_name='产权比率(%)')
    """产权比率(%):产权比率=（负债总额/所有者权益总额）*100%；若“所有者权益总额”小于等于0或为NULL，则该指标不计算，以NULL列示。"""

    CurrentAssetsToTA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='CurrentAssetsToTA', column_type='decimal(18,6)', nullable=False, chn_name='流动资产／总资产(%)')
    """流动资产／总资产(%):流动资产／总资产=（流动资产／总资产）*100%"""

    NonCurrentAssetsToTA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='NonCurrentAssetsToTA', column_type='decimal(18,6)', nullable=False, chn_name='非流动资产／总资产(%)')
    """非流动资产／总资产(%):非流动资产／总资产=（非流动资产／总资产）*100%"""

    CurrentLiabilityToTL: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='CurrentLiabilityToTL', column_type='decimal(18,6)', nullable=False, chn_name='流动负债／负债合计(%)')
    """流动负债／负债合计(%):流动负债／负债合计=（流动负债／负债合计）*100%"""

    BeginDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='BeginDate', column_type='datetime', nullable=True, chn_name='开始日期')
    """开始日期:"""

    NonCurrentLiabilityToTL: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='NonCurrentLiabilityToTL', column_type='decimal(18,6)', nullable=False, chn_name='非流动负债／负债合计(%)')
    """非流动负债／负债合计(%):非流动负债／负债合计=（非流动负债／负债合计）*100%"""

    CurrentRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='CurrentRatio', column_type='decimal(18,6)', nullable=False, chn_name='流动比率')
    """流动比率:流动比率=流动资产/流动负债"""

    QuickRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='QuickRatio', column_type='decimal(18,6)', nullable=False, chn_name='速动比率')
    """速动比率:速动比率=（流动资产-存货）/流动负债"""

    OperProfitToCL: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='OperProfitToCL', column_type='decimal(18,6)', nullable=False, chn_name='营业利润／流动负债')
    """营业利润／流动负债:营业利润／流动负债=营业溢利／流动负债"""

    OperCashFlowToCL: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='OperCashFlowToCL', column_type='decimal(18,6)', nullable=False, chn_name='经营活动产生的现金流量净额／流动负债')
    """经营活动产生的现金流量净额／流动负债:经营活动产生的现金流量净额／流动负债=经营活动产生的现金流量净额／流动负债"""

    SEWithoutMIToTL: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='SEWithoutMIToTL', column_type='decimal(18,6)', nullable=False, chn_name='归属母公司股东的权益／负债合计')
    """归属母公司股东的权益／负债合计:归属母公司股东的权益／负债合计=（归属母公司股东的权益／负债合计）*100%"""

    OperCashFlowToTL: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='OperCashFlowToTL', column_type='decimal(18,6)', nullable=False, chn_name='经营活动产生的现金流量净额／负债合计')
    """经营活动产生的现金流量净额／负债合计:经营活动产生的现金流量净额／负债合计=经营活动产生的现金流量净额／负债合计"""

    OPToTL: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='OPToTL', column_type='decimal(18,6)', nullable=False, chn_name='营业利润／负债合计')
    """营业利润／负债合计:营业利润／负债合计=（营业利润／负债合计）"""

    InventoryTRate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='InventoryTRate', column_type='decimal(18,6)', nullable=False, chn_name='存货周转率')
    """存货周转率:存货周转率=销售成本*2/（期初存货+期末存货）"""

    CurrentAssetsTRate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='CurrentAssetsTRate', column_type='decimal(18,6)', nullable=False, chn_name='流动资产周转率')
    """流动资产周转率:流动资产周转率=总收入*2/（期初流动资产+期末流动资产）"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    FixedAssetTRate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='FixedAssetTRate', column_type='decimal(18,6)', nullable=False, chn_name='固定资产周转率')
    """固定资产周转率:固定资产周转率=总收入*2/（期初物业厂房与设备+期末物业厂房与设备）"""

    TotalAssetTRate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='TotalAssetTRate', column_type='decimal(18,6)', nullable=False, chn_name='总资产周转率')
    """总资产周转率:总资产周转率=总收入*2/（期初总资产+期末总资产）"""

    OperatingRevenueGR1Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='OperatingRevenueGR1Y', column_type='decimal(18,6)', nullable=False, chn_name='营业收入(年增长率)(%)')
    """营业收入(年增长率)(%):营业收入（近1年增长率）=[（所选年度年报营业收入-前推一年年报的营业收入）/|前推一年年报的营业收入|]*100%"""

    OperatingRevenueGR3Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='OperatingRevenueGR3Y', column_type='decimal(18,6)', nullable=False, chn_name='营业收入(近3年增长率)(%)')
    """营业收入(近3年增长率)(%):营业收入（近3年增长率）=[（最近一年年报营业收入-前推三年年报的营业收入）/|前推三年年报的营业收入|]*100%"""

    GrossIncomeGR1Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='GrossIncomeGR1Y', column_type='decimal(18,6)', nullable=False, chn_name='毛利(年增长率)(%)')
    """毛利(年增长率)(%):毛利（近1年增长率）=[（所选年度年报毛利-前推一年年报的毛利）/|前推一年年报的毛利|]*100%"""

    GrossIncomeGR3Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='GrossIncomeGR3Y', column_type='decimal(18,6)', nullable=False, chn_name='毛利(近3年增长率)(%)')
    """毛利(近3年增长率)(%):毛利（近3年增长率）=[（最近一年年报毛利-前推三年年报的毛利）/|前推三年年报的毛利|]*100%"""

    OperProfitGR1Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='OperProfitGR1Y', column_type='decimal(18,6)', nullable=False, chn_name='营业利润(年增长率)(%)')
    """营业利润(年增长率)(%):营业利润（近1年增长率）=[（所选年度年报营业利润-前推一年年报的营业利润）/|前推一年年报的营业利润|]*100%"""

    OperProfitGR3Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='OperProfitGR3Y', column_type='decimal(18,6)', nullable=False, chn_name='营业利润(近3年增长率)(%)')
    """营业利润(近3年增长率)(%):营业利润（近3年增长率）=[（最近一年年报营业利润-前推三年年报的营业利润）/|前推三年年报的营业利润|]*100%"""

    EBTGR1Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='EBTGR1Y', column_type='decimal(18,6)', nullable=False, chn_name='税前利润(年增长率)(%)')
    """税前利润(年增长率)(%):税前利润（近1年增长率）=[（所选年度年报税前利润-前推一年年报的税前利润）/|前推一年年报的税前利润|]*100%"""

    EBTGR3Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='EBTGR3Y', column_type='decimal(18,6)', nullable=False, chn_name='税前利润(近3年增长率)(%)')
    """税前利润(近3年增长率)(%):税前利润（近3年增长率）=[（最近一年年报税前利润-前推三年年报的税前利润）/|前推三年年报的税前利润|]*100%"""

    PeriodMark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='PeriodMark', column_type='int', nullable=True, chn_name='日期标志')
    """日期标志:日期标志(PeriodMark)与(CT_SystemConst)表中的DM字段关联，令LB = 1314，得到日期标志的具体描述：1-1个月，2-2个月，3-3个月，4-4个月，5-5个月，6-半年度，7-7个月，8-8个月，9-9个月，10-10个月，11-11个月，12-年度，13-13个月，14-14个月，15-15个月，16-16个月，17-17个..."""

    NetProfitGR1Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='NetProfitGR1Y', column_type='decimal(18,6)', nullable=False, chn_name='净利润(年增长率)(%)')
    """净利润(年增长率)(%):净利润（近1年增长率）=[（所选年度年报净利润-前推一年年报的净利润）/|前推一年年报的净利润|]*100%"""

    NetProfitGR3Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='NetProfitGR3Y', column_type='decimal(18,6)', nullable=False, chn_name='净利润(近3年增长率)(%)')
    """净利润(近3年增长率)(%):净利润（近3年增长率）=[（最近一年年报净利润-前推三年年报的净利润）/|前推三年年报的净利润|]*100%"""

    NPParentCompanyGR1Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='NPParentCompanyGR1Y', column_type='decimal(18,6)', nullable=False, chn_name='归属母公司股东的净利润(年增长率)(%)')
    """归属母公司股东的净利润(年增长率)(%):归属母公司股东的净利润（近1年增长率）=[（所选年度年报归属母公司股东的净利润-前推一年年报的归属母公司股东的净利润）/|前推一年年报的归属母公司股东的净利润|]*100%"""

    NPParentCompanyGR3Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='NPParentCompanyGR3Y', column_type='decimal(18,6)', nullable=False, chn_name='归属母公司股东的净利润(近3年增长率)(%)')
    """归属母公司股东的净利润(近3年增长率)(%):归属母公司股东的净利润（近3年增长率）=[（最近一年年报归属母公司股东的净利润-前推三年年报的归属母公司股东的净利润）/|前推三年年报的归属母公司股东的净利润|]*100%"""

    TotalAssetGR1Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='TotalAssetGR1Y', column_type='decimal(18,6)', nullable=False, chn_name='资产总计(年增长率)(%)')
    """资产总计(年增长率)(%):资产总计（近1年增长率）=[（所选年度年报资产总计-前推一年年报的资产总计）/|前推一年年报的资产总计|]*100%"""

    TotalAssetGR3Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='TotalAssetGR3Y', column_type='decimal(18,6)', nullable=False, chn_name='资产总计(近3年增长率)(%)')
    """资产总计(近3年增长率)(%):资产总计（近3年增长率）=[（最近一年年报资产总计-前推三年年报的资产总计）/|前推三年年报的资产总计|]*100%"""

    SEWithoutMIGR1Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='SEWithoutMIGR1Y', column_type='decimal(18,6)', nullable=False, chn_name='归属母公司股东的权益(年增长率)(%)')
    """归属母公司股东的权益(年增长率)(%):归属母公司股东的权益（近1年增长率）=[（所选年度年报归属母公司股东的权益-前推一年年报的归属母公司股东的权益）/|前推一年年报的归属母公司股东的权益|]*100%"""

    SEWithoutMIGR3Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='SEWithoutMIGR3Y', column_type='decimal(18,6)', nullable=False, chn_name='归属母公司股东的权益(近3年增长率)(%)')
    """归属母公司股东的权益(近3年增长率)(%):归属母公司股东的权益（近3年增长率）=[（最近一年年报归属母公司股东的权益-前推三年年报的归属母公司股东的权益）/|前推三年年报的归属母公司股东的权益|]*100%"""

    EquityGR1Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='EquityGR1Y', column_type='decimal(18,6)', nullable=False, chn_name='股东权益(年增长率)(%)')
    """股东权益(年增长率)(%):股东权益（近1年增长率）=[（所选年度年报股东权益-前推一年年报股东权益）/|前推一年年报股东权益|]*100%"""

    EquityGR3Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='EquityGR3Y', column_type='decimal(18,6)', nullable=False, chn_name='股东权益(近3年增长率)(%)')
    """股东权益(近3年增长率)(%):股东权益（近3年增长率）=[（最近一年年报股东权益-前推三年年报的股东权益）/|前推三年年报的股东权益|]*100%"""

    PeriodDesc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='PeriodDesc', column_type='varchar(20)', nullable=False, chn_name='日期标志说明')
    """日期标志说明:"""

    LiabilityGR1Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='LiabilityGR1Y', column_type='decimal(18,6)', nullable=False, chn_name='负债合计(年增长率)(%)')
    """负债合计(年增长率)(%):负债总计（近1年增长率）=[（所选年度年报负债总计-前推一年年报的负债总计）/|前推一年年报的负债总计|]*100%"""

    LiabilityGR3Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='LiabilityGR3Y', column_type='decimal(18,6)', nullable=False, chn_name='负债合计(近3年增长率)(%)')
    """负债合计(近3年增长率)(%):负债总计（近3年增长率）=[（最近一年年报负债总计-前推三年年报的负债总计）/|前推三年年报的负债总计|]*100%"""

    BasicEPS1Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='BasicEPS1Y', column_type='decimal(18,6)', nullable=False, chn_name='基本每股收益(年增长率)(%)')
    """基本每股收益(年增长率)(%):基本每股收益（近1年增长率）=[（所选年度年报基本每股收益-前推一年年报的基本每股收益）/|前推一年年报的基本每股收益|]*100%"""

    BasicEPS3Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='BasicEPS3Y', column_type='decimal(18,6)', nullable=False, chn_name='基本每股收益(近3年增长率)(%)')
    """基本每股收益(近3年增长率)(%):基本每股收益（近3年增长率）=[（最近一年年报基本每股收益-前推三年年报的基本每股收益）/|前推三年年报的基本每股收益|]*100%"""

    NetAssetPS1Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='NetAssetPS1Y', column_type='decimal(18,6)', nullable=False, chn_name='每股净资产(年增长率)(%)')
    """每股净资产(年增长率)(%):每股净资产（近1年增长率）=[（所选年度年报每股净资产-前推一年年报的每股净资产）/|前推一年年报的每股净资产|]*100%"""

    NetAssetPS3Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='NetAssetPS3Y', column_type='decimal(18,6)', nullable=False, chn_name='每股净资产(近3年增长率)(%)')
    """每股净资产(近3年增长率)(%):每股净资产（近3年增长率）=[（最近一年年报每股净资产-前推三年年报的每股净资产）/|前推三年年报的每股净资产|]*100%"""

    DividendRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='DividendRatio', column_type='decimal(18,6)', nullable=False, chn_name='派息比率(%)')
    """派息比率(%):派息比率=∑（该次现金分红）/归属于母公司的净利润]*100%"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='修改日期')
    """修改日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    FinancialYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='FinancialYear', column_type='datetime', nullable=False, chn_name='财政年度')
    """财政年度:"""

    BasicEPS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='BasicEPS', column_type='decimal(18,6)', nullable=False, chn_name='基本每股收益')
    """基本每股收益:基本每股收益：取公告值，如果财务报表中未列报该项目，该项目以空值展示"""

    DilutedEPS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_MainIndex', column_name='DilutedEPS', column_type='decimal(18,6)', nullable=False, chn_name='稀释每股收益')
    """稀释每股收益:稀释每股收益：取公告值，如果财务报表中未列报该项目，该项目以空值展示"""

