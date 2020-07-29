# -*- coding: UTF-8 -*-
"""
从聚源的 RDBS 中读取数据，并进行更新维护 DCE 中内容的 env
"""
# from gs_framework.decorators import init_actions
# from gs_framework.stateful_srv_base_classes import Env
import os
import time
from builtins import slice
from datetime import date, datetime

from enum import Enum
from pathlib import Path
from typing import List

from arctic import Arctic, TICK_STORE, CHUNK_STORE
from arctic.chunkstore.date_chunker import DateChunker
from arctic.chunkstore.passthrough_chunker import PassthroughChunker
from pandas import MultiIndex

from gs_research_workflow.common.sql_statement_helper import SQLStatementHelper as sh
from gs_research_workflow.external_data.data_vendor.jy.ddl_entities.constant.SecuMain import SecuMain
from gs_research_workflow.external_data.data_vendor.jy.ddl_entities.corp_chn_widthadjusted.QT_DailyQuote import \
    QT_DailyQuote
from gs_research_workflow.external_data.db_server_resource.mongo import get_mongo_admin_conn_str
from gs_research_workflow.external_data.db_server_resource.rdbs import get_db_conn, RDBSDataSetByGS
import logging
import pandas as pd
import numpy as np
import tensorflow as tf

logger = logging.getLogger(__name__)


class FinI(Enum):  # financial instrument
    """获取证券相关的类型枚举值，如：股票、基金、债券等"""
    Equity = 1
    MarketIndex = 2


# 访问聚源数据库经常会用到的一些常量，避免数据库的 join ，先 hardcode 在 代码里
def get_security_category_type(entity_type: FinI) -> List[int]:
    if entity_type == FinI.Equity:
        return [1]
    elif entity_type == FinI.MarketIndex:
        return [4]
    else:
        raise Exception("Unknown entity type {}".format(entity_type))


def get_security_listed_sector_type(entity_type: FinI) -> List[int]:
    """获取证券相关的上市板块枚举值，如：主板，创业板，中小企业板"""
    if entity_type == FinI.Equity or entity_type == FinI.MarketIndex:
        # 主板，创业板，中小企业板
        return [1, 2, 6]
    else:
        raise Exception("Unknown entity type {}".format(entity_type))


