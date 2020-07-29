# -*- coding: UTF-8 -*-
"""
提供一些用于创建标准workflow 的dataset steps 相关的公共函数调用
"""

from typing import Dict, Optional, Tuple, List
from datetime import date

from gs_research_workflow.time_series.data.tushare_wrapper import TuShareProData

from gs_research_workflow.time_series.gs_steps.tf_dataset_step import TSPeriodTSByLookbackStep, \
    TSCategoryDatasetPreparingStep

from gs_research_workflow.time_series.gs_steps.data_preprocess_steps import TrainValSpiltStep

from gs_research_workflow.time_series.gs_steps.df_funcs import dfs_concat

from gs_research_workflow.common.serialization_utilities import cls_to_str

from gs_research_workflow.time_series.gs_steps.func_steps import FuncStrStep

from gs_research_workflow.time_series.gs_steps.ts_data_steps import SymbolTSStep, SymbolMultipleTSStep

from gs_research_workflow.time_series.gs_steps.data_structure_utility_steps import KeyValueListToMappingStep

from gs_research_workflow.time_series.gs_steps.local_context_step import GetContextStep

MARKET_CAP_INDEX_MEMBERSHIP_WORKFLOW_DEFAULT_CONTEXT = {"LOCAL":
        {
            "category_labels": ["BigCap", "MidCap", "SmlCap"],
            "category_by_index_membership": ["000043.SH", "000044.SH", "000045.SH"],

            # x 的 feature 的数据，来自于哪个 class
            "x_feature_query_class": cls_to_str(TuShareProData),
            # 与股票直接相关的 features
            "x_features_per_symbol": {
                "equity_basic_daily": ("fin_ind_", ["turnover_rate", "turnover_rate_f",
                                                          "volume_ratio", "pe", "pe_ttm", "pb", "ps",
                                                          "ps_ttm", "dv_ratio", "dv_ttm",
                                                          "total_share", "free_share", "total_mv", "circ_mv"]),
                "equity_backward_adjust_daily": ("backward_adj_", ["open", "high", "low", "close", "pre_close",
                                                                   "change", "pct_chg", "vol", "amount"]),
                "equity_moneyflow_daily": ("moneyflow_", ["buy_sm_vol", "buy_sm_amount", "sell_sm_vol",
                                                          "sell_sm_amount", "buy_md_vol", "buy_md_amount",
                                                          "sell_md_vol", "sell_md_amount", "buy_lg_vol",
                                                          "buy_lg_amount", "sell_lg_vol", "sell_lg_amount",
                                                          "buy_elg_vol", "buy_elg_amount", "sell_elg_vol",
                                                          "sell_elg_amount", "net_mf_vol", "net_mf_amount"])
            },



            # "x_feature_from_api": "equity_backward_adjust_daily",
            # "x_feature_columns": ["open", "high", "low", "close", "pre_close", "change", "pct_chg", "vol", "amount"],


            "train_val_ds_pip": "lambda ds: ds.repeat().batch(20)",
            "test_ds_pip": "lambda ds: ds.batch(10)",  # ALERT : test_ds 不能加 repeat，需要是一个有限集。如果是无限集，则需要加 steps 参数
        }
    }


def category_by_membership_data(workflow_context: Dict = MARKET_CAP_INDEX_MEMBERSHIP_WORKFLOW_DEFAULT_CONTEXT,
                                category_api: str = "index_weight",
                                category_symbol_cols: List[str] = ["con_code"],
                                train_start_t: date = date(2014, 1, 1), train_end_t: date = date(2019, 10, 31),
                                test_start_t: date = date(2019, 11, 1), test_end_t: date = date(2019, 12, 1),
                                train_val_split_ratio: float = 0.85, random_state: Optional[int] = 100) \
        -> Tuple[TSCategoryDatasetPreparingStep, TSCategoryDatasetPreparingStep, TSCategoryDatasetPreparingStep]:
    """
    Returns
    -------
    -
        train_ds_step , val_ds_step , test_ds_step
    """
    assert "LOCAL" in workflow_context
    assert "category_labels" in workflow_context["LOCAL"]
    assert "category_by_index_membership" in workflow_context["LOCAL"]
    assert "x_feature_query_class" in workflow_context["LOCAL"]
    assert "x_features_per_symbol" in workflow_context["LOCAL"]

    all_context_step = {k: GetContextStep(k) for k in workflow_context["LOCAL"].keys()}
    for k, v in all_context_step.items():
        v.SET_CONTEXT(workflow_context)

    kv_convert_step = KeyValueListToMappingStep(_input_steps=[
        (all_context_step["category_labels"], "key_list"),
        (all_context_step["category_by_index_membership"], "value_list")])

    # training 用到的数据集和 test 用到的数据集，通过不同的时间段进行分开
    # 约有 28K 个数据点
    train_index_membership_ts_step = SymbolTSStep(api=category_api, cols=category_symbol_cols,
                                                  _input_steps=[(kv_convert_step, "symbols")],
                                                  start_t=train_start_t, end_t=train_end_t)

    test_index_membership_ts_step = SymbolTSStep(api=category_api, cols=category_symbol_cols,
                                                 _input_steps=[(kv_convert_step, "symbols")],
                                                 start_t=test_start_t, end_t=test_end_t)

    train_concat_df_step = FuncStrStep(func_obj_str=cls_to_str(dfs_concat),
                                       _input_steps=[(train_index_membership_ts_step, "ts_process")])

    test_concat_df_step = FuncStrStep(func_obj_str=cls_to_str(dfs_concat),
                                      _input_steps=[(test_index_membership_ts_step, "ts_process")])

    train_val_set = TrainValSpiltStep(_input_steps=[(train_concat_df_step, "train_val_orig_data")],
                                      split_ratio=train_val_split_ratio,
                                      random_state=random_state)

    # 这里 hardcode 成用上证综指作为 time align 对象，以后做不同市场才考虑将该数据放开
    time_align_step = SymbolTSStep(api="index_quotation_daily", symbols="000001.SH", cols=["close"])

    x_orig_data_step = SymbolMultipleTSStep(
        _input_steps=[(all_context_step["x_feature_query_class"], "data_query_class"),
                      (all_context_step["x_features_per_symbol"], "apis_and_columns")])

    x_feature_callable_step = TSPeriodTSByLookbackStep(
        _input_steps=[(x_orig_data_step, "period_ts_callable"), (time_align_step, "time_align")])

    train_ds_with_pip = TSCategoryDatasetPreparingStep(export_symbol_in_ds=False, export_t_in_ds=False,
                                                       _input_steps=[x_feature_callable_step,
                                                                     (train_val_set, "train_set"),
                                                                     (all_context_step["category_labels"],
                                                                      "category_labels"),
                                                                     (all_context_step["train_val_ds_pip"], "ds_pip")])

    val_ds_with_pip = TSCategoryDatasetPreparingStep(export_symbol_in_ds=False, export_t_in_ds=False,
                                                     _input_steps=[x_feature_callable_step, (train_val_set, "val_set"),
                                                                   (all_context_step["category_labels"],
                                                                    "category_labels"),
                                                                   (all_context_step["train_val_ds_pip"], "ds_pip")])

    test_ds_with_pip = TSCategoryDatasetPreparingStep(export_symbol_in_ds=False, export_t_in_ds=False,
                                                      _input_steps=[x_feature_callable_step, test_concat_df_step,
                                                                    (all_context_step["category_labels"],
                                                                     "category_labels"),
                                                                    (all_context_step["test_ds_pip"], "ds_pip")])
    return train_ds_with_pip, val_ds_with_pip, test_ds_with_pip
