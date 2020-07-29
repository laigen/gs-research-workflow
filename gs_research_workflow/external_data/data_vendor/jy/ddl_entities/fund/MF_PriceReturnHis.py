# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_PriceReturnHis(SQLTableEntity):
    name: str = 'MF_PriceReturnHis'
    
    chn_name: str = '公募基金复权价格回报历史表现'
    
    business_unique: str = 'InnerCode,TradingDay'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.本表记录展示在交易所交易的封闭式基金、LOF等基金复权价格回报的最新表现，包括周、一个月、三个月、半年、一年、二年、三年、五年、十年、成立以来的回报。
2.历史数据：1998年3月起-至今。
3.信息来源：聚源计算而得。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PriceReturnHis', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    RRInThreeMonth: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PriceReturnHis', column_name='RRInThreeMonth', column_type='decimal(18,4)', nullable=False, chn_name='三个月回报率(%)')
    """三个月回报率(%):"""

    RRInSixMonth: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PriceReturnHis', column_name='RRInSixMonth', column_type='decimal(18,4)', nullable=False, chn_name='六个月回报率(%)')
    """六个月回报率(%):"""

    RRSinceThisYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PriceReturnHis', column_name='RRSinceThisYear', column_type='decimal(18,4)', nullable=False, chn_name='今年以来回报率(%)')
    """今年以来回报率(%):"""

    RRInSingleYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PriceReturnHis', column_name='RRInSingleYear', column_type='decimal(18,4)', nullable=False, chn_name='一年回报率(%)')
    """一年回报率(%):"""

    RRInTwoYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PriceReturnHis', column_name='RRInTwoYear', column_type='decimal(18,4)', nullable=False, chn_name='二年回报率(%)')
    """二年回报率(%):"""

    AnnualizedRRInTwoYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PriceReturnHis', column_name='AnnualizedRRInTwoYear', column_type='decimal(18,4)', nullable=False, chn_name='二年年化回报率(%)')
    """二年年化回报率(%):"""

    RRInThreeYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PriceReturnHis', column_name='RRInThreeYear', column_type='decimal(18,4)', nullable=False, chn_name='三年回报率(%)')
    """三年回报率(%):"""

    AnnualizedRRInThreeYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PriceReturnHis', column_name='AnnualizedRRInThreeYear', column_type='decimal(18,4)', nullable=False, chn_name='三年年化回报率(%)')
    """三年年化回报率(%):"""

    RRInFiveYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PriceReturnHis', column_name='RRInFiveYear', column_type='decimal(18,4)', nullable=False, chn_name='五年回报率(%)')
    """五年回报率(%):"""

    AnnualizedRRInFiveYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PriceReturnHis', column_name='AnnualizedRRInFiveYear', column_type='decimal(18,4)', nullable=False, chn_name='五年年化回报率(%)')
    """五年年化回报率(%):"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PriceReturnHis', column_name='InnerCode', column_type='int', nullable=True, chn_name='基金内部编码')
    """基金内部编码:基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    RRInTenYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PriceReturnHis', column_name='RRInTenYear', column_type='decimal(18,4)', nullable=False, chn_name='十年回报率(%)')
    """十年回报率(%):"""

    AnnualizedRRInTenYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PriceReturnHis', column_name='AnnualizedRRInTenYear', column_type='decimal(18,4)', nullable=False, chn_name='十年年化回报率(%)')
    """十年年化回报率(%):"""

    RRSinceStart: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PriceReturnHis', column_name='RRSinceStart', column_type='decimal(18,4)', nullable=False, chn_name='设立以来回报率(%)')
    """设立以来回报率(%):"""

    AnnualizedRRSinceStart: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PriceReturnHis', column_name='AnnualizedRRSinceStart', column_type='decimal(18,4)', nullable=False, chn_name='设立以来年化回报率(%)')
    """设立以来年化回报率(%):"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PriceReturnHis', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PriceReturnHis', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    TradingDay: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PriceReturnHis', column_name='TradingDay', column_type='datetime', nullable=True, chn_name='交易日')
    """交易日:"""

    ClosePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PriceReturnHis', column_name='ClosePrice', column_type='decimal(18,4)', nullable=False, chn_name='收盘价(后复权)')
    """收盘价(后复权):"""

    ValueDailyGrowthRate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PriceReturnHis', column_name='ValueDailyGrowthRate', column_type='decimal(18,4)', nullable=False, chn_name='日回报率(%)')
    """日回报率(%):日回报率=（最新基金复权价格/上一个交易日的基金复权价格-1）*100。"""

    RRInSelectedWeek: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PriceReturnHis', column_name='RRInSelectedWeek', column_type='decimal(18,4)', nullable=False, chn_name='本周以来回报率(%)')
    """本周以来回报率(%):"""

    RRInSingleWeek: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PriceReturnHis', column_name='RRInSingleWeek', column_type='decimal(18,4)', nullable=False, chn_name='一周回报率(%)')
    """一周回报率(%):"""

    RRInSelectedMonth: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PriceReturnHis', column_name='RRInSelectedMonth', column_type='decimal(18,4)', nullable=False, chn_name='本月以来回报率(%)')
    """本月以来回报率(%):"""

    RRInSingleMonth: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PriceReturnHis', column_name='RRInSingleMonth', column_type='decimal(18,4)', nullable=False, chn_name='一个月回报率(%)')
    """一个月回报率(%):"""

