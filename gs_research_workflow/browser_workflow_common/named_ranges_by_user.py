# -*- coding: utf-8 -*-

"""
这里先实现一个 h-index 高亮的 workflow 内容

Case 的一些假定：
    Range 是 Per Group 进行定义，只要有一个 User 定义了 Range ， 该 Group 内的其他人都能看到该 Range
        为了建模简单，每个人都有一个 Private Group 该 Group 中只有自己一个人，定义在该 Group 中的 Range 只能自己看到

定义一个 Web Range 的核心流程：
    > mouse up 事件，会生成一个 last_click_local_range (stateful srv 的 state variable)
        >> 该 range 会有 ui operation : "create range..."，需要确定 "range name"、"Save in which group" 、"range value dtype"、 "site_uri" 四项内容
        >> ui operation 的结果，会往 dce 中写入一条  site page range 的记录 (DCE : SiteExtraDataInUserGroup)
    > 有一个 Stateless srv ， 会 consume 该 DCE ，并将数据 Persistent 到 mongo 中备查

显示 Web Range 的核心流程：
    > 当前网页的 highlight 内容(如：在某个具体的author界面)
        >> 在 mongo 中查询当前 url 在当前 group 内是否已经有计算过的 doc range ， 有则直接推送给 stateful env(有一个 doc Range Process Stateful Env(即：robot)，专门提供需要在网页上需要显示的 doc range 信息)
        >> 读取 group 在 site 上标记需要显示的 doc range ， 在当前的网页上执行一次 prediction 的动作，将 prediction 的结果写入到 mongo ，并更新自己的 State
    > 当前网页的 hyper link 到网页中的 highlight 内容(如： 在 google scholar 的 keyword search result 页面)
        >> 读取DOM，收集所有的 hyper link
        >> 将所有的 hyper link 的 url 转换成 绝对 url
        >> 查询对应的 site 是否有 highlight 的定义，标识出需要进一步访问的 url 以及待  highlight 的信息
        >> 在本地的任务队列中，依次检索相应的 第二级网页标注出的 highlight 内容
                >> > mongo 中有则直接提示进行绘制
                >> > mongo 中查不到，则在本地的 headless chrome 中访问相关的网页，然后提取信息保存到 Mongo 中


"""
import logging
from datetime import datetime
from typing import NamedTuple, Union, Optional, Dict, List

from gs_framework.dce_object_define import DCE, EntityVariable, EntityVariableGroup
from gs_framework.decorators import dce_init, dce_prop_group_init
from gs_framework.common_prop_dtypes import DataType, OneDimUIObject, UrlUniqueEntity, StringT, DatetimeT, BytesT

logger = logging.getLogger(__name__)


# region NamedTuple

class UIObjectDefBySelector(NamedTuple):
    """jquery selector 版本的named range 的定义"""

    range_name: str = None
    """区域的名称，如: "h-index", "粉丝数" 等 """

    query_selector: str = None
    """jquery 的 selector 对象，用于表示该 range 的位置信息"""

    dtype: DataType = None
    """range 内需要提取的内容"""

    expire_sec: float = None
    """超过该时间，认为以前存的数据是dirty的，要重新提取一次，None 表示永不过期"""


class UIObjectDefCollection(NamedTuple):
    ui_object_defs: Dict[str, Union[UIObjectDefBySelector]] = None
    """UI Object 的数据集合， key 为 range name"""


class UIObjectInPage(NamedTuple):
    """网页上的一个 ui object 内容，除了基本的 OneDimUIObject 信息，还补充增加一些网页或业务层相关的内容"""
    ui_obj: OneDimUIObject = None

    ui_obj_gid: str = None
    """为了方便映射 ui object 的 Operation ，用一个 gid 进行数据的 join"""

    name: str = None
    """def 的名字 （NOTE：性能角度，减少一次与 def 的join，这里留了冗余信息）  """

    # ----- 与 html 相关度较高的内容 -----

    xpath: Optional[str] = None
    """如果是一个 html element 对象，则 提供其 xpath 信息"""
    outer_html: Optional[str] = None
    """这块区域的html内容"""

    # ----- 结构化相关内容 -----
    val: Optional[Union[int, float, str, bool]] = None
    """def 时声明过类型，则转换成相对应的数据类型，以便于做非string类型的运算，比如: h_index > 10 """

    sync_time: datetime = None
    """同步该数据的时间，可用于判定是否 expire 之后的重新 sync"""


