# -*- coding: utf-8 -*-

"""一些 arctic 数据同步与维护的函数，在 run train 之前，建议先把相应的数据同步好。 包括 debug 环境和 colab 环境分别维护"""
import functools
import os
import time
from datetime import datetime, date

from gs_research_workflow.time_series.data.tushare_wrapper import TuShareProData
from gs_research_workflow.time_series.gs_steps.predefined_step_fields import TSPortfolioWeightInputStep
from gs_research_workflow.time_series.gs_steps.ts_data_steps import SymbolMultipleTSStep
from gs_research_workflow.time_series.partial_workflow.ts_portfolio_weight_steps import EQUITY_TS_FEATURES_CONTEXT
import pandas as pd


class TushareReqSleepController:
    def __init__(self, tushare: TuShareProData):
        self._tushare = tushare
        self.i_query_from_tushare_block: int = 0
        self.time_cost_in_this_block: float = 0.
        self._internal_t = None
        self._internal_prev_req_count: int = None

    # tushare 的规则是 1min请求数不能超过 100 次，这里增加一些数量应该不会触发边界
    MAX_REQ_PER_MINUTES: int = 110

    def begin_internal_check(self):
        self._internal_t = datetime.now()
        self._internal_prev_req_count = self._tushare.query_orig_source_count

    def end_internal_check(self):
        t2 = datetime.now()

        if self._tushare.query_orig_source_count > self._internal_prev_req_count:
            self.time_cost_in_this_block += (t2 - self._internal_t).total_seconds()

        # 请求超过了 100 次， sleep 一段时间，以保证 tushare 不会阻止后续的请求
        # tushare 的规则是 1min请求数不能超过 100 次
        if (self._tushare.query_orig_source_count // TushareReqSleepController.MAX_REQ_PER_MINUTES) > \
                self.i_query_from_tushare_block:
            self.i_query_from_tushare_block = self._tushare.query_orig_source_count // TushareReqSleepController.MAX_REQ_PER_MINUTES
            time_to_sleep = max((60.0 - self.time_cost_in_this_block) * 1.2, 5.)
            print(f"\r\n total reqs {self._tushare.query_orig_source_count} . Another {TushareReqSleepController.MAX_REQ_PER_MINUTES} reqs in {self.time_cost_in_this_block} secs , now sleep {time_to_sleep} to avoid block")
            self.time_cost_in_this_block = 0.
            time.sleep(time_to_sleep)


def sync_equity_data(mkt_code: str = "SSE"):
    os.environ["local_cache_expire_hours"] = "12"
    query_step = SymbolMultipleTSStep(data_query_class=EQUITY_TS_FEATURES_CONTEXT["LOCAL"]["x_feature_query_class"],
                                      apis_and_columns=EQUITY_TS_FEATURES_CONTEXT["LOCAL"][
                                          "x_features_per_symbol"])

    f = query_step.symbol_ts_callable
    ts_wrapper = query_step.query_sdk
    req_freq_controller = TushareReqSleepController(ts_wrapper)

    df_stks = ts_wrapper.stock_basic(exchange=mkt_code, cols=["ts_code", "name"])

    for id_num, row in df_stks.iterrows():
        print(f"\rsync_equity_data {id_num} : {row['ts_code']} - {row['name']}  , total reqs {ts_wrapper.query_orig_source_count} ", end="")
        req_freq_controller.begin_internal_check()
        f(row['ts_code'])
        req_freq_controller.end_internal_check()


def sync_index_and_fund_nav():
    """指数和基金 portfolio 和 NAV 等"""
    # TODO: 找到 tushare 接口对象，用统一的类控制访问频度
    step = TSPortfolioWeightInputStep(use_ssh_index=True, use_szse_index=True, use_csi_index=True, use_fund_in_otc=True,
                                      use_fund_in_exchange=True)
    ls_symbol_to_ignore = []
    print(f"TOTAL ITEMS: {len(step.all_portfolio_callable)}")
    for i, (symbol, (f_weight_ts, f_cs, f_symbol_ts)) in enumerate(step.all_portfolio_callable.items()):
        print("+" * 20 + f"  {i} - {symbol} " + "+" * 20)
        t = datetime.now()
        df = f_weight_ts(symbol)
        if df is not None:
            print(f"\t [{symbol} weight data] : {df.shape}")
        t2 = datetime.now()
        if (t2-t).total_seconds() > 0.1:
            time.sleep((t2-t).total_seconds()/1.5)

        t2 = datetime.now()
        df = f_symbol_ts(symbol)
        if df is not None:
            print(f"\t [{symbol} ts data] : {df.shape}")
        t3 = datetime.now()
        if (t3-t2).total_seconds() > 0.1:
            time.sleep((t3-t2).total_seconds()/1.5)
        if df.shape[0] < 100:
            ls_symbol_to_ignore.append(symbol)
    print(f"symbols_to_ignore:{ls_symbol_to_ignore}")


def sync_equity_financial_statement(mkt_code: str = "SSE"):
    """上市公司的财务数据等"""
    os.environ["local_cache_expire_hours"] = "24"

    ts_wrapper = TuShareProData(use_l3_cache=False)
    df_stks = ts_wrapper.stock_basic(exchange=mkt_code, cols=["ts_code", "name"])
    req_freq_controller = TushareReqSleepController(ts_wrapper)

    for id_num, row in df_stks.iterrows():
        print(f"\rsync_equity_financial_statement {id_num} : {row['ts_code']} - {row['name']} , total reqs {ts_wrapper.query_orig_source_count} ", end="")
        symbol = row["ts_code"]
        req_freq_controller.begin_internal_check()
        ts_wrapper.income_by_enddate(symbol=symbol, to_single_period_val=True)
        ts_wrapper.balancesheet_by_enddate(symbol=symbol)
        ts_wrapper.cashflow_by_enddate(symbol=symbol, to_single_period_val=True)
        req_freq_controller.end_internal_check()


def sync_equity_to_sw_industry(sw_industry_lv: str, start_t: date, end_t: date, force_reinit: bool = False):
    lv_to_lib_name = {"L1": TuShareProData.DERIVED_TS_EQUITY_SW_INDUSTRY_L1,
                      "L2": TuShareProData.DERIVED_TS_EQUITY_SW_INDUSTRY_L2,
                      "L3": TuShareProData.DERIVED_TS_EQUITY_SW_INDUSTRY_L3}
    assert sw_industry_lv in lv_to_lib_name.keys()

    tushare = TuShareProData(use_l3_cache=False)
    req_freq_controller = TushareReqSleepController(tushare)

    df_sw_index = tushare.index_classify(level=sw_industry_lv, src="SW")
    df_sw_index = df_sw_index.reset_index(drop=True)
    ls_df_index_equities = []
    i_num = 0
    for idx_num, row in df_sw_index.iterrows():
        i_num += 1
        lv = row["level"]
        ind_name = row["industry_name"]
        ind_code = row["index_code"]

        req_freq_controller.begin_internal_check()
        df_index_equities = tushare.period_index_member(index_code=ind_code, resample_freq="B", start=start_t,
                                                        end=end_t)
        req_freq_controller.end_internal_check()

        df_index_equities["index_code"] = ind_code
        ls_df_index_equities.append(df_index_equities)

    df_all_index_equities = pd.concat(ls_df_index_equities)
    for i, symbol in enumerate(df_all_index_equities["symbol"].unique()):
        df_symbol_in_industry = df_all_index_equities[df_all_index_equities["symbol"] == symbol]
        df_symbol_in_industry.drop(columns=["symbol"], inplace=True)
        print(f"\rsync_equity_to_sw_industry {i}:{symbol}-{df_symbol_in_industry.index.min()}-{df_symbol_in_industry.index.max()} ", end="")
        tushare.ts_upsert_arctic_storage(lv_to_lib_name[sw_industry_lv], symbol, df_symbol_in_industry,
                                         force_reinit=force_reinit)


def _calc_sw_industry_data(tushare: TuShareProData, sw_industry_code: str, start_t: date, end_t: date,
                           f_equity_quotation_daily=None, f_equity_basic_daily=None) -> pd.DataFrame:
    # 行业指数在 date 的持仓
    df_stocks_in_industry = tushare.period_index_member(sw_industry_code, start=start_t, end=end_t,
                                                        resample_freq="B")
    if df_stocks_in_industry is None:  # 区间内没有股票，直接返回
        return
    df_stocks_in_industry = df_stocks_in_industry.reset_index().set_index(keys=["date", "symbol"])

    if f_equity_quotation_daily is None:
        f_equity_quotation_daily = tushare.cs_equity_quotation_daily
    if f_equity_basic_daily is None:
        f_equity_basic_daily = functools.partial(tushare.cs_equity_basic_daily,
                                                 cols=["turnover_rate", "turnover_rate_f",
                                                       "volume_ratio", "pe", "pe_ttm", "pb",
                                                       "ps", "ps_ttm", "dv_ratio", "dv_ttm",
                                                       "total_share", "float_share",
                                                       "free_share", "total_mv", "circ_mv"])
    # 每日指标
    mv_weighted_cols = ["open", "high", "low", "close", "pre_close", "change", "pct_chg", "turnover_rate",
                        "turnover_rate_f", "volume_ratio", "pe", "pe_ttm", "pb", "ps", "ps_ttm", "dv_ratio",
                        "dv_ttm"]  # 总市值加权的列
    # sum_cols = ["vol", "amount", "total_share", "float_share", "free_share", "total_mv", "circ_mv"]
    # 得到个股的区间数据
    df_cs_daily_industry_membership = df_stocks_in_industry.join(
        f_equity_quotation_daily(start=start_t, end=end_t), how="left").join(
        f_equity_basic_daily(start=start_t, end=end_t), how="left")
    # 市值加权列的加总计算
    for col in mv_weighted_cols:
        df_cs_daily_industry_membership[f"_{col}"] = df_cs_daily_industry_membership[col] * \
                                                     df_cs_daily_industry_membership["total_mv"]
    df_cs_daily_industry_membership.drop(columns=mv_weighted_cols, inplace=True)
    df_cs_daily_industry_membership.rename(columns={f"_{col}": col for col in mv_weighted_cols}, inplace=True)

    df_cs_daily_industry_membership = df_cs_daily_industry_membership.reset_index().groupby("date").sum()
    for col in mv_weighted_cols:
        df_cs_daily_industry_membership[f"_{col}"] = df_cs_daily_industry_membership[col] / \
                                                     df_cs_daily_industry_membership["total_mv"]
    df_cs_daily_industry_membership.drop(columns=mv_weighted_cols, inplace=True)
    df_cs_daily_industry_membership.rename(columns={f"_{col}": col for col in mv_weighted_cols}, inplace=True)
    return df_cs_daily_industry_membership


def sync_equity_cs_daily(start_t: date):
    os.environ["local_cache_expire_hours"] = "12"
    tushare = TuShareProData(use_l3_cache=False)
    df_index = tushare.index_quotation_daily("000001.SH", start=start_t, cols=["close"])
    req_freq_controller = TushareReqSleepController(tushare)

    for idx_date, row in df_index.iterrows():
        cs_t = date(idx_date.year, idx_date.month, idx_date.day)
        # 先只获取两个日期的数据
        print(f"\rEquity CS data @{cs_t} , total reqs {tushare.query_orig_source_count} ", end="")

        req_freq_controller.begin_internal_check()
        tushare.cs_equity_quotation_daily(start=cs_t, end=cs_t)
        tushare.cs_equity_basic_daily(start=cs_t, end=cs_t)
        req_freq_controller.end_internal_check()


def sync_sw_industry_index(start_t: date, end_t: date, force_reinit: bool = False):
    tushare = TuShareProData(use_l3_cache=False)
    req_freq_controller = TushareReqSleepController(tushare)
    f_equity_quotation_daily = functools.lru_cache(maxsize=2)(tushare.cs_equity_quotation_daily)
    f_equity_basic_daily = functools.lru_cache(maxsize=2)(functools.partial(tushare.cs_equity_basic_daily,
                                                                            cols=["turnover_rate", "turnover_rate_f",
                                                                                  "volume_ratio", "pe", "pe_ttm", "pb",
                                                                                  "ps", "ps_ttm", "dv_ratio", "dv_ttm",
                                                                                  "total_share", "float_share",
                                                                                  "free_share", "total_mv", "circ_mv"]))

    df_sw_index = tushare.index_classify(src="SW")
    df_sw_index = df_sw_index.reset_index(drop=True)
    ls_df_index_equities = []
    for idx_num, row in df_sw_index.iterrows():
        lv = row["level"]
        ind_name = row["industry_name"]
        ind_code = row["index_code"]
        print(
            f"\r[sync_sw_industry_index {idx_num}] Calc {lv} industry '{ind_code}'({ind_name}) index data, reqs {tushare.query_orig_source_count}",
            end="")

        req_freq_controller.begin_internal_check()
        df_ind_index = _calc_sw_industry_data(tushare, ind_code, start_t, end_t, f_equity_quotation_daily,
                                              f_equity_basic_daily)
        req_freq_controller.end_internal_check()
        if df_ind_index is not None:
            tushare.ts_upsert_arctic_storage(TuShareProData.DERIVED_TS_INDUSTRY_INDEX, ind_code, df_ind_index,
                                             force_reinit=force_reinit)


