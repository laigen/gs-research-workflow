# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_FundTradeInfo(SQLTableEntity):
    name: str = 'MF_FundTradeInfo'
    
    chn_name: str = '公募基金股票交易信息'
    
    business_unique: str = 'InnerCode,ReportDate'
    
    refresh_freq: str = """半年更新"""
    
    comment: str = """1.本表记录了中报、年报中公布报告期内股票买卖金额信息，包括买入股票成本、卖出股票收入等数据。
2.历史数据：2004年6月起-至今。
3.数据来源：基金公司披露的定期报告。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundTradeInfo', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundTradeInfo', column_name='InnerCode', column_type='int', nullable=True, chn_name='基金内部编码')
    """基金内部编码:基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundTradeInfo', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    ReportDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundTradeInfo', column_name='ReportDate', column_type='datetime', nullable=True, chn_name='报告期')
    """报告期:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundTradeInfo', column_name='InfoSource', column_type='varchar(50)', nullable=False, chn_name='信息来源')
    """信息来源:信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB = 1032，得到信息来源的具体描述：1-招股说明书，2-招股意向书，3-配股说明书，4-上市公告书，5-年度报告，6-中期报告，7-公司章程，8-增发新股招股说明书，9-增发新股招股意向书，10-增发新股上市公告书，11-可转换债券募集说明书，12-可转换债券上市..."""

    BuyingCost: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundTradeInfo', column_name='BuyingCost', column_type='decimal(19,4)', nullable=False, chn_name='买入股票成本')
    """买入股票成本:"""

    SellingIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundTradeInfo', column_name='SellingIncome', column_type='decimal(19,4)', nullable=False, chn_name='卖出股票收入')
    """卖出股票收入:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundTradeInfo', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新日期')
    """更新日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundTradeInfo', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