class JYDBManipulationEnv:  # (Env)
    """
        聚源数据的处理 Env 对象，提供的功能：
        1） RDBS 中读取历史数据， 并(通过arctic)存入到 mongo，同时写入到 dce 中
        2) 定时更新新的 Snapshot 数据
    """
    # @init_actions()
    def __init__(self):
        super().__init__()

        self._sql_db = get_db_conn(RDBSDataSetByGS.JY)

    def convert_a_share_mkt_history_data(self):
        sel_cols = {"close_price": QT_DailyQuote.ClosePrice,
                    # "open_price": QT_DailyQuote.OpenPrice,
                    # "high_price": QT_DailyQuote.HighPrice,
                    # "prev_close_price": QT_DailyQuote.PrevClosePrice,
                    # "low_price": QT_DailyQuote.LowPrice,
                    # "turnover_deals_count": QT_DailyQuote.TurnoverDeals,
                    # "turnover_dollar_volume": QT_DailyQuote.TurnoverValue,
                    # "turnover_shares_volume": QT_DailyQuote.TurnoverVolume,
                    "date": QT_DailyQuote.TradingDay,
                    "o": SecuMain.SecuCode
                    }
        sql = f"SELECT {sh.select_with_alias(sel_cols)} FROM {sh.from_(QT_DailyQuote)} " \
            f" {sh.inner_join(QT_DailyQuote.InnerCode,[SecuMain.InnerCode])} " \
            f" WHERE {sh.where_in([(SecuMain.SecuCategory,get_security_category_type(FinI.Equity)),(SecuMain.ListedSector,get_security_listed_sector_type(FinI.Equity))])}"

        # logger.info(f"sql statement:'{sql}'")
        start = time.time()
        df_all_data: pd.DataFrame = pd.read_sql_query(sql, self._sql_db, index_col=["date", "o"])
        print(f"read from rdbs: {time.time()-start}")
        file_path = os.path.join("/tmp", "jy_market.pkl")
        df_all_data.to_pickle(file_path, compression="gzip", protocol=4)
        # df_all_data: pd.DataFrame = pd.read_pickle(file_path, compression="gzip")

        logger.info(f"db summary:'{df_all_data.describe()}'")
        logger.info(f"db head:'{df_all_data.head(10)}'")

    def load_all_close_price(self) -> pd.DataFrame:
        file_path = os.path.join("/tmp", "jy_market.pkl")
        df_all_data: pd.DataFrame = pd.read_pickle(file_path, compression="gzip")
        # logger.info(f"db summary:'{df_all_data.describe()}'")
        # logger.info(f"db head:'{df_all_data.head(10)}'")
        return df_all_data

    def save_to_arctic(self):
        # see https://github.com/manahl/arctic/blob/master/howtos/201507_demo_pydata.py
        arctic_store = Arctic(get_mongo_admin_conn_str())
        # print(arctic_store.list_libraries())
        closeprice_lib = arctic_store["jy_equity_closeprice"]
        # print(closeprice_lib)
        df = self.load_all_close_price()
        # print(df.index.to_frame()["o"].unique())

        # df.reset_index(level=1, inplace=True)
        # print(df)

        df2 = df.pivot_table(values="close_price",index="t",columns="o",aggfunc=np.mean)
        # print(df2)
        #
        # print(df2.columns)
        i = 0
        for col in df2.columns:
            df3 = df2.loc[:,col]
            df3 = df3.dropna(axis=0)
            closeprice_lib.write(col, df3)
            i+=1
            print(f"{i}:{col}")
            # if i > 5 :
            #     break

        print(closeprice_lib.list_symbols())

    def save_to_arctic_v2(self):
        # see https://github.com/manahl/arctic/blob/master/howtos/201507_demo_pydata.py
        arctic_store = Arctic(get_mongo_admin_conn_str())
        # print(arctic_store.list_libraries())
        # arctic_store.initialize_library("jy_equity_closeprice_v2")
        closeprice_lib = arctic_store["jy_equity_closeprice_v2"]
        # print(closeprice_lib)
        df = self.load_all_close_price()
        # print(df.index.to_frame()["o"].unique())

        df2 = df.pivot_table(values="close_price", index="t", columns="o", aggfunc=np.mean)
        closeprice_lib.write("close_price", df2)
        print(closeprice_lib.list_symbols())


    def read_all_data_from_arctic(self):
        arctic_store = Arctic(get_mongo_admin_conn_str())
        closeprice_lib = arctic_store["jy_equity_closeprice"]
        start = time.time()
        rows_read = 0
        for s in closeprice_lib.list_symbols():
            rows_read += len(closeprice_lib.read(s).data)
        print("Symbols: %s Rows: %s  Time: %s  Rows/s: %s" % (len(closeprice_lib.list_symbols()),
                                                              rows_read,
                                                              (time.time() - start),
                                                              rows_read / (time.time() - start)))
        pass


    def read_all_data_from_arctic_v2(self):
        arctic_store = Arctic(get_mongo_admin_conn_str())
        closeprice_lib = arctic_store["jy_equity_closeprice_v2"]
        start = time.time()
        rows_read = 0
        for s in closeprice_lib.list_symbols():
            rows_read += len(closeprice_lib.read(s).data)
        print("Symbols: %s Rows: %s  Time: %s  Rows/s: %s" % (len(closeprice_lib.list_symbols()),
                                                              rows_read,
                                                              (time.time() - start),
                                                              rows_read / (time.time() - start)))

        print(closeprice_lib.read("close_price").data)
        pass

    def save_to_arctic_tickstore(self):
        # not work
        arctic_store = Arctic(get_mongo_admin_conn_str())
        arctic_store.delete_library("jy_otv_tickstore")
        arctic_store.initialize_library("jy_otv_tickstore", lib_type=TICK_STORE)
        lib_tick_store = arctic_store["jy_otv_tickstore"]
        # lib_tick_store._chunk_size = 8396800

        # print(closeprice_lib)
        df = self.load_all_close_price()
        # print(df.index.to_frame()["o"].unique())

        df2 = df.pivot_table(values="close_price", index="t", columns="o", aggfunc=np.mean)

        df2.index = df2.index.tz_localize("Asia/Shanghai")
        # df2.reset_index(df2.index.tz_localize("Asia/Shanghai"), inplace=True)
        # print(df2.head())



        lib_tick_store.write("close_price", df2)
        # print(lib_tick_store.list_symbols())

    def save_to_chunkstore(self):
        arctic_store = Arctic(get_mongo_admin_conn_str())
        arctic_store.delete_library("jy_otv_chunkstore")
        arctic_store.initialize_library("jy_otv_chunkstore", lib_type=CHUNK_STORE)
        lib_chunk_store = arctic_store["jy_otv_chunkstore"]
        # lib_tick_store._chunk_size = 8396800

        # print(closeprice_lib)
        df = self.load_all_close_price()
        df.sort_index(axis=0, ascending=True, inplace=True)
        print(df)

        # df2 = df.pivot_table(values="close_price", index="t", columns="o", aggfunc=np.mean)

        # df2.index = df2.index.tz_localize("Asia/Shanghai")
        # df2.index.rename("date",inplace=True)
        # df2.reset_index(df2.index.tz_localize("Asia/Shanghai"), inplace=True)
        # print(df2.head())
        # print(df2[-100:])

        start = time.time()
        lib_chunk_store.write("close_price", df, chunk_size="M")
        print(f"total write time {time.time()-start} ")
        # 9,688,283 rows 写入时间，
        #       52.9 sec, chunk_size = D
        #       12.3 sec , chunk_size = M
        #       12.3 sec , chunk_size = Y

        # 试验结论：整个 OTV 作为 DateChunker 写入的时间过长(30min还没完成)。卡在 dataframe 的 serializer.serialize 上
        # lib_chunk_store.write("close_price", df2, chunker=DateChunker(), chunk_size="D")

        # lib_chunk_store.write("close_price", df2, chunker=PassthroughChunker(), chunk_size="D")

    def save_to_chunkstore_per_symbol(self):
        lib_name = "jy_equity_mkt_data"
        arctic_store = Arctic(get_mongo_admin_conn_str())
        arctic_store.delete_library(lib_name)
        arctic_store.initialize_library(lib_name, lib_type=CHUNK_STORE)
        lib_chunk_store = arctic_store[lib_name]

        df = self.load_all_close_price()

        df2 = df.pivot_table(values="close_price", index="t", columns="o", aggfunc=np.mean)
        df2.index.rename("date", inplace=True)

        i = 0
        for col in df2.columns:
            df3 = df2.loc[:, col]
            df3 = df3.dropna(axis=0)
            lib_chunk_store.write(col, df3, chunker=DateChunker(), chunk_size="D")
            i += 1
            if i % 2 == 0:
                print(f"{i}:{col}")

    def read_from_chunkstore(self, start: date, end: date, cols: List[str]):
        # start = time.time()
        # df = self.load_all_close_price()
        # print(f"total read time {time.time() - start} ")
        # 9,595,866 rows 读取时间 0.48 sec , 本地 压缩的 pickles 文件

        arctic_store = Arctic(get_mongo_admin_conn_str())
        lib_name = "jy_chn_equity_otvn_chunkstore"
        lib_chunk_store = arctic_store[lib_name]

        symbol_name = "mkt_data"

        run_start = time.time()
        # data = lib_chunk_store.read("close_price")
        data: pd.DataFrame = lib_chunk_store.read(symbol_name, chunk_range=pd.date_range(start, end),
                                                  filter_data=True,
                                                  columns=cols)
        logger.info(f"total read time {time.time() - run_start} ")

        # [5Y (2012/01/15 - 2017/12/15)] 3,906,128 rows  , [ALL] 9,688,283 rows
        #  chunk_size = Y , 16.74 secs(5Y) ,  38.89 secs(ALL)
        #  chunk_size = M , 16.83 secs(5Y) ,  39.73 secs(ALL)
        #  chunk_size = D , 23.75 secs(5Y) ,  74.94 secs(ALL)

        # 增加读取的 v 的 column 对性能基本没影响，多读取两列 约增加了 0.5 sec
        # 参考: mysql 中读取 10Y(2000-2009, 3,187,574 rows) 数据约 120 secs，写入 arctic 约 77 secs


        # 之前错误的测试结果
        # # 9,595,866 rows 读取时间 11.68 sec , chunk_size = M （ALL）
        # # 6,361,499 rows 读取时间 8.19 sec , chunk_size = M （10Y）
        # # 4,018,657 rows 读取时间 5.24 sec , chunk_size = M （5Y）
        # # 8,48,959  rows 读取时间 1.16 sec , chunk_size = M （1Y）

        return data


    def show_chunk_store_info(self):
        arctic_store = Arctic(get_mongo_admin_conn_str())
        lib_chunk_store = arctic_store["jy_otv_chunkstore"]
        print("list_symbols")
        print(lib_chunk_store.list_symbols())
        print("get_info")
        print(lib_chunk_store.get_info("close_price"))
        print("chunk_ranges")
        print(list(lib_chunk_store.get_chunk_ranges("close_price")))

    def _convert_period_equity_mkt_data_to_arctic(self, start: date, end: date, lib_chunk_store, symbol: str,
                                                  chunk_period: str, is_write: bool):
        """将一个时间跨度内的 market data 转储成 arctic 的 chunk store """
        sel_cols = {"close_price": QT_DailyQuote.ClosePrice,
                    "open_price": QT_DailyQuote.OpenPrice,
                    "high_price": QT_DailyQuote.HighPrice,
                    "prev_close_price": QT_DailyQuote.PrevClosePrice,
                    "low_price": QT_DailyQuote.LowPrice,
                    "turnover_deals_count": QT_DailyQuote.TurnoverDeals,
                    "turnover_dollar_volume": QT_DailyQuote.TurnoverValue,
                    "turnover_shares_volume": QT_DailyQuote.TurnoverVolume,
                    "date": QT_DailyQuote.TradingDay,
                    "o": SecuMain.SecuCode
                    }
        sql = f"SELECT {sh.select_with_alias(sel_cols)} FROM {sh.from_(QT_DailyQuote)} " \
            f" {sh.inner_join(QT_DailyQuote.InnerCode, [SecuMain.InnerCode])} " \
            f" WHERE {sh.where_in([(SecuMain.SecuCategory, get_security_category_type(FinI.Equity)), (SecuMain.ListedSector, get_security_listed_sector_type(FinI.Equity))])} " \
            f" AND {sh.where_compare_op([(QT_DailyQuote.TradingDay,'>=',start),(QT_DailyQuote.TradingDay,'<',end)])}"
        run_start = time.time()
        df_all_data: pd.DataFrame = pd.read_sql_query(sql, self._sql_db, index_col=["date", "o"])
        df_all_data.sort_index(axis=0, ascending=True, inplace=True)
        logger.info(f"read {start}-{end} market data, cost {time.time() - run_start} secs , total {len(df_all_data)} rows")

        run_start = time.time()
        if is_write :
            lib_chunk_store.write(symbol, df_all_data, chunk_size=chunk_period)
        else:
            lib_chunk_store.append(symbol, df_all_data, upsert=True)
        logger.info(f"Write arctic time : {time.time()-run_start} secs ")

    def convert_mkt_history_data(self):
        arctic_store = Arctic(get_mongo_admin_conn_str())
        lib_name = "jy_chn_equity_otvn_chunkstore"

        arctic_store.delete_library(lib_name)
        arctic_store.initialize_library(lib_name, lib_type=CHUNK_STORE)
        lib_chunk_store = arctic_store[lib_name]

        # 先 hardcode 日期范围，可以有更优雅的表达
        for i, t_period in enumerate([(date(1990, 1, 1), date(2000, 1, 15)), (date(2000, 1, 15), date(2010, 1, 15)),
                                      (date(2010, 1, 15), date(2020, 1, 1))]):
            # 测算下来，日频数据，用 "M" 作为 chunk_size 的写入和读取效率是综合最高的
            self._convert_period_equity_mkt_data_to_arctic(t_period[0], t_period[1], lib_chunk_store, "mkt_data", "M",
                                                           i == 0)

    def test_tf_data(self):
        np.set_printoptions(precision=2)
        df = self.read_from_chunkstore(date(2017, 1, 15), date(2017, 12, 15),
                                       ["close_price", "open_price", "turnover_deals_count"])
        dataset = tf.data.Dataset.from_tensor_slices(df.to_numpy())
        for ele in dataset.take(2):
            print(ele)
        # print(dataset.element_spec)
        # item = next(iter(dataset))
        # print(item.numpy())


