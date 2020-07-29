# -*- coding: UTF-8 -*-

"""
将一些TS的历史数据导入 mongo 以便于 tableau 出相关的图
"""
import logging
from datetime import datetime
from typing import List

from gs_framework.gs_resource import set_http_proxy
from gs_framework.utilities import md5_str

from gs_research_workflow.common.mongo_resource import mongo_db_conn, used_db_position, db_nlp

from gs_research_workflow.nlp.data.docs_in_mongo import FinancialInstrumentSymbol, SymbolDataFromYahoo, \
    FinancialInstrumentDailyMarketData, FinancialInstrumentDividends, FinancialInstrumentHolders, \
    FinancialInstrumentRecommendInYahoo, GlobalEntity, FinancialInstrumentCalendarFromYahoo
from gs_research_workflow.rpa_workflow.actions.kw_actions import logger, ALL_US_SYMBOLS, ALL_HK_SYMBOLS, \
    ALL_HK_SYMBOLS_WITH_NAME, ALL_CN_SYMBOLS
from gs_research_workflow.rpa_workflow.result_extraction.utilities import upsert_document
from gs_research_workflow.time_series.data.akshare_wrapper import akshareData
from gs_research_workflow.time_series.data.tushare_wrapper import TuShareProData

from gs_research_workflow.time_series.data.yfinance_wrapper import yFinanceData

logger = logging.getLogger(__name__)


def symbol_to_yahoo_symbol(s: str) -> str:
    # NOTE: yahoo 的 港股数据没有升位，这里为了兼容，需要去掉首位'0'
    if s.endswith(".HK") and len(s) == 8:
        return s[1:]
    return s


def upsert_yahoo_financial_instrument_info(symbol: str, insert_only: bool = False):
    if insert_only:
        symbol_obj = FinancialInstrumentSymbol.objects(symbol=symbol, info_from_yahoo__exists=True).first()
        if symbol_obj is not None:
            return

    set_http_proxy()
    import yfinance as yf

    symbol_data = yf.Ticker(symbol_to_yahoo_symbol(symbol))
    try:
        dict_info = symbol_data.info
    except Exception as ex:
        logger.error(f"api exception when get {symbol} data , {ex}")
        return

    # remove : companyOfficers =  # <class 'list'>
    if "companyOfficers" in dict_info:
        del dict_info["companyOfficers"]

    # remove symbol , 重复数据
    if "symbol" in dict_info:
        del dict_info["symbol"]

    # rename "52WeekChange" -> "fiftyTwoWeekChange" , python 变量首字符不允许数字
    if "52WeekChange" in dict_info:
        dict_info["fiftyTwoWeekChange"] = dict_info["52WeekChange"]
        del dict_info["52WeekChange"]

    # rename "yield" -> "yieldVal" , python 关键字
    if "yield" in dict_info:
        dict_info["yieldVal"] = dict_info["yield"]
        del dict_info["yield"]
    if "err" in dict_info:
        del dict_info["err"]
    dict_info["mtime"] = datetime.now()

    fin_symbol = FinancialInstrumentSymbol(symbol=symbol)
    fin_symbol.info_from_yahoo = SymbolDataFromYahoo(**dict_info)
    upsert_document(fin_symbol)


def upsert_chn_stock_info_in_yahoo():
    set_http_proxy()
    tushare = TuShareProData()
    df = tushare.stock_basic(exchange="SSE", cols=["ts_code", "name"])
    for idx, row in df.iterrows():
        symbol = row["ts_code"].replace("SH", "SS")  # YAHOO 上海股市的后缀是 SS
        logger.info(f"[{idx}] {symbol}({row['name']}) symbol data in yahoo")
        upsert_yahoo_financial_instrument_info(symbol, True)

    df = tushare.stock_basic(exchange="SZSE", cols=["ts_code", "name"])
    for idx, row in df.iterrows():
        symbol = row["ts_code"]  # 深圳股市的后缀是相同的
        logger.info(f"[{idx}] {symbol}({row['name']}) symbol data in yahoo")
        upsert_yahoo_financial_instrument_info(symbol, True)


def upsert_chn_stock_name():
    tushare = TuShareProData()
    df = tushare.stock_basic(exchange="SSE", cols=["ts_code", "name"])
    for idx, row in df.iterrows():
        symbol = row["ts_code"].replace("SH", "SS")  # YAHOO 上海股市的后缀是 SS
        symbol_obj = FinancialInstrumentSymbol(symbol=symbol,full_name=row['name'])
        upsert_document(symbol_obj,False)

    df = tushare.stock_basic(exchange="SZSE", cols=["ts_code", "name"])
    for idx, row in df.iterrows():
        symbol = row["ts_code"]  # 深圳股市的后缀是相同的
        symbol_obj = FinancialInstrumentSymbol(symbol=symbol,full_name=row['name'])
        upsert_document(symbol_obj,False)


def all_chn_symbols() -> List[str]:
    symbols = FinancialInstrumentSymbol.objects(info_from_yahoo__market="cn_market").order_by("symbol").only("symbol")
    return [x.symbol for x in symbols]


