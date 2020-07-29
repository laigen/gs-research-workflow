# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class C_RR_ProfitForecast(SQLTableEntity):
    name: str = 'C_RR_ProfitForecast'
    
    chn_name: str = '研究报告_盈利预测'
    
    business_unique: str = '无'
    
    refresh_freq: str = """工作日更新"""
    
    comment: str = """1.本表主要收录各研究机构对市场上流通股票的盈利能力相关财务指标的预测数据。
2.数据范围：2004年至今
3.信息来源：各机构发布的研究报告"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='ID', column_type='bigint', nullable=False, chn_name='ID')
    """ID:"""

    OrgName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='OrgName', column_type='varchar(100)', nullable=False, chn_name='撰写机构')
    """撰写机构:"""

    WritingDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='WritingDate', column_type='datetime', nullable=False, chn_name='撰写日期')
    """撰写日期:"""

    IfForecast: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='IfForecast', column_type='int', nullable=False, chn_name='是否为预测')
    """是否为预测:是否为预测（IfForecast），该字段固定以下常量：
1-是，2-否"""

    CurrencyUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='CurrencyUnit', column_type='int', nullable=False, chn_name='货币单位')
    """货币单位:货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB=1068，得到货币单位的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，1170-约旦第纳尔，1180-科威特..."""

    EPS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='EPS', column_type='decimal(20,5)', nullable=False, chn_name='每股收益(元/股)')
    """每股收益(元/股):"""

    BPS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='BPS', column_type='decimal(20,5)', nullable=False, chn_name='每股净资产(元/股)')
    """每股净资产(元/股):"""

    OCFPS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='OCFPS', column_type='decimal(20,5)', nullable=False, chn_name='每股现金流(元/股)')
    """每股现金流(元/股):"""

    DPS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='DPS', column_type='decimal(20,5)', nullable=False, chn_name='每股股利(元/股)')
    """每股股利(元/股):"""

    OpIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='OpIncome', column_type='decimal(20,5)', nullable=False, chn_name='营业收入(万元)')
    """营业收入(万元):"""

    OpCost: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='OpCost', column_type='decimal(20,5)', nullable=False, chn_name='营业成本(万元)')
    """营业成本(万元):"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='InnerCode', column_type='int', nullable=False, chn_name='证券内部编码')
    """证券内部编码:"""

    OpProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='OpProfit', column_type='decimal(20,5)', nullable=False, chn_name='营业利润(万元)')
    """营业利润(万元):"""

    TotalProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='TotalProfit', column_type='decimal(20,5)', nullable=False, chn_name='利润总额(万元)')
    """利润总额(万元):"""

    NetProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='NetProfit', column_type='decimal(20,5)', nullable=False, chn_name='净利润(万元)')
    """净利润(万元):"""

    PNetProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='PNetProfit', column_type='decimal(20,5)', nullable=False, chn_name='归属于母公司净利润(万元)')
    """归属于母公司净利润(万元):"""

    EBIT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='EBIT', column_type='decimal(20,5)', nullable=False, chn_name='息税前利润(万元)')
    """息税前利润(万元):"""

    EBITDA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='EBITDA', column_type='decimal(20,5)', nullable=False, chn_name='息税及折旧摊销前利润(万元)')
    """息税及折旧摊销前利润(万元):"""

    ROE: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='ROE', column_type='decimal(18,4)', nullable=False, chn_name='净资产收益率')
    """净资产收益率:"""

    ROA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='ROA', column_type='decimal(18,4)', nullable=False, chn_name='总资产收益率')
    """总资产收益率:"""

    ROIC: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='ROIC', column_type='decimal(18,4)', nullable=False, chn_name='投资回报率')
    """投资回报率:"""

    PE: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='PE', column_type='decimal(18,4)', nullable=False, chn_name='市盈率')
    """市盈率:"""

    SecuCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='SecuCode', column_type='varchar(10)', nullable=False, chn_name='证券代码')
    """证券代码:"""

    PB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='PB', column_type='decimal(18,4)', nullable=False, chn_name='市净率')
    """市净率:"""

    PS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='PS', column_type='decimal(18,4)', nullable=False, chn_name='市售率')
    """市售率:"""

    EV: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='EV', column_type='decimal(18,4)', nullable=False, chn_name='企业价值倍数(倍)')
    """企业价值倍数(倍):"""

    YOYNP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='YOYNP', column_type='decimal(18,4)', nullable=False, chn_name='净利润增长率')
    """净利润增长率:"""

    YOYOpIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='YOYOpIncome', column_type='decimal(18,4)', nullable=False, chn_name='营业收入增长率')
    """营业收入增长率:"""

    Remarks: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='Remarks', column_type='varchar(1000)', nullable=False, chn_name='备注说明')
    """备注说明:"""

    DividendRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='DividendRatio', column_type='decimal(18,4)', nullable=False, chn_name='股息率')
    """股息率:"""

    GrossIncomeRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='GrossIncomeRatio', column_type='decimal(18,4)', nullable=False, chn_name='毛利率')
    """毛利率:"""

    IfCompute: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='IfCompute', column_type='int', nullable=False, chn_name='是否参与计算')
    """是否参与计算:是否参与计算（IfCompute），该字段固定以下常量：
1-否"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='UpdateTime', column_type='datetime', nullable=False, chn_name='更新时间')
    """更新时间:"""

    SecuAbbr: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='SecuAbbr', column_type='varchar(20)', nullable=False, chn_name='证券简称')
    """证券简称:"""

    ReleaseTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='ReleaseTime', column_type='datetime', nullable=False, chn_name='发布时间')
    """发布时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='JSID', column_type='bigint', nullable=False, chn_name='JSID')
    """JSID:"""

    ForecastYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='ForecastYear', column_type='int', nullable=False, chn_name='预测年度')
    """预测年度:预测年度（ForecastYear）：为具体预测年度值，如2016、2017、2018；需结合“是否为预测（IfForecast）”字段判断对应数据为实际值还是预测值。"""

    OID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='OID', column_type='bigint', nullable=False, chn_name='原文ID')
    """原文ID:原文ID（OID）：与研究报告（C_RR_ResearchReport）表的ID关联，得到对应研究报告的详细信息。"""

    Title: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='Title', column_type='varchar(200)', nullable=False, chn_name='标题')
    """标题:"""

    OrgCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='OrgCode', column_type='int', nullable=False, chn_name='撰写机构代码')
    """撰写机构代码:"""

    OrgNameAbbr: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ProfitForecast', column_name='OrgNameAbbr', column_type='varchar(100)', nullable=False, chn_name='撰写机构简称')
    """撰写机构简称:"""

