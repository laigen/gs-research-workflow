# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_StockPortfolioChange(SQLTableEntity):
    name: str = 'MF_StockPortfolioChange'
    
    chn_name: str = '公募基金股票组合重大变动'
    
    business_unique: str = 'InnerCode,ReportDate,ChangeType,StockInnerCode'
    
    refresh_freq: str = """半年更新"""
    
    comment: str = """1.本表记录中报、年报中公布报告期内股票投资组合的重大变动，比如买入了哪些股票、市值有多少、占净资产的比例等。
2.历史数据：2004年6月起-至今。
3.数据来源：基金公司披露的定期报告。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_StockPortfolioChange', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_StockPortfolioChange', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新日期')
    """更新日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_StockPortfolioChange', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_StockPortfolioChange', column_name='InnerCode', column_type='int', nullable=True, chn_name='基金内部编码')
    """基金内部编码:基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    ReportDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_StockPortfolioChange', column_name='ReportDate', column_type='datetime', nullable=True, chn_name='报告期')
    """报告期:"""

    ChangeType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_StockPortfolioChange', column_name='ChangeType', column_type='int', nullable=True, chn_name='变动类型')
    """变动类型:变动类型(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1095，得到变动类型的具体描述：1-买入，2-卖出。"""

    SerialNumber: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_StockPortfolioChange', column_name='SerialNumber', column_type='int', nullable=False, chn_name='序号')
    """序号:"""

    StockInnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_StockPortfolioChange', column_name='StockInnerCode', column_type='int', nullable=True, chn_name='股票内部代码')
    """股票内部代码:"""

    AccumulatedTradeSum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_StockPortfolioChange', column_name='AccumulatedTradeSum', column_type='decimal(19,4)', nullable=False, chn_name='累计买入/卖出金额(元)')
    """累计买入/卖出金额(元):"""

    RatioInNVAtBegin: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_StockPortfolioChange', column_name='RatioInNVAtBegin', column_type='decimal(18,6)', nullable=False, chn_name='占期初基金净值比例')
    """占期初基金净值比例:"""

    RatioInNVAtEnd: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_StockPortfolioChange', column_name='RatioInNVAtEnd', column_type='decimal(18,6)', nullable=False, chn_name='占期末基金净值比例')
    """占期末基金净值比例:"""

