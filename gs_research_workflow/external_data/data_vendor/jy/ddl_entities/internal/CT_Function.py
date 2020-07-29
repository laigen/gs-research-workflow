# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class CT_Function(SQLTableEntity):
    name: str = 'CT_Function'
    
    chn_name: str = '标准函数表'
    
    business_unique: str = '内部专用'
    
    refresh_freq: str = """"""
    
    comment: str = """收录常用函数数值表数据，包括：标准正态分布函数数值表"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Function', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    FuncCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Function', column_name='FuncCode', column_type='int', nullable=True, chn_name='函数代码')
    """函数代码:"""

    FuncName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Function', column_name='FuncName', column_type='varchar(50)', nullable=False, chn_name='函数名称')
    """函数名称:"""

    ParaCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Function', column_name='ParaCode', column_type='int', nullable=True, chn_name='参数代码')
    """参数代码:"""

    XPara: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Function', column_name='XPara', column_type='decimal(9,6)', nullable=False, chn_name='参数-X')
    """参数-X:"""

    YPara: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Function', column_name='YPara', column_type='decimal(9,6)', nullable=False, chn_name='参数-Y')
    """参数-Y:"""

    FuncResult: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Function', column_name='FuncResult', column_type='decimal(9,6)', nullable=False, chn_name='输出结果')
    """输出结果:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Function', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='修改日期')
    """修改日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Function', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

