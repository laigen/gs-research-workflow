# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class Fut_ContractMain(SQLTableEntity):
    name: str = 'Fut_ContractMain'
    
    chn_name: str = '期货合约'
    
    business_unique: str = 'ContractInnerCode'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.收录国内外商品期货、货币期货、利率期货、股指期货和虚拟货币期货5大合约类型期货合约的基本信息，包括合约代码、合约简称、合约类型、合约标的、合约状态等指标信息。
2.信息来源：各大期货交易所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    CMValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='CMValue', column_type='int', nullable=False, chn_name='合约乘数(数值)')
    """合约乘数(数值):合约乘数数值：当合约类型为股指期货时，指一指数点的价值。当合约类型为商品期货时，指一手合约的价值。"""

    ContractMultiplier: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='ContractMultiplier', column_type='varchar(50)', nullable=False, chn_name='交易单位/合约乘数')
    """交易单位/合约乘数:"""

    PriceUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='PriceUnit', column_type='varchar(50)', nullable=False, chn_name='报价单位')
    """报价单位:"""

    LittlestChangeUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='LittlestChangeUnit', column_type='varchar(50)', nullable=False, chn_name='最小变动价位')
    """最小变动价位:"""

    ChangePCTLimit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='ChangePCTLimit', column_type='varchar(200)', nullable=False, chn_name='每日涨跌幅度')
    """每日涨跌幅度:"""

    CurrencyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='CurrencyCode', column_type='int', nullable=False, chn_name='货币单位')
    """货币单位:货币单位(CurrencyCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1068，得到货币单位的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，1170-约旦第纳尔，1180-科..."""

    DeliveryYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='DeliveryYear', column_type='varchar(4)', nullable=False, chn_name='交割年')
    """交割年:"""

    DeliveryMonth: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='DeliveryMonth', column_type='varchar(2)', nullable=False, chn_name='交割月')
    """交割月:"""

    EffectiveDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='EffectiveDate', column_type='datetime', nullable=False, chn_name='生效日期')
    """生效日期:"""

    LastTradingDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='LastTradingDate', column_type='datetime', nullable=False, chn_name='最后交易日')
    """最后交易日:"""

    ContractInnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='ContractInnerCode', column_type='int', nullable=True, chn_name='合约内部编码')
    """合约内部编码:"""

    DeliveryDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='DeliveryDate', column_type='datetime', nullable=False, chn_name='交割日期')
    """交割日期:"""

    LastDeliveryDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='LastDeliveryDate', column_type='datetime', nullable=False, chn_name='最后交割日期')
    """最后交割日期:"""

    DeliveryMethod: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='DeliveryMethod', column_type='int', nullable=False, chn_name='交割方式')
    """交割方式:交割方式(DeliveryMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1462，得到交割方式的具体描述：1-实物交割，2-现金结算。"""

    DeliveryGrades: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='DeliveryGrades', column_type='text', nullable=False, chn_name='交割等级')
    """交割等级:"""

    MinMarginRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='MinMarginRatio', column_type='decimal(9,6)', nullable=False, chn_name='最低交易保证金率(%)')
    """最低交易保证金率(%):"""

    TradingCommission: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='TradingCommission', column_type='varchar(100)', nullable=False, chn_name='交易手续费')
    """交易手续费:"""

    DeliveryCommission: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='DeliveryCommission', column_type='varchar(100)', nullable=False, chn_name='交割手续费')
    """交割手续费:"""

    SettPriceCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='SettPriceCode', column_type='int', nullable=False, chn_name='结算价计算方式分类代码')
    """结算价计算方式分类代码:"""

    SettPriceDesc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='SettPriceDesc', column_type='text', nullable=False, chn_name='结算价计算方式')
    """结算价计算方式:"""

    DeliSettPriceCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='DeliSettPriceCode', column_type='int', nullable=False, chn_name='交割结算价计算方式分类代码')
    """交割结算价计算方式分类代码:"""

    ContractCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='ContractCode', column_type='varchar(10)', nullable=True, chn_name='合约代码')
    """合约代码:"""

    DeliSettPriceDesc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='DeliSettPriceDesc', column_type='text', nullable=False, chn_name='交割结算价计算方式')
    """交割结算价计算方式:"""

    ListBasisPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='ListBasisPrice', column_type='decimal(19,4)', nullable=False, chn_name='挂牌基准价')
    """挂牌基准价:"""

    ChangePCTListPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='ChangePCTListPrice', column_type='decimal(18,10)', nullable=False, chn_name='挂牌价涨跌幅(%)')
    """挂牌价涨跌幅(%):"""

    ContractState: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='ContractState', column_type='int', nullable=False, chn_name='合约状态')
    """合约状态:合约状态(ContractState)与(CT_SystemConst)表中的DM字段关联，令LB = 1176 AND DM IN (1,5,9)，得到合约状态的具体描述：1-上市，5-终止，9-其他。"""

    ChangeReason: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='ChangeReason', column_type='varchar(200)', nullable=False, chn_name='变动原因')
    """变动原因:"""

    ContractMonth: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='ContractMonth', column_type='varchar(100)', nullable=False, chn_name='合约月份')
    """合约月份:"""

    ExchangeDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='ExchangeDate', column_type='varchar(200)', nullable=False, chn_name='交易时间')
    """交易时间:"""

    LastTradingDateDesc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='LastTradingDateDesc', column_type='varchar(100)', nullable=False, chn_name='最后交易日描述')
    """最后交易日描述:"""

    LastTradingTimeDesc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='LastTradingTimeDesc', column_type='varchar(100)', nullable=False, chn_name='最后交易日交易时间描述')
    """最后交易日交易时间描述:"""

    DeliveryDateDesc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='DeliveryDateDesc', column_type='varchar(100)', nullable=False, chn_name='交割日期描述')
    """交割日期描述:"""

    ContractAbbr: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='ContractAbbr', column_type='varchar(50)', nullable=False, chn_name='合约简称')
    """合约简称:"""

    LastDeliveryDateDesc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='LastDeliveryDateDesc', column_type='varchar(100)', nullable=False, chn_name='最后交割日日期描述')
    """最后交割日日期描述:"""

    ContractIntroduction: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='ContractIntroduction', column_type='text', nullable=False, chn_name='合约简介')
    """合约简介:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    ContractName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='ContractName', column_type='varchar(100)', nullable=False, chn_name='合约全称')
    """合约全称:"""

    ExchangeCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='ExchangeCode', column_type='int', nullable=True, chn_name='交易所代码')
    """交易所代码:交易所代码(ExchangeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1324，得到交易所代码的具体描述：10-上海期货交易所，11-上海国际能源交易中心，12-中国银行间外汇市场，13-大连商品交易所，14-上海黄金交易所，15-郑州商品交易所，19-全国期货市场，20-中国金融期货交易所，31-台湾期货交易所，32-香港..."""

    ContractType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='ContractType', column_type='int', nullable=False, chn_name='合约类型')
    """合约类型:合约类型(ContractType)与(CT_SystemConst)表中的DM字段关联，令LB = 1461，得到合约类型的具体描述：1-商品期货，2-货币期货，3-利率期货，4-股指期货，5-虚拟货币期货。"""

    OptionCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='OptionCode', column_type='int', nullable=True, chn_name='合约标的')
    """合约标的:合约标的(OptionCode)与(CT_Product)表中的ProductCode字段关联，令ProductCategory = 326，得到合约标的的具体描述：46-上证50指数，305-铜，306-锡，307-铅，310-铝，311-镍，312-锌，313-黄金，314-白银，315-天然橡胶，316-SCE橡胶，317-布伦特原油，318-轻质原油..."""

    IfReal: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ContractMain', column_name='IfReal', column_type='int', nullable=False, chn_name='是否真实')
    """是否真实:是否真实(IfReal)：与“系统常量表(CT_SystemConst)”中的“代码(DM)”关联，令“LB=999”，得到该期货合约是否为真实合约。1-是，真实合约；2-否，虚拟合约"""

