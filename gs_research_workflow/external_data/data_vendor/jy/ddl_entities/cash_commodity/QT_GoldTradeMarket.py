# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class QT_GoldTradeMarket(SQLTableEntity):
    name: str = 'QT_GoldTradeMarket'
    
    chn_name: str = '上海黄金交易所交易行情'
    
    business_unique: str = 'TradeDate,DateType,TradeVariety'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.收录上海黄金交易所下黄金、白银、铂等金属标准化交易的每日盘后行情，包括开盘价、收盘价、最高价、最低价、成交量、成交额等信息
2.数据范围：2002年10月-至今
3.数据源：上海黄金交易所"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_GoldTradeMarket', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    LowPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_GoldTradeMarket', column_name='LowPrice', column_type='decimal(18,4)', nullable=False, chn_name='最低价(元/克)')
    """最低价(元/克):"""

    Change: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_GoldTradeMarket', column_name='Change', column_type='decimal(18,4)', nullable=False, chn_name='涨跌(元/克)')
    """涨跌(元/克):"""

    ChangePCT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_GoldTradeMarket', column_name='ChangePCT', column_type='decimal(18,4)', nullable=False, chn_name='涨跌幅')
    """涨跌幅:"""

    PriceWeighted: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_GoldTradeMarket', column_name='PriceWeighted', column_type='decimal(18,4)', nullable=False, chn_name='加权价(元/克)')
    """加权价(元/克):"""

    TurnVol: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_GoldTradeMarket', column_name='TurnVol', column_type='decimal(18,4)', nullable=False, chn_name='成交量(千克)')
    """成交量(千克):"""

    TurnValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_GoldTradeMarket', column_name='TurnValue', column_type='decimal(18,4)', nullable=False, chn_name='成交金额(元)')
    """成交金额(元):"""

    OpenInterest: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_GoldTradeMarket', column_name='OpenInterest', column_type='decimal(18,4)', nullable=False, chn_name='持仓量')
    """持仓量:"""

    SettlementVol: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_GoldTradeMarket', column_name='SettlementVol', column_type='decimal(18,4)', nullable=False, chn_name='交收量')
    """交收量:"""

    SettleDirection: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_GoldTradeMarket', column_name='SettleDirection', column_type='varchar(20)', nullable=False, chn_name='交收方向')
    """交收方向:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_GoldTradeMarket', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    TradeDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_GoldTradeMarket', column_name='TradeDate', column_type='datetime', nullable=False, chn_name='交易日期')
    """交易日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_GoldTradeMarket', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_GoldTradeMarket', column_name='InfoSource', column_type='varchar(100)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    DateType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_GoldTradeMarket', column_name='DateType', column_type='int', nullable=True, chn_name='日期类别')
    """日期类别:日期类别(DateType)与(CT_SystemConst)表中的DM字段关联，令LB = 1083 AND DM IN (3)，得到日期类别的具体描述：3-日。"""

    TradeVariety: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_GoldTradeMarket', column_name='TradeVariety', column_type='int', nullable=True, chn_name='交易品种')
    """交易品种:交易品种(TradeVariety)与(CT_SystemConst)表中的DM字段关联，令LB = 1135，得到交易品种的具体描述：1-Au50g，2-Au99.95，3-Au99.99，4-Au(T+5)，5-Au(T+D)，6-Pt99.95，7-Ag(T+D)，8-Ag99.9，9-Ag50g，10-Au100g，11-Au(T+N1)，12-Au..."""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_GoldTradeMarket', column_name='InnerCode', column_type='int', nullable=False, chn_name='内码编码')
    """内码编码:内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到现货的交易代码、交易简称等。"""

    OpenPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_GoldTradeMarket', column_name='OpenPrice', column_type='decimal(18,4)', nullable=False, chn_name='开盘价(元/克)')
    """开盘价(元/克):"""

    ClosePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_GoldTradeMarket', column_name='ClosePrice', column_type='decimal(18,4)', nullable=False, chn_name='收盘价(元/克)')
    """收盘价(元/克):"""

    HighPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_GoldTradeMarket', column_name='HighPrice', column_type='decimal(18,4)', nullable=False, chn_name='最高价(元/克)')
    """最高价(元/克):"""

