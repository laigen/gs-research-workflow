# -*- coding: UTF-8 -*-
from datetime import date

import pandas as pd
import tushare as ts

from gs_research_workflow.time_series.data.tushare_wrapper import TuShareProData
from gs_research_workflow.time_series.data.utilities import val_convert_to_zscore

ts_pro = ts.pro_api("8fe0d951588bf9b605de2cdce4a7b35a61c79ed3c6e128302dcca142")
gs_ts_pro = TuShareProData(use_l3_cache=True)

# 带有 t 的 category 的格式应该为：(date , category , Set[symbol])
#
#
# 方法一： 先只传 symbol , 在 loop 的时候 random 出几个 属于某个 category 的类

def test_equity_concept():
    df_j1 = gs_ts_pro.cs_equity_quotation_daily(start=None, end=date(2019, 12, 31), look_period=10)
    df_j2 = gs_ts_pro.cs_equity_adj_factor(start=None, end=date(2019, 12, 31), look_period=10)
    dfI = gs_ts_pro.cs_equity_basic_daily(start=None, end=date(2019, 12, 31), look_period=10, cols=["pe"])
    # df = gs_ts_pro.cs_equity_moneyflow(start=None, end=date(2019, 12, 31), look_period=10)
    # df = gs_ts_pro.cs_equity_margin_detail(start=None, end=date(2019, 12, 31), look_period=10)
    # df = gs_ts_pro.cs_equity_block_trade(start=None, end=date(2019, 12, 31), look_period=10)
    # df = gs_ts_pro.cs_equity_top_inst(start=None, end=date(2019, 12, 31), look_period=10)
    # print(df_j1)
    # print(df_j2)
    dfI = dfI[(dfI["pe"] < 20.0) & (dfI["pe"] > 10.0)]
    print(dfI)
    df_j = pd.DataFrame({"adj_open": df_j1["open"] * df_j2["adj_factor"],
                         "adj_close": df_j1["close"] * df_j2["adj_factor"]
                         })
    # print(df_j)
    df_j_by_I = dfI.join(df_j)
    print(df_j_by_I)
    df_agg_mean = df_j_by_I.groupby(by="date", axis="index", level=0).mean()
    print(df_agg_mean)

    df_agg_std = df_j_by_I.groupby(by="date", axis="index", level=0).std()
    print(df_agg_std)

    df_600000 = gs_ts_pro.equity_backward_adjust_daily("600188.SH")
    df_600000 = df_600000[(df_600000.index >= df_agg_mean.index.min()) & (df_600000.index <= df_agg_mean.index.max())]
    print(df_600000)

    df_600000_z = pd.DataFrame({"close": (df_600000["close"] - df_agg_mean["adj_close"]) / df_agg_std["adj_close"]})

    print(df_600000_z)

    print("*" * 20)
    print(gs_ts_pro.cs_equity_backward_adjust_daily(start=None, end=date(2019, 12, 31), look_period=10))

    # print(dfI)
    # print(df.describe())
    # print(df.info())
    # df = ts_pro.concept_detail(ts_code="600050.SH",fields="id,concept_name,ts_code,name,in_date,out_date")
    # df = ts_pro.concept_detail(id="TS115",fields="concept_name,ts_code,name,in_date,out_date")
    # df = ts_pro.new_share()
    # df = ts_pro.forecast(ts_code="002626.SZ")
    # df = ts.pro_bar(ts_code="600000.SH", api=ts_pro, asset="E", adj="hfq", freq="D")
    # print(df.transpose())
    # for _ in range(10):
    #     df = gs_ts_pro.equity_backward_adjust_daily("600102.SH", cols=["close"])
    # print(df)
    # for _ in range(10):
    #     df = gs_ts_pro.stock_basic(exchange="SSE", cols=["market"])
    # df = gs_ts_pro.index_classify(level="L1")
    # print(df)
    # print(df["index_code"].tolist())
    # print(df["industry_name"].tolist())
    # df_in_range = gs_ts_pro.period_index_member(index_code="801021.SI", start=date(2011, 1, 1), end=date(2018, 12, 31))
    # print(df_in_range)

    # df_in_range_test = gs_ts_pro.
    # (index_code="801021.SI", start=date(2019, 1, 1), end=date(2020, 1, 1))
    # print(df_in_range_test)
    # print(df_in_range_test.describe())

    # df = gs_ts_pro.index_member(ts_code="600000.SH", is_new="N")
    # print(df)

    # df = gs_ts_pro.equity_quotation_daily("600058.SH")
    # df = gs_ts_pro.equity_basic_daily("600759.SH", cols=["total_mv"])
    # df = df[df["total_mv"] > 5.0e6]
    # df = df.sample(n=2)
    # print(df)
    # df = gs_ts_pro.equity_quotation_daily("600000.SH")
    # df = gs_ts_pro.index_weight("000043.SH")
    # df = gs_ts_pro.index_weight("000045.SH",cols=["con_code"])
    # df = gs_ts_pro.index_weight("998100.MI",reinit=True)
    # df = ts_pro.index_weight(index_code="998100.MI")
    # df = df[df.index == '2019-09-30']
    # df = gs_ts_pro.pro_api.index_basic(market="SSE")
    # df = df["name"].tolist()
    # df = df[df["name"]=="超大盘"]
    # df = get_month_periods(datetime(1990, 1, 1), 4)
    # df = df.sample(n=int(0.3*len(df)))
    # for t in df.index.unique():
    #     print(t)
    #     print(set(df[df.index == t]["con_code"].tolist()))
    # df = get_category_by_t_from_index_weight(gs_ts_pro,"000045.SH")

    # ---- 这部分是时间对齐到特定跨度的情况 ------
    # df = gs_ts_pro.index_quotation_daily("000001.SH", cols=["close"])
    # df = df[df.index <= datetime(2018, 12, 31)].iloc[-128:]
    #
    # df_stk = gs_ts_pro.equity_quotation_daily("600000.SH", cols=["open"])
    # df_stk = df.join(df_stk).fillna(method="ffill").fillna(0.).iloc[:,1:]
    # print(df_stk)
    # ----- 这部分代码用于 shuffle index weight 以后区分 train 和 valid
    # df = gs_ts_pro.index_weight("000045.SH", cols=["con_code"])
    # df = df.sample(frac=1)
    # split_pos = int(len(df) * 0.9)
    # df_train, df_val = df.iloc[:split_pos], df.iloc[split_pos:]
    #
    # print(df_train)
    # print(df_val)
    # print({t: set(df[df.index == t]["con_code"].tolist()) for t in df_val.index.unique()})
    # print(ls_dt)
    # print(len(ls_dt))

    # 000045.SH , 上证小盘
    # 000043.SH , 超大盘


