# -*- coding: utf-8 -*-
# for financial statement cs mask prediction
from gs_research_workflow.common.mongo_resource import db_nlp, mongo_db_conn


def for_notebook_eval_cs_financial_statement_mask():
    from gs_research_workflow.time_series.models.ts_bert import TSBertForMaskedCS, TSBertName
    from gs_research_workflow.time_series.gs_steps.model_steps import TFModelStep
    from gs_research_workflow.common.serialization_utilities import cls_to_str
    from gs_research_workflow.time_series.data.utilities import de_zscore_to_val
    from gs_research_workflow.common.path_utilities import _DATA_ROOT
    import os
    import sys

    PRINT_HIGHLIGHT_STYLE = "\033[1;37;41m"
    #  ---------- 不同的内容，只需要修改这一部分的参数项  ---------
    model_hp = TFModelStep(model_cls_str=cls_to_str(TSBertForMaskedCS),
                           model_hp=TSBertForMaskedCS.HP(
                               name=TSBertName.CHN_EQUITY_FINANCIAL_STATEMENT,
                               hidden_size=276,
                               num_attention_heads=12))  # model hp 这里只能修改 num_attention_heads:[6,12] 和 num_hidden_layers[8,12,16,20]
    # ---------------------------------------------------------

    checkpoint_path = os.path.join(_DATA_ROOT, "ModelData", model_hp.model_cls.__name__,
                                   model_hp.model_init_hp.get_hash_str())  # 这里不能调用 TFModelStep.check_point_path() , 会创建目录的
    if not os.path.isdir(checkpoint_path):
        print(PRINT_HIGHLIGHT_STYLE,
              f"model path '{checkpoint_path}' is not existed! please check the model hyper-parameters")
        raise RuntimeError(f"model path '{checkpoint_path}' is not existed! please check the model hyper-parameters")
    checkpoint_file = os.path.join(checkpoint_path, "tf_model.h5")
    if not os.path.exists(checkpoint_file):
        print(PRINT_HIGHLIGHT_STYLE, f"model weight file '{checkpoint_file}' is not existed")
        raise RuntimeError(f"model weight file '{checkpoint_file}' is not existed")
    model = TSBertForMaskedCS.from_pre_saved(checkpoint_path)

    # -------------------------------------------------

    # 如果不需要更换 model ，只是换股票的话，只需要调整该 Cell
    symbol = "600315.SH"  # 预测的股票

    # -------------------------------------------------

    # 这部分代码不需要修改，在变更了参数项之后重新执行即可
    # 准备用于展示的数据

    import pandas as pd
    from gs_research_workflow.time_series.data.tushare_wrapper import TuShareProData
    from gs_research_workflow.time_series.data.predefined_equity_apis import equity_all_financial_statement_zscore, \
        equity_comp_type, equity_all_financial_statement_mean_and_std, equity_all_financial_statement_by_enddate
    from gs_research_workflow.time_series.gs_steps.tf_ds_for_financial_statement import \
        FinancialStatementCSMaskedTFDatasetStep
    import tensorflow as tf

    pd.set_option('display.max_columns', None)  # 显示所有列
    pd.set_option('display.max_rows', None)  # 显示所有行
    pd.set_option('max_colwidth', 80)

    tushare = TuShareProData(use_l3_cache=True)

    df_zscore, series_mean, series_std = equity_all_financial_statement_zscore(tushare, symbol, ret_mean_and_std=True)
    comp_type = equity_comp_type(tushare, symbol)

    df_y_for_pred = df_zscore.iloc[-20:][:]  # 暂时只提供预测已公布数据的最后一期值
    df_y_true_original = equity_all_financial_statement_by_enddate(tushare, symbol)[-20:][:]
    input_ids, position_id, token_id, attention_mask_id = FinancialStatementCSMaskedTFDatasetStep.df_to_model_input(
        df_y_for_pred, comp_type, series_std * 100., False, True, False)

    y_pred = model((input_ids[tf.newaxis, :], position_id[tf.newaxis, :], token_id[tf.newaxis, :],
                    attention_mask_id[tf.newaxis, :]))  # add batch axis
    np_y_pred = y_pred[0].numpy()[0]  # 去掉 batch 维
    np_y_pred = np_y_pred[1:, 0:df_y_for_pred.shape[1]]  # 去掉 COMP_TYPE 维和 padding 的日期值
    df_y_pred = pd.DataFrame(data=np_y_pred, index=df_y_for_pred.index, columns=df_y_for_pred.columns)

    # de zscore 回原始值
    df_mean, df_std = equity_all_financial_statement_mean_and_std(tushare, symbol)
    df_y_pred_orig_val = de_zscore_to_val(df_y_pred, df_mean, df_std)

    delta_v = df_y_true_original.iloc[-1] - df_y_pred_orig_val.iloc[-1]
    delta_percentage = (df_y_true_original.iloc[-1] - df_y_pred_orig_val.iloc[-1]) / df_y_true_original.iloc[-1]

    df_pred_summary = pd.DataFrame(
        {"true_val": df_y_true_original.iloc[-1], "pred_val": df_y_pred_orig_val.iloc[-1]}).dropna()
    df_pred_summary["delta_v"] = df_pred_summary["true_val"] - df_pred_summary["pred_val"]
    df_pred_summary["delta_percentage"] = (df_pred_summary["true_val"] - df_pred_summary["pred_val"]) * 100. / \
                                          df_pred_summary["true_val"]

    df_pred_zscore = pd.DataFrame({"true_val": df_zscore.iloc[-1], "pred_val": df_y_pred.iloc[-1]}).dropna()

    print(df_pred_summary)


mongo_db_conn("intranet", db_nlp)

import pandas as pd
news_objs = NewsIndex.objects(
    from_keyword__in=SearchKeyword.objects(agent__in=AgentWithTag.objects(tags="govt_central")))
df = pd.DataFrame(data=[{"title": news.title, "pub_time": news.publish_time, "abstract": news.abstract, "url": news.url,
                         "from_kw": news.from_keyword.search_keyword} for news in news_objs])
print(df)
# print(news_objs)

# news_objs = NewsIndex.objects(from_keyword__in=SearchKeyword.objects(agent="Trump"))
# print(sorted([o.agent for o in AgentWithTag.objects(tags="govt_central")]))

