# -*- coding: utf-8 -*-
import logging
import time
import warnings
from datetime import date

from gs_research_workflow.time_series.data.quandl_wrapper import QuandlData
from gs_research_workflow.time_series.data.tushare_wrapper import TuShareProData
from gs_research_workflow.time_series.data.yfinance_wrapper import yFinanceData

logger = logging.getLogger(__name__)
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")

# import os
# os.environ["http_proxy"] = "http://proxy.graphstrategist.com:8000/"
# os.environ["https_proxy"] = "http://proxy.graphstrategist.com:8000/"



import tushare as ts
import tensorflow as tf



# global_count = 0
#
# def symbol_to_tf_data(x:tf.Tensor):
#     logger.info(f"{x.name} - {x.device} - {x.op} - {type(x)}")
#     str_x = tf.strings.format("{}",x)
#     logger.info(str_x)
#     return tf.data.Dataset.from_tensors(x+"3")
#
#
# def test_tf_map_f2(x: tf.Tensor) -> str:
#     global global_count
#     str_x = x.numpy().decode("utf-8").upper()
#     # 这里增加从 tushare 代码取得数据的接口
#     logger.info(f"{global_count} : {str_x}")
#     global_count += 1
#     return str_x + "-" # for map
#
#
# def test_tf_dataset():
#     symbols = tf.constant([str(600000+i) for i in range(6)])  # 模拟产生股票代码
#     symbol_dataset = tf.data.Dataset.from_tensor_slices(symbols)
#     symbol_dataset = symbol_dataset.map(lambda x: tf.py_function(func=test_tf_map_f2, inp=[x], Tout=tf.string))
#     # symbol_dataset = symbol_dataset.interleave(lambda x: tf.py_function(func=test_tf_map_f2, inp=[x], Tout=tf.data.Dataset))
#     symbol_dataset = symbol_dataset.repeat().shuffle(6)
#
#     for line in symbol_dataset.take(50):
#         print(line)
#
#     # print(symbols)
#     # print(symbol_dataset)
#
#
# class IndexGen:
#     def __init__(self):
#         self.ls_all = [str(600000+i) for i in range(6)]
#
#     def __call__(self, *args, **kwargs):
#         global global_count
#         for i in self.ls_all:
#             logger.info(f"[{global_count}] in gen : {i}")
#             global_count += 1
#             yield i
#
#
# def test_from_gen():
#     gen = IndexGen()
#     symbol_dataset = tf.data.Dataset.from_generator(gen, tf.string, tf.TensorShape(None))
#     symbol_dataset = symbol_dataset.repeat().shuffle(6)
#
#     for line in symbol_dataset.take(50):
#         print(line)

# https://www.quora.com/Using-Python-whats-the-best-way-to-get-stock-data

def test_tushare():
    stk_hist_data = ts.get_hist_data("600050")
    print(stk_hist_data)


def test_tushare_pro():
    pro = ts.pro_api("8fe0d951588bf9b605de2cdce4a7b35a61c79ed3c6e128302dcca142")
    df = pro.daily(ts_code='000001.SH', start_date='20190101', end_date='20191021')
    # df = pro.income(ts_code='600000.SH', start_date='20180101', end_date='20180730')
                    # fields='ts_code,ann_date,f_ann_date,end_date,report_type,comp_type,basic_eps,diluted_eps')
    # df = pro.cctv_news(date="20191015")
    # df = pro.index_daily(ts_code='000001.SH', start_date='20190101', end_date='20191021')
    print(df)
    # print(df.columns)


def test_alpha_vantage():
    api_key = "01EDD3ZW8JQNC2J2"
    from alpha_vantage.timeseries import TimeSeries
    ts = TimeSeries(key=api_key, output_format='pandas')

    # Get json object with the intraday data and information of the data
    # intraday_data, data_info = ts.get_intraday('GOOGL', outputsize='full', interval='1min')
    # intraday_data, data_info = ts.get_intraday('600000.ss', outputsize='full', interval='1min')
    intraday_data, data_info = ts.get_daily('GOOGL', outputsize='full')
    print(intraday_data)
    print(data_info)

#

