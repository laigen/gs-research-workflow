# -*- coding: UTF-8 -*-

"""
与 tensorflow dataset 数据准备相关的 Step
"""
import logging
from datetime import datetime, date
from enum import IntEnum
from typing import Optional, Callable, List, Union, Any

import numpy as np
import pandas as pd
import tensorflow as tf
from dataclasses import dataclass

from gs_research_workflow.core.gs_step import GSStep
from gs_research_workflow.core.gs_step_mapping import GlobalGSStepMapping
from gs_research_workflow.time_series.gs_steps.data_preprocess_steps import TrainValSpiltStep
from gs_research_workflow.time_series.gs_steps.func_steps import FuncStrStep
from gs_research_workflow.time_series.gs_steps.local_context_step import reg_fields_from_local_step
from gs_research_workflow.time_series.gs_steps.ts_data_steps import SymbolPeriodTSCallable, SymbolTSStep, \
    SymbolPeriodTSByLookbackCallable, SymbolMultipleTSStep

logger = logging.getLogger(__name__)


class TFDSSpecDataCodingType(IntEnum):
    """tf dataset column 只支持一些基本的 scalar 数据，如果需要额外的数据类型，则需要对数据做一些特殊的 encoding , decoding 的操作"""
    utf8_str = 1
    """使用 utf8 方式进行编码的 string """
    pd_timestamp = 2
    """pandas TimeStamp 对象"""


def tf_tensor_spec_type_encoding_decoding(coding_type: TFDSSpecDataCodingType, input: Any, is_encoding: bool = True) -> Any:
    # 把 encoding decoding 放在一个函数中，便于一起调整
    # 目前支持的 coding 类型并不多，所以先用一个函数进行 if else 处理
    if coding_type == TFDSSpecDataCodingType.utf8_str:
        if is_encoding:
            assert isinstance(input, str)
            return tf.constant(input)
        else:
            assert isinstance(input, tf.Tensor)
            assert input.dtype == tf.string
            assert len(input.shape) <= 1
            if len(input.shape) == 1:  # 有 batch 的 string
                return [x.decode("utf-8") for x in input.numpy()]
            else:
                return input.numpy().decode("utf-8")
    elif coding_type == TFDSSpecDataCodingType.pd_timestamp:
        if is_encoding:
            assert isinstance(input, pd.Timestamp)
            return input.value
        else:
            assert isinstance(input, tf.Tensor)
            assert input.dtype == tf.int64 or input.dtype == tf.uint64
            assert len(input.shape) <= 1
            if len(input.shape) == 1:  # 有 batch 的 string
                return [pd.Timestamp(x) for x in input.numpy()]
            else:
                return pd.Timestamp(input.numpy())
    else:
        raise NotImplementedError


# region TSPeriodTSByLookbackStep

@dataclass
class TSPeriodTSByLookbackStep(GSStep):
    """将一个 BeginEnd 的callable 对象，转换成 根据 Lookback Period 获取数据的 Callable"""
    symbol_period_ts_callable: SymbolPeriodTSCallable

    df_time_align: pd.DataFrame
    """用于时间对齐的df，以避免出现数据长短不一致的情况"""

    f_fill_na: Optional[Callable[[pd.DataFrame], pd.DataFrame]] = lambda x: x.fillna(method="ffill").fillna(0.)

    def __post_init__(self):
        # 避免 join 的时候， time_align 的列和原始输入的列冲突
        self.df_time_align = self.df_time_align.rename(columns={col: "__align_ts_" + col for col in self.df_time_align},
                                                       inplace=False)

    def _get_ts_by_lookback(self, symbol: str, end_t: Union[date, datetime], lookback: int):
        df_stk = self.symbol_period_ts_callable(symbol, None, None)
        if df_stk is None or df_stk.empty or len(df_stk) == 0:
            return None
        df_align = self.df_time_align[self.df_time_align.index <= end_t].iloc[-1 * lookback:]
        df = df_align.join(df_stk)
        if self.f_fill_na:
            df = self.f_fill_na(df)
        df_rlt = df[df.columns[1:]]

        return df_rlt

    @property
    def ts_callable_by_lookback(self) -> SymbolPeriodTSByLookbackCallable:
        return self._get_ts_by_lookback


