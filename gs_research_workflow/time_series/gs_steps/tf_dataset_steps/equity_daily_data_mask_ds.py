# -*- coding: utf-8 -*-

"""
适用于 CS Bert ， daily 数据进行 mask fit bert 的 code

基本思路：
    1) 使用股票最近一年的 daily 数据(假定取 2019 整一年度的数据)作为 train set。
        indicator 包括：
            > 高开低收量额 等市场数据
            > 大单小单等资金面数据
            > PE / PB / 换手率 等日频的基本财务指标数据 <- 以上这三项，目前大约有 45 个指标
            > MA 等简单的技术指标数据（用 TA Lib）
        #indicators 必须是 attention_head_nums （通常取 12）的整数倍
        TS 数据将根据该时间跨度，都转换成 ZScore

    2） 某一支股票连续 N 天的数据，作为一句 sentence , 每一天的 cross sectional data 作为 word

    3 ) 每次选最多 M 支股票的同期数据作为 train element 。 相当于 paragraph
            股票的组合即为 I(t) ， 比如： PE 在 5-10 之间的股票
        如果 I(t) 的股票池个数 >M， 则 random choice M 个 ， 或作为多个 train element 传入
        股票之间使用代码升序，以维持稳定的序。 避免同样的 I 产生多份 Train Element

    4 ) position id 区间的相周期值

    5 ) token id 用于标识当前 train element 中第 1 ， 2 ... N 个股票

    6 ) MASK 以某个概率（15%），在被预测的 indicators 和 dervied data 之间取数据

    7) Loss Function 只计算基本市场数据(收盘价以及一些return)的 mae ， 一些衍生指标（如：MA,大小单等）的预测值不参与到 Loss 计算


TALIB 函数及参数列表： http://mrjbq7.github.io/ta-lib/funcs.html

有关 I(t) 的一些假定：
    1) I(t) 是一个 Snapshot 的概念， 送到 model 中数据， t0 ~ t  中的股票数是相同的
        如： I(t) 为 PE [3.,5.] ， lookback 选 50 ， 可能在这个周期中，部分股票是不在这个区间内的，但在 t 时刻，股票一定属于该集合
    2) I(t) 的结果是一个 DataFrame 对象，可以是某个函数的计算结果，也可以是某个数据库的查询结果
        DataFrame 的格式为 Index[date,I_name] , Column[Symbols] , list of str

"""
import logging
import json
import os
import warnings
from datetime import date, datetime, timedelta
from functools import lru_cache
from typing import Dict, List, Tuple, Union, Optional

import pandas as pd
import numpy as np
import talib
from dataclasses import dataclass
from gs_framework.gs_resource import is_colab_env
from gs_framework.utilities import get_random_int

from gs_research_workflow.common.google_drive import GoogleDriveWrapper, MIME_FOLDER, MIME_BINARY

from gs_research_workflow.common.google_oauth import get_google_token

from gs_research_workflow.core.gs_step_mapping import GlobalGSStepMapping

from gs_research_workflow.common.path_utilities import get_training_data_file_path

from gs_research_workflow.time_series.gs_steps.func_steps import FuncStrStep

from gs_research_workflow.common.serialization_utilities import cls_to_str

from gs_research_workflow.core.gs_step import GSStep

from gs_research_workflow.time_series.data.utilities import filter_df_by_t_and_cols

from gs_research_workflow.time_series.data.arctic_data_sync import TushareReqSleepController
from gs_research_workflow.time_series.data.tushare_wrapper import TuShareProData, get_month_periods, \
    get_month_periods_in_range
from gs_research_workflow.time_series.gs_steps.tf_dataset_steps.data_const import TS_MASK_VAL, PADDING_VAL, TS_NAN_VAL, \
    PADDING_POS, PADDING_TOKEN, TS_UNMASK_VAL
from gs_research_workflow.time_series.gs_steps.ts_data_steps import SymbolMultipleTSStep, SDKWrapperContainer
from gs_research_workflow.time_series.models.gs_loss_functions import mae_align_to_y_true, mse_align_to_y_true
from gs_research_workflow.time_series.models.ts_bert import TSBertForMaskedCS
from gs_research_workflow.time_series.partial_workflow.ts_portfolio_weight_steps import EQUITY_TS_FEATURES_CONTEXT
import tensorflow as tf

logger = logging.getLogger(__name__)


@dataclass
class TAColMapping:
    out_col_prefix: str
    """输出列的前缀"""

    in_col_prefix: str = ""
    """输入列的前缀，适用于一些指数的计算时，选择不同的列"""

    orig_open: str = "open"
    orig_close: str = "close"
    orig_high: str = "high"
    orig_low: str = "low"
    orig_vol: str = "vol"

    adj_factor_col: str = "adj_factor"
    """复权因子列名称"""
    adj_col_suffix: str = "_backward_adj"

    use_adj_factor: bool = True
    """使用复权因子"""

    @property
    def open(self):
        return f"{self.in_col_prefix}{self.orig_open}"

    @property
    def adj_auto_open(self):
        if self.use_adj_factor:
            return f"{self.in_col_prefix}{self.orig_open}{self.adj_col_suffix}"
        return self.open

    @property
    def high(self):
        return f"{self.in_col_prefix}{self.orig_high}"

    @property
    def adj_auto_high(self):
        if self.use_adj_factor:
            return f"{self.in_col_prefix}{self.orig_high}{self.adj_col_suffix}"
        else:
            return self.high

    @property
    def low(self):
        return f"{self.in_col_prefix}{self.orig_low}"

    @property
    def adj_auto_low(self):
        if self.use_adj_factor:
            return f"{self.in_col_prefix}{self.orig_low}{self.adj_col_suffix}"
        else:
            return self.low

    @property
    def close(self):
        return f"{self.in_col_prefix}{self.orig_close}"

    @property
    def adj_auto_close(self):
        if self.use_adj_factor:
            return f"{self.in_col_prefix}{self.orig_close}{self.adj_col_suffix}"
        else:
            return self.close

    @property
    def vol(self):
        return f"{self.in_col_prefix}{self.orig_vol}"


