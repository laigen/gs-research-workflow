# -*- coding: utf-8 -*-

"""
NNI 的 Search Space 的 python 对象封装，目的：
    1） 用户定义 Search Space 的时候，可以不用直接编辑 search space 的json

好处：
    1) 数据和存储的文件位置分开。这样同一份的 Search Space 可以在多个 experiment 中共用
    2) experiment 相关的配置文件，由 Platform 负责维护，可以根据需要，在运行前 dump 到特定的位置

See : https://nni.readthedocs.io/en/latest/Tutorial/SearchSpaceSpec.html
"""
import json
from typing import List, Union, Optional, Tuple, Dict

from dataclasses import dataclass

from gs_research_workflow.common.serialization_utilities import escape_nni_choice_item


@dataclass(frozen=True)
class SearchSpaceItem:
    name: str
    """parameter name"""

    def get_dict_item(self) -> Dict:
        return {self.name: {"_type": self._type, "_value": self._value()}}


@dataclass(frozen=True)
class SearchSpace:
    parameters: List[SearchSpaceItem]

    @property
    def dict_val(self) -> Dict:
        ret = dict()
        for v in self.parameters:
            ret.update(v.get_dict_item())

        return ret


@dataclass(frozen=True)
class HighLowValue:
    low: Union[float, int]
    high: Union[float, int]

    def _value(self) -> List:
        _val = [self.low, self.high]
        if hasattr(super(), "_value"):
            _val.extend(super()._value())
        return _val


@dataclass(frozen=True)
class MuSigmaValue:
    mu: Union[float, int]
    sigma: Union[float, int]

    def _value(self) -> List:
        _val = [self.mu, self.sigma]
        if hasattr(super(), "_value"):
            _val.extend(super()._value())
        return _val


@dataclass(frozen=True)
class QuantileDiscreteValue:
    q: Union[float, int]

    def _value(self) -> List:
        return [self.q]

# region SearchSpace Items


@dataclass(frozen=True)
class Choice(SearchSpaceItem):
    """
    Which means the variable’s value is one of the options. Here options should be a list of numbers or a list of strings. Using arbitrary objects as members of this list (like sublists, a mixture of numbers and strings, or null values) should work in most cases, but may trigger undefined behaviors.
    """
    _type = "choice"

    options: Optional[List[Union[float, int, str, bool, Tuple[str, Optional['Choice']]]]]
    """
    float / int / str 将输入为 array
    Tuple[str,Choice]  是 Choice 的 nested sub-search-space 结构形式, str 为 _name
    """

    def _value(self) -> List:
        if self.options is None:
            return None
        ret = list()
        for el in self.options:
            if isinstance(el, tuple) and len(el) == 2 and isinstance(el[0], str):
                item_dict = {"_name": el[0]}
                if el[1] is not None and isinstance(el[1], Choice):
                    item_dict.update(el[1].get_dict_item())
                ret.append(item_dict)
            elif isinstance(el, (float, str, int, bool, list, dict)):
                ret.append(escape_nni_choice_item(el))
            else:
                raise RuntimeError(f"Unknown choice item {el}")
        return ret


@dataclass(frozen=True)
class RandIntItem(SearchSpaceItem):
    """Choosing a random integer from lower (inclusive) to upper (exclusive).
        Note: Different tuners may interpret randint differently. Some (e.g., TPE, GridSearch) treat integers from lower to upper as unordered ones, while others respect the ordering (e.g., SMAC). If you want all the tuners to respect the ordering, please use quniform with q=1
    """
    _type = "randint"

    lower: int
    upper: int


@dataclass(frozen=True)
class Uniform(SearchSpaceItem, HighLowValue):
    """
    Which means the variable value is a value uniformly between low and high.
    When optimizing, this variable is constrained to a two-sided interval.
    """
    _type = "uniform"


