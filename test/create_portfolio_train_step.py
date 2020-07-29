# -*- coding: UTF-8 -*-
"""创建portfolio weight 相关的 training step 对象"""
import asyncio
from datetime import date, timedelta

import os
from typing import Callable

from gs_research_workflow.time_series.gs_steps.model_steps import TFModelStep
from gs_research_workflow.time_series.gs_steps.tf_dataset_steps.equity_daily_data_mask_ds import IByTGeneratorStep, \
    EquityPoolTSDatasetStep

from gs_research_workflow.time_series.gs_steps.tf_ds_for_financial_statement import ChnEquityInputStep, \
    FinancialStatementCSMaskedTFDatasetStep, FinancialStatementCSBertConst

from gs_research_workflow.common.serialization_utilities import save_mapping_to_file_or_stream, cls_to_str

from gs_research_workflow.time_series.gs_steps.tf_train_steps import TFTrainStep

from gs_research_workflow.time_series.gs_steps.ts_data_steps import SymbolMultipleTSStep

from gs_research_workflow.time_series.gs_steps.local_context_step import GetContextStep

from gs_research_workflow.time_series.gs_steps.predefined_step_fields import TSPortfolioWeightInputStep
from gs_research_workflow.time_series.models.inception_time_with_attention import \
    InceptionTimeWithAttentionForWeightPrediction
from gs_research_workflow.time_series.models.ts_bert import TSBertForWeightPrediction, TSBertForMaskedCS, TSBertName
from gs_research_workflow.time_series.partial_workflow.fit_related_steps import get_compile_step, \
    get_recommend_fit_with_callback_steps
from gs_research_workflow.time_series.partial_workflow.ts_category_model_steps import \
    get_default_inception_with_attention_model_weight_prediction_task_step, \
    get_default_ts_bert_for_weight_prediction_task_step
from gs_research_workflow.time_series.partial_workflow.ts_portfolio_weight_steps import EQUITY_TS_FEATURES_CONTEXT, \
    generate_portfolio_ts_datas


def category_portfolio_weight_train_workflow(f_get_model_step: Callable, cls_model):
    wf_context = EQUITY_TS_FEATURES_CONTEXT
    # ALERT: time_steps_as_last_dimension 参数， cnn 类 model 取 False , Bert 类 Model 取 True
    train_ds_with_pip, val_ds_with_pip, eval_ds_with_pip = generate_portfolio_ts_datas(wf_context,
                                                                                       time_steps_as_last_dimension=True)
    train_input_steps = [(train_ds_with_pip, "train_ds"), (val_ds_with_pip, "val_ds"), (eval_ds_with_pip, "test_ds")]
    # train_input_steps += [get_default_inception_with_attention_model_weight_prediction_task_step()]
    train_input_steps += [f_get_model_step()]
    train_input_steps += [get_compile_step()]

    # 大概有 600k 测试数据点，这里暂时先取其中一部分数据进行 train ，避免耗时过长
    train_input_steps += get_recommend_fit_with_callback_steps(epochs=5, steps_per_epoch=20000, validation_steps=300)
    # ONLY for smoke test
    # train_input_steps += get_recommend_fit_with_callback_steps(epochs=2, steps_per_epoch=1, validation_steps=1)

    train_step = TFTrainStep(_input_steps=train_input_steps)
    # 作为一个标准的 workflow 进行保存
    from gs_research_workflow.samples import workflow_cfg

    sample_file_path = os.path.join(os.path.dirname(workflow_cfg.__file__),
                                    f"{cls_model.__name__}_workflow_v1.yml")
    print(sample_file_path)
    save_mapping_to_file_or_stream(sample_file_path, train_step.get_init_value_dict(True), wf_context)
    return train_step


def cs_bert_workflow():
    equity_split_step = ChnEquityInputStep(train_val_split_ratio=0.9)
    train_ds_with_pip = FinancialStatementCSMaskedTFDatasetStep(ds_pip="lambda ds: ds.repeat().batch(50)",
                                                                _input_steps=[(equity_split_step, "train")])
    val_ds_with_pip = FinancialStatementCSMaskedTFDatasetStep(ds_pip="lambda ds: ds.repeat().batch(50)",
                                                              _input_steps=[(equity_split_step, "validation")])
    eval_ds_with_pip = FinancialStatementCSMaskedTFDatasetStep(ds_pip="lambda ds: ds.batch(10)",
                                                               _input_steps=[(equity_split_step, "evaluate")])
    train_input_steps = [(train_ds_with_pip, "train_ds"), (val_ds_with_pip, "val_ds"), (eval_ds_with_pip, "test_ds")]

    model_step = TFModelStep(model_cls_str=cls_to_str(TSBertForMaskedCS),
                             model_hp=TSBertForMaskedCS.HP(
                                 name=TSBertName.CHN_EQUITY_FINANCIAL_STATEMENT_CONST_MASK,
                                 hidden_size=FinancialStatementCSBertConst.FIN_STATEMENT_INDICATORS_COUNT,
                                 num_attention_heads=12))
    train_input_steps += [model_step]
    train_input_steps += [get_compile_step(loss="ts_bert_mae", metrics=["ts_bert_mae", "ts_bert_mse"])]
    train_input_steps += get_recommend_fit_with_callback_steps(epochs=5, steps_per_epoch=700, validation_steps=70)

    train_step = TFTrainStep(_input_steps=train_input_steps)
    # 作为一个标准的 workflow 进行保存
    from gs_research_workflow.samples import workflow_cfg

    sample_file_path = os.path.join(os.path.dirname(workflow_cfg.__file__),
                                    f"{TSBertForMaskedCS.__name__}_workflow_v1.yml")
    print(sample_file_path)
    save_mapping_to_file_or_stream(sample_file_path, train_step.get_init_value_dict(True), None)
    return train_step


