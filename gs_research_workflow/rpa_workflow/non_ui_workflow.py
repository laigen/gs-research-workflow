# -*- coding: utf-8 -*-

"""
先定义一些 hardcode 的直接，便于进行试用的代码
"""
import csv
import itertools
from typing import List

from gs_framework.utilities import md5_str

from gs_research_workflow.common.mongo_resource import mongo_db_conn, db_nlp, used_db_position
import pandas as pd
import logging

logger = logging.getLogger(__name__)

mongo_db_conn(used_db_position, db_nlp)


def upsert_tag_with_kws(tag_name: str, kws: List[str]):
    tag = Tag(name=tag_name)
    tag.save()
    for curr_kw in kws:
        kw = Keyword(kw=curr_kw, tags=[tag])
        kw.save()


def upsert_tag_combination(tags: List[str]):
    kw_comb = KWCombinationPattern(tags_comb_hash=md5_str("".join(sorted(tags))),
                                   tags_value="+".join(tags),
                                   tags=[Tag(name=n) for n in tags])
    kw_comb.save()


def generate_search_keywords():
    """根据已经好的 tag combination 的内容，生成  search keywords 的数据 """
    for tag_comb in KWCombinationPattern.objects:
        print("*"*10 + tag_comb.tags_value + "*"*10)
        ls_kws = list()
        for tag in tag_comb.tags:
            ls_kws.append([kw.kw for kw in Keyword.objects(tags=tag)])
        for curr_kws in itertools.product(*ls_kws):
            keywords = [Keyword(kw=k) for k in curr_kws]
            kw_for_search = KeywordForSearch(keyword=" ".join(curr_kws), from_combination=tag_comb, keywords=keywords)
            kw_for_search.save()


def query_search_kws(from_idx: int, to_idx: int) -> List[str]:
    kws = KeywordForSearch.objects.order_by("+keyword")[from_idx:to_idx]
    return [k.keyword for k in kws]


def query_news_and_output():
    # all_news = NewsIndex.objects[0:2]
    all_news = NewsIndex.objects()
    ls_news_dict = list()
    for news_idx, news in enumerate(all_news):
        dict_n = dict(uuid=news.uuid, title=news.title, publisher=news.publisher, abstract=news.abstract, url=f"https://{news.url}",
                      publish_time=news.publish_time)
        dict_n["search_kw"] = news.from_keyword.keyword
        for i, kw in enumerate(news.from_keyword.keywords):
            dict_n[f"kw_{i}"] = kw.kw
        for i, tag in enumerate(news.from_keyword.from_combination.tags):
            dict_n[f"tag_{i}"] = tag.name
        ls_news_dict.append(dict_n)
        if news_idx % 500 == 0:
            logger.info(f"read no. {news_idx} news.")
    df = pd.DataFrame(data=ls_news_dict)
    df.to_csv("/tmp/laigen/debug_data/news_extracted.csv", index=False, quoting=csv.QUOTE_NONNUMERIC)


def create_test_tags():
    upsert_tag_with_kws("govt_central", ["Xi", "Trump", "State Union", "China Standing Committee"])
    upsert_tag_with_kws("govt_central_action",
                        ["Speech", "Visiting", "Meeting", "Hiring", "Firing", "Election", "Trade War",
                         "Conventional War", "sanction"])
    upsert_tag_with_kws("state_or_province",
                        ["New York State", "New York City", "Washington", "New Jersey", "Shanghai", "Wuhan"])

    upsert_tag_with_kws("govt_branches", ["CDC", "Foreign Affairs", "Central Bank", "Statistics"])
    upsert_tag_with_kws("multi_national", ["IMF", "World Bank", "IEOR"])
    upsert_tag_with_kws("multi_national_action",
                        ["Financial Aid", "Forecasting", "Speech", "paper"])
    upsert_tag_with_kws("CEO", ["Bill Gates"])
    upsert_tag_with_kws("bull_finance", ["Goldman", "JPM", "Citi", "CICC"])
    upsert_tag_with_kws("bear_independent", ["Andy Xie", "David Ronsenberg", "Jim Rogers", "Ray Dalio"])
    upsert_tag_with_kws("pm_analyst", ["Buffett", "Munger"])

    upsert_tag_with_kws("stock", ["AAPL", "FB", "GOOG", "NFLX", "MSFT", "AMZN", "BABA", "NTES",
                                  "Tencent", "PTR", "PDD", "MAR", "CMG", "DRI", "UAL", "DAL",
                                  "YUM", "TSLA"])
    upsert_tag_with_kws("bond", ["LQD", "HYG", "investment grade"])
    upsert_tag_with_kws("ETF", ["BIZD"])
    upsert_tag_with_kws("VOL", ["VIX", "VXX", "TVIX"])

    upsert_tag_with_kws("funds_action", ["Inflow", "Outflow", "Launch", "Closing", "Liquidation"])

    upsert_tag_with_kws("ECON", ["PMI", "GDP", "CPI", "PPI", "Unemployment", "Job Creation", "jobless"])
    upsert_tag_with_kws("Commodity", ["Gold", "Oil", "Copper", "Silver", "Soybean"])
    upsert_tag_with_kws("tech", ["Iphone", "Smartphone", "Graphics Card", "DRAM"])


def create_test_tag_combination():
    for s in ["stock", "bond", "ETF", "VOL", "ECON", "Commodity", "tech"]:
        upsert_tag_combination(["govt_central", "govt_central_action", s])
        upsert_tag_combination(["state_or_province", s])
        upsert_tag_combination(["govt_branches", s])
        upsert_tag_combination(["multi_national", "multi_national_action", s])
        upsert_tag_combination(["CEO", s])
        upsert_tag_combination(["bull_finance", s])
        upsert_tag_combination(["bear_independent", s])
        upsert_tag_combination(["pm_analyst", s])


if __name__ == "__main__":
    # create_test_tags()
    # create_test_tag_combination()
    # generate_search_keywords()
    # print(query_search_kws(0, 10000))
    query_news_and_output()
