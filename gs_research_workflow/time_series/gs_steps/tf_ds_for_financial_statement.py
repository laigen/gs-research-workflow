# -*- coding: UTF-8 -*-

"""
适用于产生 financial statement 的 tf ds steps
"""
import functools
import logging
import random
from datetime import date
from typing import Optional

import pandas as pd
from dataclasses import dataclass

from gs_research_workflow.core.gs_step_mapping import GlobalGSStepMapping
from gs_research_workflow.time_series.data.utilities import de_zscore_to_val

from gs_research_workflow.time_series.gs_steps.func_steps import FuncStrStep

from gs_research_workflow.time_series.data.predefined_equity_apis import equity_all_financial_statement_zscore, \
    equity_comp_type, equity_all_financial_statement_mean_and_std, equity_all_financial_statement_by_enddate

from gs_research_workflow.common.path_utilities import _is_colab_env
from gs_research_workflow.common.serialization_utilities import cls_to_str
from gs_research_workflow.core.gs_step import GSStep
from gs_research_workflow.time_series.data.tushare_wrapper import TuShareProData
from gs_research_workflow.time_series.gs_steps.tf_dataset_steps.data_const import TS_NAN_VAL, TS_MASK_VAL
from gs_research_workflow.time_series.gs_steps.ts_data_steps import SDKWrapperContainer
import tensorflow as tf
import numpy as np

logger = logging.getLogger(__name__)


@dataclass
class ChnEquityInputStep(GSStep):
    evaluate_items_count: int = 100
    """预留多少个evaluate stock"""
    train_val_split_ratio: float = 0.9
    """Train 占到剩下股票的比例"""
    random_state: Optional[int] = 100

    def __post_init__(self):
        self._tushare = SDKWrapperContainer.get_sdk_by_cls_name(cls_to_str(TuShareProData),
                                                                {"use_l3_cache": _is_colab_env()})
        df_all_equities = pd.concat([self._tushare.stock_basic(exchange="SSE", cols=["ts_code", "name"]),
                                     self._tushare.stock_basic(exchange="SZSE", cols=["ts_code", "name"])])
        self._df_eval = df_all_equities.sample(self.evaluate_items_count, random_state=self.random_state,
                                               axis=0).reset_index(drop=True)
        df_remain = df_all_equities[~df_all_equities["ts_code"].isin(self._df_eval["ts_code"].to_list())]
        self._df_train = df_remain.sample(frac=self.train_val_split_ratio, random_state=self.random_state, axis=0).reset_index(drop=True)
        self._df_val = df_remain[~df_remain["ts_code"].isin(self._df_train["ts_code"].to_list())].reset_index(drop=True)

    @property
    def train_items(self) -> pd.DataFrame:
        return self._df_train

    @property
    def val_items(self) -> pd.DataFrame:
        return self._df_val

    @property
    def eval_items(self) -> pd.DataFrame:
        return self._df_eval


class FinancialStatementCSBertConst:
    """财务数据Bert的一些常数"""
    MAX_CS_PERIOD_LENGTH: int = 4 * 5 + 1
    """最大的传入CS的时间跨度周期， 5年季报 + 1 CLS Head """

    NAN_VAL: float = TS_NAN_VAL
    """NAN不参与 loss 计算，具体的取值应该不会有太大的影响"""

    MASK_VAL: float = TS_MASK_VAL
    """NOTE: mask 的取值，对 loss 的影响差别不大"""

    FIN_STATEMENT_INDICATORS_COUNT: int = 276  # NOTE: 必须是 num_head_counts(=6 or 12) 的整数倍，目前已有的财务指标是274项，补充两个 NONE 指标


