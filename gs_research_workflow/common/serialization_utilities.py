# -*- coding: utf-8 -*-
import json
from typing import Type, Mapping, Any, Union, Tuple, Optional

import yaml


def cls_to_str(cls) -> str:
    """class 对象转成 string ，格式为 __module__:__qualname__"""
    return f"{cls.__module__}:{cls.__qualname__}"


def str_to_cls(s: str) -> Type:
    """
    string 类型转成 class 对象，并且需要完成 import 的过程

    Parameters
    ----------
    s : class 的字符串表达，格式为 __module__:__qualname__

    Returns
    -------
    Class Object
    """
    import sys
    import importlib
    colon_pos = s.index(":")
    module_name, qual_name = s[:colon_pos], s[colon_pos + 1:]

    if module_name not in sys.modules:
        importlib.import_module(module_name)
    if qual_name.find(".") < 0:
        return getattr(sys.modules[module_name], qual_name)
    else:
        cls_path = qual_name.split(".")
        rlt_obj = getattr(sys.modules[module_name], cls_path[0])
        for cls_name in cls_path[1:]:
            rlt_obj = getattr(rlt_obj, cls_name)
        return rlt_obj


def save_mapping_to_file_or_stream(file_path_or_stream: str, step_cfg: Mapping, step_context: Mapping = None, file_format: str = None):
    """
    将一个 dictionary 对象存为本地文件

    Parameters
    ----------
    file_path_or_stream
    step_cfg
    step_context
        加载 step 时候的 context 信息
    file_format : str
        保存的数据类型，目前支持 pkl / json / yaml 三种 , None 表示根据后缀名选择
    """
    obj_to_dump = [step_cfg, {"CONTEXT": step_context}]
    if isinstance(file_path_or_stream, str):
        if file_format == "json" or (file_format is None and (file_path_or_stream.endswith(".js") or file_path_or_stream.endswith(".json"))):
            import json
            with open(file_path_or_stream, "w") as json_file:
                json.dump(obj_to_dump, json_file)
        elif file_format == "yaml" or (file_format is None and (file_path_or_stream.endswith(".yml") or file_path_or_stream.endswith(".yaml"))):
            import yaml
            with open(file_path_or_stream, "w") as yaml_file:
                yaml.dump(obj_to_dump, yaml_file)
        elif file_format == "pkl" or (file_format is None and (file_path_or_stream.endswith(".pkl") or file_path_or_stream.endswith(".pickle"))):
            import pickle
            with open(file_path_or_stream, "wb") as pkl_file:
                pickle.dump(obj_to_dump, pkl_file, pickle.HIGHEST_PROTOCOL)
    else:  # 这里是 file stream,假定都先按照 yml 输出
        import yaml
        yaml.dump(obj_to_dump, file_path_or_stream)


def load_mapping_from_file(file_path: str, file_format: str = None) -> Tuple[Mapping, Optional[Mapping]]:
    """

    Parameters
    ----------
    file_path
    file_format

    Returns
    -------
    -
        第一个值是 step config , 第二个值是 local context value
    """
    ret = None
    if file_format == "json" or (file_format is None and (file_path.endswith(".js") or file_path.endswith(".json"))):
        import json
        with open(file_path, "r") as json_file:
            ret = json.load(json_file)
    elif file_format == "yaml" or (file_format is None and (file_path.endswith(".yml") or file_path.endswith(".yaml"))):
        import yaml
        with open(file_path, "r") as yaml_file:
            ret = yaml.load(yaml_file)
    elif file_format == "pkl" or (
            file_format is None and (file_path.endswith(".pkl") or file_path.endswith(".pickle"))):
        import pickle
        with open(file_path, "rb") as pkl_file:
            ret = pickle.load(pkl_file)
    assert len(ret) == 2
    return ret[0], ret[1]["CONTEXT"]


_ESCAPE_STR_PREFIX = "[[OBJ]]\r\n"


def escape_nni_choice_item(v: Any) -> Union[float, int, str]:
    """
    nni choice 的 item 只支持 scalar 对象，但 GSStep 的 HP 中含有 Dict , List 这类Collection对象，因此需要对复杂的结构进行 escape ，编码成 String
    Note: 因为 choice 的值是会出现在 nni 的界面上，因此 escape 得到的内容，需要具有可读性
    Parameters
    ----------
    v

    Returns
    -------

    """
    if isinstance(v, (float, int)):
        return v
    elif isinstance(v, str):
        if v.startswith(_ESCAPE_STR_PREFIX):
            raise RuntimeError(f"Can't escape string '{v}' , conflict with prefix '{_ESCAPE_STR_PREFIX}'")
        return v
    else:
        return f"{_ESCAPE_STR_PREFIX}{yaml.dump(v)}"


def unescape_nni_choice_item(v: Union[float, int, str]) -> Any:
    if isinstance(v, (float, int)):
        return v
    elif isinstance(v, str):
        if v.startswith(_ESCAPE_STR_PREFIX):
            return yaml.load(v[len(_ESCAPE_STR_PREFIX):])
        else:
            return v
    else:
        raise RuntimeError(f"Unknown v type {type(v)}:{v}")
