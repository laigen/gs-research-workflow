# -*- coding: UTF-8 -*-

"""适用于从 local context (通常是在 Config Tree 不同的叶节点上使用相同的literal parameter) """
from dataclasses import dataclass, is_dataclass, fields
from typing import Dict, Any

from gs_research_workflow.core.gs_step_mapping import GlobalGSStepMapping

from gs_research_workflow.core.gs_step import GSStep


@dataclass
class GetContextStep(GSStep):
    local_var_name: str

    def SET_CONTEXT(self, context: Dict):
        """这个函数由系统负责进行设置"""
        # assert "LOCAL" in context
        self._context = context  # 暂时 context 中只有一个 local 的 key, local 是一个dictionary

    @property
    def val(self) -> Any:
        """val in local context"""
        assert hasattr(self, "_context"), f"SET_CONTEXT() hasn't been called!"
        assert self.local_var_name in self._context["LOCAL"]
        return self._context["LOCAL"][self.local_var_name]


def reg_fields_from_local_step(cls):
    """将 cls 的所有 field 以 field_name 注册能够从 GetLocalStep 的 Prop 进行赋值"""
    assert issubclass(cls, GSStep)
    assert is_dataclass(cls)
    for curr_field in fields(cls):
        if not curr_field.init:
            continue
        GlobalGSStepMapping.register(GetContextStep, cls, rule_name=curr_field.name,
                                     diff_name={GetContextStep.val: curr_field})
