# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class CT_SystemConst(SQLTableEntity):
    name: str = 'CT_SystemConst'
    
    chn_name: str = '系统常量表'
    
    business_unique: str = 'LB,DM'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """本表收录数据库中各种常量值的具体分类和常量名称描述。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_SystemConst', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_SystemConst', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='修改日期')
    """修改日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_SystemConst', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    LB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_SystemConst', column_name='LB', column_type='int', nullable=True, chn_name='常量分类编码')
    """常量分类编码:"""

    LBMC: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_SystemConst', column_name='LBMC', column_type='varchar(50)', nullable=True, chn_name='常量分类名称')
    """常量分类名称:"""

    MS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_SystemConst', column_name='MS', column_type='varchar(300)', nullable=False, chn_name='常量描述')
    """常量描述:"""

    DM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_SystemConst', column_name='DM', column_type='int', nullable=True, chn_name='常量代码')
    """常量代码:"""

    CVALUE: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_SystemConst', column_name='CVALUE', column_type='varchar(2000)', nullable=False, chn_name='字符值')
    """字符值:"""

    DVALUE: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_SystemConst', column_name='DVALUE', column_type='datetime', nullable=False, chn_name='日期值')
    """日期值:"""

    FVALUE: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_SystemConst', column_name='FVALUE', column_type='float', nullable=False, chn_name='浮点值')
    """浮点值:"""

    IVALUE: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_SystemConst', column_name='IVALUE', column_type='int', nullable=False, chn_name='整型值')
    """整型值:"""

