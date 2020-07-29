# -*- coding: UTF-8 -*-

"""GS 自定义的 loss functinons"""
import copy
from typing import Mapping, Any

import tensorflow as tf

from gs_research_workflow.time_series.gs_steps.tf_dataset_steps.data_const import TS_NAN_VAL, PADDING_VAL, TS_UNMASK_VAL
from gs_research_workflow.time_series.gs_steps.tf_ds_for_financial_statement import FinancialStatementCSBertConst
from tensorflow.python.framework import ops
from tensorflow.python.keras import backend as K
from tensorflow.python.ops import math_ops
import numpy as np


def _cs_bert_pred_true_preprocess(y_true, y_pred):
    y_pred = ops.convert_to_tensor(y_pred)
    # 不知道什么原因，一些 pred 值会出现 NaN ， 这里做数值替换
    # y_pred = tf.where(tf.math.is_nan(y_pred), FinancialStatementCSBertConst.NAN_VAL ,y_pred)
    y_true = math_ops.cast(y_true, y_pred.dtype)
    # y_pred 中修改 NAN 值 , 使其不影响到 mae 的准确性
    # 只有 Nan 不参与到 loss 计算
    # y_pred = tf.where(math_ops.abs(y_true - FinancialStatementCSBertConst.NAN_VAL) < 1e-9, y_true, y_pred)
    y_pred = tf.where(tf.math.equal(y_true, FinancialStatementCSBertConst.NAN_VAL), y_true, y_pred)
    # y_pred = tf.where(math_ops.abs(y_true - CLS_VAL) < 1e-9, CLS_VAL, y_pred)
    return y_true, y_pred


# @keras_export('keras.losses.gsmae')
def ts_bert_mae(y_true, y_pred):
    y_true, y_pred = _cs_bert_pred_true_preprocess(y_true, y_pred)
    rlt = K.mean(math_ops.abs(y_pred - y_true), axis=[-1, -2])
    # rlt = K.mean(math_ops.abs(y_pred - y_true), axis=[-1])
    return rlt


def ts_bert_mse(y_true, y_pred):
    y_true, y_pred = _cs_bert_pred_true_preprocess(y_true, y_pred)
    rlt = K.mean(math_ops.squared_difference(y_pred, y_true), axis=[-1, -2])
    return rlt


def _align_y_pre_process(y_true, y_pred):
    # MAE 的数据对齐到 y_true 的维度
    y_pred = ops.convert_to_tensor(y_pred)
    y_true = math_ops.cast(y_true, y_pred.dtype)  # shape [batch , all_symbols_look_period, indicators_to_pred]
    indicators_to_pred = y_true.shape[-1]
    # fit和直接 call model 的时候， y_pred 的 shape 会差一维，这里做一个兼容
    if len(y_pred.shape) == 4:
        y_pred_to_calc = y_pred[:, :, :, 0:indicators_to_pred]
    else:
        y_pred_to_calc = y_pred[:, :, 0:indicators_to_pred]
    # 把 y_true 的特殊值都标记成 None , 这样计算 mae 和 mse 时，这些 cell 将被排除
    y_true = tf.where(tf.math.equal(y_true, TS_NAN_VAL), np.nan, y_true)
    y_true = tf.where(tf.math.equal(y_true, PADDING_VAL), np.nan, y_true)
    y_true = tf.where(tf.math.equal(y_true, TS_UNMASK_VAL), np.nan, y_true)
    y_pred_to_calc = tf.where(tf.math.is_nan(y_true), np.nan, y_pred_to_calc)
    # print(f"\r\ny_true_not_non_count:{tf.math.count_nonzero(tf.where(tf.math.is_nan(y_true), 0, 1), axis=[-1, -2])}")
    # print(f"\r\ny_pred_not_non_count:{tf.math.count_nonzero(tf.where(tf.math.is_nan(y_pred_to_calc), 0, 1),axis=[-1, -2])}")
    # ---   old version   ---
    # y_pred_to_calc = tf.where(tf.math.equal(y_true, TS_NAN_VAL), y_true, y_pred_to_calc)
    # y_pred_to_calc = tf.where(tf.math.equal(y_true, PADDING_VAL), y_true, y_pred_to_calc)
    # y_pred_to_calc = tf.where(tf.math.equal(y_true, TS_UNMASK_VAL), y_true, y_pred_to_calc)
    # --- end old version ----
    return y_true, y_pred_to_calc


def mae_align_to_y_true(y_true, y_pred):
    # NOTE: MAE,MSE 的计算都需要将 无效值从样本值提出后再计算
    y_true_to_calc, y_pred_to_calc = _align_y_pre_process(y_true, y_pred)
    non_zero_count = tf.math.count_nonzero(tf.where(tf.math.is_nan(y_true_to_calc), 0, 1), axis=[-1, -2],
                                           dtype=tf.dtypes.float32)
    y_true_nan_to_zero = tf.where(tf.math.is_nan(y_true_to_calc), 0., y_true_to_calc)
    y_pred_nan_to_zero = tf.where(tf.math.is_nan(y_pred_to_calc), 0., y_pred_to_calc)
    mae = tf.math.divide(tf.math.reduce_sum(tf.math.abs(y_pred_nan_to_zero - y_true_nan_to_zero), axis=[-1, -2]),
                         non_zero_count)

    # -- old version --
    # rlt = K.mean(math_ops.abs(y_pred_to_calc - y_true_to_calc), axis=[-1, -2])

    return mae


def mse_align_to_y_true(y_true, y_pred):
    y_true_to_calc, y_pred_to_calc = _align_y_pre_process(y_true, y_pred)
    non_zero_count = tf.math.count_nonzero(tf.where(tf.math.is_nan(y_true_to_calc), 0, 1), axis=[-1, -2],
                                           dtype=tf.dtypes.float32)
    y_true_nan_to_zero = tf.where(tf.math.is_nan(y_true_to_calc), 0., y_true_to_calc)
    y_pred_nan_to_zero = tf.where(tf.math.is_nan(y_pred_to_calc), 0., y_pred_to_calc)

    squared_difference = math_ops.squared_difference(y_pred_nan_to_zero, y_true_nan_to_zero)
    mse = tf.math.divide(tf.math.reduce_sum(squared_difference, axis=[-1, -2]),non_zero_count)

    # old version
    # rlt = K.mean(math_ops.squared_difference(y_pred_to_calc, y_true_to_calc), axis=[-1, -2])
    return mse


SPEC_METRICS_FUNC = {
    "ts_bert_mae": ts_bert_mae,
    "ts_bert_mse": ts_bert_mse,
    "mae_align_to_y_true": mae_align_to_y_true,
    "mse_align_to_y_true": mse_align_to_y_true
}


def process_compile_loss_kwargs(compile_kwargs: Mapping[str, Any]) -> Mapping[str, Any]:
    """用于转换一些特定的 loss 参数为 function """
    # 一些自定义的 loss function
    ret_compile_kwargs = copy.deepcopy(compile_kwargs)
    if "loss" in ret_compile_kwargs:
        if ret_compile_kwargs["loss"] in SPEC_METRICS_FUNC:
            ret_compile_kwargs["loss"] = SPEC_METRICS_FUNC[compile_kwargs["loss"]]
    if "metrics" in ret_compile_kwargs:
        ls_new_metrics = []
        for metrics in ret_compile_kwargs["metrics"]:
            if metrics in SPEC_METRICS_FUNC:
                ls_new_metrics.append(SPEC_METRICS_FUNC[metrics])
            else:
                ls_new_metrics.append(metrics)
        ret_compile_kwargs["metrics"] = ls_new_metrics
    return ret_compile_kwargs