class StockFullyTSDataReader:
    """股票的完整 ts 数据的获取函数"""

    _global_inst = dict()

    @classmethod
    def get_global_instance(cls, start_t: date, end_t: date, use_cache: bool = False) -> 'StockFullyTSDataReader':
        """因为有 lru cache ，所以该 inst 的实例需要根据 init_key 保持全局的一份数据"""
        key = f"{start_t.strftime('%Y%m%d')}_{end_t.strftime('%Y%m%d')}_{use_cache}"
        if key in cls._global_inst:
            return cls._global_inst[key]
        else:
            cls._global_inst[key] = cls(start_t, end_t, use_cache)
            return cls._global_inst[key]

    def __init__(self, start_t: date, end_t: date, use_cache: bool = False):
        self.equity_daiy_query_step = SymbolMultipleTSStep(
            data_query_class=EQUITY_TS_FEATURES_CONTEXT["LOCAL"]["x_feature_query_class"],
            apis_and_columns=EQUITY_TS_FEATURES_CONTEXT["LOCAL"]["x_features_per_symbol"])
        self.tushare = self.equity_daiy_query_step.query_sdk
        self.start_t = start_t
        self.end_t = end_t
        self.use_cache: bool = use_cache # NOTE: 加了本地磁盘 cache 速度并没有提升，所以暂时先不使用了
        if self.use_cache:
            self.cache_path = os.path.join(get_training_data_file_path("tushare_pro", "derived_ts"),
                                           self.__class__.__name__,
                                           f"{self.start_t.strftime('%Y%m%d')}_{self.end_t.strftime('%Y%m%d')}")
            if not os.path.exists(self.cache_path):
                os.makedirs(self.cache_path)

    def cache_folder_clean_up(self):
        """ 有脚本根据需要删除缓存的文件夹 """
        import shutil
        if self.use_cache:
            shutil.rmtree(self.cache_path, True)
            os.mkdir(self.cache_path)

    def maybe_read_cache(self, symbol: str) -> Tuple[bool, Optional[pd.DataFrame]]:
        """ 读取本地的缓存文件 """
        if not self.use_cache:
            return False, None
        file_path = os.path.join(self.cache_path, symbol + ".pkl")
        if not os.path.isfile(file_path):
            return False, None
        df = pd.read_pickle(file_path, compression="gzip")
        return True, df

    def write_cache(self, symbol: str, df: pd.DataFrame):
        if not self.use_cache:
            return
        file_path = os.path.join(self.cache_path, symbol + ".pkl")
        df.to_pickle(file_path, compression="gzip", protocol=4)

    @staticmethod
    def append_ta_indicators(df: pd.DataFrame, col: TAColMapping):
        adj_factor = 1.
        if col.use_adj_factor:
            adj_factor = df[col.adj_factor_col]

        group_annually = df.groupby(pd.Grouper(freq="A"))
        group_quarterly = df.groupby(pd.Grouper(freq="Q"))
        group_monthly = df.groupby(pd.Grouper(freq="M"))

        df[f"{col.out_col_prefix}ret_YTD"] = group_annually[col.adj_auto_close].transform(
            lambda x: (x / x.iloc[0] - 1.0) * 100. if len(x) > 0 else None)
        df[f"{col.out_col_prefix}ret_QTD"] = group_quarterly[col.adj_auto_close].transform(
            lambda x: (x / x.iloc[0] - 1.0) * 100. if len(x) > 0 else None)
        df[f"{col.out_col_prefix}ret_MTD"] = group_monthly[col.adj_auto_close].transform(
            lambda x: (x / x.iloc[0] - 1.0) * 100. if len(x) > 0 else None)
        df[f"{col.out_col_prefix}ret_52weeks"] = df[col.adj_auto_close].rolling(window=244).apply(
            lambda x: (x[-1] / x[0] - 1.0) * 100., raw=False)
        df[f"{col.out_col_prefix}high_low_ret_52weeks"] = (df[col.adj_auto_close].rolling(window=244).max() / df[
            col.adj_auto_close].rolling(window=244).min() - 1.0) * 100.

        for i in [5, 20, 60]:
            df[f"{col.out_col_prefix}SMA_{i}"] = talib.SMA(df[col.adj_auto_close], timeperiod=i) / adj_factor
            df[f"{col.out_col_prefix}DEMA_{i}"] = talib.DEMA(df[col.adj_auto_close], timeperiod=i) / adj_factor
            df[f"{col.out_col_prefix}MIDPOINT_{i}"] = talib.MIDPOINT(df[col.adj_auto_close], timeperiod=i) / adj_factor
            if i <= 20:  # 该指标在 60 日的情况下，值为 NaN ， 所以去掉
                df[f"{col.out_col_prefix}T3_{i}"] = talib.T3(df[col.adj_auto_close], timeperiod=i, vfactor=0) / adj_factor
                df[f"{col.out_col_prefix}TEMA_{i}"] = talib.TEMA(df[col.adj_auto_close], timeperiod=i) / adj_factor
            df[f"{col.out_col_prefix}TRIMA_{i}"] = talib.TRIMA(df[col.adj_auto_close], timeperiod=i) / adj_factor
            df[f"{col.out_col_prefix}WMA_{i}"] = talib.WMA(df[col.adj_auto_close], timeperiod=i) / adj_factor
            df[f"{col.out_col_prefix}BETA_{i}"] = talib.BETA(df[col.adj_auto_high], df[col.adj_auto_low], timeperiod=i)
            df[f"{col.out_col_prefix}CORREL_{i}"] = talib.CORREL(df[col.adj_auto_high], df[col.adj_auto_low],
                                                                 timeperiod=i)
            df[f"{col.out_col_prefix}LINEARREG_{i}"] = talib.LINEARREG(df[col.adj_auto_close],
                                                                       timeperiod=i) / adj_factor
            df[f"{col.out_col_prefix}LINEARREG_ANGLE_{i}"] = talib.LINEARREG_ANGLE(df[col.adj_auto_close], timeperiod=i)
            df[f"{col.out_col_prefix}LINEARREG_INTERCEPT_{i}"] = talib.LINEARREG_INTERCEPT(df[col.adj_auto_close],
                                                                                           timeperiod=i) / adj_factor
            df[f"{col.out_col_prefix}LINEARREG_SLOPE_{i}"] = talib.LINEARREG_SLOPE(df[col.adj_auto_close], timeperiod=i)
            df[f"{col.out_col_prefix}STDDEV_{i}"] = talib.STDDEV(df[col.adj_auto_close], timeperiod=i, nbdev=1)
            df[f"{col.out_col_prefix}TSF_{i}"] = talib.TSF(df[col.adj_auto_close], timeperiod=i) / adj_factor
            df[f"{col.out_col_prefix}VAR_{i}"] = talib.VAR(df[col.adj_auto_close], timeperiod=i, nbdev=1)
            df[f"{col.out_col_prefix}MAX_{i}"] = talib.MAX(df[col.adj_auto_close], timeperiod=i) / adj_factor
            df[f"{col.out_col_prefix}MIN_{i}"] = talib.MIN(df[col.adj_auto_close], timeperiod=i) / adj_factor

            df[f"{col.out_col_prefix}MOM_{i}"] = talib.MOM(df[col.adj_auto_close], timeperiod=i)

        df[f"{col.out_col_prefix}BBANDS_upper"], df[f"{col.out_col_prefix}BBANDS_middle"], df[
            f"{col.out_col_prefix}BBANDS_lower"] = (v / adj_factor for v in
                                                    talib.BBANDS(df[col.adj_auto_close],
                                                                 timeperiod=5,
                                                                 nbdevup=2, nbdevdn=2, matype=0))

        df[f"{col.out_col_prefix}SAR"] = talib.SAR(high=df[col.adj_auto_high], low=df[col.adj_auto_low], acceleration=0,
                                                   maximum=0) / adj_factor

        df[f"{col.out_col_prefix}APO"] = talib.APO(df[col.adj_auto_close], fastperiod=12, slowperiod=26, matype=0)
        df[f"{col.out_col_prefix}AROON_DOWN"], df[f"{col.out_col_prefix}AROON_UP"] = (v / adj_factor for v in
                                                                                      talib.AROON(
                                                                                          high=df[col.adj_auto_high],
                                                                                          low=df[col.adj_auto_low],
                                                                                          timeperiod=14))
        df[f"{col.out_col_prefix}BOP"] = talib.BOP(open=df[col.adj_auto_open], high=df[col.adj_auto_high],
                                                   low=df[col.adj_auto_low],
                                                   close=df[col.adj_auto_close])
        df[f"{col.out_col_prefix}CCI"] = talib.CCI(high=df[col.adj_auto_high], low=df[col.adj_auto_low],
                                                   close=df[col.adj_auto_close], timeperiod=14)
        df[f"{col.out_col_prefix}CMO"] = talib.CMO(df[col.adj_auto_close], timeperiod=14)
        df[f"{col.out_col_prefix}DX"] = talib.DX(high=df[col.adj_auto_high], low=df[col.adj_auto_low],
                                                 close=df[col.adj_auto_close], timeperiod=14)

        df[f"{col.out_col_prefix}MACD"], df[f"{col.out_col_prefix}MACD_SIGNAL"], df[
            f"{col.out_col_prefix}MACD_HIST"] = talib.MACD(df[col.adj_auto_close], fastperiod=12,
                                                           slowperiod=26, signalperiod=9)

        df[f"{col.out_col_prefix}MACDEXT"], df[f"{col.out_col_prefix}MACDEXT_SIGNAL"], df[
            f"{col.out_col_prefix}MACDEXT_HIST"] = talib.MACDEXT(df[col.adj_auto_close],
                                                                 fastperiod=12,
                                                                 fastmatype=0, slowperiod=26,
                                                                 slowmatype=0,
                                                                 signalperiod=9, signalmatype=0)

        df[f"{col.out_col_prefix}MACDFIX"], df[f"{col.out_col_prefix}MACDFIX_SIGNAL"], df[
            f"{col.out_col_prefix}MACDFIX_HIST"] = talib.MACDFIX(df[col.adj_auto_close],
                                                                 signalperiod=9)

        df[f"{col.out_col_prefix}PPO"] = talib.PPO(df[col.adj_auto_close], fastperiod=12, slowperiod=26, matype=0)

        df[f"{col.out_col_prefix}SLOWK"], df[f"{col.out_col_prefix}SLOWD"] = talib.STOCH(high=df[col.adj_auto_high],
                                                                                         low=df[col.adj_auto_low],
                                                                                         close=df[col.adj_auto_close],
                                                                                         fastk_period=5, slowk_period=3,
                                                                                         slowk_matype=0, slowd_period=3,
                                                                                         slowd_matype=0)

        df[f"{col.out_col_prefix}FASTK"], df[f"{col.out_col_prefix}FASTD"] = talib.STOCHF(high=df[col.adj_auto_high],
                                                                                          low=df[col.adj_auto_low],
                                                                                          close=df[col.adj_auto_close],
                                                                                          fastk_period=5,
                                                                                          fastd_period=3,
                                                                                          fastd_matype=0)

        df[f"{col.out_col_prefix}TRIX"] = talib.TRIX(df[col.adj_auto_close], timeperiod=30)

        df[f"{col.out_col_prefix}ULTOSC"] = talib.ULTOSC(high=df[col.adj_auto_high], low=df[col.adj_auto_low],
                                                         close=df[col.adj_auto_close], timeperiod1=7, timeperiod2=14,
                                                         timeperiod3=28)

        df[f"{col.out_col_prefix}WILLR"] = talib.WILLR(high=df[col.adj_auto_high], low=df[col.adj_auto_low],
                                                       close=df[col.adj_auto_close], timeperiod=14)

        df[f"{col.out_col_prefix}AD"] = talib.AD(high=df[col.high], low=df[col.low], close=df[col.close],
                                                 volume=df[col.vol])

        df[f"{col.out_col_prefix}ADOSC"] = talib.ADOSC(high=df[col.high], low=df[col.low], close=df[col.close],
                                                       volume=df[col.vol], fastperiod=3,
                                                       slowperiod=10)

        df[f"{col.out_col_prefix}OBV"] = talib.OBV(df[col.close], df[col.vol])

        df[f"{col.out_col_prefix}TRANGE"] = talib.TRANGE(high=df[col.adj_auto_high], low=df[col.adj_auto_low],
                                                         close=df[col.adj_auto_close])

        df[f"{col.out_col_prefix}AVGPRICE"] = talib.AVGPRICE(open=df[col.adj_auto_close], high=df[col.adj_auto_high],
                                                             low=df[col.adj_auto_low],
                                                             close=df[col.adj_auto_close]) / adj_factor

        df[f"{col.out_col_prefix}MEDPRICE"] = talib.MEDPRICE(high=df[col.adj_auto_high],
                                                             low=df[col.adj_auto_low]) / adj_factor

        df[f"{col.out_col_prefix}TYPPRICE"] = talib.TYPPRICE(high=df[col.adj_auto_high], low=df[col.adj_auto_low],
                                                             close=df[col.adj_auto_close]) / adj_factor

        df[f"{col.out_col_prefix}WCLPRICE"] = talib.WCLPRICE(high=df[col.adj_auto_high], low=df[col.adj_auto_low],
                                                             close=df[col.adj_auto_close]) / adj_factor
        df[f"{col.out_col_prefix}SUB"] = talib.BETA(df[col.adj_auto_high], df[col.adj_auto_low]) / adj_factor

    # @lru_cache(maxsize=2000)  # 本地文件cache 并没有提速多少，所以还是继续使用内存 cache
    def _stk_ts_data(self, symbol: str) -> pd.DataFrame:
        f = self.equity_daiy_query_step.symbol_period_ts_callable
        df_orig = f(symbol, start_t=self.start_t, end_t=self.end_t)
        if df_orig.shape[0] == 0:  # 在区段内没有数据，不能送到 TA 中进行计算，否则会出现错误
            return None
        df_non_detect = df_orig.dropna(axis=0, how="all", subset=["close"])
        if df_non_detect.shape[0] == 0:  # 如果没有一期开盘的数据，则该股票需要被剔除，以免计算 TA 指标时发生错误
            return None

        StockFullyTSDataReader.append_ta_indicators(df_orig, col=TAColMapping(out_col_prefix="stk_"))
        return df_orig

    @lru_cache(maxsize=600)
    def _get_sw_industry_index_data(self, ind_code: str) -> pd.DataFrame:
        return self.tushare.read_derived_ts(TuShareProData.DERIVED_TS_INDUSTRY_INDEX, ind_code,
                                            start=self.start_t, end=self.end_t)

    def _stk_industry_index_data(self, symbol: str, index_lv: str) -> pd.DataFrame:
        lv_to_lib_name = {"L1": TuShareProData.DERIVED_TS_EQUITY_SW_INDUSTRY_L1,
                          "L2": TuShareProData.DERIVED_TS_EQUITY_SW_INDUSTRY_L2,
                          "L3": TuShareProData.DERIVED_TS_EQUITY_SW_INDUSTRY_L3}
        assert index_lv in lv_to_lib_name

        df_equity_to_industry_code = self.tushare.read_derived_ts(lv_to_lib_name[index_lv], symbol,
                                                                  start=self.start_t, end=self.end_t)
        if df_equity_to_industry_code is None:
            return None
        ind_codes_in_range = df_equity_to_industry_code["index_code"].unique()
        ls_df_stk_related_industry_idx = []
        for ind_code in ind_codes_in_range:
            df_ind = self._get_sw_industry_index_data(ind_code).copy(deep=True)
            idx_date_items = df_equity_to_industry_code[df_equity_to_industry_code["index_code"] == ind_code].index
            ls_df_stk_related_industry_idx.append(df_ind.loc[idx_date_items, :])
        df_stk_related_industry_idx = pd.concat(ls_df_stk_related_industry_idx, axis=0)
        df_stk_related_industry_idx.sort_index(axis=0, ascending=True, inplace=True)

        df_equity_total_mv = self.tushare.equity_basic_daily(symbol, start=self.start_t, end=self.end_t, cols=["total_mv"])
        df_stk_related_industry_idx["mv_ratio"] = df_equity_total_mv["total_mv"] / df_stk_related_industry_idx[
            "total_mv"]
        ls_columns = df_stk_related_industry_idx.columns
        col_prefix = "sw_ind_"+index_lv+"_"
        df_stk_related_industry_idx.rename(columns={col: f"{col_prefix}{col}" for col in ls_columns}, inplace=True)
        StockFullyTSDataReader.append_ta_indicators(df_stk_related_industry_idx,
                                                    col=TAColMapping(out_col_prefix=col_prefix,
                                                                     in_col_prefix=col_prefix,
                                                                     use_adj_factor=False))
        return df_stk_related_industry_idx

    @lru_cache(maxsize=3)
    def _get_mkt_index_data(self, index_symbol) -> pd.DataFrame:
        df_mkt_index = self.tushare.index_quotation_daily(symbol=index_symbol, start=self.start_t, end=self.end_t)
        ls_columns = df_mkt_index.columns
        col_prefix = "mkt_idx_"
        df_mkt_index.rename(columns={col: f"{col_prefix}{col}" for col in ls_columns}, inplace=True)
        StockFullyTSDataReader.append_ta_indicators(df_mkt_index,
                                                    col=TAColMapping(out_col_prefix=col_prefix,
                                                                     in_col_prefix=col_prefix,
                                                                     use_adj_factor=False))
        return df_mkt_index

    def _stk_mkt_index(self, symbol: str) -> pd.DataFrame:
        index_symbol = "000001.SH"
        if symbol.endswith(".SZ"):
            index_symbol = "399001.SZ"
        return self._get_mkt_index_data(index_symbol)

    def _get_industry_empty_df(self, lv: str) -> pd.DataFrame:
        df = self._stk_industry_index_data("600000.SH", lv)  # 用 600000 的申万行业指数作为空的 Dataframe
        return pd.DataFrame(index=df.index[-2:-1], columns=df.columns)

    def all_stk_ts_data(self, symbol: str) -> pd.DataFrame:
        is_cached, df_ts = self.maybe_read_cache(symbol)
        if df_ts is not None:
            return df_ts
        ls_dfs = list()
        df_orig_data = self._stk_ts_data(symbol)
        if df_orig_data is None:  # 没有有效的数据内容
            return None

        ls_dfs.append(df_orig_data)
        df_industry_l1 = self._stk_industry_index_data(symbol, "L1")
        if df_industry_l1 is None:
            df_industry_l1 = self._get_industry_empty_df("L1")
        ls_dfs.append(df_industry_l1)

        df_industry_l2 = self._stk_industry_index_data(symbol, "L2")
        if df_industry_l2 is None:
            df_industry_l2 = self._get_industry_empty_df("L2")
        ls_dfs.append(df_industry_l2)

        df_industry_l3 = self._stk_industry_index_data(symbol, "L3")
        if df_industry_l3 is None:
            df_industry_l3 = self._get_industry_empty_df("L3")
        ls_dfs.append(df_industry_l3)

        ls_dfs.append(self._stk_mkt_index(symbol).copy(deep=True))
        df_rlt = ls_dfs[0]
        for df in ls_dfs[1:]:
            df_rlt = df_rlt.join(df, how="left", rsuffix="_")
        self.write_cache(symbol, df_rlt)
        return df_rlt

    def sync_to_google_drive(self):
        """将 cache 过的 pkl 文件同步到 google drive"""
        import time
        import yaml

        # 用这个账号来同步 derived ts data，可以稀释固定账号对于google storage 的 limitation
        token = get_google_token("gs.sharefolder@gmail.com")
        gdrive = GoogleDriveWrapper(token)
        folders = self.cache_path.split(os.path.sep)[3:]
        i_existed_level = 3
        for i in range(len(folders) - i_existed_level):
            curr_folder_name = folders[i + i_existed_level]
            folder_parent = '/'.join(folders[0:i + i_existed_level])
            # print(f"{folder_parent} - {curr_folder_name}")
            exp_folder_obj = gdrive.create_or_update_file(curr_folder_name, MIME_FOLDER, folder_parent, get_only=False)

        parent_folder_obj = exp_folder_obj

        uploaded = dict()
        uploaded_saved_file_name = os.path.join(self.cache_path, "uploaded.yml")

        if os.path.isfile(uploaded_saved_file_name):
            with open(uploaded_saved_file_name, "r") as yaml_file:
                uploaded = yaml.load(yaml_file)

        for i, file_name in enumerate(os.listdir(self.cache_path)):
            if not file_name.endswith(".pkl"):
                continue
            if file_name in uploaded:
                continue
            file_obj = gdrive.query_object_by_name(file_name, parent_folder_obj.id)
            if file_obj is not None:
                uploaded[file_name] = file_obj.id
                with open(uploaded_saved_file_name, "w") as yaml_file:
                    yaml.dump(uploaded, yaml_file)
                print(f"[{i}] '{file_name}' has existed! id={file_obj.id}")
                time.sleep(0.5)
            else:
                error_flag = False
                for i_retry in range(5):
                    try:
                        file_obj = gdrive.create_or_update_file(file_name, MIME_BINARY, parent_folder_obj,
                                                                os.path.join(self.cache_path, file_name))
                        error_flag = False
                        uploaded[file_name] = file_obj.id
                        with open(uploaded_saved_file_name, "w") as yaml_file:
                            yaml.dump(uploaded, yaml_file)
                        print(f"\033[1;32;40m [{i}] '{file_name}' uploaded , id={file_obj.id}\033[0m")
                        time.sleep(get_random_int(1, 5))
                        break
                    except BrokenPipeError:
                        print(f"\033[1;31;43m {i_retry} BrokenPipeError when upload {file_name} , now retry! \033[0m")
                        error_flag = True
                        time.sleep(20. * (i_retry + 1))
                    except Exception as err:
                        print(f"\033[1;31;43m {i_retry} raise error '{err}' when upload {file_name} , now retry! \033[0m")
                        error_flag = True
                        time.sleep(30. * (i_retry + 1))

                if error_flag:
                    raise RuntimeError(f"\033[1;31;43m BrokenPipeError still exist , {file_name}\033[0m")


