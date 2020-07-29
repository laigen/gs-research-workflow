# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class QT_TradingCapitalFlow(SQLTableEntity):
    name: str = 'QT_TradingCapitalFlow'
    
    chn_name: str = '股票交易资金流向'
    
    business_unique: str = 'InnerCode,TradingDate,QuoteType,ValueRange'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.展示每个交易日在深沪交易所交易的股票，在不同单笔成交金额区间的累计主买、主卖金额及成交量情况。
流入量（金额）：主动买成交，即在卖盘上成交的外盘成交量(金额)；流出量（金额）：主动卖成交，即在买盘上成交的内盘成交量(金额)。
本表仅包括二级市场股票交易所产生的资金流向数据，不含大宗交易产生的资金流向；大宗交易资金流向数据可参考“股东股权变动（ LC_ShareTransfer）”表(TranMode='11')。
2.数据范围：2012-07-09起至今
3.信息来源：恒生电子"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_TradingCapitalFlow', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_TradingCapitalFlow', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_TradingCapitalFlow', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_TradingCapitalFlow', column_name='InnerCode', column_type='int', nullable=True, chn_name='内部编码')
    """内部编码:内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。"""

    TradingDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_TradingCapitalFlow', column_name='TradingDate', column_type='datetime', nullable=True, chn_name='交易日期')
    """交易日期:"""

    QuoteType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_TradingCapitalFlow', column_name='QuoteType', column_type='int', nullable=True, chn_name='行情类别')
    """行情类别:行情类别(QuoteType)，该字段固定以下常量：1-Level1行情2-Level2行情"""

    ValueRange: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_TradingCapitalFlow', column_name='ValueRange', column_type='int', nullable=True, chn_name='单笔成交金额区间')
    """单笔成交金额区间:单笔成交金额区间(ValueRange)，该字段固定以下常量：1-[0，5w)2-[5w，30w)3-[30w，100w)4-[100w，+∞)"""

    BuyVolume: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_TradingCapitalFlow', column_name='BuyVolume', column_type='bigint', nullable=False, chn_name='流入量(股)')
    """流入量(股):"""

    SellVolume: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_TradingCapitalFlow', column_name='SellVolume', column_type='bigint', nullable=False, chn_name='流出量(股)')
    """流出量(股):"""

    BuyValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_TradingCapitalFlow', column_name='BuyValue', column_type='decimal(19,4)', nullable=False, chn_name='流入金额(元)')
    """流入金额(元):"""

    SellValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_TradingCapitalFlow', column_name='SellValue', column_type='decimal(19,4)', nullable=False, chn_name='流出金额(元)')
    """流出金额(元):"""

