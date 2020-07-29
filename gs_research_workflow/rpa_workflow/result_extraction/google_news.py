# -*- coding: UTF-8 -*-
import glob
import os
from typing import Tuple, List

import numpy as np
import pandas as pd
from gs_framework.utilities import md5_str

from gs_research_workflow.nlp.data.docs_in_mongo import Article, SearchingPhrase
from gs_research_workflow.rpa_workflow.result_extraction.utilities import append_site_to_url, upsert_document
import logging
logger = logging.getLogger(__name__)


class GoogleNewsSearchProcess:

    site = "https://news.google.com"

    @staticmethod
    def proc_news_search_data(df: pd.DataFrame) -> Tuple[str, pd.DataFrame]:
        """ 对 google news 上抓取到的数据内容进行预处理，主要做的工作是：
        1) 合并 news_title - folding_news_title , url - folding_url 两列数据
        2) 将相对 url 都转成绝对 url 的内容
        """


        all_columns = set(["news_title","url","news_abstract","publisher","publish_time","keyword","source"])
        assert set(df.columns.to_list()).issuperset(all_columns), str(all_columns - set(df.columns.to_list()))

        kw = df.loc[0, "keyword"]

        df["_title"] = df.apply(
            lambda row: row["news_title"] if row["news_title"] is not np.nan else row["folding_news_title"], axis=1)

        df["_url"] = df.apply(
            lambda row: row["url"] if row["url"] is not np.nan else row["folding_url"], axis=1)

        df["abs_url"] = df["_url"].apply(lambda x: append_site_to_url(x, GoogleNewsSearchProcess.site))

        df.drop(columns=["news_title", "_url", "url", "keyword", "source"], inplace=True)
        if "folding_news_title" in df.columns:
            df.drop(columns=["folding_news_title", "folding_url"], inplace=True)
        # df["uuid"] = df.apply(lambda row: md5_str(f"{row['publisher']}-{row['_title']}"), axis=1)
        df.rename(columns={"_title": "news_title", "abs_url": "url"}, inplace=True)
        # df.set_index("uuid", drop=True, inplace=True)
        df.dropna(subset=["publish_time"], axis=0, inplace=True)
        return kw, df

    @staticmethod
    def kw_news_search(rlt_path: str, batch_action_uuid: str, action_uuid: str, save_doc: bool = True) -> List[Article]:
        rlt_articles: List[Article] = list()

        rlt_files = glob.glob(os.path.join(rlt_path, "*_index_items.csv"))
        if rlt_files:
            for i, f in enumerate(rlt_files):
                try:
                    df_from_csv = pd.read_csv(f, header=0, parse_dates=["publish_time"])
                except:
                    continue
                kw, df_rlt = GoogleNewsSearchProcess.proc_news_search_data(df_from_csv)
                if df_rlt is None:
                    continue
                logger.info(f"proecess file : {f} - {df_rlt.shape}")
                # print(df_rlt)
                for idx, row in df_rlt.iterrows():
                    dict_row = row.to_dict()
                    dict_article = dict()
                    if not pd.isna(dict_row.get("news_title", np.NaN)):
                        dict_article["title"] = dict_row["news_title"]
                    if not pd.isna(dict_row.get("url", np.NaN)):
                        dict_article["full_text_url"] = dict_row["url"]
                    if not pd.isna(dict_row.get("news_abstract", np.NaN)):
                        dict_article["abstract"] = dict_row["news_abstract"]
                    if dict_row.get("publish_time", pd.NaT) is not pd.NaT:
                        dict_article["publish_time"] = dict_row["publish_time"].to_pydatetime()

                    search_phrase_in_db = SearchingPhrase.objects(searching_phrase=kw).first()
                    if search_phrase_in_db is not None:
                        dict_article["from_searching_phase"] = search_phrase_in_db
                        if search_phrase_in_db.related_symbols is not None:
                            dict_article["related_symbols"] = search_phrase_in_db.related_symbols
                    else:
                        dict_article["from_searching_phase"] = SearchingPhrase(searching_phrase=kw)

                    dict_article["engine_site"] = "google_news"
                    if not pd.isna(dict_row.get("publisher", np.NaN)):
                        dict_article["channel_in_site"] = dict_row["publisher"]
                        dict_article["uuid"] = md5_str(f"{dict_article['channel_in_site']}-{dict_article['title']}")
                    else:  # 暂定没有 publisher 的 news 不入库
                        continue
                    dict_article["batch_action_uuid"] = batch_action_uuid
                    article = Article(**dict_article)
                    rlt_articles.append(article)
                    if save_doc:
                        upsert_document(article, True)

        return rlt_articles