GlobalGSStepMapping.register(SymbolTSStep, TSPeriodTSByLookbackStep, rule_name="period_ts_callable",
                             diff_name={
                               SymbolTSStep.symbol_period_ts_callable: TSPeriodTSByLookbackStep.symbol_period_ts_callable})

GlobalGSStepMapping.register(SymbolMultipleTSStep, TSPeriodTSByLookbackStep, rule_name="period_ts_callable",
                             diff_name={
                                 SymbolMultipleTSStep.symbol_period_ts_callable: TSPeriodTSByLookbackStep.symbol_period_ts_callable})

GlobalGSStepMapping.register(SymbolTSStep, TSPeriodTSByLookbackStep, rule_name="time_align",
                             diff_name={
                               SymbolTSStep.ts_data: TSPeriodTSByLookbackStep.df_time_align})

GlobalGSStepMapping.register(FuncStrStep, TSPeriodTSByLookbackStep, rule_name="fill_na",
                             diff_name={FuncStrStep.func: TSPeriodTSByLookbackStep.f_fill_na})

# endregion


# region TSCategoryDatasetPreparingStep

@dataclass
class TSCategoryDatasetPreparingStep(GSStep):

    category_labels: List[str]
    """所有的category的标注信息
    NOTE： 不从 df_category_symbol_by_t 拿数据，因为给的样本有可能不是覆盖所有的 category
    NOTE: 这里提供的 category 全集必须是有序的， Step 中不会对 Category 重新排序
    """

    df_category_symbol_by_t: pd.DataFrame
    x_get_data_callable: SymbolPeriodTSByLookbackCallable

    category_column_index: int = 0
    time_column_index: int = 1
    symbol_column_index: int = 2

    x_lookback_periods: int = 128
    """x回看多少期的数据"""

    export_symbol_in_ds: bool = False
    """是否将 symbol 数据在 ds 中输出"""

    export_t_in_ds: bool = False
    """是否将时间点的数据输出"""

    ds_pip: Optional[str] = None
    """在这里增加 ds_pip 对象，以便于能够直接在该类获取 num_to_category 的内容"""

    def __post_init__(self):
        self._y_category_int = {k: i for i, k in enumerate(self.category_labels, 0)}
        self._y_one_hot_matrix = np.eye(len(self._y_category_int), dtype=int)

        gen_tf_types = [tf.float32, tf.int32]
        gen_tf_shapes = [tf.TensorShape([None, None]), tf.TensorShape([self.nb_classes])]

        # 先 symbol 再 t
        if self.export_symbol_in_ds:
            gen_tf_types.append(tf.string)
            gen_tf_shapes.append(tf.TensorShape(None))  # 这里是一个 scalar，所以 shape 是 () , 而不是 ([1])

        if self.export_t_in_ds:
            gen_tf_types.append(tf.int64)  # 将时间值转成一个 int64 的表达形式
            gen_tf_shapes.append(tf.TensorShape(None))  # 这里是一个 scalar，所以 shape 是 () , 而不是 ([1])

        self._tf_ds = tf.data.Dataset.from_generator(self._ds_generator_call,
                                                     tuple(gen_tf_types),
                                                     tuple(gen_tf_shapes)
                                                     )

        if self.ds_pip:
            self._tf_ds_with_pip = FuncStrStep(func_body=self.ds_pip, single_input=self._tf_ds).func_result

    def category_to_num(self, category: str) -> int:
        return self._y_category_int.get(category, 0)

    def num_to_category(self, n: int) -> str:
        return self.category_labels[n]

    @property
    def nb_classes(self) -> int:
        return len(self._y_category_int)

    def _ds_generator_call(self):
        # col_category = self.df_category_symbol_by_t.columns[self.category_column_index]
        # col_symbol = self.df_category_symbol_by_t.columns[self.symbol_column_index]
        # col_time = self.df_category_symbol_by_t.columns[self.time_column_index]

        for index, row in self.df_category_symbol_by_t.iterrows():
            cat, t, symbol = row[self.category_column_index], row[self.time_column_index], row[self.symbol_column_index]
            df_x = self.x_get_data_callable(symbol, t, self.x_lookback_periods)
            if df_x is None:
                continue
            data_to_yield = [df_x.to_numpy(), self._y_one_hot_matrix[self.category_to_num(cat)]]
            # 先 symbol 再 t
            if self.export_symbol_in_ds:
                data_to_yield.append(
                    tf_tensor_spec_type_encoding_decoding(TFDSSpecDataCodingType.utf8_str, symbol, is_encoding=True))
            if self.export_t_in_ds:
                data_to_yield.append(
                    tf_tensor_spec_type_encoding_decoding(TFDSSpecDataCodingType.pd_timestamp, t, is_encoding=True))
            yield tuple(data_to_yield)

    @property
    def tf_ds(self) -> tf.data.Dataset:
        if self.ds_pip is None:
            return self._tf_ds
        else:
            return self._tf_ds_with_pip


