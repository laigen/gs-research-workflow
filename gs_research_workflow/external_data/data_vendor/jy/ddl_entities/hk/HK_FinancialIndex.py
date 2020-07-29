# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_FinancialIndex(SQLTableEntity):
    name: str = 'HK_FinancialIndex'
    
    chn_name: str = '港股财务指标'
    
    business_unique: str = 'CompanyCode,IfAdjusted,EndDate,PeriodMark,Currency'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.介绍港股财务指标的基本属性、每股数据、资产负债、损益和现金流量等相关信息。主要包含市场关注度较高的三大报表常用财务指标，是财务数据的简表。                                          2.数据范围：1998年至今。
3.数据来源:港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='EndDate', column_type='datetime', nullable=False, chn_name='截止日期')
    """截止日期:"""

    PeriodMark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='PeriodMark', column_type='int', nullable=False, chn_name='日期标志')
    """日期标志:日期标志(PeriodMark)与(CT_SystemConst)表中的DM字段关联，令LB = 1314，得到日期标志的具体描述：1-1个月，2-2个月，3-3个月，4-4个月，5-5个月，6-半年度，7-7个月，8-8个月，9-9个月，10-10个月，11-11个月，12-年度，13-13个月，14-14个月，15-15个月，16-16个月，17-17个..."""

    FinancialYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='FinancialYear', column_type='datetime', nullable=False, chn_name='财政年度')
    """财政年度:"""

    Currency: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='Currency', column_type='int', nullable=False, chn_name='货币单位')
    """货币单位:货币单位(Currency)与(CT_SystemConst)表中的DM字段关联，令LB = 1068，得到货币单位的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，1170-约旦第纳尔，1180-科威特第纳..."""

    OpinionType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='OpinionType', column_type='int', nullable=False, chn_name='核数师意见类型')
    """核数师意见类型:核数师意见类型(OpinionType)与(CT_SystemConst)表中的DM字段关联，令LB = 1051，得到核数师意见类型的具体描述：1-无保留，2-无保留带解释性说明，3-保留意见，4-拒绝/无法表示意见，5-否定意见，6-未经审计，7-保留带解释性说明，9-修改意见，10-经审计（不确定具体意见类型），70-国家卫计委。"""

    EPSBasic: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='EPSBasic', column_type='decimal(18,8)', nullable=False, chn_name='每股基本盈利(元)')
    """每股基本盈利(元):每股基本盈利（EPSBasic）：大多数情况数据取值自港股财报数据，因新股发行时基本每股收益数据不准确，当来源是招股章程、申请版本和聆讯后资料集时，会通过逻辑对该指标修正。计算公式=归属母公司净利润/新股上市后总股数"""

    EPS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='EPS', column_type='decimal(18,8)', nullable=False, chn_name='每股摊薄盈利(元)')
    """每股摊薄盈利(元):每股摊薄盈利（EPS）：大多数情况数据取值自港股财报数据，因新股发行时基本每股收益数据不准确，当来源是招股章程、申请版本和聆讯后资料集时，会通过逻辑对该指标修正。计算公式=归属母公司净利润/新股上市后总股数"""

    TotalAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='TotalAssets', column_type='decimal(19,4)', nullable=False, chn_name='总资产(元)')
    """总资产(元):"""

    NoncurrentAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='NoncurrentAssets', column_type='decimal(19,4)', nullable=False, chn_name='非流动资产(元)')
    """非流动资产(元):"""

    CurrentAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='CurrentAssets', column_type='decimal(19,4)', nullable=False, chn_name='流动资产(元)')
    """流动资产(元):"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到港股的交易代码、简称等。"""

    CurrentLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='CurrentLiability', column_type='decimal(19,4)', nullable=False, chn_name='流动负债(元)')
    """流动负债(元):"""

    NonurrentLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='NonurrentLiability', column_type='decimal(19,4)', nullable=False, chn_name='非流动负债(元)')
    """非流动负债(元):"""

    TotalLiability: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='TotalLiability', column_type='decimal(19,4)', nullable=False, chn_name='总负债(元)')
    """总负债(元):"""

    MinorityInterests: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='MinorityInterests', column_type='decimal(19,4)', nullable=False, chn_name='少数股东权益(元)')
    """少数股东权益(元):"""

    TotalShareholderEquity: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='TotalShareholderEquity', column_type='decimal(19,4)', nullable=False, chn_name='股东权益/资产净值(元)')
    """股东权益/资产净值(元):"""

    ShareCapital: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='ShareCapital', column_type='decimal(19,4)', nullable=False, chn_name='股本(元)')
    """股本(元):"""

    Reserves: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='Reserves', column_type='decimal(19,4)', nullable=False, chn_name='储备(元)')
    """储备(元):"""

    OperatingIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='OperatingIncome', column_type='decimal(19,4)', nullable=False, chn_name='营业额\银行经营收入(元)')
    """营业额\银行经营收入(元):"""

    OperatingProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='OperatingProfit', column_type='decimal(19,4)', nullable=False, chn_name='经营溢利(元)')
    """经营溢利(元):"""

    FinancialExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='FinancialExpense', column_type='decimal(19,4)', nullable=False, chn_name='融资成本/财务费用(元)')
    """融资成本/财务费用(元):"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='最新信息发布日期')
    """最新信息发布日期:"""

    AffiliatedComapnyprofit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='AffiliatedComapnyprofit', column_type='decimal(19,4)', nullable=False, chn_name='应占联营公司溢利(元)')
    """应占联营公司溢利(元):"""

    CooperateBusinessProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='CooperateBusinessProfit', column_type='decimal(19,4)', nullable=False, chn_name='应占共同控制实体之溢利(合营公司)(元)')
    """应占共同控制实体之溢利(合营公司)(元):"""

    EarningBeforeTax: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='EarningBeforeTax', column_type='decimal(19,4)', nullable=False, chn_name='除税前溢利(元)')
    """除税前溢利(元):"""

    TaxExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='TaxExpense', column_type='decimal(19,4)', nullable=False, chn_name='税项(元)')
    """税项(元):"""

    EarningAfterTax: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='EarningAfterTax', column_type='decimal(19,4)', nullable=False, chn_name='除税后溢利(元)')
    """除税后溢利(元):"""

    MinorityProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='MinorityProfit', column_type='decimal(19,4)', nullable=False, chn_name='少数股东损益(元)')
    """少数股东损益(元):"""

    ProfitToShareholders: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='ProfitToShareholders', column_type='decimal(19,4)', nullable=False, chn_name='股东应占溢利净额(扣税及少数权益后溢利)(元)')
    """股东应占溢利净额(扣税及少数权益后溢利)(元):"""

    GrowthRate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='GrowthRate', column_type='decimal(18,8)', nullable=False, chn_name='相对上期增减')
    """相对上期增减:"""

    Dividend: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='Dividend', column_type='decimal(19,4)', nullable=False, chn_name='股息(元)')
    """股息(元):"""

    SpecialItemProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='SpecialItemProfit', column_type='decimal(19,4)', nullable=False, chn_name='非经常性项目收益(元)')
    """非经常性项目收益(元):"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='InfoSource', column_type='varchar(100)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    ProfitExSpecialItem: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='ProfitExSpecialItem', column_type='decimal(19,4)', nullable=False, chn_name='扣除非经常性项目后溢利(元)')
    """扣除非经常性项目后溢利(元):"""

    NetOperateCashFlow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='NetOperateCashFlow', column_type='decimal(19,4)', nullable=False, chn_name='经营业务现金流量净额(元)')
    """经营业务现金流量净额(元):"""

    NetInvestCashFlow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='NetInvestCashFlow', column_type='decimal(19,4)', nullable=False, chn_name='投资活动现金流量净额(元)')
    """投资活动现金流量净额(元):"""

    NetFinanceCashFlow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='NetFinanceCashFlow', column_type='decimal(19,4)', nullable=False, chn_name='融资活动现金流量净额(元)')
    """融资活动现金流量净额(元):"""

    NetCashFlow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='NetCashFlow', column_type='decimal(19,4)', nullable=False, chn_name='现金流量净额(元)')
    """现金流量净额(元):"""

    CashEquivalentBeginPer: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='CashEquivalentBeginPer', column_type='decimal(19,4)', nullable=False, chn_name='期初现金及现金等价物(元)')
    """期初现金及现金等价物(元):"""

    EffectOfFERChanges: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='EffectOfFERChanges', column_type='decimal(19,4)', nullable=False, chn_name='外币汇率转换影响(元)')
    """外币汇率转换影响(元):"""

    CashEquivalentEndPer: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='CashEquivalentEndPer', column_type='decimal(19,4)', nullable=False, chn_name='期末现金及现金等价物(元)')
    """期末现金及现金等价物(元):"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='修改日期')
    """修改日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    AbstrPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='AbstrPublDate', column_type='datetime', nullable=False, chn_name='摘要发布日期')
    """摘要发布日期:"""

    PerformancePublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='PerformancePublDate', column_type='datetime', nullable=False, chn_name='业绩公告发布日期')
    """业绩公告发布日期:"""

    PeriodicReportPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='PeriodicReportPublDate', column_type='datetime', nullable=False, chn_name='定期报告发布日期')
    """定期报告发布日期:"""

    ChangePublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='ChangePublDate', column_type='datetime', nullable=False, chn_name='更正日期')
    """更正日期:"""

    IfAdjusted: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinancialIndex', column_name='IfAdjusted', column_type='int', nullable=False, chn_name='调整标志')
    """调整标志:调整标志(IfAdjusted)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM IN (1,2,3)，得到调整标志的具体描述：1-是，2-否，3-前。"""

