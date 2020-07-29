# -*- coding: UTF-8 -*-

"""
有关 Initial Flow 的先关 class 以及 utility functions
"""
import inspect
from functools import wraps
from typing import Mapping, Any, Type, Set, Union, NamedTuple, Tuple, List, Iterable, Optional, Dict

from dataclasses import Field, _FIELDS
from gs_framework.instance_hash_calculation import HashCalculation
from gs_framework.utilities import md5_str

from gs_research_workflow.common.serialization_utilities import str_to_cls, cls_to_str

_KEY_RULE_NAME = "RULE"
_KEY_PROPERTIES = "PROPERTIES"


class PropertyInfo(NamedTuple):
    name: str
    prop_annotation: Any
    owner_cls: Type


def _get_property_info(prop) -> PropertyInfo:
    assert type(prop) is property
    assert "return" in prop.fget.__annotations__, f"{prop} property must define return annotation"
    name = prop.fget.__name__
    ann = prop.fget.__annotations__.get("return")
    owner_cls_qualname = prop.fget.__qualname__[:prop.fget.__qualname__.rindex(".")]
    module_name = prop.fget.__module__
    cls = str_to_cls(f"{module_name}:{owner_cls_qualname}")
    return PropertyInfo(name, ann, cls)


class PropFieldMapping(NamedTuple):
    same_name: Set[Field] = None
    """相同的名称，即 Property 和 Field 的名称是相同的，用 field 进行表示"""

    different_name: Mapping[PropertyInfo, Field] = None
    """property 和 filed 之间的映射关系
        Property 因为是一个 function，所以这里是 Callable
    """

    @property
    def field_names(self) -> List[str]:
        ls_all_fields = []
        if self.same_name:
            ls_all_fields += list(self.same_name)
        if self.different_name:
            ls_all_fields += [v for k, v in self.different_name.items()]
        return [fld.name for fld in ls_all_fields]

    @property
    def property_names(self) -> List[str]:
        ls_all_prop_names = []
        if self.same_name:
            ls_all_prop_names += [fld.name for fld in self.same_name]
        if self.different_name:
            ls_all_prop_names += [k.name for k, v in self.different_name.items()]
        return ls_all_prop_names


def _input_steps_to_list(_input_steps) -> List[Tuple['GSStep', Optional[str]]]:
    """将_pip_op 的输入规整一下，以便于统一的处理方式"""
    ls_input_steps: List[Tuple['GSStep', Optional[str]]] = list()
    if hasattr(_input_steps, "__iter__") and not isinstance(_input_steps, tuple):  # 是一个 非 tuple 的 iterable 对象
        for item in _input_steps:
            if isinstance(item, Tuple):
                assert len(item) == 2 and (item[1] is None or isinstance(item[1], str))
                ls_input_steps.append(item)
            else:
                ls_input_steps.append((item, None))  # 用 default 的添加
    elif isinstance(_input_steps, tuple):
        assert len(_input_steps) == 2 and isinstance(_input_steps[1], str)
        ls_input_steps.append(_input_steps)
    else:  # GSStep 对象
        ls_input_steps.append((_input_steps, None))
    return ls_input_steps


def _input_steps_to_kwargs(
        _input_steps: Union['GSStep', Tuple['GSStep', str], Iterable[Union['GSStep', Tuple['GSStep', str]]]],
        to_step_type: Type['GSStep']) -> Mapping[str, Any]:
    """
    将 pip_op 的内容,根据映射关系，生成一个 dict 用于 kwargs

    Parameters
    ----------
    _input_steps
    to_step_type
    """
    from gs_research_workflow.core.gs_step_mapping import GlobalGSStepMapping

    # step 1 : 将 _input_steps 统一格式，转成可以迭代的对象
    ls_input_steps = _input_steps_to_list(_input_steps)

    # step 2 : 遍历 _input_steps 的内容，将 field 的结果进行输出
    dict_rlt: Mapping[str, Any] = dict()
    for input_step in ls_input_steps:
        step, rule_name = input_step
        step_mapping = GlobalGSStepMapping.get_registered(step.__class__, to_step_type, rule_name)
        curr_kwargs = step.map_to_kwargs(step_mapping)
        if curr_kwargs:
            dict_rlt.update(curr_kwargs)
    return dict_rlt


