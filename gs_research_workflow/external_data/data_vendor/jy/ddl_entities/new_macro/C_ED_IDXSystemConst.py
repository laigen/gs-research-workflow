# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class C_ED_IDXSystemConst(SQLTableEntity):
    name: str = 'C_ED_IDXSystemConst'
    
    chn_name: str = '宏观指标系统常量表'
    
    business_unique: str = '整库销售，表不单独销售'
    
    refresh_freq: str = """"""
    
    comment: str = """收录宏观指标的常量"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IDXSystemConst', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    CVALUE: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IDXSystemConst', column_name='CVALUE', column_type='varchar(500)', nullable=False, chn_name='预留标志位(字符值)')
    """预留标志位(字符值):"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IDXSystemConst', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='修改日期')
    """修改日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IDXSystemConst', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    LB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IDXSystemConst', column_name='LB', column_type='int', nullable=True, chn_name='常量分类编码')
    """常量分类编码:"""

    LBMC: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IDXSystemConst', column_name='LBMC', column_type='varchar(50)', nullable=True, chn_name='常量分类名称')
    """常量分类名称:"""

    DM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IDXSystemConst', column_name='DM', column_type='int', nullable=True, chn_name='常量代码')
    """常量代码:"""

    MS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IDXSystemConst', column_name='MS', column_type='varchar(300)', nullable=True, chn_name='常量描述')
    """常量描述:"""

    FJD: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IDXSystemConst', column_name='FJD', column_type='int', nullable=False, chn_name='父级代码')
    """父级代码:"""

    IVALUE: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IDXSystemConst', column_name='IVALUE', column_type='int', nullable=False, chn_name='预留标志位(整形值)')
    """预留标志位(整形值):"""

    FVALUE: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IDXSystemConst', column_name='FVALUE', column_type='float', nullable=False, chn_name='预留标志位(浮点值)')
    """预留标志位(浮点值):"""

    DVALUE: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IDXSystemConst', column_name='DVALUE', column_type='datetime', nullable=False, chn_name='预留标志位(日期值)')
    """预留标志位(日期值):"""