def cs_bert_equity_daily_workflow():
    start_t = date(2019, 1, 1)
    end_t = date(2019, 12, 31)

    i_t = IByTGeneratorStep(start_t=start_t, end_t=end_t - timedelta(days=92), sample_freq="2w",
                            train_val_split_ratio=0.95, evaluate_items_count=1,
                            use_concept_blocks=False, ls_i_by_condition=[("low_pe", "pe > 3.0 and pe < 8.0"),
                                                                         ("mid_pe", "pe > 15.0 and pe < 30.0"),
                                                                         ("high_pe", "pe > 30.0 and pe < 80.0"),
                                                                         ("low_pb", "pb >= 0.6 and pb <= 0.8"),
                                                                         ("mid_pb", "pb >= 0.9 and pb <= 1.1"),
                                                                         ("high_pb", "pb >= 1.3 and pb <= 1.8"),
                                                                         ("sml_cap",
                                                                          "total_mv >= 5.0e5 and total_mv < 5.0e6"),
                                                                         ("mid_cap",
                                                                          "total_mv >= 8.0e6 and total_mv < 2.0e7"),
                                                                         ("large_cap", "total_mv >= 2.0e7")
                                                                         ])

    # EquityPoolTSDatasetStep(df_i_by_t=i_t.pool_by_t, i_start_t=start_t, i_end_t=end_t,
    #                         ds_pip="lambda ds: ds.repeat().batch(8)")

    train_ds_with_pip = EquityPoolTSDatasetStep(ds_pip="lambda ds: ds.repeat().batch(5)",
                                                i_start_t=start_t, i_end_t=end_t,
                                                _input_steps=[(i_t, "train")])
    val_ds_with_pip = EquityPoolTSDatasetStep(ds_pip="lambda ds: ds.repeat().batch(5)",
                                              i_start_t=start_t, i_end_t=end_t,
                                              _input_steps=[(i_t, "validation")])
    eval_ds_with_pip = EquityPoolTSDatasetStep(ds_pip="lambda ds: ds.batch(3)",
                                               i_start_t=start_t, i_end_t=end_t,
                                               _input_steps=[(i_t, "evaluate")])

    train_input_steps = [(train_ds_with_pip, "train_ds"), (val_ds_with_pip, "val_ds"), (eval_ds_with_pip, "test_ds")]

    # model = TSBertForMaskedCS(
    #     hp=TSBertForMaskedCS.HP(hidden_size=EquityPoolTSDatasetStep.MAX_INDICATORS,
    #                             # 多一个作为 padding 的0
    #                             max_position_embeddings=EquityPoolTSDatasetStep.LOOK_PERIOD_ITEMS + 1,
    #                             type_vocab_size=EquityPoolTSDatasetStep.MAX_ENTITIES_PER_INST + 1,
    #                             num_attention_heads=12))

    model_name = TSBertName.CHN_EQUITY_DAILY_PREDICT_RETURN_LESS_INDICATORS
    model_step = TFModelStep(model_cls_str=cls_to_str(TSBertForMaskedCS),
                             model_hp=TSBertForMaskedCS.HP(
                                 name=model_name,
                                 hidden_size=EquityPoolTSDatasetStep.MAX_INDICATORS,
                                 max_position_embeddings=EquityPoolTSDatasetStep.LOOK_PERIOD_ITEMS + 1,
                                 type_vocab_size=EquityPoolTSDatasetStep.MAX_ENTITIES_PER_INST + 1,
                                 num_attention_heads=12)
                             )
    train_input_steps += [model_step]
    train_input_steps += [
        get_compile_step(loss="mae_align_to_y_true", metrics=["mae_align_to_y_true", "mse_align_to_y_true"])]
    # train_input_steps += get_recommend_fit_with_callback_steps(epochs=2, steps_per_epoch=10000, validation_steps=150)
    # train_input_steps += get_recommend_fit_with_callback_steps(epochs=1, steps_per_epoch=14000, validation_steps=200)
    train_input_steps += get_recommend_fit_with_callback_steps(epochs=3, steps_per_epoch=5000, validation_steps=200)
    # train_input_steps += get_recommend_fit_with_callback_steps(epochs=2, steps_per_epoch=20, validation_steps=4)

    train_step = TFTrainStep(_input_steps=train_input_steps)
    # 作为一个标准的 workflow 进行保存
    from gs_research_workflow.samples import workflow_cfg

    sample_file_path = os.path.join(os.path.dirname(workflow_cfg.__file__),
                                    f"{model_name}_workflow_v1.yml")
    print(sample_file_path)
    save_mapping_to_file_or_stream(sample_file_path, train_step.get_init_value_dict(True), None)
    return train_step


async def run_fit(train_step):
    train_step.prepare_metrics_recorder("test_experiment", "test_experiment_uuid", "test_trial_uuid")
    await train_step.fit()
    # TODO daily ts bert eval 没有结果的 bug
    await train_step.eval_model()
    print("----- finished ------")

if __name__ == "__main__":
    # inception with attention
    # train_step = category_portfolio_weight_train_workflow(
    #     get_default_inception_with_attention_model_weight_prediction_task_step)

    # train_step = category_portfolio_weight_train_workflow(get_default_ts_bert_for_weight_prediction_task_step,
    #                                                       TSBertForWeightPrediction)
    # train_step = cs_bert_workflow()
    train_step = cs_bert_equity_daily_workflow()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_fit(train_step))
    loop.run_forever()

