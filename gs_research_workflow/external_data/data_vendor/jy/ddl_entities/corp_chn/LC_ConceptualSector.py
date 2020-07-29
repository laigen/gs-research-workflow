# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_ConceptualSector(SQLTableEntity):
    name: str = 'LC_ConceptualSector'
    
    chn_name: str = '个股所属板块常量表'
    
    business_unique: str = '建议使用概念板块相关新表'
    
    refresh_freq: str = """"""
    
    comment: str = """个股所属板块（新）表中的个股所属板块常量"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ConceptualSector', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    BeginDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ConceptualSector', column_name='BeginDate', column_type='datetime', nullable=False, chn_name='板块生成时间')
    """板块生成时间:"""

    LOneName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ConceptualSector', column_name='LOneName', column_type='varchar(50)', nullable=True, chn_name='父板块名称')
    """父板块名称:"""

    LOneCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ConceptualSector', column_name='LOneCode', column_type='int', nullable=False, chn_name='父板块编码')
    """父板块编码:"""

    LTwoName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ConceptualSector', column_name='LTwoName', column_type='varchar(50)', nullable=False, chn_name='板块名称')
    """板块名称:"""

    LTwoCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ConceptualSector', column_name='LTwoCode', column_type='varchar(50)', nullable=False, chn_name='板块编码')
    """板块编码:"""

    Flag: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ConceptualSector', column_name='Flag', column_type='int', nullable=False, chn_name='板块状态')
    """板块状态:板块状态(Flag)与(CT_SystemConst)表中的DM字段关联，令LB = 1815 AND DM IN (1,2)，得到板块状态的具体描述：1-正常，2-终止。"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ConceptualSector', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ConceptualSector', column_name='JSID', column_type='bigint', nullable=False, chn_name='JSID')
    """JSID:"""

