# -*- coding: UTF-8 -*-
__author__ = "laigen"

# 本module主要提供了与 Mongo 有关的 资源内容
from gs_framework.gs_resource import set_http_proxy

db_nlp = "nlp"
# used_db_position = "google"  # for "intranet" or "google"
used_db_position = "intranet"


def mongo_db_conn(db_position: str, db_name: str):
    from mongoengine import connect
	return connect(db_name, host="your mongo account", port=27017, username="mongo user name", password="mongo password",
                authentication_source="admin")