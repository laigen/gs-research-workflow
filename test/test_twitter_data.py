# -*- coding: UTF-8 -*-
from datetime import datetime
import logging

from gs_framework.gs_resource import set_http_proxy

from gs_research_workflow.rpa_workflow.result_extraction.eastmoney import EastMoneyDataProcess
from gs_research_workflow.time_series.data.tushare_wrapper import TuShareProData

from gs_research_workflow.time_series.data.yfinance_wrapper import yFinanceData

from gs_research_workflow.rpa_workflow.act_msg_data import ActionResultBinary
from gs_research_workflow.rpa_workflow.envs.general_rpa_action_assign_to_run import GeneralRPAActionExecutionEnv
import pandas as pd

from gs_research_workflow.rpa_workflow.result_extraction.seeking_alpha import SeekingAlphaDataProcess

logger = logging.getLogger(__name__)


def debug_one_action_result(action_uuid: str):
    rlt_bin_data = None
    rlt_bin_doc = ActionResultBinary.objects.get(action_uuid=action_uuid)
    rlt_bin_data = rlt_bin_doc.bin
    logger.info(f"bin data result length={len(rlt_bin_data)}")
    GeneralRPAActionExecutionEnv.proc_action_result(action_uuid, rlt_bin_data)

# debug_one_action_result("652B2988BF6D4775BD7DC09C9D6E5A2C")

# print(datetime.now().isoformat())


if __name__ == "__main__":
    pd.set_option("display.max_rows", 20)
    pd.set_option("display.max_columns", None)

    # EastMoneyDataProcess.symbol_analysis_report("/tmp/laigen/debug_data/eastmoney_stock_analysis", "manually_import",
    #                                             True)

    # f = "/tmp/laigen/debug_data/eastmoney_stock_analysis/20200528_224650_symbol_analysis.csv"
    # df_from_csv = pd.read_csv(f, header=0)
    # df = EastMoneyDataProcess.proc_stock_analysis(df_from_csv)
    # print(df)
    # print(df.columns)

    # set_http_proxy()

    import yfinance as yf
    import json


    # df[f"{col.out_col_prefix}high_low_ret_52weeks"] = (df[col.adj_auto_close].rolling(window=244).max() / df[
    #     col.adj_auto_close].rolling(window=244).min() - 1.0) * 100.

    # print(f"52week_high:{df['Close'].rolling(window=244).max()[-1]}")
    # print(f"52week_low:{df['Close'].rolling(window=244).min()[-1]}")



# api exception when get XNY data , 'regularMarketOpen'
# api exception when get XOM data , list index out of range
#     tushare = TuShareProData()
    # print(tushare.stock_basic(exchange="SZSE",cols=["ts_code","name"]))
    # print(tushare.stock_basic(exchange="SSE", cols=["ts_code", "name"]))
    # df = tushare.stock_basic(exchange="SSE", cols=["ts_code", "name"])
    # for idx, row in df.iterrows():
    #     symbol = row["ts_code"].replace("SH", "SS")
    #     print(symbol)

    # msft = yf.Ticker("600000.SS")
    # msft = yf.Ticker("002001.SZ")
    # msft = yf.Ticker("000001.SZ")
    # msft = yf.Ticker("MSFT")
    # dict_info = msft.info
    # print(json.dumps(dict_info))

    # for k,v in dict_info.items():
    #     if v is None:
    #         print(f"{k} = StringField() #???")
    #     elif isinstance(v, str):
    #         print(f"{k} = StringField()")
    #     elif isinstance(v, int):
    #         print(f"{k} = IntField()")
    #     elif isinstance(v, float):
    #         print(f"{k} = FloatField()")
    #     else:
    #         print(f"{k} = #{type(v)}")
    #     print(dict_info.keys())

    # print(msft.financials)

    # tickers = yf.Tickers('msft aapl goog')
    # print(tickers.msft.info)

    pass
    # f = "/tmp/laigen/debug_data/seeking_alpha_symbol_summary_action/20200525_144910_symbol_analysis.csv"
    # SeekingAlphaDataProcess.symbol_summary("/tmp/laigen/debug_data/seeking_alpha_symbol_summary_action", "test_batch_seeking_alpha",
    #                                        True)
    # df_from_csv = pd.read_csv(f, header=0, parse_dates=["extract_t"])
    # symbol, df_rlt = SeekingAlphaDataProcess.proc_symbol_analysis(df_from_csv)
    # print(df_rlt)
