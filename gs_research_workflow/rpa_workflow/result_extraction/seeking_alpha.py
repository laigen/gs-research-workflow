# -*- coding: UTF-8 -*-
import glob
import logging
import os
from datetime import datetime, timedelta
from typing import Union, Optional, Tuple, List, Dict

import numpy as np
import pandas as pd
from furl import furl
from gs_framework.utilities import md5_str
from pandas._libs.tslibs.timestamps import Timestamp

from gs_research_workflow.nlp.data.docs_in_mongo import Article, AuthorInSeekingAlpha, FinancialInstrumentSymbol, \
    SeekingAlphaArticleExtra, SymbolInfoBySeekingAlpha, SearchingPhrase
from gs_research_workflow.rpa_workflow.result_extraction.utilities import append_site_to_url, upsert_document, \
    parse_num_from_str

logger = logging.getLogger(__name__)


class SeekingAlphaDataProcess:
    """ 提供 Seeking Alpha 上爬取的数据内容的预处理 """

    site = "https://seekingalpha.com"

    @staticmethod
    def parse_display_dt_str(s: str, extract_t: Union[datetime, Timestamp], log_error: bool = False) -> Optional[
        datetime]:
        """
        s 有几种典型的值 ：
            Today, 7:06 AM
            Yesterday, 7:02 AM
            Mon, May 4, 11:30 AM
            Mon, Apr. 4, 11:30 AM
            Dec. 22, 2019, 6:18 AM
            Mon, May 4
        """
        if pd.isna(s):
            return s
        # https://docs.python.org/3.6/library/datetime.html#strftime-and-strptime-behavior
        if s.startswith("Today"):  # Today, 7:06 AM => Nov. 28, 2019, 7:06 AM
            str_t = s.replace("Today", extract_t.strftime("%b. %d, %Y"))
            if s.endswith("AM") or s.endswith("PM"):
                t_fmt = "%b. %d, %Y,  %I:%M %p"
            else:
                t_fmt = "%b. %d, %Y"
        elif s.startswith("Yesterday"):  # Yesterday, 7:02 AM => Nov. 28, 2019, 7:06 AM
            str_t = s.replace("Yesterday", (extract_t + timedelta(days=-1)).strftime("%b. %d, %Y"))
            if s.endswith("AM") or s.endswith("PM"):
                t_fmt = "%b. %d, %Y,  %I:%M %p"
            else:
                t_fmt = "%b. %d, %Y"
        elif len(s) > 4 and s[0:4] in {"Sun,", "Mon,", "Tue,", "Wed,", "Thu,", "Fri,", "Sat,"}:
            # Mon, May 4, 11:30 AM => 2019 Mon, May 4, 11:30 AM
            # Thu, Apr. 30, 8:53 AM => 2019 Thu, Apr 30, 8:53 AM ，注意 上一个月会多一个点
            # 这个分支是当年度显示的字符
            str_t = extract_t.strftime("%Y") + " " + s
            str_t = str_t.replace(".", "")  # "Tue, Apr. 28" 和 "Sun, May 3" 会根据是否当月，'.'会时而不出现
            if s.endswith("AM") or s.endswith("PM"):
                t_fmt = "%Y %a, %b %d, %I:%M %p"
            else:
                t_fmt = "%Y %a, %b %d"
        elif len(s) > 4 and s[0:4] in {"Jan.", "Feb.", "Mar.", "Apr.", "May.", "Jun.", "Jul.", "Aug.", "Sep.", "Oct.",
                                       "Nov.", "Dec."}:
            # Dec. 22, 2019, 6:18 AM
            # 这个分支是上一年度的显示字符
            str_t = s
            if s.endswith("AM") or s.endswith("PM"):
                t_fmt = "%b. %d, %Y,  %I:%M %p"
            else:
                t_fmt = "%b. %d, %Y"
        else:
            # 用 Pandas 默认的进行尝试
            try:
                return pd.to_datetime(s)
            except Exception as ex:
                if log_error:
                    logger.error(ex)
                return None
        try:
            return datetime.strptime(str_t, t_fmt)
        except ValueError as ex:
            if log_error:
                logger.error(ex)
            return None

    # region column articles 各专栏

    @staticmethod
    def proc_article_data(df: pd.DataFrame) -> Tuple[str, pd.DataFrame]:
        """
        csv 文件的后缀为 *.articles.csv
        数据列清洗的逻辑：
            "title" : 保留
            "article_url" : 如果不是以 'http' 开头，则添加前缀 'https://seekingalpha.com/'
            "pub_time" : 从 "pub_time_normal" +  "pub_time_has_editor_pick" 两列中判定
                        editor_pick 字段非空，取  pub_time_has_editor_pick 否则取 pub_time_normal （需判定该字段出现 symbol 的情况）
                        是否为一个日期值，是 则进行 str2cdate 的转换
            "author_url" : 如果不是以 'http' 开头，则添加前缀 'https://seekingalpha.com/'
            "comments" : 提取数值部分
            "related_symbol1" / "related_symbol1_fullname"
            "related_symbol2" / "related_symbol2_fullname"
            "related_symbol3" / "related_symbol3_fullname" 清理有保留有效的内容
        """
        all_columns = set(['title', 'article_url', 'pub_time_normal', 'author_url', 'comments',
                           # symbol 1~3 允许提取过程中不出现
                           # 'related_symbol1', 'related_symbol1_fullname',
                           # 'related_symbol2', 'related_symbol2_fullname',
                           # 'related_symbol3', 'related_symbol3_fullname',
                           'pub_time_has_editor_pick', 'editor_pick', 'channel',
                           'extract_t'])
        assert set(df.columns.to_list()).issuperset(all_columns), str(all_columns-set(df.columns.to_list()))
        df["article_url"] = df["article_url"].apply(lambda x: append_site_to_url(x, SeekingAlphaDataProcess.site))
        df["author_url"] = df["author_url"].apply(lambda x: append_site_to_url(x, SeekingAlphaDataProcess.site))

        def _pubtime(row) -> Optional[datetime]:
            dt_extract_t = row["extract_t"]
            if not pd.isna(row["editor_pick"]):
                return SeekingAlphaDataProcess.parse_display_dt_str(row["pub_time_has_editor_pick"],
                                                                    dt_extract_t)
            else:
                return SeekingAlphaDataProcess.parse_display_dt_str(row["pub_time_normal"], dt_extract_t)

        df["publish_time"] = df.apply(lambda row: _pubtime(row), axis=1)
        df.drop(columns=["pub_time_normal", "pub_time_has_editor_pick", "editor_pick", "extract_t"], inplace=True)

        def _comments(cell) -> Optional[int]:
            if pd.isna(cell):
                return cell
            if not isinstance(cell, str):
                return cell
            s = cell.lower().replace("comments", "").replace("comment", "").strip()
            return int(s)

        df["comments"] = df["comments"].apply(lambda x: _comments(x))
        df["comments"] = df["comments"].astype("Int64")

        channel = df.loc[0, "channel"]
        df.drop(columns=["channel"], inplace=True)
        return channel, df

    @staticmethod
    def column_articles(rlt_path: str, batch_action_uuid: str, action_uuid: str, save_doc: bool = True) -> List[Article]:
        rlt_articles = list()

        # region articles
        rlt_files = glob.glob(os.path.join(rlt_path, "*_articles.csv"))
        if rlt_files:
            for f in rlt_files:
                logger.info(f"proecess file : {f} ")
                df_from_csv = pd.read_csv(f, header=0, parse_dates=["extract_t"])
                kw, df_rlt = SeekingAlphaDataProcess.proc_article_data(df_from_csv)
                for idx, row in df_rlt.iterrows():
                    dict_row = row.to_dict()
                    dict_article = dict()  # for Article
                    if not pd.isna(dict_row.get("title", np.NaN)):
                        dict_article["title"] = dict_row["title"]
                    if not pd.isna(dict_row.get("author_url", np.NaN)):
                        author_url: str = dict_row["author_url"]
                        author_id = author_url.split("/")[-1]
                        dict_article["seeking_alpha_author"] = AuthorInSeekingAlpha(author_id=author_id, url=author_url)
                    if not pd.isna(dict_row.get("article_url", np.NaN)):
                        article_url = furl(dict_row["article_url"])
                        abs_url_str = f"{article_url.origin}{article_url.path}"
                        dict_article["full_text_url"] = abs_url_str
                        dict_article["uuid"] = md5_str(abs_url_str)
                    if dict_row.get("publish_time", pd.NaT) is not pd.NaT:
                        dict_article["publish_time"] = dict_row["publish_time"].to_pydatetime()
                    dict_article["engine_site"] = "SeekingAlpha"
                    ls_related_symbols: List[FinancialInstrumentSymbol] = list()
                    for symbol_key_pair in [("related_symbol1", "related_symbol1_fullname"),
                                            ("related_symbol2", "related_symbol2_fullname"),
                                            ("related_symbol3", "related_symbol3_fullname")]:
                        if not pd.isna(dict_row.get(symbol_key_pair[0], np.NaN)) and not pd.isna(dict_row.get(symbol_key_pair[1], np.NaN)):
                            fin_instrument_symbol = FinancialInstrumentSymbol(symbol=dict_row[symbol_key_pair[0]],
                                                                              full_name=dict_row[symbol_key_pair[1]],
                                                                              batch_action_uuid=batch_action_uuid)
                            ls_related_symbols.append(fin_instrument_symbol)
                            # ListField(ReferenceField(FinancialInstrumentSymbol)) 似乎不会级联保存，这里创建的时候同时保存
                            if save_doc:
                                upsert_document(fin_instrument_symbol, True)
                    if ls_related_symbols:
                        dict_article["related_symbols"] = ls_related_symbols

                    if not pd.isna(dict_row.get("comments", np.NaN)):
                        dict_article["seeking_alpha_extra"] = SeekingAlphaArticleExtra(comments=dict_row["comments"])

                    dict_article["channel_in_site"] = kw
                    dict_article["batch_action_uuid"] = batch_action_uuid
                    article = Article(**dict_article)
                    rlt_articles.append(article)
                    if save_doc:
                        upsert_document(article, True)
        # endregion

        return rlt_articles

    # endregion

    # region author and author articles

    @staticmethod
    def proc_author_articles(df: pd.DataFrame) -> Tuple[str, pd.DataFrame]:
        all_columns = set(
            ["title", "news_url", "ext_info1", "ext_info2", "extract_t", "author"])
        if not set(df.columns.to_list()).issuperset(all_columns):
            logger.error(f"Only has columns {df.columns.to_list()} , return None")
            return None, None
        df["news_url"] = df["news_url"].apply(lambda x: append_site_to_url(x, SeekingAlphaDataProcess.site))

        def _pubtime(row) -> Optional[datetime]:
            dt_extract_t = row["extract_t"]
            for col in ["ext_info1", "ext_info2", "ext_info3", "ext_info4"]:
                if col not in row:
                    continue
                if pd.isna(row[col]):
                    continue
                dt = SeekingAlphaDataProcess.parse_display_dt_str(row[col], dt_extract_t)
                if isinstance(dt, datetime):
                    return dt
            return None

        df["publish_time"] = df.apply(lambda row: _pubtime(row), axis=1)

        def _comments(row) -> Optional[int]:
            for col in ["ext_info1", "ext_info2", "ext_info3", "ext_info4"]:
                if col not in row:
                    continue
                if pd.isna(row[col]):
                    continue
                if not isinstance(row[col], str):
                    continue
                if row[col].lower().find("comment") >= 0 :
                    s = row[col].lower().replace("comments", "").replace("comment", "").strip()
                    return int(s)
            return None

        df["comments"] = df.apply(lambda row: _comments(row), axis=1)
        df["comments"] = df["comments"].astype("Int64")

        def _symbols(row) -> Optional[str]:
            dt_extract_t = row["extract_t"]
            for col in ["ext_info1", "ext_info2", "ext_info3", "ext_info4"]:
                if not col in row:
                    continue
                if pd.isna(row[col]):
                    continue
                if not isinstance(row[col], str):
                    continue
                if row[col].lower().find("comment") >= 0:
                    continue
                dt = SeekingAlphaDataProcess.parse_display_dt_str(row[col], dt_extract_t)
                if isinstance(dt, datetime):
                    continue
                s = str(row[col])
                if s:
                    return s.strip()
            return None

        df["symbols"] = df.apply(lambda row: _symbols(row), axis=1)

        author = df.loc[0, "author"]
        for col in ["ext_info1", "ext_info2", "ext_info3", "ext_info4"] :
            if col in df.columns :
                df.drop(columns=[col], inplace=True)
        df.drop(columns=["author", "extract_t"], inplace=True)
        return author, df

    @staticmethod
    def proc_author_info(df: pd.DataFrame) -> Optional[Dict]:
        all_columns = set(['field_name', 'field_value'])
        assert set(df.columns.to_list()).issuperset(all_columns)

        rlt_dict = dict()
        for idx, row in df.iterrows():
            k = str(row["field_name"])
            v = str(row["field_value"])
            if not v:
                continue
            if k in {"articles", "authors_picks", "comments", "stocktalks", "instablogs" , "likes", "followers", "following"}:
                f_v = parse_num_from_str(v)
                if f_v is not None:
                    rlt_dict[k] = int(f_v)
            elif k in {'author', 'author_intro'}:
                rlt_dict[k] = v
        return rlt_dict

    @staticmethod
    def author_detail(rlt_path: str, batch_action_uuid: str, action_uuid: str, save_doc: bool = True) -> Tuple[
        List[AuthorInSeekingAlpha], List[Article]]:
        rlt_articles: List[Article] = list()
        rlt_authors: List[AuthorInSeekingAlpha] = list()

        # region author articles
        rlt_files = glob.glob(os.path.join(rlt_path, "*_author_articles.csv"))
        if rlt_files:
            for i, f in enumerate(rlt_files):
                logger.info(f"proecess file : {f} ")
                df_from_csv = pd.read_csv(f, header=0, parse_dates=["extract_t"])
                author_id, df_rlt = SeekingAlphaDataProcess.proc_author_articles(df_from_csv)
                if df_rlt is not None :
                    for idx, row in df_rlt.iterrows():
                        dict_row = row.to_dict()
                        dict_article = dict()
                        if not pd.isna(dict_row.get("title", np.NaN)):
                            dict_article["title"] = dict_row["title"]
                        if not pd.isna(dict_row.get("news_url", np.NaN)):
                            article_url = furl(dict_row["news_url"])
                            abs_url_str = f"{article_url.origin}{article_url.path}"
                            dict_article["full_text_url"] = abs_url_str
                            dict_article["uuid"] = md5_str(abs_url_str)
                        if dict_row.get("publish_time", pd.NaT) is not pd.NaT:
                            dict_article["publish_time"] = dict_row["publish_time"].to_pydatetime()
                        if not pd.isna(dict_row.get("comments", np.NaN)):
                            dict_article["seeking_alpha_extra"] = SeekingAlphaArticleExtra(comments=dict_row["comments"])
                        if not pd.isna(dict_row.get("symbols", np.NaN)):
                            ls_related_symbols: List[FinancialInstrumentSymbol] = [
                                FinancialInstrumentSymbol(symbol=s.strip()) for s in dict_row["symbols"].split(",")]
                            if ls_related_symbols:
                                for symbol in ls_related_symbols:
                                    if save_doc:
                                        upsert_document(symbol, True)
                                dict_article["related_symbols"] = ls_related_symbols
                        dict_article["engine_site"] = "SeekingAlpha"
                        dict_article["batch_action_uuid"] = batch_action_uuid
                        article = Article(**dict_article)
                        rlt_articles.append(article)
                        if save_doc:
                            upsert_document(article, True)

        # endregion

        # region author info
        rlt_files = glob.glob(os.path.join(rlt_path, "*_author_info.csv"))
        if rlt_files:
            for f in rlt_files:
                logger.info(f"proecess file : {f} ")
                df_from_csv = pd.read_csv(f, header=0)
                dict_author_info = SeekingAlphaDataProcess.proc_author_info(df_from_csv)
                if not dict_author_info:
                    continue
                if "author" not in dict_author_info:
                    continue
                author = AuthorInSeekingAlpha(author_id=dict_author_info.get("author"),
                                              intro=dict_author_info.get("author_intro", ""),
                                              articles=dict_author_info.get("articles", None),
                                              picks=dict_author_info.get("authors_picks", None),
                                              blog_posts=dict_author_info.get("instablogs", None),
                                              comments=dict_author_info.get("comments", None),
                                              stock_talks=dict_author_info.get("stocktalks", None),
                                              likes=dict_author_info.get("likes", None),
                                              followers=dict_author_info.get("followers", None),
                                              following=dict_author_info.get("following", None),
                                              mtime=datetime.now(),
                                              batch_action_uuid=batch_action_uuid
                                              )
                if save_doc:
                    upsert_document(author, True)
                rlt_authors.append(author)
        # endregion

        return rlt_authors, rlt_articles

    # endregion

    # region symbol data

    @staticmethod
    def proc_symbol_analysis(df: pd.DataFrame) -> Tuple[str, pd.DataFrame]:
        all_columns = set(
            ["title", "article_url", "author_url", "publish_time", "extract_t", "symbol"])
        if not set(df.columns.to_list()).issuperset(all_columns) :
            return None , None

        df["article_url"] = df["article_url"].apply(lambda x: append_site_to_url(x, SeekingAlphaDataProcess.site))

        def _author_id(author_url: str):
            if not isinstance(author_url, str):
                return None
            if author_url.startswith("/author"):
                return author_url.split("/")[-1]
            elif author_url.startswith("/user"):
                return author_url.split("/")[-2]
            else:
                return None

        df["author_id"] = df["author_url"].apply(lambda x: _author_id(x))

        # 注意，必须先计算 author_id ， 然后再补充 site-info
        df["author_url"] = df["author_url"].apply(lambda x: append_site_to_url(x, SeekingAlphaDataProcess.site))

        def _pubtime(row) -> Optional[datetime]:
            dt_extract_t = row["extract_t"]
            for col in ["publish_time", "publish_time_no_sentiments"]:
                if col not in row:
                    continue
                if pd.isna(row[col]):
                    continue
                dt = SeekingAlphaDataProcess.parse_display_dt_str(row[col], dt_extract_t)
                if isinstance(dt, datetime):
                    return dt
            return None

        df["_publish_time"] = df.apply(lambda row: _pubtime(row), axis=1)

        def _comments(row) -> Optional[int]:
            for col in ["comments", "comments_no_sentiments"]:
                if not col in row:
                    continue
                if pd.isna(row[col]):
                    continue
                if not isinstance(row[col], str):
                    continue
                if row[col].lower().find("comment") >= 0:
                    s = row[col].lower().replace("comments", "").replace("comment", "").strip()
                    return int(s)
            return None

        df["_comments"] = df.apply(lambda row: _comments(row), axis=1)
        df["_comments"] = df["_comments"].astype("Int64")

        def _rating(s) -> Optional[int]:
            if not isinstance(s, str):
                return None
            s = s.lower()
            if s == "very bullish":
                return 2
            elif s == "bullish":
                return 1
            elif s == "neutral":
                return 0
            elif s == "bearish":
                return -1
            elif s == "very bearish":
                return -2
            else:
                return None

        if "rating" in df.columns :
            df["rating"] = df["rating"].apply(lambda x:_rating(x))
            df["rating"] = df["rating"].astype("Int64")

        symbol = df.loc[0, "symbol"]
        for col in ["publish_time", "comments", "symbol", "extract_t"]:
            if col in df.columns:
                df.drop(columns=[col], inplace=True)
        if "publish_time_no_sentiments" in df.columns:
            df.drop(columns=["publish_time_no_sentiments"], inplace=True)
        if "comments_no_sentiments" in df.columns:
            df.drop(columns=["comments_no_sentiments"], inplace=True)

        df.rename({"_publish_time": "publish_time", "_comments": "comment"}, axis=1, inplace=True)
        return symbol, df

    @staticmethod
    def proc_symbol_news(df: pd.DataFrame) -> Tuple[str, pd.DataFrame]:
        all_columns = set(["title", "news_url", "news_source_pub_t_comments", "extract_t", "symbol"])

        assert set(df.columns.to_list()).issuperset(all_columns)

        df["news_url"] = df["news_url"].apply(lambda x: append_site_to_url(x, SeekingAlphaDataProcess.site))

        def _pubtime(row) -> Optional[datetime]:
            dt_extract_t = row["extract_t"]
            if pd.isna(row["news_source_pub_t_comments"]):
                return None
            v = str(row["news_source_pub_t_comments"])
            ls_v = v.split("•")
            if len(ls_v) >= 2:
                dt = SeekingAlphaDataProcess.parse_display_dt_str(ls_v[1], dt_extract_t)
                if isinstance(dt, datetime):
                    return dt
            return None

        df["publish_time"] = df.apply(lambda row: _pubtime(row), axis=1)

        def _comments(row) -> Optional[int]:
            if pd.isna(row["news_source_pub_t_comments"]):
                return None
            v = str(row["news_source_pub_t_comments"])
            ls_v = v.split("•")
            if len(ls_v) >= 3 and ls_v[2].lower().find("comment") >= 0:
                s = ls_v[2].lower().replace("comments", "").replace("comment", "").strip()
                return int(s)
            return None
        df["comments"] = df.apply(lambda row: _comments(row), axis=1)
        df["comments"] = df["comments"].astype("Int64")

        def _orig_source(row) -> Optional[str]:
            if pd.isna(row["news_source_pub_t_comments"]):
                return None
            v = str(row["news_source_pub_t_comments"])
            ls_v = v.split("•")
            if len(ls_v) == 1:
                v = ls_v[0].replace("at ","")
                t_pos = v.find("(")
                if t_pos > 0 :
                    return v[0:t_pos].strip()
                else:
                    return v
            elif len(ls_v) >= 2:
                return ls_v[0]
            return None

        df["orig_source"] = df.apply(lambda row: _orig_source(row), axis=1)
        symbol = df.loc[0, "symbol"]
        df.drop(columns=["news_source_pub_t_comments", "symbol", "extract_t"], inplace=True)
        return symbol, df

    @staticmethod
    def proc_symbol_indicator(df: pd.DataFrame) -> Optional[Dict]:
        all_columns = set(['field_name', 'field_val'])
        assert set(df.columns.to_list()).issuperset(all_columns)

        rlt_dict = dict()
        for idx, row in df.iterrows():
            k = str(row["field_name"]).replace(":", "")
            v = str(row["field_val"])
            if not v:
                continue
            if k in {"52wk high", "52wk low", "EPS (FWD)", "PE (FWD)", "Div Rate (FWD)", "Yield (FWD)", "Market Cap",
                     "Volume", "followers"}:
                v = v.replace("$", "").replace("%", "")
                f_v = parse_num_from_str(v)
                if f_v is not None and not pd.isna(f_v):
                    if k == "followers":
                        rlt_dict[k] = int(f_v)
                    elif k == "Yield (FWD)":
                        rlt_dict[k] = f_v/100.
                    else:
                        rlt_dict[k] = f_v
            elif k in {'symbol'}:
                rlt_dict[k] = v
        return rlt_dict

    @staticmethod
    def symbol_summary(rlt_path: str, batch_action_uuid: str, action_uuid: str, save_doc: bool = True) -> Tuple[
        List[FinancialInstrumentSymbol], List[Article]]:
        rlt_articles: List[Article] = list()
        rlt_symbols: List[FinancialInstrumentSymbol] = list()

        # region symbol analysis
        rlt_files = glob.glob(os.path.join(rlt_path, "*_symbol_analysis.csv"))
        if rlt_files:
            for i, f in enumerate(rlt_files):
                logger.info(f"proecess file : {f} ")
                df_from_csv = pd.read_csv(f, header=0, parse_dates=["extract_t"])
                symbol, df_rlt = SeekingAlphaDataProcess.proc_symbol_analysis(df_from_csv)
                if df_rlt is not None:
                    for idx, row in df_rlt.iterrows():
                        dict_row = row.to_dict()
                        dict_article = dict()
                        if not pd.isna(dict_row.get("title", np.NaN)):
                            dict_article["title"] = dict_row["title"]
                        if not pd.isna(dict_row.get("article_url", np.NaN)):
                            article_url = furl(dict_row["article_url"])
                            abs_url_str = f"{article_url.origin}{article_url.path}"
                            dict_article["full_text_url"] = abs_url_str
                            dict_article["uuid"] = md5_str(abs_url_str)
                        if not pd.isna(dict_row.get("author_url", np.NaN)):
                            author_url: str = dict_row["author_url"]
                            author_id = dict_row["author_id"]
                            # NO author_name extracted!!
                            # author_name = None
                            # if not pd.isna(dict_row.get("author", np.NaN)):
                            #     author_name = dict_row["author"]
                            author = AuthorInSeekingAlpha(author_id=author_id, url=author_url)
                            dict_article["seeking_alpha_author"] = author
                            if save_doc:
                                upsert_document(author, True)
                        if not pd.isna(dict_row.get("rating", np.NaN)):
                            dict_article["rating"] = dict_row["rating"]

                        if dict_row.get("publish_time", pd.NaT) is not pd.NaT:
                            dict_article["publish_time"] = dict_row["publish_time"].to_pydatetime()
                        if not pd.isna(dict_row.get("comments", np.NaN)):
                            dict_article["seeking_alpha_extra"] = SeekingAlphaArticleExtra(comments=dict_row["comments"])
                        ls_related_symbols: List[FinancialInstrumentSymbol] = [FinancialInstrumentSymbol(symbol=symbol)]
                        if save_doc:
                            upsert_document(ls_related_symbols[0])
                        dict_article["related_symbols"] = ls_related_symbols
                        dict_article["engine_site"] = "SeekingAlpha"
                        dict_article["channel_in_site"] = "analysis"
                        dict_article["batch_action_uuid"] = batch_action_uuid

                        article = Article(**dict_article)
                        rlt_articles.append(article)
                        if save_doc:
                            upsert_document(article, True)

        # endregion

        # region symbol news

        rlt_files = glob.glob(os.path.join(rlt_path, "*_symbol_news.csv"))
        for i, f in enumerate(rlt_files):
            logger.info(f"proecess file : {f} ")
            df_from_csv = pd.read_csv(f, header=0, parse_dates=["extract_t"])
            symbol, df_rlt = SeekingAlphaDataProcess.proc_symbol_news(df_from_csv)

            for idx, row in df_rlt.iterrows():
                dict_row = row.to_dict()
                dict_article = dict()
                if not pd.isna(dict_row.get("title", np.NaN)):
                    dict_article["title"] = dict_row["title"]
                if not pd.isna(dict_row.get("news_url", np.NaN)):
                    article_url = furl(dict_row["news_url"])
                    abs_url_str = f"{article_url.origin}{article_url.path}"
                    # 仅 seeking alpha 内部的链接考虑去掉参数项，其他站点的行文，不确定url参数是否也构成了 unique 的情况
                    if abs_url_str.find("seekingalpha") > 0:
                        dict_article["full_text_url"] = abs_url_str
                        dict_article["uuid"] = md5_str(abs_url_str)
                    else:
                        dict_article["full_text_url"] = article_url.url
                        dict_article["uuid"] = md5_str(article_url.url)

                if dict_row.get("publish_time", pd.NaT) is not pd.NaT:
                    dict_article["publish_time"] = dict_row["publish_time"].to_pydatetime()
                if not pd.isna(dict_row.get("comments", np.NaN)):
                    dict_article["seeking_alpha_extra"] = SeekingAlphaArticleExtra(comments=dict_row["comments"])
                ls_related_symbols: List[FinancialInstrumentSymbol] = [FinancialInstrumentSymbol(symbol=symbol)]
                if save_doc:
                    upsert_document(ls_related_symbols[0])
                dict_article["related_symbols"] = ls_related_symbols
                dict_article["engine_site"] = "SeekingAlpha"
                dict_article["batch_action_uuid"] = batch_action_uuid
                if not pd.isna(dict_row.get("orig_source", np.NaN)):
                    dict_article["channel_in_site"] = dict_row["orig_source"]

                article = Article(**dict_article)
                rlt_articles.append(article)
                if save_doc:
                    upsert_document(article, True)

        # endregion

        # region symbol info
        rlt_files = glob.glob(os.path.join(rlt_path, "*_symbol_indicators.csv"))
        if rlt_files:
            for f in rlt_files:
                logger.info(f"proecess file : {f} ")
                df_from_csv = pd.read_csv(f, header=0)
                dict_symbol_info = SeekingAlphaDataProcess.proc_symbol_indicator(df_from_csv)
                if not dict_symbol_info:
                    continue
                if "symbol" not in dict_symbol_info:
                    continue
                symbol = FinancialInstrumentSymbol(symbol=dict_symbol_info.get("symbol"),
                                                   info_from_seeking_alpha=SymbolInfoBySeekingAlpha(
                                                       followers=dict_symbol_info.get("followers", None),
                                                       high_52wk=dict_symbol_info.get("52wk high", None),
                                                       low_52wk=dict_symbol_info.get("52wk low", None),
                                                       eps_fwd=dict_symbol_info.get("EPS (FWD)", None),
                                                       pe_fwd=dict_symbol_info.get("PE (FWD)", None),
                                                       yield_fwd=dict_symbol_info.get("Yield (FWD)", None),
                                                       div_rate_fwd=dict_symbol_info.get("Div Rate (FWD)", None),
                                                       mkt_cap=dict_symbol_info.get("Market Cap", None),
                                                       volume=dict_symbol_info.get("Volume", None),
                                                       mtime=datetime.now()
                                                    )
                                                   )
                if save_doc:
                    upsert_document(symbol, True)
                rlt_symbols.append(symbol)
        # endregion

        return rlt_symbols, rlt_articles
    # endregion

    # region kw search

    @staticmethod
    def proc_kw_search(df: pd.DataFrame) -> Tuple[str, pd.DataFrame]:
        all_columns = set(
            ["title", "news_url", "summary", "meta1", "extract_t", "keywords"]
        )
        # "meta2", "meta3",
        # meta1	maybe_article_t	meta_item_ticker	meta_item_ticker_url	meta2	meta3
        assert set(df.columns.to_list()).issuperset(all_columns)
        df["title"] = df["title"].apply(lambda x: x.replace("\n", "").strip())
        df["news_url"] = df["news_url"].apply(lambda x: append_site_to_url(x, SeekingAlphaDataProcess.site))

        def _pubtime(row) -> Optional[datetime]:
            dt_extract_t = row["extract_t"]
            for col in ["meta3", "meta2", "meta1"]:
                if col not in row:
                    continue
                if pd.isna(row[col]):
                    continue
                dt = SeekingAlphaDataProcess.parse_display_dt_str(row[col], dt_extract_t)
                if isinstance(dt, datetime):
                    return dt
            return None

        df["publish_time"] = df.apply(lambda row: _pubtime(row), axis=1)

        def _symbols(row) -> Optional[str]:
            # 反过来遍历，先找到 publish_t , 前一个非空字段即为 symbols
            dt_extract_t = row["extract_t"]
            b_found_pub_t = False
            for col in ["meta3", "meta2", "meta1"]:
                if col not in row:
                    continue
                if pd.isna(row[col]):
                    continue
                dt = SeekingAlphaDataProcess.parse_display_dt_str(row[col], dt_extract_t)
                if isinstance(dt, datetime):
                    b_found_pub_t = True
                    continue
                if b_found_pub_t:
                    return row[col].replace("...", "")
            return None

        df["symbols"] = df.apply(lambda row: _symbols(row), axis=1)

        kw = df.loc[0, "keywords"]
        cols_to_del = []
        for col_name in ["meta1", "maybe_article_t", "meta_item_ticker", "meta_item_ticker_url", "meta2", "meta3",
                         "extract_t", "keywords"]:
            if col_name in df.columns:
                cols_to_del.append(col_name)
        df.drop(columns=cols_to_del, inplace=True)

        return kw, df

    @staticmethod
    def kw_search(rlt_path: str, batch_action_uuid: str, action_uuid: str, save_doc: bool = True) -> List[Article]:
        rlt_articles: List[Article] = list()

        rlt_files = glob.glob(os.path.join(rlt_path, "*_kw_search_result.csv"))
        if rlt_files:
            for i, f in enumerate(rlt_files):
                logger.info(f"proecess file : {f} ")
                df_from_csv = pd.read_csv(f, header=0, parse_dates=["extract_t"])
                kw, df_rlt = SeekingAlphaDataProcess.proc_kw_search(df_from_csv)
                # print(df_rlt)
                for idx, row in df_rlt.iterrows():
                    dict_row = row.to_dict()
                    dict_article = dict()
                    if not pd.isna(dict_row.get("title", np.NaN)):
                        dict_article["title"] = dict_row["title"]
                    if not pd.isna(dict_row.get("news_url", np.NaN)):
                        article_url = furl(dict_row["news_url"])
                        abs_url_str = f"{article_url.origin}{article_url.path}"
                        # 仅 seeking alpha 内部的链接考虑去掉参数项，其他站点的行文，不确定url参数是否也构成了 unique 的情况
                        if abs_url_str.find("seekingalpha") > 0:
                            dict_article["full_text_url"] = abs_url_str
                            dict_article["uuid"] = md5_str(abs_url_str)
                        else:
                            dict_article["full_text_url"] = article_url.url
                            dict_article["uuid"] = md5_str(article_url.url)
                    if dict_row.get("publish_time", pd.NaT) is not pd.NaT:
                        dict_article["publish_time"] = dict_row["publish_time"].to_pydatetime()
                    if not pd.isna(dict_row.get("symbols", np.NaN)):
                        symbols = [x.strip() for x in dict_row.get("symbols").split(",")]
                        ls_related_symbols: List[FinancialInstrumentSymbol] = [FinancialInstrumentSymbol(symbol=x) for x in symbols]
                        if save_doc:
                            map(upsert_document, ls_related_symbols)
                        dict_article["related_symbols"] = ls_related_symbols
                    dict_article["from_searching_phase"] = SearchingPhrase(searching_phrase=kw)
                    dict_article["engine_site"] = "SeekingAlpha"
                    dict_article["channel_in_site"] = "Search"
                    dict_article["batch_action_uuid"] = batch_action_uuid
                    article = Article(**dict_article)
                    rlt_articles.append(article)
                    if save_doc:
                        upsert_document(article, True)

        return rlt_articles

    # endregion
