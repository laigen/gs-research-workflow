# -*- coding: UTF-8 -*-
"""
一些 OTVn 数据内容信息的描述，描述的内容包括：
     1) 最源头的 RDBS 的数据定义信息
     2) Arctic 中的 store 信息内容

NOTE: 这里仅包括预先已经将数据存入 arctic 的应用场景

区别于另一种提供 sdk api 的接口（如：tushare）是采用两级缓存的机制，取数据的同时，对两级 cache 进行维护更新

该描述信息的应用场景：
    1) 将历史数据从 RDBS 中导出到 arctic
    2) 从 arctic 中读取数据到 local cache
"""
import inspect
from datetime import date
from typing import Union, Optional, List, Generic, TypeVar, Type, Tuple, Any, Set, ClassVar
import re

from arctic import CHUNK_STORE

from gs_research_workflow.time_series.envs.jy_data_extract_env import get_security_category_type, FinI, \
    get_security_listed_sector_type

from gs_research_workflow.external_data.data_vendor.jy.ddl_entities.constant.SecuMain import SecuMain

from gs_research_workflow.external_data.data_vendor.jy.ddl_entities.corp_chn.QT_DailyQuote import QT_DailyQuote

from gs_research_workflow.external_data.table_declaration_base import TableColumnDeclarationEntity, SQLTableEntity
from gs_research_workflow.common.sql_statement_helper import SQLStatementHelper as sh
import pandas as pd


class _Column:
    name: str
    """列名称"""
    description: str
    """列的描述信息"""
    nullable: bool

    def __repr__(self):
        return f"name:{self.name} - desc:{self.description} - nullable:{self.nullable}"


class _ColumnMaybeFromRDBS:
    rdbs_original: Optional[TableColumnDeclarationEntity]
    """数据的原始出处"""

    @classmethod
    def from_rdbs_column(cls, name: str, col: TableColumnDeclarationEntity, **kwargs):
        ret = cls()
        ret.name = name
        ret.nullable = col.nullable
        ret.description = col.chn_name
        ret.rdbs_original = col
        return ret


class VColumn(_Column, _ColumnMaybeFromRDBS):
    """OTVn 中的V列的描述信息 """
    unit: str
    """v的单位信息"""

    @classmethod
    def from_rdbs_column(cls, name: str, col: TableColumnDeclarationEntity) -> 'VColumn':
        ret = super().from_rdbs_column(name, col)

        # NOTE: 可能有性能问题，调用次数不多，先不管这里
        # 聚源的数据说明中，有形如 '昨收盘(元)' 的单位信息，用正则将 Unit 抽取出来
        match_obj = re.match(r"(\S*)\((\S*)\)", col.chn_name, re.I | re.M)
        if match_obj:
            ret.unit = match_obj.group(2)
        return ret


class TColumn(_Column, _ColumnMaybeFromRDBS):
    freq: str

    @classmethod
    def from_rdbs_column(cls, name: str, col: TableColumnDeclarationEntity, freq: str) -> 'TColumn':
        ret = super().from_rdbs_column(name, col)
        ret.freq = freq
        return ret


class OColumn(_Column, _ColumnMaybeFromRDBS):
    # 暂时先用string的方式表示 set，以后是需要跟 entity stream 中的 entity 做关联的
    entity_set: str

    @classmethod
    def from_rdbs_column(cls, name: str, col: TableColumnDeclarationEntity, entity_set: str) -> 'OColumn':
        ret = super().from_rdbs_column(name, col)
        ret.entity_set = entity_set
        return ret


class OTVTableInArctic:
    name: str
    """ table name , 如: "mkt_daily_quotation"
            table name 在保存到 arctic 时，填入 write()/update() 函数的 symbol 参数项 
            table name 也作为保存 local cache 的 pickle file name
    """
    o: Union[OColumn, List[OColumn]]
    t: Union[TColumn, List[TColumn]]
    v: Union[VColumn, List[VColumn]]

    arctic_lib_name: str
    """一般一个数据厂商一类o的 set 多个 otv 数据在一个 library
        如: 聚源沪深股票的行情数据(otv1) , 沪深股票的财务数据(otv2) 存储在 lib "jy_chn_equity_otv_chunkstore"
            聚源香港股票的行情数据(otv3) , 沪深股票的财务数据(otv4) 存储在 lib "jy_hk_equity_otv_chunckstore"
    """
    arctic_lib_type: ClassVar[str] = CHUNK_STORE
    """这里目前是固定值，CHUNK_STORE"""
    arctic_chunk_size: str
    """
    根据 arctic chunk_size 的规范，填入的是 pandas 有关 freq 的字符，如： BD,D,M,Y 等
    
    经过实验验证，一般chunk_size填入比数据低一些的频率会得到较好的 performance
        如： D -> M ， M -> Y 
    """
    def _read_from_arctic(self) -> pd.DataFrame:
        # TODO
        pass

    def _write_to_local_cache(self):
        # TODO
        pass

    def get_data(self) -> pd.DataFrame:
        # TODO
        pass

    def get_data_with_condition(self, o_filter: Optional[Set[Any]] = None, t_filter: Optional[Tuple[date, date]] = None,
                                v_cols: Optional[List[str]] = None) -> pd.DataFrame:
        """
        支持带过滤条件的数据获取方式
            前提，数据已经保存到了 arctic 中

        Parameters
        ----------
        o_filter :
            o 的过滤条件，None 表示所有 O

        t_filter :
            ( start_t , end_t ) t 的过滤条件， None 表示所有 T

        v_cols :
            选择哪些列的内容

        Returns
        -------

        """
        # TODO
        pass


