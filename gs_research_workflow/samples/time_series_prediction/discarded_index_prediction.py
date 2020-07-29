# -*- coding: UTF-8 -*-
import os
from datetime import date, datetime

from numpy.compat import os_PathLike

from gs_research_workflow.time_series.data.tushare_wrapper import TuShareProData
import tensorflow as tf
import logging
import pandas
logger = logging.getLogger(__name__)


class SampleTushareDataGenerator:
    # 以下这些属于 Hyper Parameter，可以参与到 Tune
    lookback = 120
    predict_count = 5  # 预测之后的N期数据
    feature = ["close", "change", "vol", "amount"]
    target_column = "close"

    # 以下这些一般不参与到 tune
    x_symbols = ["600000.SH", "600028.SH", "600050.SH"]  # 示意用，一般是板块的股票，这个symbol 的序是与 model 强关联的
    y_symbol = "000001.SH"  # 暂时假定在这个类中能够预测的一定是股票

    def __init__(self, start_t: date, end_t: date):
        self.start_t = start_t

        # 从 pkl 读数据是另外一个 class 处理
        # cache 的文件路径将根据 start_t , end_t , FEATURES 做 hash
        # 暂时根据 start / end 确定存盘路径，以后改成只有一份全部数据的 pickle
        self.tushare = TuShareProData()
        df_all_x = [self.tushare.equity_quotation_daily(x, start=start_t, end=end_t, cols=self.feature) for x in
                    self.x_symbols]
        df_y = self.tushare.index_quotation_daily(self.y_symbol, start=start_t, end=end_t, cols=[self.target_column])
        self.df_all_data = df_y
        for x_symbol, x_df in zip(self.x_symbols, df_all_x):
            self.df_all_data = self.df_all_data.join(x_df, rsuffix=f"_{x_symbol}")
        self.df_all_data.fillna(method="ffill", inplace=True)

    def x_shape(self) -> tf.TensorShape:
        return tf.TensorShape([self.lookback, len(self.x_symbols) * len(self.feature)]).as_list()

    def __call__(self):

        for i in range(len(self.df_all_data) - self.lookback - self.predict_count - 1):
            yield (self.df_all_data.iloc[i:i + self.lookback, 1:].to_numpy(),# [9, lookback]
                   self.df_all_data[self.df_all_data.columns[0]][i:i + self.predict_count].to_numpy())


def create_or_get_model(input_shape):
    multi_step_model = tf.keras.models.Sequential()
    multi_step_model.add(tf.keras.layers.LSTM(32,
                                              return_sequences=True,
                                              input_shape=input_shape))
    multi_step_model.add(tf.keras.layers.LSTM(16, activation='relu'))
    multi_step_model.add(tf.keras.layers.Dense(SampleTushareDataGenerator.predict_count))
    return multi_step_model


def normalize_x_instance(x, y):
    x_mean = tf.math.reduce_mean(x, 0)
    x_std = tf.math.reduce_std(x, 0)

    # y_mean = tf.math.reduce_mean(y,0)
    # y_std = tf.math.reduce_std(y,0)

    # Y 的 normalize 的方式有问题
    # return (x - x_mean) / x_std, (y - y_mean) / y_std
    # logger.info(f"x:{(x - x_mean) / x_std}")
    # logger.info(f"y:{y}")
    return (x - x_mean) / x_std, y


class SamplePricePrediction:
    def __init__(self):
        self.train_dataset_gen = SampleTushareDataGenerator(start_t=date(2010, 1, 1), end_t=date(2016, 12, 31))

        self.val_dataset_gen = SampleTushareDataGenerator(start_t=date(2017, 1, 1), end_t=date(2018, 12, 31))

    def run_pipline(self):
        # data = next(iter(source_gen()))
        # print(data.shape)
        train_dataset = tf.data.Dataset.from_generator(self.train_dataset_gen, (tf.float32, tf.float32),
                                                       (tf.TensorShape([self.train_dataset_gen.lookback,
                                                                        len(self.train_dataset_gen.x_symbols) * len(
                                                                            self.train_dataset_gen.feature)]),
                                                        tf.TensorShape([self.train_dataset_gen.predict_count])))
        train_dataset = train_dataset.map(normalize_x_instance, num_parallel_calls=2)
        train_dataset = train_dataset.shuffle(200).batch(10).repeat()

        #暂时先重复 train , validation 的处理过程，以后再包装成函数
        val_dataset = tf.data.Dataset.from_generator(self.val_dataset_gen, (tf.float32, tf.float32),
                                                     (tf.TensorShape([None, None]), tf.TensorShape([None])))
        val_dataset = val_dataset.map(normalize_x_instance, num_parallel_calls=2)
        val_dataset = val_dataset.batch(10).repeat()

        logger.info(f"train_dataset:{train_dataset}")

        # for value in train_dataset.take(1):
        #     x, y = value
        #     print(x)
        #     print(y)

        logger.info(f"x_shape:{self.train_dataset_gen.x_shape()}")
        model = create_or_get_model(self.train_dataset_gen.x_shape())
        model.compile(optimizer=tf.keras.optimizers.RMSprop(clipvalue=1.0), loss="mae")
        logger.info(f"{model.summary()}")

        checkpoint_path = f"/tmp/{self.__class__.__name__}/cp.ckpt"

        # Create a callback that saves the model's weights
        cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                         save_weights_only=True,
                                                         verbose=1)

        log_dir = "/tmp/logs/fit/" + datetime.now().strftime("%Y%m%d-%H%M%S")
        tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

        train_step_history = model.fit(train_dataset, epochs=10,
                                       steps_per_epoch=200,
                                       validation_data=val_dataset,
                                       validation_steps=50,
                                       callbacks=[cp_callback, tensorboard_callback])