def test_quandl():
    # import quandl
    # data = quandl.get("WIKI/KO", start_date="1990-01-01", end_date="2018-01-01", api_key="XUzye-X4s_TdWhuM5Y5Y")
    # data = quandl.get("EOD/MSFT", start_date="1990-01-01", end_date="2018-01-01", api_key="XUzye-X4s_TdWhuM5Y5Y")
    # data = quandl.get("NASDAQOMX/XQC", start_date="1990-01-01", end_date="2018-01-01", api_key="XUzye-X4s_TdWhuM5Y5Y")
    # data = quandl.get("ODA/ALB_LP", start_date="1990-01-01", end_date="2018-01-01", api_key="XUzye-X4s_TdWhuM5Y5Y")
    quandl = QuandlData()
    # data = quandl.get_daily_data("ODA","ALB_LP")
    data = quandl.get_daily_data("ODA", "NRU_BCA_NGDPD")
    print(data)

def test_yahoo():
    # yahoo = yFinanceData()
    # df = yahoo.history("MSFT")
    # print(df)

    import yfinance as yf
    spdb = yf.Ticker("MSFT")
    df = spdb.history(start="2019-01-01",end="2019-01-30")
    print(df)
    print(df.columns)
    # print(df.rename_axis("date"))
    # print(spdb.history(period="1d",interval="1m"))
    # print(spdb.get_financials())
    # print(spdb.dividends)
    # print(spdb.actions)
    # print(spdb.sustainability)
    # print(spdb.options)
    # print(spdb.get_balance_sheet(proxy="http://proxy.graphstrategist.com:8000/"))

    # data = yf.download('HDFCBANK.NS', '2016-01-01', '2019-01-01')
    # print(data)

def test_tushare_wrapper():
    tushare = TuShareProData()
    # df = tushare.mkt_quotation_daily("000002.SZ", start=date(2019, 1, 3), end=date(2019, 10, 16),
    #                                  cols=["open", "high", "low"])
    # print(df)
    # df = tushare.mkt_quotation_daily("600001.SH")
    # df = tushare.income("600000.SH")
    df = tushare.equity_basic_daily("600000.SH")
    # run_start = time.time()
    # for _ in range(3000):
    #     df = tushare.mkt_quotation_daily("600000.SH", start=date(2019, 1, 3), end=date(2019, 10, 19),
    #                                      cols=["open", "high", "low"])
    # print(f"query time : {time.time() - run_start} secs ")

    # tushare.mkt_qutation_daily("600000.SH")
    # tushare.test_read_arctic("600000.SH")
    # print(tushare.mkt_qutation_daily("000001.SZ"))
    # print(df)
    # tushare.test_refresh_data("600000.SH")


    # df = tushare._read_period("tushare_daily_per_symbol", "600000.SH", date(2019, 1, 1), date(2019, 12, 12))
    print(df.transpose())


def test_join_by_t():
    tushare = TuShareProData()
    start = date(2019, 1, 3)
    end = date(2019, 10, 19)
    cols = ["open", "high", "low"]
    df1 = tushare.equity_quotation_daily("600000.SH", start=start, end=end, cols=cols)
    df2 = tushare.equity_quotation_daily("600028.SH", start=start, end=end, cols=cols)
    df3 = tushare.equity_quotation_daily("600050.SH", start=start, end=end, cols=cols)
    df4 = tushare.index_quotation_daily("000001.SH", start=start, end=end, cols=["close"])
    df = df4.join(df3, rsuffix="_600050.SH").join(df2, rsuffix="_600028.SH").join(df1, rsuffix="_600000.SH")
    print(df[df.columns[0]][0:20].to_numpy())
    print(df.iloc[0:20, 1:].to_numpy())
    print(df)
    # print(df.iloc[1:,:])
    # print(df[1:-1, 0:20])

    # print(df1)
    # print(df2)
    # print(df3)
    # print(df4)
    

# eikon , https://developers.refinitiv.com/eikon-apis/eikon-data-apis/qa
# interactive broker
# fxcmpy ， 外汇数据

if __name__ == "__main__":
    # test_tf_dataset()
    # test_from_gen()
    # test_tushare()
    # test_yahoo()
    # test_google_finance()
    # test_quandl()
    # test_tushare_pro()
    # test_alpha_vantage()
    test_tushare_wrapper()
    # test_join_by_t()
