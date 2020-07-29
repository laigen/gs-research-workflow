# -*- coding: utf-8 -*-
# DEL BY laigen , 2020.04.25
# from random import choice, sample
# from typing import Dict
#
# import dataset
# from dataset import Table
# from gs_framework.common_prop_dtypes import DataType
# from gs_framework.utilities import md5_str
#
# from gs_research_workflow.browser_workflow_common.named_ranges_by_user import UrlGroupAndUserGroup, \
#     UIObjectDefBySelector
# from gs_research_workflow.browser_workflow_common.url_is_entity import RuleBasedUrlEntityClassifier
#
# from gs_research_workflow.common.mongo_func import MongoAPI
# from gs_framework.namedtuple_func import get_namedtuple_from_dict
# import pprint
#
# from gs_research_workflow.common.random_func import random_gauss
#
#
# def test_mongo_db():
#     mongo_db = MongoAPI.get_mongo_client("mlData")
#     mongo_url_group_clct = MongoAPI.get_collection_from_db(mongo_db, "mlData", "url_group")
#     pk = UrlGroupAndUserGroup("ml_tech_v2", "https://scholar.baidu.com/citations")
#     v = UIObjectDefBySelector(range_name="h-index-v1", query_selector="#yyy > ddd.yyy", dtype=DataType.int.value,
#                               expire_sec=36000.)
#     mongo_url_group_clct.delete_one({"_id":md5_str(f"{pk.user_group}:{pk.url_group}:{v.query_selector}")})
#
#     # dict_ui_object_def = pk._asdict()
#     # dict_ui_object_def.update(v._asdict())
#     # dict_ui_object_def["_id"] = md5_str(f"{pk.user_group}:{pk.url_group}:{v.query_selector}")
#     # MongoAPI.replace_one(mongo_url_group_clct, "_id", dict_ui_object_def["_id"], dict_ui_object_def)
#
#     for doc in mongo_url_group_clct.find({"user_group": "ml_tech"}):
#         v_pk = get_namedtuple_from_dict(doc, UrlGroupAndUserGroup)
#         v_ui_obj_def = get_namedtuple_from_dict(doc, UIObjectDefBySelector)
#         pprint.pprint(v_pk)
#         pprint.pprint(v_ui_obj_def)
#
#
# def test_named_tuple():
#     print(dir(UIObjectDefBySelector))
#
#
# def test_mongo_query():
#     db = MongoAPI.get_mongo_client("mlData")
#     clct = MongoAPI.get_collection_from_db(db, "mlData", "url_based_entity_props")
#
#     ls_url_entites = ["https://scholar.google.com/citations?user=O3FVg9AAAAAJ&hl=en&oi=sra",
#                       "https://scholar.google.com/citations?user=7HCKL10AAAAJ&hl=en&oi=sra"]
#
#     joined_group = {"ml_tech"}
#
#     dict_query = {
#         "entity_url": {"$in": ls_url_entites},
#         "def_from_usr_group": {"$elemMatch": {"$in": list(joined_group)}}
#     }
#     rlt = clct.find(dict_query)
#
#     dict_entity_val: Dict[str, Dict[str, object]] = {}
#     for item in rlt:
#         if item["entity_url"] in dict_entity_val:
#             dict_entity_val[item["entity_url"]][item["prop_name"]] = item["val"]
#         else:
#             dict_entity_val[item["entity_url"]] = {item["prop_name"]: item["val"]}
#     for doc in rlt:
#         print(doc)
#     print(dict_entity_val)
#
#
# def test_mongo_update():
#     db = MongoAPI.get_mongo_client("mlData")
#     clct = MongoAPI.get_collection_from_db(db, "mlData", "url_based_entity_props")
#     joined_group = {"ml_tech"}
#     clct.update_many({"url_group": "https://scholar.google.com/citations",
#                       "def_from_usr_group": {"$elemMatch": {"$in": list(joined_group)}}}, {"$set": {"status": 1}})
#
#
# if __name__ == "__main__":
#
#     pass
#     # for _ in range(500):
#     #     print(random_gauss(min_v=0.5, max_v=20., mu=6., sigma=1.5))
#
#     # test_mongo_db()
#     # test_named_tuple()
#     # test_mongo_query()
#     # test_mongo_update()
#     # a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     # true_a = [1, 3, 5]
#     # print(sample(a, min(33, len(a))))
#     # db = dataset.connect("sqlite:///:memory:", ensure_schema=False)
#     # tbl: Table = db.create_table("test_db", primary_id="id", primary_type=db.types.string)
#     # tbl.create_column("valid_flag", db.types.boolean)
#     # for i in a:
#     #     tbl.insert({"id": str(i), "valid_flag": False})
#     # sql = f"""UPDATE test_db set valid_flag=1 where id in ({','.join(["'"+str(s)+"'" for s in true_a])})"""
#     # print(sql)
#     # db.query(sql)
#     # print( tbl.count(valid_flag=True))
