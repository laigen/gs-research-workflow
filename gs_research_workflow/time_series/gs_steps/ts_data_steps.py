# -*- coding: UTF-8 -*-

"""与获取 ts_data 相关的 GSStep"""
import json
import logging
import collections
from datetime import date, datetime
from typing import Union, List, Callable, Mapping, Optional, NamedTuple, Dict, Any, Tuple

from dataclasses import dataclass, field
from gs_research_workflow.time_series.data.arctic_and_local_cache import ArcticAndLocalCacheBySymbol

from gs_research_workflow.time_series.data.tushare_wrapper import TuShareProData

from gs_research_workflow.common.serialization_utilities import str_to_cls, cls_to_str

from gs_research_workflow.time_series.gs_steps.data_structure_utility_steps import KeyValueListToMappingStep
from gs_research_workflow.time_series.gs_steps.func_steps import FuncStrStep

from gs_research_workflow.core.gs_step_mapping import GlobalGSStepMapping

from gs_research_workflow.core.gs_step import GSStep
import pandas as pd

from gs_research_workflow.time_series.gs_steps.local_context_step import reg_fields_from_local_step

logger = logging.getLogger(__name__)

SymbolPeriodTSCallable = Callable[[str, Union[date, datetime], Union[date, datetime]], pd.DataFrame]
"""参数的含义为: (symbol,start_time, end_time) """

SymbolPeriodTSByLookbackCallable = Callable[[str, Union[date, datetime], int], pd.DataFrame]
"""提供 lookback 参数的 period ts 数据获取函数，参数的含义为：(Symbol,end_time,lookback) """

SymbolTSCallable = Callable[[str], pd.DataFrame]
"""参数的含义为： (symbol)"""

CSPeriodByLookbackCallable = Callable[[Union[date, datetime], int], pd.DataFrame]
"""获取一段时间的 CS 数据，参数的含义为 (end_time,lookback) """

CSSnapshotCallable = Callable[[Union[date, datetime]], pd.DataFrame]
"""取离enddate最近的一期数据"""


@dataclass
class TSSDKWrapper(GSStep):
    """一些 通过接口提供的 TS 资源的 wrapper """

    data_source: str = "tushare_pro"
    """数据源，目前仅支持 tushare_pro"""

    data_source_auth: str = None
    """数据源的认证信息，None 表示 不提供，用平台默认的
        目前相对于 tushare_pro , authentication 为 token
    """


class SDKWrapperContainer:
    """为了避免频繁的创建 tushare_wrapper 这类对象（会重复创建多份 arctic storage），这里做一个全局的缓存"""
    _all_sdk_wrapper: Dict[str, ArcticAndLocalCacheBySymbol] = {}

    @classmethod
    def get_sdk(cls, wrapper_def: TSSDKWrapper, use_l3_cache: bool) -> ArcticAndLocalCacheBySymbol:
        cache_key = f"{wrapper_def.data_source}-{wrapper_def.data_source_auth}-{use_l3_cache}"
        if cache_key in cls._all_sdk_wrapper:
            return cls._all_sdk_wrapper[cache_key]
        if wrapper_def.data_source == "tushare_pro":
            from gs_research_workflow.time_series.data.tushare_wrapper import TuShareProData
            if wrapper_def.data_source_auth is None:
                _sdk = TuShareProData(use_l3_cache=use_l3_cache)
            else:
                _sdk = TuShareProData(wrapper_def.data_source_auth, use_l3_cache=use_l3_cache)
            cls._all_sdk_wrapper[cache_key] = _sdk
            return _sdk
        else:
            raise NotImplementedError

    @classmethod
    def get_sdk_by_cls_name(cls, cls_name: str, init_kwargs: Optional[Dict]) -> ArcticAndLocalCacheBySymbol:
        cache_key = f"{cls_name}-{init_kwargs}"
        if cache_key in cls._all_sdk_wrapper:
            return cls._all_sdk_wrapper[cache_key]

        data_cls = str_to_cls(cls_name)
        sdk = data_cls(**init_kwargs)
        cls._all_sdk_wrapper[cache_key] = sdk
        return sdk


