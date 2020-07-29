# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_ShortST(SQLTableEntity):
    name: str = 'HK_ShortST'
    
    chn_name: str = '港股卖空数据'
    
    business_unique: str = 'InnerCode,TradingDay'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.港股卖空数量，卖空金额和变动数量数据。    
2.数据范围：2016-04 至今。
3.数据来源：港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShortST', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    Volume: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShortST', column_name='Volume', column_type='decimal(18,6)', nullable=False, chn_name='全天成交量(股)')
    """全天成交量(股):"""

    Turnover: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShortST', column_name='Turnover', column_type='decimal(19,4)', nullable=False, chn_name='全天成交额(元)')
    """全天成交额(元):"""

    AdjShortShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShortST', column_name='AdjShortShares', column_type='decimal(18,6)', nullable=False, chn_name='调整全天卖空数量(股)')
    """调整全天卖空数量(股):"""

    AdjShortAmt: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShortST', column_name='AdjShortAmt', column_type='decimal(19,4)', nullable=False, chn_name='调整全天卖空金额(元)')
    """调整全天卖空金额(元):"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShortST', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShortST', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShortST', column_name='InnerCode', column_type='int', nullable=True, chn_name='证券内部编码')
    """证券内部编码:证券内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。"""

    TradingDay: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShortST', column_name='TradingDay', column_type='datetime', nullable=True, chn_name='交易日')
    """交易日:"""

    Currency: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShortST', column_name='Currency', column_type='int', nullable=False, chn_name='货币')
    """货币:货币(Currency)与(CT_SystemConst)表中的DM字段关联，令LB=1068，得到货币的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，1170-约旦第纳尔，1180-科威特第纳尔，1190..."""

    IfDesShtSec: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShortST', column_name='IfDesShtSec', column_type='int', nullable=False, chn_name='是否指定卖空证券')
    """是否指定卖空证券:是否指定卖空证券(IfDesShtSec)与(CT_SystemConst)表中的DM字段关联，令LB=1906，得到是否指定卖空证券的具体描述：1-指定证券，2-非指定证券。"""

    ShortSharesAM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShortST', column_name='ShortSharesAM', column_type='decimal(18,6)', nullable=False, chn_name='上午卖空数量(股)')
    """上午卖空数量(股):"""

    ShortAmtAM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShortST', column_name='ShortAmtAM', column_type='decimal(19,4)', nullable=False, chn_name='上午卖空金额(元)')
    """上午卖空金额(元):"""

    ShortShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShortST', column_name='ShortShares', column_type='decimal(18,6)', nullable=False, chn_name='全天卖空数量(股)')
    """全天卖空数量(股):"""

    ShortAmt: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShortST', column_name='ShortAmt', column_type='decimal(19,4)', nullable=False, chn_name='全天卖空金额(元)')
    """全天卖空金额(元):"""

