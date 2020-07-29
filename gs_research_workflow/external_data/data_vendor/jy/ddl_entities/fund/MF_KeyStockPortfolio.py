# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_KeyStockPortfolio(SQLTableEntity):
    name: str = 'MF_KeyStockPortfolio'
    
    chn_name: str = '公募基金重仓股票组合'
    
    business_unique: str = 'InnerCode,ReportDate,SerialNumber,InvestType'
    
    refresh_freq: str = """季更新"""
    
    comment: str = """1.本表记录基金季报公布重仓股票组合信息，主要包括前十大持有股票的股票代码、数量、市值、占净资产的比例等数据。
2.历史数据：1998年6月起-至今。
3.数据来源：基金公司披露的定期报告。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_KeyStockPortfolio', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    RatioInNV: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_KeyStockPortfolio', column_name='RatioInNV', column_type='decimal(18,6)', nullable=False, chn_name='占资产净值比例')
    """占资产净值比例:"""

    InvestType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_KeyStockPortfolio', column_name='InvestType', column_type='int', nullable=True, chn_name='投资类型')
    """投资类型:投资类型(InvestType)与(CT_SystemConst)表中的DM字段关联，令LB = 1090，得到投资类型的具体描述：1-综合投资，2-积极投资，3-指数投资，4-境内投资，5-沪港通投资。"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_KeyStockPortfolio', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_KeyStockPortfolio', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_KeyStockPortfolio', column_name='InnerCode', column_type='int', nullable=True, chn_name='基金内部编码')
    """基金内部编码:基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_KeyStockPortfolio', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_KeyStockPortfolio', column_name='InfoSource', column_type='varchar(100)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    ReportDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_KeyStockPortfolio', column_name='ReportDate', column_type='datetime', nullable=True, chn_name='报告期')
    """报告期:"""

    SerialNumber: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_KeyStockPortfolio', column_name='SerialNumber', column_type='int', nullable=False, chn_name='序号')
    """序号:"""

    StockInnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_KeyStockPortfolio', column_name='StockInnerCode', column_type='int', nullable=True, chn_name='股票内部代码')
    """股票内部代码:股票内部代码（StockInnerCode）: 当StockInnerCode<1000000时，与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得股票的交易代码、简称等；当StockInnerCode在1000000与2000000之间时，与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）..."""

    SharesHolding: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_KeyStockPortfolio', column_name='SharesHolding', column_type='decimal(18,4)', nullable=False, chn_name='持股数量(股)')
    """持股数量(股):"""

    MarketValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_KeyStockPortfolio', column_name='MarketValue', column_type='decimal(19,4)', nullable=False, chn_name='市值(元)')
    """市值(元):"""

