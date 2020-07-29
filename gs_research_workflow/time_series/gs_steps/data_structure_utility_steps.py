# -*- coding: UTF-8 -*-
"""
提供一些数据结构相关的 Step
"""
from dataclasses import dataclass
from typing import List, Any, Mapping

from gs_research_workflow.core.gs_step import GSStep
from gs_research_workflow.time_series.gs_steps.local_context_step import reg_fields_from_local_step


@dataclass
class KeyValueListToMappingStep(GSStep):
    """部分场景下，为了更方便的展示 feature 的内容，加入通过 Key Value 两个 list 的方式得到 dictionary 对象
    """
    key_list: List[Any]
    value_list: List[Any]

    def __post_init__(self):
        assert len(self.key_list) == len(self.value_list)
        self._mapping_data = {k: v for k, v in zip(self.key_list, self.value_list)}

    @property
    def mapping_data(self) -> Mapping:
        return self._mapping_data


reg_fields_from_local_step(KeyValueListToMappingStep)

if __name__ == "__main__":
    kv_convert_step = KeyValueListToMappingStep(key_list=["BigCap", "MidCap", "SmlCap"],
                                                value_list=["000043.SH", "000044.SH", "000045.SH"])
    print(kv_convert_step.mapping_data)
