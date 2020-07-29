# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_BondPortifolioStru(SQLTableEntity):
    name: str = 'MF_BondPortifolioStru'
    
    chn_name: str = '公募基金债券组合结构'
    
    business_unique: str = 'InnerCode,ReportDate,BondType'
    
    refresh_freq: str = """半年更新"""
    
    comment: str = """1.本表记录基金债券组合结构信息，包括国债、金融债、企业债、可转债、央行票据等各类券种占债券总体的比重。
2.历史数据：2000年3月起-至今。
3.数据来源：基金公司披露的定期报告。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BondPortifolioStru', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BondPortifolioStru', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BondPortifolioStru', column_name='InnerCode', column_type='int', nullable=True, chn_name='基金内部编码')
    """基金内部编码:基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BondPortifolioStru', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    ReportDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BondPortifolioStru', column_name='ReportDate', column_type='datetime', nullable=True, chn_name='报告期')
    """报告期:"""

    BondType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BondPortifolioStru', column_name='BondType', column_type='varchar(50)', nullable=True, chn_name='债券类型')
    """债券类型:债券类型（BondType）：包括国债、金融债、企业债、可转换债券、央行票据"""

    MarketValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BondPortifolioStru', column_name='MarketValue', column_type='decimal(19,4)', nullable=False, chn_name='市值(元)')
    """市值(元):"""

    RatioInNV: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BondPortifolioStru', column_name='RatioInNV', column_type='decimal(18,6)', nullable=False, chn_name='占资产净值比例')
    """占资产净值比例:"""

    RatioInBondPortfolio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BondPortifolioStru', column_name='RatioInBondPortfolio', column_type='decimal(18,6)', nullable=False, chn_name='占债券组合市值比例')
    """占债券组合市值比例:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_BondPortifolioStru', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新日期')
    """更新日期:"""

