# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class JYDB_DeleteRec(SQLTableEntity):
    name: str = 'JYDB_DeleteRec'
    
    chn_name: str = 'JYDB_删除表'
    
    business_unique: str = '无'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """本表记录各表删除记录的ID值"""

    TABLENAME: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='JYDB_DeleteRec', column_name='TABLENAME', column_type='varchar(100)', nullable=True, chn_name='表名')
    """表名:"""

    RECID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='JYDB_DeleteRec', column_name='RECID', column_type='bigint', nullable=True, chn_name='被删除表ID')
    """被删除表ID:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='JYDB_DeleteRec', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='修改日期')
    """修改日期:"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='JYDB_DeleteRec', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='JYDB_DeleteRec', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

