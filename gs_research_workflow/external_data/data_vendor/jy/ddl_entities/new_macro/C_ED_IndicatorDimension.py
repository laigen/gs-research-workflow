# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class C_ED_IndicatorDimension(SQLTableEntity):
    name: str = 'C_ED_IndicatorDimension'
    
    chn_name: str = '宏观指标维度表'
    
    business_unique: str = 'IndicatorCode,CategoryCode'
    
    refresh_freq: str = """"""
    
    comment: str = """收录宏观指标的维度信息"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IndicatorDimension', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    IndicatorCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IndicatorDimension', column_name='IndicatorCode', column_type='int', nullable=True, chn_name='指标代码')
    """指标代码:指标代码（IndicatorCode）：与“宏观指标主表（C_ED_IndicatorMain）”中的“指标代码（IndicatorCode）” 关联，得到宏观指标的基础信息。"""

    CategoryCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IndicatorDimension', column_name='CategoryCode', column_type='int', nullable=True, chn_name='维度类别')
    """维度类别:"""

    CategoryName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IndicatorDimension', column_name='CategoryName', column_type='varchar(50)', nullable=False, chn_name='维度类别名称')
    """维度类别名称:"""

    DimensionCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IndicatorDimension', column_name='DimensionCode', column_type='int', nullable=True, chn_name='维度代码')
    """维度代码:"""

    DimensionName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IndicatorDimension', column_name='DimensionName', column_type='varchar(300)', nullable=False, chn_name='维度名称')
    """维度名称:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IndicatorDimension', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IndicatorDimension', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