class TestTSDataGenerator:
    # 以下这些属于 Hyper Parameter，可以参与到 Tune
    LOOKBACK = 120
    PREDICT_COUNT = 5  # 预测之后的N期数据
    FEATURES = ["close_price", "open_price", "turnover_deals_count"]
    TARGET_COLUMN = "close_price"


    # 以下这些一般不参与到 tune
    # start_t = date(1990, 1, 1)
    # end_t = date(2018, 12, 31)
    x_symbols = ["600000", "600050", "600519"]  # 示意用，一般是板块的股票，这个symbol 的序是与 model 强关联的
    y_symbol = "600000"  # 暂时先用一个股票代替被预测的指数

    def __init__(self, start_t=date(2010, 1, 1), end_t=date(2016, 12, 31)):
        # 从 pkl 读数据是另外一个 class 处理
        # cache 的文件路径将根据 start_t , end_t , FEATURES 做 hash
        # 暂时根据 start / end 确定存盘路径，以后改成只有一份全部数据的 pickle
        cache_file_path = os.path.join("/tmp", f"TestTSDataGenerator_{start_t.isocalendar()}_{end_t.isoformat()}.pkl")
        self.original_data: pd.DataFrame = None
        self.df_x_to_loop: pd.DataFrame = None
        self.df_y_to_loop: pd.DataFrame = None

        if os.path.isfile(cache_file_path):
            self.original_data = pd.read_pickle(cache_file_path, compression="gzip")
        else:  # 从  arctic 读取数据并缓存
            arctic_store = Arctic(get_mongo_admin_conn_str())
            lib_name = "jy_chn_equity_otvn_chunkstore"
            lib_chunk_store = arctic_store[lib_name]
            symbol_name = "mkt_data"
            self.original_data: pd.DataFrame = lib_chunk_store.read(symbol_name,
                                                                    chunk_range=pd.date_range(start_t, end_t),
                                                                    filter_data=True,
                                                                    columns=self.FEATURES)
            self.original_data.to_pickle(cache_file_path, compression="gzip", protocol=4)

    # 将 原始的 OTVVV 数据转成适合于 成为 tf.dataset 一个 sample 的结构内容
    def df_transform(self):
        # 目前没有将该数据内容做 cache， 应该仅保留该 df 的 local cache 即可
        df_x = self.original_data.copy().reset_index()
        df_x = df_x.loc[df_x["o"].isin(self.x_symbols)]
        df_x = df_x.pivot(index="date", columns="o", values=self.FEATURES)
        # 暂时先不优化定义的位置
        self.df_x_to_loop: pd.DataFrame = df_x.fillna(method="ffill")

        df_y = self.original_data.copy().reset_index()  # 这里应该改成取指数数据（暂时还未获取该数据）
        df_y = df_y.loc[df_y["o"].isin([self.y_symbol])]
        df_y = df_y.pivot(index="date", columns="o", values=self.TARGET_COLUMN)
        self.df_y_to_loop: pd.DataFrame = df_y.fillna(method="ffill")
        assert len(self.df_x_to_loop) == len(self.df_y_to_loop)

        # logger.info(f"df_x_to_loop:{self.df_x_to_loop}")
        # logger.info(f"df_y_to_loop:{self.df_y_to_loop[self.y_symbol][0:10].to_numpy()}")

    def x_shape(self) -> tf.TensorShape:
        return tf.TensorShape([self.LOOKBACK, len(self.x_symbols) * len(self.FEATURES)]).as_list()

    def __call__(self):
        for i in range(len(self.df_x_to_loop) - self.LOOKBACK - self.PREDICT_COUNT-1):
            # logger.info(f"y:{self.df_y_to_loop[self.y_symbol][i + self.LOOKBACK:i + self.LOOKBACK + self.PREDICT_COUNT].to_numpy()}")
            yield (self.df_x_to_loop[i:i + self.LOOKBACK].to_numpy(),
                   self.df_y_to_loop[self.y_symbol][i + self.LOOKBACK:i + self.LOOKBACK + self.PREDICT_COUNT].to_numpy())



