# -*- coding: utf-8 -*-

"""
提供 arctic chunkstore 的一些功能
"""
import logging
import time
from datetime import datetime, date
from typing import Dict, Any

from arctic import Arctic, CHUNK_STORE
from arctic.exceptions import NoDataFoundException

from gs_research_workflow.external_data.db_server_resource.mongo import get_mongo_admin_conn_str
import pandas as pd

logger = logging.getLogger(__name__)


def _get_df_rows_count(df) -> int:
    if df is not None and not df.empty:
        return len(df)
    else:
        return 0


class ArcticChunkStorage:
    """
    有关 Arctic 的存储方式：
        TS 方式 存储的数据：
            - lib_name 对应于一个数据的调用接口
            - symbol 对应于一个股票
            - chunk_size 一般取 M（对于 daily 的数据）
        CS 方式 存储的数据：
            - lib_name 考虑 Per Data Vendor一个，或者几个接口合用同一个 lib_name
            - symbol 数据接口的名称
            - chunk_size 取 D，一个 chunk 一期数据（这里一般不会一次取出多期数据，本地磁盘也会有pkl的缓存）

    """
    META_KEY_MTIME = "mtime"
    META_KEY_MAX_T_INSTORE = "max_t"

    def __init__(self):
        self.arctic_store = Arctic(get_mongo_admin_conn_str(), connectTimeoutMS=600 * 1000,
                                   serverSelectionTimeoutMS=600 * 1000)
        # NOTE: arctic_store 已经有 library 的 cache 机制

    def check_library(self, lib_name: str):
        if not self.arctic_store.library_exists(lib_name):
            self.arctic_store.initialize_library(lib_name, lib_type=CHUNK_STORE)

    def is_symbol_exist(self, lib_name: str, symbol: str) -> bool:
        if not self.arctic_store.library_exists(lib_name):
            return False
        lib_chunk_store = self.arctic_store[lib_name]
        return lib_chunk_store.has_symbol(symbol)

    def is_cs_date_exist(self, lib_name: str, api_name: str, date_v: date) -> bool:
        if not self.is_symbol_exist(lib_name, api_name):
            return False
        df = self.arctic_store[lib_name].read(api_name, chunk_range=pd.date_range(date_v, date_v))
        return _get_df_rows_count(df) > 0

    def init_write_chunk_lib(self, lib_name: str, chunk_size: str, symbol: str, df: pd.DataFrame):
        if not self.arctic_store.library_exists(lib_name):
            self.arctic_store.initialize_library(lib_name, lib_type=CHUNK_STORE)
        lib_chunk_store = self.arctic_store[lib_name]
        if lib_chunk_store.has_symbol(symbol):
            lib_chunk_store.delete(symbol)

        run_start = time.time()
        # 仅写入有数据的dataframe，如果 dataframe没有一行数据，则只写入 meta 的内容
        lib_chunk_store.write(symbol, df, chunk_size=chunk_size, upsert=True)

        logger.debug(
            f"Init write {lib_name}-{symbol} arctic , used {time.time() - run_start} secs, {_get_df_rows_count(df)} rows ")
        max_date_in_db = df.index.max()

        lib_chunk_store.write_metadata(symbol, {self.META_KEY_MTIME: datetime.now(),
                                                self.META_KEY_MAX_T_INSTORE: max_date_in_db})

    def _write_cs_chunk_lib(self, lib_name: str, api_name: str, df: pd.DataFrame):
        if not self.arctic_store.library_exists(lib_name):
            self.arctic_store.initialize_library(lib_name, lib_type=CHUNK_STORE)
        lib_chunk_store = self.arctic_store[lib_name]

        run_start = time.time()
        if not lib_chunk_store.has_symbol(api_name):
            lib_chunk_store.write(api_name, df, chunk_size="D", upsert=True)
        else:
            lib_chunk_store.update(api_name, df, upsert=True)
        logger.debug(
            f"Init write {lib_name}-{api_name} arctic , used {time.time() - run_start} secs, {_get_df_rows_count(df)} rows ")

        lib_chunk_store.write_metadata(api_name, {self.META_KEY_MTIME: datetime.now()})

    def _append_write_chunk_lib(self, lib_name: str, symbol: str, df: pd.DataFrame):
        lib_chunk_store = self.arctic_store[lib_name]
        min_date = df.index.min()

        df_last_chunk = next(lib_chunk_store.reverse_iterator(symbol))  # 读取出最后一个 chunk 的数据，需要一同进行更新
        max_date_in_db = df_last_chunk.index.max()
        if max_date_in_db >= min_date:
            err_msg = f"Can't append data {lib_name}-{symbol} already existed in db. max_db_t:{max_date_in_db} , min_data_t:{min_date}." \
                      f"Maybe another one has updated ts data!"
            logger.error(err_msg)
            # NOTE : 这里不再抛出异常，有可能同时会有多个进程同时在更新arctic 上的同一个数据，会引起数据已经进行过了更新
            # raise RuntimeError(err_msg)
            # meta 还是更新，避免下次还会被 update
            lib_chunk_store.write_metadata(symbol, {self.META_KEY_MTIME: datetime.now(),
                                                    self.META_KEY_MAX_T_INSTORE: max_date_in_db})
            return

        # 叠加最后一个 chunk 的数据
        df = df.append(df_last_chunk)
        df.sort_index(axis=0, ascending=True, inplace=True)
        run_start = time.time()
        lib_chunk_store.update(symbol, df, upsert=True)
        logger.debug(
            f"Upsert {lib_name}-{symbol} , used {time.time() - run_start} secs, {_get_df_rows_count(df)} rows ")

        max_date_in_db = df.index.max()
        lib_chunk_store.write_metadata(symbol, {self.META_KEY_MTIME: datetime.now(),
                                                self.META_KEY_MAX_T_INSTORE: max_date_in_db})

    def _read_all(self, lib_name: str, symbol: str) -> pd.DataFrame:
        lib_chunk_store = self.arctic_store[lib_name]
        if not lib_chunk_store.has_symbol(symbol):
            return None
        run_start = time.time()
        df = lib_chunk_store.read(symbol)
        logger.debug(
            f"Read {lib_name}-{symbol} arctic , used {time.time() - run_start} secs, {_get_df_rows_count(df)} rows ")
        return df

    def _read_period(self, lib_name: str, symbol: str, start_t: date = date(1990, 1, 1),
                     end_t: date = date(2050, 12, 31)) -> pd.DataFrame:
        lib_chunk_store = self.arctic_store[lib_name]
        run_start = time.time()
        df = lib_chunk_store.read(symbol, chunk_range=pd.date_range(start_t, end_t), filter_data=True)
        logger.debug(
            f"Read {lib_name}-{symbol} period [{start_t}-{end_t}] , used {time.time() - run_start} secs , {_get_df_rows_count(df)} rows ")
        return df

    def _read_cs(self, lib_name: str, api_name: str, t: date) -> pd.DataFrame:
        if not self.is_symbol_exist(lib_name, api_name):
            return None
        lib_chunk_store = self.arctic_store[lib_name]
        run_start = time.time()
        df = lib_chunk_store.read(api_name, chunk_range=pd.date_range(t, t), filter_data=True)
        logger.debug(
            f"Read {lib_name}-{api_name} date {t} , used {time.time() - run_start} secs , {_get_df_rows_count(df)} rows ")
        return df

    def _read_meta(self, lib_name: str, symbol: str) -> Dict[str, Any]:
        lib_chunk_store = self.arctic_store[lib_name]
        try:
            meta_data = lib_chunk_store.read_metadata(symbol)
            return meta_data
        except NoDataFoundException:
            return None

    def _write_meta(self, lib_name: str, symbol: str, meta: Dict[str, Any]):
        lib_chunk_store = self.arctic_store[lib_name]
        lib_chunk_store.write_metadata(symbol, meta)

    def _remove_symbol(self, lib_name: str, symbol: str):
        if not self.arctic_store.library_exists(lib_name):
            return
        lib_chunk_store = self.arctic_store[lib_name]
        lib_chunk_store.delete(symbol)

    def ts_upsert_arctic_storage(self, lib_name: str, symbol: str, df: pd.DataFrame, chunk_size: str = "M",
                                 force_reinit: bool = False):
        """一些 derived ts 数据， arctic 只负责存储这些衍生的数据内容"""
        assert df is not None and df.shape[0] > 0  # 不允许写入一个空的 df 对象
        if force_reinit:
            self._remove_symbol(lib_name, symbol)

        if not self.arctic_store.library_exists(lib_name):
            self.arctic_store.initialize_library(lib_name, lib_type=CHUNK_STORE)
        lib_chunk_store = self.arctic_store[lib_name]
        run_start = time.time()
        if not lib_chunk_store.has_symbol(symbol):  # 第一次写入
            lib_chunk_store.write(symbol, df, chunk_size=chunk_size, upsert=True)
            logger.debug(
                f"Init write {lib_name}-{symbol} arctic , used {time.time() - run_start} secs, {_get_df_rows_count(df)} rows ")
        else:  # upsert
            min_date = df.index.min()
            df_last_chunk = next(lib_chunk_store.reverse_iterator(symbol))  # 读取出最后一个 chunk 的数据，需要一同进行更新
            max_date_in_db = df_last_chunk.index.max()
            if max_date_in_db >= min_date:
                err_msg = f"Can't append data {lib_name}-{symbol} already existed in db. max_db_t:{max_date_in_db} , min_data_t:{min_date}." \
                          f"Maybe another one has updated ts data!"
                logger.error(err_msg)
                return

            # 叠加最后一个 chunk 的数据
            df = df.append(df_last_chunk)
            df.sort_index(axis=0, ascending=True, inplace=True)
            run_start = time.time()
            lib_chunk_store.update(symbol, df, upsert=True)
            logger.debug(
                f"Upsert {lib_name}-{symbol} , used {time.time() - run_start} secs, {_get_df_rows_count(df)} rows ")

        max_date_in_db = df.index.max()
        lib_chunk_store.write_metadata(symbol, {self.META_KEY_MTIME: datetime.now(),
                                                self.META_KEY_MAX_T_INSTORE: max_date_in_db})
