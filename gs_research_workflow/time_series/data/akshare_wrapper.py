# -*- coding: UTF-8 -*-

"""
see : https://github.com/jindaxiang/akshare
"""
import logging
from datetime import date, datetime, timedelta
from typing import Union, Optional, List

import pandas as pd
import akshare as ak


from gs_research_workflow.time_series.data.arctic_and_local_cache import ArcticAndLocalCacheBySymbol, \
    SymbolTSRemoteSyncToArcticInfo, convert_column_as_datetime
from gs_research_workflow.time_series.data.arctic_version_storage import ArcticVersionStorageMixin
from gs_research_workflow.time_series.data.utilities import filter_df_by_t_and_cols, \
    arctic_daily_data_expired_default_strategy, arctic_non_ts_data_expired_default_strategy

logger = logging.getLogger(__name__)


class akshareData(ArcticVersionStorageMixin, ArcticAndLocalCacheBySymbol):
    API_PROVIDER_NAME: str = "akshare"
    lib_prefix: str = "akshare_"
    NON_TS_LIBNAME = "non_ts_version"

    DAILY_ALL_HISTORY_QUERY_PERIOD = [(date(1980, 1, 1), date(1989, 12, 31)),
                                      (date(1990, 1, 1), date(2005, 12, 31)),
                                      (date(2006, 1, 1), date(2015, 12, 31)),
                                      (date(2016, 1, 1), datetime.today().date())]
    """历史数据不能一次性取出，所以这里对 tushare 的数据做分段情况"""

    def __init__(self, use_l3_cache: bool = True):
        super().__init__(use_l3_cache)

    def _run_non_ts_get_data_and_return(self, lib_name: str, symbol: str, sync_info: SymbolTSRemoteSyncToArcticInfo, cols,
                                        re_init: bool) -> pd.DataFrame:
        full_lib_name = self.lib_prefix + lib_name

        if re_init:
            self.clean_up_version_object_data(full_lib_name, symbol)

        df = self._maybe_read_version_object_from_local_cache(full_lib_name, symbol, sync_info)
        return filter_df_by_t_and_cols(df, None, None, cols)

    def get_non_ts_sync_info(self, f_query, **kwargs) -> SymbolTSRemoteSyncToArcticInfo:
        """获取非 ts 类数据的更新数据结构"""
        sync_info = SymbolTSRemoteSyncToArcticInfo()
        sync_info.f_init_query = lambda: f_query(**kwargs)

        sync_info.f_new_data_query = None
        sync_info.ls_init_query_paras = None
        sync_info.f_check_arctic_need_update = arctic_non_ts_data_expired_default_strategy
        sync_info.chunk_size = None
        return sync_info

    def get_us_stock_name(self, cols: Optional[List[str]] = None, re_init: bool = False) -> pd.DataFrame:
        """获取美股的名称代码表"""
        sync_info = self.get_non_ts_sync_info(ak.get_us_stock_name)
        obj_uuid = "get_us_stock_name"
        return self._run_non_ts_get_data_and_return(self.NON_TS_LIBNAME, obj_uuid, sync_info, cols, re_init)
