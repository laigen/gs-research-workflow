# -*- coding: utf-8 -*-
from datetime import datetime

from gs_research_workflow.rpa_workflow.envs.general_rpa_action_assign_to_run import debug_one_action_result

from gs_research_workflow.common.mongo_resource import db_nlp, used_db_position, mongo_db_conn

from gs_research_workflow.rpa_workflow.actions.action_doc_in_mongo import RPAActionDoc

mongo_db_conn(used_db_position, db_nlp)


def re_extract_batch_action_result(batch_action_uuid: str):
    actions = RPAActionDoc.objects(batch_id=batch_action_uuid)
    for action in actions:
        print(action.act_id)
        debug_one_action_result(action.act_id)


def _parse_date(date_string: str) -> datetime:
    # NOTE:这里 new DateDataParser() 对象，避免上一次的判断条件会产生影响，将该函数变成 non state 的
    from dateparser import DateDataParser
    data = DateDataParser(try_previous_locales=False).get_date_data(date_string, None)
    if data:
        return data['date_obj']


def split_by_chn_dot(s: str) -> str:
    """适用于从 雪球 获取的时间字符串，eg : "05-29 13:55 · 来自新闻" => "05-29 13:55"""
    return s.split("·")[0].strip()


if __name__ == "__main__":
    re_extract_batch_action_result("BDECD1C872EF415404B6E0879EAF5AE9")
#     ls_dates=["今天 15:41 · 来自新闻",
# "今天 14:44 · 来自新闻",
# "今天 13:51 · 来自新闻",
# "今天 13:11 · 来自新闻",
# "今天 10:27 · 来自新闻",
# "今天 09:26 · 来自新闻",
# "今天 08:15 · 来自新闻",
# "06-27 15:43 · 来自新闻",
# "06-27 13:41 · 来自新闻",
# "06-27 09:21 · 来自新闻",
# "06-26 16:18 · 来自新闻",
# "06-25 23:11 · 来自新闻",
# "06-25 16:14 · 来自新闻",
# "06-25 09:53 · 来自新闻",
# "06-25 08:49 · 来自新闻",
# "06-25 07:11 · 来自新闻",
# "06-21 17:30 · 来自新闻",
# "06-19 12:00 · 来自新闻",
# "06-18 16:35 · 来自新闻",
# "06-18 14:24 · 来自新闻",
# "06-18 10:04 · 来自新闻",
# "06-18 02:05 · 来自新闻",
# "06-17 17:48 · 来自新闻",
# "06-17 17:30 · 来自新闻",
# "06-17 15:10 · 来自新闻",
# "06-17 14:59 · 来自新闻",
# "06-17 13:51 · 来自新闻",
# "06-17 01:54 · 来自新闻",
# "06-11 15:12 · 来自新闻",
# "06-09 11:46 · 来自新闻",
# "06-09 08:25 · 来自新闻",
# "06-08 16:55 · 来自新闻",
# "06-08 15:53 · 来自新闻",
# "06-07 15:24 · 来自新闻",
# "05-28 17:44 · 来自新闻",
# "05-23 03:06 · 来自新闻",
# "05-12 11:31 · 来自新闻",
# "04-29 17:29 · 来自新闻",
# "04-29 14:09 · 来自新闻",
# "04-29 11:47 · 来自新闻",
# "04-27 10:10 · 来自新闻",
# "04-25 22:59 · 来自新闻",
# "04-19 00:45 · 来自新闻",
# "04-16 17:01 · 来自新闻",
# "04-16 14:32 · 来自新闻",
# "04-13 07:28 · 来自新闻",
# "04-09 12:01 · 来自新闻",
# "04-08 19:17 · 来自新闻",
# "04-08 11:04 · 来自新闻",
# "03-29 12:03 · 来自新闻"
# ]
#     for s in ls_dates:
#         print(_parse_date(split_by_chn_dot(s)))