@dataclass
class FinancialStatementCSMaskedTFDatasetStep(GSStep):
    """Financial Statement 进行 CS Mask 的步骤"""

    df_equities: pd.DataFrame
    """ 股票清单， col[0] 为 symbol , col[1] 为 name """

    ds_pip: Optional[str] = None
    """在这里增加 ds_pip 对象"""

    MAX_PERIOD_LENGTH: int = 48
    """最多返回12年48期的季度报表数据"""
    MIN_PERIOD_LENGTH: int = 12
    """最少需要返回3年"""

    def __post_init__(self):
        self._tushare = SDKWrapperContainer.get_sdk_by_cls_name(cls_to_str(TuShareProData),
                                                                {"use_l3_cache": _is_colab_env()})

        self._tf_ds = tf.data.Dataset.from_generator(self._ds_generator_call,
                                                     output_types=(
                                                         (tf.float32, tf.int32, tf.int32, tf.int32),
                                                         tf.float32),
                                                     output_shapes=(
                                                         (
                                                             # input_ids(with mask)
                                                             tf.TensorShape(
                                                                 [FinancialStatementCSBertConst.MAX_CS_PERIOD_LENGTH,
                                                                  FinancialStatementCSBertConst.FIN_STATEMENT_INDICATORS_COUNT]),
                                                             # position_ids
                                                             tf.TensorShape(
                                                                 [FinancialStatementCSBertConst.MAX_CS_PERIOD_LENGTH]),
                                                             # token_ids
                                                             tf.TensorShape(
                                                                 [FinancialStatementCSBertConst.MAX_CS_PERIOD_LENGTH]),
                                                             # attention_mask
                                                             tf.TensorShape(
                                                                 [FinancialStatementCSBertConst.MAX_CS_PERIOD_LENGTH])
                                                         ),

                                                         # y_true
                                                         tf.TensorShape(
                                                             [FinancialStatementCSBertConst.MAX_CS_PERIOD_LENGTH,
                                                              FinancialStatementCSBertConst.FIN_STATEMENT_INDICATORS_COUNT]),
                                                        )
                                                     )
        if self.ds_pip:
            self._tf_ds_with_pip = FuncStrStep(func_body=self.ds_pip, single_input=self._tf_ds).func_result

        self._f_financial_statement = functools.lru_cache(maxsize=2500)(
            functools.partial(equity_all_financial_statement_zscore, tushare_sdk=self._tushare,
                              mean_base_t=None, start_end_period=(date(2008, 1, 1), date(2019, 12, 31)),
                              ret_mean_and_std=True))
        self._f_comp_type = functools.lru_cache(maxsize=2500)(
            functools.partial(equity_comp_type, tushare_sdk=self._tushare))

    @staticmethod
    def _df_column_padding(df: pd.DataFrame, col_length: int = FinancialStatementCSBertConst.FIN_STATEMENT_INDICATORS_COUNT,
                           padding_fill_val: float = FinancialStatementCSBertConst.NAN_VAL):
        col_count_delta = col_length - df.shape[1]
        if col_count_delta <= 0:
            return df
        for i in range(col_count_delta):
            df[f"padding_{i}"] = padding_fill_val
        return df

    @staticmethod
    def _series_column_padding(series: pd.Series,
                               col_length: int = FinancialStatementCSBertConst.FIN_STATEMENT_INDICATORS_COUNT,
                               padding_fill_val: float = FinancialStatementCSBertConst.NAN_VAL):
        col_count_delta = col_length - len(series)
        if col_count_delta <= 0:
            return series

        for i in range(col_count_delta):
            series[f"padding_{i}"] = padding_fill_val
        return series

    @staticmethod
    def df_to_model_input(df_zscore_orig: pd.DataFrame, comp_type: int, series_mask: pd.Series,
                          output_y_true: bool = True, b_mask_last_slice: bool = True, b_append_pred: bool = False):
        """
        将一个 dataframe 对象整理成 bert model 需要的输入格式

        Parameters
        ----------
        df_zscore_orig
            已经 zscore 处理过的，并且 period 也已经 slice 过的 dataframe 对象

        series_mask
            用于填写 mask 的数据对应值，每列的 mask 值是不同的

        comp_type
            公司类型，使用 tushare中的原始值 ， 1一般工商业 2银行 3保险 4证券

        output_y_true
            是否输出 y_true

        b_mask_last_slice
            是否 把最后一期进行 mask ， 如果为 None ， 则扩展一期数据让 model 进行预测未公布的数据

        b_append_pred
            最后增加一期数据 （masked） ， 专门用于预测尚未公布的财务数据()

        Returns
        -------
            (input_ids, position_id,token_id,attention_mask_id) , (y_true_zscore, y_true_flag)

        """
        # NOTE: 暂时先去掉，不支持 comp_type，以免因为 comp_type 引起 loss 增加
        # comp_type = 0
        # comp_type += 5  # 公司类型从 6 开始编码，以避开正常的数据的 在score 值

        df_zscore_orig = df_zscore_orig.copy(deep=True)

        # padding 到能够能够被 model 所 fit 的状态(目前是 276 个，这样 head_num 可以取 12 或者 6)
        df_zscore_orig = FinancialStatementCSMaskedTFDatasetStep._df_column_padding(df_zscore_orig)

        df_masked = df_zscore_orig.copy(deep=True)

        if b_mask_last_slice:
            if series_mask is None:
                df_masked.iloc[-1, :] = FinancialStatementCSBertConst.MASK_VAL  # 固定以最后一期作为 Mask ，以训练 model 的预测能力
            else:
                df_masked.iloc[-1, :] = series_mask

        df_masked.fillna(FinancialStatementCSBertConst.NAN_VAL, inplace=True)
        # NOTE： series_mask 里可能会有 None 值，所以必须在这里进行 fillna
        df_zscore_orig.fillna(FinancialStatementCSBertConst.NAN_VAL, inplace=True)

        if b_append_pred:
            # TODO: 增加一期未公布的数据作为 MASK 的内容，让 model 进行预测
            raise NotImplementedError

        # assert df_masked.isnull().sum().sum() == 0
        # assert df_zscore_orig.isnull().sum().sum() == 0

        valid_cs_items = df_masked.shape[0]

        # 拼输入的 tensor
        cs_length_to_padding = FinancialStatementCSBertConst.MAX_CS_PERIOD_LENGTH - valid_cs_items - 1  # 需要在最后补充多少期的数据
        ls_input_tensor = [
            # 第一层切片是 comp_type
            tf.constant(comp_type, shape=(1, FinancialStatementCSBertConst.FIN_STATEMENT_INDICATORS_COUNT),
                        dtype=tf.float32),
            tf.convert_to_tensor(df_masked.to_numpy(), dtype=tf.float32)]
        if output_y_true:
            y_true_input_tensors = [
                tf.constant(comp_type, shape=(1, FinancialStatementCSBertConst.FIN_STATEMENT_INDICATORS_COUNT),
                            dtype=tf.float32),
                tf.convert_to_tensor(df_zscore_orig.to_numpy(), dtype=tf.float32)]

        ls_position_id = [0] + [int(t.month / 3) for t in df_masked.index]
        ls_token_id = [0] + [int(comp_type)] * len(df_masked.index.to_list())
        attention_mask = [1] * len(ls_token_id)
        if cs_length_to_padding > 0:
            ls_input_tensor.append(
                tf.constant(FinancialStatementCSBertConst.NAN_VAL,
                            shape=(cs_length_to_padding, FinancialStatementCSBertConst.FIN_STATEMENT_INDICATORS_COUNT),
                            dtype=tf.float32))
            if output_y_true:
                y_true_input_tensors.append(tf.constant(FinancialStatementCSBertConst.NAN_VAL,
                                                        shape=(cs_length_to_padding,
                                                               FinancialStatementCSBertConst.FIN_STATEMENT_INDICATORS_COUNT),
                                                        dtype=tf.float32))
            ls_position_id += [0] * cs_length_to_padding
            ls_token_id += [0] * cs_length_to_padding
            attention_mask += [0] * cs_length_to_padding
        input_ids = tf.concat(ls_input_tensor, axis=0)
        position_id = tf.convert_to_tensor(ls_position_id, dtype=tf.int32)
        token_id = tf.convert_to_tensor(ls_token_id, dtype=tf.int32)
        attention_mask_id = tf.convert_to_tensor(attention_mask, dtype=tf.int32)
        if output_y_true:
            y_true = tf.concat(y_true_input_tensors, axis=0)

        # for check none value in input
        # assert np.count_nonzero(np.isnan(input_ids.numpy())) == 0
        # assert np.count_nonzero(np.isnan(position_id.numpy())) == 0
        # assert np.count_nonzero(np.isnan(token_id.numpy())) == 0
        # assert np.count_nonzero(np.isnan(attention_mask_id.numpy())) == 0
        # assert np.count_nonzero(np.isnan(y_true.numpy())) == 0

        if output_y_true:
            return (input_ids, position_id, token_id, attention_mask_id), y_true
        else:
            return input_ids, position_id, token_id, attention_mask_id

    def _ds_generator_call(self):
        for row_num, row in self.df_equities.iterrows():
            symbol = row[0]
            stk_name = row[1]
            df_orig_zscore, series_mean, series_std = self._f_financial_statement(symbol=symbol)
            if df_orig_zscore is None:
                continue
            # to be discussed : 可能改成 10 std 的值作为 mask
            # ALERT 先不用可变数值填充 mask , pred 的值会出现 NaN ，具体原因未知
            # serise_mask = (0.-series_mean)/series_std
            serise_mask = 100.0 * series_std
            # # 增加 padding
            serise_mask = FinancialStatementCSMaskedTFDatasetStep._series_column_padding(serise_mask)

            # 可能是新上市的股票，数据跨度不够，无法加入到 dataset
            reports_count = df_orig_zscore.shape[0]
            if reports_count < self.MIN_PERIOD_LENGTH:
                continue
            comp_type = self._f_comp_type(symbol=symbol)

            # comp_type += 5 # 公司类型从 6 开始编码，以避开正常的数据， 6一般工商业 7银行 8保险 9证券
            # padding 到能够能够被 model 所 fit 的状态(目前是 276 个，这样 head_num 可以取 12 或者 6)
            # df_orig = FinancialStatementCSMaskedTFDatasetStep._df_column_padding(df_orig)
            # df_orig.fillna(FinancialStatementCSBertConst.NAN_VAL, inplace=True)

            # 每个股票，都有 50% 的概率将某一期的数据进行 mask
            ls_idx_to_mask = random.sample(range(self.MIN_PERIOD_LENGTH - 1, reports_count),
                                           max(int((reports_count - self.MIN_PERIOD_LENGTH) / 2), 1))
            # print(f"{row_num}:{symbol}-{stk_name} choice {ls_idx_to_mask}")
            for idx_to_mask in ls_idx_to_mask:
                start_idx = max(0, idx_to_mask - 5 * 4 + 1)  # 最多送5年的数据进行预测，并且 Mask 的数据一定送进去的最后一期数据
                start_t = df_orig_zscore.index[start_idx]
                end_t = df_orig_zscore.index[idx_to_mask]

                df_orig_slice = df_orig_zscore.iloc[start_idx:idx_to_mask + 1][:]
                (input_ids, position_id, token_id,
                 attention_mask_id), y_true = FinancialStatementCSMaskedTFDatasetStep.df_to_model_input(
                    df_orig_slice, comp_type=comp_type, series_mask= None , # serise_mask, # ALERT: 暂时不允许传入 +N std 否则 predict 的结果会出现 None
                    output_y_true=True,
                    b_mask_last_slice=True,
                    b_append_pred=False)

                # print(f"\t {start_t} - {end_t} - {idx_to_mask} - {start_idx}")
                yield (input_ids, position_id, token_id, attention_mask_id), y_true
                # return for debug
                # return (input_ids, position_id, token_id, attention_mask_id), y_true

    @property
    def tf_ds(self) -> tf.data.Dataset:
        if self.ds_pip is None:
            return self._tf_ds
        else:
            return self._tf_ds_with_pip


