# -*- coding: utf-8 -*-

"""
代码参考自： https://www.tensorflow.org/beta/tutorials/text/time_series

主要功能， 提供 time series 的基本数据准备

Notes
-----
    a)  暂时为了简单处理，env 和 agent 对于 training data set 的数据交互，通过本地文件的方式进行。
        以后将通过 arctic + mongo 的方式进行数据交互

"""
import os
import pathlib
from typing import Set, List
import logging
from gs_framework.decorators import init_actions, actionable
from gs_framework.stateful_srv_base_classes import Env
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

logger = logging.getLogger(__name__)


class WeatherDataEnv:  # (Env):
    """提供天气数据的基本准备

    主要的功能为：
        从original resource（如： jy mysql 、 tushare、 yahoo api ）上获取数据(非爬虫)，保存到本地文件或arctic mongo中。

        https://docs.google.com/document/d/1XaJvvGkM3IM0FtU7Dd22j9yqLjNfqWA7gawJ9WqufPQ/edit#heading=h.6424zjk9x1ca

    Tensorflow RecordSet 不能一行代码把 DataSet Object 产生出来，所以需要用这个类对各种来源的数据进行整理。
    如： tushare 每次只能获取一个股票的历史数据，如果需要全市场股票的所有数据，需要多次调用



    """
    REQUIRED_STATEFUL_SUBSCRIPTIONS: Set[str] = {}

    features_considered: List[str] = ['p (mbar)', 'T (degC)', 'rho (g/m**3)']
    """x的 column name"""

    # @init_actions()
    def __init__(self):
        super().__init__()
        self.df_original_data: pd.DataFrame = None
        self.df_features: pd.DataFrame = None
        self.np_features: np.ndarray = None
        self.np_targets: np.ndarray = None

    def _read_data_from_original_source(self):
        zip_path = tf.keras.utils.get_file(
            origin='https://storage.googleapis.com/tensorflow/tf-keras-datasets/jena_climate_2009_2016.csv.zip',
            fname='jena_climate_2009_2016.csv.zip',
            extract=True)
        csv_path, _ = os.path.splitext(zip_path)
        self.df_original_data = pd.read_csv(csv_path)
        logger.info(self.df_original_data.head())

    def _prepare_xy(self):
        assert self.df_original_data is not None, f" Original data set is missing"
        self.df_features = self.df_original_data[__class__.features_considered]
        self.df_features.index = self.df_original_data["Date Time"]
        # NOTE: 按照 Sample Code 中的 Normalization 方法是有 look ahead bias
        mean_value = self.df_features.values.mean(axis=0)
        std_value = self.df_features.values.std(axis=0)
        self.np_features = (self.df_features.values - mean_value) / std_value
        self.np_targets = self.np_features[:, 1]  # 把第二列挑选出来作为 y 进行预测

        logger.info(f"x_shape:{self.np_features.shape} , y_shape:{self.np_targets.shape}")
        # TODO: 存本地文件，改为存 mongo (arctic)

        # note: 暂时用文件交互，文件位置hardcode
        file_path = os.path.join("/var", "tmp")
        x_file_path = os.path.join(file_path, "sample_weather_x.npy")
        y_file_path = os.path.join(file_path, "sample_weather_y.npy")
        pathlib.Path(file_path).mkdir(parents=True, exist_ok=True)
        np.save(x_file_path, self.np_features)
        np.save(y_file_path, self.np_targets)

        # ptcharm local 调试是用的 plot 写法
        # self.df_features.plot(subplots=True)
        # plt.show()


    # # @actionable(variables=["active_flag"])
    # async def a_on_active_flag_change(self, v: int):
    #     if v == 1:
    #         pass
