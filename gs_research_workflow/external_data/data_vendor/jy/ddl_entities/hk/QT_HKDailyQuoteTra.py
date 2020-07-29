# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class QT_HKDailyQuoteTra(SQLTableEntity):
    name: str = 'QT_HKDailyQuoteTra'
    
    chn_name: str = '港股行情指标计算用表'
    
    business_unique: str = 'InnerCode,StatDate'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.记录港股最新计算会使用到的指标，主要用于常用估值指标的计算。包含字段有：已上市股数、最近一年年末净利润、年滚动净利润、最近一年年末基本每股收益增长率、最新报表净资产、最近一年主营业务收入、最近一年现金流量净额、上一财年股息总额、近12月股息总额等。
2.数据范围：2005年至今。
3.数据来源：港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteTra', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    NetProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteTra', column_name='NetProfit', column_type='decimal(19,4)', nullable=False, chn_name='最近一年年末净利润(元)')
    """最近一年年末净利润(元):"""

    RollingNetProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteTra', column_name='RollingNetProfit', column_type='decimal(19,4)', nullable=False, chn_name='年滚动净利润(元)')
    """年滚动净利润(元):"""

    EPSGrowthRate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteTra', column_name='EPSGrowthRate', column_type='decimal(19,4)', nullable=False, chn_name='最近一年年末基本每股收益增长率(%)')
    """最近一年年末基本每股收益增长率(%):"""

    NetAsset: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteTra', column_name='NetAsset', column_type='decimal(19,4)', nullable=False, chn_name='最新报表净资产(元)')
    """最新报表净资产(元):"""

    SalesRevenue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteTra', column_name='SalesRevenue', column_type='decimal(19,4)', nullable=False, chn_name='最近一年主营业务收入(元)')
    """最近一年主营业务收入(元):"""

    NetCashFlow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteTra', column_name='NetCashFlow', column_type='decimal(19,4)', nullable=False, chn_name='最近一年现金流量净额(元)')
    """最近一年现金流量净额(元):"""

    CurrencyUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteTra', column_name='CurrencyUnit', column_type='int', nullable=False, chn_name='货币单位')
    """货币单位:货币类别（CurrencyUnit）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令LB=“1068”，得到“货币单位”描述：1000-美元，1100-港元，1160-日本元，1320-新加坡元，1420-人民币元，3000-欧元，3030-英镑，5010-加拿大元，6010-澳大利亚元。"""

    TraCurrUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteTra', column_name='TraCurrUnit', column_type='int', nullable=False, chn_name='交易货币单位')
    """交易货币单位:交易货币类别（TraCurrUnit）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令LB=“1068”，得到“货币单位”描述：1000-美元，1100-港元，1160-日本元，1320-新加坡元，1420-人民币元，3000-欧元，3030-英镑，5010-加拿大元，6010-澳大利亚元。"""

    ToCashDivLFY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteTra', column_name='ToCashDivLFY', column_type='decimal(19,4)', nullable=False, chn_name='上一财年股息总额(港元)')
    """上一财年股息总额(港元):"""

    ToCashDivRW: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteTra', column_name='ToCashDivRW', column_type='decimal(19,4)', nullable=False, chn_name='近12月股息总额(港元)')
    """近12月股息总额(港元):"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteTra', column_name='InnerCode', column_type='int', nullable=True, chn_name='内部代码')
    """内部代码:内部代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteTra', column_name='UpdateTime', column_type='datetime', nullable=False, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteTra', column_name='JSID', column_type='bigint', nullable=False, chn_name='JSID')
    """JSID:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteTra', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到所属公司股票的交易代码、简称等。"""

    StatDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteTra', column_name='StatDate', column_type='datetime', nullable=True, chn_name='统计日期')
    """统计日期:"""

    ListedShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteTra', column_name='ListedShares', column_type='decimal(16,0)', nullable=False, chn_name='已上市股数(股)')
    """已上市股数(股):"""

    AuthShaComSha: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteTra', column_name='AuthShaComSha', column_type='decimal(16,0)', nullable=False, chn_name='法定股数(股)')
    """法定股数(股):"""

    NotHKShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteTra', column_name='NotHKShares', column_type='decimal(16,0)', nullable=False, chn_name='非港股股数(股)')
    """非港股股数(股):"""

    Ashares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteTra', column_name='Ashares', column_type='decimal(16,0)', nullable=False, chn_name='A股股数(股)')
    """A股股数(股):"""

    Bshares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_HKDailyQuoteTra', column_name='Bshares', column_type='decimal(16,0)', nullable=False, chn_name='B股股数(股)')
    """B股股数(股):"""

