# -*- coding: UTF-8 -*-
"""
得到某个时间点，某个指数/基金等有 membership 概念的 in / not in 的数据集合
"""
import functools
import logging
from datetime import date, datetime
from typing import Dict, Callable, Union, Tuple, List, Optional

import os
from dataclasses import dataclass
from gs_framework.gs_resource import is_colab_env

from gs_research_workflow.time_series.gs_steps.func_steps import FuncStrStep

from gs_research_workflow.time_series.gs_steps.local_context_step import GetContextStep, reg_fields_from_local_step

from gs_research_workflow.time_series.data.yfinance_wrapper import yFinanceData

from gs_research_workflow.time_series.data.arctic_and_local_cache import convert_column_as_datetime

from gs_research_workflow.core.gs_step_mapping import GlobalGSStepMapping

from gs_research_workflow.time_series.data.tushare_wrapper import TuShareProData
from gs_research_workflow.time_series.gs_steps.predefined_step_fields import TSPortfolioWeightInputStep


from gs_research_workflow.time_series.gs_steps.ts_data_steps import SymbolTSStep, OneCSAPIStep, SymbolTSCallable, \
    CSSnapshotCallable, SymbolMultipleTSStep

from gs_research_workflow.core.gs_step import GSStep
import pandas as pd
import numpy as np
import tensorflow as tf

logger = logging.getLogger(__name__)


