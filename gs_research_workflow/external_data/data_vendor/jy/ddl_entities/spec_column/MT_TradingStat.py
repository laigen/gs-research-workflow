# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MT_TradingStat(SQLTableEntity):
    name: str = 'MT_TradingStat'
    
    chn_name: str = '融资融券交易总量'
    
    business_unique: str = 'TradingDay,SecuMarket,ReportPeriod'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.收录国内证券交易所披露的融资融券日交易汇总数据
2.历史数据：2010年3月起-至今。
3.数据来源：聚源按照上交所、深交所原始披露整理"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingStat', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    SecurityValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingStat', column_name='SecurityValue', column_type='decimal(19,4)', nullable=False, chn_name='融券余量金额(元)')
    """融券余量金额(元):"""

    SecuritySellVolume: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingStat', column_name='SecuritySellVolume', column_type='decimal(18,2)', nullable=False, chn_name='融券卖出量(股)')
    """融券卖出量(股):融券卖出量（SecuritySellVolume）：深交所=公布数据；上交所=本日交易明细融券卖出量求和"""

    TradingValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingStat', column_name='TradingValue', column_type='decimal(19,4)', nullable=False, chn_name='融资融券交易总金额(元)')
    """融资融券交易总金额(元):"""

    FinaInTVRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingStat', column_name='FinaInTVRatio', column_type='decimal(9,6)', nullable=False, chn_name='融资占融资融券总额比(%)')
    """融资占融资融券总额比(%):融资占融资融券总额比（FinaInTotalRatio）=（融资余额/融资融券交易总金额）*100"""

    TVChangeRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingStat', column_name='TVChangeRatio', column_type='decimal(9,4)', nullable=False, chn_name='融资融券总额变动(%)')
    """融资融券总额变动(%):融资融券总额变动（TVChangeRatio）=（本日的融资融券交易总金额/上一日的融资融券交易总金额-1）*100"""

    TVChangeRatioHS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingStat', column_name='TVChangeRatioHS', column_type='decimal(9,4)', nullable=False, chn_name='沪深融资融券总额变动(%)')
    """沪深融资融券总额变动(%):沪深融资融券总额变动（TVChangeRatioHS）=（沪深市场本日的融资融券交易总金额/沪深市场上一日的融资融券交易总金额-1）*100"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingStat', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingStat', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingStat', column_name='InfoSource', column_type='varchar(50)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    TradingDay: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingStat', column_name='TradingDay', column_type='datetime', nullable=True, chn_name='信用交易日期')
    """信用交易日期:"""

    SecuMarket: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingStat', column_name='SecuMarket', column_type='int', nullable=True, chn_name='证券市场')
    """证券市场:证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB = 201 AND DM IN (83,90)，得到证券市场的具体描述：83-上海证券交易所，90-深圳证券交易所。"""

    ReportPeriod: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingStat', column_name='ReportPeriod', column_type='int', nullable=True, chn_name='统计期间')
    """统计期间:统计期间(ReportPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 1074 AND DM = 5，得到统计期间的具体描述：5-日。"""

    FinanceValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingStat', column_name='FinanceValue', column_type='decimal(19,4)', nullable=False, chn_name='融资余额(元)')
    """融资余额(元):"""

    FinanceBuyValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingStat', column_name='FinanceBuyValue', column_type='decimal(19,4)', nullable=False, chn_name='融资买入额(元)')
    """融资买入额(元):"""

    FinanceRefundValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingStat', column_name='FinanceRefundValue', column_type='decimal(19,4)', nullable=False, chn_name='融资偿还额(元)')
    """融资偿还额(元):"""

    SecurityVolume: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingStat', column_name='SecurityVolume', column_type='decimal(18,2)', nullable=False, chn_name='融券余量(股)')
    """融券余量(股):融券余量（股）（SecurityVolume）：有公布取公布值；未公布则等于本日交易明细融券余量求和"""

