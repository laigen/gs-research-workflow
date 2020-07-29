# -*- coding: utf-8 -*-

"""
    与 html , url 相关的工具函数

    其中的依赖项包括：
        url 相关的操作，使用  furl : https://github.com/gruns/furl
        jquery 相关的操作，使用 pyquery : https://github.com/gawel/pyquery
        dom 相关的操作，使用 lxml

    jquery 语法: https://www.w3schools.com/jquery/jquery_ref_selectors.asp

"""

# 以下函数来自于原先王优所编写的
# D:\work\newQuant_local\gs_projects\gs_client_related_case\tasks\url_env_default_task.py
import logging
from typing import List, Optional, Tuple, Union, NamedTuple, Dict

from furl import furl
from lxml import etree
from lxml.etree import _Element, _ElementUnicodeResult
from lxml.html import HtmlElement
from pyquery import PyQuery
logger = logging.getLogger(__name__)


class SelectorOneItem:
    """一项 selector 对象"""

    def __init__(self, selector: str, index_in_parent: Optional[int] = None):
        self._selector = selector
        self.index_in_parent = index_in_parent

    @property
    def selector_str(self) -> str:
        if self.index_in_parent is None:
            return self._selector
        else:
            return f"{self._selector}:nth-child({self.index_in_parent + 1})"


def _get_single_selector_str(element:_Element) -> str:
    """根据一个 lxml element 对象，得到尽可能唯一识别该 element 的 jquery 表达
        如果 tag 有 id ， 则 用 id 做标记
        如果 tag 有 class 对象，则 class 进行约定
        如果 tag 有其他属性值，则用这些属性值来定位
    """
    if element.get('id'):
        return '#' + element.get('id')
    elif element.get('class'):
        return element.tag + '.' + '.'.join(element.get('class').split())
    elif len(element.keys()):
        return '[' + element.keys()[0] + '=' + element.get(element.keys()[0]) + ']'
    else:
        return element.tag


def _get_child_element_index(parent_ele: _Element, child_ele: _Element) -> int:
    return parent_ele.index(child_ele)


def xpath_2_jquery_selector(html: str, xpath: str, match_one: bool = True) -> str:
    """
        通过对 xpath 以及其 Parent tag 的分析，匹配到一个能够表示选中 tag 的 jquery selector 对象

        Parameters
        ----------
        html : str
            原始网页

        xpath : str
            mouseup 所捕获到的内容


        match_one : bool
            判定是要求能够匹配一个元素，还是满足该特性的多个元素
    """
    htmlparser = etree.HTMLParser()
    doc = etree.fromstring(html, htmlparser)
    els = doc.xpath(xpath)
    if not len(els):
        raise RuntimeError(f"Invalid xpath '{xpath}' in html")

    ls_selector: List[SelectorOneItem] = list()

    current_node = els[0]
    selector = _get_single_selector_str(current_node)
    ls_selector.insert(0, SelectorOneItem(selector))
    hit_items_count = len(doc.cssselect(selector))

    assert hit_items_count > 0, f"Can't find selector at first try!"
    if match_one and hit_items_count == 1:
        return ls_selector[0].selector_str

    # todo 如果 match_one == false ， 可以将每次结果做统计，返回命中数最少和次少的最短的两个 jquery string
    #           match_one == false 一般用来匹配 list 对象中的内容
    while True:
        parent_node = current_node.getparent()
        if parent_node is None:
            raise RuntimeError(f"Can't unique element at root level!")
        # 增加 parent 的约束
        ls_selector[0].index_in_parent = _get_child_element_index(parent_node, current_node)
        ls_selector.insert(0, SelectorOneItem(_get_single_selector_str(parent_node)))
        curr_jquery_selector = " > ".join([item.selector_str for item in ls_selector])
        new_items_count = len(doc.cssselect(curr_jquery_selector))
        logger.debug(f"#{new_items_count} : {curr_jquery_selector}")
        if new_items_count == 0:
            raise RuntimeError("jQuery condition too strict , match zero ")
        if match_one and new_items_count == 1:
            return curr_jquery_selector
        assert new_items_count <= hit_items_count, f"Can't be more item matched!"
        # 准备进入到下一轮的判定
        hit_items_count = new_items_count
        current_node = parent_node

    raise RuntimeError(f"Can't unique element at root level!")


def element_to_xpath(el: Union[PyQuery, HtmlElement]) -> str:
    if isinstance(el, PyQuery):
        if el:
            return el[0].getroottree().getpath(el[0])
        else:
            return None
    elif isinstance(el, (HtmlElement, _Element)):
        return el.getroottree().getpath(el)


def are_elements_equal(el1: Union[PyQuery, HtmlElement], el2: Union[PyQuery, HtmlElement]) -> bool:
    """
    比较两个元素是否是dom中的同一个元素
    """
    # NOTE: 用几个最基本的属性进行预判断，主要为了性能角度考虑
    # 暂时先去掉，需要考虑 el1 / el2 是 PyQuery 或  HtmlElement 两种对象的情形

    # if el1[0].tag != el2[0].tag or el1[0].tail != el2[0].tail or el1[0].text != el2[0].text:
    #     return False
    xpath1 = element_to_xpath(el1)
    xpath2 = element_to_xpath(el2)
    # logger.info(f"[{xpath1==xpath2}] {xpath1} vs {xpath2}")
    return xpath1 == xpath2


def is_pq_object_visible(el: PyQuery):
    if el.is_("script") or el.is_("noscript") or el.is_("style"):
        return False
    else:
        return True