def _wrap_init(orig_init):

    @wraps(orig_init)
    def init_wrapper(self, *args,
                     _input_steps: Union[
                         'GSStep', Tuple['GSStep', str], Iterable[Union['GSStep', Tuple['GSStep', str]]]] = None,
                     **kwargs):
        """
        wrapper 了 __init__ 以增加功能：
        1） 记录 init 中对于 field 的传参情况
            a) 通过 args 传入的，能够 Mapping 到 field name
            b) 有 default值，且没有在 __init__ 时传入的，不做记录

        2) 允许通过 _input_steps 参数，接收来自于另一个 GSStep 的 props 的内容
            a) 根据 mapping 关系展开后传入 kwargs
            b) 记录下 step inst 之间的 prop to field 的关系

        Parameters
        ----------
        self
        args
        _input_steps:Union[Type['GSStep'], Tuple[Type['GSStep'], str], Iterable[Union[Type['GSStep'], Tuple[Type['GSStep'], str]]]]
            已经注册过的 GSStep 的映射关系对象，允许的输入包括：
                单个的 GSStep Inst ， 使用 DEFAULT mapping rule
                单个的 GSStep Inst + registered mapping rule
                多个 GSStep Inst + mapping rule
        kwargs
        """

        # 调用GSStep基类的_set_init_inputs() 函数，记录 init 的参数
        input_arg_names = inspect.getfullargspec(orig_init).args
        if len(input_arg_names) > 0 and input_arg_names[0] == "self":
            input_arg_names.pop(0)
        self._log_init_inputs(_input_steps, input_arg_names, *args, **kwargs)

        if _input_steps:
            # unpack _input_steps into kwargs
            additional_kwargs = _input_steps_to_kwargs(_input_steps, self.__class__)
            if additional_kwargs is not None:
                if kwargs is not None:
                    kwargs.update(additional_kwargs)
                else:
                    kwargs = additional_kwargs
        orig_init(self, *args, **kwargs)

    return init_wrapper


class _GSStepMeta(type):
    # 重载 __getattribute__ 以使得 Class.field 的时候能够返回得到 field 字段
    def __getattribute__(self, name):
        # 所有系统的 attribute 直接返回，避免出现递归
        if name.startswith("__") and name.endswith("__"):
            return super().__getattribute__(name)

        if hasattr(self, _FIELDS) and name in getattr(self, _FIELDS):
            return getattr(self, _FIELDS)[name]
        else:
            return super().__getattribute__(name)

    def __setattr__(self, key, value):
        if key == "__init__":
            value = _wrap_init(value)
        return super().__setattr__(key, value)


