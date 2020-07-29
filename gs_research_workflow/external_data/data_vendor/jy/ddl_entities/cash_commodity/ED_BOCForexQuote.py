# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class ED_BOCForexQuote(SQLTableEntity):
    name: str = 'ED_BOCForexQuote'
    
    chn_name: str = '中国银行外汇牌价'
    
    business_unique: str = 'EndDate,StatPeriodCode,CurrencyCode'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.收录中国银行公布的当天首笔外汇价格，包括现汇买入价、现钞买入价、卖出价、基准价等
2.数据范围：1994年8月-至今
3.数据源：中国银行"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='ED_BOCForexQuote', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='ED_BOCForexQuote', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新日期')
    """更新日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='ED_BOCForexQuote', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='ED_BOCForexQuote', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='ED_BOCForexQuote', column_name='InfoSource', column_type='varchar(50)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    StatPeriodCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='ED_BOCForexQuote', column_name='StatPeriodCode', column_type='int', nullable=False, chn_name='数据统计期间代码')
    """数据统计期间代码:数据统计期间代码(StatPeriodCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1074 AND DM IN (3)，得到数据统计期间代码的具体描述：3-期末累计。"""

    CurrencyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='ED_BOCForexQuote', column_name='CurrencyCode', column_type='int', nullable=False, chn_name='货币代码')
    """货币代码:货币代码(CurrencyCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1068，得到货币代码的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，1170-约旦第纳尔，1180-科..."""

    BidPriceSpot: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='ED_BOCForexQuote', column_name='BidPriceSpot', column_type='decimal(19,4)', nullable=False, chn_name='现汇买入价(人民币元/100外币)')
    """现汇买入价(人民币元/100外币):"""

    BidPriceCurrency: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='ED_BOCForexQuote', column_name='BidPriceCurrency', column_type='decimal(19,4)', nullable=False, chn_name='现钞买入价(人民币元/100外币)')
    """现钞买入价(人民币元/100外币):"""

    AskedPriceSpot: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='ED_BOCForexQuote', column_name='AskedPriceSpot', column_type='decimal(19,4)', nullable=False, chn_name='卖出价(人民币元/100外币)')
    """卖出价(人民币元/100外币):"""

    BenchMarkPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='ED_BOCForexQuote', column_name='BenchMarkPrice', column_type='decimal(19,4)', nullable=False, chn_name='基准价(人民币元/100外币)')
    """基准价(人民币元/100外币):"""