def upsert_daily_market_data(symbol: str, start_t: datetime):
    yahoo_ts = yFinanceData()
    df = yahoo_ts.history(symbol_to_yahoo_symbol(symbol), start=start_t)
    logger.info(f"upsert_daily_market_data : {symbol}-{df.shape}")
    df["fifty_two_week_high"] = df["Close"].rolling(window=244).max()
    df["fifty_two_week_low"] = df["Close"].rolling(window=244).min()

    for t, row in df.iterrows():
        dict_info = {"t": t, "open": row["Open"], "high": row["High"], "low": row["Low"], "close": row["Close"],
                     "volume": row["Volume"], "dividends": row["Dividends"], "splits": row["Stock Splits"],
                     "fifty_two_week_low": row["fifty_two_week_low"], "fifty_two_week_high": row["fifty_two_week_high"],
                     "symbol": FinancialInstrumentSymbol(symbol=symbol), "uid": md5_str(f"{t.isoformat()}-{symbol}")}
        upsert_document(FinancialInstrumentDailyMarketData(**dict_info))


def upsert_dividends(symbol: str, start_t: datetime):
    yahoo_ts = yFinanceData()
    try:
        df = yahoo_ts.dividends(symbol_to_yahoo_symbol(symbol), start=start_t)
        logger.info(f"upsert_dividends : {symbol}-{df.shape}")
        for t, row in df.iterrows():
            dict_info = {"t": t, "divident": row["Dividends"],
                         "symbol": FinancialInstrumentSymbol(symbol=symbol), "uid": md5_str(f"{t.isoformat()}-{symbol}")}
            upsert_document(FinancialInstrumentDividends(**dict_info))
    except:
        return


def upsert_splits(symbol: str, start_t: datetime):
    yahoo_ts = yFinanceData()
    try:
        df = yahoo_ts.splits(symbol_to_yahoo_symbol(symbol), start=start_t)
        logger.info(f"upsert_splits : {symbol}-{df.shape}")
        for t, row in df.iterrows():
            dict_info = {"t": t, "split": row["Stock Splits"],
                         "symbol": FinancialInstrumentSymbol(symbol=symbol),
                         "uid": md5_str(f"{t.isoformat()}-{symbol}")}
            upsert_document(FinancialInstrumentDividends(**dict_info))
    except:
        return


def upsert_yahoo_symbol_holder(symbol: str):
    import yfinance as yf
    symbol_data = yf.Ticker(symbol_to_yahoo_symbol(symbol))
    try:
        df = symbol_data.institutional_holders
        logger.info(f"upsert_yahoo_symbol_holder : {symbol} {df.shape}")
        for idx, row in df.iterrows():
            t = row["Date Reported"]
            dict_info = {"t": t,
                         "symbol": FinancialInstrumentSymbol(symbol=symbol),
                         "holder": GlobalEntity(entity_id=row["Holder"]),
                         "shares": row["Shares"],
                         "value": row["Value"],
                         "percentage_out": row["% Out"],
                         "uid": md5_str(f"{t.isoformat()}-{symbol}-{row['Holder']}")}
            upsert_document(FinancialInstrumentHolders(**dict_info), True)
    except Exception as ex:
        logger.error(f"api exception when get data , {ex}")


def upsert_yahoo_recommend(symbol: str):
    yahoo_ts = yFinanceData()
    try:
        df = yahoo_ts.recommendations(symbol_to_yahoo_symbol(symbol))
        logger.info(f"upsert_yahoo_recommend : {symbol}-{df.shape}")
        for t, row in df.iterrows():
            firm = GlobalEntity(entity_id=row["Firm"])
            dict_info = {"t": t,
                         "symbol": FinancialInstrumentSymbol(symbol=symbol),
                         "firm": firm,
                         "uid": md5_str(f"{t.isoformat()}-{symbol}-{row['Firm']}"),
                         "to_grade": None if row["To Grade"] == "" else row["To Grade"],
                         "from_grade": None if row["From Grade"] == "" else row["From Grade"],
                         "action": None if row["Action"] == "" else row["Action"]
                         }
            upsert_document(firm)
            upsert_document(FinancialInstrumentRecommendInYahoo(**dict_info), False)
    except Exception as ex:
        logger.error(ex)
        return


def _convert_non_t_v(v):
    if pd.isna(v) or v is None:
        return None
    if v == pd.NaT:
        return None
    return v


def upsert_yahoo_earning_analysis(symbol: str):
    """see https://finance.yahoo.com/quote/MSFT/analysis?p=MSFT"""
    import yfinance as yf
    symbol_data = yf.Ticker(symbol_to_yahoo_symbol(symbol))
    try:
        df = symbol_data.calendar.T
        logger.info(f"upsert_yahoo_earning_analysis : {symbol}  {df.shape}")
        for idx, row in df.iterrows():
            t = row["Earnings Date"]
            dict_info = {"t": t,
                         "symbol": FinancialInstrumentSymbol(symbol=symbol),
                         "earnings_average": _convert_non_t_v(row["Earnings Average"]),
                         "earnings_low": _convert_non_t_v(row["Earnings Low"]),
                         "earnings_high": _convert_non_t_v(row["Earnings High"]),
                         "revenue_average": _convert_non_t_v(row["Revenue Average"]),
                         "revenue_low": _convert_non_t_v(row["Revenue Low"]),
                         "revenue_high": _convert_non_t_v(row["Revenue High"]),
                         "uid": md5_str(f"{t.isoformat()}-{symbol}")}
            upsert_document(FinancialInstrumentCalendarFromYahoo(**dict_info), True)
    except Exception as ex:
        logger.error(f"api exception when get data , {ex}")