class HasSDKWrapperMixin:
    def _init_sdk(self):
        from gs_research_workflow.common.path_utilities import _is_colab_env
        use_l3_cache = _is_colab_env()
        self._sdk = SDKWrapperContainer.get_sdk(self.sdk_wrapper, use_l3_cache)
        assert self._sdk is not None


@dataclass
class SymbolTSStep(HasSDKWrapperMixin, GSStep):
    """从 tushare / yfinance 等的 wrapper 接口中，获取一个 symbol 的 数据内容"""

    # region fields

    api: str

    cols: List[str]

    symbols: Optional[Union[str, List[str], Mapping[str, str]]] = None
    """ Symbol 支持单数和复数
    
        Examples
        --------
        "600000.SH"     表示单个股票， ts_data 为 Dataframe
        
        ["600000.SH","600050.SH"] 表示多个股票，ts_data 为 List[Dataframe]
        
        {"BigCap":"000043.SH", "MidCap":"000044.SH","SmlCap":"000045.SH"} 
                表示带 label含义的多个 symbol 数据， ts_data 为 Mapping[label,Dataframe]
    """

    start_t: Union[date, datetime] = None

    end_t: Union[date, datetime] = None

    sdk_wrapper: TSSDKWrapper = TSSDKWrapper()

    process_after_query: Optional[str] = None
    """查询完成后的数据处理步骤"""

    # endregion

    def __post_init__(self):
        self._init_sdk()
        if self.process_after_query:
            self._func_after_query = FuncStrStep(func_body=self.process_after_query).func
        else:
            self._func_after_query = lambda x: x  # 方便写代码，这里定义一个不做任何处理的函数

    @property
    def query_sdk(self) -> ArcticAndLocalCacheBySymbol:
        return self._sdk

    @property
    def ts_data(self) -> Union[pd.DataFrame, List[pd.DataFrame], Mapping[str, pd.DataFrame]]:
        """得到 symbols 的 ts数据 """
        assert self.symbols is not None
        if isinstance(self.symbols, str):
            return self._func_after_query(
                getattr(self._sdk, self.api)(self.symbols, self.start_t, self.end_t, self.cols))
        elif isinstance(self.symbols, list):
            return [self._func_after_query(
                getattr(self._sdk, self.api)(s, self.start_t, self.end_t, self.cols) for s in self.symbols)]
        elif isinstance(self.symbols, collections.Mapping):
            return {k: self._func_after_query(getattr(self._sdk, self.api)(s, self.start_t, self.end_t, self.cols)) for
                    k, s in
                    self.symbols.items()}
        else:
            raise RuntimeError(f"Invalid symbol type {type(self.symbols)}")

    @property
    def symbol_ts_callable(self) -> SymbolTSCallable:
        """symbol在某个 ts 跨度内的 callable"""
        assert self.symbols is None
        return lambda symbol: self._func_after_query(
            getattr(self._sdk, self.api)(symbol, self.start_t, self.end_t, cols=self.cols))

    @property
    def symbol_period_ts_callable(self) -> SymbolPeriodTSCallable:
        """按照 symbol 获取一段时间的 callable 对象 """
        assert self.symbols is None and self.start_t is None and self.end_t is None
        return lambda symbol, start_t, end_t: self._func_after_query(
            getattr(self._sdk, self.api)(symbol, start_t, end_t, cols=self.cols))


reg_fields_from_local_step(SymbolTSStep)

# ts 取值的结果能够套入一个函数的输出内容
GlobalGSStepMapping.register(SymbolTSStep, FuncStrStep, rule_name="ts_process",
                             diff_name={SymbolTSStep.ts_data: FuncStrStep.single_input})

GlobalGSStepMapping.register(KeyValueListToMappingStep, SymbolTSStep, rule_name="symbols",
                             diff_name={KeyValueListToMappingStep.mapping_data: SymbolTSStep.symbols})


