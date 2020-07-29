# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class Fut_TradingQuote(SQLTableEntity):
    name: str = 'Fut_TradingQuote'
    
    chn_name: str = '金融期货每日行情'
    
    business_unique: str = 'ContractInnerCode,TradingDay'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.收录股指期货、国债期货的日行情数据。包括高开低收、涨跌幅、持仓量、成交量、成交额、持仓量变化和基差等指标。
2.数据范围：2010-04-16——至今。
3.信息来源：中国金融期货交易所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_TradingQuote', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    OpenPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_TradingQuote', column_name='OpenPrice', column_type='decimal(19,4)', nullable=False, chn_name='开盘价')
    """开盘价:"""

    HighPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_TradingQuote', column_name='HighPrice', column_type='decimal(19,4)', nullable=False, chn_name='最高价')
    """最高价:"""

    LowPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_TradingQuote', column_name='LowPrice', column_type='decimal(19,4)', nullable=False, chn_name='最低价')
    """最低价:"""

    ClosePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_TradingQuote', column_name='ClosePrice', column_type='decimal(19,4)', nullable=False, chn_name='收盘价')
    """收盘价:"""

    ChangeOfCTPS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_TradingQuote', column_name='ChangeOfCTPS', column_type='decimal(19,4)', nullable=False, chn_name='收盘较前结算涨跌')
    """收盘较前结算涨跌:"""

    ChangePCTCTPS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_TradingQuote', column_name='ChangePCTCTPS', column_type='decimal(18,10)', nullable=False, chn_name='收盘较前结算涨跌幅(%)')
    """收盘较前结算涨跌幅(%):"""

    ChangeOfClosePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_TradingQuote', column_name='ChangeOfClosePrice', column_type='decimal(19,4)', nullable=False, chn_name='收盘价涨跌')
    """收盘价涨跌:"""

    ChangePCTClosePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_TradingQuote', column_name='ChangePCTClosePrice', column_type='decimal(18,10)', nullable=False, chn_name='收盘价涨跌幅(%)')
    """收盘价涨跌幅(%):"""

    SettlePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_TradingQuote', column_name='SettlePrice', column_type='decimal(19,4)', nullable=False, chn_name='结算价')
    """结算价:"""

    ChangeOfSettPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_TradingQuote', column_name='ChangeOfSettPrice', column_type='decimal(19,4)', nullable=False, chn_name='结算价涨跌')
    """结算价涨跌:"""

    ContractInnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_TradingQuote', column_name='ContractInnerCode', column_type='int', nullable=True, chn_name='合约内部编码')
    """合约内部编码:合约内部编码（ContractInnerCode）：与“期货合约主表（Fut_ContractMain）”中的“合约内部编码（ContractInnerCode）”关联，得到该期货合约的基础信息。"""

    ChangePCTSettPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_TradingQuote', column_name='ChangePCTSettPrice', column_type='decimal(18,10)', nullable=False, chn_name='结算价涨跌幅(%)')
    """结算价涨跌幅(%):"""

    OpenInterest: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_TradingQuote', column_name='OpenInterest', column_type='decimal(18,4)', nullable=False, chn_name='持仓量(手)')
    """持仓量(手):"""

    ChangeOfOpenInterest: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_TradingQuote', column_name='ChangeOfOpenInterest', column_type='decimal(18,4)', nullable=False, chn_name='持仓量变化(手)')
    """持仓量变化(手):"""

    ChangePCTOpenInterest: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_TradingQuote', column_name='ChangePCTOpenInterest', column_type='decimal(18,10)', nullable=False, chn_name='持仓量变化幅度(%)')
    """持仓量变化幅度(%):"""

    TurnoverVolume: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_TradingQuote', column_name='TurnoverVolume', column_type='decimal(18,4)', nullable=False, chn_name='成交量(手)')
    """成交量(手):"""

    ChangeOfTurnoverVolume: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_TradingQuote', column_name='ChangeOfTurnoverVolume', column_type='decimal(18,4)', nullable=False, chn_name='成交量变化(手)')
    """成交量变化(手):"""

    ChangePCTTurnoverVolume: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_TradingQuote', column_name='ChangePCTTurnoverVolume', column_type='decimal(18,10)', nullable=False, chn_name='成交量变化幅度(%)')
    """成交量变化幅度(%):"""

    TurnoverValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_TradingQuote', column_name='TurnoverValue', column_type='decimal(19,4)', nullable=False, chn_name='成交金额(元)')
    """成交金额(元):"""

    ChangeOfTurnoverValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_TradingQuote', column_name='ChangeOfTurnoverValue', column_type='decimal(19,4)', nullable=False, chn_name='成交金额变化(元)')
    """成交金额变化(元):"""

    ChangePCTTurnoverValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_TradingQuote', column_name='ChangePCTTurnoverValue', column_type='decimal(18,10)', nullable=False, chn_name='成交金额变化幅度(%)')
    """成交金额变化幅度(%):"""

    TradingDay: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_TradingQuote', column_name='TradingDay', column_type='datetime', nullable=True, chn_name='交易日期')
    """交易日期:"""

    BasisValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_TradingQuote', column_name='BasisValue', column_type='decimal(18,4)', nullable=False, chn_name='基差')
    """基差:基差（BasisValue）：当“合约类型”为股指期货，基差=期货市场收盘价-现货市场收盘价"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_TradingQuote', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_TradingQuote', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    ContractCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_TradingQuote', column_name='ContractCode', column_type='varchar(100)', nullable=False, chn_name='合约代码')
    """合约代码:"""

    ExchangeCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_TradingQuote', column_name='ExchangeCode', column_type='int', nullable=False, chn_name='交易所代码')
    """交易所代码:交易所代码(ExchangeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1324 AND DM = 20，得到交易所代码的具体描述：20-中国金融期货交易所。"""

    OptionCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_TradingQuote', column_name='OptionCode', column_type='int', nullable=False, chn_name='合约标的')
    """合约标的:当合约标的(OptionCode) in（46,3145,4978）时，与证券主表（ SecuMain）的证券内部编码（InnerCode）字段关联，得到合约标的的具体描述：46-上证50指数，3145-沪深300指数，4978-中证500指数；当合约标的(OptionCode) in（501,502）时与产品表(CT_Product)中的产品代码（Prod..."""

    SeriesFlag: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_TradingQuote', column_name='SeriesFlag', column_type='int', nullable=False, chn_name='合约序列标志')
    """合约序列标志:合约序列标志（SeriesFlag），该字段固定以下常量：1-当月合约；2-下月合约；3-隔季合约；4-下季合约"""

    PrevSettlePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_TradingQuote', column_name='PrevSettlePrice', column_type='decimal(19,4)', nullable=False, chn_name='前结算')
    """前结算:"""

    PrevClosePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_TradingQuote', column_name='PrevClosePrice', column_type='decimal(19,4)', nullable=False, chn_name='前收盘')
    """前收盘:"""