def get_pq_object_inner_text(el: PyQuery):
    """获取元素的 innerText"""
    inner_text = ''
    if not is_pq_object_visible(el):
        return inner_text
    for e in el.contents():
        if isinstance(e, _ElementUnicodeResult):
            inner_text += e
        else:
            inner_text += get_pq_object_inner_text(PyQuery(e))
    return inner_text


def get_dom_node_start_pos(parent_node: PyQuery, target_el: PyQuery) -> Tuple[int, bool]:
    """
    找到在 parent node 的文字段落中的 target_el 的文字起始位置

    Examples
    --------
        doc = PyQuery(html_str)
        selected_item = doc(jquery_selector)
        start_pos,is_find = get_dom_node_start_pos(doc, selected_item)

    Parameters
    ----------
    parent_node
        表示上一个parent node， 是一个PyQuery object类型的节点

    target_el
        要找到的节点，是一个 PyQuery 类型的节点

    Returns
    -------
    Tuple[int, bool]
       int: 当前遍历到的字符串位置，找不到是该值也可能为一个正数
       bool: 是否找到目标元素
    """

    pos = 0
    if not is_pq_object_visible(parent_node):
        return pos, False
    child_nodes = parent_node.contents()
    target_el_xpath = element_to_xpath(target_el)
    for child in child_nodes:
        if isinstance(child, _ElementUnicodeResult):  # 字符文本
            pos += len(child)
        else:
            child_xpath = element_to_xpath(child)
            if child_xpath == target_el_xpath:
                return pos, True
            else:
                child_pos, child_found = get_dom_node_start_pos(PyQuery(child), target_el)
                if child_found:
                    return pos + child_pos, True
                else:
                    pos += child_pos
    return pos, False


def _match_xpaths(pos: int, parent_node: PyQuery, xpath_dict: Dict[str, int]) -> int:
    if not is_pq_object_visible(parent_node):
        return pos
    child_nodes = parent_node.contents()
    for child in child_nodes:
        if isinstance(child, _ElementUnicodeResult):  # 字符文本
            pos += len(child)
        else:
            child_xpath = element_to_xpath(child)
            if child_xpath in xpath_dict:
                xpath_dict[child_xpath] = pos
            pos = _match_xpaths(pos, PyQuery(child), xpath_dict)
    return pos


def batch_get_dom_node_start_pos(parent_node: PyQuery, target_eles: List[PyQuery]) -> List[int]:
    dict_xpath = {}
    ls_xpaths = []
    for ele in target_eles:
        curr_xpath = element_to_xpath(ele)
        dict_xpath[curr_xpath] = -1
        ls_xpaths.append(curr_xpath)
    _match_xpaths(0, parent_node, dict_xpath)
    ls_rlt = []
    for xpath in ls_xpaths:
        ls_rlt.append(dict_xpath[xpath])
    return ls_rlt


class HyperLinkingInPage(NamedTuple):
    start_pos: int = None
    """文本的起始位置"""
    end_pos: int = None
    """文本的结束位置"""
    text: str = None
    """超链接中的文本块"""
    url: str = None
    """超链接地址，绝对地址"""
    query_obj: PyQuery = None
    """可用于 query 的 PyQuery 对象"""


def get_doc_hyperlinking(doc: PyQuery, base_url: str) -> List[HyperLinkingInPage]:
    """
    获取网页的超链接列表

    Parameters
    ----------
    doc : PyQuery
        整个文档的 pyquery 对象

    base_url : str
        网页的地址信息，用于将相对地址转换成绝对地址
    """
    rlt = []
    doc.make_links_absolute(base_url=base_url)
    all_href = doc("a")
    body_text = get_pq_object_inner_text(doc)
    ls_href_to_query = []
    for link in all_href:
        link_obj = PyQuery(link)
        url = str(link_obj.attr("href"))
        if not url.startswith("http"):
            continue
        ls_href_to_query.append(link_obj)
    ls_start_pos = batch_get_dom_node_start_pos(doc, ls_href_to_query)
    for ui_ele, start_pos in zip(ls_href_to_query, ls_start_pos):
        if start_pos < 0:
            logger.error(f"Can't find ui object '{ui_ele}'")
        text = get_pq_object_inner_text(ui_ele)
        if text != body_text[start_pos:start_pos+len(text)]:
            logger.error(f"inner text is not equal with doc body '{text}' ?= '{body_text[start_pos:start_pos+len(text)]}'")
        url = str(ui_ele.attr("href"))
        hyperlinking_in_page = HyperLinkingInPage(start_pos=start_pos, end_pos=start_pos + len(text), text=text,
                                                  url=url, query_obj=ui_ele)
        rlt.append(hyperlinking_in_page)
    return rlt


def get_url_group_str(url: str) -> str:
    """得到 url 的 group 信息，用户划定的 ui_position 的数据，会保存到 url_group 上，以便于类似的网页也能应用该 position
        如果是动态网页，则返回动态网页地址
        如果是静态网页，则返回静态网页上一级的地址
    """
    # url 格式名词定义： scheme://username:password@host:port/path?query#fragment
    url_obj = furl(url)
    if len(url_obj.query.params) > 0:  # 动态网页，返回去掉参数后的地址
        return f"{url_obj.origin}/{'/'.join(url_obj.path.segments)}"
    elif len(url_obj.path.segments) > 0:  # 静态网页，去掉最后一级的地址
        return f"{url_obj.origin}/{'/'.join(url_obj.path.segments[0:-1])}"
    else:  # 返回基础地址
        return url_obj.origin


def get_url_without_fragment(url: str) -> str:
    url_obj = furl(url)
    return url_obj.remove(fragment=True).url
