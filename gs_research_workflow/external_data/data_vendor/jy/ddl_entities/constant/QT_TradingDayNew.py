# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class QT_TradingDayNew(SQLTableEntity):
    name: str = 'QT_TradingDayNew'
    
    chn_name: str = '交易日表(新)'
    
    business_unique: str = 'TradingDate,SecuMarket'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """本表收录各个市场的交易日信息，包括每个日期是否是交易日，是否周、月、季、年最后一个交易日"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_TradingDayNew', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_TradingDayNew', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    TradingDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_TradingDayNew', column_name='TradingDate', column_type='datetime', nullable=True, chn_name='日期')
    """日期:"""

    IfTradingDay: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_TradingDayNew', column_name='IfTradingDay', column_type='int', nullable=False, chn_name='是否交易日')
    """是否交易日:是否交易日（IfTradingDay），该字段固定以下常量：1-是，2-否。"""

    SecuMarket: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_TradingDayNew', column_name='SecuMarket', column_type='int', nullable=False, chn_name='证券市场')
    """证券市场:证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB = 201，得到证券市场的具体描述：71-柜台交易市场，72-香港联交所，77-美国纳斯达克证券交易所，83-上海证券交易所，85-伦敦证券交易所，89-银行间债券市场。"""

    IfWeekEnd: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_TradingDayNew', column_name='IfWeekEnd', column_type='int', nullable=False, chn_name='是否周最后交易日')
    """是否周最后交易日:是否周最后交易日（IfWeekEnd），该字段固定以下常量：1-是，2-否。"""

    IfMonthEnd: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_TradingDayNew', column_name='IfMonthEnd', column_type='int', nullable=False, chn_name='是否月最后交易日')
    """是否月最后交易日:是否月最后交易日（IfMonthEnd），该字段固定以下常量：1-是，2-否。"""

    IfQuarterEnd: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_TradingDayNew', column_name='IfQuarterEnd', column_type='int', nullable=False, chn_name='是否季最后交易日')
    """是否季最后交易日:是否季最后交易日（IfQuarterEnd），该字段固定以下常量：1-是，2-否。"""

    IfYearEnd: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_TradingDayNew', column_name='IfYearEnd', column_type='int', nullable=False, chn_name='是否年最后交易日')
    """是否年最后交易日:是否年最后交易日（IfYearEnd），该字段固定以下常量：1-是，2-否。"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_TradingDayNew', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