def create_or_get_model(input_shape):
    multi_step_model = tf.keras.models.Sequential()
    multi_step_model.add(tf.keras.layers.LSTM(32,
                                              return_sequences=True,
                                              input_shape=input_shape))
    multi_step_model.add(tf.keras.layers.LSTM(16, activation='relu'))
    multi_step_model.add(tf.keras.layers.Dense(TestTSDataGenerator.PREDICT_COUNT))
    return multi_step_model


def normalize_x_instance(x, y):
    x_mean = tf.math.reduce_mean(x, 0)
    x_std = tf.math.reduce_std(x, 0)

    # y_mean = tf.math.reduce_mean(y,0)
    # y_std = tf.math.reduce_std(y,0)

    # Y 的 normalize 的方式有问题
    # return (x - x_mean) / x_std, (y - y_mean) / y_std
    logger.info(f"x:{(x - x_mean) / x_std}")
    logger.info(f"y:{y}")
    print(f"y:{y}")
    return (x - x_mean) / x_std, y


class TestTFDatePipline:
    def __init__(self):
        self.train_dataset_gen = TestTSDataGenerator(start_t=date(2010, 1, 1), end_t=date(2016, 12, 31))
        self.train_dataset_gen.df_transform()

        self.val_dataset_gen = TestTSDataGenerator(start_t=date(2017, 1, 1), end_t=date(2018, 12, 31))
        self.val_dataset_gen.df_transform()

    def ds_pipline(self):
        # data = next(iter(source_gen()))
        # print(data.shape)
        train_dataset = tf.data.Dataset.from_generator(self.train_dataset_gen, (tf.float32, tf.float32),
                                                       (tf.TensorShape([self.train_dataset_gen.LOOKBACK,
                                                                        len(self.train_dataset_gen.x_symbols) * len(
                                                                            self.train_dataset_gen.FEATURES)]),
                                                        tf.TensorShape([self.train_dataset_gen.PREDICT_COUNT])))
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

        checkpoint_path = "/tmp/training_1/cp.ckpt"
        checkpoint_dir = os.path.dirname(checkpoint_path)

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