class GSStep(metaclass=_GSStepMeta):
    """ GS 搭建 workflow 是由派生自 GSStep 的类对象完成"""

    def _log_init_inputs(self,
                         _input_steps: Union[
                             'GSStep', Tuple['GSStep', str], Iterable[Union['GSStep', Tuple['GSStep', str]]]] = None,
                         input_arg_names: List[str] = None, *args, **kwargs):
        """设置所有的 init input 的输入，在 wrapped init function 中被调用"""
        _direct_init_field_value = dict()  # Mapping[str, Any], _direct_init_field_value 不能加 annotation ，以免被当做 field 处理
        """
        出现在 init 中 field 的填值情况，这里仅包括非 _input_steps 方式填入的 field 的值
        用途： 输出到 tape 时用到该信息
        说明： 有些 field 是含有缺省值的，对于缺省值的 field 如果没有在 __init__ 中赋值,则不输出到 tape 中。
            这样已经 dump 的 tape 在缺省值发生变更后，依然能够使用新的缺省值
        """
        for (arg_name, arg_val) in zip(input_arg_names, args):
            _direct_init_field_value[arg_name] = arg_val
        for arg_name, arg_val in kwargs.items():
            _direct_init_field_value[arg_name] = arg_val
        _ls_input_steps = None
        if _input_steps:
            _ls_input_steps = _input_steps_to_list(_input_steps)
        # NOTE: 当 dataclass 的实现似乎有 bug, 当 frozen = True 的时候，未定义为 field 的属性也会被禁止赋值，所以这里直接设置 __dict__ 以绕开该 bug
        self.__dict__["_direct_init_field_value"] = _direct_init_field_value
        self.__dict__["_ls_input_steps"] = _ls_input_steps

    def get_init_value_dict(self, out_self_cls: bool = False) -> Mapping[str, Any]:
        """获取 init 的 dictionay 对象
        Notes : 这里不作为 property , 避免产生一个与 dataclass 定义业务意义无关的 property 内容
        Notes : 递归嵌套的 dict 关系是 lazy 产生的,init 过程中仅保留相关的数据链路关系

        Parameters
        ----------
        out_self_cls:bool
            是否多输出一层当前 class 的内容
        """
        import copy
        from gs_research_workflow.core.gs_step_mapping import GlobalGSStepMapping

        # TODO: 这里需要 composition 的情况
        init_dict_rlt = dict()
        if self._direct_init_field_value:
            for k, v in self._direct_init_field_value.items():
                if isinstance(v, GSStep):
                    init_dict_rlt[k] = v.get_init_value_dict(out_self_cls)
                else:
                    init_dict_rlt[k] = copy.deepcopy(v)
        # init_dict_rlt = copy.deepcopy(self._direct_init_field_value)

        if self._ls_input_steps:
            for curr_step in self._ls_input_steps:
                field_mapping = GlobalGSStepMapping.get_registered(curr_step[0].__class__, self.__class__, curr_step[1])
                # pip 的选项，使用的格式为 "#field1,field2# rule_name
                key = "#" + ",".join(field_mapping.field_names) + "#"
                init_dict_rlt[key] = curr_step[0].get_init_value_dict(True)
                init_dict_rlt[key][_KEY_PROPERTIES] = ",".join(field_mapping.property_names)
                if curr_step[1] is not None:
                    init_dict_rlt[key][_KEY_RULE_NAME] = curr_step[1]

        if out_self_cls:
            return {cls_to_str(self.__class__): init_dict_rlt}
        else:
            return init_dict_rlt

    @classmethod
    def has_field(cls, fld: Field) -> bool:
        cls_fld = getattr(cls, fld.name, None)
        return fld is cls_fld

    def map_to_kwargs(self, prop_field_mapping: PropFieldMapping) -> Mapping[str, Any]:
        """
        输出 target 对象的 kwargs
        Parameters
        ----------
        prop_field_mapping : Union[Type, PropFieldMapping]
            如果是 class 则必须是预先 register 的，适用于Pre Define的参数关系转换
            如果是 PropFieldMapping 则适用于runtime调整的参数关系转换

        Returns
        -------
        符合 target 要求 mapping 的 kwargs 的部分内容
        """
        dict_rlt = dict()
        if prop_field_mapping.same_name:
            for fld in prop_field_mapping.same_name:
                dict_rlt[fld.name] = getattr(self, fld.name)

        if prop_field_mapping.different_name:
            for prop, fld in prop_field_mapping.different_name.items():
                assert issubclass(self.__class__, prop.owner_cls)
                dict_rlt[fld.name] = getattr(self, prop.name)
        
        return dict_rlt

    def get_hash_str(self) -> str:
        hp_dict = self.get_init_value_dict(True)
        return md5_str(HashCalculation.value_to_hash_str(hp_dict))


def is_context_loc(loc: str):
    return loc.startswith("LOCAL")


def create_step_by_dict(init_data: Mapping[str, Any], step_context: Dict = None, cls_str: str = None, lv: int = 0) -> GSStep:
    """根据init配置的内容，创建 step 对象"""
    if lv == 0:
        assert len(init_data) == 1  # 假定只能有一个最顶层的 step inst 对象，这里不支持反序列化为多值的 workflow
        k, v = next(iter(init_data.items()))
        assert isinstance(k, str)
        assert isinstance(v, dict)
        return create_step_by_dict(v, step_context, k, lv + 1)

    assert cls_str is not None
    cls_obj = str_to_cls(cls_str)

    input_step: List[Tuple[GSStep, Optional[str]]] = list()
    kwargs = dict()
    for k, v in init_data.items():
        if isinstance(v, dict) and isinstance(k, str) and k.startswith("#") and k.endswith(
                "#"):  # 这部分 field 来自于某个 step 的 property
            assert 2 <= len(v) <= 3
            pip_rule_name = v.get(_KEY_RULE_NAME, None)
            sub_step_cls_name = ""
            sub_step_fields = None
            for step_k, step_v in v.items():
                if step_k == _KEY_RULE_NAME or step_k == _KEY_PROPERTIES:
                    continue
                sub_step_cls_name = step_k
                sub_step_fields = step_v
                break
            assert len(sub_step_cls_name) > 0
            assert sub_step_fields is not None

            input_step.append(
                (create_step_by_dict(sub_step_fields, step_context, sub_step_cls_name, lv + 1), pip_rule_name))
        elif isinstance(v, dict):  # 可能 v 还是一个 GSStep ， 是一个 GSStep Composition 的组合
            if len(v) == 1 and next(iter(v.keys())).count(":") == 1 and isinstance(next(iter(v.values())), dict):
                kwargs[k] = create_step_by_dict(next(iter(v.values())), step_context, next(iter(v.keys())), lv + 1)
            else:
                kwargs[k] = v
        else:
            kwargs[k] = v
    step_inst = cls_obj(_input_steps=input_step, **kwargs)

    # 如果是依赖于 context 变量的，则将 context 变量传入
    if hasattr(step_inst, "SET_CONTEXT"):
        step_inst.SET_CONTEXT(step_context)
    return step_inst


