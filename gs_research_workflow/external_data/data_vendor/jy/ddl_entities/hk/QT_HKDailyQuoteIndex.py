# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class QT_HKDailyQuoteIndex(SQLTableEntity):
    name: str = 'QT_HKDailyQuoteIndex'
    
    chn_name: str = '港股行情指标表'
    
    business_unique: str = 'InnerCode,TradingDay'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.记录随港股行情变动的重要指标，包含的字段有：最小变动价格、港股股数、非港股股数、市盈率、动态市盈率、滚动市盈率、市销率、市净率、市现率、股息率（报告期）、股息率（近12个月）。
2.数据范围：2005年至今。
3.数据来源：港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteIndex', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    HKStkMV: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteIndex', column_name='HKStkMV', column_type='decimal(19,4)', nullable=False, chn_name='港股市值(元)')
    """港股市值(元):"""

    NegotiableMV: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteIndex', column_name='NegotiableMV', column_type='decimal(19,4)', nullable=False, chn_name='港股流通市值(元)')
    """港股流通市值(元):"""

    NotHKStkShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteIndex', column_name='NotHKStkShares', column_type='decimal(16,0)', nullable=False, chn_name='非港股股数(股)')
    """非港股股数(股):"""

    Ashares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteIndex', column_name='Ashares', column_type='decimal(16,0)', nullable=False, chn_name='A股股数(股)')
    """A股股数(股):"""

    Bshares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteIndex', column_name='Bshares', column_type='decimal(16,0)', nullable=False, chn_name='B股股数(股)')
    """B股股数(股):"""

    TurnoverRate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteIndex', column_name='TurnoverRate', column_type='decimal(18,4)', nullable=False, chn_name='换手率')
    """换手率:"""

    PERatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteIndex', column_name='PERatio', column_type='decimal(18,4)', nullable=False, chn_name='市盈率')
    """市盈率:市盈率(%)=当日总市值/上一年度净利润"""

    FPE: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteIndex', column_name='FPE', column_type='decimal(18,4)', nullable=False, chn_name='动态市盈率')
    """动态市盈率:动态市盈率(%)=（当日总市值/上一年度净利润）/(1+EPS增长率）^1"""

    PETTM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteIndex', column_name='PETTM', column_type='decimal(18,4)', nullable=False, chn_name='滚动市盈率')
    """滚动市盈率:滚动市盈率(%)=当日总市值/截止到当日为止前推一年间净利润"""

    PS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteIndex', column_name='PS', column_type='decimal(18,4)', nullable=False, chn_name='市销率')
    """市销率:市销率(%)=当日总市值/上一年度主营业务收入"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteIndex', column_name='InnerCode', column_type='int', nullable=True, chn_name='证券内码')
    """证券内码:证券内码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。"""

    PB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteIndex', column_name='PB', column_type='decimal(18,4)', nullable=False, chn_name='市净率')
    """市净率:市净率(%)=当日总市值/最近一份财报净资产"""

    PCF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteIndex', column_name='PCF', column_type='decimal(18,4)', nullable=False, chn_name='市现率')
    """市现率:市现率(%)=当日总市值/上一年度现金流量净额"""

    DividendRatioFY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteIndex', column_name='DividendRatioFY', column_type='decimal(19,4)', nullable=False, chn_name='股息率(报告期)')
    """股息率(报告期):股息率(报告期)=当日总市值/上一财年股息总额"""

    DividendRatioRW: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteIndex', column_name='DividendRatioRW', column_type='decimal(19,4)', nullable=False, chn_name='股息率(近12个月)')
    """股息率(近12个月):股息率(近12个月)=当日总市值/最近12个月股息总额"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteIndex', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteIndex', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InsertTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteIndex', column_name='InsertTime', column_type='datetime', nullable=False, chn_name='发布时间')
    """发布时间:"""

    TradingDay: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteIndex', column_name='TradingDay', column_type='datetime', nullable=True, chn_name='交易日')
    """交易日:"""

    ClosePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteIndex', column_name='ClosePrice', column_type='decimal(19,4)', nullable=True, chn_name='收盘价')
    """收盘价:"""

    MinPriceChg: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteIndex', column_name='MinPriceChg', column_type='decimal(19,4)', nullable=False, chn_name='最小变动价格')
    """最小变动价格:"""

    TurnoverVolume: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteIndex', column_name='TurnoverVolume', column_type='decimal(16,0)', nullable=False, chn_name='成交股数(股)')
    """成交股数(股):"""

    TurnoverValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteIndex', column_name='TurnoverValue', column_type='decimal(19,4)', nullable=False, chn_name='成交额(元)')
    """成交额(元):"""

    HKStkShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteIndex', column_name='HKStkShares', column_type='decimal(16,0)', nullable=False, chn_name='港股股数(股)')
    """港股股数(股):"""

    LimitedShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteIndex', column_name='LimitedShares', column_type='decimal(16,0)', nullable=False, chn_name='港股限售股股数(股)')
    """港股限售股股数(股):"""

