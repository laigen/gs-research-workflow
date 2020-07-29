# -*- coding: utf-8 -*-
"""
一些预定义，方便获取数据的多个 api 的组合接口
"""
from datetime import date, datetime
from typing import Optional, Tuple, Union

import pandas as pd
import numpy as np
from gs_research_workflow.time_series.data.tushare_wrapper import TuShareProData

from gs_research_workflow.time_series.data.utilities import val_convert_to_zscore, _filter_df_by_start_end


def equity_all_financial_statement_by_enddate(tushare_sdk: TuShareProData, symbol: str,
                                              start_end_period: Tuple[Optional[date], Optional[date]] = (
                                                      date(2008, 1, 1), date(2019, 12, 31)),
                                              to_single_period: bool = True) -> pd.DataFrame:
    df_income = tushare_sdk.income_by_enddate(symbol=symbol, to_single_period_val=to_single_period)
    df_balance_sheet = tushare_sdk.balancesheet_by_enddate(symbol=symbol)
    df_cashflow = tushare_sdk.cashflow_by_enddate(symbol=symbol, to_single_period_val=to_single_period)
    df_all = df_income.join(df_balance_sheet, how="left", lsuffix="_inc", rsuffix="_bs").join(df_cashflow, how="left",
                                                                                              rsuffix="_cf")
    start, end = start_end_period
    df_all = _filter_df_by_start_end(df_all, start, end)
    return df_all


def equity_all_financial_statement_zscore(tushare_sdk: TuShareProData, symbol: str,
                                          mean_base_t: date = None,
                                          start_end_period: Tuple[Optional[date], Optional[date]] = (
                                                  date(2008, 1, 1), date(2019, 12, 31)),
                                          ret_mean_and_std: bool = False) -> Union[
    pd.DataFrame, Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]]:
    """三大表数据的 zscore"""
    df_all_orig = equity_all_financial_statement_by_enddate(tushare_sdk, symbol, start_end_period, True)
    df_all_zscore, series_mean, series_std = val_convert_to_zscore(df_all_orig, mean_base_t, start_end_period,
                                                                   output_std_and_mean=True)
    if not ret_mean_and_std:
        return df_all_zscore
    else:
        return df_all_zscore, series_mean, series_std


def equity_all_financial_statement_mean_and_std(tushare_sdk: TuShareProData, symbol: str,
                                                mean_base_t: date = date(2018, 12, 31),
                                                start_end_period: Tuple[Optional[date], Optional[date]] = (
                                                        date(2008, 1, 1), date(2019, 12, 31))) -> Tuple[
    pd.DataFrame, pd.DataFrame]:
    df_all = equity_all_financial_statement_by_enddate(tushare_sdk, symbol, start_end_period, True)

    df_mean_base = df_all[df_all.index == datetime.combine(mean_base_t, datetime.min.time())]

    df_delta = df_all.sub(df_all[df_all.index == datetime.combine(mean_base_t, datetime.min.time())].to_numpy()[0],
                          axis=1)
    df_std = (df_delta ** 2).agg("sum", axis=0).apply(np.sqrt)
    return df_mean_base, df_std


def equity_comp_type(tushare_sdk: TuShareProData, symbol: str) -> int:
    """获取公司的类型，  1一般工商业 2银行 3保险 4证券 """
    df_income = tushare_sdk.income(symbol=symbol, report_type=1)
    comp_type = df_income["comp_type"].unique()
    rlt = 1
    try:
        rlt = int(comp_type[0])
    except:
        pass
    return rlt
