# -*- coding: utf-8 -*-

import logging
from datetime import date, datetime, timedelta
import yfinance as yf
from typing import Union, Optional, List

import pandas as pd


from gs_research_workflow.time_series.data.arctic_and_local_cache import ArcticAndLocalCacheBySymbol, \
    SymbolTSRemoteSyncToArcticInfo, convert_column_as_datetime
from gs_research_workflow.time_series.data.utilities import filter_df_by_t_and_cols, arctic_daily_data_expired_default_strategy

logger = logging.getLogger(__name__)


class yFinanceData(ArcticAndLocalCacheBySymbol):
    API_PROVIDER_NAME: str = "yFinance"
    lib_prefix: str = "yfinance_"

    DAILY_ALL_HISTORY_QUERY_PERIOD = [(date(1980, 1, 1), date(1989, 12, 31)),
                                      (date(1990, 1, 1), date(2005, 12, 31)),
                                      (date(2006, 1, 1), date(2015, 12, 31)),
                                      (date(2016, 1, 1), datetime.today().date())]
    """历史数据不能一次性取出，所以这里对 tushare 的数据做分段情况"""

    def __init__(self, use_l3_cache: bool = True):
        super().__init__(use_l3_cache)

    def get_recommend_sync_info(self, yahoo_ticker_caller,
                                init_query_paras=DAILY_ALL_HISTORY_QUERY_PERIOD) -> SymbolTSRemoteSyncToArcticInfo:
        """提供一个适合于大多数情况的 sync_info 的数据内容，各接口可根据具体情况，进行细项目的调整
        NOTE: 这里假定 init_query_paras 是升序排列的，逆序调用接口时，只要找到第一条不符合内容的信息，则不再向前追溯
        """
        sync_info = SymbolTSRemoteSyncToArcticInfo()
        sync_info.f_init_query = lambda start, end: yahoo_ticker_caller(
            start=start.strftime("%Y-%m-%d"),
            end=end.strftime("%Y-%m-%d"))
        sync_info.f_new_data_query = lambda last_t: yahoo_ticker_caller(
            start_date=(last_t + timedelta(days=1)).strftime(
                "%Y-%m-%d"))
        sync_info.ls_init_query_paras = init_query_paras
        sync_info.f_check_arctic_need_update = arctic_daily_data_expired_default_strategy
        sync_info.chunk_size = "M"

        return sync_info

    def get_recommend_series_prop_info(self, ticker, attr_name: str,
                                       init_query_paras=DAILY_ALL_HISTORY_QUERY_PERIOD,
                                       series_attr: bool = True) -> SymbolTSRemoteSyncToArcticInfo:
        """提供一个适合于大多数情况的 sync_info 的数据内容，各接口可根据具体情况，进行细项目的调整
        NOTE: 这里假定 init_query_paras 是升序排列的，逆序调用接口时，只要找到第一条不符合内容的信息，则不再向前追溯
        """
        sync_info = SymbolTSRemoteSyncToArcticInfo()
        if series_attr:
            sync_info.f_init_query = lambda start, end: getattr(ticker, attr_name).to_frame().loc[start.strftime("%Y-%m-%d"):end.strftime("%Y-%m-%d")]
            sync_info.f_new_data_query = lambda last_t: getattr(ticker, attr_name).to_frame().loc[last_t.strftime("%Y-%m-%d")]
        else:
            sync_info.f_init_query = lambda start, end: getattr(ticker, attr_name).loc[start.strftime("%Y-%m-%d"):end.strftime("%Y-%m-%d")]
            sync_info.f_new_data_query = lambda last_t: getattr(ticker, attr_name).loc[last_t.strftime("%Y-%m-%d")]

        sync_info.ls_init_query_paras = init_query_paras
        sync_info.f_check_arctic_need_update = arctic_daily_data_expired_default_strategy
        sync_info.chunk_size = "M"

        return sync_info

    def _run_get_data_and_return(self, lib_name: str, symbol: str, start, end,
                                 sync_info: SymbolTSRemoteSyncToArcticInfo, cols,
                                 re_init: bool) -> pd.DataFrame:
        full_lib_name = self.lib_prefix + lib_name

        if re_init:
            self.clean_up_symbol_data(full_lib_name, symbol)

        df = self._maybe_read_from_local_cache(full_lib_name, symbol, sync_info)
        return filter_df_by_t_and_cols(df, start, end, cols)

    def history(self, symbol: str, start: Optional[Union[date, datetime]] = None,
                end: Optional[Union[date, datetime]] = None,
                cols: Optional[List[str]] = None,
                re_init: bool = False) -> pd.DataFrame:
        symbol_ticker = yf.Ticker(symbol)
        sync_info = self.get_recommend_sync_info(symbol_ticker.history)

        sync_info.f_original_df_process = lambda x: x.rename_axis("date")
        # 指数的symbol形如 "^NYA",
        return self._run_get_data_and_return("daily_per_symbol", symbol.replace("^", "_"), start, end, sync_info, cols,
                                             re_init)

    def dividends(self, symbol: str, start: Optional[Union[date, datetime]] = None,
                  end: Optional[Union[date, datetime]] = None,
                  cols: Optional[List[str]] = None,
                  re_init: bool = False) -> pd.DataFrame:
        symbol_ticker = yf.Ticker(symbol)
        sync_info = self.get_recommend_series_prop_info(symbol_ticker, "dividends", series_attr=True)
        sync_info.f_original_df_process = lambda x: x.rename_axis("date")
        # 指数的symbol形如 "^NYA",
        return self._run_get_data_and_return("dividends_per_symbol", symbol.replace("^", "_"), start, end, sync_info, cols,
                                             re_init)

    def splits(self, symbol: str, start: Optional[Union[date, datetime]] = None,
                  end: Optional[Union[date, datetime]] = None,
                  cols: Optional[List[str]] = None,
                  re_init: bool = False) -> pd.DataFrame:
        symbol_ticker = yf.Ticker(symbol)
        sync_info = self.get_recommend_series_prop_info(symbol_ticker, "splits", series_attr=True)
        sync_info.f_original_df_process = lambda x: x.rename_axis("date")
        # 指数的symbol形如 "^NYA",
        return self._run_get_data_and_return("splits_per_symbol", symbol.replace("^", "_"), start, end, sync_info, cols,
                                             re_init)

    def recommendations(self, symbol: str, start: Optional[Union[date, datetime]] = None,
                        end: Optional[Union[date, datetime]] = None,
                        cols: Optional[List[str]] = None,
                        re_init: bool = False) -> pd.DataFrame:
        symbol_ticker = yf.Ticker(symbol)
        sync_info = self.get_recommend_series_prop_info(symbol_ticker, "recommendations", series_attr=False)
        sync_info.f_original_df_process = lambda x: x.rename_axis("date")
        # 指数的symbol形如 "^NYA",
        return self._run_get_data_and_return("recommendation_per_symbol", symbol.replace("^", "_"), start, end,
                                             sync_info, cols, re_init)
