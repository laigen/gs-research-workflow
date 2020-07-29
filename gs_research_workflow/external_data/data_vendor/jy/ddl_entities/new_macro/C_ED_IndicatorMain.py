# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class C_ED_IndicatorMain(SQLTableEntity):
    name: str = 'C_ED_IndicatorMain'
    
    chn_name: str = '宏观指标主表'
    
    business_unique: str = 'IndicatorCode'
    
    refresh_freq: str = """"""
    
    comment: str = """收录宏观指标信息，包括指标名称、各种维度。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IndicatorMain', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    BeginDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IndicatorMain', column_name='BeginDate', column_type='datetime', nullable=False, chn_name='起始日期')
    """起始日期:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IndicatorMain', column_name='EndDate', column_type='datetime', nullable=False, chn_name='截止日期(最新日期)')
    """截止日期(最新日期):"""

    UnitCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IndicatorMain', column_name='UnitCode', column_type='int', nullable=False, chn_name='单位代码')
    """单位代码:单位代码(UnitCode)与(C_ED_IDXSystemConst)表中的DM字段关联，令LB = 17，得到单位代码的具体描述："""

    UnitCodeReport: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IndicatorMain', column_name='UnitCodeReport', column_type='int', nullable=False, chn_name='单位代码(披露)')
    """单位代码(披露):单位代码(披露)(UnitCodeReport)与(C_ED_IDXSystemConst)表中的DM字段关联，令LB = 17，得到单位代码(披露)的具体描述："""

    DisclosureFrequency: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IndicatorMain', column_name='DisclosureFrequency', column_type='int', nullable=False, chn_name='数据披露频率')
    """数据披露频率:数据披露频率(DisclosureFrequency)与(C_ED_IDXSystemConst)表中的DM字段关联，令LB = 11，得到数据披露频率的具体描述："""

    IndiRemark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IndicatorMain', column_name='IndiRemark', column_type='varchar(2000)', nullable=False, chn_name='备注')
    """备注:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IndicatorMain', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IndicatorMain', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    IndicatorCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IndicatorMain', column_name='IndicatorCode', column_type='int', nullable=True, chn_name='指标代码')
    """指标代码:指标代码(IndicatorCode)：宏观指标聚源自编内码"""

    IndicatorName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IndicatorMain', column_name='IndicatorName', column_type='varchar(300)', nullable=False, chn_name='指标名称')
    """指标名称:"""

    InfoSourceCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IndicatorMain', column_name='InfoSourceCode', column_type='int', nullable=False, chn_name='信息来源代码')
    """信息来源代码:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IndicatorMain', column_name='InfoSource', column_type='varchar(50)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    PowerNumber: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IndicatorMain', column_name='PowerNumber', column_type='smallint', nullable=False, chn_name='量纲系数')
    """量纲系数:量纲系数(PowerNumber)：聚源宏观数据都存放最小单位数据，此字段对应展示单位。例如：如果数据按百万公布，即10的6次方，则此处存的是6。"""

    IndiDimension: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IndicatorMain', column_name='IndiDimension', column_type='varchar(500)', nullable=False, chn_name='指标维度')
    """指标维度:指标维度(IndiDimension)：宏观指标所有维度的代码序列"""

    IndiCategory: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IndicatorMain', column_name='IndiCategory', column_type='int', nullable=False, chn_name='指标类别')
    """指标类别:指标类别(IndiCategory)与(C_ED_IDXSystemConst)表中的DM字段关联，令LB = 1001，得到指标类别的具体描述："""

    IndiState: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_IndicatorMain', column_name='IndiState', column_type='tinyint', nullable=False, chn_name='指标状态')
    """指标状态:指标状态(IndiState)，该字段固定以下常量：1-有效  ；5-终止"""