# NOTE: quantile 的类必须在 HighLow 之后，生成 _value 信息用到该数据
@dataclass(frozen=True)
class QUniform(SearchSpaceItem, HighLowValue, QuantileDiscreteValue):
    """
    Which means the variable value is a value like clip(round(uniform(low, high) / q) * q, low, high), where the clip operation is used to constraint the generated value in the bound. For example, for _value specified as [0, 10, 2.5], possible values are [0, 2.5, 5.0, 7.5, 10.0]; For _value specified as [2, 10, 5], possible values are [2, 5, 10].
    """
    _type = "quniform"


@dataclass(frozen=True)
class LogUniform(SearchSpaceItem, HighLowValue):
    """
    Which means the variable value is a value drawn from a range [low, high] according to a loguniform distribution like exp(uniform(log(low), log(high))), so that the logarithm of the return value is uniformly distributed.
    When optimizing, this variable is constrained to be positive
    """
    _type = "loguniform"


@dataclass(frozen=True)
class QLogUniform(SearchSpaceItem, HighLowValue, QuantileDiscreteValue):
    """
    Which means the variable value is a value like clip(round(loguniform(low, high) / q) * q, low, high), where the clip operation is used to constraint the generated value in the bound.
    Suitable for a discrete variable with respect to which the objective is “smooth” and gets smoother with the size of the value, but which should be bounded both above and below.
    """
    _type = "qloguniform"


@dataclass(frozen=True)
class Normal(SearchSpaceItem, MuSigmaValue):
    """
    Which means the variable value is a real value that’s normally-distributed with mean mu and standard deviation sigma. When optimizing, this is an unconstrained variable.
    """
    _type = "normal"


@dataclass(frozen=True)
class QNormal(SearchSpaceItem, MuSigmaValue, QuantileDiscreteValue):
    """
    Which means the variable value is a value like round(normal(mu, sigma) / q) * q
    Suitable for a discrete variable that probably takes a value around mu, but is fundamentally unbounded.
    """
    _type = "qnormal"


@dataclass(frozen=True)
class LogNormal(SearchSpaceItem, MuSigmaValue):
    """
    Which means the variable value is a value drawn according to exp(normal(mu, sigma)) so that the logarithm of the return value is normally distributed. When optimizing, this variable is constrained to be positive.
    """
    _type = "lognormal"


@dataclass(frozen=True)
class QLogNormal(SearchSpaceItem, MuSigmaValue, QuantileDiscreteValue):
    """
    Which means the variable value is a value like round(exp(normal(mu, sigma)) / q) * q
Suitable for a discrete variable with respect to which the objective is smooth and gets smoother with the size of the variable, which is bounded from one side.
    """
    _type = "qlognormal"

# endregion


if __name__ == "__main__":
    def case1():
        # tutorial case : https://nni.readthedocs.io/en/latest/Tutorial/SearchSpaceSpec.html
        ss = SearchSpace(parameters=[
            Uniform(name="dropout_rate", low=0.1, high=0.5),
            Choice(name="conv_size", options=[2, 3, 5, 7]),
            Choice(name="hidden_size", options=[124, 512, 1024]),
            Choice(name="batch_size", options=[50, 250, 500]),
            Uniform(name="learning_rate", low=0.0001, high=0.1)
        ]
        )
        print(ss.dict_val)

    def case2():
        # nested search space definition case :
        #   https://github.com/microsoft/nni/blob/master/examples/trials/mnist-nested-search-space/search_space.json

        ss = SearchSpace(
            parameters=list(map(lambda x:
                                Choice(name=f"layer{x}", options=[
                                    ("Empty", None),
                                    ("Conv", Choice(name="kernel_size", options=[1, 2, 3, 5])),
                                    ("Max_pool", Choice(name="pooling_size", options=[2, 3, 5])),
                                    ("Avg_pool", Choice(name="pooling_size", options=[2, 3, 5])),
                                ]), range(0, 4, 1))
                            )
        )
        print(json.dumps(ss.dict_val))

        pass

    # case1()
    case2()
