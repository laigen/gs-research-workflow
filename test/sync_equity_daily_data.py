# -*- coding: utf-8 -*-

"""
调用远程接口，同步沪深个股的数据，这样可以加速 train 的动作
"""
from datetime import date

from gs_research_workflow.time_series.data.arctic_data_sync import sync_equity_data, sync_equity_to_sw_industry, \
    sync_equity_cs_daily, sync_sw_industry_index

if __name__ == "__main__":
    import logging
    debug_level_modules = ["gs_research_workflow.time_series.data.arctic_and_local_cache", "__main__"]
    for n in debug_level_modules:
        logging.getLogger(n).setLevel(logging.INFO)

    # sync_equity_data("SZSE")
    # sync_equity_data("SSE")
    # sync_index_and_fund_nav()
    # sync_equity_financial_statement("SSE")
    # sync_equity_financial_statement("SZSE")
    # sync_equity_to_sw_industry("L1", start_t=date(1990, 1, 1), end_t=date(2019, 12, 31))
    # sync_equity_to_sw_industry("L2", start_t=date(1990, 1, 1), end_t=date(2019, 12, 31))
    # sync_equity_to_sw_industry("L3", start_t=date(1990, 1, 1), end_t=date(2019, 12, 31))
    # sync_equity_cs_daily(start_t=date(2000, 1, 1))

    # NOTE 计算申万指数之前，必须先同步好所有的 ts 数据
    sync_sw_industry_index(start_t=date(2000, 2, 1), end_t=date(2020, 2, 29))
