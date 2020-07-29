# -*- coding: UTF-8 -*-

"""
试着使用 arctic 的 version storage 来保存 google account 的 oauth 的内容
"""
import pickle

from arctic import Arctic, VERSION_STORE
from gs_framework.utilities import get_random_str, object_2_bytes, bytes_2_object

from gs_research_workflow.common.arctic_binary import ArcticBinary
from gs_research_workflow.external_data.db_server_resource.mongo import get_mongo_admin_conn_str

if __name__ == "__main__":
    arctic_bin = ArcticBinary()
    str_to_save = get_random_str(40, 50)
    bin = object_2_bytes(str_to_save)
    arctic_bin.write_bin_object(bin,"test_bin_obj")
    new_bin = arctic_bin.read_bin_object("test_bin_obj")
    assert bin == new_bin
