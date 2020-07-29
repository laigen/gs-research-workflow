# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class QT_IndexQuote(SQLTableEntity):
    name: str = 'QT_IndexQuote'
    
    chn_name: str = '指数行情'
    
    business_unique: str = 'InnerCode,TradingDay'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.收录了指数每日的行情数据，包括了国内外指数发布机构发布的常用指数的高、开、低、收等信息；
2.使用说明：库内交易所指数代码对应的成交量额统计口径为其样本券的成交量额的总和（不包含成份股的大宗交易）、深交所同时提供市场成交量、额统计口径，代码以“395***”开头；
3.补充说明：常见发布方指数的全量行情，如申万系列指数全量行情详见“申万指数行情表QT_SYWGIndexQuote”、中证系列指数全量行情详见“中证指数行情QT_CSIIndexQuote”、中债系列指数全量行情详见“中债指数行情Bond_ChinaBondIndexQuote”。
4.历史数据：1928年10月至今
5.数据源：中证指数有限公司、上海证券交易所、深圳证券交易所、中央国债登记结算有限责任公司、申银万国研究所、标普道琼斯指数公司等"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_IndexQuote', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    TurnoverValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_IndexQuote', column_name='TurnoverValue', column_type='decimal(19,4)', nullable=False, chn_name='成交金额(元)')
    """成交金额(元):"""

    TurnoverDeals: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_IndexQuote', column_name='TurnoverDeals', column_type='int', nullable=False, chn_name='成交笔数')
    """成交笔数:"""

    ChangePCT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_IndexQuote', column_name='ChangePCT', column_type='decimal(19,8)', nullable=False, chn_name='涨跌幅')
    """涨跌幅:"""

    NegotiableMV: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_IndexQuote', column_name='NegotiableMV', column_type='decimal(19,4)', nullable=False, chn_name='流通市值')
    """流通市值:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_IndexQuote', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_IndexQuote', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_IndexQuote', column_name='InnerCode', column_type='int', nullable=True, chn_name='证券内部编码')
    """证券内部编码:证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称等。"""

    TradingDay: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_IndexQuote', column_name='TradingDay', column_type='datetime', nullable=True, chn_name='交易日')
    """交易日:"""

    PrevClosePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_IndexQuote', column_name='PrevClosePrice', column_type='decimal(10,4)', nullable=False, chn_name='昨收盘(元/点)')
    """昨收盘(元/点):"""

    OpenPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_IndexQuote', column_name='OpenPrice', column_type='decimal(10,4)', nullable=False, chn_name='今开盘(元/点)')
    """今开盘(元/点):"""

    HighPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_IndexQuote', column_name='HighPrice', column_type='decimal(10,4)', nullable=False, chn_name='最高价(元/点)')
    """最高价(元/点):"""

    LowPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_IndexQuote', column_name='LowPrice', column_type='decimal(10,4)', nullable=False, chn_name='最低价(元/点)')
    """最低价(元/点):"""

    ClosePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_IndexQuote', column_name='ClosePrice', column_type='decimal(10,4)', nullable=False, chn_name='收盘价(元/点)')
    """收盘价(元/点):"""

    TurnoverVolume: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_IndexQuote', column_name='TurnoverVolume', column_type='decimal(19,2)', nullable=False, chn_name='成交量')
    """成交量:"""

