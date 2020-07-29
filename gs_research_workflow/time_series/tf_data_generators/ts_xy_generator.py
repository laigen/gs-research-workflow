# -*- coding: UTF-8 -*-

"""
提供适用于 tf.data 中 from_generator 的对象
该 generator 适用于 y 是 ts 类的 model

"""
from datetime import date, datetime
from typing import List, Union, Callable, Optional
import logging
from dataclasses import dataclass
import pandas as pd
import tensorflow as tf

from gs_research_workflow.time_series.tf_data_generators.generator_related_classes import TSCallableData, MultiTSData

logger = logging.getLogger(__name__)


@dataclass
class TSXYGenerator(MultiTSData):  # NOTE: ClassName 还是太 general，后续把根据该类能提供的功能进行窄化
    """
        适用于 tf.data 中 from_generator 的数据对象，使用该 Generator 生成的数据，有以下几个假定（约束）：
        1) x,y 的数据频度是对齐的， y.t left join x.t
        2) 所有取数据的 function signature 符合规则 get_data( symbol:str , start_t:Union[date,datetime] , end_t:Union[date,datetime] , cols:List[str])
        3) y 必须是 ts, 并且在选择的时间点之后的 n 期
    """
    x_symbols: List[str]
    """x有哪些symbol，这些 symbol 必须是数据获取接口支持的 symbol 格式
        Examples
        --------
            ["600000.SH", "600028.SH", "600050.SH"] , tushare 支持的 symbol
    """
    y_symbol: Union[List[str], str]
    """
        一个或多个预测的 y 的值
        Examples
        --------
        "000001.SH" or ["000001.SH","000050.SH"]
            
    """

    x_get_data_objs: List[TSCallableData]
    """
        X 取数据的信息，多个数据接口获取的内容必须是相同频度，并且会被先 join 起来
        Examples
        --------
            tushare = TuShareProData().equity_quotation_daily
            [tushare.equity_quotation_daily, ["close", "change", "vol", "amount"] , "{symbol}_" , 
            tushare.equity_basic_daily , ["turnover_rate", "pe","pb"] , "{symbol}_" ]
    """
    y_get_data_objs: List[TSCallableData]

    x_loopback: int = 120

    y_predict_count: int = 5
    """预测y的多少期数据"""

    f_fill_na: Optional[Callable[[pd.DataFrame], pd.DataFrame]] = lambda x: x.fillna(method="ffill")

    def __post_init__(self):
        ls_df_all_x = [self._loop_get_data_and_join(symbol, self.x_get_data_objs) for symbol in self.x_symbols]

        if isinstance(self.y_symbol, list):
            ls_all_y_symbols = self.y_symbol
        else:
            ls_all_y_symbols = [self.y_symbol]

        ls_df_all_y = [self._loop_get_data_and_join(symbol, self.y_get_data_objs) for symbol in ls_all_y_symbols]
        self._y_df_data = ls_df_all_y[0]
        if len(ls_df_all_y) > 1:
            for df in ls_df_all_y[1:]:
                self._y_df_data = self._y_df_data.join(df)
        self._y_columns_count = len(self._y_df_data.columns)

        self._yx_df_data = self._y_df_data
        for df in ls_df_all_x:
            self._yx_df_data = self._yx_df_data.join(df)  # 这里假定 column 都已经 rename 过，不会有重名的问题

        if self.f_fill_na:
            self._yx_df_data = self.f_fill_na(self._yx_df_data)

        self._y_df_data = self._yx_df_data[self._yx_df_data.columns[0:self._y_columns_count]]
        self._x_df_data = self._yx_df_data[self._yx_df_data.columns[self._y_columns_count:]]

    @property
    def x_shape(self) -> tf.TensorShape:
        return tf.TensorShape([self.x_loopback, len(self._x_df_data.columns)])

    @property
    def y_shape(self) -> tf.TensorShape:
        if self._y_columns_count == 1:
            return tf.TensorShape([self.y_predict_count])
        else:
            return tf.TensorShape([self.y_predict_count, self._y_columns_count])

    @property
    def x_data(self):
        """x的数据，便于 plot查看数据"""
        return self._x_df_data

    @property
    def y_data(self):
        return self._y_df_data

    def __call__(self):
        for i in range(len(self._yx_df_data) - self.x_loopback - self.y_predict_count - 1):
            if self._y_columns_count == 1:
                yield (self._x_df_data.iloc[i:i + self.x_loopback, :].to_numpy(),
                       self._y_df_data[self._y_df_data.columns[0]][i:i + self.y_predict_count].to_numpy())
            else:
                yield (self._x_df_data.iloc[i:i + self.x_loopback, :].to_numpy(),
                       self._y_df_data.iloc[i:i + self.y_predict_count, :].to_numpy())


if __name__ == "__main__":
    from gs_research_workflow.time_series.data.tushare_wrapper import TuShareProData

    tushare = TuShareProData()

    gen = TSXYGenerator(x_symbols=["600000.SH", "600028.SH", "600050.SH"],
                        y_symbol="000001.SH",
                        x_get_data_objs=[
                              TSCallableData(tushare.equity_quotation_daily, ["close", "change", "vol", "amount"],
                                             "{symbol}_"),
                              TSCallableData(tushare.equity_basic_daily, ["turnover_rate", "pe", "pb"], "{symbol}_")],
                        y_get_data_objs=[TSCallableData(tushare.index_quotation_daily, ["close"], "{symbol}_")],
                        start_t=date(2010, 1, 1),
                        end_t=date(2016, 12, 31),
                        x_loopback=120,
                        y_predict_count=5,
                        )
    first_slice = next(gen())
    print(first_slice[0])
    print(first_slice[0].shape)
    print(first_slice[1])
    print(first_slice[1].shape)

    # df = tushare.equity_basic_daily("600000.SH")
    # print(df)

