# -*- coding: UTF-8 -*-
"""
新建一个典型的 prediction workflow
"""
import asyncio
from datetime import date

from gs_research_workflow.time_series.gs_steps.tf_dataset_step import TSPeriodTSByLookbackStep, \
    TSCategoryDatasetPreparingStep, TFDSSpecDataCodingType

from gs_research_workflow.time_series.gs_steps.func_steps import FuncStrStep

from gs_research_workflow.time_series.gs_steps.df_funcs import dfs_concat

from gs_research_workflow.common.serialization_utilities import cls_to_str, save_mapping_to_file_or_stream

from gs_research_workflow.time_series.gs_steps.ts_data_steps import SymbolTSStep

from gs_research_workflow.time_series.gs_steps.data_structure_utility_steps import KeyValueListToMappingStep

from gs_research_workflow.time_series.gs_steps.local_context_step import GetContextStep

from gs_research_workflow.time_series.models.inception_time import InceptionTime

from gs_research_workflow.time_series.gs_steps.model_steps import ModelPathGeneratorStep, ModelWithWeightSaveLoadStep, \
    AdditionalColumnInDS

import os


def category_prediction_workflow():
    WORKFLOW_CONTEXT = {"LOCAL":
        {
            "category_labels": ["BigCap", "MidCap", "SmlCap"],
            "category_by_index_membership": ["000043.SH", "000044.SH", "000045.SH"],
            "x_feature_from_api": "equity_backward_adjust_daily",
            "x_feature_columns": ["open", "high", "low", "close", "pre_close", "change", "pct_chg", "vol", "amount"],
            "pred_ds_pip": "lambda ds: ds.batch(10)",
            "y_start_t":date(2019, 11, 1),
            "y_end_t":date(2019, 12, 1),
        }
    }
    all_context_step = {k: GetContextStep(k) for k in WORKFLOW_CONTEXT["LOCAL"].keys()}
    for k, v in all_context_step.items():
        v.SET_CONTEXT(WORKFLOW_CONTEXT)

    kv_convert_step = KeyValueListToMappingStep(_input_steps=[
        (all_context_step["category_labels"], "key_list"),
        (all_context_step["category_by_index_membership"], "value_list")])

    test_index_membership_ts_step = SymbolTSStep(api="index_weight", cols=["con_code"],
                                                 _input_steps=[(kv_convert_step, "symbols"),
                                                               (all_context_step["y_start_t"], "start_t"),
                                                               (all_context_step["y_end_t"], "end_t")])

    time_align_step = SymbolTSStep(api="index_quotation_daily", symbols="000001.SH", cols=["close"])

    test_concat_df_step = FuncStrStep(func_obj_str=cls_to_str(dfs_concat),
                                      _input_steps=[(test_index_membership_ts_step, "ts_process")])

    x_orig_data_step = SymbolTSStep(
        _input_steps=[(all_context_step["x_feature_from_api"], "api"),
                      (all_context_step["x_feature_columns"], "cols")])

    x_feature_callable_step = TSPeriodTSByLookbackStep(
        _input_steps=[(x_orig_data_step, "period_ts_callable"), (time_align_step, "time_align")])

    pred_ds_with_pip = TSCategoryDatasetPreparingStep(export_symbol_in_ds=True, export_t_in_ds=True,
                                                      _input_steps=[x_feature_callable_step, test_concat_df_step,
                                                                    (all_context_step["category_labels"],
                                                                     "category_labels"),
                                                                    (all_context_step["pred_ds_pip"], "ds_pip")])

    # save test ds pip
    # NOTE: 这里只需要保存 prediction_ds 的workflow 即可，有关 model 可以直接定义在 run 的 env 里
    from gs_research_workflow.samples import workflow_cfg
    sample_file_path = os.path.join(os.path.dirname(workflow_cfg.__file__), "category_prediction_ds_workflow_v1.yml")
    print(sample_file_path)
    save_mapping_to_file_or_stream(sample_file_path, pred_ds_with_pip.get_init_value_dict(True), WORKFLOW_CONTEXT)


    # 这里是 用来验证
    # # UUID="808CCED2DF57AE1BC7030C9B57F9A23A" for debug-73
    model_inst_path = ModelPathGeneratorStep(InceptionTime.__name__, "F24E10E3C3C556FC3FDC0C4B18EFA3C5")
    model_with_weight_step = ModelWithWeightSaveLoadStep(_input_steps=[model_inst_path])
    df = model_with_weight_step.predict(pred_ds_with_pip.tf_ds, y_true_col_index=1,
                                        additional_cols=[
                                            AdditionalColumnInDS(2, "symbol", TFDSSpecDataCodingType.utf8_str),
                                            AdditionalColumnInDS(3, "t", TFDSSpecDataCodingType.pd_timestamp)])


    print(df)


if __name__ == "__main__":
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(category_prediction_workflow())
    # loop.run_forever()
    category_prediction_workflow()