def obj_to_list(obj: Any) -> List[Any]:
    if obj is None:
        return []
    else:
        return obj if isinstance(obj, list) else [obj]


SQL_TABLE_T = TypeVar('SQL_TABLE_T', bound=SQLTableEntity)


class TableFromRDBS(OTVTableInArctic):
    """如果数据来自于 RDBS ， 则这里处理与 rdbs 操作相关的内容"""

    # 这块属于 生成 select 语句的基本元素
    from_table: Type[SQL_TABLE_T]
    """数据主要来自于哪一张表。 eg: QT_DailyQuote """

    inner_join_relation: Tuple[TableColumnDeclarationEntity, List[TableColumnDeclarationEntity]]
    """Join 的关系， 不支持 a inner join b , b inner join c 的级联条件 ，如需支持再增加属性
        eg: (QT_DailyQuote.InnerCode, [SecuMain.InnerCode]) ，表示主表为 QT_DailyQuote 和 SecuMain 进行 inner join  
    """
    where_in_condition: List[Tuple[TableColumnDeclarationEntity, List[Any]]]
    """where in 的条件 eg: [(SecuMain.SecuCategory, [1]),(SecuMain.ListedSector, [2])]"""

    # 得到 sql statement(进一步抽象出一个相对更加通用的结构体)
    def get_sql_select_by_t(self, start: date, end: date) -> str:
        sel_cols = {**{col.name: col.rdbs_original for col in
                       obj_to_list(self.o) + obj_to_list(self.t) + obj_to_list(self.v)}}
        t_column = obj_to_list(self.t)[0].rdbs_original

        sql = f"SELECT {sh.select_with_alias(sel_cols)} FROM {sh.from_(QT_DailyQuote)} " \
            f" {sh.inner_join(*self.inner_join_relation)} " \
            f" WHERE {sh.where_in(self.where_in_condition)} " \
            f" AND {sh.where_compare_op([(t_column, '>=', start), (t_column, '<', end)])}"
        return sql

    def init_history_data(self):
        """
        初始化历史数据，将数据从 RDBS 中读取出来，存入到 arctic 中
        """
        pass


#这个可能是 instance ， 暂时先用 def 进行测试用
class ChnEquityMarketQuotation(TableFromRDBS):
    o = OColumn.from_rdbs_column("equity", SecuMain.SecuCode, "chn_equity")

    # arctic 是通过 column name 为 "date" 来寻找 t 列的，这里 name 不能随意指定
    t = TColumn.from_rdbs_column("date", QT_DailyQuote.TradingDay, "BD")

    v = [
        VColumn.from_rdbs_column("close_price", QT_DailyQuote.ClosePrice),
        VColumn.from_rdbs_column("open_price", QT_DailyQuote.OpenPrice),
        VColumn.from_rdbs_column("high_price", QT_DailyQuote.HighPrice),
        VColumn.from_rdbs_column("prev_close_price", QT_DailyQuote.PrevClosePrice),
        VColumn.from_rdbs_column("low_price", QT_DailyQuote.LowPrice),
        VColumn.from_rdbs_column("turnover_deals_count", QT_DailyQuote.TurnoverDeals),
        VColumn.from_rdbs_column("turnover_dollar_volume", QT_DailyQuote.TurnoverValue),
        VColumn.from_rdbs_column("turnover_shares_volume", QT_DailyQuote.TurnoverVolume)
    ]

    # 这块属于 生成 select 语句的基本元素
    from_table: Type[SQL_TABLE_T] = QT_DailyQuote
    inner_join_relation = (QT_DailyQuote.InnerCode, [SecuMain.InnerCode])
    where_in_condition = [(SecuMain.SecuCategory, get_security_category_type(FinI.Equity)),
                          (SecuMain.ListedSector, get_security_listed_sector_type(FinI.Equity))]


"""
    def _convert_period_equity_mkt_data_to_arctic(self, start: date, end: date, lib_chunk_store, symbol: str,
                                                  chunk_period: str, is_write: bool):
        "将一个时间跨度内的 market data 转储成 arctic 的 chunk store "
        sel_cols = {"close_price": QT_DailyQuote.ClosePrice,
                    "open_price": QT_DailyQuote.OpenPrice,
                    "high_price": QT_DailyQuote.HighPrice,
                    "prev_close_price": QT_DailyQuote.PrevClosePrice,
                    "low_price": QT_DailyQuote.LowPrice,
                    "turnover_deals_count": QT_DailyQuote.TurnoverDeals,
                    "turnover_dollar_volume": QT_DailyQuote.TurnoverValue,
                    "turnover_shares_volume": QT_DailyQuote.TurnoverVolume,
                    "date": QT_DailyQuote.TradingDay,
                    "o": SecuMain.SecuCode
                    }
        sql = f"SELECT {sh.select_with_alias(sel_cols)} FROM {sh.from_(QT_DailyQuote)} " \
            f" {sh.inner_join(QT_DailyQuote.InnerCode, [SecuMain.InnerCode])} " \
            f" WHERE {sh.where_in([(SecuMain.SecuCategory, get_security_category_type(FinI.Equity)), (SecuMain.ListedSector, get_security_listed_sector_type(FinI.Equity))])} " \
            f" AND {sh.where_compare_op([(QT_DailyQuote.TradingDay,'>=',start),(QT_DailyQuote.TradingDay,'<',end)])}"
        run_start = time.time()
        df_all_data: pd.DataFrame = pd.read_sql_query(sql, self._sql_db, index_col=["date", "o"])
        df_all_data.sort_index(axis=0, ascending=True, inplace=True)
        logger.info(f"read {start}-{end} market data, cost {time.time() - run_start} secs , total {len(df_all_data)} rows")
 
"""