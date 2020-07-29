# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_DarkPoolQuote(SQLTableEntity):
    name: str = 'HK_DarkPoolQuote'
    
    chn_name: str = '港股新股暗盘行情表'
    
    business_unique: str = 'InnerCode,TradStockbroker'
    
    refresh_freq: str = """滚动更新"""
    
    comment: str = """1.记录辉立证券、耀才证券在新股上市之前一个营业日在自营交易场新股的成交情况。包含主要字段有：交易券商、交易日期、上市日期、收盘价、涨跌幅、成交股数、成交金额等。
2.数据范围：2017-02至今。
3.数据来源：辉立证券、耀才证券。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DarkPoolQuote', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    ClosePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DarkPoolQuote', column_name='ClosePrice', column_type='decimal(19,4)', nullable=False, chn_name='收盘价(元)')
    """收盘价(元):"""

    ChangeOfPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DarkPoolQuote', column_name='ChangeOfPrice', column_type='decimal(19,4)', nullable=False, chn_name='涨跌(元)')
    """涨跌(元):"""

    ChangePCT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DarkPoolQuote', column_name='ChangePCT', column_type='decimal(18,4)', nullable=False, chn_name='涨跌幅(%)')
    """涨跌幅(%):"""

    TransactionNO: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DarkPoolQuote', column_name='TransactionNO', column_type='decimal(14,6)', nullable=False, chn_name='成交盘数')
    """成交盘数:"""

    TurnoverVolume: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DarkPoolQuote', column_name='TurnoverVolume', column_type='decimal(14,0)', nullable=False, chn_name='成交股数(股)')
    """成交股数(股):"""

    TurnoverValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DarkPoolQuote', column_name='TurnoverValue', column_type='decimal(19,4)', nullable=False, chn_name='成交金额(元)')
    """成交金额(元):"""

    Lot: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DarkPoolQuote', column_name='Lot', column_type='decimal(18,4)', nullable=False, chn_name='交易单位(股/手)')
    """交易单位(股/手):"""

    MinPriceChg: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DarkPoolQuote', column_name='MinPriceChg', column_type='decimal(19,4)', nullable=False, chn_name='最小变动价格')
    """最小变动价格:"""

    CurrencyUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DarkPoolQuote', column_name='CurrencyUnit', column_type='int', nullable=False, chn_name='货币单位')
    """货币单位:货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB=1068，得到货币单位的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，1170-约旦第纳尔，1180-科威特..."""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DarkPoolQuote', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新日期')
    """更新日期:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DarkPoolQuote', column_name='InnerCode', column_type='int', nullable=True, chn_name='证券内部代码')
    """证券内部代码:证券内部代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DarkPoolQuote', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    TradingDay: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DarkPoolQuote', column_name='TradingDay', column_type='datetime', nullable=True, chn_name='交易日期')
    """交易日期:"""

    ListedDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DarkPoolQuote', column_name='ListedDate', column_type='datetime', nullable=False, chn_name='上市日期')
    """上市日期:"""

    TradStockbroker: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DarkPoolQuote', column_name='TradStockbroker', column_type='varchar(20)', nullable=True, chn_name='交易券商')
    """交易券商:交易券商（TradStockbroker）：为提供港股暗盘交易的券商，目前有两家，分别是辉立证券和耀才证券。"""

    IssuePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DarkPoolQuote', column_name='IssuePrice', column_type='decimal(19,4)', nullable=False, chn_name='发行价(元)')
    """发行价(元):"""

    OpenPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DarkPoolQuote', column_name='OpenPrice', column_type='decimal(19,4)', nullable=False, chn_name='开盘价(元)')
    """开盘价(元):"""

    HighPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DarkPoolQuote', column_name='HighPrice', column_type='decimal(19,4)', nullable=False, chn_name='最高价(元)')
    """最高价(元):"""

    LowPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DarkPoolQuote', column_name='LowPrice', column_type='decimal(19,4)', nullable=False, chn_name='最低价(元)')
    """最低价(元):"""