@dataclass
class SymbolMultipleTSStep(GSStep):
    """适用于将多个 Symbol TS 的数据按照 t Join 之后的 callable 或者 ts_data
    先简化一些，只能来自于一个 sdk wrapper 的多个接口
    """

    data_query_class: str
    """query的类定义，如 tushare"""

    apis_and_columns: Dict[str, Tuple[str, List[str]]]
    """数据结构为Dict[api_name,Tuple[column_prefix,List[cols]]]"""

    data_query_class_init_kwargs: Dict[str, Any] = field(default_factory=dict)

    symbols: Optional[Union[str, List[str], Mapping[str, str]]] = None
    """ Symbol 支持单数和复数

        Examples
        --------
        "600000.SH"     表示单个股票， ts_data 为 Dataframe

        ["600000.SH","600050.SH"] 表示多个股票，ts_data 为 List[Dataframe]

        {"BigCap":"000043.SH", "MidCap":"000044.SH","SmlCap":"000045.SH"} 
                表示带 label含义的多个 symbol 数据， ts_data 为 Mapping[label,Dataframe]
    """

    start_t: Union[date, datetime] = None

    end_t: Union[date, datetime] = None
    
    def __post_init__(self):
        from gs_research_workflow.time_series.data.tushare_wrapper import TuShareProData
        from gs_research_workflow.common.path_utilities import _is_colab_env

        assert len(self.apis_and_columns) > 0
        assert self.data_query_class

        self._data_query_insts = []

        data_cls_init_kwargs = self.data_query_class_init_kwargs
        # NOTE: 暂时找不到好的地方做这种 use_l3_cache 参数的自动原则，暂时先 hardcode 在这个函数中
        data_cls_init_kwargs["use_l3_cache"] = _is_colab_env()
        self._data_query_insts.append(
            SDKWrapperContainer.get_sdk_by_cls_name(self.data_query_class, data_cls_init_kwargs))

    @staticmethod
    def _eval_one_api(sdk, api: str, join_rsuffix: str, symbol: str, start: Union[date, datetime],
                      end: Union[date, datetime], cols: List[str],
                      df_to_join: Optional[pd.DataFrame] = None) -> pd.DataFrame:
        df = getattr(sdk, api)(symbol, start, end, cols)
        if df is None:
            return None
        if df_to_join is not None:
            df = df_to_join.join(df, how="left", rsuffix=join_rsuffix if join_rsuffix else "")
        return df

    def iter_apis_and_eval(self, symbol: str, start: Union[date, datetime],
                           end: Union[date, datetime]) -> pd.DataFrame:
        df = None
        for api, (prefix, cols) in self.apis_and_columns.items():
            df = SymbolMultipleTSStep._eval_one_api(self._data_query_insts[0], api, prefix, symbol, start,
                                                    end, cols, df)
        return df

    @property
    def query_sdk(self) -> ArcticAndLocalCacheBySymbol:
        return self._data_query_insts[0]

    @property
    def ts_data(self) -> Union[pd.DataFrame, List[pd.DataFrame], Mapping[str, pd.DataFrame]]:
        """得到 symbols 的 ts数据 """
        assert self.symbols is not None
        if isinstance(self.symbols, str):
            return self.iter_apis_and_eval(self.symbols, self.start_t, self.end_t)
        elif isinstance(self.symbols, list):
            return [self.iter_apis_and_eval(s, self.start_t, self.end_t) for s in self.symbols]
        elif isinstance(self.symbols, collections.Mapping):
            return {k: self.iter_apis_and_eval(s, self.start_t, self.end_t) for k, s in
                    self.symbols.items()}
        else:
            raise RuntimeError(f"Invalid symbol type {type(self.symbols)}")

    @property
    def symbol_ts_callable(self) -> SymbolTSCallable:
        """symbol在某个 ts 跨度内的 callable"""
        assert self.symbols is None
        return lambda symbol: self.iter_apis_and_eval(symbol, self.start_t, self.end_t)

    @property
    def symbol_period_ts_callable(self) -> SymbolPeriodTSCallable:
        """按照 symbol 获取一段时间的 callable 对象 """
        assert self.symbols is None and self.start_t is None and self.end_t is None
        return lambda symbol, start_t, end_t: self.iter_apis_and_eval(symbol, start_t, end_t)


reg_fields_from_local_step(SymbolMultipleTSStep)


