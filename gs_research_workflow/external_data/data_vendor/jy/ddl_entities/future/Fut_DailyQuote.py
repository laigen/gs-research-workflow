# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class Fut_DailyQuote(SQLTableEntity):
    name: str = 'Fut_DailyQuote'
    
    chn_name: str = '商品期货每日行情'
    
    business_unique: str = 'EndDate,ReportPeriod,ReportArea,AdjustMark,Exchange,ContractName,OptionCode,Term'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.收录国内外各大交易所的商品期货的日收盘行情以及沪深300指数期货仿真行情，包括高开低收、成交量、持仓量、成交额等指标。其中：统计类别为交易所品种合约。
2.数据范围：1981-11-17——至今
3.信息来源：上海期货交易所、大连商品交易所、郑州商品交易所等。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_DailyQuote', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    Term: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_DailyQuote', column_name='Term', column_type='varchar(100)', nullable=False, chn_name='期限描述')
    """期限描述:"""

    SettlementYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_DailyQuote', column_name='SettlementYear', column_type='varchar(4)', nullable=False, chn_name='交割年')
    """交割年:"""

    SettlementMonth: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_DailyQuote', column_name='SettlementMonth', column_type='varchar(2)', nullable=False, chn_name='交割月')
    """交割月:"""

    SettlementDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_DailyQuote', column_name='SettlementDate', column_type='datetime', nullable=False, chn_name='交割日期')
    """交割日期:从2018-02-01日起该字段不再维护，请使用期货合约（Fut_ContractMain）表中的交割日期（DeliveryDate）字段。"""

    Code: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_DailyQuote', column_name='Code', column_type='int', nullable=False, chn_name='编码')
    """编码:"""

    ContinuumMark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_DailyQuote', column_name='ContinuumMark', column_type='int', nullable=False, chn_name='连续标志')
    """连续标志:连续标志（ContinuumMark），该字段固定以下常量：1-是"""

    MainContractMark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_DailyQuote', column_name='MainContractMark', column_type='int', nullable=False, chn_name='主力标志')
    """主力标志:主力标志，该字段固定以下常量：1-是。同一交易日期，同一交易所，同一品种，优先选取持仓量最大的合约为主力标志；如果持仓量存在相等的情况，则选择成交量最大的合约为主力标志；如果成交量也存在相等的情况，再选择交割时间离当下最近的合约为主力标志。"""

    PrevSettlePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_DailyQuote', column_name='PrevSettlePrice', column_type='decimal(19,4)', nullable=False, chn_name='前结算(元/吨)')
    """前结算(元/吨):"""

    OpenPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_DailyQuote', column_name='OpenPrice', column_type='decimal(19,4)', nullable=False, chn_name='开盘价(元/吨)')
    """开盘价(元/吨):"""

    HighPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_DailyQuote', column_name='HighPrice', column_type='decimal(19,4)', nullable=False, chn_name='最高价(元/吨)')
    """最高价(元/吨):"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_DailyQuote', column_name='InnerCode', column_type='int', nullable=False, chn_name='合约内部编码')
    """合约内部编码:合约内部编码（InnerCode）：与“期货合约主表（Fut_ContractMain）”中的“合约内部编码（ContractInnerCode）”关联，得到该期货合约的基础信息。"""

    LowPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_DailyQuote', column_name='LowPrice', column_type='decimal(19,4)', nullable=False, chn_name='最低价(元/吨)')
    """最低价(元/吨):"""

    ClosePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_DailyQuote', column_name='ClosePrice', column_type='decimal(19,4)', nullable=False, chn_name='收盘价(元/吨)')
    """收盘价(元/吨):"""

    SettlePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_DailyQuote', column_name='SettlePrice', column_type='decimal(19,4)', nullable=False, chn_name='结算价(元/吨)')
    """结算价(元/吨):"""

    Volume: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_DailyQuote', column_name='Volume', column_type='decimal(18,2)', nullable=False, chn_name='成交量(手)')
    """成交量(手):"""

    OpenInterest: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_DailyQuote', column_name='OpenInterest', column_type='decimal(18,2)', nullable=False, chn_name='持仓量(手)')
    """持仓量(手):"""

    OpenInterestChange: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_DailyQuote', column_name='OpenInterestChange', column_type='decimal(18,2)', nullable=False, chn_name='持仓量变化(手)')
    """持仓量变化(手):"""

    Turnover: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_DailyQuote', column_name='Turnover', column_type='decimal(19,4)', nullable=False, chn_name='成交额(元)')
    """成交额(元):"""

    Notes: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_DailyQuote', column_name='Notes', column_type='varchar(500)', nullable=False, chn_name='备注说明')
    """备注说明:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_DailyQuote', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_DailyQuote', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_DailyQuote', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    ReportPeriod: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_DailyQuote', column_name='ReportPeriod', column_type='int', nullable=True, chn_name='数据统计期间')
    """数据统计期间:数据统计期间(ReportPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 1074 AND DM IN (5)，得到数据统计期间的具体描述：5-日。"""

    ReportArea: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_DailyQuote', column_name='ReportArea', column_type='int', nullable=True, chn_name='统计区域类别')
    """统计区域类别:统计区域类别(ReportArea)与(CT_SystemConst)表中的DM字段关联，令LB = 1076 AND DM IN (6403)，得到统计区域类别的具体描述：6403-按交易所品种合约。"""

    AdjustMark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_DailyQuote', column_name='AdjustMark', column_type='int', nullable=False, chn_name='调整标志')
    """调整标志:调整标志(AdjustMark)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM IN (2)，得到调整标志的具体描述：2-否。"""

    Exchange: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_DailyQuote', column_name='Exchange', column_type='int', nullable=False, chn_name='交易所')
    """交易所:交易所(Exchange)与(CT_SystemConst)表中的DM字段关联，令LB = 1324，得到交易所的具体描述：10-上海期货交易所，11-上海国际能源交易中心，12-中国银行间外汇市场，13-大连商品交易所，14-上海黄金交易所，15-郑州商品交易所，19-全国期货市场，20-中国金融期货交易所，31-台湾期货交易所，32-香港期货交易所，33..."""

    ContractName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_DailyQuote', column_name='ContractName', column_type='varchar(100)', nullable=False, chn_name='合约名称')
    """合约名称:"""

    OptionCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_DailyQuote', column_name='OptionCode', column_type='int', nullable=False, chn_name='品种代码')
    """品种代码:品种代码(OptionCode)与(CT_Product)表中的ProductCode字段关联，令ProductCategory = 326，得到品种代码的具体描述：46-上证50指数，305-铜，306-锡，307-铅，310-铝，311-镍，312-锌，313-黄金，314-白银，315-天然橡胶，316-SCE橡胶，317-布伦特原油，318-轻质原油..."""

