# -*- coding: UTF-8 -*-
from datetime import date

from gs_research_workflow.external_data.data_vendor.jy.ddl_entities.corp_chn.QT_DailyQuote import QT_DailyQuote

from gs_research_workflow.time_series.data.otv_table_in_arctic import ChnEquityMarketQuotation


def test_data_process():
    otv = ChnEquityMarketQuotation()
    sql = otv.get_sql_select_by_t(date(2010, 1, 1), date(2012, 12, 31))
    print(sql)



if __name__ == "__main__":
    test_data_process()

