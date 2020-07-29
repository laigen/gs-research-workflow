# -*- coding: utf-8 -*-

"""
一些通用的 variable 数据类型
"""
from typing import NamedTuple, Dict, List

from gs_framework.common_prop_dtypes import UrlUniqueEntity

from gs_research_workflow.browser_workflow_common.named_ranges_by_user import UIObjectInPage


class PageWithDOM(NamedTuple):
    url_without_fragment: str = None
    dom_binary: bytes = None


class UIObjectsAndEntityLinkingInOnePage(NamedTuple):
    url_without_fragment: str = None
    ui_objects: Dict[str, UIObjectInPage] = None
    """所有的 ui_object 对象，key 为 ui_object name"""
    entities_linking: Dict[str, List[UrlUniqueEntity]] = None
    """一部分 ui object 的 entity linking , key 为 ui_object gid"""


class UIObjectsInOnePage(NamedTuple):
    url_without_fragment: str = None
    ui_objects: Dict[str, UIObjectInPage] = None
    """所有的 ui_object 对象，key 为 ui_object name"""

