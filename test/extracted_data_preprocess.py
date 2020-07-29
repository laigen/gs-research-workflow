# -*- coding: UTF-8 -*-

"""
TO BE REMOVED
"""
import logging
from datetime import datetime

import pandas as pd

from gs_research_workflow.common.mongo_resource import db_nlp, mongo_db_conn, used_db_position

from gs_research_workflow.rpa_workflow.result_extraction.google_news import GoogleNewsSearchProcess
from gs_research_workflow.rpa_workflow.result_extraction.seeking_alpha import SeekingAlphaDataProcess

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    mongo_db_conn(used_db_position, db_nlp)
    # mongo_db_conn("google", db_nlp)



    # SeekingAlphaDataProcess.column_articles("/tmp/laigen/debug_data/seeking_alpha_special_columns_action",True)
    # SeekingAlphaDataProcess.author_detail("/tmp/laigen/debug_data/seeking_alpha_author_info_action", True)
    # SeekingAlphaDataProcess.symbol_summary("/tmp/laigen/debug_data/seeking_alpha_symbol_summary_action", True)
    # SeekingAlphaDataProcess.kw_search("/tmp/laigen/debug_data/seeking_alpha_kw_search_action", False)
    # TwitterDataProcess.kw_search("/tmp/laigen/debug_data/twitter_kw_search_action", True)
    # TwitterDataProcess.twitter_user_following("/tmp/laigen/debug_data/twitter_following_action", True)
    # AzureDataProcess.txt_analyse("/tmp/laigen/debug_data/azure_txt_ana_action", True)
    GoogleNewsSearchProcess.kw_news_search("/tmp/laigen/debug_data/google_news_search_action", True)

    # print(SeekingAlphaDataProcess.parse_display_dt_str("Wednesday, April 22nd 2020",datetime.now()))


    # file = "/tmp/laigen/debug_data/seeking_alpha_special_columns_action/20200508_205713_articles.csv"
    # df_articles = pd.read_csv(file, header=0, parse_dates=["extract_t"])
    # kw, df_rlt = SeekingAlphaExtractedDataPreProcess.proc_article_data(df_articles)

    # file = "/tmp/laigen/debug_data/seeking_alpha_author_info_action/20200508_210826_author_articles.csv"
    # df_articles = pd.read_csv(file, header=0, parse_dates=["extract_t"])
    # kw, df_rlt = SeekingAlphaExtractedDataPreProcess.proc_author_articles(df_articles)
    # print(kw)
    # print(df_rlt)

    # file = "/tmp/laigen/debug_data/seeking_alpha_symbol_summary_action/20200508_211937_symbol_indicators.csv"
    # df_articles = pd.read_csv(file, header=0)
    # symbol, df_info = SeekingAlphaDataProcess.proc_symbol_analysis(df_articles)
    # symbol, df_info = SeekingAlphaDataProcess.proc_symbol_news(df_articles)
    # symbol_indicator = SeekingAlphaDataProcess.proc_symbol_indicator(df_articles)

    # print(symbol_indicator)
    # print(df_info)




    # /article/4340069-banking-is-changing-and-will-not-look-back?source=all_articles_title

    def date_str_parser_unit_test():
        ls_t_test = ["Dec. 22, 2019, 6:18 AM", "Dec. 19, 2019, 2:32 PM", "Nov. 28, 2019, 4:17 AM",
                     "Mon, May 4, 11:30 AM", "Wed, May 6, 9:40 AM", "Wed, May 6, 8:13 PM", "Yesterday, 7:02 AM",
                     "Today, 7:06 AM"]
        for s in ls_t_test:
            print(SeekingAlphaDataProcess.parse_display_dt_str(s, datetime.now()))
