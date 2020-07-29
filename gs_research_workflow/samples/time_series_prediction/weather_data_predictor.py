# -*- coding: utf-8 -*-

"""
代码参考自： https://www.tensorflow.org/beta/tutorials/text/time_series

主要功能， 提供 time series 的 Predict 功能

KeyPoint:
    1) 不需要 tune 的数据预处理参数，放在 env 中

"""
import os
from typing import Tuple

import tensorflow as tf
import numpy as np
import logging

logger = logging.getLogger(__name__)


def multivariate_data(x_data: np.ndarray, y_data: np.ndarray, start_index: int, end_index: int, lookback_size: int,
                      predict_size: int, step: int, single_step: bool = False) -> Tuple[np.ndarray, np.ndarray]:
    data = []
    labels = []

    start_index = start_index + lookback_size
    if end_index is None:
        end_index = len(x_data) - predict_size

    for i in range(start_index, end_index):
        indices = range(i - lookback_size, i, step)
        data.append(x_data[indices])

        if single_step:
            labels.append(y_data[i + predict_size])
        else:
            labels.append(y_data[i:i + predict_size])

    return np.array(data), np.array(labels)


class WeatherDataPredictor:  # (Agent):
    # NOTE 这些参数都可能被 tune 所以才定义在 agent 中。  即便是只有 0.01% 的可能性，比如： train_split

    TRAIN_SPLIT = 300000  # 前面前面有多少期的数据作为 training
    STEP = 6  # 抽取数据的间隔频度，这里是每六期数据一个点
    BATCH_SIZE = 256
    BUFFER_SIZE = 10000
    EPOCHS = 10
    EVALUATION_INTERVAL = 200

    # @init_actions()
    def __init__(self, predict_mode: bool = False):
        super().__init__()
        self.predict_mode: bool = predict_mode

        # 原始的 features 和 targets 内容

        self.np_features: np.ndarray = None
        self.np_targets: np.ndarray = None

        # 经过 split 等 pre process 之后的数据
        self.np_x_train: np.ndarray = None
        self.np_y_train: np.ndarray = None
        self.np_x_val: np.ndarray = None
        self.np_y_val: np.ndarray = None
        self.tf_dataset_train: tf.data.Dataset = None
        self.tf_dataset_val: tf.data.Dataset = None
        self._model = None
        self._train_step_history = None

    def create_or_get_model(self, input_shape):
        multi_step_model = tf.keras.models.Sequential()
        multi_step_model.add(tf.keras.layers.LSTM(32,
                                                  return_sequences=True,
                                                  input_shape=input_shape))
        multi_step_model.add(tf.keras.layers.LSTM(16, activation='relu'))
        multi_step_model.add(tf.keras.layers.Dense(72))
        return multi_step_model

    # compile_model 可能不需要变成一个 单独的函数
    def compile_model(self, optimizer, loss: str):
        self._model.compile(optimizer=optimizer, loss=loss)

    def _load_data(self):
        file_path = os.path.join("/var", "tmp")

        self.np_features = np.load(os.path.join(file_path, "sample_weather_x.npy"))
        self.np_targets = np.load(os.path.join(file_path, "sample_weather_y.npy"))

        logger.info(f"original data : {self.np_features.shape} - {self.np_targets.shape}")

    def _pre_process_data(self):
        past_history = 720  # 预测数据用多少期数据
        future_target = 72  # 每次预测多少期的数据

        self.np_x_train, self.np_y_train = multivariate_data(self.np_features, self.np_targets, 0,

                                                             __class__.TRAIN_SPLIT, past_history,
                                                             future_target, __class__.STEP)
        self.np_x_val, self.np_y_val = multivariate_data(self.np_features, self.np_targets,
                                                         __class__.TRAIN_SPLIT, None, past_history,
                                                         future_target, __class__.STEP)
        logger.info(f"train:{self.np_x_train.shape} - {self.np_y_train.shape}")
        logger.info(f"validation:{self.np_x_val.shape} - {self.np_y_val.shape}")

        self.tf_dataset_train = tf.data.Dataset.from_tensor_slices((self.np_x_train, self.np_y_train))
        self.tf_dataset_train = self.tf_dataset_train.cache().shuffle(__class__.BUFFER_SIZE).batch(
            __class__.BATCH_SIZE).repeat()

        self.tf_dataset_val = tf.data.Dataset.from_tensor_slices((self.np_x_val, self.np_y_val))
        self.tf_dataset_val = self.tf_dataset_val.batch(__class__.BATCH_SIZE).repeat()

        logger.info(f"tf dataset train: {self.tf_dataset_train}")

    def train_flow(self):

        # 加载数据，一般从 磁盘，或者从 mongo 中将数据加载到 numpy 的数据对象，但不涉及数据的预处理
        # supervisor learning 假设数据是已经有的，passive learner 不需要从stream processor (eg:kafka) 拿增量数据，可以更有效的一次拿到所有数据
            # 如：银行系统中，每间隔一天 retrain passive agent。 用 stream processor 的 window 实现收集到足够多的数据之后再 retrain
        # RL 的 on-policy 是 agent 与 env 互动，增量数据从 stream processor 上获取
        self._load_data()

        # 数据预处理，切分 train 和 validation ， 然后生成 tf.data.Dataset 对象进行 shuffle 和 batch 等操作
        self._pre_process_data()

        # 创建并编译 model
        self._model = self.create_or_get_model(self.np_x_train.shape[-2:])
        logger.info(f"x_train_shape:{self.np_x_train.shape[-2:]}")
        self.compile_model(optimizer=tf.keras.optimizers.RMSprop(clipvalue=1.0), loss="mae")
        logger.info(f"{self._model.summary()}")

        # 运行 training
        self._train_step_history = self._model.fit(self.tf_dataset_train, epochs=__class__.EPOCHS,
                                                   steps_per_epoch=__class__.EVALUATION_INTERVAL,
                                                   validation_data=self.tf_dataset_val,
                                                   validation_steps=50)

