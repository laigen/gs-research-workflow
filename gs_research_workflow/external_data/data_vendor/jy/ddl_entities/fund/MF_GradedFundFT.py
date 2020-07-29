# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_GradedFundFT(SQLTableEntity):
    name: str = 'MF_GradedFundFT'
    
    chn_name: str = '公募基金_分级基金附表'
    
    business_unique: str = '2015年8月后无数据更新，但不排除后续会更新，故保留正常销售'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.本表记录分级基金的份额配比数据。
2.历史数据：2007年7月起-至今。
3.数据来源：基金产品招募说明书。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GradedFundFT', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GradedFundFT', column_name='InnerCode', column_type='int', nullable=True, chn_name='基金内部编码')
    """基金内部编码:基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    EffectiveDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GradedFundFT', column_name='EffectiveDate', column_type='datetime', nullable=True, chn_name='生效日期')
    """生效日期:"""

    DataType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GradedFundFT', column_name='DataType', column_type='int', nullable=True, chn_name='数据类别')
    """数据类别:数据类别(DataType)与(CT_SystemConst)表中的DM字段关联，令LB = 1770 AND DM = 20，得到数据类别的具体描述：20-份额配对转换比例。"""

    DataValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GradedFundFT', column_name='DataValue', column_type='float', nullable=True, chn_name='数值')
    """数值:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GradedFundFT', column_name='EndDate', column_type='datetime', nullable=False, chn_name='截止日期')
    """截止日期:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GradedFundFT', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GradedFundFT', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

