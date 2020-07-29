# -*- coding: UTF-8 -*-

"""
通用的 browser 结果的保存

CSV 数据保存需要补充的信息：
    1) base uri
    2) column 与 Article Document 之间的映射关系
    3) dateparser 的预处理函数


output folder 中的内容：
    1) *_webpage_content.pdf , 页面内容pdf版本截屏，含整个网页的内容
                    如果网页无内容，则不提供 pdf version 的 screenshot
    2) *_browser_screenshot.png , screenshot 文件，单页
                    如果网页被判断无内容，该 screenshot 文件依然会提供，用于 debug
    3) *_articles.csv , 提取到的网页内容
    4) *_extract_info.js , 提取数据用到的一些 js 内容

articles 中一些 Column 命名规范：
    1) "title" => Article.title ， 一般不做特殊处理，有则填入
    2) "abstract" => Article.abstract , 摘要，一般不做特殊处理
    3) "channel_in_site" => Article.channel_in_site , 二级分类，站点内的
    4) "full_text_url" => Article.full_text_url ， 正文的链接
    5) "publish_time" => Article.publish_time , 可能需要有数据预处理

extract_info.js 中含有的 Key :
    1) cfg_name : str
    2) url : str , 程序定位产生的 url
    3) real_url : str , 实际上最终的 url
    4) publish_time_preprocess : str 解析时间的预处理函数
    5) article_site : str 标记 article 来自于哪个 site


# NOTE : 使用 dateparser 这个 package 来解决 human readable time string to realtime
see : https://github.com/scrapinghub/dateparser

# NOTE : 使用 pycld3 进行 language detection
see : https://github.com/bsolomon1124/pycld3
code 代码参考 ： https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

"""
import gzip
import hashlib
import logging
from datetime import datetime
from typing import Callable, Dict, List
import glob
import os
import json
import pandas as pd
import numpy as np
from furl import furl
from gs_framework.utilities import md5_str
from gs_research_workflow.nlp.data.general_browser_workflow_docs import BinaryAttachment, GeneralBrowserActionInstance

from gs_research_workflow.nlp.data.docs_in_mongo import Article

from gs_research_workflow.rpa_workflow.result_extraction.utilities import append_site_to_url, upsert_document

logger = logging.getLogger(__name__)


def md5_binary(bin: bytes) -> str:
    return hashlib.md5(bin).digest().hex().upper()


def _parse_date(date_string: str) -> datetime:
    # NOTE:这里 new DateDataParser() 对象，避免上一次的判断条件会产生影响，将该函数变成 non state 的
    from dateparser import DateDataParser
    data = DateDataParser(try_previous_locales=False).get_date_data(date_string, None)
    if data:
        return data['date_obj']

# region 一些时间字符串在解析之前的预处理函数

def split_by_chn_dot(s: str) -> str:
    """适用于从 雪球 获取的时间字符串，eg : "05-29 13:55 · 来自新闻" => "05-29 13:55"""
    return s.split("·")[0].strip()

# endregion


TIME_STR_PREPROCESS: Dict[str, Callable] = {"split_by_chn_dot": split_by_chn_dot}


