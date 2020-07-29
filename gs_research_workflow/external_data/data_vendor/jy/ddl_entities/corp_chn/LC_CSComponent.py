# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_CSComponent(SQLTableEntity):
    name: str = 'LC_CSComponent'
    
    chn_name: str = '个股所属板块(新)'
    
    business_unique: str = '建议使用概念板块相关新表'
    
    refresh_freq: str = """"""
    
    comment: str = """记录A股市场中，个股所属概念板块和地域板块的信息。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CSComponent', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CSComponent', column_name='JSID', column_type='bigint', nullable=False, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CSComponent', column_name='InnerCode', column_type='int', nullable=True, chn_name='证券内部编码')
    """证券内部编码:"""

    SecuCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CSComponent', column_name='SecuCode', column_type='varchar(10)', nullable=False, chn_name='证券代码')
    """证券代码:"""

    SecuAbbr: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CSComponent', column_name='SecuAbbr', column_type='varchar(20)', nullable=False, chn_name='证券简称')
    """证券简称:"""

    CSCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CSComponent', column_name='CSCode', column_type='int', nullable=False, chn_name='所属板块编码')
    """所属板块编码:所属板块编码(CSCode):与“个股所属板块常量表(LC_ConceptualSector)”中的“板块编码(LTwoCode)”关联，得到具体板块名称。"""

    InDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CSComponent', column_name='InDate', column_type='datetime', nullable=False, chn_name='纳入日期')
    """纳入日期:"""

    OutDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CSComponent', column_name='OutDate', column_type='datetime', nullable=False, chn_name='剔除日期')
    """剔除日期:"""

    Flag: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CSComponent', column_name='Flag', column_type='int', nullable=False, chn_name='所属状态')
    """所属状态:所属状态(Flag)与(CT_SystemConst)表中的DM字段关联，令LB = 1815 AND DM IN (1,2)，得到所属状态的具体描述：1-正常，2-终止。"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CSComponent', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

