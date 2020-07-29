# -*- coding: UTF-8 -*-
from typing import NamedTuple

from gs_framework.common_prop_dtypes import StringT, IntT, DatetimeT
from gs_framework.dce_object_define import EntityVariable, DCE, EntityVariableGroup
from gs_framework.decorators import dce_prop_group_init

__author__ = "laigen"

"""
适用于 DCE Attribute 的主要数据类型
"""


class EntityWithIndicator(NamedTuple):
    """实体的某一项ts指标数据"""

    entity_symbol: str = None
    """
        如果是标准的可交易证券，建议使用 Bloomberg 的 symbol 定义体系。 如： '600000:CH', '1:HK', 'MSFT:US'
        如果是非标的entity:
                    可以是一个 url。 如： wikipedia 的 link ，或者 google author 上的一个 link
                    也可以是某个体系内部的唯一代码。如： 身份证号码，企业机构代码，ISBN，DOI, 某个 DataVendor 分配的代码
        为了尽量的全局唯一，建议将体系的名称作为前缀。 如： DOI:10.1021/ja00095a066  
                                                            ISBN:978-7-03-025494-8  
                                                            URL:https://scholar.google.com/citations?user=CZp3uv4AAAAJ&hl=en&oi=sra
    """

    indicator_hash: str = None
    """
    指标的 Hash 值，可以任意方式确定，只要确保不重复即可。
        如： 聚源的 股票日收盘数据， MD5( "JYDB" + "表名" + "列名" + "FILTER_CONDITION")
             tushare 的股票日收盘数据， MD5( "TUSHARE" + "接口.__qualname__" + "接口主要参数" )
    """

# region -------------  针对于 entity_symbol , 类似于 名称代码表，股票基本信息 的 DCE -----------


# NOTE : 为了避免创建 Topic ， 暂时先将 DCE 的声明注释掉
# @dce_init(partitions=3)
class EntitySnapshot(DCE):
    """ Entity 的 snapshot 数据信息  """
    pk = EntityVariable(value_cls=StringT, help="Entity Symbol 对象")


@dce_prop_group_init(dce=EntitySnapshot)
class PlatformAttrs(EntityVariableGroup):
    """由平台负责维护的属性"""
    lgid = EntityVariable(value_cls=IntT, help="适用于 pandas 等场景中，可快速 join 用的 gid")


@dce_prop_group_init(dce=EntitySnapshot)
class TradeableEntityAttrsByExchangeMarket(EntityVariableGroup):
    """在交易所可交易的实体的（在交易所中的）属性"""
    exchange_market = EntityVariable(value_cls=StringT, help="交易所代码")
    str_symbol_in_market = EntityVariable(value_cls=StringT, help="股票的交易所代码，字符串格式")
    int_symbol_in_market = EntityVariable(value_cls=IntT, help="股票的交易所代码，数字格式（如有）")
    entity_name = EntityVariable(value_cls=StringT, help="如：股票名称")
    lot_size = EntityVariable(value_cls=IntT, help="最小交易单位")
    list_date = EntityVariable(value_cls=DatetimeT, help="上市日期")
    delist_date = EntityVariable(value_cls=DatetimeT, help="摘牌日期")
    exchange_board = EntityVariable(value_cls=StringT, help="如：科创板，主板")
    # 其他待补充

# 其他可交易实体的属性包括:
#           股票类：Entity 的简要描述，上市主体的 symbol，招股说明书，发行价，承销商等
#           债券类：利率，到期时间，付息方式，抵押信息等
#           Option：....
#
# 非可交易实体的属性包括：
#           某种维度的指标，如： 身高，体重，h-index，出版日期，关键词 等（sync from html）

# endregion

# region ----------- 针对于 indicator 的 meta -----------------


# @dce_init(partitions=1)
class Indicator(DCE):
    """一个指标对应于一行"""
    pk = EntityVariable(value_cls=StringT, help="indicator hash")


@dce_prop_group_init(dce=Indicator)
class DataVendorMeta(EntityVariableGroup):
    """该 indicator 采集与发布 提供商"""
    vendor_name = EntityVariable(value_cls=StringT, help="数据厂商名称")
    vendor_entity_symbol = EntityVariable(value_cls=StringT, help="如果 Vendor 已经是一个 entity ， 则填入该 symbol")


@dce_prop_group_init(dce=Indicator)
class RDBSDataSource(EntityVariableGroup):
    db_type = EntityVariable(value_cls=StringT, help="数据库类型，mysql,oracle, db2,sqlserver等")
    table_name = EntityVariable(value_cls=StringT, help="指标来自于哪一张(主)表")
    o_col_name = EntityVariable(value_cls=StringT)
    t_col_name = EntityVariable(value_cls=StringT)
    v_col_name = EntityVariable(value_cls=StringT)
    row_filter_cond = EntityVariable(value_cls=StringT)
    join_table = EntityVariable(value_cls=StringT)
    join_condition = EntityVariable(value_cls=StringT)


@dce_prop_group_init(dce=Indicator)
class OMeta(EntityVariableGroup):
    category_symbol = EntityVariable(value_cls=StringT, help="属于哪个类别，如： OSET:chn_stk")


@dce_prop_group_init(dce=Indicator)
class TMeta(EntityVariableGroup):
    t_freq = EntityVariable(value_cls=StringT, help="频率的描述，可能是一个panda.freq 的对象")
    t_observer = EntityVariable(value_cls=StringT, help="观察着是 inside,public, vendor 等")
    # ...


@dce_prop_group_init(dce=Indicator)
class VMeta(EntityVariableGroup):
    v_unit_symbol = EntityVariable(value_cls=StringT, help="v的单位描述，将做成一个 unit 对象")
    precision = EntityVariable(value_cls=IntT, help="v的数据精度")
    # ...

# endregion

# -------------------- OTV 数据 ---------------------

# 要解决的问题：
#   一个是 T 在不同的 Entity 之间会发生数据的重复冗余
#

# @dce_init(partitions=5)
class EquityLowFreqTS(DCE):
    """  股票类的低频TS数据（这里低频指的是日频以及日频以下的频率）

        NOTES ：目前暂时先采用 一类实体的(按频度切分)一大类数据的 DCE 划分方式，避免所有的数据放在一个 DCE 里。
                也可以是 Entity OSet + DataVendor + T Freq 的 DCE 划分方式
    """
    pk = EntityVariable(value_cls=EntityWithIndicator, help="实体的某一个指标数据")


@dce_prop_group_init(dce=EquityLowFreqTS)
class PeriodTSData(EntityVariableGroup):
    """
    一段周期的 TS 数据
    !!! ALERT: 这类的 Variable / VariableGroup 目前是 (Code) Pre Define，后续要支持 runtime 增加  EntityVariable
    """
    ...





