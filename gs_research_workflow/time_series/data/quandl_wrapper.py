# -*- coding: utf-8 -*-

import logging
from datetime import date, datetime, timedelta
import quandl
from typing import Union, Optional, List

import pandas as pd
from gs_research_workflow.time_series.data.arctic_and_local_cache import ArcticAndLocalCacheBySymbol, \
    SymbolTSRemoteSyncToArcticInfo, convert_column_as_datetime
from gs_research_workflow.time_series.data.utilities import filter_df_by_t_and_cols, arctic_daily_data_expired_default_strategy

logger = logging.getLogger(__name__)

_API_KEY_LAIGEN: str = "" # your quandl api key


class QuandlData(ArcticAndLocalCacheBySymbol):
    API_PROVIDER_NAME: str = "quandl"
    lib_prefix: str = "quandl_"

    DAILY_ALL_HISTORY_QUERY_PERIOD = [(date(1980, 1, 1), date(1989, 12, 31)), (date(1990, 1, 1), date(2005, 12, 31)),
                                      (date(2006, 1, 1), date(2015, 12, 31)),
                                      (date(2016, 1, 1), datetime.today().date())]
    """历史数据不能一次性取出，所以这里对 tushare 的数据做分段情况"""

    def __init__(self, api_key: str = _API_KEY_LAIGEN):
        super().__init__()
        self._api_key = api_key

    def get_daily_data(self, data_name: str, symbol: str, start: Optional[Union[date, datetime]] = None,
                       end: Optional[Union[date, datetime]] = None,
                       cols: Optional[List[str]] = None) -> pd.DataFrame:

        sync_info = SymbolTSRemoteSyncToArcticInfo()

        sync_info.f_init_query = lambda start, end: quandl.get(f"{data_name}/{symbol}",
                                                               start=start.strftime("%Y-%m-%d"),
                                                               end=end.strftime("%Y-%m-%d"),
                                                               api_key=self._api_key)
        sync_info.f_new_data_query = lambda last_t: quandl.get(f"{data_name}/{symbol}",
                                                               start_date=(last_t + timedelta(days=1)).strftime(
                                                                   "%Y-%m-%d"),
                                                               api_key=self._api_key)
        sync_info.ls_init_query_paras = self.DAILY_ALL_HISTORY_QUERY_PERIOD
        sync_info.f_check_arctic_need_update = arctic_daily_data_expired_default_strategy
        sync_info.chunk_size = "M"

        sync_info.f_original_df_process = lambda x: x.rename_axis("date")

        df = self._maybe_read_from_local_cache(self.lib_prefix + "_" + data_name + "daily_per_symbol", symbol,
                                               sync_info)
        return filter_df_by_t_and_cols(df, start, end, cols)