def set_symbol_important_flag(symbol: str):
    symbol_doc = FinancialInstrumentSymbol(symbol=symbol, important=True)
    upsert_document(symbol_doc)


def set_hk_stock_chn_name():
    for symbol, chn_name in ALL_HK_SYMBOLS_WITH_NAME:
        fin_data = FinancialInstrumentSymbol(symbol=symbol, full_name=chn_name)
        upsert_document(fin_data)
        # logger.info(f"{symbol}-{chn_name}")


def upsert_us_stock_nametable_and_chn_name():
    akshare_data = akshareData()
    df_us_stocks = akshare_data.get_us_stock_name()
    logger.info(f"table shape:{df_us_stocks.shape}")
    for idx, row in df_us_stocks.iterrows():
        if idx <= 9425:
            continue
        symbol = row["symbol"]
        chn_name = row["cname"]
        eng_name = row["name"]
        logger.info(f"[{idx}] {symbol} - {chn_name} - {eng_name}")
        fin_data = FinancialInstrumentSymbol(symbol=symbol, full_name=eng_name, eng_name=eng_name, chn_name=chn_name)
        upsert_document(fin_data)
        upsert_yahoo_financial_instrument_info(symbol, True)


# NOTE:东方财富的美股研报已经不更新了

if __name__ == "__main__":
    import pandas as pd
    pd.set_option('display.max_rows', 200)
    pd.set_option('display.max_columns', None)

    set_http_proxy()
    mongo_db_conn(used_db_position, db_nlp)
    upsert_us_stock_nametable_and_chn_name()

    # set_hk_stock_chn_name()

    # print([symbol_to_yahoo_symbol(x) for x in ALL_HK_SYMBOLS])
    # print(symbol_to_yahoo_symbol("AAPL"))

    # for i, symbol in enumerate(ALL_US_SYMBOLS):
    # for i, symbol in enumerate(ALL_HK_SYMBOLS):
    # for i, symbol in enumerate(ALL_CN_SYMBOLS):
    #     logger.info("-"*30)
    #     logger.info(f"[{i}] upsert '{symbol}' data")
    #     upsert_yahoo_financial_instrument_info(symbol, False)
    #     upsert_daily_market_data(symbol, datetime(2000, 1, 1))
    #     upsert_dividends(symbol, datetime(1970, 1, 1))
    #     upsert_splits(symbol, datetime(1970, 1, 1))
    #     upsert_yahoo_symbol_holder(symbol)
    #     upsert_yahoo_recommend(symbol)
    #     upsert_yahoo_earning_analysis(symbol)
    #     set_symbol_important_flag(symbol)

    # yahoo_ts = yFinanceData()
    # df = yahoo_ts.recommendations("AAPL")
    # print(df)
    # print(f"To Grade: {df['To Grade'].unique()}")
    # print(f"From Grade: {df['From Grade'].unique()}")
    # print(f'Action:{df["Action"].unique()}')

    # 目前需要从yahoo导入的数据
    # (1) info 基本数据 *
    # (2) history 历史数据 *
    # (3) dividends 股息数据
    # (4) splits 股票拆分数据
    # (5) institutional_holders 机构持有人数据，只有一期数据
    # (6) recommendations 机构的买入卖出推荐数据
    # (7) calendar 数据

    # import yfinance as yf
    #
    # # symbol_data = yf.Ticker("1113.HK")
    # symbol_data = yf.Ticker("600050.SS")
    # # symbol_data = yf.Ticker("MSFT")
    # # symbol_data = yf.Ticker("GSX")
    # try:
    #     ser = symbol_data.info
    #     # ser = symbol_data.history(period="max")
    #     # ser = symbol_data.dividends
    #     # ser = symbol_data.splits # NONE for hk,cn
    #     # ser = symbol_data.institutional_holders # none for cn
    #     # ser = symbol_data.recommendations # NONE for hk,cn
    #     # ser = symbol_data.calendar # NONE for HK
    #     print(ser)
        # print(type(ser))
        # print(ser.T)
        # print(ser.T.columns)

        # print(ser.to_frame().loc[datetime(1900, 1, 1).strftime("%Y-%m-%d"):datetime(2022, 1, 1).strftime("%Y-%m-%d")])
        # dict_info = symbol_data.info
        # print(symbol_data.institutional_holders)
        # print(symbol_data.options)
    # except Exception as ex:
    #     logger.error(f"api exception when get data , {ex}")
