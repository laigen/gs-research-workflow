# -*- coding: UTF-8 -*-
from enum import Enum

from gs_research_workflow.common.path_utilities import _is_colab_env
from pymongo import MongoClient


class MongoDataSetByGS(Enum):
    JY = 1
    """聚源的数据资源"""

    UGC_DATA = 2

    PLATFORM_DATA = 3


def get_mongo_client(dataset: MongoDataSetByGS) -> MongoClient:
    # !!! 暂时先把 用户名和密码 Hardcode 在这里，以后再考虑通过 os.env 的方式读取
    if dataset == MongoDataSetByGS.JY:
        return MongoClient(f"mongodb://gftQuant:gs2018@mongo.graphstrategist.com:27017/jy_arctic")
    elif dataset == MongoDataSetByGS.UGC_DATA:
        return MongoClient(f"mongodb://gftQuant:gs2018@mongo.graphstrategist.com:27017/mlData")
    elif dataset == MongoDataSetByGS.PLATFORM_DATA:
        return MongoClient(f"mongodb://admin:gft#test#2018@mongo.graphstrategist.com:27017/admin")
    else:
        raise RuntimeError(f"unknown dataset {dataset}")


def get_mongo_admin_conn_str() -> str:
    # return "mongodb://admin:gft#test#2018@gftoffice.sedns.cn:27017"
    # 暂定先只使用云上的 Mongo
    return "mongodb://root:hjDIbSKTN8@mongo.graphstrategist.com:32001"
    # if _is_colab_env():
    #     return "mongodb://root:Qo5X5Q2L5F2r@35.193.3.162:27017"
    # else:
    #     # connect(db_name, host="mongo.graphstrategist.com", port=32001, username="root", password="",
    #     #         authentication_source="admin")
    #     return "mongodb://root:hjDIbSKTN8@mongo.graphstrategist.com:32001"


def get_intranet_mongo_conn_str() -> str:
    return "mongodb://root:hjDIbSKTN8@mongo.graphstrategist.com:32001"


def get_google_mongo_conn_str() -> str:
    return "mongodb://root:Qo5X5Q2L5F2r@35.193.3.162:27017"
