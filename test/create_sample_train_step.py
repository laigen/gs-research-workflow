# -*- coding: UTF-8 -*-
"""创建一个典型的 training step 对象"""
import asyncio

import os
from gs_research_workflow.time_series.data.tushare_wrapper import TuShareProData

from gs_research_workflow.common.serialization_utilities import save_mapping_to_file_or_stream
from gs_research_workflow.time_series.gs_steps.tf_train_steps import TFTrainStep
from gs_research_workflow.time_series.partial_workflow.fit_related_steps import get_recommend_fit_with_callback_steps, \
    get_category_compile_step
from gs_research_workflow.time_series.partial_workflow.ts_category_dataset_steps import \
    category_by_membership_data, MARKET_CAP_INDEX_MEMBERSHIP_WORKFLOW_DEFAULT_CONTEXT
from gs_research_workflow.time_series.partial_workflow.ts_category_model_steps import get_default_inception_model_classification_task_step



async def category_trial_workflow(f_get_model_step, model_name: str):
    wf_context = MARKET_CAP_INDEX_MEMBERSHIP_WORKFLOW_DEFAULT_CONTEXT
    wf_context["LOCAL"]["x_feature_from_api"] = "equity_basic_daily"
    wf_context["LOCAL"]["x_feature_columns"] = ["turnover_rate", "volume_ratio", "pe", "pe_ttm", "pb", "ps", "ps_ttm",
                                                "dv_ratio", "dv_ttm"]
    # 改为 category 的数据
    # category_type = "industry"
    # gs_ts_pro = TuShareProData()
    # df = gs_ts_pro.index_classify(level="L1")
    # # 这种定义方式有点风险，industry 可能会有增减，暂时简单先这么写
    # wf_context["LOCAL"]["category_labels"] = df["industry_name"].tolist()
    # wf_context["LOCAL"]["category_by_index_membership"] = df["index_code"].tolist()
    #
    # train_ds_with_pip, val_ds_with_pip, test_ds_with_pip = \
    #     category_by_membership_data(wf_context, category_api="period_index_member", category_symbol_cols=None)

    # index member ship
    category_type = "index_cap_membership"
    train_ds_with_pip, val_ds_with_pip, test_ds_with_pip = \
        category_by_membership_data(wf_context, category_api="index_weight", category_symbol_cols=None)


    # Training Workflow 部分
    train_input_steps = [(train_ds_with_pip, "train_ds"), (val_ds_with_pip, "val_ds"), (test_ds_with_pip, "test_ds")]
    train_input_steps += [f_get_model_step(len(wf_context["LOCAL"]["category_labels"])), get_category_compile_step()]

    train_input_steps += get_recommend_fit_with_callback_steps(steps_per_epoch=5000)
    # ONLY for smoke test
    # train_input_steps += get_recommend_fit_with_callback_steps(epochs=1, steps_per_epoch=1, validation_steps=1)

    train_step = TFTrainStep(_input_steps=train_input_steps)

    # 作为一个标准的 workflow 进行保存
    from gs_research_workflow.samples import workflow_cfg

    sample_file_path = os.path.join(os.path.dirname(workflow_cfg.__file__), f"{model_name}_{category_type}_category_workflow_v1.yml")
    print(sample_file_path)
    save_mapping_to_file_or_stream(sample_file_path, train_step.get_init_value_dict(True), wf_context)

    await train_step.fit()
    await train_step.eval_model()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(category_trial_workflow(get_default_inception_with_attention_model_step, "inception_with_attention"))
    loop.run_until_complete(category_trial_workflow(get_default_inception_model_classification_task_step, "inception_for_classification"))
    # loop.run_until_complete(category_trial_workflow(get_default_simple_lstm_model_step, "simple_lstm"))
    # loop.run_forever()
    # inception_category()