@dataclass
class OneCSAPIStep(HasSDKWrapperMixin, GSStep):
    api: str
    cols: List[str]
    sdk_wrapper: TSSDKWrapper = TSSDKWrapper()

    process_after_query: Optional[str] = None
    """查询完成后的数据处理步骤"""

    def __post_init__(self):
        self._init_sdk()
        self._func_after_query = None
        if self.process_after_query:
            self._func_after_query = FuncStrStep(func_body=self.process_after_query).func
        else:
            self._func_after_query = lambda x: x  # 方便写代码，这里定义一个不做任何处理的函数

    @property
    def query_sdk(self) -> ArcticAndLocalCacheBySymbol:
        return self._sdk

    @property
    def snapshot_callable(self) -> CSSnapshotCallable:
        """symbol在某个 ts 跨度内的 callable"""
        return lambda t: self._func_after_query(getattr(self._sdk, self.api)(end=t, look_period=1, cols=self.cols))

    @property
    def cs_endtime_with_lookback_callable(self) -> CSPeriodByLookbackCallable:
        """根据 enddate 和 lookback 获取切片数据集合"""
        return lambda t, n: self._func_after_query(getattr(self._sdk, self.api)(end=t, look_period=n, cols=self.cols))



# 该类暂时先不用 2020.01.27
# @dataclass
# class SymbolTSZScoreStep(GSStep):
#     f_cs_I_data_query: CSPeriodByLookbackCallable
#     """通过该接口获取 I(t) 筛选前的原始数据"""
#
#     I_condition: str
#     """ I 的条件，用 I 代表 cs_df
#         eg: (I["pe"]<20.0) & (I["pe"]>10)
#         NOTE : column 必须是能够在 f_cs_data_query 中返回的数据
#     """
#
#     f_cs_J_original_query: CSPeriodByLookbackCallable





if __name__ == "__main__":

    def test_multi_symbol_ts():
        multi_symbol_ts = SymbolMultipleTSStep(
            data_query_class=cls_to_str(TuShareProData),
            apis_and_columns={
                "equity_basic_daily": ("fin_ind_", ["turnover_rate", "turnover_rate_f",
                                                    "volume_ratio", "pe", "pe_ttm",
                                                    "pb", "ps",
                                                    "ps_ttm", "dv_ratio", "dv_ttm",
                                                    "total_share", "free_share",
                                                    "total_mv", "circ_mv"]),
                "equity_backward_adjust_daily": (
                    "backward_adj_", ["open", "high", "low", "close", "pre_close",
                                      "change", "pct_chg", "vol", "amount"]),
                "equity_moneyflow_daily": ("moneyflow_", ["buy_sm_vol", "buy_sm_amount",
                                                          "sell_sm_vol", "sell_sm_vol",
                                                          "sell_sm_amount",
                                                          "buy_md_vol", "buy_md_amount",
                                                          "sell_md_vol",
                                                          "sell_md_amount",
                                                          "buy_lg_vol",
                                                          "buy_lg_amount",
                                                          "sell_lg_vol",
                                                          "sell_lg_amount",
                                                          "buy_elg_vol",
                                                          "buy_elg_amount",
                                                          "sell_elg_vol",
                                                          "sell_elg_amount",
                                                          "net_mf_vol",
                                                          "net_mf_amount"])
            },
            symbols=["600000.SH", "600050.SH"])
        print(json.dumps(multi_symbol_ts.get_init_value_dict(out_self_cls=True)))
        print(multi_symbol_ts.ts_data[0].info())
        print(multi_symbol_ts.ts_data[0].describe())
        print(multi_symbol_ts.ts_data[0].T)



    test_multi_symbol_ts()

    # symbol_ts_step = SymbolTSStep(api="equity_backward_adjust_daily", symbols="600000.SH",
    #                             cols=["open", "high", "low", "close", "pre_close", "change", "pct_chg", "vol", "amount"])
    #
    # print(symbol_ts_step.ts_data)
    #
    # symbol_ts_step.symbols = ["600004.SH", "600050.SH"]
    # for ts in symbol_ts_step.ts_data:
    #     print(ts)
    #
    # symbol_ts_step = SymbolTSStep(api="index_weight",
    #                               symbols={"BigCap": "000043.SH", "MidCap": "000044.SH", "SmlCap": "000045.SH"},
    #                               cols=["con_code"])
    # for k, v in symbol_ts_step.ts_data.items():
    #     print(k)
    #     print(v)


    # print(ts_api.symbol_ts_callable("600010.SH"))
    # print(ts_api.get_init_value_dict(True))
