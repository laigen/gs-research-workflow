# -*- coding: utf-8 -*-
"""
提供按照 Symbol 获取数据的两级 Cache 机制

核心的封装思路为：
    1) 所有从网络接口上来的数据，先保存到 arctic 上
        好处：
            a) 降低外部网络调用的压力
            b) 同一个网络接口账号，可以多人共享使用
            c) 账号到期后，数据服务没有中断，只是不更新
        arctic 存储方式：
            a) 每个接口提供的数据，是一个 chunkstore library
            b) chunk size 为相同频度的内容，symbol 填入具体的symbol 值
                一般接口都不提供 cross section 的数据，所以这部分数据需要自己按照 symbol 进行累积
    2) 数据读取到内存的访问顺序为：
        local pickle > arctic > original
    3) 暂时先用阻塞的方式进行缓存的维护，以后再考虑异步的方式，用另一个 service 进行数据维护

"""
import logging
import os
from datetime import date, datetime, timedelta
import time
from functools import reduce, lru_cache
from itertools import starmap
from typing import Union, List, Dict, Callable, Any, Tuple, Optional

import pandas as pd

from gs_research_workflow.common.path_utilities import get_training_data_file_path
from gs_research_workflow.time_series.data.arctic_chunk_storage import ArcticChunkStorage
from diskcache import Cache

logger = logging.getLogger(__name__)

OS_ENV_KEY_LOCAL_CACHE_EXPIRE_HOURS = "local_cache_expire_hours"


def _local_cache_expire_hours() -> int:
    return int(os.environ.get(OS_ENV_KEY_LOCAL_CACHE_EXPIRE_HOURS, 24*7))


class SymbolTSRemoteSyncToArcticInfo:
    """适用于按照 symbol 取数据类的接口"""
    f_init_query: Callable[..., pd.DataFrame]
    """初始获取数据的查询函数
        调用该函数，能够返回一个 ts 的 dataframe 对象，通常是提供商的取数据接口
    """

    ls_init_query_paras: List[Any]
    """ 传入 f_init_query 的 args ，一个 item 是一项数据内容
        Note : 因为有些数据不是一次调用能取到的，需要转换成多次调用才能获取到完整的数据内容
        Examples: 每次获取10年数据，才能把股票的历史收盘价数据获取完整
    """

    f_original_df_process: Callable[[pd.DataFrame], pd.DataFrame]
    """
        获取到的 dataframe 数据的处理函数，也需要返回 dataframe 对象
        Examples : tushare 返回的日期数据列是 YYYYMMDD 的 string 格式，需要转成 date 格式才能保存到 arctic 的 chunkstore 中
    """

    f_new_data_query: Callable[[Union[date, datetime]], pd.DataFrame]
    """从源头查询有没有新的数据内容，传入的参数为上一次的时间戳"""

    f_check_arctic_need_update: Callable[[datetime, Union[date, datetime]], bool]
    """arctic中的数据是否需要更新，第一个参数为 meta 中保存的 mtime , 第二个参数为 meta 中保存的最大数据时间"""

    chunk_size: str
    """数据存到 chunk store 用的 chunk_size"""


class CSApiRemoteSyncToArcticInfo:
    """适用于cs类的接口，同步到 arctic"""
    f_query_by_t: Callable[[Union[date, datetime]], pd.DataFrame]
    f_original_df_process: Callable[[pd.DataFrame], pd.DataFrame]
    """
        获取到的 dataframe 数据的处理函数，也需要返回 dataframe 对象
        Examples : tushare 返回的日期数据列是 YYYYMMDD 的 string 格式，需要转成 date 格式才能保存到 arctic 的 chunkstore 中
    """


