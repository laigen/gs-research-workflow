# -*- coding: utf-8 -*-

"""与 model 有关的一些常量的定义内容"""

TS_MASK_VAL: float = 1000000.

TS_NAN_VAL: float = 100.
"""NAN不参与 loss 计算，具体的取值应该不会有太大的影响"""

TS_UNMASK_VAL: float = 5000.
"""用于在 y_true 中，未 mask 的数据项，以便于 loss function 中只看 mask_val 的 true"""


PADDING_VAL: float = 200.
PADDING_POS: int = 0
PADDING_TOKEN: int = 0
