# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_SHSellingList(SQLTableEntity):
    name: str = 'HK_SHSellingList'
    
    chn_name: str = '港股卖空名单表'
    
    business_unique: str = 'InnerCode,InDate,IfEffected'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.记录港股指定卖空名单变化，包含字段有：信息发布日期、豁免卖空价规例、入选日期 、剔除日期 等。                                          2.数据范围：2016-05至今。
3.数据来源：港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SHSellingList', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SHSellingList', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SHSellingList', column_name='InnerCode', column_type='int', nullable=True, chn_name='内部代码')
    """内部代码:内部代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SHSellingList', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    ExempSPRule: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SHSellingList', column_name='ExempSPRule', column_type='int', nullable=False, chn_name='豁免卖空价规例')
    """豁免卖空价规例:豁免卖空价规例（ExempSPRule），该字段固定以下常量：1-是，2-否。"""

    InDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SHSellingList', column_name='InDate', column_type='datetime', nullable=True, chn_name='入选日期')
    """入选日期:"""

    OutDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SHSellingList', column_name='OutDate', column_type='datetime', nullable=False, chn_name='剔除日期')
    """剔除日期:"""

    IfEffected: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SHSellingList', column_name='IfEffected', column_type='int', nullable=True, chn_name='是否有效')
    """是否有效:是否有效（IfEffected），该字段固定以下常量：1-是，2-否。"""

    Remarks: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SHSellingList', column_name='Remarks', column_type='varchar(200)', nullable=False, chn_name='备注')
    """备注:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SHSellingList', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

