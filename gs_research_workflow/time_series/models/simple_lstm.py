# -*- coding: UTF-8 -*-
"""
一个作为对比的简化版的 lstm 模型，参考链接：
https://www.tensorflow.org/tutorials/structured_data/time_series
"""
from dataclasses import dataclass
from gs_research_workflow.core.gs_step import GSStep

from gs_research_workflow.core.dataclass_utilities import ModelHPMixIn
from tensorflow import keras


class SimpleLSTM(ModelHPMixIn, keras.Model):
    @dataclass(frozen=True)
    class HP(GSStep):
        nb_classes: int
        lstm_units: int = 8
        l1_factor: float = 0.01
        l2_factor: float = 0.01

    hp: HP = None

    def __init__(self, hp: HP, **kwargs):
        super().__init__(**kwargs)
        self.hp = hp

        self.output_layer = keras.layers.Dense(self.hp.nb_classes, activation='softmax',
                                               kernel_regularizer=keras.regularizers.l1(self.hp.l1_factor),
                                               bias_regularizer=keras.regularizers.l2(self.hp.l2_factor))

    def build(self, batch_input_shape):
        # ?? 这里 lstm 的 units 这个参数是否需要作为 hp ??
        self.lstm_layer = keras.layers.LSTM(self.hp.lstm_units, input_shape=batch_input_shape[-2:])

    def call(self, inputs):
        x = self.lstm_layer(inputs)
        x = self.output_layer(x)
        return x