class UIObjectsByUserGroup(NamedTuple):
    ui_objs: Dict[str, UIObjectInPage] = dict()
    """ui objects 的集合，key 为 UIObjectInPage.name"""
    user_group: str = None


class UrlGroupAndUserGroup(NamedTuple):
    """User Group 中定义的有关 url group 中的内容"""
    user_group: str = None
    """用户组，如果是私有数据，则用户组名为 account_id"""
    url_group: str = None
    """信息定义在哪个 url group 上"""


# endregion


# region DCE UrlGroupDataByUserGroup
@dce_init(partitions=2)
class UrlGroupDataByUserGroup(DCE):
    """ 每个用户组在 url_group 上的定义内容 """
    pk = EntityVariable(value_cls=UrlGroupAndUserGroup, default_val=None,
                        help="Per UserGroup + Per UrlGroup 上额外记录的UrlGroup上的内容")


@dce_prop_group_init(dce=UrlGroupDataByUserGroup)
class UIObjectDefsInUrlGroup(EntityVariableGroup):
    """ PerUser PerPageSite 记录的 doc range 的内容"""

    # 通过维护 newly_added_range , newly_removed_range 以维护 all_ranges_in_site 数据的准确性
    newly_added_object_def = EntityVariable(value_cls=UIObjectDefBySelector, default_val=None,
                                            help="新增加的 range，由 ChromeDesktopEnv 基于 ui operation 写入")
    newly_removed_object_def = EntityVariable(value_cls=UIObjectDefBySelector, default_val=None,
                                              help="新移除的 range，由 ChromeDesktopEnv 基于 ui operation 写入")
    # NOTE: 暂不提供 modify 的接口，通过 remove range + add range 的方式完成。因为目前不能把 selector 作为 pk 进行修改

    curr_object_defs = EntityVariable(value_cls=UIObjectDefCollection, default_val=None,
                                      help="当前该Url Group有效的 ui object def")

# endregion


# region DCE UrlBasedEntities(暂废弃)

# class UIObjectEntityLinks(NamedTuple):
#     """ 一组 UI Object 与 Entity 的 linking 关系
#         如： Scholar Search 页面的一个超链接(UI Object) 可以和一个 Author 的 Entity 进行 Link
#     """
#     entity_links: Dict[str, List[UrlUniqueEntity]] = None
#     """key 为 ui_obj_gid , value 为 对应到的多个 entity"""

# @dce_init(partitions=3)
# class UrlBasedEntities(DCE):
#     """以 不同 url 代表不同的 entity """
#     pk = EntityVariable(value_cls=UrlUniqueEntity, default_val=None, help="一种定义 entity 的方式")
#
#
# @dce_prop_group_init(dce=UrlBasedEntities)
# class WebPageData(EntityVariableGroup):
#     # 对 dom 数据压缩，是考虑到在 kafka 上的传输效率问题
#     dom_binary = EntityVariable(value_cls=BytesT, default_val=None, help="转成binary的dom数据，会加入gzip等处理")
#
#     # 以下两个属性是为了 debug 方便附加的
#     sync_from_acct = EntityVariable(value_cls=StringT, default_val=None, help="哪个账号同步的")
#     sync_from_pc = EntityVariable(value_cls=StringT, default_val=None, help="哪台pc同步的")
#
#     # env_gid 的属性是为了程序用的
#     sync_from_env_gid = EntityVariable(value_cls=StringT, default_val=None, help="同步该page的env gid ")
#     sync_time = EntityVariable(value_cls=DatetimeT, default_val=None, help="提交同步的时间")
#
#
# @dce_prop_group_init(dce=UrlBasedEntities)
# class ExtractedUIObjectsAndLinking(EntityVariableGroup):
#     newly_detected_ui_objects_in_page = EntityVariable(value_cls=UIObjectsByUserGroup, default_val=None,
#                                                        help="新探测到的基于user group分组的 ui objects in page")
#     newly_entity_links = EntityVariable(value_cls=UIObjectEntityLinks, default_val=None,
#                                         help="ui_object与 entity 之间的 linking 关系")

# endregion