@dataclass
class TSPortfolioWeightTFDSStep(GSStep):
    """
    用 (is or is not) membership 的方式，进行模型的训练
    membership 通常使用， index membership , industry membership , fund portfolio 等作为来源数据
        而具体是哪个 index , industry , fund 的数据，作为 x 的一组 features
    相对比，会提供一些 false 的数据，这些数据，来自于一个（获取全部数据集的） cs 数据接口中，从中按约定的比例进行 sample
        false 中的 x features ， 除了 individual equity 的数据不同以外，其他 x features 的数据与 true 样本集的数据是相同的

    通过这种方式，可以使得 ts 类数据的 train dataset 达到足够的数量
    """

    all_portfolio_callable: Dict[str, Tuple[SymbolTSCallable, CSSnapshotCallable, SymbolTSCallable]]
    """所有获取membership 的函数调用接口.
        Dict 的 key 为 symbol (如：指数代码，基金代码等) , 
        Value 为 
                 get_membership(symbol:str)->pd.DataFrame , Dataframe 的 Index 为 t， columns 为 individual (equity) symbol , weight
                 get_all_snapshot_symbols(t:date)->pd.Dataframe , dataframe 的 index 为 t , column 为 symbol
                 get_index_ts_data(symbol:str)->pd.DataFrame , 获取指数的数据
    """

    equity_ts_callable: SymbolTSCallable
    """单个股票ts数据的调用函数"""

    market_indicator: pd.DataFrame
    """市场相关的数据，这里是一个长时间跨度的数据，根据迭代的情况进行数据筛选"""

    false_sample_ratio: float = 1.0
    """同一期，预留多少 false 的数据内容"""

    random_state: int = None
    """选择 false sample 的 random state"""

    lookback_period: int = 72
    """看多少期数据"""

    time_steps_as_last_dimension: bool = False
    """
    把时间段的数据作为最后一维数据，适用的场景：
        inception_time model 的input shape为 ： [batch, time steps, #channels]
        ts_bert 的 input shape 为： [batch,#channels,time steps(similar to embedding)]
    """

    ds_pip: Optional[str] = None
    """在这里增加 ds_pip 对象，以便于能够直接在该类获取 num_to_category 的内容"""

    # 这里 hardcode fill_na 函数
    def f_fill_na(self, df):
        return df.fillna(method="ffill").fillna(0.)

    def __post_init__(self):
        # 股票数据的获取，支持 cache,以便于访问的加速
        if is_colab_env():
            self.equity_ts_callable = functools.lru_cache(maxsize=1500)(self.equity_ts_callable)

        # 填充 None 值，后面slice时就不需要再填充了
        self.market_indicator = self.f_fill_na(self.market_indicator)
        self.df_align = self.market_indicator[[self.market_indicator.columns[0]]]

        tf_ds_types = [tf.float32, tf.float32]
        tf_ds_shapes = [tf.TensorShape([None, None]), tf.TensorShape([1])]

        self._tf_ds = tf.data.Dataset.from_generator(self._ds_generator_call,
                                                     tuple(tf_ds_types),
                                                     tuple(tf_ds_shapes)
                                                     )
        if self.ds_pip:
            self._tf_ds_with_pip = FuncStrStep(func_body=self.ds_pip, single_input=self._tf_ds).func_result

    def _get_ts_by_lookback(self, symbol: str, f_query_ts: SymbolTSCallable, end_t: Union[date, datetime]):
        df_stk = f_query_ts(symbol)  # 先取出所有的数据，然后再 slice
        if df_stk is None or df_stk.empty or len(df_stk) == 0:
            return None

        df_align = self.df_align[self.df_align.index <= end_t].iloc[-1 * self.lookback_period:]
        df = df_align.join(df_stk, lsuffix="_original")
        df = self.f_fill_na(df)
        return df[df.columns[1:]]

    def _mkt_indicator_by_t(self, end_t: Union[date, datetime]):
        return self.market_indicator[self.market_indicator.index <= end_t].iloc[-1 * self.lookback_period:]

    @property
    def element_count(self) -> int:
        """共用多少个样本数据"""
        if hasattr(self, "_element_count"):
            return self._element_count
        self._element_count = 0
        id_num = 0
        for index_symbol, (membership_callable, cs_all_symbols_callable) in self.all_portfolio_callable.items():
            id_num += 1
            df_memberships = membership_callable(index_symbol)
            self._element_count += len(df_memberships)
            if id_num % 10 == 0:
                logger.debug(f"{id_num}:{self._element_count}")
        self._element_count = int(self._element_count * (1 + self.false_sample_ratio))
        return self._element_count

    def _ds_generator_call(self):
        # NOTE : 增加 shuffle ， 不直接遍历输入的 fields
        import random
        ls_index_symbols = list(self.all_portfolio_callable.keys())
        if self.random_state:
            np.random.seed(self.random_state)
        np.random.shuffle(ls_index_symbols)
        n_elements = 0

        MAX_ELEMENTS = 9999999  # 设一个遍历的最大止损长度，用于 smoke test , 如果不需要，可以设置为一个极大值

        for index_symbol in ls_index_symbols:
            portfolio_weight_callable, cs_all_symbols_callable, index_ts_callable = self.all_portfolio_callable[
                index_symbol]
            df_index_data = index_ts_callable(index_symbol)
            if df_index_data is None or df_index_data.shape[0] == 0:
                logger.debug(f"index '{index_symbol}' has no ts data , should del from input.")
                continue

            logger.debug(f"query {index_symbol}'s membership")
            df_portfolio_weights = portfolio_weight_callable(index_symbol)
            ls_t = df_portfolio_weights.index.drop_duplicates().tolist()
            np.random.shuffle(ls_t)
            for t in ls_t:
                df_portfolio_at_t = df_portfolio_weights.loc[[t]]  # note:必须是一个 list 才能确保输出的是 Dataframe 的数据结构
                equity_symbol_col_name = df_portfolio_at_t.columns[0]
                equity_weight_col_name = df_portfolio_at_t.columns[1]
                # 去掉一些 weight 为 0 的数据列(可能是一些原始数据的错误，也可能是)
                df_portfolio_at_t = df_portfolio_at_t[df_portfolio_at_t[equity_weight_col_name] >= 0.01]
                if df_portfolio_at_t.shape[0] == 0 : # 防止数据错误，一行结果都没有
                    continue
                ls_portfolio_symbols_at_t = df_portfolio_at_t[equity_symbol_col_name].tolist()
                df_all_symbols_at_time = cs_all_symbols_callable(t)
                df_symbols_except_portfolio = df_all_symbols_at_time.loc[
                    ~df_all_symbols_at_time[df_all_symbols_at_time.columns[0]].isin(ls_portfolio_symbols_at_t)]
                df_all_random_choiced_symbol = df_symbols_except_portfolio.sample(
                    n=min(len(df_symbols_except_portfolio), int(self.false_sample_ratio * len(df_portfolio_at_t))),
                    random_state=self.random_state)
                ls_symbols_not_portfolio_at_t = df_all_random_choiced_symbol[
                    df_all_random_choiced_symbol.columns[0]].tolist()
                # logger.debug(f"{index_symbol} @ {t} in sample {len(ls_portfolio_symbols_at_t)} symbols , "
                #              f"ALL NOT in sample {len(df_symbols_except_portfolio)} symbols, "
                #              f"select {len(ls_symbols_not_portfolio_at_t)}  symbols。"
                #              f"in sample {ls_portfolio_symbols_at_t} , not in sample {ls_symbols_not_portfolio_at_t}")

                df_mkt_indicator = self._mkt_indicator_by_t(t)
                df_index_indicator = self._get_ts_by_lookback(index_symbol, index_ts_callable, t)
                # 指数的数据不全(时间跨度没有足够的数据)
                if df_index_indicator is None or df_index_indicator.shape[0] != df_mkt_indicator.shape[0]:
                    if df_index_indicator is None:
                        logger.debug(f"index {index_symbol} data is none at {t}")
                    else:
                        logger.debug(f"index {index_symbol} df shape is not equal {df_index_indicator.shape[0]} vs {df_mkt_indicator.shape[0]} at {t}")
                    continue
                df_portfolio_at_t = df_portfolio_at_t.sample(frac=1., random_state=self.random_state)

                for row_id, row in df_portfolio_at_t.iterrows():
                    equity_symbol = row[equity_symbol_col_name]
                    equity_weight = row[equity_weight_col_name]
                    if equity_weight is None:
                        continue
                    t1 = datetime.now()
                    df_equity_at_t = self._get_ts_by_lookback(equity_symbol, self.equity_ts_callable, t)
                    if df_equity_at_t is None or df_equity_at_t.shape[0] != df_index_indicator.shape[0]:
                        if df_equity_at_t is not None:
                            logger.debug(
                                f"{equity_symbol} at {t} only have {df_equity_at_t.shape[0]} rows , but {df_index_indicator.shape[0]} is needed! skip this data")
                        else:
                            logger.debug(f"{equity_symbol} at {t}'s data is None")
                        continue
                    # 拼一个数据的全集
                    t2 = datetime.now()
                    df_x = df_mkt_indicator.join(df_index_indicator, how="left", rsuffix=f"_index").join(df_equity_at_t,
                                                                                                         how="left",
                                                                                                         rsuffix="_equity")
                    t3 = datetime.now()
                    if (t2 - t1).total_seconds() > 1.5:
                        logger.debug(
                            f"{index_symbol} {equity_symbol} at {t} weight {'%.4f' % equity_weight} | {df_x.shape} | {(t2 - t1).total_seconds()} secs , {(t3 - t2).total_seconds()} secs")
                    # NOTE: df.to_numpy() 得到的 shape 是 (rows,columns) 即 [t,channel]
                    # 但在 进入model 的数据，shape 应该是 [channel,t] , 所以需要 transpose
                    # target x shape : [channels, lookback_period]
                    x = df_x.to_numpy()
                    if self.time_steps_as_last_dimension:
                        x = np.transpose(x, [1, 0])
                    np.nan_to_num(x, copy=False, nan=0.0)  # 安全起见，可能还会出现 Nan 值，填入 0.
                    data_to_yield = [x, np.array([equity_weight], dtype="f")]
                    yield tuple(data_to_yield)
                    n_elements += 1
                    if n_elements >= MAX_ELEMENTS:
                        break
                for not_in_portfolio_equity_symbol in ls_symbols_not_portfolio_at_t:
                    t1 = datetime.now()
                    df_equity_at_t = self._get_ts_by_lookback(not_in_portfolio_equity_symbol, self.equity_ts_callable,
                                                              t)
                    if df_equity_at_t is None or df_equity_at_t.shape[0] != df_index_indicator.shape[0]:
                        if df_equity_at_t is not None:
                            logger.debug(
                                f"{not_in_portfolio_equity_symbol} at {t} only have {df_equity_at_t.shape[0]} rows , but {df_index_indicator.shape[0]} is needed! skip this data")
                        else:
                            logger.debug(f"{not_in_portfolio_equity_symbol} at {t}'s data is None")
                        continue
                    # 拼一个数据的全集
                    t2 = datetime.now()
                    df_x = df_mkt_indicator.join(df_index_indicator, how="left", rsuffix=f"_index").join(df_equity_at_t,
                                                                                                         how="left",
                                                                                                         rsuffix="_equity")
                    t3 = datetime.now()
                    if (t2 - t1).total_seconds() > 1.5:
                        logger.debug(
                            f"{index_symbol} {not_in_portfolio_equity_symbol} at {t} weight {0.} | {df_x.shape} | {(t2 - t1).total_seconds()} secs , {(t3 - t2).total_seconds()} secs")
                    x = df_x.to_numpy()
                    if self.time_steps_as_last_dimension:
                        x = np.transpose(x, [1, 0])
                    np.nan_to_num(x, copy=False, nan=0.0)
                    data_to_yield = [x, np.array([0.], dtype="f")]
                    yield tuple(data_to_yield)
                    n_elements += 1
                    if n_elements >= MAX_ELEMENTS:
                        break
                if n_elements >= MAX_ELEMENTS:
                    break
                logger.debug("*"*20)
            if n_elements >= MAX_ELEMENTS:
                break

    @property
    def tf_ds(self) -> tf.data.Dataset:
        if self.ds_pip is None:
            return self._tf_ds
        else:
            return self._tf_ds_with_pip


