# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_FundPortifolioDetail(SQLTableEntity):
    name: str = 'MF_FundPortifolioDetail'
    
    chn_name: str = '公募基金投资基金明细'
    
    business_unique: str = 'InnerCode,ReportDate,FundInnerCode'
    
    refresh_freq: str = """半年更新"""
    
    comment: str = """1.本表记录期末投资目标基金明细。
2.历史数据：2009年12月起-至今。
3.数据来源：基金公司披露的定期报告。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundPortifolioDetail', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundPortifolioDetail', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundPortifolioDetail', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundPortifolioDetail', column_name='InnerCode', column_type='int', nullable=True, chn_name='基金内部编码')
    """基金内部编码:基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundPortifolioDetail', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    ReportDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundPortifolioDetail', column_name='ReportDate', column_type='datetime', nullable=True, chn_name='报告期')
    """报告期:"""

    SerialNumber: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundPortifolioDetail', column_name='SerialNumber', column_type='int', nullable=False, chn_name='序号')
    """序号:"""

    FundInnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundPortifolioDetail', column_name='FundInnerCode', column_type='int', nullable=True, chn_name='投资基金内部编码')
    """投资基金内部编码:投资基金内部编码（FundInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得投资基金的交易代码、简称等。"""

    SharesHolding: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundPortifolioDetail', column_name='SharesHolding', column_type='decimal(18,4)', nullable=False, chn_name='持有数量(份)')
    """持有数量(份):"""

    MarketValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundPortifolioDetail', column_name='MarketValue', column_type='decimal(18,4)', nullable=False, chn_name='公允价值(元)')
    """公允价值(元):"""

    RatioInNV: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundPortifolioDetail', column_name='RatioInNV', column_type='decimal(9,6)', nullable=False, chn_name='占资产净值比例(%)')
    """占资产净值比例(%):"""