def calc_dfs_zscore(dict_dfs: Dict[str, pd.DataFrame]) -> Dict[str, pd.DataFrame]:
    """用整个 I 的数据一起进行 zscore 的计算"""
    ls_np = list()
    t1 = datetime.now()
    for symbol, df in dict_dfs.items():
        ls_np.append(df.to_numpy())
    t2 = datetime.now()
    np_all = np.concatenate(ls_np, axis=0)
    t3 = datetime.now()

    with warnings.catch_warnings():
        # ignore 全 nan 时的 warning
        warnings.simplefilter("ignore", category=RuntimeWarning)
        np_mean = np.nanmean(np_all, axis=0, dtype=np.float32)  # 可能会出现 nan 值，必须用 nanmean / nanstd
        try:
            np_std = np.nanstd(np_all, axis=0, dtype=np.float32, ddof=5)
            np_std = np.where(np_std == 0., np.nan, np_std)
        # 在colab 运行时，会偶尔（在 927 个 step）出现 TypeError: unsupported operand type(s) for -: 'NoneType' and 'float'
        # 但是在 debug 环境中，未发现该错误，所以先用 try catch 的方式进行保护，通过日志定位该问题
        except TypeError as err:
            logger.error(f"TypeError when calc nanstd. {err}")
            return None

    t4 = datetime.now()


    t5 = datetime.now()

    rlt_dfs = dict()
    for symbol, df in dict_dfs.items():
        # NOTE: 转到 numpy 比 在 dataframe 多次计算的性能要高
        v1 = df.to_numpy()
        v2 = (v1 - np_mean) / np_std
        rlt_dfs[symbol] = pd.DataFrame(data=v2, index=df.index, columns=df.columns)

    t6 = datetime.now()

    # print(f"t2-t1={(t2-t1).total_seconds()},t3-t2={(t3-t2).total_seconds()},t4-t3={(t4-t3).total_seconds()}，t5-t4={(t5-t4).total_seconds()},t6-t5={(t6-t5).total_seconds()}")
    return rlt_dfs


