# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class QT_SYWGIndexQuote(SQLTableEntity):
    name: str = 'QT_SYWGIndexQuote'
    
    chn_name: str = '申万指数行情'
    
    business_unique: str = '申万授权，二、三级行业需授权，一级行业是公开数据'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.收录了申银万国研究所发布的指数行情，包括风格指数、行业类指数等的高开低收、成交量/额等信息。
2.历史数据：1999年12月至今
3.数据源：申银万国研究所"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_SYWGIndexQuote', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    TurnoverValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_SYWGIndexQuote', column_name='TurnoverValue', column_type='decimal(19,4)', nullable=False, chn_name='成交金额(元)')
    """成交金额(元):"""

    IndexPE: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_SYWGIndexQuote', column_name='IndexPE', column_type='decimal(19,4)', nullable=False, chn_name='指数市盈率')
    """指数市盈率:"""

    IndexPB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_SYWGIndexQuote', column_name='IndexPB', column_type='decimal(19,4)', nullable=False, chn_name='指数市净率')
    """指数市净率:"""

    TotalMarketValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_SYWGIndexQuote', column_name='TotalMarketValue', column_type='decimal(19,4)', nullable=False, chn_name='总市值(万元)')
    """总市值(万元):"""

    AShareTotalMV: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_SYWGIndexQuote', column_name='AShareTotalMV', column_type='decimal(19,4)', nullable=False, chn_name='A股流通市值(万元)')
    """A股流通市值(万元):"""

    TurnoverDeals: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_SYWGIndexQuote', column_name='TurnoverDeals', column_type='int', nullable=False, chn_name='成交笔数')
    """成交笔数:"""

    ChangePCT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_SYWGIndexQuote', column_name='ChangePCT', column_type='decimal(19,8)', nullable=False, chn_name='涨跌幅')
    """涨跌幅:"""

    RightLevel: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_SYWGIndexQuote', column_name='RightLevel', column_type='tinyint', nullable=True, chn_name='权限级别')
    """权限级别:权限级别（RightLevel）：聚源保留字段，不做实际使用"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_SYWGIndexQuote', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_SYWGIndexQuote', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_SYWGIndexQuote', column_name='InnerCode', column_type='int', nullable=True, chn_name='证券内部编码')
    """证券内部编码:证券内部编码（InnerCode）：与“指数基本情况表（LC_IndexBasicInfo）”中的“指数内部代码（IndexCode）”关联，得到指数的发布机构、行业类别等；或与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的交易代码、简称等。"""

    TradingDay: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_SYWGIndexQuote', column_name='TradingDay', column_type='datetime', nullable=True, chn_name='交易日')
    """交易日:"""

    PrevClosePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_SYWGIndexQuote', column_name='PrevClosePrice', column_type='decimal(10,4)', nullable=False, chn_name='昨收盘(元/点)')
    """昨收盘(元/点):"""

    OpenPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_SYWGIndexQuote', column_name='OpenPrice', column_type='decimal(10,4)', nullable=False, chn_name='今开盘(元/点)')
    """今开盘(元/点):"""

    HighPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_SYWGIndexQuote', column_name='HighPrice', column_type='decimal(10,4)', nullable=False, chn_name='最高价(元/点)')
    """最高价(元/点):"""

    LowPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_SYWGIndexQuote', column_name='LowPrice', column_type='decimal(10,4)', nullable=False, chn_name='最低价(元/点)')
    """最低价(元/点):"""

    ClosePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_SYWGIndexQuote', column_name='ClosePrice', column_type='decimal(10,4)', nullable=False, chn_name='收盘价(元/点)')
    """收盘价(元/点):"""

    TurnoverVolume: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_SYWGIndexQuote', column_name='TurnoverVolume', column_type='decimal(19,2)', nullable=False, chn_name='成交量')
    """成交量:"""

