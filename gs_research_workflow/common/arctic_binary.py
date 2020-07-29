# -*- coding: UTF-8 -*-

"""
使用 arctic version storage 进行 binary object 的存储接口
"""
from arctic import Arctic, VERSION_STORE

from gs_research_workflow.external_data.db_server_resource.mongo import get_mongo_admin_conn_str, \
    get_google_mongo_conn_str, get_intranet_mongo_conn_str

GOOG_TOKEN_LIB: str = "google_token"

_ARCTIC_BINARY_LIBRARY: str = "binary_lib"


class ArcticBinary:
    def __init__(self, lib_name: str = _ARCTIC_BINARY_LIBRARY, mongo_db: str = "auto"):
        """假定一个 instance 只操作一个 library
            mongo_db :
                "auto" 根据环境是否为 colab 自动选择  google 还是 local
                "google" 选择 google 的 mongo
                "intranet" 选择机房中的Mongo
        """
        # 这里 暂时先 hardcode arctic 所使用的 mongo 地址
        mongo_db_conn_str = get_mongo_admin_conn_str()
        if mongo_db == "google":
            mongo_db_conn_str = get_google_mongo_conn_str()
        elif mongo_db == "intranet":
            mongo_db_conn_str = get_intranet_mongo_conn_str()
        self._store = Arctic(mongo_db_conn_str)
        if not self._store.library_exists(lib_name):
            self._store.initialize_library(lib_name, VERSION_STORE)
        self._lib = self._store[lib_name]

    def write_bin_object(self, bin_data: bytes, symbol: str):
        self._lib.write(symbol, bin_data)

    def read_bin_object(self, symbol: str) -> bytes:
        return self._lib.read(symbol).data

    def has_symbol(self, symbol: str) -> bytes:
        return self._lib.has_symbol(symbol)
