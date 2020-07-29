# -*- coding: UTF-8 -*-
"""有关数据预处理的 Steps"""
import collections
from typing import Union, Mapping, Callable, Any, Optional

from dataclasses import dataclass
import pandas as pd
from gs_research_workflow.core.gs_step_mapping import GlobalGSStepMapping

from gs_research_workflow.core.gs_step import GSStep
from gs_research_workflow.time_series.gs_steps.func_steps import FuncStrStep
from gs_research_workflow.time_series.gs_steps.ts_data_steps import SymbolTSStep


@dataclass
class TrainValSpiltStep(GSStep):
    """
    将 orig_data 的内容，拆分成 train , validation
    NOTE : 2020.01.02 修改为：该 Set 仅包括
    """

    train_val_orig_data: pd.DataFrame
    """train validation split 之前的原始数据"""

    split_ratio: float = 0.9
    """trainiing set 在 train_val_orig_data 中的占比"""

    f_after_split: Callable = None
    """在 Split 之后，数据写入 set 之前调用的函数
        Notes: 有些数据处理，必须放在 split 之后才能进行，放在该 Step 中的好处在于，可以减少两次重复的对 train / val set 的数据处理的调用
    """

    random_state: Optional[int] = None
    """eed for the random number generator (if int)"""

    def __post_init__(self):
        assert self.train_val_orig_data is not None
        assert 0. < self.split_ratio < 1.

        random_df = self.train_val_orig_data.sample(frac=1.0, random_state=self.random_state)
        train_pos = int(len(random_df) * self.split_ratio)
        self._train_set, self._val_set = random_df.iloc[:train_pos], random_df.iloc[train_pos:]
        if self.f_after_split is not None:
            self._train_set = self.f_after_split(self._train_set)
            self._val_set = self.f_after_split(self._train_set)

    @property
    def train_set(self) -> pd.DataFrame:
        return self._train_set

    @property
    def val_set(self) -> pd.DataFrame:
        return self._val_set


GlobalGSStepMapping.register(SymbolTSStep, TrainValSpiltStep, diff_name={SymbolTSStep.ts_data: TrainValSpiltStep.train_val_orig_data})
GlobalGSStepMapping.register(FuncStrStep, TrainValSpiltStep,
                             diff_name={FuncStrStep.func: TrainValSpiltStep.f_after_split})
GlobalGSStepMapping.register(FuncStrStep, TrainValSpiltStep, rule_name="train_val_orig_data",
                             diff_name={FuncStrStep.func_result: TrainValSpiltStep.train_val_orig_data})

if __name__ == "__main__":
    import pprint

    pp = pprint.PrettyPrinter(indent=1, compact=True)

    symbol_ts_step = SymbolTSStep(api="index_weight",
                                  symbols={"BigCap": "000043.SH", "MidCap": "000044.SH", "SmlCap": "000045.SH"},
                                  cols=["con_code"])
    f_after_split_step = FuncStrStep(func_body="lambda df : {t: set(df[df.index == t][df.columns[0]].tolist()) for t in df.index.unique()}")
    train_val_set = TrainValSpiltStep(_input_steps=[symbol_ts_step, f_after_split_step], split_ratio=0.85)
    pp.pprint(train_val_set.get_init_value_dict(True))
    for k, v in train_val_set.val_set.items():
        print(k)
        print(v)
