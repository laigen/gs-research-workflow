# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class Fut_WRStatByOption(SQLTableEntity):
    name: str = 'Fut_WRStatByOption'
    
    chn_name: str = '期货仓单统计_按品种'
    
    business_unique: str = 'EndDate,ExchangeCode,ReportPeriod,OptionCode'
    
    refresh_freq: str = """日更新和周更新"""
    
    comment: str = """1.1.收录上海期货交易所、上海国际能源交易中心、大连商品交易所、郑州商品交易所公布的以品种为维度的日度仓单数据和上海期货交易所公布的以品种为维度的周度库存数据。
2.数据范围：2005-04-22——至今。
3.信息来源：上海期货交易所、上海国际能源交易中心、大连商品交易所和郑州商品交易所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_WRStatByOption', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    WRQIncrease: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_WRStatByOption', column_name='WRQIncrease', column_type='decimal(18,4)', nullable=False, chn_name='仓单增加量')
    """仓单增加量:"""

    WRQWriteOff: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_WRStatByOption', column_name='WRQWriteOff', column_type='decimal(18,4)', nullable=False, chn_name='仓单注销量')
    """仓单注销量:"""

    WRQCurrent: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_WRStatByOption', column_name='WRQCurrent', column_type='decimal(18,4)', nullable=False, chn_name='本期仓单量')
    """本期仓单量:"""

    WRQPrediction: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_WRStatByOption', column_name='WRQPrediction', column_type='decimal(18,4)', nullable=False, chn_name='有效预报量')
    """有效预报量:"""

    StockPrior: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_WRStatByOption', column_name='StockPrior', column_type='decimal(18,4)', nullable=False, chn_name='上期库存小计')
    """上期库存小计:"""

    StockCurrent: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_WRStatByOption', column_name='StockCurrent', column_type='decimal(18,4)', nullable=False, chn_name='本期库存小计')
    """本期库存小计:"""

    AvailableStockPrior: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_WRStatByOption', column_name='AvailableStockPrior', column_type='decimal(18,4)', nullable=False, chn_name='上期可用库容量')
    """上期可用库容量:"""

    AvailableStockCurrent: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_WRStatByOption', column_name='AvailableStockCurrent', column_type='decimal(18,4)', nullable=False, chn_name='本期可用库容量')
    """本期可用库容量:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_WRStatByOption', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_WRStatByOption', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_WRStatByOption', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    ExchangeCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_WRStatByOption', column_name='ExchangeCode', column_type='int', nullable=True, chn_name='交易所')
    """交易所:交易所代码（ExchangeCode）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令“LB=1324”，得到具体交易所名称。10-上海期货交易所，11-上海国际能源交易中心，13-大连商品交易所，15-郑州商品交易所。"""

    ReportPeriod: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_WRStatByOption', column_name='ReportPeriod', column_type='int', nullable=True, chn_name='数据统计期间')
    """数据统计期间:数据统计期间(ReportPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 1074 AND DM IN (5,6)，得到数据统计期间的具体描述：5-日，6-周。"""

    OptionCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_WRStatByOption', column_name='OptionCode', column_type='int', nullable=True, chn_name='品种代码')
    """品种代码:品种代码(OptionCode)与(CT_Product)表中的ProductCode字段关联，令ProductCategory = 326，得到品种代码的具体描述：46-上证50指数，305-铜，306-锡，307-铅，310-铝，311-镍，312-锌，313-黄金，314-白银，315-天然橡胶，316-SCE橡胶，317-布伦特原油，318-轻质原油..."""

    OptionName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_WRStatByOption', column_name='OptionName', column_type='varchar(20)', nullable=False, chn_name='品种名称')
    """品种名称:"""

    UnitCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_WRStatByOption', column_name='UnitCode', column_type='int', nullable=False, chn_name='单位代码')
    """单位代码:单位代码(UnitCode)与(CT_SystemConst)表中的DM字段关联,令LB=102  AND DM IN (8,12,24,31,33)，得到单位代码的具体描述：8-千克，12-吨，24-张，31-手，33-手。"""

    UnitName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_WRStatByOption', column_name='UnitName', column_type='varchar(20)', nullable=False, chn_name='单位名称')
    """单位名称:"""

    WRQPrior: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_WRStatByOption', column_name='WRQPrior', column_type='decimal(18,4)', nullable=False, chn_name='上期仓单量')
    """上期仓单量:"""

