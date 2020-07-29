# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class C_ED_MacroIndicatorData(SQLTableEntity):
    name: str = 'C_ED_MacroIndicatorData'
    
    chn_name: str = '宏观基础指标数据'
    
    business_unique: str = 'IndicatorCode,EndDate'
    
    refresh_freq: str = """"""
    
    comment: str = """收录宏观基础指标时间序列数据"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_MacroIndicatorData', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    IndicatorCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_MacroIndicatorData', column_name='IndicatorCode', column_type='int', nullable=True, chn_name='指标代码')
    """指标代码:指标代码（IndicatorCode）：与“宏观指标主表（C_ED_IndicatorMain）”中的“指标代码（IndicatorCode）” 关联，得到宏观指标的基础信息。"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_MacroIndicatorData', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_MacroIndicatorData', column_name='EndDate', column_type='datetime', nullable=False, chn_name='截止日期')
    """截止日期:"""

    DataValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_MacroIndicatorData', column_name='DataValue', column_type='decimal(28,6)', nullable=False, chn_name='指标数据')
    """指标数据:"""

    PowerNumber: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_MacroIndicatorData', column_name='PowerNumber', column_type='smallint', nullable=False, chn_name='量纲系数')
    """量纲系数:量纲系数（PowerNumber）：聚源宏观数据都存放最小单位数据，此字段对应展示单位。例如：如果数据按百万公布，即10的6次方，则此处存的是6。"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_MacroIndicatorData', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_ED_MacroIndicatorData', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

