# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_AdjFactorNew(SQLTableEntity):
    name: str = 'HK_AdjFactorNew'
    
    chn_name: str = '港股复权因子(新)'
    
    business_unique: str = 'InnerCode,ExDiviDate'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.港股复权因子表数据主要基于三部分数据计算而得，港股分红、港股发行与上市、港股并股拆股。                                                                               2.本表已处理的情况包括，送股,分红送股，配股(也即供股)，并股拆股；本表处理的特殊情况如实物派送、红利认股证、以股代息等不涉及股本变动的情况，会结合行情表除权的数据进行更新。                                                 
3.对于货币单位问题。均以除权除息日30日内的平均汇率作为计算依据换算为交易货币。 
4.数据范围：1999年至今。
5.数据来源：恒生聚源。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_AdjFactorNew', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_AdjFactorNew', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_AdjFactorNew', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_AdjFactorNew', column_name='InnerCode', column_type='int', nullable=True, chn_name='内部编码')
    """内部编码:港股内部代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。"""

    ExDiviDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_AdjFactorNew', column_name='ExDiviDate', column_type='datetime', nullable=True, chn_name='除权除息日')
    """除权除息日:"""

    AdjustingFactor: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_AdjFactorNew', column_name='AdjustingFactor', column_type='decimal(19,10)', nullable=False, chn_name='精确累积复权因子')
    """精确累积复权因子:"""

    AdjustingConst: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_AdjFactorNew', column_name='AdjustingConst', column_type='decimal(19,10)', nullable=False, chn_name='精确累积复权常数')
    """精确累积复权常数:"""

    AdjustFactor: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_AdjFactorNew', column_name='AdjustFactor', column_type='decimal(19,10)', nullable=False, chn_name='精确复权因子')
    """精确复权因子:"""

    AdjustConst: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_AdjFactorNew', column_name='AdjustConst', column_type='decimal(19,10)', nullable=False, chn_name='精确复权常数')
    """精确复权常数:"""

    RatioAdjustingFactor: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_AdjFactorNew', column_name='RatioAdjustingFactor', column_type='decimal(19,10)', nullable=False, chn_name='比例复权因子')
    """比例复权因子:"""

    InsertTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_AdjFactorNew', column_name='InsertTime', column_type='datetime', nullable=False, chn_name='发布时间')
    """发布时间:"""

