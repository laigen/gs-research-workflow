# -*- coding: UTF-8 -*-

from typing import List, Tuple, Dict, Any
import datetime

from gs_research_workflow.external_data.table_declaration_base import TableColumnDeclarationEntity, SQLTableEntity


class SQLStatementHelper:

    @staticmethod
    def literal_to_sql(l) -> str:
        if isinstance(l, int):
            return str(l)
        elif isinstance(l, datetime.date):
            return l.strftime("'%Y-%m-%d'")
        elif isinstance(l, str):
            return "'" + str + "'"
        else:
            return str(l)

    @staticmethod
    def select(select_fields: List[TableColumnDeclarationEntity]) -> str:
        return " , ".join([x.tbl_name + "." + x.name for x in select_fields])

    @staticmethod
    def select_with_alias(fields: Dict[str, TableColumnDeclarationEntity]) -> str:
        return " , ".join([col.tbl_name + "." + col.name + " as " + col_alias for (col_alias, col) in fields.items()])

    @staticmethod
    def from_(from_table: SQLTableEntity) -> str:
        # NOTE: FROM python 是保留字，所以加了一个下划线作为后缀
        return " " + from_table.table_name()

    @staticmethod
    def inner_join(main_table_column: TableColumnDeclarationEntity,
                   join_table_columns: List[TableColumnDeclarationEntity]) -> str:
        return " ".join(
            [" INNER JOIN {join_table} ON {join_field1} = {join_field2}".format(join_table=x.tbl_name,
                                                                                join_field1=main_table_column.tbl_name + "." + main_table_column.name,
                                                                                join_field2=x.tbl_name + "." + x.name)
             for x in join_table_columns])

    @staticmethod
    def where_in(conditions: List[Tuple[TableColumnDeclarationEntity, List[Any]]]) -> str:
        return " AND ".join([" {field} in ({conds}) ".format(field=x[0].tbl_name + "." + x[0].name,
                                                             conds=",".join(
                                                                 [SQLStatementHelper.literal_to_sql(i) for i in x[1]]))
                             for x in conditions])

    @staticmethod
    def where_compare_op(conditions: List[Tuple[TableColumnDeclarationEntity, str, Any]]) -> str:
        """比较操作符，如 [（field1,'>=',v1), (field2,'<=',v2)]"""
        return " AND ".join([" {field} {op} {cond}".format(field=x[0].tbl_name + "." + x[0].name, op=x[1],
                                                           cond=SQLStatementHelper.literal_to_sql(x[2]))
                             for x in conditions])

    @staticmethod
    def order_by(sort_cond: List[Tuple[TableColumnDeclarationEntity, bool]]) -> str:
        return " , ".join([" {field} {asc} ".format(field=x[0].tbl_name + "." + x[0].name,
                                                    asc=x[1]) for x in sort_cond])

    @staticmethod
    def limit(rows_count: int, start_pos: int = 1) -> str:
        return " LIMIT " + str(start_pos) + " , " + str(rows_count)
