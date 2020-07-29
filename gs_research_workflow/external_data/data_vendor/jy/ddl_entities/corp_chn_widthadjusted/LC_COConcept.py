# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_COConcept(SQLTableEntity):
    name: str = 'LC_COConcept'
    
    chn_name: str = '概念所属公司表'
    
    business_unique: str = 'InnerCode,ConceptCode,InDate'
    
    refresh_freq: str = """8点"""
    
    comment: str = """记录A股上市公司所属概念信息"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_COConcept', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_COConcept', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_COConcept', column_name='InnerCode', column_type='int', nullable=True, chn_name='证券内部编码')
    """证券内部编码:证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。"""

    ConceptCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_COConcept', column_name='ConceptCode', column_type='int', nullable=True, chn_name='概念代码')
    """概念代码:概念代码(ConceptCode)：与“概念板块表(LC_ConceptList)”中的“概念代码(ConceptCode)”关联，得到所属概念的信息。"""

    InDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_COConcept', column_name='InDate', column_type='datetime', nullable=True, chn_name='纳入日期')
    """纳入日期:"""

    OutDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_COConcept', column_name='OutDate', column_type='datetime', nullable=False, chn_name='剔除日期')
    """剔除日期:"""

    IndiState: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_COConcept', column_name='IndiState', column_type='int', nullable=True, chn_name='所属状态')
    """所属状态:所属状态(IndiState)，该字段固定以下常量：1-正常，0-终止。"""

    Remark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_COConcept', column_name='Remark', column_type='varchar(500)', nullable=False, chn_name='备注')
    """备注:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_COConcept', column_name='InfoPublDate', column_type='datetime', nullable=True, chn_name='发布时间')
    """发布时间:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_COConcept', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