reg_fields_from_local_step(TSPortfolioWeightTFDSStep)

GlobalGSStepMapping.register(TSPortfolioWeightInputStep, TSPortfolioWeightTFDSStep,
                             diff_name={
                                 TSPortfolioWeightInputStep.all_portfolio_callable: TSPortfolioWeightTFDSStep.all_portfolio_callable})

GlobalGSStepMapping.register(TSPortfolioWeightInputStep, TSPortfolioWeightTFDSStep,
                             diff_name={
                                 TSPortfolioWeightInputStep.market_indicator: TSPortfolioWeightTFDSStep.market_indicator},
                             rule_name="market_indicator")

GlobalGSStepMapping.register(SymbolMultipleTSStep, TSPortfolioWeightTFDSStep,
                             diff_name={
                                 SymbolMultipleTSStep.symbol_ts_callable: TSPortfolioWeightTFDSStep.equity_ts_callable},
                             rule_name="equity_ts_callable")


if __name__ == "__main__":
    def test_membership_step():
        from gs_research_workflow.time_series.partial_workflow.ts_portfolio_weight_steps import \
            EQUITY_TS_FEATURES_CONTEXT
        workflow_context = EQUITY_TS_FEATURES_CONTEXT
        all_context_step = {k: GetContextStep(k) for k in workflow_context["LOCAL"].keys()}
        for k, v in all_context_step.items():
            v.SET_CONTEXT(workflow_context)
        equity_data_step = SymbolMultipleTSStep(
            _input_steps=[(all_context_step["x_feature_query_class"], "data_query_class"),
                          (all_context_step["x_features_per_symbol"], "apis_and_columns")])

        pre_define_data_step = TSPortfolioWeightInputStep(use_ssh_index=True, use_szse_index=True, use_csi_index=True,
                                                          use_fund_in_otc=True, use_fund_in_exchange=True,
                                                          query_start_t=date(2017, 1, 1), query_end_t=date(2019, 10, 1))
        membership_step = TSPortfolioWeightTFDSStep(
            random_state=100,
            false_sample_ratio=1,
            # 目前同一个step 的多个 Property 传入 多个 Fields 会出错，所以用 rule_name 的方式，在 list 中 repeat
            _input_steps=[pre_define_data_step, (pre_define_data_step, "market_indicator"),
                          (equity_data_step, "equity_ts_callable"),(all_context_step["train_val_ds_pip"], "ds_pip")]
        )
        for ds in membership_step.tf_ds.take(1):
            print(ds)
        # membership_step._ds_generator_call()
        # print(membership_step.get_init_value_dict())
        # print(f"element_count:{membership_step.element_count}")

    def prepare_index_portfolio_data():
        import tushare as ts
        import time
        import yaml

        ts_wrapper = TuShareProData(use_l3_cache=True)

        # 可以使用的 market : "SSE" / "SZSE" / "CSI"

        # 没有 portfolio 信息的 market : "CICC" / "MSCI" / "SW" / "OTH"

        ls_index_has_weight_data = []
        mkt_code = "OTH"
        dict_valid_index_code: Dict[
            str, Tuple[str, int]] = dict()  # key ： symbol code , value : (index_name,portfolio_count)
        yml_file_path = os.path.join("/tmp", f"{mkt_code}_index_member.yml")
        if os.path.isfile(yml_file_path):
            with open(yml_file_path, "r") as yaml_file:
                dict_valid_index_code = yaml.load(yaml_file)

        df_all_index = ts_wrapper.index_basic(market=mkt_code)
        print(f"{len(df_all_index)} indexes to query portfolio")
        for id_num, row in df_all_index.iterrows():
            idx_code = row["ts_code"]
            if idx_code in dict_valid_index_code:
                continue

            df_index_member = ts_wrapper.index_weight(symbol=idx_code)
            if len(df_index_member) > 0:
                ls_index_has_weight_data.append(idx_code)
                print(f"index[{id_num}]:{idx_code}-{row['name']}-{len(df_index_member)}")
            else:
                if (id_num - len(ls_index_has_weight_data) + 1) % 5 == 0:
                    print(f"sleep for empty data {id_num} , count {id_num - len(ls_index_has_weight_data) + 1}")
                    time.sleep(5)
            dict_valid_index_code[idx_code] = (row['name'], len(df_index_member))
            # 先简化代码，每次都 dump 一下数据
            with open(yml_file_path, "w") as yaml_file:
                yaml.dump(dict_valid_index_code, yaml_file)


        print(f"total have index {len(ls_index_has_weight_data)}")
        print(ls_index_has_weight_data)

    def read_index_has_portfolio_data():
        import yaml
        # 可以使用的 market : "SSE" / "SZSE" / "CSI"
        # 基金的数据包括有 : "Fund_O" / "Fund_E"
        mkt_code = "Fund_E"
        dict_valid_index_code: Dict[
            str, Tuple[str, int]] = dict()  # key ： symbol code , value : (index_name,portfolio_count)
        # yml_file_path = os.path.join("/tmp", f"{mkt_code}_index_member.yml")
        yml_file_path = os.path.join("/tmp", f"{mkt_code}_portfolio.yml")
        with open(yml_file_path, "r") as yaml_file:
            dict_valid_index_code = yaml.load(yaml_file)

        ls_data: List[Tuple[str, str]] = []
        for index_symbol, (index_name, member_data_count) in dict_valid_index_code.items():
            if 20 < member_data_count < 10000:
                print(f"{index_symbol}:{index_name}:{member_data_count}")
                ls_data.append((index_symbol, index_name))
        print(len(ls_data))
        print("-"*20)
        print(len(ls_data))
        print(ls_data)

    def prepare_fund_portfolio_data():
        import tushare as ts
        import yaml
        import time
        ts_pro = ts.pro_api("8fe0d951588bf9b605de2cdce4a7b35a61c79ed3c6e128302dcca142")
        ts_wrapper = TuShareProData(use_l3_cache=True)

        # print(ts_wrapper.fund_nav("001753.OF", re_init=True))

        # print(ts_wrapper.cs_fund_nav(end=date(2020, 1, 23), look_period=1))

        # print(ts_pro.fund_nav(ts_code="001753.OF"))  # 公募基金的累计净值，可以作为 x_feature 的 by value 部分
        # print(ts_pro.fund_portfolio(ts_code="008140.OF")) # 公募基金的持仓作为 membership 的数据
        # df = ts_pro.fund_basic(market="O")

        # --- 所关注的开放式基金列表 ----
        # df = ts_wrapper.fund_basic(market="E")
        # df = df[~df["invest_type"].str.contains("货币型|黄金现货|债券型|原油主题|期货型")]
        # print(df["invest_type"].unique())
        # print(df)

        # print(ts_wrapper.fund_portfolio("515070.SH"))
        # -------

        # ---- 遍历有持仓数据的基金列表 ------
        ls_fund_has_weight_data = []
        mkt_code = "Fund_E"
        dict_valid_fund_code: Dict[
            str, Tuple[str, int]] = dict()  # key ： symbol code , value : (index_name,portfolio_count)
        yml_file_path = os.path.join("/tmp", f"{mkt_code}_portfolio.yml")
        if os.path.isfile(yml_file_path):
            with open(yml_file_path, "r") as yaml_file:
                dict_valid_fund_code = yaml.load(yaml_file)

        df_all_fund = ts_wrapper.fund_basic(market="E")
        df_valid_fund = df_all_fund[~df_all_fund["invest_type"].str.contains("货币型|黄金现货|债券型|原油主题|期货型")]

        print(f"{len(df_valid_fund)} funds to query portfolio")
        for id_num, row in df_valid_fund.iterrows():
            fund_code = row["ts_code"]
            if fund_code in dict_valid_fund_code:
                continue

            df_fund_portfolio = ts_wrapper.fund_portfolio(symbol=fund_code)
            if len(df_fund_portfolio) > 0:
                ls_fund_has_weight_data.append(fund_code)
                print(f"fund [{id_num}]:{fund_code}-{row['name']}-{len(df_fund_portfolio)}")
            else:
                if (id_num - len(ls_fund_has_weight_data) + 1) % 5 == 0:
                    print(f"sleep for empty data {id_num} , count {id_num - len(ls_fund_has_weight_data) + 1}")
                    time.sleep(5)
            dict_valid_fund_code[fund_code] = (row['name'], len(df_fund_portfolio))
            # 先简化代码，每次都 dump 一下数据
            with open(yml_file_path, "w") as yaml_file:
                yaml.dump(dict_valid_fund_code, yaml_file)
        # -----


    def test_index_data_callable():
        symbol = "007072.OF"
        # symbol = '000031.OF'
        f = SymbolTSStep(api="fund_portfolio", cols=["symbol", "stk_mkv_ratio"],
                         start_t=date(2016, 1, 1),
                         end_t=date(2019, 10, 1)).symbol_ts_callable
        df = f(symbol)
        # print(df.head(50))
        # ls_t = df.index.drop_duplicates().tolist()
        # np.random.shuffle(ls_t)
        # for t in ls_t:
        #     df_portfolio_at_t = df.loc[[t]]
        #     ls_portfolio_symbols_at_t = df_portfolio_at_t[df_portfolio_at_t.columns[0]].tolist()
        #     print(ls_portfolio_symbols_at_t)

    def debug_ts_interface():
        from gs_research_workflow.time_series.partial_workflow.ts_portfolio_weight_steps import \
            EQUITY_TS_FEATURES_CONTEXT
        f = SymbolMultipleTSStep(data_query_class=EQUITY_TS_FEATURES_CONTEXT["LOCAL"]["x_feature_query_class"],
                                 apis_and_columns=EQUITY_TS_FEATURES_CONTEXT["LOCAL"][
                                     "x_features_per_symbol"]).symbol_ts_callable
        print(f("603077.SH"))


    test_membership_step()
    # prepare_index_portfolio_data()
    # read_index_has_portfolio_data()
    # prepare_fund_portfolio_data()
    # test_index_data_callable()
    # debug_ts_interface()
