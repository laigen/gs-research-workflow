# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_PerformanceForecast(SQLTableEntity):
    name: str = 'LC_PerformanceForecast'
    
    chn_name: str = '业绩预告'
    
    business_unique: str = 'CompanyCode,InfoPublDate,EndDate,ForcastType,ForecastObject'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.收录上市公司对未来报告期本公司业绩的预计情况，包括业绩预计类型、预计内容、具体预计值等，并收录了实际指标和研究员的一致性预测值。
2.数据范围：2001-12-31至今
3.信息来源：上市公司公告"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceForecast', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    EGrowthRateFloor: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceForecast', column_name='EGrowthRateFloor', column_type='decimal(18,8)', nullable=False, chn_name='预计幅度起始(披露)(%)')
    """预计幅度起始(披露)(%):预计幅度起始(披露)(%)：为公告原始披露数据。"""

    EGrowRateFloorC: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceForecast', column_name='EGrowRateFloorC', column_type='decimal(18,8)', nullable=False, chn_name='预计幅度起始(计算)(%)')
    """预计幅度起始(计算)(%):预计幅度起始（计算）（%）（EGrowRateFloorC）：若没有披露预计幅度，而披露净利润预计值，则做计算。当ABS(预计利润起始-上年同期净利润）<ABS(预计利润截止-上年同期净利润）时，预计幅度起始（计算）（%）=（预计利润起始-上年同期净利润）/|上年同期净利润|*100，否则取（预计利润截止-上年同期净利润）/|上年同期净利润|*100。"""

    EGrowthRateCeiling: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceForecast', column_name='EGrowthRateCeiling', column_type='decimal(18,8)', nullable=False, chn_name='预计幅度截止(披露)(%)')
    """预计幅度截止(披露)(%):预计幅度截止(披露)(%)：为公告原始披露数据。"""

    EGrowthRateCeilC: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceForecast', column_name='EGrowthRateCeilC', column_type='decimal(18,8)', nullable=False, chn_name='预计幅度截止(计算)(%)')
    """预计幅度截止(计算)(%):预计幅度截止（计算）（%）（EGrowthRateCeilC）：若没有披露预计幅度，而披露净利润预计值，则做计算。当ABS(预计利润起始-上年同期净利润）<ABS(预计利润截止-上年同期净利润）时，预计幅度截止（计算）（%）=（预计利润截止-上年同期净利润）/|上年同期净利润|*100，否则取（预计利润起始-上年同期净利润）/|上年同期净利润|*100。"""

    EEarningFloor: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceForecast', column_name='EEarningFloor', column_type='decimal(19,4)', nullable=False, chn_name='预计收入起始(元)')
    """预计收入起始(元):"""

    EEarningCeiling: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceForecast', column_name='EEarningCeiling', column_type='decimal(19,4)', nullable=False, chn_name='预计收入截止(元)')
    """预计收入截止(元):"""

    EProfitFloor: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceForecast', column_name='EProfitFloor', column_type='decimal(19,4)', nullable=False, chn_name='预计净利润起始(元)')
    """预计净利润起始(元):"""

    EProfitCeiling: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceForecast', column_name='EProfitCeiling', column_type='decimal(19,4)', nullable=False, chn_name='预计净利润截止(元)')
    """预计净利润截止(元):"""

    EEPSFloor: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceForecast', column_name='EEPSFloor', column_type='decimal(19,4)', nullable=False, chn_name='预计每股收益起始(元)')
    """预计每股收益起始(元):"""

    EEPSCeiling: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceForecast', column_name='EEPSCeiling', column_type='decimal(19,4)', nullable=False, chn_name='预计每股收益截止(元)')
    """预计每股收益截止(元):"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceForecast', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。"""

    NPYOYConsistentForecast: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceForecast', column_name='NPYOYConsistentForecast', column_type='decimal(18,4)', nullable=False, chn_name='一致预期净利润增幅(%)')
    """一致预期净利润增幅(%):一致预期净利润增幅（NPYOYConsistentForecast））＝(预测净利润平均值(t年)/最近报告期披露的归属母公司净利润－1）*100%"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceForecast', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceForecast', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceForecast', column_name='InfoPublDate', column_type='datetime', nullable=True, chn_name='信息发布日期')
    """信息发布日期:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceForecast', column_name='EndDate', column_type='datetime', nullable=True, chn_name='业绩预计报告期')
    """业绩预计报告期:"""

    ForcastType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceForecast', column_name='ForcastType', column_type='int', nullable=False, chn_name='业绩预计类型')
    """业绩预计类型:业绩预计类型(ForcastType)与(CT_SystemConst)表中的DM字段关联，令LB = 1158，得到业绩预计类型的具体描述：1-预亏，2-预警，3-预盈，4-预增，5-预平，6-经营计划，7-减亏，8-预降，9-减增，10-提前披露，18-减降，19-由盈转亏，20-扭亏为盈，21-同向上升，22-同向下降。"""

    ForcastReason: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceForecast', column_name='ForcastReason', column_type='int', nullable=False, chn_name='业绩预计原因')
    """业绩预计原因:"""

    ResultStatement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceForecast', column_name='ResultStatement', column_type='varchar(50)', nullable=False, chn_name='业绩预计结果说明')
    """业绩预计结果说明:"""

    ForcastContent: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceForecast', column_name='ForcastContent', column_type='text', nullable=False, chn_name='业绩预计内容描述')
    """业绩预计内容描述:"""

    ForecastObject: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_PerformanceForecast', column_name='ForecastObject', column_type='int', nullable=False, chn_name='预计对象')
    """预计对象:预计对象(ForecastObject)与(CT_SystemConst)表中的DM字段关联，令LB = 1505，得到预计对象的具体描述：10-累计利润，13-季度利润，20-累计收入，23-季度收入。"""

