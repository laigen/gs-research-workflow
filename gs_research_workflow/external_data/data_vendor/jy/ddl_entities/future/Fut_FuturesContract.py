# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class Fut_FuturesContract(SQLTableEntity):
    name: str = 'Fut_FuturesContract'
    
    chn_name: str = '期货品种'
    
    business_unique: str = 'ContractName,ContractOption,Exchange'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.收录国内外商品期货、货币期货、利率期货、股指期货和虚拟货币期货5大合约类型期货标准合约的基本信息。包括品种名称、交易标的、交易所、合约类型、交易时间、交割日期、交割等级等指标信息。
2.信息来源：各大商品期货交易所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FuturesContract', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    LittlestChangeUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FuturesContract', column_name='LittlestChangeUnit', column_type='varchar(50)', nullable=False, chn_name='最小变动价位')
    """最小变动价位:"""

    ChangePCTLim: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FuturesContract', column_name='ChangePCTLim', column_type='varchar(200)', nullable=False, chn_name='每日涨跌幅度')
    """每日涨跌幅度:"""

    ContractMonth: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FuturesContract', column_name='ContractMonth', column_type='varchar(100)', nullable=False, chn_name='合约月份')
    """合约月份:"""

    ExchangeDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FuturesContract', column_name='ExchangeDate', column_type='varchar(200)', nullable=False, chn_name='交易时间')
    """交易时间:"""

    NightTradingTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FuturesContract', column_name='NightTradingTime', column_type='varchar(200)', nullable=False, chn_name='夜盘交易时间(描述)')
    """夜盘交易时间(描述):"""

    LastTradingDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FuturesContract', column_name='LastTradingDate', column_type='varchar(100)', nullable=False, chn_name='最后交易日')
    """最后交易日:"""

    LastTradingTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FuturesContract', column_name='LastTradingTime', column_type='varchar(100)', nullable=False, chn_name='最后交易日交易时间')
    """最后交易日交易时间:针对国内交易所交易品种。"""

    DeliveryDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FuturesContract', column_name='DeliveryDate', column_type='varchar(100)', nullable=False, chn_name='交割日期')
    """交割日期:"""

    LastDeliveryDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FuturesContract', column_name='LastDeliveryDate', column_type='varchar(100)', nullable=False, chn_name='最后交割日')
    """最后交割日:"""

    DeliverableGrades: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FuturesContract', column_name='DeliverableGrades', column_type='text', nullable=False, chn_name='交割等级')
    """交割等级:"""

    ContractInnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FuturesContract', column_name='ContractInnerCode', column_type='int', nullable=True, chn_name='品种内部编码')
    """品种内部编码:"""

    MaintainRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FuturesContract', column_name='MaintainRatio', column_type='decimal(18,8)', nullable=False, chn_name='合约交易保证金率')
    """合约交易保证金率:"""

    Fee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FuturesContract', column_name='Fee', column_type='varchar(100)', nullable=False, chn_name='交易手续费')
    """交易手续费:"""

    SettlementPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FuturesContract', column_name='SettlementPrice', column_type='text', nullable=False, chn_name='结算价及计算方式')
    """结算价及计算方式:"""

    FinalSettlementPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FuturesContract', column_name='FinalSettlementPrice', column_type='text', nullable=False, chn_name='交割结算价及计算方式')
    """交割结算价及计算方式:"""

    DeliveryMethod: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FuturesContract', column_name='DeliveryMethod', column_type='int', nullable=False, chn_name='交割方式')
    """交割方式:交割方式(DeliveryMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1462，得到交割方式的具体描述：1-实物交割，2-现金结算。"""

    ContractIntroduction: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FuturesContract', column_name='ContractIntroduction', column_type='text', nullable=False, chn_name='合约简介')
    """合约简介:"""

    ContractState: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FuturesContract', column_name='ContractState', column_type='int', nullable=False, chn_name='品种状态')
    """品种状态:品种状态(ContractState)与(CT_SystemConst)表中的DM字段关联，令LB = 1176 AND DM IN (1,5,9)，得到合约状态的具体描述：1-上市，5-终止，9-其他。"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FuturesContract', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FuturesContract', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    ContractName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FuturesContract', column_name='ContractName', column_type='varchar(100)', nullable=True, chn_name='品种名称')
    """品种名称:"""

    ContractOption: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FuturesContract', column_name='ContractOption', column_type='int', nullable=True, chn_name='交易标的')
    """交易标的:交易标的（ContractOption）：与“产品表（CT_Product）”中的“产品代码（ProductCode）”关联，令“ProductCategory （产品分类）＝326”，得到合约的标的名称:305-铜，306-锡，307-铅，310-铝，311-镍，312-锌，313-黄金，314-白银，315-天然橡胶，317-布伦特原油，318-轻质原油..."""

    Exchange: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FuturesContract', column_name='Exchange', column_type='int', nullable=True, chn_name='交易所')
    """交易所:交易所(Exchange)与(CT_SystemConst)表中的DM字段关联，令LB=1324，得到交易所的具体描述：10-上海期货交易所，11-上海国际能源交易中心，12-中国银行间外汇市场，13-大连商品交易所，14-上海黄金交易所，15-郑州商品交易所，19-全国期货市场，20-中国金融期货交易所，31-台湾期货交易所，32-香港期货交易所，33-新..."""

    TradingCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FuturesContract', column_name='TradingCode', column_type='varchar(10)', nullable=False, chn_name='交易代码')
    """交易代码:"""

    ContractType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FuturesContract', column_name='ContractType', column_type='int', nullable=False, chn_name='合约类型')
    """合约类型:合约类型（ContractType）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令“LB=1461”，得到合约的类型描述。1-商品期货，2-货币期货，3-利率期货，4-股指期货，5-虚拟货币期货。"""

    ContractMulti: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FuturesContract', column_name='ContractMulti', column_type='varchar(50)', nullable=False, chn_name='交易单位/合约乘数')
    """交易单位/合约乘数:"""

    PriceUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FuturesContract', column_name='PriceUnit', column_type='varchar(50)', nullable=False, chn_name='报价单位')
    """报价单位:"""

