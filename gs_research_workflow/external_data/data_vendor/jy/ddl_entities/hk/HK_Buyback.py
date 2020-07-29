# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_Buyback(SQLTableEntity):
    name: str = 'HK_Buyback'
    
    chn_name: str = '港股股份回购'
    
    business_unique: str = 'InnerCode,CompanyCode,EndDate'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.介绍港股发生股份回购的相关资料,如回购的股票类型、回购数量、回购金额、回购的最高价和最低价等。
2.数据范围：2001年至今。 
3.信息来源：港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Buyback', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    ParValueUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Buyback', column_name='ParValueUnit', column_type='varchar(50)', nullable=False, chn_name='面值单位')
    """面值单位:"""

    ParValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Buyback', column_name='ParValue', column_type='decimal(19,8)', nullable=False, chn_name='面值(元/股)')
    """面值(元/股):"""

    BuybackSum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Buyback', column_name='BuybackSum', column_type='decimal(18,4)', nullable=False, chn_name='本次回购数量(股)')
    """本次回购数量(股):"""

    HighPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Buyback', column_name='HighPrice', column_type='decimal(18,4)', nullable=False, chn_name='最高价(元)')
    """最高价(元):"""

    LowPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Buyback', column_name='LowPrice', column_type='decimal(18,4)', nullable=False, chn_name='最低价(元)')
    """最低价(元):"""

    BuybackMoney: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Buyback', column_name='BuybackMoney', column_type='decimal(19,4)', nullable=False, chn_name='回购金额(元)')
    """回购金额(元):"""

    CumulativeSum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Buyback', column_name='CumulativeSum', column_type='decimal(18,4)', nullable=False, chn_name='本年累计回购数量(股)')
    """本年累计回购数量(股):"""

    CumulativeSumToTS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Buyback', column_name='CumulativeSumToTS', column_type='decimal(19,8)', nullable=False, chn_name='本年累计回购数量占总股本的比例')
    """本年累计回购数量占总股本的比例:"""

    MethodStatement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Buyback', column_name='MethodStatement', column_type='varchar(500)', nullable=False, chn_name='回购方法说明')
    """回购方法说明:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Buyback', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Buyback', column_name='InnerCode', column_type='int', nullable=True, chn_name='港股内部代码')
    """港股内部代码:港股内部代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Buyback', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Buyback', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到所属公司股票的交易代码、简称等。"""

    PublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Buyback', column_name='PublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Buyback', column_name='InfoSource', column_type='varchar(50)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Buyback', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    ShareTypeCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Buyback', column_name='ShareTypeCode', column_type='int', nullable=False, chn_name='股份类别代码')
    """股份类别代码:股份类别代码(ShareTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1341，得到股份类别代码的具体描述：10-普通股，20-优先股，30-债权证，40-普通股-A类，50-普通股-B类。"""

    ShareType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Buyback', column_name='ShareType', column_type='varchar(50)', nullable=False, chn_name='股份类别')
    """股份类别:"""

    ParValueCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Buyback', column_name='ParValueCode', column_type='int', nullable=False, chn_name='面值单位代码')
    """面值单位代码:面值单位代码(ParValueCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1068，得到面值单位代码的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，1170-约旦第纳尔，11..."""

