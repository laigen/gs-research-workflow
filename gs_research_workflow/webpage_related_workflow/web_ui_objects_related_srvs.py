# -*- coding: utf-8 -*-

"""
适用于网页中提取 ui_objects 的流程

[N]  ChromeDesktopEnv(acct_id , pc_name)   :  [1]  WebUIObjectsManageEnv(acct_id)
                                                   + var(UserJoinedGroups) ， 用户加入过哪些 Group 的状态

    + var(url + dom)                    ===>    根据 User 加入的 Group 信息，预测 UI Object 和 Entity Linking
                                                （这类 rule base 的 object detection 逻辑，直接在 env 中实现）

     render ui objects                 <===    var(ui_objects_in_page)

     open url ，get dom , close        <===    var(url based entity to sync)
"""
# DEL by laigen , 2020.04.25 等重新启动后再开放
# import copy
# from datetime import datetime
# from random import choice
# from typing import Dict, Tuple, List, Set
# import logging
#
# import dataset
# from dataset import Table
# from gs_framework.common_prop_dtypes import UrlUniqueEntity, OneDimUIObject, DataType
# from gs_framework.decorators import init_actions, actionable, timer
# from gs_framework.instance_reference import DCERef
# from gs_framework.namedtuple_func import get_namedtuple_from_dict
# from gs_framework.state_variable import StateVariable
# from gs_framework.stateful_srv_base_classes import Env
# from gs_framework.stateless_srv_base_classes import _StatelessBasicSrv
# from gs_framework.utilities import md5_str, bytes_2_object, get_random_uuid
# from pymongo import ReplaceOne, UpdateOne
# from pyquery import PyQuery
#
# from gs_research_workflow.browser_workflow_common.browser_job import BrowserVisitUrlsJob, JobStatus, JobHeartBeats, \
#     BrowserJobStatus
# from gs_research_workflow.browser_workflow_common.common_variable_dtype import PageWithDOM, \
#     UIObjectsAndEntityLinkingInOnePage, UIObjectsInOnePage
# from gs_research_workflow.browser_workflow_common.named_ranges_by_user import UrlGroupDataByUserGroup, \
#     UrlGroupAndUserGroup, UIObjectDefBySelector, UIObjectDefsInUrlGroup, UIObjectDefCollection, UIObjectInPage
# from gs_research_workflow.browser_workflow_common.url_is_entity import RuleBasedUrlEntityClassifier
# from gs_research_workflow.common.mongo_func import MongoAPI
# from gs_research_workflow.common.web_utilities import get_url_group_str, batch_get_dom_node_start_pos, \
#     get_pq_object_inner_text, element_to_xpath, get_doc_hyperlinking, get_url_without_fragment
#
# logger = logging.getLogger(__name__)
#
#
# class UrlGroupDCESrv(_StatelessBasicSrv):
#     """用于维护 UrlGroupDataByUserGroup dce 中的数据内容。
#         包含的功能：
#             1) 根据 newly_add , newly_del 维护 mongo 中的 snapshot 数据，并将 snapshot 数据写回 UrlGroupDataByUserGroup 中
#     """
#
#     _subscribed_dce = UrlGroupDataByUserGroup
#     _saved_props = {}
#
#     @init_actions()
#     def __init__(self):
#         super().__init__()
#         self._mongo_db = MongoAPI.get_mongo_client("mlData")
#         self._mongo_url_group_clct = MongoAPI.get_collection_from_db(self._mongo_db, "mlData", "url_group")
#
#     async def _query_and_send_curr_object_defs(self, pk: UrlGroupAndUserGroup):
#         """取 user group 中该 url_group 的所有内容进行更新，发回 dce"""
#         ui_object_defs = {}
#         for doc in self._mongo_url_group_clct.find({"user_group": pk.user_group, "url_group": pk.url_group}):
#             v_ui_obj_def = get_namedtuple_from_dict(doc, UIObjectDefBySelector)
#             ui_object_defs[v_ui_obj_def.range_name] = v_ui_obj_def
#
#         await self.write_current_entity_props(pk, {
#             UIObjectDefsInUrlGroup.curr_object_defs: UIObjectDefCollection(ui_object_defs=ui_object_defs)})
#
#     @actionable(variables=[UIObjectDefsInUrlGroup.newly_added_object_def])
#     async def a_on_newly_added_ui_object_def(self, pk: UrlGroupAndUserGroup, v: UIObjectDefBySelector):
#         # 往 mongo upsert 数据
#         dict_ui_object_def = pk._asdict()
#         dict_ui_object_def.update(v._asdict())
#         dict_ui_object_def["_id"] = md5_str(f"{pk.user_group}:{pk.url_group}:{v.query_selector}")
#         MongoAPI.upsert_one(self._mongo_url_group_clct, "_id", dict_ui_object_def["_id"], dict_ui_object_def)
#         await self._query_and_send_curr_object_defs(pk)
#
#     @actionable(variables=[UIObjectDefsInUrlGroup.newly_removed_object_def])
#     async def a_on_newly_removed_ui_object_def(self, pk: UrlGroupAndUserGroup, v: UIObjectDefBySelector):
#         self._mongo_url_group_clct.delete_one({"_id": md5_str(f"{pk.user_group}:{pk.url_group}:{v.query_selector}")})
#         await self._query_and_send_curr_object_defs(pk)
#
#
# class WebUIObjectsManageEnv(Env):
#     """
#     每个 user (acct) 会有一个对应的 WebUIObjectsManageEnv ， 用于管理 页面上的 UI Object 以及 Entity Linking 等信息
#     """
#
#     REQUIRED_STATEFUL_SUBSCRIPTIONS: Set[str] = {"chrome_desktop_env"}
#
#     @init_actions()
#     def __init__(self, acct_id: str):
#         super().__init__()
#         self._user_id = acct_id
#
#         self._mongo_db = MongoAPI.get_mongo_client("mlData")
#         self._mongo_entity_props_clct = MongoAPI.get_collection_from_db(self._mongo_db, "mlData",
#                                                                         "url_based_entity_props")
#         self._mongo_url_can_not_extract = MongoAPI.get_collection_from_db(self._mongo_db, "mlData",
#                                                                           "url_can_not_extract")
#
#         self._db = dataset.connect("sqlite:///:memory:", ensure_schema=False)
#         self.tbl_urls_to_visit: Table = self._db.create_table("urls_to_visit", primary_id="id",
#                                                               primary_type=self._db.types.string)
#         self.tbl_urls_to_visit.create_column("user_id", self._db.types.string)
#         self.tbl_urls_to_visit.create_column("desktop_env_gid", self._db.types.string)
#         self.tbl_urls_to_visit.create_column("target_url", self._db.types.string)
#         self.tbl_urls_to_visit.create_column("triggered_from_url", self._db.types.string)
#         self.tbl_urls_to_visit.create_column("assigned_batch_gid", self._db.types.string)
#         self.tbl_urls_to_visit.create_column("job_status", self._db.types.integer)
#         self.tbl_urls_to_visit.create_column("mtime", self._db.types.datetime)
#
#         self.user_joined_groups = StateVariable(value_cls=Set[str], default_val=None, help="用户已经加入的业务组")
#
#         self._all_ui_object_defs_in_url_group = StateVariable(value_cls=Dict[str, Dict[str, UIObjectDefCollection]],
#                                                               default_val=None)
#         """所加入的 user group 中保存的所有 url group 中的 ui_object_defs
#             结构为 UserGroup > UrlGroup > UIObjectDefCollection
#         """
#
#         self.newly_updated_ui_object_defs = StateVariable(value_cls=Tuple[str, str, UIObjectDefCollection],
#                                                           default_val=None,
#                                                           memory_only=True)
#         """用于维护局部数据的某一个url_group 中的网页内容，
#             Tuple 的含义为 UserGroup > UrlGroup > UIObjectDefCollection
#         """
#
#         self.detected_ui_objects_and_linking = StateVariable(value_cls=Tuple[str, UIObjectsAndEntityLinkingInOnePage],
#                                                              default_val=None, memory_only=True)
#         """检测到的 ui object 和 entity , 以提供给 desktop chrome env 订阅"""
#
#         self.newly_assign_visit_urls_job = StateVariable(value_cls=BrowserVisitUrlsJob, default_val=None,
#                                                          memory_only=True)
#         """新分配给 Desktop Chrome Env 的 Task ，让其依次打开一批的网页"""
#
#         self.entities_value_to_sync = StateVariable(value_cls=Tuple[str, List[UIObjectsInOnePage]], default_val=None,
#                                                     memory_only=True)
#         """需要同步到 Chrome Desktop Env 的有关 Entity 的 value 内容"""
#
#         # DCE 的引用
#         self.url_group_dce_ref = DCERef(UrlGroupDataByUserGroup, write=False, read=True)
#
#         # 普通的 object attribute (memory)
#         self.available_chrome_envs_to_assign_job: Set[str] = set()
#         """可以指派任务的 chrome env 对象，是一个 hash_gid 的 set """
#
#     @actionable(variables=[UIObjectDefsInUrlGroup.curr_object_defs], subscription_from="url_group_dce_ref")
#     async def a_on_ui_object_def_update(self, pk: UrlGroupAndUserGroup, curr_object_defs: UIObjectDefCollection):
#         """从DCE中听有关当前 user group 中某个 url_group 的 ui_object_defs 的 snapshot """
#         if pk.user_group not in self.user_joined_groups.VALUE:
#             return
#         # NOTE: 如果要删除某个 url_group 中定义的 ui_object_defs 则会有一个 空的 dict 推送
#         await self.save_external_value("newly_updated_ui_object_defs", (pk.user_group, pk.url_group, curr_object_defs))
#
#     @actionable(variables=["newly_updated_ui_object_defs"])
#     async def a_on_newly_updated_ui_object_defs(self,
#                                                 ui_object_defs_in_url_group: Tuple[str, str, UIObjectDefCollection]):
#         """根据dce中维护的信息，更新本地文件中 url_group 的数据"""
#         user_group, url_group, ui_object_clct = ui_object_defs_in_url_group
#         dict_all_ui_object_defs_user_group = self._all_ui_object_defs_in_url_group.VALUE
#         if dict_all_ui_object_defs_user_group is None:
#             dict_all_ui_object_defs_user_group = dict()
#
#         dict_all_ui_object_defs_url_group = dict()
#         if user_group in dict_all_ui_object_defs_user_group:
#             dict_all_ui_object_defs_url_group = dict_all_ui_object_defs_user_group[user_group]
#         else:
#             dict_all_ui_object_defs_user_group[user_group] = dict_all_ui_object_defs_url_group
#
#         if ui_object_clct is None or ui_object_clct.ui_object_defs is None or len(ui_object_clct.ui_object_defs) == 0:
#             # 删除 url_group 中的内容
#             if url_group in dict_all_ui_object_defs_url_group:
#                 del dict_all_ui_object_defs_url_group[url_group]
#         else:
#             dict_all_ui_object_defs_url_group[url_group] = ui_object_clct
#         self._all_ui_object_defs_in_url_group.VALUE = dict_all_ui_object_defs_user_group
#
#         # mongo 中该 user_group 该 url_group 中已经提取出的内容，设置为 None
#         result = self._mongo_entity_props_clct.update_many({"url_group": url_group,
#                                                             "def_from_usr_group": {
#                                                                 "$elemMatch": {"$in": [user_group]}}},
#                                                            {"$set": {"status": 0}})
#         logger.info(f"Updated mongo set status = 0. {result}")
#
#
#     def _get_ui_object_defs_by_url_group(self, url_group: str,
#                                          dict_val: Dict[str, Dict[str, UIObjectDefCollection]]) \
#             -> Tuple[UIObjectDefCollection, Set[str]]:
#         """遍历所有的 user group ，得到符合 url_group 的 UIObjectDefCollection 数据
#
#         Returns
#         -------
#         -
#             Tuple[UIObjectDefs, Set[User_Group]]
#
#         """
#
#         dict_all_data = {}
#         matched_user_group = set()
#         for user_group, url_group_dict in dict_val.items():
#             if url_group not in url_group_dict:
#                 continue
#             dict_all_data.update(copy.deepcopy(url_group_dict[url_group].ui_object_defs))
#             matched_user_group.add(user_group)
#         if len(dict_all_data) > 0:
#             return UIObjectDefCollection(ui_object_defs=dict_all_data), matched_user_group
#         else:
#             return None, None
#
#     def _save_extracted_info(self, url_without_fragment: str, ui_objs: Dict[str, UIObjectInPage],
#                              from_user_groups: Set[str]):
#         """将提取到的 ui_object 信息，保存到 mongo ，以便于通过其他属性字段的方式进行查询"""
#         # NOTE: local storage因为没有索引或者无法提供 HA 特性，所以不适合在这个场景中使用）
#         ls_req = []
#         url_group = get_url_group_str(url_without_fragment)
#         for prop_name, prop_val_from_page in ui_objs.items():
#             dict_entity_prop_val = {}
#             dict_entity_prop_val["entity_url"] = url_without_fragment
#             dict_entity_prop_val["url_group"] = url_group  # 加 url group 是为了方便做 invalidate/expire 等标记
#             dict_entity_prop_val["start"] = prop_val_from_page.ui_obj.start
#             dict_entity_prop_val["end"] = prop_val_from_page.ui_obj.end
#             dict_entity_prop_val["str_val"] = prop_val_from_page.ui_obj.text_in_range
#             dict_entity_prop_val["prop_name"] = prop_name
#             dict_entity_prop_val["val"] = prop_val_from_page.val
#             dict_entity_prop_val["sync_time"] = prop_val_from_page.sync_time
#             dict_entity_prop_val["def_from_usr_group"] = list(from_user_groups)
#             dict_entity_prop_val["status"] = 1  # status , 1:valid , 0:invalid
#             id = md5_str(f"{url_without_fragment}-{prop_name}-{','.join(sorted(list(from_user_groups)))}")
#             dict_entity_prop_val["_id"] = id
#
#             dict_add_to_set = {"users": self._user_id}  # 叠加有哪些用户同步过该数据内容，以后可以作为某一个网页是否访问过的打卡记录
#             ls_req.append(
#                 UpdateOne({"_id": id}, {"$set": dict_entity_prop_val, "$addToSet": dict_add_to_set}, upsert=True))
#         result = self._mongo_entity_props_clct.bulk_write(ls_req)
#         logger.info(f"Save entity props in mongo {result}")
#
#     def _save_cant_extract_info(self, url_without_fragment: str, from_user_groups: Set[str]):
#         dict_row = dict()
#         dict_row["entity_url"] = url_without_fragment
#         dict_row["url_group"] = get_url_group_str(url_without_fragment)
#         dict_row["def_from_usr_group"] = list(from_user_groups)
#         dict_row["status"] = 1  # status , 1:valid , 0:invalid
#         dict_row["mtime"] = datetime.now()
#         id = md5_str(f"{url_without_fragment}-{','.join(sorted(list(from_user_groups)))}")
#         dict_row["_id"] = id
#         self._mongo_url_can_not_extract.replace_one({"_id": id}, dict_row, upsert=True)
#
#     @actionable(variables=["page_dom"], subscription_from="chrome_desktop_env")  # 如果来自于其他 inst 则前一个名字是 slot 的名字
#     async def a_on_page_dom_update(self, subscription_name: str, inst_hash: str, page_dom: PageWithDOM):
#         """监听 page_dom 的变动，提取页面中的 ui_objects"""
#         url = page_dom.url_without_fragment
#         url_group = get_url_group_str(url)
#
#         dict_all_ui_object_def = self._all_ui_object_defs_in_url_group.VALUE
#
#         all_extracted_ui_objects_in_page: Dict[str, UIObjectInPage] = dict()
#         all_ui_objects_entity_linking: Dict[str, List[UrlUniqueEntity]] = dict()
#
#         doc = PyQuery(bytes_2_object(page_dom.dom_binary))
#         # 先识别该 url_group 是否为当前网页需要处理的 url_group
#         curr_ui_object_defs, matched_user_group = self._get_ui_object_defs_by_url_group(url_group,
#                                                                                         dict_all_ui_object_def)
#         # region 检测 webpage 中定义过的 ui_objects
#
#         if curr_ui_object_defs:
#             ls_range_query_obj = list()
#             ls_range_def = list()
#             for range_name, range_def in curr_ui_object_defs.ui_object_defs.items():
#                 ui_obj_query_obj = doc(range_def.query_selector)
#                 if len(ui_obj_query_obj) > 0:  # 确保是一个在当前页面有效的 jquery selector才加入
#                     ls_range_query_obj.append(ui_obj_query_obj)
#                     ls_range_def.append(range_def)
#
#             if len(ls_range_query_obj) > 0:  # 确保至少能提取到一项数据内容
#                 ls_all_start_pos = batch_get_dom_node_start_pos(doc, ls_range_query_obj)
#                 for range_def, range_query_obj, range_start_pos in zip(ls_range_def, ls_range_query_obj,
#                                                                        ls_all_start_pos):
#                     if range_start_pos < 0:
#                         continue
#                     txt_in_range = get_pq_object_inner_text(range_query_obj)
#                     if not txt_in_range:  # 假定区域内一定要有文字
#                         continue
#                     ui_obj = OneDimUIObject(start=range_start_pos, end=range_start_pos + len(txt_in_range),
#                                             text_in_range=txt_in_range)
#                     ui_obj_gid = md5_str(f"{range_def.range_name}-{url}-{range_start_pos}")
#                     val = txt_in_range
#                     if range_def.dtype == DataType.int.value:
#                         val = int(val)
#                     elif range_def.dtype == DataType.float.value:
#                         val = float(val)
#                     elif range_def.dtype == DataType.bool.value:
#                         val = bool(val)
#                     ui_obj_in_page = UIObjectInPage(ui_obj=ui_obj, ui_obj_gid=ui_obj_gid, name=range_def.range_name,
#                                                     xpath=element_to_xpath(range_query_obj),
#                                                     outer_html=range_query_obj.outerHtml(), val=val,
#                                                     sync_time=datetime.now())
#
#                     all_extracted_ui_objects_in_page[range_def.range_name] = ui_obj_in_page
#                 # 页面上有哪些 named range 信息，更新到 mongo 中，以备查
#                 self._save_extracted_info(url, all_extracted_ui_objects_in_page, matched_user_group)
#             else:
#                 self._save_cant_extract_info(url, matched_user_group)
#
#         clct_eneities_to_query: Set[str] = set()
#         dict_entity_val: Dict[str, UIObjectsInOnePage] = dict()  # key 为 url , value 为各range 的 value
#
#         b_is_url_from_visit_job = False
#         if self.tbl_urls_to_visit.find_one(target_url=url):
#             b_is_url_from_visit_job = True
#
#         # 解析页面中的超链接，是否有符合 url_group 中的内容，标记出 ui_object 和 entity_linking
#         if not b_is_url_from_visit_job:
#             all_linking_objects = get_doc_hyperlinking(doc, base_url=url)
#             for linking_entity in all_linking_objects:
#                 # 必须有文字内容的超链接
#                 if not linking_entity.text or len(linking_entity.text) == 0:
#                     continue
#
#                 # 过滤掉一些不是 rule based entity 内容
#                 if not RuleBasedUrlEntityClassifier.is_entity_url(linking_entity.url):
#                     continue
#
#                 # url group 需要是被监测的
#                 inner_url_group = get_url_group_str(linking_entity.url)
#                 # 与当前网页是相同的 动态网页，一般是翻页类型的，这里不作为 entity linking ，避免无限循环
#                 if inner_url_group == url_group:
#                     continue
#
#                 inner_ui_object_defs, inner_matched_user_group = self._get_ui_object_defs_by_url_group(inner_url_group,
#                                                                                                        dict_all_ui_object_def)
#                 if not inner_ui_object_defs:
#                     continue
#                 ui_obj = OneDimUIObject(start=linking_entity.start_pos, end=linking_entity.end_pos,
#                                         text_in_range=linking_entity.text)
#                 ui_obj_gid = md5_str(f"linking_in_page-{url}-{linking_entity.start_pos}")
#                 ui_obj_name = f"linking_in_page#{linking_entity.start_pos}"
#                 ui_obj_in_page = UIObjectInPage(ui_obj=ui_obj, ui_obj_gid=ui_obj_gid, name=ui_obj_name,
#                                                 xpath=element_to_xpath(linking_entity.query_obj),
#                                                 outer_html=linking_entity.query_obj.outerHtml(), val=linking_entity.text,
#                                                 sync_time=datetime.now())
#                 all_extracted_ui_objects_in_page[ui_obj_name] = ui_obj_in_page
#                 all_ui_objects_entity_linking[ui_obj_gid] = [UrlUniqueEntity(url=linking_entity.url)]
#                 clct_eneities_to_query.add(linking_entity.url)
#
#             # 从 Mongo 中得到 ls_eneities_to_query 中的 prop 信息，并赋值到 dict 中
#             dict_query = {
#                 "entity_url": {"$in": list(clct_eneities_to_query)},
#                 "def_from_usr_group": {"$elemMatch": {"$in": list(self.user_joined_groups.VALUE)}}
#             }
#
#             rlt_extracted_props = self._mongo_entity_props_clct.find(dict_query)
#             # NOTE:两个查询条件正好是一致的
#             # 以后可以基于 status 的条件，控制更加精准的范围
#             rlt_cant_extract = self._mongo_url_can_not_extract.find(dict_query)
#
#             clct_cant_extract_urls = set([row["entity_url"] for row in rlt_cant_extract])
#             clct_invalid_entity_urls = set()  # 为了便于查询，收集已经 Invalid 的 内容
#
#             # 只保留尚未查询过的 entities 的内容
#             clct_eneities_to_query = clct_eneities_to_query.difference(clct_cant_extract_urls)
#
#             for item in rlt_extracted_props:
#                 if item["status"] == 0:
#                     clct_invalid_entity_urls.add(item["entity_url"])
#                 ui_obj = UIObjectInPage(
#                     ui_obj=OneDimUIObject(start=item["start"], end=item["end"], text_in_range=item["str_val"]),
#                     ui_obj_gid=item["_id"], name=item["prop_name"], val=item["val"], sync_time=item["sync_time"])
#                 if item["entity_url"] in dict_entity_val:
#                     dict_entity_val[item["entity_url"]].ui_objects[item["prop_name"]] = ui_obj
#                 else:
#                     dict_entity_val[item["entity_url"]] = UIObjectsInOnePage(url_without_fragment=item["entity_url"],
#                                                                              ui_objects={item["prop_name"]: ui_obj})
#
#             # 将需要同步的 entities 维护到 tbl_urls_to_visit
#             for entity_url in clct_eneities_to_query:
#                 # 已经invalid 或者没查到 ui object 的 entity linking 都需要被同步
#                 # NOTE : 这里还缺少 entity url 属于例外，无法提取到 entity 的情况
#                 #       （解决方法：也设定出至少一个 range 避免重复）
#                 if entity_url in clct_invalid_entity_urls or entity_url not in dict_entity_val:
#                     # NOTE : 因为这里是内存表，且没有 upsert_many 的接口，所以先不批量
#                     self.tbl_urls_to_visit.upsert({
#                         "id": md5_str(f"{self._user_id}-{entity_url}"),
#                         "user_id": self._user_id,
#                         "desktop_env_gid": inst_hash,
#                         "target_url": entity_url,
#                         "triggered_from_url": url,
#                         "job_status": JobStatus.not_assigned.value,
#                         "mtime": datetime.now()
#                     }, ["id"])
#
#         self.detected_ui_objects_and_linking.VALUE = (inst_hash,
#                                                       UIObjectsAndEntityLinkingInOnePage(url_without_fragment=url,
#                                                                                          ui_objects=all_extracted_ui_objects_in_page,
#                                                                                          entities_linking=all_ui_objects_entity_linking))
#
#         if dict_entity_val:  # 有超链接的 entities 的 value , 通知 desktop 进行同步
#             self.entities_value_to_sync.VALUE = (inst_hash, [v for v in dict_entity_val.values()])
#
#     @actionable(variables=["newly_joined_group"], subscription_from="chrome_desktop_env")
#     async def a_on_newly_joined_group(self, subscription_name: str, inst_hash: str, newly_joined_group: str):
#         joined_groups = self.user_joined_groups.VALUE
#         if joined_groups is None:
#             joined_groups = set()
#         if newly_joined_group not in joined_groups :
#             joined_groups.add(newly_joined_group)
#             self.user_joined_groups.VALUE = joined_groups
#
#     @actionable(variables=["newly_leave_group"], subscription_from="chrome_desktop_env")
#     async def a_on_newly_leave_group(self, subscription_name: str, inst_hash: str, newly_leave_group: str):
#         joined_groups = self.user_joined_groups.VALUE
#         if joined_groups is None:
#             joined_groups = set()
#         # remove
#         if newly_leave_group in joined_groups:
#             joined_groups.discard(newly_leave_group)
#             self.user_joined_groups.VALUE = joined_groups
#
#     @actionable(variables=["job_heart_beats"], subscription_from="chrome_desktop_env")
#     async def a_on_chrome_env_heart_beats(self, subscription_name: str, inst_hash: str, job_heart_beats: JobHeartBeats):
#         # 先判定 kafka 中是一个有效的心跳包，而不是一个历史心跳包的内容
#         if abs((job_heart_beats.beats_ts - datetime.now()).total_seconds()) > 30. * 60:
#             return
#         if not job_heart_beats.remain_jobs and job_heart_beats.can_assign_jobs:
#             self.available_chrome_envs_to_assign_job.add(inst_hash)
#
#     @actionable(variables=["job_status"], subscription_from="chrome_desktop_env")
#     async def a_on_job_status_update(self, subscription_name: str, inst_hash: str, job_status: BrowserJobStatus):
#         if job_status.status == JobStatus.finish.value:
#             count_before_del = self.tbl_urls_to_visit.count()
#             self.tbl_urls_to_visit.delete(desktop_env_gid=inst_hash, assigned_batch_gid=job_status.job_id)
#             logger.info(f"Urls visit job have {self.tbl_urls_to_visit.count()} rows , pre value is {count_before_del} ")
#             self.available_chrome_envs_to_assign_job.add(inst_hash)
#
#     @actionable(variables=["urls_redirection"], subscription_from="chrome_desktop_env")
#     async def a_on_urls_redirection(self, subscription_name: str, inst_hash: str,
#                                     urls_redirection: List[Tuple[str, str]]):
#         """网页重定向的信息被探测到，在 mongo 中记录重定向的源地址是一个异常地址，避免重复的提取数据"""
#         for from_to_url in urls_redirection:
#             from_url, to_url = from_to_url
#             url_without_fragment = get_url_without_fragment(from_url)
#             self._save_cant_extract_info(url_without_fragment, self.user_joined_groups.VALUE)
#             self.tbl_urls_to_visit.delete(target_url=from_url)
#
#     @actionable(variables=["active_flag"])
#     async def a_on_active_flag_change(self, v: int):
#         if v == 1:
#             # TODO: 比对 mongo 中有关 user group 数据的存储信息
#             pass
#
#     async def _url_visit_job_to_assign(self):
#         if not self.available_chrome_envs_to_assign_job:
#             return
#         env_to_assign = choice(list(self.available_chrome_envs_to_assign_job))
#         # 固定取最新的10条记录，以后再加 random choice
#         rows = self.tbl_urls_to_visit.find(job_status=JobStatus.not_assigned.value, _limit=10, order_by=["-mtime"])
#
#         urls_to_navi: List[Tuple[str,str]] = list()
#         ids_to_update: List[str] = list()
#         # ALERT : rows 只能遍历一次，是一个类似于 cursor 对象
#         for row in rows:
#             urls_to_navi.append((row["triggered_from_url"], row["target_url"]))
#             ids_to_update.append("'"+str(row["id"])+"'")
#
#         if not urls_to_navi:
#             return
#         job_batch_gid = get_random_uuid()
#
#         sql = f"""UPDATE urls_to_visit SET assigned_batch_gid='{job_batch_gid}' , job_status={JobStatus.waiting.value} WHERE id in ({','.join(ids_to_update)})"""
#         logger.info(sql)
#         self._db.query(sql)
#
#         self.newly_assign_visit_urls_job.VALUE = BrowserVisitUrlsJob(id=job_batch_gid, runner_env_id=env_to_assign,
#                                                                      urls_to_navi=urls_to_navi,
#                                                                      assigned_time=datetime.now())
#         logger.info(self.newly_assign_visit_urls_job.VALUE)
#         self.available_chrome_envs_to_assign_job.remove(env_to_assign)
#
#     @timer(interval=10.0)
#     async def on_timer_10secs(self):
#         """每十秒钟检查一次，是否需要指派任务到 chrome desktop env"""
#         await self._url_visit_job_to_assign()
