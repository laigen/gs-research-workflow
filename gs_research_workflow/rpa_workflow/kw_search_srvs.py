# -*- coding: UTF-8 -*-

"""
与 keywords search 有关的 Service，将以 RL Framework 的方式定义 Service

Env ： 接收 Keywords (Action) 提交到前端，搜索到的内容作为 State
Agent : 提供 keyword 的内容

"""

import logging

import faust

from gs_research_workflow.common.mongo_resource import db_nlp, used_db_position, mongo_db_conn

logger = logging.getLogger(__name__)

topic_kw_search = faust.types.TP("kw_search_envs_and_angents-v001", 1)

mongo_db_conn(used_db_position, db_nlp)

#
# class KWSearchExternalEnv(Env):
#     """ 实现 keyword search 相关服务的 env """
#
#     uipath_action_stream = ObjectStateStream.bind_at_runtime()
#     agent = ObjectRef.bind_at_runtime()
#
#     state = StateVariable(dtype=pd.DataFrame, default_val=None, help="Search Result by keywords")
#
#     def __init__(self, target_site: str = "news.google.com", target_terminal: str = "gs_win10_vm_001"):
#         super().__init__()
#         self._target_site = target_site
#         self._target_terminal = target_terminal
#
#     @state_var_change_handler(state_vars=["action"], state_var_source=agent)
#     @pick_one_change
#     async def on_agent_action(self, state_var_owner_pk: Any, state_var_name: str, kws: List[str]):
#         # create a kw search
#         act_uuid = generate_uuid()
#         act = create_stateful_object(act_uuid, WinRPAAction)
#         act[WinRPAAction.action_uuid].VALUE = act_uuid
#         act[WinRPAAction.action].VALUE = RPAAction(creator_cls=cls_to_str(self.__class__), creator_uuid=self.pk,
#                                                    action_executor_required_tags=[f"ext_envs:{self._target_site}",
#                                                                                   f"terminal_id:{self._target_terminal}"],
#                                                    ctime=datetime.now(),
#                                                    description=f"create by {cls_to_str(self.__class__)}(pk={self.pk}) @{datetime.now()} ",
#                                                    action=[AtomAction(
#                                                        workflow_name="browser_kw_search_actions/act_batch_google_news_search",
#                                                        para=kws)])
#         logger.info(f"A keyword search is sent. '{kws}'")
#         return StatefulObjectAndCommitStream(act, self.uipath_action_stream)
#
#     @state_var_change_handler(state_vars=WinRPAAction.action_orig_result, state_var_source=uipath_action_stream)
#     @pick_one_change
#     async def on_act_orig_result(self, state_var_owner_pk: Any, state_var_name: str,
#                                  act_orig_result: RPAActionOrigResult):
#         # logger.info(f"Search result msg. {act_orig_result.creator_uuid} - {self.pk}")
#         if act_orig_result.creator_uuid != self.pk:
#             return
#         logger.info(f"Search result returned. {act_orig_result.creator_uuid} - {act_orig_result.success_flag}")
#         # act_orig_result.rlt_data 解包解压后存入 Mongo，同时生成 state 的 dataframe 数据对象
#         if act_orig_result.rlt_bin_data_uuid:
#             rlt_bin_data = None
#             if act_orig_result.rlt_bin_data_uuid:
#                 rlt_bin_doc = ActionResultBinary.objects.get(uuid=act_orig_result.rlt_bin_data_uuid)
#                 rlt_bin_data = rlt_bin_doc.bin
#                 logger.info(f"bin data result length={len(rlt_bin_data)}")
#             KWSearchExternalEnv.upload_search_result_via_tar_binary(state_var_owner_pk, rlt_bin_data)
#
#     @staticmethod
#     def upload_search_result_via_tar_binary(act_uuid: str, tar_gz_binary: bytes):
#         import tarfile
#         import glob
#         import os
#         import tempfile
#
#         with tempfile.TemporaryDirectory() as tmp_dir:
#             tar_file = os.path.join(tmp_dir, "search_result.tar.gz")
#             with open(tar_file, "w+b") as tar_f:
#                 tar_f.write(tar_gz_binary)
#                 tar_f.flush()
#             tar = tarfile.open(tar_file, "r:gz")
#             tar.extractall(tmp_dir)
#             tar.close()
#             kw_search_results = glob.glob(os.path.join(tmp_dir, act_uuid, "*_index_items.csv"))
#             if kw_search_results:
#                 for f in kw_search_results:
#                     logger.info(f"upload search result file {f}")
#                     try:
#                         df = pd.read_csv(f, header=0, parse_dates=["publish_time"])
#                         df = KWSearchExternalEnv.google_news_data_preprocess(df)
#                         KWSearchExternalEnv.save_news_data_to_mongo(df)
#                     except Exception as ex:
#                         logger.error(f"{ex}")
#                         continue
#
#     @staticmethod
#     def google_news_data_preprocess(df: pd.DataFrame) -> pd.DataFrame:
#         """ 对 google news 上抓取到的数据内容进行预处理，主要做的工作是：
#         1) 合并 news_title - folding_news_title , url - folding_url 两列数据
#         2) 将相对 url 都转成绝对 url 的内容
#         """
#         if "publish_time" not in df.columns:  # 没有抓到过 publish time 的数据
#             return None
#         df["_title"] = df.apply(
#             lambda row: row["news_title"] if row["news_title"] is not np.nan else row["folding_news_title"], axis=1)
#         df["_url"] = df.apply(
#             lambda row: row["url"] if row["url"] is not np.nan else row["folding_url"], axis=1)
#         df["abs_url"] = df["_url"].apply(lambda x: "news.google.com" + x[1:])
#         df.drop(columns=["news_title", "_url", "url"], inplace=True)
#         if "folding_news_title" in df.columns:
#             df.drop(columns=["folding_news_title", "folding_url"], inplace=True)
#         df["uuid"] = df.apply(lambda row: md5_str(f"{row['publisher']}-{row['_title']}"), axis=1)
#         df.rename(columns={"_title": "news_title", "abs_url": "url"}, inplace=True)
#         df.set_index("uuid", drop=True, inplace=True)
#         df.dropna(subset=["publish_time"], axis=0, inplace=True)
#         return df
#
#     @staticmethod
#     def save_news_data_to_mongo(df: pd.DataFrame):
#         if df is None:
#             return
#         for news_uuid, row in df.iterrows():
#             kw_for_search = KeywordForSearch(keyword=row["keyword"])
#             news = NewsIndex(uuid=news_uuid, title=row["news_title"], abstract=row["news_abstract"], url=row["url"],
#                              publisher=row["publisher"],
#                              publish_time=row["publish_time"], search_engine=row["source"],
#                              from_keyword=kw_for_search)
#             news.save()
#             # logger.info(f"""add news {news.uuid} - {news.title}""")
#
#
# class RuleBasedKWGenerator(Agent):
#     env = ObjectRef.bind_at_runtime()
#     action = StateVariable(dtype=List[str], default_val=None, help="keywords as action")
#     smoke_test_ts = StateVariable(dtype=datetime, default_val=None, help="trigger for create a smoke test action")
#
#     def __init__(self, kw_source: str):
#         """
#         kw_source 可用于约定 rule base 的来源。 比如说，是 来自于某个用户所管理的 kw 内容
#         """
#         super().__init__()
#
#     @state_var_change_handler(state_vars=smoke_test_ts)
#     @pick_one_change
#     async def on_smoke_test_ts_changed(self, state_var_owner_pk: Any, state_var_name: str, smoke_test_ts: datetime):
#         # keywords for smoke test
#         logger.info(f"Start a smoke test.")
#         sml_query_kws = query_search_kws(0, 2)
#         if not sml_query_kws:
#             sml_query_kws = ["Trump Speech", "Trump Hiring"]
#         self.action.VALUE = sml_query_kws
#
#     @timer(interval=3600. * 24)
#     async def on_one_day_timer(self):
#         # TODO: 从 mongo 中读取 keywords list
#         # self.action.VALUE = query_search_kws(0, 1000000)
#         # self.smoke_test_ts.VALUE = datetime.now()
#         # await self.commit_state_var_changes()
#         pass
#
#
# async def start_google_news_search(target_terminal: str = "gs_win10_vm_001", kw_source: str = "ZT"):
#     logger.info(f"----------- preparing -------------")
#     env = KWSearchExternalEnv(target_site="news.google.com", target_terminal=target_terminal)
#     agent = RuleBasedKWGenerator(kw_source)
#     env.bind(topic_define=topic_kw_search)
#     agent.bind(topic_define=topic_kw_search)
#
#     env.agent.bind(agent.pk, topic_define=topic_kw_search)
#     agent.env.bind(env.pk, topic_define=topic_kw_search)
#
#     env.uipath_action_stream.bind(topic_define=topic_uipath_actions)
#
#     logger.info(f"----------- env start -------------")
#     await env.start()
#
#     logger.info(f"----------- agent start -------------")
#     await agent.start()
#
#     logger.info(f"----------- start finished , kick off smoke test -------------")
#     agent.smoke_test_ts.VALUE = datetime.now()
#     agent.commit_state_var_changes()
#
#
# def manually_upload_news_content():
#     file_path = "/tmp/laigen/debug_data/35C095879BDB45148654B04CF4BB5DB2_rlt.tar.gz"
#     with open(file_path, "r+b") as f:
#         bin_data = f.read()
#     KWSearchExternalEnv.upload_search_result_via_tar_binary("35C095879BDB45148654B04CF4BB5DB2", bin_data)
#
#
# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     # target_terminal = "gs_win10_vm_001" # laigen's desktop
#     target_terminal = "gs_robot_win10_vm_001"  # one of vpc
#     loop.run_until_complete(start_google_news_search(target_terminal=target_terminal))
#     loop.run_forever()
