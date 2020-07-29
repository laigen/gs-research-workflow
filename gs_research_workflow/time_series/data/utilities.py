# -*- coding: utf-8 -*-
from datetime import date, datetime, timezone, timedelta
from typing import Optional, Union, List, Tuple

import pandas as pd
import numpy as np

# ----- pd.Dataframe 一些常用的数据处理函数  ------


def _filter_df_by_start_end(df: pd.DataFrame, start: Optional[Union[date, datetime]] = None,
                            end: Optional[Union[date, datetime]] = None) -> pd.DataFrame:
    if df is None:
        return None
    if start:
        if isinstance(start, date):
            start = datetime.combine(start, datetime.min.time())
        df = df[df.index >= start]
    if end:
        if isinstance(end, date):
            end = datetime.combine(end, datetime.max.time())
        df = df[df.index <= end]
    return df


def filter_df_by_t_and_cols(df: pd.DataFrame, start: Optional[Union[date, datetime]] = None,
                            end: Optional[Union[date, datetime]] = None,
                            cols: Optional[List[str]] = None) -> pd.DataFrame:
    if df is None:
        return df
    df = _filter_df_by_start_end(df, start, end)
    if cols:
        df = df[cols]
    return df


def val_convert_to_zscore(df: pd.DataFrame, mean_base_date: Optional[date],
                          calc_period: Tuple[Optional[date], Optional[date]],
                          output_std_and_mean: bool = False) -> pd.DataFrame:
    """计算 calc_period 时间跨度内，以 mean_base_date 数据为均值计算 zscore 的值
        这里假定 mean_base_date 一定在 calc_period 的时间区段内

        NOTE:mean_base_date 值为 None 的时候，计算 mean 值，而不是以某一期的数据作为 mean
    """
    start, end = calc_period
    df = _filter_df_by_start_end(df, start, end)
    # 减去某一期的固定值
    if mean_base_date is None:
        series_mean = df.agg("mean", axis=0)
    else:
        series_mean = df[df.index == datetime.combine(mean_base_date, datetime.min.time())].iloc[0]

    df_delta = df.sub(series_mean, axis=1)
    df_std = df.agg("std", axis=0)
    df_zscore = df_delta.div(df_std, axis=1)
    if output_std_and_mean:
        return df_zscore, series_mean, df_std
    else:
        return df_zscore


def de_zscore_to_val(df_zscore: pd.DataFrame, df_mean_base: pd.DataFrame, series_std: pd.Series) -> pd.DataFrame:
    df = df_zscore.mul(series_std, axis=1)
    df = df.add(df_mean_base.to_numpy()[0],axis=1)
    return df
# ----- 一些超时策略的计算函数 -----


def arctic_daily_data_expired_default_strategy(mtime, data_max_t) -> bool:
    is_over_4H = (datetime.now() - mtime).total_seconds() > 3600. * 4
    # NOTE : 如果是日频数据，data_max_t 填入的时间是 零点
    dt_now = datetime.now(timezone(timedelta(hours=8)))  # 假定先 hardcode 为东八区的时间
    is_next_trade_day_close = (dt_now - data_max_t.replace(tzinfo=timezone(timedelta(hours=8)))).total_seconds() > (
                3600 * (24 + 16))

    return is_over_4H and is_next_trade_day_close


def arctic_non_ts_data_expired_default_strategy(mtime, _) -> bool:
    is_over_24H = (datetime.now() - mtime).total_seconds() > 3600. * 24
    return is_over_24H


def arctic_non_ts_data_expired_month_end(mtime: datetime, _) -> bool:
    """有些数据，月底的时候才会进行更新，这时候的超时时间增加一些更新时间点的判断"""
    dt_now = datetime.now()
    # 月份换了
    if (mtime.year * 1000 + mtime.month) != (dt_now.year * 1000 + dt_now.month):
        return True
    if mtime.day <= 10:  # 上旬更新时间，则最长2天一次检查
        return (dt_now - mtime).total_seconds() > 3600. * 24 * 2
    else:  # 下旬，则两周一次检查
        return (dt_now - mtime).total_seconds() > 3600. * 24 * 14
