# -*- coding: UTF-8 -*-
import glob
import os
from datetime import datetime
from typing import Optional, Tuple, List, Dict

import numpy as np
import pandas as pd
from gs_framework.utilities import md5_str

from gs_research_workflow.nlp.data.docs_in_mongo import Article, UserInTwitter, TweetExtra, SearchingPhrase, \
    FinancialInstrumentSymbol, AuthorInSeekingAlpha
from gs_research_workflow.rpa_workflow.result_extraction.utilities import parse_num_from_str, upsert_document, \
    append_site_to_url
import logging
logger = logging.getLogger(__name__)


class EastMoneyDataProcess:

    @staticmethod
    def proc_stock_analysis(df: pd.DataFrame) -> pd.DataFrame:
        def _symbol_to_yahoo_symbol(x):
            if isinstance(x, str):
                if x.startswith("6"):
                    return f"{x}.SS"
                else:
                    return f"{x}.SZ"
            elif isinstance(x, int):
                if 700000 > x >= 600000:
                    return f"{x}.SS"
                else:
                    return f"{x:06}.SZ"
            else:
                return x

        df["symbol"] = df["symbol"].apply(_symbol_to_yahoo_symbol)
        report_url_root = "http://data.eastmoney.com/report"
        df["article_url"] = df["article_url"].apply(
            lambda x: append_site_to_url(x, report_url_root))
        df["org_url"] = df["org_url"].apply(
            lambda x: append_site_to_url(x, report_url_root))
        df["industry_url"] = df["industry_url"].apply(
            lambda x: append_site_to_url(x, report_url_root))

        def _rating_to_int(x) -> Optional[int]:
            # ['买入' '增持' '-' '中性' '持有' '回避' '卖出']
            if x == "买入":
                return 2
            elif x == "增持":
                return 1
            elif x == "中性" or x == "持有":
                return 0
            elif x == "回避":
                return -1
            elif x == "卖出":
                return -2
            else:
                return None

        df["rating"] = df["rating"].apply(_rating_to_int)
        df["rating"] = df["rating"].astype("Int64")

        def _rating_chg_to_int(x) -> Optional[int]:
            # ['首次' '维持' '调高' '-' '调低' '无']
            if x == "首次":
                return None
            elif x == "维持":
                return 0
            elif x == "调高":
                return 1
            elif x == "调低":
                return -1
            else :
                return None

        df["rating_chg"] = df["rating_chg"].apply(_rating_chg_to_int)
        df["rating_chg"] = df["rating_chg"].astype("Int64")

        df["report_date"] = df["report_date"].apply(lambda x: datetime.strptime(x, "%Y-%m-%d"))
        df["report_date"] = df["report_date"].astype("datetime64")
        for col in ["id", "industry", "industry_url", "symbol_url"]:
            if col in df.columns:
                df.drop(columns=[col], inplace=True)

        return df

    @staticmethod
    def symbol_analysis_report(rlt_path: str, batch_action_uuid: str, action_uuid: str, save_doc: bool = True) -> List[Article]:

        rlt_articles: List[Article] = list()

        rlt_files = glob.glob(os.path.join(rlt_path, "*_symbol_analysis.csv"))
        if rlt_files:
            for i, f in enumerate(rlt_files):
                logger.info(f"proecess file : {f} ")
                df_from_csv = pd.read_csv(f, header=0)
                df_rlt = EastMoneyDataProcess.proc_stock_analysis(df_from_csv)
                if df_rlt is not None:
                    for idx, row in df_rlt.iterrows():
                        dict_row = row.to_dict()
                        dict_article = dict()
                        if not pd.isna(dict_row.get("article", np.NaN)):
                            dict_article["title"] = dict_row["article"]
                        if not pd.isna(dict_row.get("article_url", np.NaN)):
                            dict_article["full_text_url"] = dict_row["article_url"]
                            dict_article["uuid"] = md5_str(dict_row["article_url"])

                        if not pd.isna(dict_row.get("org_url", np.NaN)):
                            # 暂时先把机构名直接存在 seeking alpha 的 author 数据中，这样画图方便一些
                            author_url: str = dict_row["org_url"]
                            author_id = dict_row["org"]
                            # NO author_name extracted!!
                            # author_name = None
                            # if not pd.isna(dict_row.get("author", np.NaN)):
                            #     author_name = dict_row["author"]
                            author = AuthorInSeekingAlpha(author_id=author_id, url=author_url)
                            if not pd.isna(dict_row.get("reports_within_one_month", np.NaN)):
                                author.articles = dict_row["reports_within_one_month"]

                            dict_article["seeking_alpha_author"] = author
                            if save_doc:
                                upsert_document(author, True)
                        if not pd.isna(dict_row.get("rating", np.NaN)):
                            dict_article["rating"] = dict_row["rating"]
                        if not pd.isna(dict_row.get("rating_chg", np.NaN)):
                            dict_article["rating_change"] = dict_row["rating_chg"]
                        if not pd.isna(dict_row.get("pred_2020_ret", np.NaN)):
                            dict_article["pred_ret_this_yr"] = dict_row["pred_2020_ret"]
                        if not pd.isna(dict_row.get("pred_2020_pe", np.NaN)):
                            dict_article["pred_pe_this_yr"] = dict_row["pred_2020_pe"]
                        if not pd.isna(dict_row.get("pred_2021_pe", np.NaN)):
                            dict_article["pred_pe_next_yr"] = dict_row["pred_2021_pe"]
                        if not pd.isna(dict_row.get("pred_2021_ret", np.NaN)):
                            dict_article["pred_ret_next_yr"] = dict_row["pred_2021_ret"]
                        if dict_row.get("report_date", pd.NaT) is not pd.NaT:
                            dict_article["publish_time"] = dict_row["report_date"].to_pydatetime()

                        symbol = dict_row["symbol"]
                        ls_related_symbols: List[FinancialInstrumentSymbol] = [FinancialInstrumentSymbol(symbol=symbol)]
                        if save_doc:
                            ls_related_symbols[0].full_name = dict_row["symbol_name"]
                            upsert_document(ls_related_symbols[0])
                        dict_article["related_symbols"] = ls_related_symbols
                        dict_article["engine_site"] = "EastMoney"
                        dict_article["channel_in_site"] = "StockAnalysis"
                        dict_article["batch_action_uuid"] = batch_action_uuid

                        article = Article(**dict_article)
                        rlt_articles.append(article)
                        if save_doc:
                            upsert_document(article, True)

        return rlt_articles
