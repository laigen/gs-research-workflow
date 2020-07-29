# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class QT_DailyQuote(SQLTableEntity):
    name: str = 'QT_DailyQuote'
    
    chn_name: str = '日行情表'
    
    business_unique: str = 'InnerCode,TradingDay(-)'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.收录股票、债券（不包含银行间交易的债券）、基金、指数每个交易日收盘行情数据，包括昨收盘、今开盘、最高价、最低价、收盘价、成交量、成交金额、成交笔数等行情指标。
2.数据范围：证券上市起-至今
3.信息来源：上交所/深交所每日行情收盘文件"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_DailyQuote', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    TurnoverValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_DailyQuote', column_name='TurnoverValue', column_type='decimal(19,4)', nullable=False, chn_name='成交金额(元)')
    """成交金额(元):"""

    TurnoverDeals: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_DailyQuote', column_name='TurnoverDeals', column_type='int', nullable=False, chn_name='成交笔数(笔)')
    """成交笔数(笔):"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_DailyQuote', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_DailyQuote', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_DailyQuote', column_name='InnerCode', column_type='int', nullable=True, chn_name='证券内部编码')
    """证券内部编码:证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。"""

    TradingDay: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_DailyQuote', column_name='TradingDay', column_type='datetime', nullable=True, chn_name='交易日')
    """交易日:"""

    PrevClosePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_DailyQuote', column_name='PrevClosePrice', column_type='decimal(10,4)', nullable=False, chn_name='昨收盘(元)')
    """昨收盘(元):"""

    OpenPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_DailyQuote', column_name='OpenPrice', column_type='decimal(10,4)', nullable=False, chn_name='今开盘(元)')
    """今开盘(元):"""

    HighPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_DailyQuote', column_name='HighPrice', column_type='decimal(10,4)', nullable=False, chn_name='最高价(元)')
    """最高价(元):"""

    LowPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_DailyQuote', column_name='LowPrice', column_type='decimal(10,4)', nullable=False, chn_name='最低价(元)')
    """最低价(元):"""

    ClosePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_DailyQuote', column_name='ClosePrice', column_type='decimal(10,4)', nullable=False, chn_name='收盘价(元)')
    """收盘价(元):"""

    TurnoverVolume: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_DailyQuote', column_name='TurnoverVolume', column_type='decimal(20,0)', nullable=False, chn_name='成交量(股)')
    """成交量(股):"""