class GeneralBrowserBackendProcess:

    @staticmethod
    def process_action_result(rlt_path: str, batch_action_uuid: str, action_uuid: str, save_doc: bool = True):
        dict_extract_info: Dict[str, str] = {}

        extract_info_files = glob.glob(os.path.join(rlt_path, "*_extract_info.js"))
        if extract_info_files:
            with open(extract_info_files[0], "r") as f:
                dict_extract_info = json.load(f)

        article_files = glob.glob(os.path.join(rlt_path, "*_articles.csv"))
        ls_all_article_uuid: List[str] = list()
        """保存所有的 uuid ，用于到 Mongo 中查询哪些是已经 Insert 的"""
        ls_all_article_doc_dict: List[Dict] = list()
        """先保存到一个 list , 然后统一 upsert document """

        if article_files:
            df_articles = pd.read_csv(article_files[0], header=0)
            for idx, row in df_articles.iterrows():
                dict_row = row.to_dict()
                dict_article = dict()
                # "title" = > Article.title ， 一般不做特殊处理，有则填入
                if not pd.isna(dict_row.get("title", np.NaN)):
                    dict_article["title"] = dict_row["title"]
                # "abstract" = > Article.abstract, 摘要，一般不做特殊处理
                if not pd.isna(dict_row.get("abstract", np.NaN)):
                    dict_article["abstract"] = dict_row["abstract"]
                # "channel_in_site" = > Article.channel_in_site, 二级分类，站点内的
                if not pd.isna(dict_row.get("channel_in_site", np.NaN)):
                    dict_article["channel_in_site"] = dict_row["channel_in_site"]
                # "full_text_url" = > Article.full_text_url ， 正文的链接，需要做地址转换
                if not pd.isna(dict_row.get("full_text_url", np.NaN)):
                    full_text_url = dict_row["full_text_url"]
                    # 尝试拼接 site
                    page_url = dict_extract_info.get("real_url", "")
                    if page_url:
                        full_text_url = append_site_to_url(full_text_url, furl(page_url).origin)
                    dict_article["full_text_url"] = full_text_url
                # "publish_time" = > Article.publish_time, 可能需要有数据预处理
                if not pd.isna(dict_row.get("publish_time", np.NaN)):
                    s_time = dict_row["publish_time"]
                    s_time_preprocess = dict_extract_info.get("publish_time_preprocess", "")
                    if s_time_preprocess:
                        assert s_time_preprocess in TIME_STR_PREPROCESS
                        s_time = TIME_STR_PREPROCESS[s_time_preprocess](s_time)
                    dt_time = _parse_date(s_time)
                    if dt_time:
                        dict_article["publish_time"] = dt_time
                if "article_site" in dict_extract_info:
                    dict_article["engine_site"] = dict_extract_info["article_site"]
                # 生成 uuid
                if "full_text_url" in dict_article:  # 优先考虑 url 作为 uuid
                    dict_article["uuid"] = md5_str(dict_article["full_text_url"])
                elif "title" in dict_article and "engine_site" in dict_article:  # 标题+site作为 uuid
                    # note: publish_time 不能计算 MD5 , 因为一些比较模糊的字符串，比如 5h 在不同的时间解析，会得到不一致的内容
                    dict_article["uuid"] = md5_str(f"{dict_article['engine_site']}-{dict_article['title']}")
                else:
                    continue
                dict_article["action_uuid"] = action_uuid
                dict_article["batch_action_uuid"] = batch_action_uuid
                ls_all_article_uuid.append(dict_article["uuid"])
                ls_all_article_doc_dict.append(dict_article)

        # TODO: 查询数据库中是否存在该项内容，用于标记 new / existed
        all_exist_docs = Article.objects(uuid__in=ls_all_article_uuid).only("uuid")
        set_existed_uuid = set([doc.uuid for doc in all_exist_docs])

        # 更新 db
        related_articles: List[Article] = list()
        new_found_articles: List[Article] = list()
        for article_doc_dict in ls_all_article_doc_dict:
            related_articles.append(Article(uuid=article_doc_dict["uuid"]))
            if article_doc_dict["uuid"] in set_existed_uuid:
                logger.info(f"Doc '{article_doc_dict['uuid']}' is existed already.")
                continue
            new_found_articles.append(Article(uuid=article_doc_dict["uuid"]))
            if save_doc:
                upsert_document(Article(**article_doc_dict), True)
        logger.info(f"Action '{action_uuid}' found {len(new_found_articles)} new articles")

        # 存 img 和 pdf
        pdf_screen_files = glob.glob(os.path.join(rlt_path, "*_webpage_content.pdf"))
        orig_pdf_bin_uuid: str = None
        if pdf_screen_files:
            with open(pdf_screen_files[0], "rb") as f:
                bin_pdf = f.read()
            bin_pdf_gz = gzip.compress(bin_pdf)
            orig_pdf_bin_uuid = md5_binary(bin_pdf)
            if save_doc:
                pdf_attach = BinaryAttachment(uuid=orig_pdf_bin_uuid, bin_data=bin_pdf_gz, file_ext="pdf", is_gzip=True,
                                              bin_length=len(bin_pdf_gz), ctime=datetime.now(), action_uuid=action_uuid)
                upsert_document(pdf_attach, False)

        png_screenshot_files = glob.glob(os.path.join(rlt_path, "*_browser_sceenshot.png"))
        orig_png_bin_uuid: str = None
        if pdf_screen_files:
            with open(png_screenshot_files[0], "rb") as f:
                bin_png = f.read()
            bin_png_gz = gzip.compress(bin_png)
            orig_png_bin_uuid = md5_binary(bin_png)
            if save_doc:
                png_attach = BinaryAttachment(uuid=orig_png_bin_uuid, bin_data=bin_png_gz, file_ext="png", is_gzip=True,
                                              bin_length=len(bin_png_gz), ctime=datetime.now(), action_uuid=action_uuid)
                upsert_document(png_attach, False)

        # 存 GeneralBrowserActionInstance
        if save_doc:
            general_browser_action_doc = GeneralBrowserActionInstance(uuid=action_uuid,related_articles=related_articles,
                                                                      new_found_articles=new_found_articles,
                                                                      pdf_page_snapshot=BinaryAttachment(uuid=orig_pdf_bin_uuid),
                                                                      img_page_snapshot=BinaryAttachment(uuid=orig_png_bin_uuid)
                                                                      )
            upsert_document(general_browser_action_doc, False)


if __name__ == "__main__":

    from gs_research_workflow.common.mongo_resource import mongo_db_conn, used_db_position, db_nlp

    mongo_db_conn(used_db_position, db_nlp)

    pd.set_option("display.max_rows", 20)
    pd.set_option("display.max_columns", None)
    # GeneralBrowserBackendProcess.process_action_result(
    #     "/tmp/laigen/debug_data/general_desktop_browser_backend_action/xueqiu", "", False)

    GeneralBrowserBackendProcess.process_action_result(
        "/tmp/laigen/debug_data/general_desktop_browser_backend_action/google_news_tab", "debug_batch_uuid",
        "debug_action_uuid_1", True)

    # import dateparser
    #
    # ls_s = ["3 hours ago", "22-Jun-20", "05-29 23:24 ", "Thu, Mar. 19", "Fri, May 22", "Aug. 19, 2019",
    #         "1分钟前", "3天前", "5小时前", "57m", "5h", "Yesterday, 2:07 PM", "Today, 12:58 AM", "5 years ago"]
    # for s in ls_s:
    #     print(f"'{s}' => {dateparser.parse(s)}")
    # print(dateparser.parse(split_by_chn_dot("05-29 13:55 · 来自新闻")))


