# -*- coding: utf-8 -*-

"""
提供 arctic version storage 的一些功能
适用于 整块数据的全部更新
"""
import logging
import time
from datetime import datetime, timedelta
from typing import Dict, Any, Tuple, Optional, Union

import os
import pandas as pd
from arctic import VERSION_STORE

from gs_research_workflow.time_series.data.arctic_and_local_cache import SymbolTSRemoteSyncToArcticInfo, \
    _local_cache_expire_hours

logger = logging.getLogger(__name__)


class ArcticVersionStorageMixin:

    def check_version_library(self, lib_name: str):
        if not self.arctic_store.library_exists(lib_name):
            self.arctic_store.initialize_library(lib_name, lib_type=VERSION_STORE)

    def is_versioned_object_exist(self, lib_name: str, obj_uuid: str) -> bool:
        if not self.arctic_store.library_exists(lib_name):
            return False
        lib_chunk_store = self.arctic_store[lib_name]
        return lib_chunk_store.has_symbol(obj_uuid)

    def init_write_version_lib(self, lib_name: str, obj_uuid: str, data: Union[bytes, pd.DataFrame]):
        if not self.arctic_store.library_exists(lib_name):
            self.arctic_store.initialize_library(lib_name, lib_type=VERSION_STORE)
        lib_version_store = self.arctic_store[lib_name]
        if lib_version_store.has_symbol(obj_uuid):
            lib_version_store.delete(obj_uuid)

        run_start = time.time()
        lib_version_store.write(obj_uuid, data)
        logger.debug(f"Init write {lib_name}-{obj_uuid}, used {time.time() - run_start} secs, {len(data)} bytes ")

        lib_version_store.write_metadata(obj_uuid, {self.META_KEY_MTIME: datetime.now()})

    def _read_version_storage(self, lib_name: str, obj_uuid: str) -> Union[bytes, pd.DataFrame]:
        lib_version_store = self.arctic_store[lib_name]
        run_start = time.time()
        bin_data = lib_version_store.read(obj_uuid)
        logger.debug(
            f"Read {lib_name}-{obj_uuid} arctic , used {time.time() - run_start} secs, {len(bin_data)} bytes ")
        return bin_data

    def _write_version_meta(self, lib_name: str, obj_uuid: str, meta: Dict[str, Any]):
        lib_version_store = self.arctic_store[lib_name]
        lib_version_store.write_metadata(obj_uuid, meta)

    def _remove_object_uuid(self, lib_name: str, obj_uuid: str):
        lib_bin_store = self.arctic_store[lib_name]
        lib_bin_store.delete(obj_uuid)

    def clean_up_version_object_data(self, lib_name: str, obj_uuid: str):
        path, file_path = self._get_local_path_file(lib_name, obj_uuid)
        if os.path.isfile(file_path):
            os.remove(file_path)
        self._remove_object_uuid(lib_name, obj_uuid)

    def _maybe_init_arctic_version_storage(self, lib_name: str, obj_uuid: str,
                                           sync_info: SymbolTSRemoteSyncToArcticInfo, force_update: bool = False) -> Tuple[
        Optional[pd.DataFrame], bool]:
        if not force_update and self.is_versioned_object_exist(lib_name, obj_uuid):
            return None, True

        # 这里按照 all_data_query 逆序请求，从有数据到无数据的第一项出现时，有一项没有数据时，即停止遍历
        i_valid_rows = 0
        run_start = time.time()
        # version store 假定数据是一次性取出的，无法做成分批次的调用接口
        if hasattr(self, "query_orig_source_count"):
            self.query_orig_source_count += 1
        df = sync_info.f_init_query()
        i_valid_rows += len(df)

        if len(df) > 0:
            logger.debug(f"Init write {lib_name}:'{obj_uuid}' [{len(df)}] rows to arctic, used {time.time() - run_start} secs")
            self.init_write_version_lib(lib_name, obj_uuid, df)
            return df, True
        else:
            logger.info(f"{lib_name}:'{obj_uuid}' has no data.")
            return df, False

    def _maybe_update_arctic_version_storage(self, lib_name: str, obj_uuid: str, sync_info: SymbolTSRemoteSyncToArcticInfo):
        check_time_key = f"{lib_name}:{obj_uuid}"
        last_check_time = self._last_arctic_check_time.get(check_time_key, datetime.now() - timedelta(days=1))

        # 先做一个简单的控制，同一个 symbol 最多 8H 进行一次 arctic 检查有无最新数据
        if (datetime.now() - last_check_time).total_seconds() < 3600. * 8:
            return None
        self._last_arctic_check_time[check_time_key] = datetime.now()

        meta = self._read_meta(lib_name, obj_uuid)

        if meta is None:
            logger.error(f"{lib_name}:'{obj_uuid}' meta data is None.")
            # delete symbol in lib , and reinit
            self._remove_object_uuid(lib_name, obj_uuid)
            self._maybe_init_arctic_version_storage(lib_name, obj_uuid, sync_info, force_update=True)
            return None
        meta = meta.metadata

        mtime = meta.get(self.META_KEY_MTIME)

        if sync_info.f_check_arctic_need_update(mtime, None):
            self._maybe_init_arctic_version_storage(lib_name, obj_uuid, sync_info, True)
            mtime = datetime.now()
        return mtime

    def _init_version_arctic_and_save(self, file_path: str, lib_name: str, obj_uuid: str,
                                      sync_info: SymbolTSRemoteSyncToArcticInfo) -> pd.DataFrame:
        df, b_in_arctic = self._maybe_init_arctic_version_storage(lib_name, obj_uuid, sync_info)
        if df is None and b_in_arctic:  # 已经初始化过了，读取全部的数据内容
            # 读取之前，先做一次 arctic 的数据更新操作
            self._maybe_update_arctic_version_storage(lib_name, obj_uuid, sync_info)
            df = self._read_version_storage(lib_name, obj_uuid).data
        if df is not None and not df.empty:
            df.to_pickle(file_path, compression="gzip", protocol=4)
        return df

    def _maybe_read_version_object_from_local_cache(self, lib_name: str, obj_uuid: str,
                                                    sync_info: SymbolTSRemoteSyncToArcticInfo) -> pd.DataFrame:

        path, file_path = self._get_local_path_file(lib_name, obj_uuid)

        if os.path.isfile(file_path):
            try:
                if self.is_local_cache_expired(file_path, lib_name, obj_uuid):
                    # 只有在本地文件已经过期后，才检查远程的数据是否有更新，可能会有些滞后，但性能会提升
                    self.check_version_library(lib_name)
                    self._maybe_update_arctic_version_storage(lib_name, obj_uuid, sync_info)
                    df = pd.read_pickle(file_path, compression="gzip")
                else:
                    df = pd.read_pickle(file_path, compression="gzip")
                return df
            except EOFError:
                logger.error(f"Read '{file_path}' error, re-init '{obj_uuid}'")
                os.remove(file_path)
                df = self._init_version_arctic_and_save(file_path, lib_name, obj_uuid, sync_info)
                return df
        else:
            df = self._init_version_arctic_and_save(file_path, lib_name, obj_uuid, sync_info)
            return df
