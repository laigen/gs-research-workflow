# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_ConceptList(SQLTableEntity):
    name: str = 'LC_ConceptList'
    
    chn_name: str = '概念板块常量表'
    
    business_unique: str = 'ClassCode,SubclassCode,ConceptCode,BeginDate'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """记录A股市场中热点概念的相关信息"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ConceptList', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    ConceptState: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ConceptList', column_name='ConceptState', column_type='int', nullable=True, chn_name='所属状态')
    """所属状态:所属状态(ConceptState)，该字段固定以下常量：1-正常，0-终止。"""

    Remark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ConceptList', column_name='Remark', column_type='varchar(500)', nullable=False, chn_name='备注')
    """备注:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ConceptList', column_name='InfoPublDate', column_type='datetime', nullable=True, chn_name='发布时间')
    """发布时间:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ConceptList', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ConceptList', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    ClassCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ConceptList', column_name='ClassCode', column_type='int', nullable=True, chn_name='所属1级概念代码')
    """所属1级概念代码:"""

    ClassName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ConceptList', column_name='ClassName', column_type='varchar(100)', nullable=False, chn_name='所属1级概念名称')
    """所属1级概念名称:"""

    SubclassCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ConceptList', column_name='SubclassCode', column_type='int', nullable=True, chn_name='所属2级概念代码')
    """所属2级概念代码:"""

    SubclassName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ConceptList', column_name='SubclassName', column_type='varchar(100)', nullable=False, chn_name='所属2级概念名称')
    """所属2级概念名称:"""

    ConceptCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ConceptList', column_name='ConceptCode', column_type='int', nullable=True, chn_name='概念代码')
    """概念代码:"""

    ConceptName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ConceptList', column_name='ConceptName', column_type='varchar(100)', nullable=False, chn_name='概念名称')
    """概念名称:"""

    BeginDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ConceptList', column_name='BeginDate', column_type='datetime', nullable=True, chn_name='生成日期')
    """生成日期:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ConceptList', column_name='EndDate', column_type='datetime', nullable=False, chn_name='终止日期')
    """终止日期:"""

