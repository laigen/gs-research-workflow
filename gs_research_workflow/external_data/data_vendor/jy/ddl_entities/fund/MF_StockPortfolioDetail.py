# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_StockPortfolioDetail(SQLTableEntity):
    name: str = 'MF_StockPortfolioDetail'
    
    chn_name: str = '公募基金股票组合明细'
    
    business_unique: str = 'InnerCode,ReportDate,InvestType,SerialNumber'
    
    refresh_freq: str = """半年更新"""
    
    comment: str = """1.本表记录基金年报、半年报公布股票组合明细信息，包括股票的名称、代码、持有数量、持有市值、市值占基金净资产的比例等数据。
2.历史数据：1998年12月起-至今。
3.数据来源：基金公司披露的定期报告。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_StockPortfolioDetail', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    RatioInNV: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_StockPortfolioDetail', column_name='RatioInNV', column_type='decimal(18,6)', nullable=False, chn_name='占资产净值比例')
    """占资产净值比例:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_StockPortfolioDetail', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新日期')
    """更新日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_StockPortfolioDetail', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_StockPortfolioDetail', column_name='InnerCode', column_type='int', nullable=True, chn_name='基金内部编码')
    """基金内部编码:基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_StockPortfolioDetail', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    ReportDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_StockPortfolioDetail', column_name='ReportDate', column_type='datetime', nullable=True, chn_name='报告期')
    """报告期:"""

    InvestType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_StockPortfolioDetail', column_name='InvestType', column_type='int', nullable=True, chn_name='投资类型')
    """投资类型:投资类型(InvestType)与(CT_SystemConst)表中的DM字段关联，令LB = 1090，得到投资类型的具体描述：1-综合投资，2-积极投资，3-指数投资，4-境内投资，5-沪港通投资。"""

    SerialNumber: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_StockPortfolioDetail', column_name='SerialNumber', column_type='int', nullable=True, chn_name='序号')
    """序号:"""

    StockInnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_StockPortfolioDetail', column_name='StockInnerCode', column_type='int', nullable=True, chn_name='股票代码')
    """股票代码:股票内部代码（StockInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得股票的交易代码、简称等。"""

    SharesHolding: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_StockPortfolioDetail', column_name='SharesHolding', column_type='decimal(18,0)', nullable=False, chn_name='持股数量(股)')
    """持股数量(股):"""

    MarketValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_StockPortfolioDetail', column_name='MarketValue', column_type='decimal(19,4)', nullable=False, chn_name='市值(元)')
    """市值(元):"""

