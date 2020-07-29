# -*- coding: UTF-8 -*-

"""
GSStep之间的映射规则
"""

from typing import Mapping, Type, Set, Callable, TypeVar, Optional

from dataclasses import Field

from gs_research_workflow.common.serialization_utilities import cls_to_str
from gs_research_workflow.core.gs_step import GSStep, PropFieldMapping, _get_property_info


class GlobalGSStepMapping:
    __registered_mapping: [str, PropFieldMapping] = {}
    """暂时先将注册过的 mapping 存储在内存中，以后考虑其他方式的 persistent"""

    @staticmethod
    def _get_key(from_step: Type[GSStep], to_step: Type[GSStep], rule_name: str):
        if not rule_name:
            rule_name = "DEFAULT"
        return f"{cls_to_str(from_step)}-{cls_to_str(to_step)}-{rule_name}"

    @classmethod
    def register(cls, from_step: Type[GSStep], to_step: Type[GSStep], rule_name: str = None,
                 same_name: Set[Field] = None, diff_name: Mapping[Callable, Field] = None):
        """
        注册一个全局的 class prop field 的映射关系，在 target kwargs 时可以使用该信息内容以简化输入
        Note: register 的好处在于，如果这层转换关系是固定的，可以通过 register 的方式进行 predefine 。
            以后也可以使用 register 的信息进行 recommendation

        Parameters
        ----------
        from_step
        to_step
        rule_name : str
            from_step 与 to_step 之间允许映射多种的规则，这些映射规则之间，通过 name 进行区分
            rule_name 为 None 时，表示为 default mapping rule
        same_name
        diff_name

        Returns
        -------

        """

        if same_name:
            for fld in same_name:
                assert to_step.has_field(fld), f"{fld} in para same_name_prop_fields should from {to_step}"
        different_name = {}
        if diff_name:
            for prop, fld in diff_name.items():
                prop_info = _get_property_info(prop)
                assert prop_info.owner_cls is from_step, f"{prop_info.owner_cls}"
                different_name[prop_info] = fld
        cls.__registered_mapping[GlobalGSStepMapping._get_key(from_step, to_step, rule_name)] = PropFieldMapping(
            same_name,
            different_name)

    @classmethod
    def is_registered(cls, from_step: Type[GSStep], to_step: Type[GSStep], rule_name: str = None) -> bool:
        return GlobalGSStepMapping._get_key(from_step, to_step, rule_name) in cls.__registered_mapping

    @classmethod
    def get_registered(cls, from_step: Type[GSStep], to_step: Type[GSStep], rule_name: str = None) \
            -> Optional[PropFieldMapping]:
        assert cls.is_registered(from_step, to_step,
                                 rule_name), f"{from_step} to {to_step} prop field rule '{rule_name}' hasn't registered"
        return cls.__registered_mapping.get(GlobalGSStepMapping._get_key(from_step, to_step, rule_name))
