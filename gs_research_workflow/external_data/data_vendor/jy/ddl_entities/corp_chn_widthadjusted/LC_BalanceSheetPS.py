# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_BalanceSheetPS(SQLTableEntity):
    name: str = 'LC_BalanceSheetPS'
    
    chn_name: str = '资产负债表附注'
    
    business_unique: str = 'CompanyCode,EndDate,Mark,ItemCategory,ItemName'
    
    refresh_freq: str = """季更新"""
    
    comment: str = """1.收录新会计准则下，上市公司资产负债表附注的明细情况。
2.对于公告原文披露的项目名称，收录在“科目名称（ItemName）”中；“科目代码（ItemCode）”则对披露的科目进行了归类，以便于横向比较。
3.数据范围：1997-12-31至今
4.信息来源：招股说明书、定报、审计报告等"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetPS', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    OpeningBalance: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetPS', column_name='OpeningBalance', column_type='decimal(19,4)', nullable=False, chn_name='1.期初金额')
    """1.期初金额:"""

    CalculatingSumStart: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetPS', column_name='CalculatingSumStart', column_type='decimal(19,4)', nullable=False, chn_name='期初计提金额')
    """期初计提金额:"""

    CurrentIncrease: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetPS', column_name='CurrentIncrease', column_type='decimal(19,4)', nullable=False, chn_name='2.本期增加')
    """2.本期增加:"""

    IncreaseByMA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetPS', column_name='IncreaseByMA', column_type='decimal(19,4)', nullable=False, chn_name='#购并增加')
    """#购并增加:"""

    IncreaseByWriteBack: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetPS', column_name='IncreaseByWriteBack', column_type='decimal(19,4)', nullable=False, chn_name='#本期转回增加')
    """#本期转回增加:"""

    IncreaseByOtherWay: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetPS', column_name='IncreaseByOtherWay', column_type='decimal(19,4)', nullable=False, chn_name='#其他增加')
    """#其他增加:"""

    CurrentDecrease: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetPS', column_name='CurrentDecrease', column_type='decimal(19,4)', nullable=False, chn_name='3.本期减少')
    """3.本期减少:"""

    DecreaseByTransferredOut: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetPS', column_name='DecreaseByTransferredOut', column_type='decimal(19,4)', nullable=False, chn_name='#本期转出或转回减少')
    """#本期转出或转回减少:"""

    DecreaseByAmortization: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetPS', column_name='DecreaseByAmortization', column_type='decimal(19,4)', nullable=False, chn_name='#本期摊销或转销减少')
    """#本期摊销或转销减少:"""

    DecreaseByOtherWay: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetPS', column_name='DecreaseByOtherWay', column_type='decimal(19,4)', nullable=False, chn_name='#其他减少')
    """#其他减少:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetPS', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。"""

    EndingBalance: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetPS', column_name='EndingBalance', column_type='decimal(19,4)', nullable=False, chn_name='4.期末金额')
    """4.期末金额:"""

    CalculatingSumEnd: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetPS', column_name='CalculatingSumEnd', column_type='decimal(19,4)', nullable=False, chn_name='期末计提金额')
    """期末计提金额:"""

    Remarks: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetPS', column_name='Remarks', column_type='varchar(500)', nullable=False, chn_name='备注说明')
    """备注说明:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetPS', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetPS', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetPS', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetPS', column_name='InfoSource', column_type='varchar(50)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    Mark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetPS', column_name='Mark', column_type='int', nullable=True, chn_name='合并调整标志')
    """合并调整标志:合并调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1511，得到合并调整标志的具体描述：1-合并调整，2-合并未调整，3-母公司调整，4-母公司未调整，5-专项合并调整，6-专项合并未调整。"""

    ItemCategory: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetPS', column_name='ItemCategory', column_type='int', nullable=True, chn_name='科目类别')
    """科目类别:科目类别(ItemCategory)与(CT_SystemConst)表中的DM字段关联，令LB = 1041，得到科目类别的具体描述：10100-货币资金，10110-现金，10130-银行存款，10150-非银行存款，10190-其他货币资金，10200-短期投资，10210-短期股票投资，10211-上市股票投资，10213-非上市股票投资，10220..."""

    ItemName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetPS', column_name='ItemName', column_type='varchar(200)', nullable=True, chn_name='科目名称')
    """科目名称:"""

    ItemCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetPS', column_name='ItemCode', column_type='int', nullable=False, chn_name='科目代码')
    """科目代码:科目代码（ItemCode）与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，当科目代码（ItemCode）为四位数时，令“LB=1134”；当科目代码（ItemCode）为五位数时,令“LB=1041”，得到资产负债表附注科目类别下具体科目。"""

    CurrencyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BalanceSheetPS', column_name='CurrencyCode', column_type='int', nullable=False, chn_name='计价货币')
    """计价货币:计价货币(CurrencyCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1068，得到计价货币的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，1170-约旦第纳尔，1180-科..."""

