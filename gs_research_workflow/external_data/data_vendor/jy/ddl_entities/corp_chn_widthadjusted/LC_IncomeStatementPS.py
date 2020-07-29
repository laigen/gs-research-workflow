# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_IncomeStatementPS(SQLTableEntity):
    name: str = 'LC_IncomeStatementPS'
    
    chn_name: str = '利润分配表附注'
    
    business_unique: str = 'CompanyCode,EndDate,ItemCategory,ItemName'
    
    refresh_freq: str = """季更新"""
    
    comment: str = """1.描述新会计准则下，上市公司利润分配表附注的明细情况。
2.对于公告原文披露的项目名称，收录在“科目名称(ItemName)”中；“科目代码(ItemCode)”则对披露的科目进行了归类，以便于横向比较。
3.数据范围：1997-12-31至今
4.信息来源：招股说明书、定报、审计报告等"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementPS', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    ValueLastPeriod: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementPS', column_name='ValueLastPeriod', column_type='decimal(19,4)', nullable=False, chn_name='上年同期金额(元)')
    """上年同期金额(元):"""

    ValueThisPeriod: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementPS', column_name='ValueThisPeriod', column_type='decimal(19,4)', nullable=False, chn_name='本期金额(元)')
    """本期金额(元):"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementPS', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementPS', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementPS', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementPS', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    DateType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementPS', column_name='DateType', column_type='int', nullable=False, chn_name='日期类型')
    """日期类型:日期类型(DateType)与(CT_SystemConst)表中的DM字段关联，令LB = 1074 AND DM = 3，得到日期类型的具体描述：3-期末累计。"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementPS', column_name='InfoSource', column_type='varchar(50)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    ItemCategory: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementPS', column_name='ItemCategory', column_type='int', nullable=True, chn_name='科目类别')
    """科目类别:科目类别(ItemCategory)与(CT_SystemConst)表中的DM字段关联，令LB = 1041，得到科目类别的具体描述：10100-货币资金，10110-现金，10130-银行存款，10150-非银行存款，10190-其他货币资金，10200-短期投资，10210-短期股票投资，10211-上市股票投资，10213-非上市股票投资，10220..."""

    ItemCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementPS', column_name='ItemCode', column_type='int', nullable=False, chn_name='科目代码')
    """科目代码:科目代码(ItemCode):与“系统常量表(CT_SystemConst)”中的“代码(DM)”关联，当ItemCategory=18400时,令“LB=1134”，当ItemCategory为其他值时,令“LB=1041”，得到附注所属科目类别下具体科目的分类描述。"""

    ItemName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementPS', column_name='ItemName', column_type='varchar(100)', nullable=True, chn_name='科目名称')
    """科目名称:"""

    CurrencyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementPS', column_name='CurrencyCode', column_type='int', nullable=False, chn_name='计价货币')
    """计价货币:计价货币(CurrencyCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1068，得到计价货币的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，1170-约旦第纳尔，1180-科..."""

