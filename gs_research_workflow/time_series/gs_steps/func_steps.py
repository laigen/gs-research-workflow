# -*- coding: UTF-8 -*-
"""
与函数有关的Step
"""
from typing import Optional, Callable, List, Any, Mapping

from dataclasses import dataclass, field
from gs_research_workflow.core.gs_step_mapping import GlobalGSStepMapping

from gs_research_workflow.common.serialization_utilities import str_to_cls, cls_to_str

from gs_research_workflow.core.gs_step import GSStep
from gs_research_workflow.time_series.gs_steps.local_context_step import reg_fields_from_local_step


@dataclass
class FuncStrStep(GSStep):
    """从 str 得到 callable 对象的 Step"""
    func_body: Optional[str] = None
    """提供 function body 进行动态编译后得到的 function 的内容，一般为 lambda 的函数
    Examples
    --------
        func_body = "lambda x: print(x)"
    """

    func_obj_str: Optional[str] = None
    """Function Object 对象的 string, __module__:__qualname__"""

    single_input: Optional[Any] = None
    """为了避免产生二义性，增加了一个单值输入的情况"""

    args: Optional[List[Any]] = None

    kwargs: Optional[Mapping[str, Any]] = None

    def __post_init__(self):
        assert bool(self.func_body) != bool(self.func_obj_str)
        self._func = None
        if self.func_body:
            self._func = eval(self.func_body)
        else:
            self._func = str_to_cls(self.func_obj_str)

    @property
    def func(self) -> Callable:
        return self._func

    @property
    def func_result(self) -> Any:
        """执行函数，并将结果返回"""
        args = self.args
        if self.single_input is not None:
            args = [self.single_input]
        args = [] if args is None else args
        kwargs = {} if self.kwargs is None else self.kwargs or {}
        return self.func(*args, **kwargs)

# 适用于 function 搭建 pip line
GlobalGSStepMapping.register(FuncStrStep, FuncStrStep, rule_name="single_ret_pip",
                             diff_name={FuncStrStep.func_result: FuncStrStep.single_input})

GlobalGSStepMapping.register(FuncStrStep, FuncStrStep, rule_name="args_ret_pip",
                             diff_name={FuncStrStep.func_result: FuncStrStep.args})

GlobalGSStepMapping.register(FuncStrStep, FuncStrStep, rule_name="kwargs_ret_pip",
                             diff_name={FuncStrStep.func_result: FuncStrStep.kwargs})

reg_fields_from_local_step(FuncStrStep)


if __name__ == "__main__":
    def print_x(x):
        print(x)

    # f_step = FuncStrStep(func_body="lambda x: print(x)")
    f_step = FuncStrStep(func_obj_str=cls_to_str(print_x))
    f_step.func("abc")





