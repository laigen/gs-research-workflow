# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MT_TradingDetail(SQLTableEntity):
    name: str = 'MT_TradingDetail'
    
    chn_name: str = '融资融券交易明细'
    
    business_unique: str = 'InnerCode,TradingDay'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.收录国内证券交易所披露的收录融资融券日交易明细数据
2.历史数据：2010年3月起-至今。
3.数据来源：聚源按照上交所、深交所原始披露整理"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingDetail', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    SecuritySellVolume: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingDetail', column_name='SecuritySellVolume', column_type='decimal(18,2)', nullable=False, chn_name='融券卖出量(股)')
    """融券卖出量(股):"""

    SecurityRefundVolume: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingDetail', column_name='SecurityRefundVolume', column_type='decimal(18,2)', nullable=False, chn_name='融券偿还量(股)')
    """融券偿还量(股):"""

    SecurityValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingDetail', column_name='SecurityValue', column_type='decimal(19,4)', nullable=False, chn_name='融券余额(元)')
    """融券余额(元):融券余额（SecurityValue）：深交所=公布数据；上交所=融券余量与对应的股价乘积"""

    TradingValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingDetail', column_name='TradingValue', column_type='decimal(19,4)', nullable=False, chn_name='融资融券交易总金额(元)')
    """融资融券交易总金额(元):融资融券交易总金额（TradingValue）：深交所=公布数据；上交所=融资余额+融券余额"""

    FinaInTotalRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingDetail', column_name='FinaInTotalRatio', column_type='decimal(9,6)', nullable=False, chn_name='融资占交易所融资余额比(%)')
    """融资占交易所融资余额比(%):融资占交易所融资余额比（FinaInTotalRatio）=融资余额/当日交易所融资余额*100"""

    SecuInTotalRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingDetail', column_name='SecuInTotalRatio', column_type='decimal(9,6)', nullable=False, chn_name='融券占交易所融券余额比(%)')
    """融券占交易所融券余额比(%):融券占交易所融券余额比（SecuInTotalRatio）=融券余额/当日交易所融券余量金额*100"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingDetail', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingDetail', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingDetail', column_name='InfoSource', column_type='varchar(50)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingDetail', column_name='InnerCode', column_type='int', nullable=True, chn_name='内部编码')
    """内部编码:内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。"""

    TradingDay: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingDetail', column_name='TradingDay', column_type='datetime', nullable=True, chn_name='信用交易日期')
    """信用交易日期:"""

    SecuMarket: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingDetail', column_name='SecuMarket', column_type='int', nullable=False, chn_name='证券市场')
    """证券市场:证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB = 201 AND DM IN (83,90)，得到证券市场的具体描述：83-上海证券交易所，90-深圳证券交易所。"""

    FinanceValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingDetail', column_name='FinanceValue', column_type='decimal(19,4)', nullable=False, chn_name='融资余额(元)')
    """融资余额(元):"""

    FinanceBuyValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingDetail', column_name='FinanceBuyValue', column_type='decimal(19,4)', nullable=False, chn_name='融资买入额(元)')
    """融资买入额(元):"""

    FinanceRefundValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingDetail', column_name='FinanceRefundValue', column_type='decimal(19,4)', nullable=False, chn_name='融资偿还额(元)')
    """融资偿还额(元):融资偿还额（FinanceRefundValue）：深交所=前日融资余额+本日融资买入额-本日融资余额；上交所=公布数据"""

    SecurityVolume: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TradingDetail', column_name='SecurityVolume', column_type='decimal(18,2)', nullable=False, chn_name='融券余量(股)')
    """融券余量(股):"""