class EquityPoolGenerator:
    def __init__(self, tushare: TuShareProData):
        self.tushare = tushare
        self.__all_I_by_t: Dict[str, pd.DataFrame] = dict()

    KEY_CONCEPT: str = "concept"

    def enable_stk_concept(self, ls_end_t: List[Union[date, datetime]]):
        if EquityPoolGenerator.KEY_CONCEPT in self.__all_I_by_t:
            return
        req_controller = TushareReqSleepController(self.tushare)
        dict_all_concept_equity: Dict[str, List[str]] = dict()
        df_concept = self.tushare.concept(cols=["code", "name"])
        for idx, row in df_concept.iterrows():
            concept_code = row["code"]
            concept_name = row["name"]
            req_controller.begin_internal_check()
            dict_all_concept_equity[concept_name] = sorted(
                self.tushare.concept_detail(concept_id=concept_code)["ts_code"].unique().tolist(), reverse=False)
            req_controller.end_internal_check()

        ls_data = list()
        for end_t in ls_end_t:
            for concept_name, symbols_in_concept in dict_all_concept_equity.items():
                ls_data.append({"t": end_t, "name": concept_name, "symbols": symbols_in_concept})
        df_i_t = pd.DataFrame(data=ls_data)
        df_i_t.set_index(keys=["t", "name"], inplace=True)
        self.__all_I_by_t[EquityPoolGenerator.KEY_CONCEPT] = df_i_t

    def add_pool_by_cs_filter(self, name: str, df_cs: pd.DataFrame, cs_cond: str,
                              f_to_symbols=lambda df: df.drop(columns=df.columns).reset_index().groupby(["date"]).apply(
                                  lambda tdf: tdf.symbol.unique().tolist()).to_frame("symbols")):
        """
        添加一个以 cs 为过滤条件的 I(t)
        Parameters
        ----------
        f_to_symbols
            过滤之后调用该函数产生 symbols 的 dataframe 函数

        df_cs
            cs 的数据结果集
        name :

        df_cs ：

        cs_cond : 过滤 cs 数据的条件
            Examples `pe > 3.0 and pe < 8.0`


        Returns
        -------

        """
        if name in self.__all_I_by_t:
            return
        df_filter = df_cs.query(cs_cond)
        df_filter = f_to_symbols(df_filter)
        df_filter["name"] = name
        df_filter = df_filter.reset_index().rename(columns={"date": "t"}).set_index(keys=["t","name"])
        self.__all_I_by_t[name] = df_filter

    @property
    def pool_by_t(self) -> pd.DataFrame:
        return pd.concat(objs=[v for v in self.__all_I_by_t.values()], axis=0)


@dataclass
class IByTGeneratorStep(GSStep):
    start_t: date
    """I(t) 数据的起始时间"""

    end_t: date
    """I(t) 数据的截止时间"""

    sample_freq: str = "2w"
    """I(t) 样本的频度"""

    use_concept_blocks: bool = True
    """使用概念板块"""

    ls_i_by_condition: List[Tuple[str, str]] = None
    """ 根据 cs 的条件得到的 I(t) 对象，暂时假定 条件的数据接口来自于一个固定的 cs 获取函数
        tuple 对象为 (pool_name , pool_cs_condition) 
    """

    evaluate_items_count: int = 20
    """预留多少个evaluate stock"""
    train_val_split_ratio: float = 0.9
    """Train 占到剩下股票的比例"""
    random_state: Optional[int] = 100

    def __post_init__(self):
        # 使用全局的 tushare api 对象
        self._tushare = SDKWrapperContainer.get_sdk_by_cls_name(cls_to_str(TuShareProData),
                                                                {"use_l3_cache": False})
        self.i_t_gen = EquityPoolGenerator(self.tushare)
        # 得到 I(t) 的时间切片。 用 上证综指的 index time 作为标尺进行 resample ，将调频后的时间点与其对齐
        # NOTE 目前使用期初时间点，改成期末只要把 first() 改为 last() 即可
        self.ls_pool_t = [d.date() for d in
                          self._tushare.index_quotation_daily("000001.SH", start=self.start_t, end=self.end_t,
                                                             cols=["close"]).reset_index().resample(self.sample_freq,
                                                                                                    on="date").first().dropna().reset_index(
                              drop=True).set_index(keys=["date"]).index.tolist()]
        if self.use_concept_blocks:
            self.i_t_gen.enable_stk_concept(self.ls_pool_t)
        # 暂时先用一个固定的 cs 数据获取函数，后续这个函数可以从外部传入
        f_cs_data = lambda ls_t: self._tushare.cs_equity_basic_daily(by_dates=ls_t)
        if self.ls_i_by_condition:
            for (i_pool_name, i_pool_cond) in self.ls_i_by_condition:
                df_cs = f_cs_data(self.ls_pool_t)
                self.i_t_gen.add_pool_by_cs_filter(i_pool_name, df_cs, i_pool_cond)

        # 分 eval , train , validation
        self._df_eval = self.pool_by_t.sample(self.evaluate_items_count, random_state=self.random_state,
                                              axis=0)
        df_remain = self.pool_by_t[~self.pool_by_t.index.isin(self._df_eval.index)]
        self._df_train = df_remain.sample(frac=self.train_val_split_ratio, random_state=self.random_state, axis=0)
        self._df_val = df_remain[~df_remain.index.isin(self._df_train.index)]

    @property
    def pool_by_t(self) -> pd.DataFrame:
        # 暂时先返回所有的内容，后续再考虑根据 train , val 进行 split
        # 对数据先做一从 shuffle
        if hasattr(self, "_pool_by_t"):
            return self._pool_by_t
        else:
            self._pool_by_t = self.i_t_gen.pool_by_t.sample(frac=1., random_state=self.random_state)
            return self._pool_by_t

    @property
    def tushare(self) -> TuShareProData:
        return self._tushare

    @property
    def train_items(self) -> pd.DataFrame:
        return self._df_train

    @property
    def val_items(self) -> pd.DataFrame:
        return self._df_val

    @property
    def eval_items(self) -> pd.DataFrame:
        return self._df_eval


