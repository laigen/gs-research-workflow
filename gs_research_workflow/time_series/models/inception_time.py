# -*- coding: UTF-8 -*-

"""
Original Paper : https://arxiv.org/pdf/1909.04939.pdf
Original Model Code : https://github.com/hfawaz/InceptionTime/blob/master/classifiers/inception.py

"""
from dataclasses import dataclass
from tensorflow import keras

from gs_research_workflow.core.dataclass_utilities import ModelHPMixIn
from gs_research_workflow.core.gs_step import GSStep
import tensorflow as tf

from gs_research_workflow.time_series.models.gs_model_mixin import GSModelMixin


class ShortCutBlock(ModelHPMixIn, keras.layers.Layer):
    """修改自 _shortcut_layer()"""

    @dataclass(frozen=True)
    class HP(GSStep):
        pass

    hp: HP = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.batch_normalization = keras.layers.BatchNormalization()
        self.add = keras.layers.Add(name="shortcut_add")
        self.activation = keras.layers.Activation('relu', name="shortcut_act")

    def build(self, batch_input_shape):
        input_tensor_shape, output_tensor_shape = batch_input_shape
        self.conv1d = keras.layers.Conv1D(filters=output_tensor_shape[-1], kernel_size=1, padding='same',
                                          use_bias=False, name="shortcut_conv1d")
        super().build(batch_input_shape)

    def call(self, inputs):
        input_tensor, output_tensor = inputs
        shortcut_y = self.conv1d(input_tensor)
        shortcut_y = self.batch_normalization(shortcut_y)
        x = self.add([shortcut_y, output_tensor])
        x = self.activation(x)
        return x


