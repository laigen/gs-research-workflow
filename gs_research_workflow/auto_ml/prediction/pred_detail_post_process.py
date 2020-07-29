# -*- coding: UTF-8 -*-

"""
prediction 结果的后续处理操作类，主要支持的功能包括：
1) 在 prediction 的结果 dataframe 中增加便于阅读的类，如： symbol name , category label 等
"""
from typing import Dict

from gs_research_workflow.time_series.data.tushare_wrapper import TuShareProData


class TushareSymbolToName:
    def __init__(self, tushare_pro: TuShareProData):
        dict_all_symbol = tushare_pro.stock_basic(exchange="SSE").set_index("ts_code").to_dict("index")
        dict_all_symbol.update(tushare_pro.stock_basic(exchange="SZSE").set_index("ts_code").to_dict("index"))
        self._dict_all_symbols: Dict[str, Dict] = dict_all_symbol
        """ symbol 的详细信息内容"""

    def __call__(self, ret_cal_name: str, col_name:str, row):
        return self._dict_all_symbols[getattr(row, col_name)][ret_cal_name]


class CategoryIntToLabel:
    def __init__(self, category_label_mapping_object):
        assert hasattr(category_label_mapping_object, "num_to_category")
        self._category_label_mapping = category_label_mapping_object

    def __call__(self, col_name: str, row):
        return self._category_label_mapping.num_to_category(getattr(row, col_name))
