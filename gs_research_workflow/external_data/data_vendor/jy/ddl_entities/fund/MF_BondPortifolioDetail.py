# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_BondPortifolioDetail(SQLTableEntity):
    name: str = 'MF_BondPortifolioDetail'
    
    chn_name: str = '公募基金债券组合明细'
    
    business_unique: str = 'InnerCode,ReportDate,BondCode,IfInConvertibleTerm'
    
    refresh_freq: str = """半年更新"""
    
    comment: str = """1.本表记录基金债券组合中重仓的债券及处于转股期的可转换债券明细，包括债券代码、持有数量、持有市值、市值占净资产的比例等数据。
2.历史数据：2000年12月起-至今。
3.数据来源：基金公司披露的定期报告。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BondPortifolioDetail', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    IfInConvertibleTerm: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BondPortifolioDetail', column_name='IfInConvertibleTerm', column_type='tinyint', nullable=True, chn_name='报告期末是否处于转股期')
    """报告期末是否处于转股期:报告期末是否处于转股期（IfInConvertibleTerm），该字段固定以下常量：1-处于转股期的可转换债券；0-重仓债券投资明细（排名包含转股期可转债）"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BondPortifolioDetail', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新日期')
    """更新日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BondPortifolioDetail', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BondPortifolioDetail', column_name='InnerCode', column_type='int', nullable=True, chn_name='基金内部编码')
    """基金内部编码:基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BondPortifolioDetail', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    ReportDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BondPortifolioDetail', column_name='ReportDate', column_type='datetime', nullable=True, chn_name='报告期')
    """报告期:"""

    SerialNumber: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BondPortifolioDetail', column_name='SerialNumber', column_type='int', nullable=True, chn_name='序号')
    """序号:"""

    BondCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BondPortifolioDetail', column_name='BondCode', column_type='int', nullable=False, chn_name='债券代码')
    """债券代码:债券代码（BondCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得债券的交易代码、简称等。"""

    HoldVolume: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BondPortifolioDetail', column_name='HoldVolume', column_type='decimal(18,4)', nullable=False, chn_name='持有数量(张)')
    """持有数量(张):"""

    MarketValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BondPortifolioDetail', column_name='MarketValue', column_type='decimal(19,4)', nullable=False, chn_name='市值(元)')
    """市值(元):"""

    RatioInNV: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BondPortifolioDetail', column_name='RatioInNV', column_type='decimal(18,6)', nullable=False, chn_name='占资产净值比例')
    """占资产净值比例:"""

