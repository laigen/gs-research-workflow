# -*- coding: UTF-8 -*-

"""
执行 prediction 的 步骤
"""

import logging
from datetime import datetime

from functools import partial

import pandas as pd
import os

from gs_research_workflow.auto_ml.prediction.pred_detail_post_process import TushareSymbolToName, CategoryIntToLabel
from gs_research_workflow.common.path_utilities import get_prediction_output_path
from gs_research_workflow.time_series.data.tushare_wrapper import TuShareProData
from gs_research_workflow.time_series.gs_steps.tf_dataset_step import TFDSSpecDataCodingType

from gs_research_workflow.time_series.gs_steps.model_steps import ModelPathGeneratorStep, ModelWithWeightSaveLoadStep, \
    AdditionalColumnInDS

from gs_research_workflow.core.gs_step import create_step_by_dict

from gs_research_workflow.common.serialization_utilities import load_mapping_from_file

logger = logging.getLogger(__name__)


def run_category_prediction(model_name: str, model_inst_gid: str, pred_ds_cfg_path: str, pred_name: str) -> pd.DataFrame:
    """ load model 并且执行 Prediction 的操作 """
    assert os.path.isfile(pred_ds_cfg_path), logger.error(f" cfg file {pred_ds_cfg_path} is not existed!")
    pred_ds_workflow_cfg, pred_ds_workflow_context = load_mapping_from_file(pred_ds_cfg_path)
    pred_ds = create_step_by_dict(pred_ds_workflow_cfg, pred_ds_workflow_context)

    model_inst_path = ModelPathGeneratorStep(model_name, model_inst_gid)
    model_with_weight_step = ModelWithWeightSaveLoadStep(_input_steps=[model_inst_path])
    # NOTE: 这里 predict 的 Input parameter 暂时先 hardcode， 以后考虑做到 Prediction 的 workflow 的其他参数项中
    df = model_with_weight_step.predict(pred_ds.tf_ds, y_true_col_index=1,
                                        additional_cols=[
                                            AdditionalColumnInDS(2, "symbol", TFDSSpecDataCodingType.utf8_str),
                                            AdditionalColumnInDS(3, "t", TFDSSpecDataCodingType.pd_timestamp)])

    #叠加 额外的辅助列
    from gs_research_workflow.common.path_utilities import _is_colab_env
    tushare = TuShareProData(use_l3_cache=_is_colab_env())
    symbol_info_lookup = TushareSymbolToName(tushare)
    df["symbol_name"] = df.apply(partial(symbol_info_lookup, "name", "symbol"), axis=1)

    cat_label_mapping = CategoryIntToLabel(pred_ds)
    df["y_true_label"] = df.apply(partial(cat_label_mapping, "y_true"), axis=1)
    df["y_pred_label"] = df.apply(partial(cat_label_mapping, "y_pred"), axis=1)

    csv_path = os.path.join(get_prediction_output_path(model_name, pred_name),
                            datetime.now().strftime("%Y%m%d_%H%M%S") + ".csv")

    df.to_csv(csv_path, header=True, index=True, encoding="utf-8-sig", quotechar="\"")
    return df


if __name__ == "__main__":
    cfg_path = os.path.join(os.path.dirname(__file__), "../..",
                                    "samples/workflow_cfg/category_prediction_ds_workflow_v1.yml")
    from gs_research_workflow.time_series.models.inception_time import InceptionTime
    # UUID="808CCED2DF57AE1BC7030C9B57F9A23A" for debug-73
    df = run_category_prediction(InceptionTime.__name__, "F24E10E3C3C556FC3FDC0C4B18EFA3C5", cfg_path, "SSHMarketCap")
    print(df)
