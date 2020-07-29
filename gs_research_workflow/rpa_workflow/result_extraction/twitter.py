# -*- coding: UTF-8 -*-
import glob
import os
from datetime import datetime
from typing import Optional, Tuple, List, Dict

import numpy as np
import pandas as pd
from gs_framework.utilities import md5_str

from gs_research_workflow.nlp.data.docs_in_mongo import Article, UserInTwitter, TweetExtra, SearchingPhrase
from gs_research_workflow.rpa_workflow.result_extraction.utilities import parse_num_from_str, upsert_document
import logging
logger = logging.getLogger(__name__)


class TwitterDataProcess:

    @staticmethod
    def _int_val(x) -> Optional[int]:
        x = parse_num_from_str(x)
        if not pd.isna(x):
            return int(x)
        else:
            return None

    @staticmethod
    def process_follower_following(s_val, extract_following: bool) -> int:
        if not s_val:
            return None
        if extract_following:
            v = parse_num_from_str(s_val.split("|")[0].lower().replace("following", "").strip())
            if v is not None :
                return int(v)
            else:
                return None
        else:
            v = parse_num_from_str(s_val.split("|")[1].lower().replace("followers", "").strip())
            if v is not None:
                return int(v)
            else:
                return None

    @staticmethod
    def proc_posts(df: pd.DataFrame) -> Tuple[str, pd.DataFrame]:
        all_columns = set(["poster_id", "poster_name", "post_time", "post_content", "extract_t", "search_phase"])
        assert set(df.columns.to_list()).issuperset(all_columns), str(all_columns - set(df.columns.to_list()))

        df["poster_id"] = df["poster_id"].apply(lambda x: x.replace("@", "") if not pd.isna(x) else None)
        if "comments" in df.columns:
            df["comments"] = df["comments"].apply(lambda x: TwitterDataProcess._int_val(x))
        if "retweet" in df.columns:
            df["retweet"] = df["retweet"].apply(lambda x: TwitterDataProcess._int_val(x))
        if "like" in df.columns:
            df["like"] = df["like"].apply(lambda x: TwitterDataProcess._int_val(x))

        kw = df.loc[0, "search_phase"]
        df.drop(columns=["search_phase", "extract_t"], inplace=True)
        df = df.drop(df.loc[pd.isna(df["poster_id"])].index)
        return kw, df

    @staticmethod
    def proc_follower_following_info(df: pd.DataFrame, additional_field_name: str) -> Tuple[
        datetime, str, pd.DataFrame]:
        all_columns = set(["poster_id", "follower_following", "extract_t"])
        assert set(df.columns.to_list()).issuperset(all_columns), str(all_columns - set(df.columns.to_list()))

        t = df.loc[0, "extract_t"]
        additional_field = df.loc[0, additional_field_name]

        df.loc[:, "following"] = df["follower_following"].apply(
            lambda x: TwitterDataProcess.process_follower_following(x, True))
        df.loc[:, "follower"] = df["follower_following"].apply(
            lambda x: TwitterDataProcess.process_follower_following(x, False))
        df.drop(columns=["follower_following", "extract_t", additional_field_name], inplace=True)
        df = df.drop(df.loc[pd.isna(df["poster_id"])].index)
        return t, additional_field, df

    @staticmethod
    def proc_following_intro(df: pd.DataFrame) -> Tuple[datetime, pd.DataFrame]:
        all_columns = set(["user_name", "user_id", "intro_txt", "extract_t"])
        assert set(df.columns.to_list()).issuperset(all_columns), str(all_columns - set(df.columns.to_list()))

        t = df.loc[0, "extract_t"]
        df["user_id"] = df["user_id"].apply(lambda x: x.replace("@", "") if not pd.isna(x) else None)
        # NOTE, 抓数据的限制，第一行 user 的 intor_txt 会填入到第二行，而第二行的用户是留空的，这里做调整
        if df.shape[0] >= 2 :
            df.loc[0, "intro_txt"] = df.loc[1, "intro_txt"]
        df.drop(columns=["from_who", "extract_t"], inplace=True)
        df = df.drop(df.loc[pd.isna(df["user_id"])].index)
        return t, df

    @staticmethod
    def kw_search(rlt_path: str, batch_action_uuid: str, action_uuid: str, save_doc: bool = True) -> Tuple[
        List[Article], List[UserInTwitter]]:
        rlt_articles: List[Article] = list()
        rlt_posters: List[UserInTwitter] = list()

        rlt_files = glob.glob(os.path.join(rlt_path, "*_posts.csv"))
        if rlt_files:
            for i, f in enumerate(rlt_files):
                logger.info(f"proecess file : {f} ")
                df_from_csv = pd.read_csv(f, header=0, parse_dates=["post_time", "extract_t"])
                kw, df_rlt = TwitterDataProcess.proc_posts(df_from_csv)
                # print(kw)
                # print(df_rlt)

                for idx, row in df_rlt.iterrows():
                    dict_row = row.to_dict()
                    dict_article = dict()
                    if not pd.isna(dict_row.get("post_content", np.NaN)):
                        dict_article["title"] = dict_row["post_content"]
                    if not pd.isna(dict_row.get("post_content_detail", np.NaN)):
                        dict_article["abstract"] = dict_row["post_content_detail"]
                    if not pd.isna(dict_row.get("post_additional_url", np.NaN)):
                        dict_article["full_text_url"] = dict_row["post_additional_url"]
                    if not pd.isna(dict_row.get("post_image_url", np.NaN)):
                        dict_article["related_image_url"] = dict_row["post_image_url"]
                    if dict_row.get("post_time", pd.NaT) is not pd.NaT:
                        dict_article["publish_time"] = dict_row["post_time"].to_pydatetime()
                    if not pd.isna(dict_row.get("poster_name", np.NaN)):
                        poster = UserInTwitter(user_id=dict_row["poster_id"], name=dict_row["poster_name"])
                    else:
                        poster = UserInTwitter(user_id=dict_row["poster_id"])
                    dict_article["twitter_poster"] = poster
                    # uuid 的计算规则为 posterid + post_time
                    dict_article["uuid"] = md5_str(f"{poster.user_id}|{dict_article['publish_time'].isoformat()}")
                    if not pd.isna(dict_row.get("comments", np.NaN)) or not pd.isna(
                            dict_row.get("retweet", np.NaN)) or not pd.isna(dict_row.get("retweet", np.NaN)):
                        extra_data = TweetExtra()
                        if not pd.isna(dict_row.get("comments", np.NaN)):
                            extra_data.comments = int(dict_row["comments"])
                        if not pd.isna(dict_row.get("retweet", np.NaN)):
                            extra_data.retweet = int(dict_row["retweet"])
                        if not pd.isna(dict_row.get("like", np.NaN)):
                            extra_data.like = int(dict_row["like"])
                        dict_article["tweet_extra"] = extra_data

                    search_phrase_in_db = SearchingPhrase.objects(searching_phrase=kw).first()
                    if search_phrase_in_db is not None:
                        dict_article["from_searching_phase"] = search_phrase_in_db
                        if search_phrase_in_db.related_symbols is not None:
                            dict_article["related_symbols"] = search_phrase_in_db.related_symbols
                    else:
                        dict_article["from_searching_phase"] = SearchingPhrase(searching_phrase=kw)
                    dict_article["engine_site"] = "Twitter"
                    dict_article["batch_action_uuid"] = batch_action_uuid
                    article = Article(**dict_article)
                    rlt_articles.append(article)
                    if save_doc:
                        upsert_document(article, True)

        rlt_files = glob.glob(os.path.join(rlt_path, "*_follower_following.csv"))
        if rlt_files:
            for i, f in enumerate(rlt_files):
                logger.info(f"proecess file : {f} ")
                df_from_csv = pd.read_csv(f, header=0, parse_dates=["extract_t"])
                t, kw, df_rlt = TwitterDataProcess.proc_follower_following_info(df_from_csv, "search_phase")
                # print(kw)
                # print(df_rlt)
                for idx, row in df_rlt.iterrows():
                    dict_row = row.to_dict()
                    twitter_user = UserInTwitter(user_id=dict_row["poster_id"])
                    if not pd.isna(dict_row.get("following", np.NaN)):
                        twitter_user.following = int(dict_row["following"])
                    if not pd.isna(dict_row.get("follower", np.NaN)):
                        twitter_user.follower = int(dict_row["follower"])
                    twitter_user.mtime = t
                    twitter_user.batch_action_uuid = batch_action_uuid
                    rlt_posters.append(twitter_user)
                    if save_doc:
                        upsert_document(twitter_user, True)
        return rlt_articles, rlt_posters

    @staticmethod
    def twitter_user_following(rlt_path: str, batch_action_uuid: str, action_uuid: str, save_doc: bool = True) -> Dict[
        str, UserInTwitter]:

        dict_twitter_user: Dict[str, UserInTwitter] = dict()

        rlt_files = glob.glob(os.path.join(rlt_path, "*_follower_following.csv"))
        if rlt_files:
            for i, f in enumerate(rlt_files):
                logger.info(f"proecess file : {f} ")
                df_from_csv = pd.read_csv(f, header=0, parse_dates=["extract_t"])
                t, from_who, df_rlt = TwitterDataProcess.proc_follower_following_info(df_from_csv, "from_who")
                key_twitter_user = UserInTwitter(user_id=from_who)
                key_twitter_user.arr_following = list()
                key_twitter_user.batch_action_uuid = batch_action_uuid

                dict_twitter_user[from_who] = key_twitter_user

                # print(df_rlt)
                for idx, row in df_rlt.iterrows():
                    dict_row = row.to_dict()
                    following_user = UserInTwitter(user_id=dict_row["poster_id"])
                    if not pd.isna(dict_row.get("following", np.NaN)):
                        following_user.following = int(dict_row["following"])
                    if not pd.isna(dict_row.get("follower", np.NaN)):
                        following_user.follower = int(dict_row["follower"])
                    following_user.mtime = t
                    following_user.batch_action_uuid = batch_action_uuid
                    if save_doc:
                        upsert_document(following_user, True)
                    key_twitter_user.arr_following.append(following_user)
                if save_doc:
                    upsert_document(key_twitter_user, True)

        rlt_files = glob.glob(os.path.join(rlt_path, "*_following_intro.csv"))
        if rlt_files:
            for i, f in enumerate(rlt_files):
                logger.info(f"proecess file : {f} ")
                df_from_csv = pd.read_csv(f, header=0, parse_dates=["extract_t"])
                t, df_rlt = TwitterDataProcess.proc_following_intro(df_from_csv)
                # print(df_rlt)
                for idx, row in df_rlt.iterrows():
                    dict_row = row.to_dict()
                    following_user = UserInTwitter(user_id=dict_row["user_id"])
                    if not pd.isna(dict_row.get("user_name", np.NaN)):
                        following_user.name = dict_row["user_name"].strip()
                    if not pd.isna(dict_row.get("intro_txt", np.NaN)):
                        following_user.intro = dict_row["intro_txt"].strip()
                    following_user.mtime = t
                    following_user.batch_action_uuid = batch_action_uuid
                    if save_doc:
                        upsert_document(following_user)

        return dict_twitter_user