class ArcticAndLocalCacheBySymbol(ArcticChunkStorage):
    """
    TS 类的数据，一个 symbol 一个 pkl 文件
    CS 类的数据，一个 t 一个 pkl 文件
    """

    API_PROVIDER_NAME: str = "unknown"
    """派生类必须重载该变量，用于区分保存local file path 的信息"""

    def __init__(self, use_l3_cache: bool):
        super().__init__()
        self._last_arctic_check_time: Dict[str, datetime] = dict()
        self._last_local_file_check_time: Dict[str, datetime] = dict()
        self.query_orig_source_count = 0
        # NOTE: use_l3_cache 在 colab 运行环境中可能会发生死锁，所以暂时先 HardCode 禁用该功能
        # self._use_l3_cache = use_l3_cache
        self._use_l3_cache = False
        self._l3_cache: Cache = None
        if self._use_l3_cache:
            self._l3_cache = Cache()

    # region symbol ts 类的接口
    def _maybe_init_arctic_storage(self, lib_name: str, symbol: str, sync_info: SymbolTSRemoteSyncToArcticInfo) -> Tuple[
        Optional[pd.DataFrame], bool]:
        """
        初始化某个 symbol 在 arctic 中的数据内容
            如果该 symbol 已经在 arctic 中，则返回 None
            如果该 Symbol 在 arctic 中不存在，则调用 f_init_query 函数获取全部数据后写入 arctic 中的内容，并返回

        Returns
        -------
        -
            如果已经存在，则返回 None , 否则返回初始化获取数据后写入 arctic 的数据内容

        """
        if self.is_symbol_exist(lib_name, symbol):
            return None, True

        # 这里按照 all_data_query 逆序请求，从有数据到无数据的第一项出现时，有一项没有数据时，即停止遍历
        all_df_data = list()
        first_df = None

        max_tried_latest_period = 3  # 为了避免空数据时的过多次数遍历，设定一个最多匹配多少项空置的止损
        source_req_count = 0  # 增加对于原始接口请求次数过多时候的等待保护

        run_start = time.time()
        for i, args in enumerate(reversed(sync_info.ls_init_query_paras)):
            df = sync_info.f_init_query(*args)
            self.query_orig_source_count += 1
            source_req_count += 1
            if source_req_count % 5 == 0:  # 避免单次请求过快（http socket来不及释放，触发 timeout），每10次 sleep 1 秒
                time.sleep(0.7)
            if first_df is None:
                first_df = df
            if df is not None and len(df) > 0:
                all_df_data.append(sync_info.f_original_df_process(df))
            else:
                if i >= max_tried_latest_period:
                    break

        if source_req_count >= 10:
            sleep_time = source_req_count / 10.
            logger.debug(f"{lib_name}:'{symbol}' has queried {source_req_count} times,now sleep {sleep_time} secs")
            time.sleep(sleep_time)

        if len(all_df_data) > 0:
            # 将多个 df 数据拼接起来
            df = reduce(lambda x, y: x.append(y), all_df_data)
            df.sort_index(axis=0, ascending=True, inplace=True)

            logger.debug(f"Init write {lib_name}:'{symbol}' [{len(df)}] rows to arctic, used {time.time() - run_start} secs")
            self.init_write_chunk_lib(lib_name, sync_info.chunk_size, symbol, df)
            return df, True
        else:
            logger.debug(f"{lib_name}:'{symbol}' has no data .")
            return first_df, False

    def _maybe_update_arctic_storage(self, lib_name: str, symbol: str, sync_info: SymbolTSRemoteSyncToArcticInfo):
        check_time_key = f"{lib_name}:{symbol}"
        last_check_time = self._last_arctic_check_time.get(check_time_key, datetime.now() - timedelta(days=1))

        # 先做一个简单的控制，同一个 symbol 最多 8H 进行一次 arctic 检查有无最新数据
        if (datetime.now() - last_check_time).total_seconds() < 3600. * 16:
            return None
        self._last_arctic_check_time[check_time_key] = datetime.now()

        meta = self._read_meta(lib_name, symbol)

        if meta is None:
            logger.error(f"{lib_name}:'{symbol}' meta data is None.")
            # delete symbol in lib , and reinit
            self._remove_symbol(lib_name, symbol)
            self._maybe_init_arctic_storage(lib_name, symbol, sync_info)
            return None
        mtime = meta.get(self.META_KEY_MTIME)
        data_max_t = meta.get(self.META_KEY_MAX_T_INSTORE)

        if sync_info.f_check_arctic_need_update(mtime, data_max_t):
            run_start = time.time()
            df = sync_info.f_new_data_query(data_max_t)
            self.query_orig_source_count += 1
            if df is not None and len(df) > 0:
                df = sync_info.f_original_df_process(df)
                self._append_write_chunk_lib(lib_name, symbol, df)
                logger.debug(
                    f"Insert {lib_name}-'{symbol} into arctic [{len(df)}] rows, used {time.time() - run_start} secs")
            else:  # 检查过源头数据未发生更新，修改 meta 中的 mtime 值
                meta[self.META_KEY_MTIME] = datetime.now()
                self._write_meta(lib_name, symbol, meta)
        return data_max_t

    def is_local_cache_expired(self, file_path: str, lib_name: str, symbol: str):
        check_time_key = f"{lib_name}:{symbol}"
        # 重新增加的 18H 内本地文件发生了更新，不做超时判断
        last_local_cache_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
        if (datetime.now() - last_local_cache_mtime).total_seconds() < (3600. * _local_cache_expire_hours()):
            return False

        last_check_time = self._last_local_file_check_time.get(check_time_key, datetime.now() - timedelta(days=1))
        if (datetime.now() - last_check_time).total_seconds() < (3600. * _local_cache_expire_hours()):
            return False
        self._last_local_file_check_time[check_time_key] = datetime.now()
        return True

    def compare_max_t_changed(self, lib_name: str, symbol: str, local_data: pd.DataFrame):
        t1 = datetime.now()
        meta = self._read_meta(lib_name, symbol)
        logger.debug(f"read {lib_name} - {symbol} arctic meta, used {(datetime.now()-t1).total_seconds()} secs")
        if meta is None:
            logger.error(f"{lib_name}-'{symbol}' meta data is None.")
            # delete symbol in lib , and reinit
            self._remove_symbol(lib_name, symbol)
            return True
        arctic_data_max_t = meta.get(self.META_KEY_MAX_T_INSTORE)
        if arctic_data_max_t > local_data.index.max():
            return True
        return False

    def update_local_cache_mtime(self, file_path: str):
        """更新本地的缓存文件时间，以避免发生频繁的read meta"""
        import os
        t = (datetime.now() - timedelta(hours=_local_cache_expire_hours() / 2)).timestamp()
        os.utime(file_path, (t, t))

    def _init_arctic_and_save(self, file_path: str, lib_name: str, symbol: str,
                              sync_info: SymbolTSRemoteSyncToArcticInfo) -> pd.DataFrame:
        df, b_in_arctic = self._maybe_init_arctic_storage(lib_name, symbol, sync_info)
        if df is None and b_in_arctic:  # 已经初始化过了，读取全部的数据内容
            # 读取之前，先做一次 arctic 的数据更新操作
            self._maybe_update_arctic_storage(lib_name, symbol, sync_info)
            df = self._read_all(lib_name, symbol)
        if df is not None and not df.empty:
            df.to_pickle(file_path, compression="gzip", protocol=4)
        return df

    def _get_local_path_file(self, lib_name: str, symbol: str):
        path = get_training_data_file_path(self.API_PROVIDER_NAME, lib_name)
        file_path = os.path.join(path, symbol + ".pkl")
        return path, file_path

    def clean_up_symbol_data(self, lib_name: str, symbol: str):
        path, file_path = self._get_local_path_file(lib_name, symbol)
        if os.path.isfile(file_path):
            os.remove(file_path)
        self._remove_symbol(lib_name, symbol)

    @staticmethod
    def _l3_cache_key(lib_name: str, symbol: str) -> str:
        return f"{lib_name}-{symbol}"

    def _is_in_l3_cache(self, lib_name: str, symbol: str) -> bool:
        if self._l3_cache is None:
            return False
        return ArcticAndLocalCacheBySymbol._l3_cache_key(lib_name, symbol) in self._l3_cache

    def _get_from_l3_cache(self, lib_name: str, symbol: str) -> pd.DataFrame:
        if self._l3_cache is None:
            return None
        return self._l3_cache.get(ArcticAndLocalCacheBySymbol._l3_cache_key(lib_name, symbol))

    def _set_into_l3_cache(self, lib_name: str, symbol: str, df: pd.DataFrame) -> bool:
        if self._l3_cache is None:
            return False
        return self._l3_cache.set(ArcticAndLocalCacheBySymbol._l3_cache_key(lib_name, symbol), df)

    def _clean_l3_cache(self, lib_name: str, symbol: str):
        if self._l3_cache is None:
            return
        if self._is_in_l3_cache(lib_name, symbol):
            del self._l3_cache[ArcticAndLocalCacheBySymbol._l3_cache_key(lib_name, symbol)]

    def _maybe_read_from_local_cache(self, lib_name: str, symbol: str,
                                     sync_info: SymbolTSRemoteSyncToArcticInfo) -> pd.DataFrame:
        if self._is_in_l3_cache(lib_name, symbol):
            return self._get_from_l3_cache(lib_name, symbol)

        path, file_path = self._get_local_path_file(lib_name, symbol)

        if os.path.isfile(file_path):
            try:
                if self.is_local_cache_expired(file_path, lib_name, symbol):
                    # 只有在本地文件已经过期后，才检查远程的数据是否有更新，可能会有些滞后，但性能会提升
                    self.check_library(lib_name)
                    self._maybe_update_arctic_storage(lib_name, symbol, sync_info)
                    df = pd.read_pickle(file_path, compression="gzip")
                    if self.compare_max_t_changed(lib_name, symbol, df):
                        data_max_t = df.index.max()
                        df_new = self._read_period(lib_name, symbol, data_max_t + timedelta(days=1), datetime.today())
                        if df_new is not None and not df_new.empty:
                            # 增量部分补充进数据，并保存
                            df = df.append(df_new)
                            df.sort_index(axis=0, ascending=True, inplace=True)
                            df.to_pickle(file_path, compression="gzip", protocol=4)
                            logger.debug(
                                f" Append write {lib_name}-{symbol} pkl file, last end_t '{data_max_t}' , append write '{df_new.index.min()}' - '{df_new.index.max()}' ")
                    else:
                        self.update_local_cache_mtime(file_path)
                else:
                    try:
                        df = pd.read_pickle(file_path, compression="gzip")
                    except Exception as ex:
                        logger.error(f"Read pickle '{file_path}' error, re-init '{symbol}' , {ex} ")
                        os.remove(file_path)
                        df = self._init_arctic_and_save(file_path, lib_name, symbol, sync_info)

                self._set_into_l3_cache(lib_name, symbol, df)
                return df
            except EOFError:
                logger.error(f"Read '{file_path}' error, re-init '{symbol}'")
                os.remove(file_path)
                df = self._init_arctic_and_save(file_path, lib_name, symbol, sync_info)
                self._set_into_l3_cache(lib_name, symbol, df)
                return df

        else:
            df = self._init_arctic_and_save(file_path, lib_name, symbol, sync_info)
            self._set_into_l3_cache(lib_name, symbol, df)
            return df

    # endregion

    # region cs 类的接口

    @staticmethod
    def _cs_l3_cache_key(lib_name: str, api_name: str, t: date) -> str:
        return f"{lib_name}-{api_name}-{t}"

    def _cs_is_in_l3_cache(self, lib_name: str, api_name: str, t: date) -> bool:
        if self._l3_cache is None:
            return False
        return ArcticAndLocalCacheBySymbol._cs_l3_cache_key(lib_name, api_name, t) in self._l3_cache

    def _cs_get_from_l3_cache(self, lib_name: str, api_name: str, t: date) -> pd.DataFrame:
        if self._l3_cache is None:
            return None
        return self._l3_cache.get(ArcticAndLocalCacheBySymbol._cs_l3_cache_key(lib_name, api_name, t))

    def _cs_set_into_l3_cache(self, lib_name: str, api_name: str, t: date, df: pd.DataFrame) -> bool:
        if self._l3_cache is None:
            return False
        return self._l3_cache.set(ArcticAndLocalCacheBySymbol._cs_l3_cache_key(lib_name, api_name, t), df)

    def _cs_clean_l3_cache(self, lib_name: str, api_name: str, t: date):
        if self._l3_cache is None:
            return
        if self._cs_is_in_l3_cache(lib_name, api_name, t):
            del self._l3_cache[ArcticAndLocalCacheBySymbol._cs_l3_cache_key(lib_name, api_name, t)]

    def _cs_get_local_path_file(self, lib_name: str, api_name: str, t: date):
        path = get_training_data_file_path(self.API_PROVIDER_NAME, lib_name)
        path = os.path.join(path, api_name)
        if not os.path.exists(path):
            os.makedirs(path)
        file_path = os.path.join(path, t.strftime("%Y%m%d") + ".pkl")
        return path, file_path

    def cs_clean_up_data(self, lib_name: str, api_name: str):
        path, file_path = self._cs_get_local_path_file(lib_name, api_name, date(2000, 1, 1))  # 这里date不会使用，所以随便取一个
        if os.path.exists(path):
            import shutil
            shutil.rmtree(path, True)
        self._remove_symbol(lib_name, api_name)

    def _cs_maybe_read_from_arctic(self, file_path: str, lib_name: str, api_name: str, t: date,
                                   query_info: CSApiRemoteSyncToArcticInfo) -> pd.DataFrame:
        df = self._read_cs(lib_name, api_name, t)
        if df is None or df.empty:
            # query data from original source
            self.query_orig_source_count += 1
            df = query_info.f_query_by_t(t)
            df = query_info.f_original_df_process(df)
            if df is not None and not df.empty:
                self._write_cs_chunk_lib(lib_name, api_name, df)

        if df is not None and not df.empty:
            df.to_pickle(file_path, compression="gzip", protocol=4)
        return df

    @lru_cache(maxsize=1024, typed=False)
    def _cs_maybe_read_from_local_cache(self, lib_name: str, api_name: str, t: date,
                                        query_info: CSApiRemoteSyncToArcticInfo) -> pd.DataFrame:
        if self._cs_is_in_l3_cache(lib_name, api_name, t):
            return self._cs_get_from_l3_cache(lib_name, api_name, t)

        path, file_path = self._cs_get_local_path_file(lib_name, api_name, t)

        if os.path.isfile(file_path):
            # CS 类与TS不同点在于，只要T时刻取得过数据，就不需要再更新，直接使用缓存数据即可
            try:
                df = pd.read_pickle(file_path, compression="gzip")
                self._cs_set_into_l3_cache(lib_name, api_name, df, t)
                return df
            except EOFError:
                logger.error(f"Read '{file_path}' error, re-init '{api_name}'")
                os.remove(file_path)
                df = self._cs_maybe_read_from_arctic(file_path, lib_name, api_name, t, query_info)
                self._cs_set_into_l3_cache(lib_name, api_name, t, df)
                return df
        else:
            df = self._cs_maybe_read_from_arctic(file_path, lib_name, api_name, t, query_info)
            self._set_into_l3_cache(lib_name, api_name, df)
            return df
    # endregion

    # region derived TS write and read
    def _read_arctic_and_save(self, file_path: str, lib_name: str, symbol: str) -> pd.DataFrame:
        df = self._read_all(lib_name, symbol)
        if df is not None and not df.empty:
            df.to_pickle(file_path, compression="gzip", protocol=4)
        return df

    def _read_ts_without_vendor_source(self, lib_name: str, symbol: str) -> pd.DataFrame:
        """仅从本地等没有 vendor源头 更新信息的环节读取 ts 数据 """
        if self._is_in_l3_cache(lib_name, symbol):
            return self._get_from_l3_cache(lib_name, symbol)

        path, file_path = self._get_local_path_file(lib_name, symbol)

        if os.path.isfile(file_path):
            try:
                if self.is_local_cache_expired(file_path, lib_name, symbol):
                    # 只有在本地文件已经过期后，才检查远程的数据是否有更新，可能会有些滞后，但性能会提升
                    self.check_library(lib_name)
                    df = pd.read_pickle(file_path, compression="gzip")
                    if self.compare_max_t_changed(lib_name, symbol, df):
                        data_max_t = df.index.max()
                        df_new = self._read_period(lib_name, symbol, data_max_t + timedelta(days=1), datetime.today())
                        if df_new is not None and not df_new.empty:
                            # 增量部分补充进数据，并保存
                            df = df.append(df_new)
                            df.sort_index(axis=0, ascending=True, inplace=True)
                            df.to_pickle(file_path, compression="gzip", protocol=4)
                            logger.debug(
                                f" Append write {lib_name}-{symbol} pkl file, last end_t '{data_max_t}' , append write '{df_new.index.min()}' - '{df_new.index.max()}' ")
                    else:
                        self.update_local_cache_mtime(file_path)
                else:
                    try:
                        df = pd.read_pickle(file_path, compression="gzip")
                    except Exception as ex:
                        logger.error(f"Read pickle '{file_path}' error, re-init '{symbol}' , {ex} ")
                        os.remove(file_path)

                self._set_into_l3_cache(lib_name, symbol, df)
                return df
            except EOFError:
                logger.error(f"Read '{file_path}' error, re-init '{symbol}'")
                os.remove(file_path)
                df = self._read_arctic_and_save(file_path, lib_name, symbol)
                self._set_into_l3_cache(lib_name, symbol, df)
                return df
        else:
            df = self._read_arctic_and_save(file_path, lib_name, symbol)
            if df is not None:
                self._set_into_l3_cache(lib_name, symbol, df)
            return df
    # endregion

def convert_column_as_datetime(df: pd.DataFrame, old_t_column: str, new_t_column: str,
                               t_format: str = "%Y%m%d") -> pd.DataFrame:
    df.loc[:, new_t_column] = df[old_t_column].apply(lambda x: datetime.strptime(x, t_format))
    return df


def convert_columns_as_datetime(df: pd.DataFrame, columns: List[str], t_format: str = "%Y%m%d") -> pd.DataFrame:
    for col in columns:
        df.loc[:, "_" + col] = df[col].apply(lambda x: datetime.strptime(x, t_format))
    df.drop(columns=columns, inplace=True)
    df.rename(columns={"_" + col: col for col in columns}, inplace=True)
    return df


def convert_column_as_datetime_minus_one_day(df: pd.DataFrame, old_t_column: str, new_t_column: str,
                                             t_format: str = "%Y%m%d") -> pd.DataFrame:
    """处理 tushare 的fx数据，用的格林威治时间（比北京时间晚一天），用这个函数将其转换成北京时间"""
    df.loc[:, new_t_column] = df[old_t_column].apply(lambda x: datetime.strptime(x, t_format) - timedelta(days=1))
    return df
