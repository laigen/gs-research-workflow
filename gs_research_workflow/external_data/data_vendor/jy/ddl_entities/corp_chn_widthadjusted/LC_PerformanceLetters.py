# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_PerformanceLetters(SQLTableEntity):
    name: str = 'LC_PerformanceLetters'
    
    chn_name: str = '业绩快报'
    
    business_unique: str = 'CompanyCode,EndDate,Mark,PeriodMark'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.收录上市公司在业绩快报中披露的主要财务数据和指标，包括本期数据、去年同期或本期期初数据以及同比或与期初比数值等内容。
2.数据范围：2004-12-31至今
3.信息来源：业绩快报等"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    OperatingProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='OperatingProfit', column_type='decimal(19,4)', nullable=False, chn_name='营业利润(元)')
    """营业利润(元):"""

    TotalProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='TotalProfit', column_type='decimal(19,4)', nullable=False, chn_name='利润总额(元)')
    """利润总额(元):"""

    NPParentCompanyOwners: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='NPParentCompanyOwners', column_type='decimal(19,4)', nullable=False, chn_name='归属母公司净利润(元)')
    """归属母公司净利润(元):"""

    NetProfitCut: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='NetProfitCut', column_type='decimal(19,4)', nullable=False, chn_name='扣除非经常性损益后净利润(元)')
    """扣除非经常性损益后净利润(元):"""

    NetOperateCashFlow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='NetOperateCashFlow', column_type='decimal(19,4)', nullable=False, chn_name='经营活动现金流量净额(元)')
    """经营活动现金流量净额(元):"""

    TotalAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='TotalAssets', column_type='decimal(19,4)', nullable=False, chn_name='总资产(元)')
    """总资产(元):"""

    SEWithoutMI: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='SEWithoutMI', column_type='decimal(19,4)', nullable=False, chn_name='归属母公司股东权益(元)')
    """归属母公司股东权益(元):"""

    TotalShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='TotalShares', column_type='decimal(19,4)', nullable=False, chn_name='总股本(股)')
    """总股本(股):"""

    BasicEPS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='BasicEPS', column_type='decimal(19,4)', nullable=False, chn_name='基本每股收益')
    """基本每股收益:"""

    EPSWeighted: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='EPSWeighted', column_type='decimal(19,4)', nullable=False, chn_name='每股收益(加权)(元)')
    """每股收益(加权)(元):"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。"""

    EPSCut: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='EPSCut', column_type='decimal(19,4)', nullable=False, chn_name='每股收益(扣除)(元)')
    """每股收益(扣除)(元):"""

    EPSCutWeighted: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='EPSCutWeighted', column_type='decimal(19,4)', nullable=False, chn_name='每股收益(扣除加权)(元)')
    """每股收益(扣除加权)(元):"""

    ROE: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='ROE', column_type='decimal(18,6)', nullable=False, chn_name='净资产收益率(摊薄)(%)')
    """净资产收益率(摊薄)(%):"""

    ROEWeighted: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='ROEWeighted', column_type='decimal(18,6)', nullable=False, chn_name='净资产收益率(加权)(%)')
    """净资产收益率(加权)(%):"""

    ROECut: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='ROECut', column_type='decimal(18,6)', nullable=False, chn_name='净资产收益率(扣除摊薄)(%)')
    """净资产收益率(扣除摊薄)(%):"""

    ROECutWeighted: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='ROECutWeighted', column_type='decimal(18,6)', nullable=False, chn_name='净资产收益率(扣除加权)(%)')
    """净资产收益率(扣除加权)(%):"""

    NetOperateCashFlowPS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='NetOperateCashFlowPS', column_type='decimal(19,4)', nullable=False, chn_name='每股经营活动现金流量净额(元)')
    """每股经营活动现金流量净额(元):"""

    NetAssetPS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='NetAssetPS', column_type='decimal(19,4)', nullable=False, chn_name='每股净资产(元)')
    """每股净资产(元):"""

    OperatingRevenueLYCP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='OperatingRevenueLYCP', column_type='decimal(19,4)', nullable=False, chn_name='T-1主营业务收入(元)')
    """T-1主营业务收入(元):"""

    GrossProfitLYCP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='GrossProfitLYCP', column_type='decimal(19,4)', nullable=False, chn_name='T-1主营业务利润(元)')
    """T-1主营业务利润(元):"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    OperatingProfitLYCP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='OperatingProfitLYCP', column_type='decimal(19,4)', nullable=False, chn_name='T-1营业利润(元)')
    """T-1营业利润(元):"""

    TotalProfitLYCP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='TotalProfitLYCP', column_type='decimal(19,4)', nullable=False, chn_name='T-1利润总额(元)')
    """T-1利润总额(元):"""

    NPParentCompanyOwnersLYCP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='NPParentCompanyOwnersLYCP', column_type='decimal(19,4)', nullable=False, chn_name='T-1归属母公司净利润(元)')
    """T-1归属母公司净利润(元):"""

    NetProfitCutLYCP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='NetProfitCutLYCP', column_type='decimal(19,4)', nullable=False, chn_name='T-1扣除非经常性损益后净利润(元)')
    """T-1扣除非经常性损益后净利润(元):"""

    NetOperateCashFlowLYCP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='NetOperateCashFlowLYCP', column_type='decimal(19,4)', nullable=False, chn_name='T-1经营活动现金流量净额(元)')
    """T-1经营活动现金流量净额(元):"""

    TotalAssetsLY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='TotalAssetsLY', column_type='decimal(19,4)', nullable=False, chn_name='T-1年末总资产(元)')
    """T-1年末总资产(元):"""

    SEWithoutMILY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='SEWithoutMILY', column_type='decimal(19,4)', nullable=False, chn_name='T-1年末归属母公司股东权益(元)')
    """T-1年末归属母公司股东权益(元):"""

    BasicEPSLYCP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='BasicEPSLYCP', column_type='decimal(19,4)', nullable=False, chn_name='T-1每股收益(摊薄)(元)')
    """T-1每股收益(摊薄)(元):"""

    EPSWeightedLYCP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='EPSWeightedLYCP', column_type='decimal(19,4)', nullable=False, chn_name='T-1每股收益(加权)(元)')
    """T-1每股收益(加权)(元):"""

    EPSCutLYCP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='EPSCutLYCP', column_type='decimal(19,4)', nullable=False, chn_name='T-1每股收益(扣除)(元)')
    """T-1每股收益(扣除)(元):"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='InfoSource', column_type='varchar(100)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    EPSCutWeightedLYCP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='EPSCutWeightedLYCP', column_type='decimal(19,4)', nullable=False, chn_name='T-1每股收益(扣除加权)(元)')
    """T-1每股收益(扣除加权)(元):"""

    ROELYCP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='ROELYCP', column_type='decimal(18,6)', nullable=False, chn_name='T-1净资产收益率(摊薄)(%)')
    """T-1净资产收益率(摊薄)(%):"""

    ROEWeightedLYCP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='ROEWeightedLYCP', column_type='decimal(18,6)', nullable=False, chn_name='T-1净资产收益率(加权)(%)')
    """T-1净资产收益率(加权)(%):"""

    ROECutLYCP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='ROECutLYCP', column_type='decimal(18,6)', nullable=False, chn_name='T-1净资产收益率(扣除摊薄)(%)')
    """T-1净资产收益率(扣除摊薄)(%):"""

    ROECutWeightedLYCP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='ROECutWeightedLYCP', column_type='decimal(18,6)', nullable=False, chn_name='T-1净资产收益率(扣除加权)(%)')
    """T-1净资产收益率(扣除加权)(%):"""

    NetOperateCashFlowPSLYCP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='NetOperateCashFlowPSLYCP', column_type='decimal(19,4)', nullable=False, chn_name='T-1每股经营活动现金流量净额(元)')
    """T-1每股经营活动现金流量净额(元):"""

    NetAssetPSLY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='NetAssetPSLY', column_type='decimal(19,4)', nullable=False, chn_name='T-1年末每股净资产(元)')
    """T-1年末每股净资产(元):"""

    OperatingRevenueYOY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='OperatingRevenueYOY', column_type='decimal(18,6)', nullable=False, chn_name='主营业务收入同比(%)')
    """主营业务收入同比(%):"""

    GrossProfitYOY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='GrossProfitYOY', column_type='decimal(18,6)', nullable=False, chn_name='主营业务利润同比(%)')
    """主营业务利润同比(%):"""

    OperatingProfitYOY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='OperatingProfitYOY', column_type='decimal(18,6)', nullable=False, chn_name='营业利润同比(%)')
    """营业利润同比(%):"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    TotalProfitYOY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='TotalProfitYOY', column_type='decimal(18,6)', nullable=False, chn_name='利润总额同比(%)')
    """利润总额同比(%):"""

    NPParentCompanyOwnersYOY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='NPParentCompanyOwnersYOY', column_type='decimal(18,6)', nullable=False, chn_name='归属母公司净利润同比(%)')
    """归属母公司净利润同比(%):"""

    NetProfitCutYOY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='NetProfitCutYOY', column_type='decimal(18,6)', nullable=False, chn_name='扣除非经常性损益后净利润同比(%)')
    """扣除非经常性损益后净利润同比(%):"""

    NetOperateCashFlowYOY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='NetOperateCashFlowYOY', column_type='decimal(18,6)', nullable=False, chn_name='经营活动现金流量净额同比(%)')
    """经营活动现金流量净额同比(%):"""

    TotalAssetsToOpening: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='TotalAssetsToOpening', column_type='decimal(18,6)', nullable=False, chn_name='总资产较期初比(%)')
    """总资产较期初比(%):"""

    SEWithoutMIToOpening: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='SEWithoutMIToOpening', column_type='decimal(18,6)', nullable=False, chn_name='归属母公司股东权益较期初比(%)')
    """归属母公司股东权益较期初比(%):"""

    BasicEPSYOY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='BasicEPSYOY', column_type='decimal(18,6)', nullable=False, chn_name='每股收益(摊薄)同比(%)')
    """每股收益(摊薄)同比(%):"""

    EPSWeightedYOY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='EPSWeightedYOY', column_type='decimal(18,6)', nullable=False, chn_name='每股收益(加权)同比(%)')
    """每股收益(加权)同比(%):"""

    EPSCutYOY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='EPSCutYOY', column_type='decimal(18,6)', nullable=False, chn_name='每股收益(扣除)同比(%)')
    """每股收益(扣除)同比(%):"""

    EPSCutWeightedYOY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='EPSCutWeightedYOY', column_type='decimal(18,6)', nullable=False, chn_name='每股收益(扣除加权)同比(%)')
    """每股收益(扣除加权)同比(%):"""

    Mark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='Mark', column_type='int', nullable=True, chn_name='合并调整标志')
    """合并调整标志:合并调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1511，得到合并调整标志的具体描述：1-合并调整，2-合并未调整，3-母公司调整，4-母公司未调整，5-专项合并调整，6-专项合并未调整。"""

    ROEYOY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='ROEYOY', column_type='decimal(18,6)', nullable=False, chn_name='净资产收益率(摊薄)同比(%)')
    """净资产收益率(摊薄)同比(%):"""

    ROEWeightedYOY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='ROEWeightedYOY', column_type='decimal(18,6)', nullable=False, chn_name='净资产收益率(加权)同比(%)')
    """净资产收益率(加权)同比(%):"""

    ROECutYOY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='ROECutYOY', column_type='decimal(18,6)', nullable=False, chn_name='净资产收益率(扣除摊薄)同比(%)')
    """净资产收益率(扣除摊薄)同比(%):"""

    ROECutWeightedYOY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='ROECutWeightedYOY', column_type='decimal(18,6)', nullable=False, chn_name='净资产收益率(扣除加权)同比(%)')
    """净资产收益率(扣除加权)同比(%):"""

    NetOperateCashFlowPSYOY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='NetOperateCashFlowPSYOY', column_type='decimal(18,6)', nullable=False, chn_name='每股经营活动现金流量净额同比(%)')
    """每股经营活动现金流量净额同比(%):"""

    NetAssetPSToOpening: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='NetAssetPSToOpening', column_type='decimal(18,6)', nullable=False, chn_name='每股净资产较期初比(%)')
    """每股净资产较期初比(%):"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新日期')
    """更新日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    PeriodMark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='PeriodMark', column_type='int', nullable=True, chn_name='日期标志')
    """日期标志:日期标志(PeriodMark)与(CT_SystemConst)表中的DM字段关联，令LB = 1074，得到日期标志的具体描述：1-月份，2-季度，3-期末累计，4-当月及累计，5-日，6-周，7-旬，8-半月，9-年度，11-上年同月，12-上年同期，13-上年同季，14-期末，21-上月=100，22-2005年=100，23-2005年=100（季..."""

    OperatingRevenue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='OperatingRevenue', column_type='decimal(19,4)', nullable=False, chn_name='营业收入or主营业务收入(元)')
    """营业收入or主营业务收入(元):营业收入or主营业务收入（GrossProfit）：若某条记录中，“主营业务利润”字段下有值，则该记录中的本字段下收录的为“主营业务收入”数值；否则，本字段收录“营业收入”数值。"""

    GrossProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceLetters', column_name='GrossProfit', column_type='decimal(19,4)', nullable=False, chn_name='主营业务利润(元)')
    """主营业务利润(元):"""

