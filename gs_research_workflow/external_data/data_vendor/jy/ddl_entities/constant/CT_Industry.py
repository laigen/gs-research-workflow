# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class CT_Industry(SQLTableEntity):
    name: str = 'CT_Industry'
    
    chn_name: str = '行业表'
    
    business_unique: str = 'IndustryNum'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """本表收录行业名称、代码、板块等基本信息。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Industry', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    IndustryNum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Industry', column_name='IndustryNum', column_type='int', nullable=True, chn_name='行业编码')
    """行业编码:"""

    IndustryName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Industry', column_name='IndustryName', column_type='varchar(50)', nullable=True, chn_name='行业名称')
    """行业名称:"""

    IndustryCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Industry', column_name='IndustryCode', column_type='varchar(20)', nullable=True, chn_name='行业代码')
    """行业代码:"""

    IndustryPlate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Industry', column_name='IndustryPlate', column_type='varchar(20)', nullable=False, chn_name='行业板块')
    """行业板块:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Industry', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Industry', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

