# -*- coding: UTF-8 -*-
"""
RDBS 资源
"""
from enum import Enum

import mysql.connector
from mysql.connector import MySQLConnection


class RDBSDataSetByGS(Enum):
    JY = 1
    """聚源数据"""


def get_db_conn(dataset: RDBSDataSetByGS) -> MySQLConnection:
    if dataset == RDBSDataSetByGS.JY:
        return mysql.connector.connect(user="datatec", database="jydb", host="192.168.1.101", port=3306,
                                       password="0.618")
