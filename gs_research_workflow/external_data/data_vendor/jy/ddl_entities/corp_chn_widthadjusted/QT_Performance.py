# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class QT_Performance(SQLTableEntity):
    name: str = 'QT_Performance'
    
    chn_name: str = '股票行情表现'
    
    business_unique: str = 'InnerCode,TradingDay'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.收录股票从最近一个交易日往前追溯一段时期的行情表现信息，包括近1周、1周以来、近1月、1月以来、近3月、近半年、近1年、今年以来、上市以来的表现情况，以及β、α、波动率、夏普比率等风险指标。
计算方法：1)区间成交金额＝∑区间每个交易日成交金额 2)区间成交量＝∑区间每个交易日成交量 3)区间涨跌幅＝(区间内最新复权收盘价/区间首日复权昨收盘－1)*100 4)区间振幅＝(区间最高复权价－区间最低复权家价)/区间首日复权昨收盘*100 5)区间换手率＝区间内成交量之和/区间内最新未限售流通股*100 6) 区间成交均价＝区间成交金额之和/区间成交量之和 7) 区间日均成交金额＝区间成交金额之和/区间交易日天数 8) 区间日均换手率＝区间每日换手率之和/区间交易日天数
2.数据范围：股票上市起-至今"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    TurnoverValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverValue', column_type='decimal(19,4)', nullable=False, chn_name='成交金额(万元)')
    """成交金额(万元):"""

    BetaCompositeIndex: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='BetaCompositeIndex', column_type='decimal(18,4)', nullable=False, chn_name='Beta值(相对综合指数,一年)')
    """Beta值(相对综合指数,一年):参考指数的取法：如在上海交易所上市，则是沪综指；在深圳交易所上市，则是深成指。"""

    BetaSYWGIndustryIndex: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='BetaSYWGIndustryIndex', column_type='decimal(18,4)', nullable=False, chn_name='Beta值(相对申万行业,一年)')
    """Beta值(相对申万行业,一年):参考指数的取法：该股票所属的申万行业指数。"""

    BetaWeekly2Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='BetaWeekly2Y', column_type='decimal(18,4)', nullable=False, chn_name='Beta值(两年,周步长)')
    """Beta值(两年,周步长):Beta值（两年,周步长）（BetaWeekly2Y）：Beta=[n∑RXiRi-(∑RXi)*(∑Ri)]／[n∑（RXi^2）-(∑RXi)^2]Ri为步长区间股票增长率Rxi为步长区间基准增长率"""

    AdjustBetaWeekly2Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='AdjustBetaWeekly2Y', column_type='decimal(18,4)', nullable=False, chn_name='调整Beta值(两年,周步长)')
    """调整Beta值(两年,周步长):调整Beta值（两年,周步长）（AdjustBetaWeekly2Y）：BETA值（两年,周步长）*0.67+0.33"""

    AlphaHS300Index: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='AlphaHS300Index', column_type='decimal(18,4)', nullable=False, chn_name='Alpha(相对沪深300,一年)')
    """Alpha(相对沪深300,一年):"""

    AlphaCompositeIndex: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='AlphaCompositeIndex', column_type='decimal(18,4)', nullable=False, chn_name='Alpha(相对综合指数,一年)')
    """Alpha(相对综合指数,一年):参考指数的取法：如在上海交易所上市，则是沪综指；在深圳交易所上市，则是深成指。"""

    AlphaSYWGIndustryIndex: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='AlphaSYWGIndustryIndex', column_type='decimal(18,4)', nullable=False, chn_name='Alpha(相对申万行业,一年)')
    """Alpha(相对申万行业,一年):参考指数的取法：该股票所属的申万行业指数。"""

    Y1Volatility: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='Y1Volatility', column_type='decimal(18,4)', nullable=False, chn_name='波动率σ(一年)')
    """波动率σ(一年):波动率σ(一年)（Y1Volatility）:计算中为日步长数据。"""

    Y1SharpeRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='Y1SharpeRatio', column_type='decimal(18,4)', nullable=False, chn_name='夏普比率(一年)')
    """夏普比率(一年):"""

    MarketIndexROR_ArithAvg: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='MarketIndexROR_ArithAvg', column_type='decimal(18,4)', nullable=False, chn_name='市场收益率(算术平均)')
    """市场收益率(算术平均):市场收益率（算术平均）（MarketIndexROR_ArithAvg）：Rm=（Rm1+Rm2）/2Rm1为上证指数年收益率（算术平均）Rm2为深成指年收益率（算术平均）指数年平均收益率Rxi=(∑（Ri）/10)*100%"""

    ChangePCT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='ChangePCT', column_type='decimal(18,4)', nullable=False, chn_name='涨跌幅(%)')
    """涨跌幅(%):"""

    MarketIndexROR_GeomMean: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='MarketIndexROR_GeomMean', column_type='decimal(18,4)', nullable=False, chn_name='市场收益率(几何平均)')
    """市场收益率(几何平均):市场收益率（几何平均）（MarketIndexROR_GeomMean）：Rm=（Rm1+Rm2）/2Rm1为上证指数年收益率（几何平均）Rm2为深成指年收益率（几何平均）"""

    TotalMV: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TotalMV', column_type='decimal(19,4)', nullable=False, chn_name='总市值(万元)')
    """总市值(万元):"""

    NegotiableMV: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='NegotiableMV', column_type='decimal(19,4)', nullable=False, chn_name='流通市值(万元)')
    """流通市值(万元):"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    RangePCT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='RangePCT', column_type='decimal(18,4)', nullable=False, chn_name='振幅(%)')
    """振幅(%):"""

    TurnoverRate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverRate', column_type='decimal(18,4)', nullable=False, chn_name='换手率(%)')
    """换手率(%):"""

    AvgPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='AvgPrice', column_type='decimal(19,4)', nullable=False, chn_name='均价')
    """均价:"""

    TurnoverValueRW: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverValueRW', column_type='decimal(19,4)', nullable=False, chn_name='周成交金额(万元)')
    """周成交金额(万元):"""

    TurnoverVolumeRW: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverVolumeRW', column_type='decimal(18,4)', nullable=False, chn_name='周成交量(万股)')
    """周成交量(万股):"""

    ChangePCTRW: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='ChangePCTRW', column_type='decimal(18,4)', nullable=False, chn_name='周涨跌幅(%)')
    """周涨跌幅(%):"""

    RangePCTRW: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='RangePCTRW', column_type='decimal(18,4)', nullable=False, chn_name='周振幅(%)')
    """周振幅(%):"""

    TurnoverRateRW: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverRateRW', column_type='decimal(18,4)', nullable=False, chn_name='周换手率(%)')
    """周换手率(%):"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='InnerCode', column_type='int', nullable=True, chn_name='证券内部编码')
    """证券内部编码:证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。"""

    AvgPriceRW: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='AvgPriceRW', column_type='decimal(19,4)', nullable=False, chn_name='周成交均价(元)')
    """周成交均价(元):"""

    HighPriceRW: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='HighPriceRW', column_type='decimal(19,4)', nullable=False, chn_name='周最高价(元)')
    """周最高价(元):"""

    LowPriceRW: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='LowPriceRW', column_type='decimal(19,4)', nullable=False, chn_name='周最低价(元)')
    """周最低价(元):"""

    HighestClosePriceRW: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='HighestClosePriceRW', column_type='decimal(19,4)', nullable=False, chn_name='周收盘最高价(元)')
    """周收盘最高价(元):"""

    LowestClosePriceRW: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='LowestClosePriceRW', column_type='decimal(19,4)', nullable=False, chn_name='周收盘最低价(元)')
    """周收盘最低价(元):"""

    TurnoverValuePerDayRW: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverValuePerDayRW', column_type='decimal(19,4)', nullable=False, chn_name='周日均成交金额(万元)')
    """周日均成交金额(万元):"""

    TurnoverRatePerDayRW: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverRatePerDayRW', column_type='decimal(18,4)', nullable=False, chn_name='周日均换手率(%)')
    """周日均换手率(%):"""

    TurnoverValueTW: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverValueTW', column_type='decimal(19,4)', nullable=False, chn_name='本周以来成交金额(万元)')
    """本周以来成交金额(万元):"""

    TurnoverVolumeTW: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverVolumeTW', column_type='decimal(18,4)', nullable=False, chn_name='本周以来成交量(万股)')
    """本周以来成交量(万股):"""

    ChangePCTTW: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='ChangePCTTW', column_type='decimal(18,4)', nullable=False, chn_name='本周以来涨跌幅(%)')
    """本周以来涨跌幅(%):"""

    TradingDay: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TradingDay', column_type='datetime', nullable=True, chn_name='交易日')
    """交易日:"""

    RangePCTTW: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='RangePCTTW', column_type='decimal(18,4)', nullable=False, chn_name='本周以来振幅(%)')
    """本周以来振幅(%):"""

    TurnoverRateTW: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverRateTW', column_type='decimal(18,4)', nullable=False, chn_name='本周以来换手率(%)')
    """本周以来换手率(%):"""

    AvgPriceTW: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='AvgPriceTW', column_type='decimal(19,4)', nullable=False, chn_name='本周以来成交均价(元)')
    """本周以来成交均价(元):"""

    HighPriceTW: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='HighPriceTW', column_type='decimal(19,4)', nullable=False, chn_name='本周以来最高价(元)')
    """本周以来最高价(元):"""

    LowPriceTW: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='LowPriceTW', column_type='decimal(19,4)', nullable=False, chn_name='本周以来最低价(元)')
    """本周以来最低价(元):"""

    HighestClosePriceTW: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='HighestClosePriceTW', column_type='decimal(19,4)', nullable=False, chn_name='本周以来收盘最高价(元)')
    """本周以来收盘最高价(元):"""

    LowestClosePriceTW: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='LowestClosePriceTW', column_type='decimal(19,4)', nullable=False, chn_name='本周以来收盘最低价(元)')
    """本周以来收盘最低价(元):"""

    TurnoverValuePerDayTW: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverValuePerDayTW', column_type='decimal(19,4)', nullable=False, chn_name='本周以来日均成交金额(万元)')
    """本周以来日均成交金额(万元):"""

    TurnoverRatePerDayTW: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverRatePerDayTW', column_type='decimal(18,4)', nullable=False, chn_name='本周以来日均换手率(%)')
    """本周以来日均换手率(%):"""

    TurnoverValueRM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverValueRM', column_type='decimal(19,4)', nullable=False, chn_name='月成交金额(万元)')
    """月成交金额(万元):"""

    PrevClosePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='PrevClosePrice', column_type='decimal(10,4)', nullable=False, chn_name='昨收盘')
    """昨收盘:"""

    TurnoverVolumeRM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverVolumeRM', column_type='decimal(18,4)', nullable=False, chn_name='月成交量(万股)')
    """月成交量(万股):"""

    ChangePCTRM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='ChangePCTRM', column_type='decimal(18,4)', nullable=False, chn_name='月涨跌幅(%)')
    """月涨跌幅(%):"""

    RangePCTRM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='RangePCTRM', column_type='decimal(18,4)', nullable=False, chn_name='月振幅(%)')
    """月振幅(%):"""

    TurnoverRateRM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverRateRM', column_type='decimal(18,4)', nullable=False, chn_name='月换手率(%)')
    """月换手率(%):"""

    AvgPriceRM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='AvgPriceRM', column_type='decimal(19,4)', nullable=False, chn_name='月成交均价(元)')
    """月成交均价(元):"""

    HighPriceRM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='HighPriceRM', column_type='decimal(19,4)', nullable=False, chn_name='月最高价(元)')
    """月最高价(元):"""

    LowPriceRM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='LowPriceRM', column_type='decimal(19,4)', nullable=False, chn_name='月最低价(元)')
    """月最低价(元):"""

    HighestClosePriceRM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='HighestClosePriceRM', column_type='decimal(19,4)', nullable=False, chn_name='月收盘最高价(元)')
    """月收盘最高价(元):"""

    LowestClosePriceRM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='LowestClosePriceRM', column_type='decimal(19,4)', nullable=False, chn_name='月收盘最低价(元)')
    """月收盘最低价(元):"""

    TurnoverValuePerDayRM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverValuePerDayRM', column_type='decimal(19,4)', nullable=False, chn_name='月日均成交金额(万元)')
    """月日均成交金额(万元):"""

    OpenPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='OpenPrice', column_type='decimal(10,4)', nullable=False, chn_name='今开盘')
    """今开盘:"""

    TurnoverRatePerDayRM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverRatePerDayRM', column_type='decimal(18,4)', nullable=False, chn_name='月日均换手率(%)')
    """月日均换手率(%):"""

    TurnoverValueTM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverValueTM', column_type='decimal(19,4)', nullable=False, chn_name='本月以来成交金额(万元)')
    """本月以来成交金额(万元):"""

    TurnoverVolumeTM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverVolumeTM', column_type='decimal(18,4)', nullable=False, chn_name='本月以来成交量(万股)')
    """本月以来成交量(万股):"""

    ChangePCTTM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='ChangePCTTM', column_type='decimal(18,4)', nullable=False, chn_name='本月以来涨跌幅(%)')
    """本月以来涨跌幅(%):"""

    RangePCTTM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='RangePCTTM', column_type='decimal(18,4)', nullable=False, chn_name='本月以来振幅(%)')
    """本月以来振幅(%):"""

    TurnoverRateTM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverRateTM', column_type='decimal(18,4)', nullable=False, chn_name='本月以来换手率(%)')
    """本月以来换手率(%):"""

    AvgPriceTM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='AvgPriceTM', column_type='decimal(19,4)', nullable=False, chn_name='本月以来成交均价(元)')
    """本月以来成交均价(元):"""

    HighPriceTM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='HighPriceTM', column_type='decimal(19,4)', nullable=False, chn_name='本月以来最高价(元)')
    """本月以来最高价(元):"""

    LowPriceTM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='LowPriceTM', column_type='decimal(19,4)', nullable=False, chn_name='本月以来最低价(元)')
    """本月以来最低价(元):"""

    HighestClosePriceTM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='HighestClosePriceTM', column_type='decimal(19,4)', nullable=False, chn_name='本月以来收盘最高价(元)')
    """本月以来收盘最高价(元):"""

    HighPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='HighPrice', column_type='decimal(10,4)', nullable=False, chn_name='最高价')
    """最高价:综合评级（CompositeRating）：根据综合投资评级分数，确定归属于哪一类投资评级。[1.0， 1.5)-卖出，[1.5， 2.5)-减持，[2.5， 3.5)-中性，[3.5， 4.5)-增持，[4.5， 5.0]-买入。"""

    LowestClosePriceTM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='LowestClosePriceTM', column_type='decimal(19,4)', nullable=False, chn_name='本月以来收盘最低价(元)')
    """本月以来收盘最低价(元):"""

    TurnoverValuePerDayTM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverValuePerDayTM', column_type='decimal(19,4)', nullable=False, chn_name='本月以来日均成交金额(万元)')
    """本月以来日均成交金额(万元):"""

    TurnoverRatePerDayTM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverRatePerDayTM', column_type='decimal(18,4)', nullable=False, chn_name='本月以来日均换手率(%)')
    """本月以来日均换手率(%):"""

    TurnoverValueR3M: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverValueR3M', column_type='decimal(19,4)', nullable=False, chn_name='三个月成交金额(万元)')
    """三个月成交金额(万元):"""

    TurnoverVolumeR3M: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverVolumeR3M', column_type='decimal(18,4)', nullable=False, chn_name='三个月成交量(万股)')
    """三个月成交量(万股):"""

    ChangePCTR3M: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='ChangePCTR3M', column_type='decimal(18,4)', nullable=False, chn_name='三个月涨跌幅(%)')
    """三个月涨跌幅(%):"""

    RangePCTR3M: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='RangePCTR3M', column_type='decimal(18,4)', nullable=False, chn_name='三个月振幅(%)')
    """三个月振幅(%):"""

    TurnoverRateR3M: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverRateR3M', column_type='decimal(18,4)', nullable=False, chn_name='三个月换手率(%)')
    """三个月换手率(%):"""

    TurnoverValueR6M: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverValueR6M', column_type='decimal(19,4)', nullable=False, chn_name='六个月成交金额(万元)')
    """六个月成交金额(万元):"""

    TurnoverVolumeR6M: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverVolumeR6M', column_type='decimal(18,4)', nullable=False, chn_name='六个月成交量(万股)')
    """六个月成交量(万股):"""

    LowPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='LowPrice', column_type='decimal(10,4)', nullable=False, chn_name='最低价')
    """最低价:"""

    ChangePCTR6M: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='ChangePCTR6M', column_type='decimal(18,4)', nullable=False, chn_name='六个月涨跌幅(%)')
    """六个月涨跌幅(%):"""

    RangePCTR6M: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='RangePCTR6M', column_type='decimal(18,4)', nullable=False, chn_name='六个月振幅(%)')
    """六个月振幅(%):"""

    TurnoverRateR6M: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverRateR6M', column_type='decimal(18,4)', nullable=False, chn_name='六个月换手率(%)')
    """六个月换手率(%):"""

    TurnoverValueR12M: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverValueR12M', column_type='decimal(19,4)', nullable=False, chn_name='十二个月成交金额(万元)')
    """十二个月成交金额(万元):"""

    TurnoverVolumeR12M: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverVolumeR12M', column_type='decimal(18,4)', nullable=False, chn_name='十二个月成交量(万股)')
    """十二个月成交量(万股):"""

    ChangePCTR12M: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='ChangePCTR12M', column_type='decimal(18,4)', nullable=False, chn_name='十二个月涨跌幅(%)')
    """十二个月涨跌幅(%):"""

    RangePCTR12M: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='RangePCTR12M', column_type='decimal(18,4)', nullable=False, chn_name='十二个月振幅(%)')
    """十二个月振幅(%):"""

    TurnoverRateR12M: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverRateR12M', column_type='decimal(18,4)', nullable=False, chn_name='十二个月换手率(%)')
    """十二个月换手率(%):"""

    AvgPriceR12M: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='AvgPriceR12M', column_type='decimal(19,4)', nullable=False, chn_name='十二个月成交均价(元)')
    """十二个月成交均价(元):"""

    HighPriceR12M: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='HighPriceR12M', column_type='decimal(19,4)', nullable=False, chn_name='十二个月最高价(元)')
    """十二个月最高价(元):"""

    ClosePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='ClosePrice', column_type='decimal(10,4)', nullable=False, chn_name='收盘价')
    """收盘价:"""

    LowPriceR12M: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='LowPriceR12M', column_type='decimal(19,4)', nullable=False, chn_name='十二个月最低价(元)')
    """十二个月最低价(元):"""

    HighestClosePriceR12M: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='HighestClosePriceR12M', column_type='decimal(19,4)', nullable=False, chn_name='十二个月收盘最高价(元)')
    """十二个月收盘最高价(元):"""

    LowestClosePriceR12M: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='LowestClosePriceR12M', column_type='decimal(19,4)', nullable=False, chn_name='十二个月收盘最低价(元)')
    """十二个月收盘最低价(元):"""

    TurnoverValuePerDayR12M: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverValuePerDayR12M', column_type='decimal(19,4)', nullable=False, chn_name='十二个月日均成交金额(万元)')
    """十二个月日均成交金额(万元):"""

    TurnoverRatePerDayR12M: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverRatePerDayR12M', column_type='decimal(18,4)', nullable=False, chn_name='十二个月日均换手率(%)')
    """十二个月日均换手率(%):"""

    TurnoverValueYTD: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverValueYTD', column_type='decimal(19,4)', nullable=False, chn_name='今年以来成交金额(万元)')
    """今年以来成交金额(万元):"""

    TurnoverVolumeYTD: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverVolumeYTD', column_type='decimal(18,4)', nullable=False, chn_name='今年以来成交量(万股)')
    """今年以来成交量(万股):"""

    ChangePCTYTD: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='ChangePCTYTD', column_type='decimal(18,4)', nullable=False, chn_name='今年以来涨跌幅(%)')
    """今年以来涨跌幅(%):"""

    RangePCTYTD: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='RangePCTYTD', column_type='decimal(18,4)', nullable=False, chn_name='今年以来振幅(%)')
    """今年以来振幅(%):"""

    TurnoverRateYTD: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverRateYTD', column_type='decimal(18,4)', nullable=False, chn_name='今年以来换手率(%)')
    """今年以来换手率(%):"""

    TurnoverVolume: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverVolume', column_type='decimal(18,4)', nullable=False, chn_name='成交量(万股)')
    """成交量(万股):"""

    AvgPriceYTD: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='AvgPriceYTD', column_type='decimal(19,4)', nullable=False, chn_name='今年以来成交均价(元)')
    """今年以来成交均价(元):"""

    HighPriceYTD: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='HighPriceYTD', column_type='decimal(19,4)', nullable=False, chn_name='今年以来最高价(元)')
    """今年以来最高价(元):"""

    LowPriceYTD: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='LowPriceYTD', column_type='decimal(19,4)', nullable=False, chn_name='今年以来最低价(元)')
    """今年以来最低价(元):"""

    HighestClosePriceYTD: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='HighestClosePriceYTD', column_type='decimal(19,4)', nullable=False, chn_name='今年以来收盘最高价(元)')
    """今年以来收盘最高价(元):"""

    LowestClosePriceYTD: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='LowestClosePriceYTD', column_type='decimal(19,4)', nullable=False, chn_name='今年以来收盘最低价(元)')
    """今年以来收盘最低价(元):"""

    TurnoverValuePerDayYTD: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverValuePerDayYTD', column_type='decimal(19,4)', nullable=False, chn_name='今年以来日均成交金额(万元)')
    """今年以来日均成交金额(万元):"""

    TurnoverRatePerDayYTD: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='TurnoverRatePerDayYTD', column_type='decimal(18,4)', nullable=False, chn_name='今年以来日均换手率(%)')
    """今年以来日均换手率(%):"""

    HighestAdjustedPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='HighestAdjustedPrice', column_type='decimal(19,4)', nullable=False, chn_name='上市以来后复权最高价(元)')
    """上市以来后复权最高价(元):"""

    HighestAdjustedPriceDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='HighestAdjustedPriceDate', column_type='datetime', nullable=False, chn_name='上市以来后复权最高价时间')
    """上市以来后复权最高价时间:"""

    BetaHS300Index: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_Performance', column_name='BetaHS300Index', column_type='decimal(18,4)', nullable=False, chn_name='Beta值(相对沪深300,一年)')
    """Beta值(相对沪深300,一年):"""