def test_news_api():
    # 显示所有列
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)
    # 设置value的显示长度为100，默认为50
    pd.set_option('max_colwidth')
    # df = ts_pro.news(src="yuncaijing", start_date='2019-11-21 09:00:00', end_date='2019-12-22 10:10:00')
    # df = ts_pro.major_news(src='新浪财经', start_date='2018-11-21 00:00:00', end_date='2018-11-22 00:00:00',
    #                        fields='title,content,src,pub_time')
    df = ts_pro.cctv_news(date='20181211')
    print(df)


def is_semi_yearly_report_col(df: pd.DataFrame, col: str):
    df["non_val"] = df.apply(lambda row: 1 if pd.notna(row[col]) else 0, axis=1)
    rows_count = df.shape[0]
    ratio = df["non_val"].sum() / rows_count
    # print(f"{col}:{ratio}={df['non_val'].sum()}/{rows_count}")
    # print(f"{(rows_count/2-1)/rows_count} <= {ratio} <= {(rows_count/2+1)/rows_count}")
    # return (rows_count/2-1)/rows_count <= ratio <= (rows_count/2+1)/rows_count
    return 0.3 < ratio < 0.7


def test_corp_financial_statement():
    # df = equity_all_financial_statement("600000.SH")
    # print(df)
    # print(df.shape)
    # print(df.fillna(100))
    # print(df["net_profit"].tail(20))

    df_stks = gs_ts_pro.stock_basic(exchange="SSE", cols=["ts_code", "name"])

    df_stks = df_stks[df_stks["ts_code"] == "601628.SH"]

    for id_num, row in df_stks.iterrows():
        # print(f"\r{id_num} : {row['ts_code']} - {row['name']} ")
        df = gs_ts_pro.income(symbol=row["ts_code"])
        print(f"{id_num}-{row['ts_code']}-{row['name']}:{df['comp_type'][0]}")
        if id_num > 300:
            break

def test_adj_factor():
    print(gs_ts_pro.equity_adj_factor_daily("600030.SH"))
    pass


if __name__ == "__main__":
    import logging

    debug_level_modules = ["gs_research_workflow.time_series.data.arctic_and_local_cache", "__main__"]
    for n in debug_level_modules:
        logging.getLogger(n).setLevel(logging.DEBUG)

    # 显示所有列
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)
    # 设置value的显示长度为100，默认为50
    pd.set_option('max_colwidth', 80)

    # test_equity_concept()
    # test_news_api()
    # test_corp_financial_statement()
    # df = ts_pro.cashflow(ts_code="600000.SH")
    # print(df.columns.tolist())
    test_adj_factor()