class InceptionBlock(ModelHPMixIn, keras.layers.Layer):
    """  _inception_module() """

    @dataclass(frozen=True)
    class HP(GSStep):
        stride: int = 1
        nb_filters: int = 32
        use_bottleneck: bool = True
        kernel_size: int = 41
        activation: str = "linear"

    hp: HP = None

    def __init__(self, hp, **kwargs):
        super().__init__(**kwargs)
        self.hp = hp
        kernel_size_s = [self.hp.kernel_size // (2 ** i) for i in range(3)]
        self.bottleneck_size = 32  # 作者源代码中，将 bottleneck_size hardcode，并没有作为 hp 的方式暴露出来
        self.conv_list = []
        for i in range(len(kernel_size_s)):
            self.conv_list.append(keras.layers.Conv1D(self.hp.nb_filters, kernel_size=kernel_size_s[i],
                                                      strides=self.hp.stride, padding='same',
                                                      activation=self.hp.activation,
                                                      use_bias=False, name=f"inception_conv1d_{i}"))
        self.max_pool = keras.layers.MaxPool1D(pool_size=3, strides=self.hp.stride, padding='same',
                                               name="inception_max_pool")
        self.conv_6 = keras.layers.Conv1D(filters=self.hp.nb_filters, kernel_size=1, padding='same',
                                          activation=self.hp.activation,
                                          use_bias=False, name="inception_conv1d_6")
        self.concatenate = keras.layers.Concatenate(axis=2, name="inception_concate")
        self.batch_normalization = keras.layers.BatchNormalization(name="inception_batch_norm")
        self.activation_layer = keras.layers.Activation(activation='relu', name="inception_act")
        self.use_inception: bool = False

    def build(self, batch_input_shape):
        if self.hp.use_bottleneck and int(batch_input_shape[-1]) > 1:
            self.inception = keras.layers.Conv1D(filters=self.bottleneck_size, kernel_size=1,
                                                 padding='same', activation=self.hp.activation, use_bias=False)
            self.use_inception = True
        super().build(batch_input_shape)

    def call(self, inputs):
        if self.use_inception:
            input_inception = self.inception(inputs)
        else:
            input_inception = inputs
        ls_concate = []
        for f in self.conv_list:
            ls_concate.append(f(input_inception))
        max_pool_1 = self.max_pool(inputs)
        conv_6 = self.conv_6(max_pool_1)
        ls_concate.append(conv_6)

        x = self.concatenate(ls_concate)
        x = self.batch_normalization(x)
        x = self.activation_layer(x)
        return x


class InceptionTimeBlock(ModelHPMixIn, keras.layers.Layer):
    """修改自 build_model() """

    @dataclass(frozen=True)
    class HP(GSStep):
        depth: int = 6
        use_residual: bool = True
        inception_block_hp: InceptionBlock.HP = InceptionBlock.HP()
        """model 内 block 的 hp，使用 composition 的方式组合，减少 redundancy"""

    hp: HP = None

    def __init__(self, hp: HP, **kwargs):
        super().__init__(**kwargs)
        self.hp = hp

        self.ls_inception_block = list()
        self.ls_shortcut_block = list()

        for d in range(self.hp.depth):
            self.ls_inception_block.append(InceptionBlock(self.hp.inception_block_hp, name=f"inception_{d}"))
            if self.hp.use_residual and d % 3 == 2:
                self.ls_shortcut_block.append(ShortCutBlock(name=f"shortcut_{(d - 2) / 3}"))

    def call(self, inputs):
        x = inputs
        input_res = x

        for d in range(self.hp.depth):
            x = self.ls_inception_block[d](x)

            if self.hp.use_residual and d % 3 == 2:
                n = int((d - 2) / 3)
                x = self.ls_shortcut_block[n]((input_res, x))
                input_res = x
        return x


class InceptionTimeForClassification(ModelHPMixIn, GSModelMixin, keras.Model):
    """修改自 build_model() """
    _dummy_input_shape = (1, 2, 41)  # [batch,lookback,channels]

    @dataclass(frozen=True)
    class HP(GSStep):
        nb_classes: int
        inception_time_hp: InceptionTimeBlock.HP = InceptionTimeBlock.HP()
        """model 内 block 的 hp，使用 composition 的方式组合，减少 redundancy"""

    hp: HP = None

    def __init__(self, hp: HP, **kwargs):
        super().__init__(**kwargs)
        self.hp = hp
        self.inception_time = InceptionTimeBlock(self.hp.inception_time_hp, name="inception_time")
        self.gap_layer = keras.layers.GlobalAveragePooling1D(name="global_pooling_1d")
        self.output_layer = keras.layers.Dense(self.hp.nb_classes, activation='softmax', name="classifier_output")
        
    def call(self, inputs):
        x = self.inception_time(inputs)
        gap = self.gap_layer(x)
        output = self.output_layer(gap)
        return output


if __name__ == "__main__":
    # from gs_research_workflow.time_series.data.tushare_wrapper import TuShareProData
    # from datetime import date
    # import numpy as np
    #
    # train_symbols = ["600000.SH", "600028.SH", "600050.SH", "600276.SH", "600104.SH"]
    # val_symbols = ["600019.SH", "601319.SH", "601766.SH"]
    # fields = ["turnover_rate", "pe", "pb","ps"]
    # start_t = date(2015, 1, 1)
    # end_t = date(2019, 10, 20)
    # tushare = TuShareProData()
    #
    # df_index = tushare.index_quotation_daily("000001.SH", start_t, end_t, ["close"])
    #
    # ls_train_x = []
    # ls_train_y = []
    # dummy_category = 0
    # for symbol in train_symbols:
    #     df_x = tushare.equity_basic_daily(symbol, start_t, end_t, cols=fields)
    #     # 与指数对齐以后，能得到相同的 datatime index
    #     df_x = df_index.join(df_x).fillna(method="ffill").iloc[:, 1:]
    #     category = dummy_category % 3
    #     dummy_category += 1
    #     ls_train_x.append(df_x.to_numpy())
    #     ls_train_y.append(np.int(category))
    #
    # ls_val_x = []
    # ls_val_y = []
    # dummy_category = 0
    # for symbol in val_symbols:
    #     df_x = tushare.equity_basic_daily(symbol, start_t, end_t, cols=fields)
    #     # 与指数对齐以后，能得到相同的 datatime index
    #     df_x = df_index.join(df_x).fillna(method="ffill").iloc[:, 1:]
    #     category = dummy_category % 3
    #     dummy_category += 1
    #     ls_val_x.append(df_x.to_numpy())
    #     ls_val_y.append(np.int(category))
    #
    # tf_dataset_train = tf.data.Dataset.from_tensor_slices((ls_train_x, ls_train_y)).repeat().batch(3)
    # tf_dataset_val = tf.data.Dataset.from_tensor_slices((ls_val_x, ls_val_y)).repeat().batch(3)
    #
    # # x_shape = list(ls_train_x[0].shape)
    # # print(x_shape)
    #
    # for data in tf_dataset_train.take(1):
    #     print(data[0])
    #     print(data[1])

    # ---------- model part ------------
    # hp = InceptionTime.HP(nb_classes=3, inception_block_hp=InceptionBlock.HP(use_bottleneck=False, kernel_size=60))
    # print(hp.get_init_value_dict(out_self_cls=True))
    # import yaml
    # print(yaml.dump(hp.get_init_value_dict(out_self_cls=True)))
    print(getattr(InceptionTimeForClassification, "HP").__qualname__)



    # model = InceptionTime(InceptionTime.HP(nb_classes=3,inception_block_hp=InceptionBlock.HP(use_bottleneck=True)))
    # model.build(input_shape=tf.TensorShape([None] + [128, 9]))
    # model.compile(loss='categorical_crossentropy',
    #               optimizer=keras.optimizers.Adam(),
    #               metrics=['accuracy'])
    #
    # # model.fit(tf_dataset_train, epochs=2, steps_per_epoch=3, validation_data=tf_dataset_val, validation_steps=1)
    # # print(model.summary())
    # print(model.hp.get_init_value_dict(out_self_cls=True))