GlobalGSStepMapping.register(ChnEquityInputStep, FinancialStatementCSMaskedTFDatasetStep, diff_name={
    ChnEquityInputStep.train_items: FinancialStatementCSMaskedTFDatasetStep.df_equities}, rule_name="train")

GlobalGSStepMapping.register(ChnEquityInputStep, FinancialStatementCSMaskedTFDatasetStep, diff_name={
    ChnEquityInputStep.val_items: FinancialStatementCSMaskedTFDatasetStep.df_equities}, rule_name="validation")

GlobalGSStepMapping.register(ChnEquityInputStep, FinancialStatementCSMaskedTFDatasetStep, diff_name={
    ChnEquityInputStep.eval_items: FinancialStatementCSMaskedTFDatasetStep.df_equities}, rule_name="evaluate")

if __name__ == "__main__":
    def cs_financial_statement_model_evaluate():
        from gs_research_workflow.time_series.models.ts_bert import TSBertForMaskedCS
        from gs_research_workflow.time_series.gs_steps.model_steps import TFModelStep

        # 显示所有列
        pd.set_option('display.max_columns', None)
        # 显示所有行
        pd.set_option('display.max_rows', None)
        # 设置value的显示长度为100，默认为50
        pd.set_option('max_colwidth', 80)

        # stks = ChnEquityInputStep()
        # tf_ds_step = FinancialStatementCSMaskedTFDatasetStep(df_equities=stks.train_items,
        #                                                      ds_pip="lambda ds: ds.repeat().batch(20)")
        # tf_ds_step._ds_generator_call()
        # for ele in tf_ds_step.tf_ds.take(10):
        #     print(ele)
            # y = model(ele[0])
            # loss = gs_mean_absolute_error(ele[1], y)
            # print(loss)
        symbol = "600315.SH"
        tushare = TuShareProData(use_l3_cache=True)

        df_zscore = equity_all_financial_statement_zscore(tushare, symbol)
        comp_type = equity_comp_type(tushare, symbol)

        df_y_for_pred = df_zscore.iloc[-20:][:]
        df_y_true_original = equity_all_financial_statement_by_enddate(tushare, symbol)[-20:][:]
        input_ids, position_id, token_id, attention_mask_id = FinancialStatementCSMaskedTFDatasetStep.df_to_model_input(
            df_y_for_pred, comp_type, False, True, False)
        # load model
        # model_hp = TFModelStep(model_cls_str=cls_to_str(TSBertForMaskedCS),
        #                        model_hp=TSBertForMaskedCS.HP(hidden_size=276, num_attention_heads=6, num_hidden_layers=10))
        model_hp = TFModelStep(model_cls_str=cls_to_str(TSBertForMaskedCS),
                               model_hp=TSBertForMaskedCS.HP(hidden_size=276, num_attention_heads=12))

        checkpoint_path = model_hp.check_point_path
        model = TSBertForMaskedCS.from_pre_saved(checkpoint_path)
        # add batch axis
        y_pred = model((input_ids[tf.newaxis, :], position_id[tf.newaxis, :], token_id[tf.newaxis, :],
                        attention_mask_id[tf.newaxis, :]))
        np_y_pred = y_pred[0].numpy()[0]  # 去掉 batch 维
        np_y_pred = np_y_pred[1:, 0:df_y_for_pred.shape[1]]  # 去掉 COMP_TYPE 维和 padding 的日期值
        df_y_pred = pd.DataFrame(data=np_y_pred,index=df_y_for_pred.index, columns=df_y_for_pred.columns)

        # de zscore 回原始值
        df_mean, df_std = equity_all_financial_statement_mean_and_std(tushare, symbol)
        df_y_pred_orig_val = de_zscore_to_val(df_y_pred, df_mean, df_std)
        # df_y_pred_orig_val = (df_y_for_pred/df_y_for_pred) *df_y_pred_orig_val
        delta_v = df_y_true_original.iloc[-1] - df_y_pred_orig_val.iloc[-1]
        delta_percentage = (df_y_true_original.iloc[-1] - df_y_pred_orig_val.iloc[-1]) / df_y_true_original.iloc[-1]

        # print(f"y_true:{df_y_true_original.iloc[-1]}")
        # print(f"y_pred:{df_y_pred_orig_val.iloc[-1]}")
        # print(f"delta_v:{delta_v}")
        print(f"delta_percentage:{delta_percentage.dropna().sort_values(ascending=True)}")

        # print(y_pred.numpy()[0])
        # print(model)
        # print(f"input_ids:{input_ids}")


        # df_orig_de_zscore = de_zscore_to_val(df_zscore, df_mean, df_std)
        # df_orig = equity_all_financial_statement_by_enddate(tushare, symbol)
        # df_delta = df_orig_de_zscore - df_orig
        # print(df_delta.agg("sum", axis=0) > 0.0001)


    def change_mask_value():
        stks = ChnEquityInputStep()
        tf_ds_train = FinancialStatementCSMaskedTFDatasetStep(df_equities=stks.train_items,
                                                              ds_pip="lambda ds: ds.repeat().batch(20)")
        # tf_ds_train._ds_generator_call()
        i = 0
        for ele in tf_ds_train.tf_ds.take(100):
            print(ele[0])

    change_mask_value()
