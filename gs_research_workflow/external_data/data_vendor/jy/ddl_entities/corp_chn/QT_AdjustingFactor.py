# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class QT_AdjustingFactor(SQLTableEntity):
    name: str = 'QT_AdjustingFactor'
    
    chn_name: str = '复权因子表'
    
    business_unique: str = 'InnerCode,ExDiviDate'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.收录股票、基金、债券等因为分红配股发生除权除息，衍生计算出的复权因子、复权常数、比例复权因子等指标，可用于推算股票前复权或后复权价格。
2.数据范围:证券上市起-至今"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_AdjustingFactor', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_AdjustingFactor', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    ExDiviDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_AdjustingFactor', column_name='ExDiviDate', column_type='datetime', nullable=True, chn_name='除权除息日')
    """除权除息日:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_AdjustingFactor', column_name='InnerCode', column_type='int', nullable=True, chn_name='证券内部编码')
    """证券内部编码:证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。"""

    AdjustingFactor: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_AdjustingFactor', column_name='AdjustingFactor', column_type='float', nullable=False, chn_name='精确复权因子')
    """精确复权因子:"""

    AdjustingConst: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_AdjustingFactor', column_name='AdjustingConst', column_type='float', nullable=False, chn_name='精确复权常数')
    """精确复权常数:"""

    RatioAdjustingFactor: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_AdjustingFactor', column_name='RatioAdjustingFactor', column_type='float', nullable=False, chn_name='比例复权因子')
    """比例复权因子:"""

    AccuCashDivi: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_AdjustingFactor', column_name='AccuCashDivi', column_type='float', nullable=False, chn_name='累计分红')
    """累计分红:"""

    AccuBonusShareRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_AdjustingFactor', column_name='AccuBonusShareRatio', column_type='float', nullable=False, chn_name='累计送股')
    """累计送股:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_AdjustingFactor', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

