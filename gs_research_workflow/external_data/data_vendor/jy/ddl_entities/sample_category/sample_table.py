# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class Sample_Table(SQLTableEntity):
    name: str = 'CT_Function'

    chn_name: str = '标准函数表'

    business_unique: str = '内部专用'

    refresh_freq: str = """"""

    comment: str = """收录常用函数数值表数据，包括：标准正态分布函数数值表"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Function', column_name='ID', column_type='bigint',nullable=True, chn_name='ID')
    """"""

    FuncCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Function', column_name='FuncCode', column_type='int',nullable=True, chn_name='函数代码')
    """"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Function', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='修改日期')
    """"""
