# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class QT_HKDailyQuote(SQLTableEntity):
    name: str = 'QT_HKDailyQuote'
    
    chn_name: str = '港股行情库表'
    
    business_unique: str = '恒生指数相关数据请见新表: 境外指数行情(含香港)QT_OSIndexQuote'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.香港联合交易所交易日行情报价盘后数据。包含主要字段有：最高价、最低价、开盘价、昨收盘价、收盘价、涨跌幅、交易单位、成交量、成交额等。
2.数据范围：1990年至今。
3.数据来源：港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuote', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    OpenPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuote', column_name='OpenPrice', column_type='decimal(19,4)', nullable=False, chn_name='开盘价(元)')
    """开盘价(元):开盘价（OpenPrice）：当交易所行情源在没有提供开盘价，并且当天非停牌，正常是没有成交的情况下，会用当天收盘价进行填充。"""

    Change: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuote', column_name='Change', column_type='float', nullable=False, chn_name='涨跌(元)')
    """涨跌(元):"""

    PrevClosePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuote', column_name='PrevClosePrice', column_type='decimal(19,4)', nullable=False, chn_name='昨收盘(元)')
    """昨收盘(元):昨收盘（PrevClosePrice）：当交易所行情源在没有提供昨收盘价，并且当天非停牌，会分几种情况处理，以补充昨收维持涨跌幅和涨跌的计算。其中，新股上市正常不会提供昨收盘价，这时会以发行价做填充，如果是介绍上市等没有明确发行价的情况，为了最大限度接近真实价值，以开盘价填充昨收盘价。除分红、送红股、拆股并股等简单除权的情港交所在实物分配、红利认股证等情况，..."""

    PERatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuote', column_name='PERatio', column_type='decimal(18,4)', nullable=False, chn_name='市盈率')
    """市盈率:"""

    DividendYield: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuote', column_name='DividendYield', column_type='decimal(9,5)', nullable=False, chn_name='息率')
    """息率:"""

    BidVolume: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuote', column_name='BidVolume', column_type='decimal(19,4)', nullable=False, chn_name='买入成交')
    """买入成交:"""

    AskVolume: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuote', column_name='AskVolume', column_type='decimal(19,4)', nullable=False, chn_name='卖出成交')
    """卖出成交:"""

    BidPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuote', column_name='BidPrice', column_type='decimal(19,4)', nullable=False, chn_name='买入价')
    """买入价:"""

    AskPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuote', column_name='AskPrice', column_type='decimal(19,4)', nullable=False, chn_name='卖出价')
    """卖出价:"""

    ChangePCT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuote', column_name='ChangePCT', column_type='float', nullable=False, chn_name='变动百分比(%)')
    """变动百分比(%):"""

    TradingDay: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuote', column_name='TradingDay', column_type='datetime', nullable=True, chn_name='日期')
    """日期:"""

    CurrencyUnitCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuote', column_name='CurrencyUnitCode', column_type='int', nullable=False, chn_name='货币单位代码')
    """货币单位代码:货币单位代码(CurrencyUnitCode)与(CT_SystemConst)表中的DM字段关联，令LB=1068，得到货币单位代码的具体描述：1000-美元，1100-港元，1420-人民币元"""

    Currency: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuote', column_name='Currency', column_type='varchar(20)', nullable=False, chn_name='货币')
    """货币:"""

    SMA10: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuote', column_name='SMA10', column_type='decimal(19,4)', nullable=False, chn_name='SMA10')
    """SMA10:"""

    SMA20: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuote', column_name='SMA20', column_type='decimal(19,4)', nullable=False, chn_name='SMA20')
    """SMA20:"""

    SMA50: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuote', column_name='SMA50', column_type='decimal(19,4)', nullable=False, chn_name='SMA50')
    """SMA50:"""

    SMA250: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuote', column_name='SMA250', column_type='decimal(19,4)', nullable=False, chn_name='SMA250')
    """SMA250:"""

    AnnualHigh: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuote', column_name='AnnualHigh', column_type='decimal(19,4)', nullable=False, chn_name='年最高价')
    """年最高价:"""

    AnnualLow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuote', column_name='AnnualLow', column_type='decimal(19,4)', nullable=False, chn_name='年最低价')
    """年最低价:"""

    MonthHigh: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuote', column_name='MonthHigh', column_type='decimal(19,4)', nullable=False, chn_name='月最高价')
    """月最高价:"""

    MonthLow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuote', column_name='MonthLow', column_type='decimal(19,4)', nullable=False, chn_name='月最低价')
    """月最低价:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuote', column_name='InnerCode', column_type='int', nullable=True, chn_name='证券内部编码')
    """证券内部编码:证券内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。"""

    Mark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuote', column_name='Mark', column_type='int', nullable=False, chn_name='标识')
    """标识:标识（ Mark ）：固定以下常量：1-正常交易，2-全天停牌，3-恢复交易，4-非全天停牌，6-港交所披露空值，8-其他"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuote', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuote', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    ClosePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuote', column_name='ClosePrice', column_type='decimal(19,4)', nullable=False, chn_name='收盘价(元)')
    """收盘价(元):"""

    HighPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuote', column_name='HighPrice', column_type='decimal(19,4)', nullable=False, chn_name='最高价(元)')
    """最高价(元):最高价（HighPrice）：当交易所行情源在没有提供最高价，并且当天非停牌，正常是没有成交的情况下，会用当天收盘价进行填充。因交易所的价格生成规则，会有存在最高价<收盘价的情况，会有存在最高价<开盘价的情况。"""

    LowPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuote', column_name='LowPrice', column_type='decimal(19,4)', nullable=False, chn_name='最低价(元)')
    """最低价(元):最低价（LowPrice）：当交易所行情源在没有提供最低价，并且当天非停牌，正常是没有成交的情况下，会用当天收盘价进行填充。因交易所的价格生成规则，会有存在最低价>收盘价的情况，会有存在最低价>开盘价的情况。"""

    TurnoverValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuote', column_name='TurnoverValue', column_type='decimal(19,4)', nullable=False, chn_name='成交金额(元)')
    """成交金额(元):"""

    TurnoverVolume: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuote', column_name='TurnoverVolume', column_type='decimal(18,0)', nullable=False, chn_name='成交量(股)')
    """成交量(股):"""

    Lot: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuote', column_name='Lot', column_type='int', nullable=False, chn_name='交易单位(股/手)')
    """交易单位(股/手):"""