@dataclass
class EquityPoolTSDatasetStep(GSStep):
    df_i_by_t: pd.DataFrame
    """I(t) 的数据对象， index 为 [t,name] , column 为 [symbols]"""

    i_start_t: date
    """i选择的开始时间"""

    i_end_t: date
    """i选择的结束时间"""

    ds_pip: Optional[str] = None
    """在这里增加 ds_pip 对象"""

    only_mask_val_in_y_true: bool = True

    mask_ratio: float = 0.15  # 有多少比率的数据被 mask 掉了

    # COLS_TO_PREDICT = ["close", "pct_chg", "stk_ret_YTD", "stk_ret_QTD", "stk_ret_MTD", "stk_ret_52weeks",
    #                    "stk_high_low_ret_52weeks"]
    COLS_TO_PREDICT = ["pct_chg"]  # 只预测 mask 掉的涨跌幅数据
    """需要用作被预测的列，固定在开始位置的列，以便于标记 Mask 以及只针对于这部分列计算 loss"""

    COLS_ALL_TA = [  # ---新增加的一些需要去掉的指标
                    'open', 'high', 'low', 'close', 'change',
                    'open_backward_adj', 'high_backward_adj', 'low_backward_adj', 'close_backward_adj', 'change_backward_adj',
                    'pct_chg_backward_adj',
                    'sw_ind_L1_open', 'sw_ind_L1_high', 'sw_ind_L1_low', 'sw_ind_L1_close', 'sw_ind_L1_change',
                    'sw_ind_L2_open', 'sw_ind_L2_high', 'sw_ind_L2_low', 'sw_ind_L2_close', 'sw_ind_L2_change',
                    'sw_ind_L3_open', 'sw_ind_L3_high', 'sw_ind_L3_low', 'sw_ind_L3_close', 'sw_ind_L3_change',
                    'mkt_idx_close', 'mkt_idx_open', 'mkt_idx_high', 'mkt_idx_low', 'mkt_idx_change',
                    # ----
                    'pre_close', 'pre_close_backward_adj', 'stk_DEMA_5', 'stk_MIDPOINT_5', 'stk_T3_5',
                   'stk_TEMA_5', 'stk_TRIMA_5', 'stk_WMA_5', 'stk_BETA_5', 'stk_CORREL_5',
                   'stk_LINEARREG_5', 'stk_LINEARREG_ANGLE_5', 'stk_LINEARREG_INTERCEPT_5',
                   'stk_LINEARREG_SLOPE_5', 'stk_STDDEV_5', 'stk_TSF_5', 'stk_VAR_5', 'stk_MAX_5',
                   'stk_MIN_5', 'stk_MOM_5', 'stk_SMA_20', 'stk_DEMA_20', 'stk_MIDPOINT_20',
                   'stk_T3_20', 'stk_TEMA_20', 'stk_TRIMA_20', 'stk_WMA_20', 'stk_BETA_20',
                   'stk_CORREL_20', 'stk_LINEARREG_20', 'stk_LINEARREG_ANGLE_20',
                   'stk_LINEARREG_INTERCEPT_20', 'stk_LINEARREG_SLOPE_20', 'stk_STDDEV_20',
                   'stk_TSF_20', 'stk_VAR_20', 'stk_MAX_20', 'stk_MIN_20', 'stk_MOM_20', 'stk_SMA_60',
                   'stk_DEMA_60', 'stk_MIDPOINT_60', 'stk_TRIMA_60', 'stk_WMA_60', 'stk_BETA_60',
                   'stk_CORREL_60', 'stk_LINEARREG_60', 'stk_LINEARREG_ANGLE_60',
                   'stk_LINEARREG_INTERCEPT_60', 'stk_LINEARREG_SLOPE_60', 'stk_STDDEV_60',
                   'stk_TSF_60', 'stk_VAR_60', 'stk_MAX_60', 'stk_MIN_60', 'stk_MOM_60',
                   'stk_BBANDS_upper', 'stk_BBANDS_middle', 'stk_BBANDS_lower', 'stk_SAR', 'stk_APO',
                   'stk_AROON_DOWN', 'stk_AROON_UP', 'stk_BOP', 'stk_CCI', 'stk_CMO', 'stk_DX',
                   'stk_MACD', 'stk_MACD_SIGNAL', 'stk_MACD_HIST', 'stk_MACDEXT', 'stk_MACDEXT_SIGNAL',
                   'stk_MACDEXT_HIST', 'stk_MACDFIX', 'stk_MACDFIX_SIGNAL', 'stk_MACDFIX_HIST',
                   'stk_PPO', 'stk_SLOWK', 'stk_SLOWD', 'stk_FASTK', 'stk_FASTD', 'stk_TRIX',
                   'stk_ULTOSC', 'stk_WILLR', 'stk_AD', 'stk_ADOSC', 'stk_OBV', 'stk_TRANGE',
                   'stk_AVGPRICE', 'stk_MEDPRICE', 'stk_TYPPRICE', 'stk_WCLPRICE', 'stk_SUB',
                   'sw_ind_L2_pre_close', 'sw_ind_L3_pre_close', 'sw_ind_L1_pre_close',
                   'sw_ind_L1_DEMA_5', 'sw_ind_L1_MIDPOINT_5', 'sw_ind_L1_T3_5', 'sw_ind_L1_TEMA_5',
                   'sw_ind_L1_TRIMA_5', 'sw_ind_L1_WMA_5', 'sw_ind_L1_BETA_5', 'sw_ind_L1_CORREL_5',
                   'sw_ind_L1_LINEARREG_5', 'sw_ind_L1_LINEARREG_ANGLE_5',
                   'sw_ind_L1_LINEARREG_INTERCEPT_5', 'sw_ind_L1_LINEARREG_SLOPE_5',
                   'sw_ind_L1_STDDEV_5', 'sw_ind_L1_TSF_5', 'sw_ind_L1_VAR_5', 'sw_ind_L1_MAX_5',
                   'sw_ind_L1_MIN_5', 'sw_ind_L1_MOM_5', 'sw_ind_L1_SMA_20', 'sw_ind_L1_DEMA_20',
                   'sw_ind_L1_MIDPOINT_20', 'sw_ind_L1_T3_20', 'sw_ind_L1_TEMA_20',
                   'sw_ind_L1_TRIMA_20', 'sw_ind_L1_WMA_20', 'sw_ind_L1_BETA_20', 'sw_ind_L1_CORREL_20',
                   'sw_ind_L1_LINEARREG_20', 'sw_ind_L1_LINEARREG_ANGLE_20',
                   'sw_ind_L1_LINEARREG_INTERCEPT_20', 'sw_ind_L1_LINEARREG_SLOPE_20',
                   'sw_ind_L1_STDDEV_20', 'sw_ind_L1_TSF_20', 'sw_ind_L1_VAR_20', 'sw_ind_L1_MAX_20',
                   'sw_ind_L1_MIN_20', 'sw_ind_L1_MOM_20', 'sw_ind_L1_SMA_60', 'sw_ind_L1_DEMA_60',
                   'sw_ind_L1_MIDPOINT_60', 'sw_ind_L1_TRIMA_60', 'sw_ind_L1_WMA_60',
                   'sw_ind_L1_BETA_60', 'sw_ind_L1_CORREL_60', 'sw_ind_L1_LINEARREG_60',
                   'sw_ind_L1_LINEARREG_ANGLE_60', 'sw_ind_L1_LINEARREG_INTERCEPT_60',
                   'sw_ind_L1_LINEARREG_SLOPE_60', 'sw_ind_L1_STDDEV_60', 'sw_ind_L1_TSF_60',
                   'sw_ind_L1_VAR_60', 'sw_ind_L1_MAX_60', 'sw_ind_L1_MIN_60', 'sw_ind_L1_MOM_60',
                   'sw_ind_L1_BBANDS_upper', 'sw_ind_L1_BBANDS_middle', 'sw_ind_L1_BBANDS_lower',
                   'sw_ind_L1_SAR', 'sw_ind_L1_APO', 'sw_ind_L1_AROON_DOWN', 'sw_ind_L1_AROON_UP',
                   'sw_ind_L1_BOP', 'sw_ind_L1_CCI', 'sw_ind_L1_CMO', 'sw_ind_L1_DX', 'sw_ind_L1_MACD',
                   'sw_ind_L1_MACD_SIGNAL', 'sw_ind_L1_MACD_HIST', 'sw_ind_L1_MACDEXT',
                   'sw_ind_L1_MACDEXT_SIGNAL', 'sw_ind_L1_MACDEXT_HIST', 'sw_ind_L1_MACDFIX',
                   'sw_ind_L1_MACDFIX_SIGNAL', 'sw_ind_L1_MACDFIX_HIST', 'sw_ind_L1_PPO',
                   'sw_ind_L1_SLOWK', 'sw_ind_L1_SLOWD', 'sw_ind_L1_FASTK', 'sw_ind_L1_FASTD',
                   'sw_ind_L1_TRIX', 'sw_ind_L1_ULTOSC', 'sw_ind_L1_WILLR', 'sw_ind_L1_AD',
                   'sw_ind_L1_ADOSC', 'sw_ind_L1_OBV', 'sw_ind_L1_TRANGE', 'sw_ind_L1_AVGPRICE',
                   'sw_ind_L1_MEDPRICE', 'sw_ind_L1_TYPPRICE', 'sw_ind_L1_WCLPRICE', 'sw_ind_L1_SUB',
                   'sw_ind_L2_DEMA_5', 'sw_ind_L2_MIDPOINT_5', 'sw_ind_L2_T3_5', 'sw_ind_L2_TEMA_5',
                   'sw_ind_L2_TRIMA_5', 'sw_ind_L2_WMA_5', 'sw_ind_L2_BETA_5', 'sw_ind_L2_CORREL_5',
                   'sw_ind_L2_LINEARREG_5', 'sw_ind_L2_LINEARREG_ANGLE_5',
                   'sw_ind_L2_LINEARREG_INTERCEPT_5', 'sw_ind_L2_LINEARREG_SLOPE_5',
                   'sw_ind_L2_STDDEV_5', 'sw_ind_L2_TSF_5', 'sw_ind_L2_VAR_5', 'sw_ind_L2_MAX_5',
                   'sw_ind_L2_MIN_5', 'sw_ind_L2_MOM_5', 'sw_ind_L2_SMA_20', 'sw_ind_L2_DEMA_20',
                   'sw_ind_L2_MIDPOINT_20', 'sw_ind_L2_T3_20', 'sw_ind_L2_TEMA_20',
                   'sw_ind_L2_TRIMA_20', 'sw_ind_L2_WMA_20', 'sw_ind_L2_BETA_20', 'sw_ind_L2_CORREL_20',
                   'sw_ind_L2_LINEARREG_20', 'sw_ind_L2_LINEARREG_ANGLE_20',
                   'sw_ind_L2_LINEARREG_INTERCEPT_20', 'sw_ind_L2_LINEARREG_SLOPE_20',
                   'sw_ind_L2_STDDEV_20', 'sw_ind_L2_TSF_20', 'sw_ind_L2_VAR_20', 'sw_ind_L2_MAX_20',
                   'sw_ind_L2_MIN_20', 'sw_ind_L2_MOM_20', 'sw_ind_L2_SMA_60', 'sw_ind_L2_DEMA_60',
                   'sw_ind_L2_MIDPOINT_60', 'sw_ind_L2_TRIMA_60', 'sw_ind_L2_WMA_60',
                   'sw_ind_L2_BETA_60', 'sw_ind_L2_CORREL_60', 'sw_ind_L2_LINEARREG_60',
                   'sw_ind_L2_LINEARREG_ANGLE_60', 'sw_ind_L2_LINEARREG_INTERCEPT_60',
                   'sw_ind_L2_LINEARREG_SLOPE_60', 'sw_ind_L2_STDDEV_60', 'sw_ind_L2_TSF_60',
                   'sw_ind_L2_VAR_60', 'sw_ind_L2_MAX_60', 'sw_ind_L2_MIN_60', 'sw_ind_L2_MOM_60',
                   'sw_ind_L2_BBANDS_upper', 'sw_ind_L2_BBANDS_middle', 'sw_ind_L2_BBANDS_lower',
                   'sw_ind_L2_SAR', 'sw_ind_L2_APO', 'sw_ind_L2_AROON_DOWN', 'sw_ind_L2_AROON_UP',
                   'sw_ind_L2_BOP', 'sw_ind_L2_CCI', 'sw_ind_L2_CMO', 'sw_ind_L2_DX', 'sw_ind_L2_MACD',
                   'sw_ind_L2_MACD_SIGNAL', 'sw_ind_L2_MACD_HIST', 'sw_ind_L2_MACDEXT',
                   'sw_ind_L2_MACDEXT_SIGNAL', 'sw_ind_L2_MACDEXT_HIST', 'sw_ind_L2_MACDFIX',
                   'sw_ind_L2_MACDFIX_SIGNAL', 'sw_ind_L2_MACDFIX_HIST', 'sw_ind_L2_PPO',
                   'sw_ind_L2_SLOWK', 'sw_ind_L2_SLOWD', 'sw_ind_L2_FASTK', 'sw_ind_L2_FASTD',
                   'sw_ind_L2_TRIX', 'sw_ind_L2_ULTOSC', 'sw_ind_L2_WILLR', 'sw_ind_L2_AD',
                   'sw_ind_L2_ADOSC', 'sw_ind_L2_OBV', 'sw_ind_L2_TRANGE', 'sw_ind_L2_AVGPRICE',
                   'sw_ind_L2_MEDPRICE', 'sw_ind_L2_TYPPRICE', 'sw_ind_L2_WCLPRICE', 'sw_ind_L2_SUB',
                   'sw_ind_L3_DEMA_5', 'sw_ind_L3_MIDPOINT_5', 'sw_ind_L3_T3_5', 'sw_ind_L3_TEMA_5',
                   'sw_ind_L3_TRIMA_5', 'sw_ind_L3_WMA_5', 'sw_ind_L3_BETA_5', 'sw_ind_L3_CORREL_5',
                   'sw_ind_L3_LINEARREG_5', 'sw_ind_L3_LINEARREG_ANGLE_5',
                   'sw_ind_L3_LINEARREG_INTERCEPT_5', 'sw_ind_L3_LINEARREG_SLOPE_5',
                   'sw_ind_L3_STDDEV_5', 'sw_ind_L3_TSF_5', 'sw_ind_L3_VAR_5', 'sw_ind_L3_MAX_5',
                   'sw_ind_L3_MIN_5', 'sw_ind_L3_MOM_5', 'sw_ind_L3_SMA_20', 'sw_ind_L3_DEMA_20',
                   'sw_ind_L3_MIDPOINT_20', 'sw_ind_L3_T3_20', 'sw_ind_L3_TEMA_20',
                   'sw_ind_L3_TRIMA_20', 'sw_ind_L3_WMA_20', 'sw_ind_L3_BETA_20', 'sw_ind_L3_CORREL_20',
                   'sw_ind_L3_LINEARREG_20', 'sw_ind_L3_LINEARREG_ANGLE_20',
                   'sw_ind_L3_LINEARREG_INTERCEPT_20', 'sw_ind_L3_LINEARREG_SLOPE_20',
                   'sw_ind_L3_STDDEV_20', 'sw_ind_L3_TSF_20', 'sw_ind_L3_VAR_20', 'sw_ind_L3_MAX_20',
                   'sw_ind_L3_MIN_20', 'sw_ind_L3_MOM_20', 'sw_ind_L3_SMA_60', 'sw_ind_L3_DEMA_60',
                   'sw_ind_L3_MIDPOINT_60', 'sw_ind_L3_TRIMA_60', 'sw_ind_L3_WMA_60',
                   'sw_ind_L3_BETA_60', 'sw_ind_L3_CORREL_60', 'sw_ind_L3_LINEARREG_60',
                   'sw_ind_L3_LINEARREG_ANGLE_60', 'sw_ind_L3_LINEARREG_INTERCEPT_60',
                   'sw_ind_L3_LINEARREG_SLOPE_60', 'sw_ind_L3_STDDEV_60', 'sw_ind_L3_TSF_60',
                   'sw_ind_L3_VAR_60', 'sw_ind_L3_MAX_60', 'sw_ind_L3_MIN_60', 'sw_ind_L3_MOM_60',
                   'sw_ind_L3_BBANDS_upper', 'sw_ind_L3_BBANDS_middle', 'sw_ind_L3_BBANDS_lower',
                   'sw_ind_L3_SAR', 'sw_ind_L3_APO', 'sw_ind_L3_AROON_DOWN', 'sw_ind_L3_AROON_UP',
                   'sw_ind_L3_BOP', 'sw_ind_L3_CCI', 'sw_ind_L3_CMO', 'sw_ind_L3_DX', 'sw_ind_L3_MACD',
                   'sw_ind_L3_MACD_SIGNAL', 'sw_ind_L3_MACD_HIST', 'sw_ind_L3_MACDEXT',
                   'sw_ind_L3_MACDEXT_SIGNAL', 'sw_ind_L3_MACDEXT_HIST', 'sw_ind_L3_MACDFIX',
                   'sw_ind_L3_MACDFIX_SIGNAL', 'sw_ind_L3_MACDFIX_HIST', 'sw_ind_L3_PPO',
                   'sw_ind_L3_SLOWK', 'sw_ind_L3_SLOWD', 'sw_ind_L3_FASTK', 'sw_ind_L3_FASTD',
                   'sw_ind_L3_TRIX', 'sw_ind_L3_ULTOSC', 'sw_ind_L3_WILLR', 'sw_ind_L3_AD',
                   'sw_ind_L3_ADOSC', 'sw_ind_L3_OBV', 'sw_ind_L3_TRANGE', 'sw_ind_L3_AVGPRICE',
                   'sw_ind_L3_MEDPRICE', 'sw_ind_L3_TYPPRICE', 'sw_ind_L3_WCLPRICE', 'sw_ind_L3_SUB',
                   'mkt_idx_DEMA_5', 'mkt_idx_MIDPOINT_5', 'mkt_idx_T3_5', 'mkt_idx_TEMA_5',
                   'mkt_idx_TRIMA_5', 'mkt_idx_WMA_5', 'mkt_idx_BETA_5', 'mkt_idx_CORREL_5',
                   'mkt_idx_LINEARREG_5', 'mkt_idx_LINEARREG_ANGLE_5', 'mkt_idx_LINEARREG_INTERCEPT_5',
                   'mkt_idx_LINEARREG_SLOPE_5', 'mkt_idx_STDDEV_5', 'mkt_idx_TSF_5', 'mkt_idx_VAR_5',
                   'mkt_idx_MAX_5', 'mkt_idx_MIN_5', 'mkt_idx_MOM_5', 'mkt_idx_SMA_20',
                   'mkt_idx_DEMA_20', 'mkt_idx_MIDPOINT_20', 'mkt_idx_T3_20', 'mkt_idx_TEMA_20',
                   'mkt_idx_TRIMA_20', 'mkt_idx_WMA_20', 'mkt_idx_BETA_20', 'mkt_idx_CORREL_20',
                   'mkt_idx_LINEARREG_20', 'mkt_idx_LINEARREG_ANGLE_20',
                   'mkt_idx_LINEARREG_INTERCEPT_20', 'mkt_idx_LINEARREG_SLOPE_20', 'mkt_idx_STDDEV_20',
                   'mkt_idx_TSF_20', 'mkt_idx_VAR_20', 'mkt_idx_MAX_20', 'mkt_idx_MIN_20',
                   'mkt_idx_MOM_20', 'mkt_idx_SMA_60', 'mkt_idx_DEMA_60', 'mkt_idx_MIDPOINT_60',
                   'mkt_idx_TRIMA_60', 'mkt_idx_WMA_60', 'mkt_idx_BETA_60', 'mkt_idx_CORREL_60',
                   'mkt_idx_LINEARREG_60', 'mkt_idx_LINEARREG_ANGLE_60',
                   'mkt_idx_LINEARREG_INTERCEPT_60', 'mkt_idx_LINEARREG_SLOPE_60', 'mkt_idx_STDDEV_60',
                   'mkt_idx_TSF_60', 'mkt_idx_VAR_60', 'mkt_idx_MAX_60', 'mkt_idx_MIN_60',
                   'mkt_idx_MOM_60', 'mkt_idx_BBANDS_upper', 'mkt_idx_BBANDS_middle',
                   'mkt_idx_BBANDS_lower', 'mkt_idx_SAR', 'mkt_idx_APO', 'mkt_idx_AROON_DOWN',
                   'mkt_idx_AROON_UP', 'mkt_idx_BOP', 'mkt_idx_CCI', 'mkt_idx_CMO', 'mkt_idx_DX',
                   'mkt_idx_MACD', 'mkt_idx_MACD_SIGNAL', 'mkt_idx_MACD_HIST', 'mkt_idx_MACDEXT',
                   'mkt_idx_MACDEXT_SIGNAL', 'mkt_idx_MACDEXT_HIST', 'mkt_idx_MACDFIX',
                   'mkt_idx_MACDFIX_SIGNAL', 'mkt_idx_MACDFIX_HIST', 'mkt_idx_PPO', 'mkt_idx_SLOWK',
                   'mkt_idx_SLOWD', 'mkt_idx_FASTK', 'mkt_idx_FASTD', 'mkt_idx_TRIX', 'mkt_idx_ULTOSC',
                   'mkt_idx_WILLR', 'mkt_idx_AD', 'mkt_idx_ADOSC', 'mkt_idx_OBV', 'mkt_idx_TRANGE',
                   'mkt_idx_AVGPRICE', 'mkt_idx_MEDPRICE', 'mkt_idx_TYPPRICE', 'mkt_idx_WCLPRICE',
                   'mkt_idx_SUB', 'mkt_idx_pre_close']
    """所有 TA 的列，用于 drop"""

    LOOK_PERIOD_ITEMS = 60
    """ 看多少期的数据 ， 暂定看的跨度略长一些，可能容易 train 出结果 """

    MAX_ENTITIES_PER_INST = 20
    """ 每个 train inst 中最多的股票数，不足的需要 padding ， 超过的需要拆分成多个 inst """

    # MAX_INDICATORS = 648
    MAX_INDICATORS = 168  # 全部指标 620 个，删减到 159 个
    """最多的指标数，需要能够被6 或者 12 整除，作为 model.hidden_size ，目前已有的指标数 620 """

    random_state: Optional[int] = 100

    @property
    def x_d1_size(self) -> int:
        return EquityPoolTSDatasetStep.MAX_ENTITIES_PER_INST * EquityPoolTSDatasetStep.LOOK_PERIOD_ITEMS

    @property
    def x_d2_size(self) -> int:
        return EquityPoolTSDatasetStep.MAX_INDICATORS

    @property
    def y_d2_size(self) -> int:
        return len(EquityPoolTSDatasetStep.COLS_TO_PREDICT)

    def __post_init__(self):
        self._tushare = SDKWrapperContainer.get_sdk_by_cls_name(cls_to_str(TuShareProData),
                                                                {"use_l3_cache": False})
        # 计算 mask 用到的随机数
        if self.random_state:
            np.random.seed(self.random_state)
        # 多读一年数据，以便于TA指标都能计算出数值（如：52 weeks return）
        # 使用 global inst 这样数据能够方便缓存
        self.ts_reader = StockFullyTSDataReader.get_global_instance(start_t=self.i_start_t - timedelta(days=366),
                                                                    end_t=self.i_end_t, use_cache=True)
        self.market_bd_index = self._tushare.chn_equity_business_daily_freq()

        self._tf_ds = tf.data.Dataset.from_generator(self._tf_gen_call,
                                                     output_types=(
                                                         (tf.float32, tf.int32, tf.int32, tf.int32), tf.float32),
                                                     output_shapes=(
                                                         (  # input_ids(with mask)
                                                             tf.TensorShape([self.x_d1_size, self.x_d2_size]),
                                                             # position_ids
                                                             tf.TensorShape([self.x_d1_size]),
                                                             # token_ids
                                                             tf.TensorShape([self.x_d1_size]),
                                                             # attention_mask
                                                             tf.TensorShape([self.x_d1_size])),
                                                         # y_true
                                                         tf.TensorShape([self.x_d1_size, self.y_d2_size]),
                                                     )
                                                     )
        if self.ds_pip:
            self._tf_ds_with_pip = FuncStrStep(func_body=self.ds_pip, single_input=self._tf_ds).func_result

        # 如果是 colab 运行环境，考虑将这个接口进行 lru cache ，已获得更佳的性能
        self.f_all_stk_ts_data = self.ts_reader.all_stk_ts_data
        if is_colab_env():
            self.f_all_stk_ts_data = lru_cache(maxsize=1300)(self.ts_reader.all_stk_ts_data)

    @property
    def tushare(self) -> TuShareProData:
        return self._tushare

    @classmethod
    def reindex_indicator_cols(cls, df: pd.DataFrame) -> pd.DataFrame:
        # 将 close pct_change 的列 挪到 第一/第二 列
        if df is None:
            return None
        ls_cols = df.columns.tolist()
        for col in cls.COLS_TO_PREDICT:
            ls_cols.remove(col)
        ls_cols = cls.COLS_TO_PREDICT + ls_cols
        df_rlt = df[ls_cols]
        return df_rlt

    @staticmethod
    def mask_ndarray(data: np.ndarray, mask_ratio: float, mask_val: float) -> Tuple[np.ndarray, np.ndarray]:
        """mask 一个 ndarray 对象，并且返回用于 mask 的数据信息"""
        mask = np.random.choice([False, True], len(data.ravel()), p=[1 - mask_ratio, mask_ratio]).reshape(data.shape)
        return np.where(mask, mask_val, data), mask

    def _tf_gen_call(self):
        for (t, name), row in self.df_i_by_t.iterrows():

            # 取这个时间跨度的时间坐标（取 t 之后的 n_period 期数据）
            period_index = self.market_bd_index[self.market_bd_index >= t][0:self.LOOK_PERIOD_ITEMS]
            # print(f"{t}-{name}")
            ls_entities = row["symbols"]

            not_qualify_entities = list()  # 如果某个股票在该区段内一期数据都没有，则需要被移除
            # 先把 I 中的所有股票取出来，计算区间 z-score
            dict_dfs_to_zscore: Dict[str, pd.DataFrame] = dict()
            for one_symbol in ls_entities:
                # 第一步： 得到所有的数据内容
                df = self.f_all_stk_ts_data(one_symbol)
                if df is None :
                    continue
                # 2020.03.23 , laigen , indicator 数据太多，去掉TA类的 column
                df = df.drop(columns=EquityPoolTSDatasetStep.COLS_ALL_TA)
                # 数据列调整顺序，将需要被预测的列放在 前面的位置
                df_symbol_all_period_data = EquityPoolTSDatasetStep.reindex_indicator_cols(df)
                if df_symbol_all_period_data is None:  # 没有有效数据，需要剔除该股票
                    not_qualify_entities.append(one_symbol)
                    continue
                try:
                    dict_dfs_to_zscore[one_symbol] = df_symbol_all_period_data.loc[
                        df_symbol_all_period_data.index.intersection(period_index)]
                    # dict_dfs_to_zscore[one_symbol] = df_symbol_all_period_data.loc[period_index]
                except KeyError:  # index 内容找不到，则将股票从 I(t) 中移除
                    not_qualify_entities.append(one_symbol)
            if not_qualify_entities:
                ls_entities = sorted(list(set(ls_entities) - set(not_qualify_entities)))
            # 没有任何有效的数据，则返回
            if not ls_entities:
                continue

            dict_zscore_dfs = calc_dfs_zscore(dict_dfs_to_zscore)
            if dict_zscore_dfs is None:
                logger.error(f"error raised when call calc_dfs_zscore()! {t} - {name} - {len(ls_entities)} equities.\r\n ")
                continue

            # 股票分成几个区段，每段最多 num_symbols_per_inst 只股票
            ls_entity_insts = [ls_entities[i * self.MAX_ENTITIES_PER_INST:(i + 1) * self.MAX_ENTITIES_PER_INST] for i in
                               range(len(ls_entities) // self.MAX_ENTITIES_PER_INST + 1)]
            # 整除的话，最后一项是空，则去除
            if len(ls_entities) % self.MAX_ENTITIES_PER_INST == 0:
                ls_entity_insts = ls_entity_insts[0:-1]
            for entities_in_one_element in ls_entity_insts:
                ls_indicators_np_to_concat = list()
                ls_position_np_to_concat = list()  # position 填的是区间内距离期初多少期数据
                ls_token_np_to_concat = list()  # token 填的是区间内的股票数
                i_entity_token = 1
                for one_symbol in entities_in_one_element:
                    ls_indicators_np_to_concat.append(
                        dict_zscore_dfs[one_symbol].to_numpy(dtype=np.float32, copy=True))
                    ls_position_np_to_concat.append(
                        np.array([period_index.get_loc(idx)+1 for idx in dict_zscore_dfs[one_symbol].index],
                                 dtype=np.int32))
                    ls_token_np_to_concat.append(
                        np.array([i_entity_token] * len(dict_zscore_dfs[one_symbol].index), dtype=np.int32))
                    i_entity_token += 1
                # print(f"xxx {t} - {name} - {len(ls_entities)} - {i_entity_token} : {len(ls_indicators_np_to_concat)} : {ls_entity_insts} ")
                np_one_element_indicators = np.concatenate(ls_indicators_np_to_concat, axis=0)
                np_one_element_position = np.concatenate(ls_position_np_to_concat, axis=0)
                np_one_element_token = np.concatenate(ls_token_np_to_concat, axis=0)
                # 需要对齐的长度内容
                num_indicators_to_padding = EquityPoolTSDatasetStep.MAX_INDICATORS - np_one_element_indicators.shape[
                    1]  # 第二维的 padding
                num_entities_to_padding = EquityPoolTSDatasetStep.MAX_ENTITIES_PER_INST * EquityPoolTSDatasetStep.LOOK_PERIOD_ITEMS - \
                                          np_one_element_position.shape[0]  # 第一维的 padding

                # attention mask 用于标记哪些是有效的数据，有效值标记为 1
                np_attention_mask = np.asarray([1] * np_one_element_position.shape[0] + [0] * num_entities_to_padding,
                                               dtype=np.int32)

                np_one_element_position = np.pad(np_one_element_position, (0, num_entities_to_padding), mode="constant",
                                                 constant_values=PADDING_POS)
                np_one_element_token = np.pad(np_one_element_token, (0, num_entities_to_padding), mode="constant",
                                              constant_values=PADDING_TOKEN)

                # filna
                np_one_element_indicators = np.nan_to_num(np_one_element_indicators, copy=True, nan=TS_NAN_VAL)

                y_true = np_one_element_indicators[:, 0:len(EquityPoolTSDatasetStep.COLS_TO_PREDICT)]
                x_related_data = np_one_element_indicators[:, len(EquityPoolTSDatasetStep.COLS_TO_PREDICT):]


                # print(f"--- num_entities_to_padding:{num_entities_to_padding} - {y_true_padded.shape} - {y_true.shape}")
                for _ in range(3):  # 同样一片数据， 可以多次 mask 作为多次的数据
                    # mask
                    # 把 需要被预测的内容，以及其他相关联的数据，分开做 mask ，以保证分配的比例相同
                    x_indicator_1, mask_matrix = EquityPoolTSDatasetStep.mask_ndarray(y_true.copy(), self.mask_ratio,
                                                                                      TS_MASK_VAL)
                    x_indicator_2, _ = EquityPoolTSDatasetStep.mask_ndarray(x_related_data.copy(), self.mask_ratio,
                                                                            TS_MASK_VAL)
                    x_indicators_with_mask = np.concatenate([x_indicator_1, x_indicator_2], axis=1)

                    # y_true 中只提供 mask 的值，便于 Model 只关心 mask 的数据准确性
                    y_true_without_unmask = np.where(mask_matrix, y_true, TS_UNMASK_VAL)


                    # padding
                    x_indicators_with_mask = np.pad(x_indicators_with_mask,
                                                    ((0, num_entities_to_padding), (0, num_indicators_to_padding)),
                                                    mode="constant",
                                                    constant_values=PADDING_VAL)

                    y_true_padded = np.pad(y_true_without_unmask, ((0, num_entities_to_padding), (0, 0)), mode="constant",
                                           constant_values=PADDING_VAL)

                    # print(f"indicator shape:{x_indicators_with_mask.shape}")
                    # print(f"position shape: {np_one_element_position.shape} - sample : {np_one_element_position[0:10]} ")
                    # print(f"token shape: {np_one_element_token.shape} - sample : {np_one_element_token[0:10]} ")
                    # print(f"y_true_shape：{y_true_padded.shape}")
                    # print(f"np_attention_mask：{np_attention_mask.shape}")
                    yield (x_indicators_with_mask, np_one_element_position, np_one_element_token,
                           np_attention_mask), y_true_padded
                    # return  # break for debug

    @property
    def tf_ds(self) -> tf.data.Dataset:
        if self.ds_pip is None:
            return self._tf_ds
        else:
            return self._tf_ds_with_pip


GlobalGSStepMapping.register(IByTGeneratorStep, EquityPoolTSDatasetStep, diff_name={
    IByTGeneratorStep.train_items: EquityPoolTSDatasetStep.df_i_by_t}, rule_name="train")

GlobalGSStepMapping.register(IByTGeneratorStep, EquityPoolTSDatasetStep, diff_name={
    IByTGeneratorStep.val_items: EquityPoolTSDatasetStep.df_i_by_t}, rule_name="validation")

GlobalGSStepMapping.register(IByTGeneratorStep, EquityPoolTSDatasetStep, diff_name={
    IByTGeneratorStep.eval_items: EquityPoolTSDatasetStep.df_i_by_t}, rule_name="evaluate")


def calc_test():
    # import tushare as ts
    # ts_pro = ts.pro_api("8fe0d951588bf9b605de2cdce4a7b35a61c79ed3c6e128302dcca142")
    # tushare = TuShareProData(use_l3_cache=False)
    # # req_controller = TushareReqSleepController(tushare)

    start_t = date(2019, 1, 1)
    end_t = date(2019, 12, 31)

    i_t = IByTGeneratorStep(start_t=start_t, end_t=end_t - timedelta(days=92), sample_freq="2w",
                            train_val_split_ratio=0.95, evaluate_items_count=20,
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


    # i_t = IByTGeneratorStep(start_t=start_t, end_t=end_t, sample_freq="m",
    #                         use_concept_blocks=True, ls_i_by_condition=[("low_pe", "pe > 3.0 and pe < 8.0"),
    #                                                                     ("mid_pe", "pe > 15.0 and pe < 30.0"),
    #                                                                     ("high_pe", "pe > 30.0 and pe < 100.0")])
    data_tf_gen = EquityPoolTSDatasetStep(df_i_by_t=i_t.train_items, i_start_t=start_t, i_end_t=end_t,
                                          ds_pip="lambda ds: ds.repeat().batch(5)")

    model = TSBertForMaskedCS(
        hp=TSBertForMaskedCS.HP(hidden_size=EquityPoolTSDatasetStep.MAX_INDICATORS,
                                # 多一个作为 padding 的0
                                max_position_embeddings=EquityPoolTSDatasetStep.LOOK_PERIOD_ITEMS + 1,
                                type_vocab_size=EquityPoolTSDatasetStep.MAX_ENTITIES_PER_INST + 1,
                                num_attention_heads=12))
    model.compile(loss=mae_align_to_y_true, metrics=[mae_align_to_y_true,mse_align_to_y_true], optimizer="adam")
    model.fit(data_tf_gen.tf_ds, validation_data=data_tf_gen.tf_ds, epochs=1, steps_per_epoch=15,
              validation_steps=1)
    i_cur = 0
    for ele in data_tf_gen.tf_ds.take(3800):
        input_indicator = ele[0][0]
        nan_count = tf.math.count_nonzero(tf.where(input_indicator == TS_NAN_VAL, 1, 0))
        mask_count = tf.math.count_nonzero(tf.where(input_indicator == TS_MASK_VAL, 1, 0))
        padding = tf.math.count_nonzero(tf.where(input_indicator == PADDING_VAL, 1, 0))
        total = input_indicator.shape[0] * input_indicator.shape[1] * input_indicator.shape[2]
        y_true = ele[1]
        y_true_total = y_true.shape[0] * y_true.shape[1]
        y_true_unmask = tf.math.count_nonzero(tf.where(y_true == TS_UNMASK_VAL, 1, 0))
        print(
            f"\r{i_cur}:{input_indicator.shape} - nan_pct: {float(nan_count) / total} - mask_pct : {float(mask_count) / total} padding_pct:{(float(padding) / total)} "
            f" - y_true_unmask_pct ： {float(y_true_unmask)/y_true_total}",
            end="")
        # print(y_true)
        i_cur += 1
        y = model(ele[0])
        # # print(y)
        loss = mae_align_to_y_true(ele[1], y)
        print(f"mae:{loss}")
        print(f"mse:{mse_align_to_y_true(ele[1],y)}")

    # model.summary()

    # ---------------  这些是有用的调用代码 ---------
    # import tushare as ts
    # ts_pro = ts.pro_api("8fe0d951588bf9b605de2cdce4a7b35a61c79ed3c6e128302dcca142")
    # tushare = TuShareProData(use_l3_cache=False)
    #


def reduce_indicators():
    ts_reader = StockFullyTSDataReader.get_global_instance(start_t=date(2019, 1, 1) - timedelta(days=366),
                                                           end_t=date(2019, 12, 31), use_cache=True)
    df = ts_reader.all_stk_ts_data("600000.SH")
    df = df.drop(columns=EquityPoolTSDatasetStep.COLS_ALL_TA, axis=1)
    print(df.tail(2).T)
    print(f"{len(df.columns)}")
    print(f"{df.columns.tolist()}")


def cache_ts_data():
    ts_reader = StockFullyTSDataReader.get_global_instance(start_t=date(2019, 1, 1) - timedelta(days=366),
                                                           end_t=date(2019, 12, 31), use_cache=True)

    tushare = TuShareProData(use_l3_cache=False)
    mkt_code = "SZSE"

    df_stks = tushare.stock_basic(exchange=mkt_code, cols=["ts_code", "name"])
    for id_num, row in df_stks.iterrows():
        # if id_num < 1590:
        #     continue
        print(f"\rcache data {id_num} : {row['ts_code']} - {row['name']} ", end="")
        ts_reader.all_stk_ts_data(row["ts_code"])


def sync_data_to_google_drive():
    ts_reader = StockFullyTSDataReader.get_global_instance(start_t=date(2019, 1, 1) - timedelta(days=366),
                                                           end_t=date(2019, 12, 31), use_cache=True)
    ts_reader.sync_to_google_drive()


if __name__ == "__main__":
    pd.set_option('display.max_columns', None)  # 显示所有列
    pd.set_option('display.max_rows', None)  # 显示所有行
    pd.set_option('max_colwidth', 80)

    reduce_indicators()

    # calc_test()
    # cache_ts_data()
    # sync_data_to_google_drive()

    # TODO ： 减少 indicator , 只预测 涨跌幅，扩大 time period 的范围