GlobalGSStepMapping.register(TSPeriodTSByLookbackStep, TSCategoryDatasetPreparingStep, diff_name={
    TSPeriodTSByLookbackStep.ts_callable_by_lookback: TSCategoryDatasetPreparingStep.x_get_data_callable})

GlobalGSStepMapping.register(SymbolTSStep, TSCategoryDatasetPreparingStep, diff_name={
    SymbolTSStep.ts_data: TSCategoryDatasetPreparingStep.df_category_symbol_by_t})

GlobalGSStepMapping.register(FuncStrStep, TSCategoryDatasetPreparingStep, diff_name={
    FuncStrStep.func_result: TSCategoryDatasetPreparingStep.df_category_symbol_by_t})

GlobalGSStepMapping.register(TrainValSpiltStep, TSCategoryDatasetPreparingStep, "train_set", diff_name={
    TrainValSpiltStep.train_set: TSCategoryDatasetPreparingStep.df_category_symbol_by_t})

GlobalGSStepMapping.register(TrainValSpiltStep, TSCategoryDatasetPreparingStep, "val_set", diff_name={
    TrainValSpiltStep.val_set: TSCategoryDatasetPreparingStep.df_category_symbol_by_t})

GlobalGSStepMapping.register(TSCategoryDatasetPreparingStep, FuncStrStep, rule_name="ds_pip", diff_name={
    TSCategoryDatasetPreparingStep.tf_ds: FuncStrStep.single_input})

reg_fields_from_local_step(TSCategoryDatasetPreparingStep)


# endregion


if __name__ == "__main__":
    import json
    symbol_ts_step = SymbolTSStep(api="index_weight",
                                  symbols={"BigCap": "000043.SH", "MidCap": "000044.SH", "SmlCap": "000045.SH"},
                                  cols=["con_code"])
    f_after_split_step = FuncStrStep(
        func_body="lambda df : {t: set(df[df.index == t][df.columns[0]].tolist()) for t in df.index.unique()}")
    train_val_set = TrainValSpiltStep(_input_steps=[symbol_ts_step, f_after_split_step], split_ratio=0.85,
                                      max_test_items_count=10)
    time_align_step = SymbolTSStep(api="index_quotation_daily", symbols="000001.SH", cols=["close"])
    x_ts_data_step = SymbolTSStep(api="equity_backward_adjust_daily",
                                  cols=["open", "high", "low", "close", "pre_close", "change", "pct_chg", "vol", "amount"])

    train_val_tf_ds_step = DELTSCategoryMultiPeriodDatasetStep(
        _input_steps=[train_val_set, (time_align_step, "time_align"), (x_ts_data_step, "x_data_callable")])

    print(json.dumps(train_val_tf_ds_step.get_init_value_dict(True)))

    for ds in train_val_tf_ds_step.train_tf_ds.take(1):
        print(ds)

