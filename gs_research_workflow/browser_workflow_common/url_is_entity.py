# -*- coding: utf-8 -*-

"""探测url是不是可以被视作一个 entity 对象

    Note : 暂时先用 rule base 的方式定义几个，以后用 RL 的方式解决这类 entity 的判定问题
"""
from typing import List, Dict

from furl import furl
from gs_research_workflow.common.web_utilities import get_url_group_str


class _UrlEntityClassifierBase:
    url_group: str = None
    """对哪一类的 url 有效"""

    @classmethod
    def is_entity(cls, url) -> bool:
        raise NotImplementedError


class GoogleScholarAuthor(_UrlEntityClassifierBase):
    url_group = "https://scholar.google.com/citations"

    @classmethod
    def is_entity(cls, url) -> bool:
        url_obj = furl(url)
        if len(url_obj.query.params) > 0:
            if url_obj.query.params.has_key("user"):
                return True
        return False


class RuleBasedUrlEntityClassifier:
    _all_classifier:List[_UrlEntityClassifierBase] = [GoogleScholarAuthor]

    _dict_classifier: Dict[str, _UrlEntityClassifierBase] = {o.url_group: o for o in _all_classifier}

    @classmethod
    def is_entity_url(cls, url: str) -> bool:
        """判定是否为一个 entity 的 url"""
        url_group = get_url_group_str(url)
        if url_group in cls._dict_classifier:
            return cls._dict_classifier[url_group].is_entity(url)
        # 找不到的情况下，目前缺省都是 True
        return True
