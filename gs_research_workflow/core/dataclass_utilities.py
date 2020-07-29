# -*- coding: UTF-8 -*-

import copy
from typing import Mapping, Collection, Type, Optional, Any

from dataclasses import is_dataclass, fields, MISSING, field, Field
from gs_framework.utilities import md5_str


def field_default_value_to_dict(obj):
    """dataclass 对象中，将所有含default value 的 field 输出为 dictionary"""
    if is_dataclass(obj):
        result = []
        for field in fields(obj):
            value = None
            if field.default is MISSING:
                continue
            # dataclass compose dataclass
            elif is_dataclass(field.type):
                if field.default is MISSING:  # 没有填值的情况下用 class 取 default value
                    value = field_default_value_to_dict(field.type)
                else:
                    value = field_default_value_to_dict(field.default)
            else:
                value = field_default_value_to_dict(field.default)
            result.append((field.name, value))
        return dict(result)
    elif isinstance(obj, Mapping):
        return dict((field_default_value_to_dict(k), field_default_value_to_dict(v)) for k, v in obj.items())
    elif isinstance(obj, Collection) and not isinstance(obj, str) and not isinstance(obj, bytes):
        return list(field_default_value_to_dict(v) for v in obj)
    else:
        return copy.deepcopy(obj)


def find_field_in_dataclass(field_name: str, cls: Type) -> Optional[Field]:
    """找到 dataclass 中的一个 field ， 找不到则返回 None"""
    assert is_dataclass(cls)
    for curr_field in fields(cls):
        if curr_field.name == field_name:
            return curr_field
    return None


class ModelHPMixIn:
    """适用于 tf.Model , tf.Layer 有关 hyper parameter 的相关内容"""

    def get_init_value_dict(self, out_self_cls: bool = False) -> Mapping[str, Any]:
        return self.hp.get_init_value_dict(out_self_cls)

    def get_hp_hash(self) -> str:
        return self.hp.get_hash_str()