def _lookup_and_upsert_cfg_dict(partial_step_cfg: Mapping[str, Any], ls_loc: List[str], para_val: Any) -> int:
    """
    按照深度优先的方式遍历 dict 内容，找到匹配项之后返回

    Returns
    -------
    int
        更新过的内容项
    """
    rlt_upserted_items = 0
    for k, v in partial_step_cfg.items():
        if k == ls_loc[0]:
            if isinstance(v, dict):
                if len(ls_loc) == 2:
                    if ls_loc[1] in v:
                        if type(v[ls_loc[1]]) == type(para_val):  # 这里为了防止误替换掉 dictionary 的内容
                            v[ls_loc[1]] = para_val
                            rlt_upserted_items += 1
                    else:  # key 不存在的情况下
                        v[ls_loc[1]] = para_val
                        rlt_upserted_items += 1
                else:  # 继续深入一层寻找匹配项
                    rlt_upserted_items += _lookup_and_upsert_cfg_dict(v, ls_loc[1:], para_val)
        elif isinstance(v, dict):  # 深度优先继续找到匹配项
            rlt_upserted_items += _lookup_and_upsert_cfg_dict(v, ls_loc, para_val)
    return rlt_upserted_items


def _lookup_cfg_dict(partial_step_cfg: Mapping[str, Any], ls_loc: List[str]) -> Optional[Any]:
    for k, v in partial_step_cfg.items():
        if k == ls_loc[0]:
            if isinstance(v, dict):
                if len(ls_loc) == 2:
                    if ls_loc[1] in v:
                        return v[ls_loc[1]]
                    else:  # key 不存在的情况下
                        continue
                else:  # 继续深入一层寻找匹配项
                    item_to_find = _lookup_cfg_dict(v, ls_loc[1:])
                    if item_to_find is not None:  # NOTE: cfg 参数项可能会有整数0的选项，因此不能直接使用 "if found_item"这种写法
                        return item_to_find
        elif isinstance(v, dict):  # 深度优先继续找到匹配项
            item_to_find = _lookup_cfg_dict(v, ls_loc)
            if item_to_find is not None:
                return item_to_find
    return None


def upsert_step_cfg_para(step_cfg: Mapping[str, Any], context_cfg: Mapping[str, Any], para_loc: str,
                         para_val: Any) -> int:
    """
    在 config 的 dictionary tree 上找到 para_loc 位置的参数进行数值更新

    NOTE: 匹配到片段位置后，将修改 step_cfg 的值
    Parameters
    ----------
    step_cfg

    para_loc ： str
        参数的位置信息，不同的 key 之间用 ">" 分隔，可以不要求是从根位置开始

        Examples
        --------
        gs_research_workflow.time_series.models.inception_time:InceptionTime.HP > depth
        gs_research_workflow.time_series.models.inception_time:InceptionTime.HP > inception_block_hp > gs_research_workflow.time_series.models.inception_time:InceptionBlock.HP > stride

    para_val

    Returns
    -------
    int
        修改过的匹配项

    """

    ls_loc_pos = [x.strip() for x in para_loc.split(">")]
    assert len(ls_loc_pos) >= 2
    if is_context_loc(para_loc):
        return _lookup_and_upsert_cfg_dict(context_cfg, ls_loc_pos, para_val)
    else:
        return _lookup_and_upsert_cfg_dict(step_cfg, ls_loc_pos, para_val)


def lookup_step_cfg_para(step_cfg: Mapping[str, Any], context_cfg: Mapping[str, Any], para_loc: str):
    """
    在 config 的 dictionary tree 上找到 para_loc 位置的参数值，并返回
    """
    ls_loc_pos = [x.strip() for x in para_loc.split(">")]
    assert len(ls_loc_pos) >= 2, f"ls_loc_pos:{ls_loc_pos}"
    if is_context_loc(para_loc):
        return _lookup_cfg_dict(context_cfg, ls_loc_pos)
    else:
        return _lookup_cfg_dict(step_cfg, ls_loc_pos)
