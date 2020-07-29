# -*- coding: UTF-8 -*-

from datetime import date, datetime
from typing import List, Callable, Optional, Set, Tuple, Union
import logging
from dataclasses import dataclass
import pandas as pd
import numpy as np
from gs_research_workflow.time_series.models.inception_time import InceptionTime

from gs_research_workflow.time_series.tf_data_generators.generator_related_classes import TSCallableData, MultiTSData, \
    NONE_CATEGORY_STR

logger = logging.getLogger(__name__)


@dataclass
class TSCategorySinglePeriodGeneratorDEL(MultiTSData):
    """ 适用于 所有的 x instance 的时间跨度相同，y 的 category 基于 x 的期末数据而确定
    Notes : 即将被 MultiPeriodGenerator  给替代
    """

    x_symbols_with_category: List[Tuple[str, str]]
    """
        x 的 symbol 以及相对应的 category
        Examples
        --------
            [( "6000000.SH","价值"),("600028.SH","成长")] 
    """
    category_vocabs: List[str]
    """所有的category内容
        NOTE: 这里先假定最简单的 category 的形式，即：所有的 category 是有限（总数<10）且已知的
    """
    non_category_x_symbols: Set[str]
    """不属于任何 category 的 x 样本集"""

    x_get_data_objs: List[TSCallableData]
    """
        X 取数据的信息，多个数据接口获取的内容必须是相同频度，并且会被先 join 起来
        Examples
        --------
            tushare = TuShareProData().equity_quotation_daily
            [tushare.equity_quotation_daily, ["close", "change", "vol", "amount"] , "{symbol}_" , 
            tushare.equity_basic_daily , ["turnover_rate", "pe","pb"] , "{symbol}_" ]
    """

    df_time_align: pd.DataFrame
    """用于时间对齐的df，以避免出现数据长短不一致的情况"""

    start_t: Union[date, datetime]

    end_t: Union[date, datetime]


    non_category_x_ratio: float = 1.0
    """需要用多少没有 category 信息的 x"""

    f_fill_na: Optional[Callable[[pd.DataFrame], pd.DataFrame]] = lambda x: x.fillna(method="ffill")

    def __post_init__(self):
        # NOTE: 先不使用 tf.feature_column 相关的api 将 category 数字化
        self._y_category_int = {k: i+1 for i, k in enumerate(self.category_vocabs)}
        self._y_category_int[NONE_CATEGORY_STR] = 0

        self._non_category_x = np.random.choice(list(self.non_category_x_symbols), size=int(
            min(len(self.x_symbols_with_category) * self.non_category_x_ratio, len(self.non_category_x_symbols))))

        self._all_samples = [(symbol, NONE_CATEGORY_STR) for symbol in
                             self._non_category_x] + self.x_symbols_with_category
        np.random.shuffle(self._all_samples)  # 这里先做一次 shuffle，避免集中给出 某一个 category 的内容

    def category_to_num(self, category: str) -> int:
        return self._y_category_int.get(category, 0)

    def num_to_category(self, n: int) -> str:
        if n == 0:
            return NONE_CATEGORY_STR
        return self.category_vocabs[n-1]

    @property
    def nb_classes(self) -> int:
        return len(self._y_category_int)

    def __call__(self):
        for symbol, s_category in self._all_samples:
            df = self._loop_get_data_and_join(symbol, self.x_get_data_objs, self.start_t, self.end_t)
            df = self.df_time_align.join(df)
            if self.f_fill_na:
                df = self.f_fill_na(df)
            # yield df[df.columns[1:]].to_numpy(), np.int(self.category_to_num(s_category))
            yield df[df.columns[1:]].to_numpy(), np.array([int(self.category_to_num(s_category))])


if __name__ == "__main__":
    from gs_research_workflow.time_series.data.tushare_wrapper import TuShareProData, get_category_symbols, \
        get_all_market_symbols
    import tensorflow as tf
    from tensorflow import keras

    tushare = TuShareProData()
    category_vocabs = ["密集调研", "高股息", "白马股", "养老金持股", "混改", "次新股", "回购", "兜底式增持", "筹码集中", "高送转",
                   "社保重仓", "业绩预增", "股权争夺", "破发次新", "举牌股"]
    x_symbols_with_category, all_symbols_with_category = get_category_symbols(tushare, category_vocabs)
    all_stock_symbols = get_all_market_symbols(tushare)
    all_symbols_without_category = all_stock_symbols - all_symbols_with_category

    np.random.shuffle(x_symbols_with_category)
    split_ratio = 0.8
    split_pos = int(len(x_symbols_with_category) * split_ratio)
    train_set, val_set = x_symbols_with_category[:split_pos], x_symbols_with_category[split_pos:]

    start_t = date(2018, 10, 1)
    end_t = date(2019, 10, 28)

    gen_kwargs = dict(x_symbols_with_category=train_set,
                      category_vocabs=category_vocabs,
                      non_category_x_symbols=all_symbols_without_category,
                      x_get_data_objs=[
                          TSCallableData(tushare.equity_quotation_daily,
                                         ["open", "high", "low", "close", "pre_close", "change", "pct_chg",
                                          "vol", "amount"],
                                         "{symbol}_"),
                          TSCallableData(tushare.equity_basic_daily,
                                         ["turnover_rate", "turnover_rate_f", "volume_ratio", "pe", "pe_ttm",
                                          "pb", "ps", "ps_ttm", "total_share", "float_share", "free_share",
                                          "total_mv", "circ_mv"], "{symbol}_")],
                      df_time_align=tushare.index_quotation_daily("000001.SH", start_t, end_t, ["close"]),
                      start_t=start_t,
                      end_t=end_t,
                      non_category_x_ratio=0.1,
                      f_fill_na=lambda x: x.fillna(method="ffill").fillna(0.),
                      )

    gen_train = TSCategorySinglePeriodGeneratorDEL(**gen_kwargs)
    val_kwargs = gen_kwargs.copy()
    val_kwargs["x_symbols_with_category"] = val_set
    gen_val = TSCategorySinglePeriodGeneratorDEL(**val_kwargs)

    tf_dataset_train = tf.data.Dataset.from_generator(gen_train, (tf.float32, tf.int32),
                                                      (tf.TensorShape([None, None]), tf.TensorShape([1])))\
        .repeat().batch(5)
    tf_dataset_val = tf.data.Dataset.from_generator(gen_val, (tf.float32, tf.int32),
                                                    (tf.TensorShape([None, None]), tf.TensorShape([1])))\
        .repeat().batch(5)

    # for data in tf_dataset_val.take(1):
    #     print(data)

    model = InceptionTime(len(category_vocabs) + 1)
    model.compile(loss=tf.keras.losses.CategoricalCrossentropy(),
                  optimizer=keras.optimizers.Adam(),
                  metrics=['accuracy'])

    checkpoint_path = f"/tmp/inception_time/test1/cp.ckpt"

    # Create a callback that saves the model's weights
    cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                     save_weights_only=True,
                                                     verbose=1)
    log_dir = "/tmp/logs/inception_time/" + datetime.now().strftime("%Y%m%d-%H%M%S")
    tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

    model.fit(tf_dataset_train, epochs=10, steps_per_epoch=500, validation_data=tf_dataset_val, validation_steps=100,
              callbacks=[cp_callback, tensorboard_callback])
    print(model.summary())
