# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_SpecialNotice(SQLTableEntity):
    name: str = 'HK_SpecialNotice'
    
    chn_name: str = '港股特别提示'
    
    business_unique: str = 'InnerCode,NoticeStartDate,NoticeEndDate,NoticeType'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.公司发行上市、分红配股、公告停牌、临时停牌、召开股东大会、报告预约披露等等方面的当日提示、未来提示。
2.数据范围：1999年至今。
3.数据来源：港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SpecialNotice', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    NoticeType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SpecialNotice', column_name='NoticeType', column_type='int', nullable=False, chn_name='提示信息类别代码')
    """提示信息类别代码:提示信息类别代码(NoticeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1355，得到提示信息类别代码的具体描述：100-上市日，110-认购申请截止日，120-寄发日，130-发行结果公布日，140-买卖未缴款股份日，150-缴款截止日，160-除净日，165-股权登记日，170-记录日，180-截止过户日，190-股息应..."""

    NoticeTypeName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SpecialNotice', column_name='NoticeTypeName', column_type='varchar(40)', nullable=False, chn_name='提示信息类别名称')
    """提示信息类别名称:"""

    Content: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SpecialNotice', column_name='Content', column_type='varchar(500)', nullable=False, chn_name='提示信息内容')
    """提示信息内容:"""

    SusReTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SpecialNotice', column_name='SusReTime', column_type='varchar(10)', nullable=False, chn_name='停/复牌时间')
    """停/复牌时间:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SpecialNotice', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SpecialNotice', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SpecialNotice', column_name='InnerCode', column_type='int', nullable=True, chn_name='内部代码')
    """内部代码:内部代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。"""

    SecuCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SpecialNotice', column_name='SecuCode', column_type='varchar(20)', nullable=True, chn_name='证券代码')
    """证券代码:"""

    SecuAbbr: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SpecialNotice', column_name='SecuAbbr', column_type='varchar(20)', nullable=False, chn_name='证券简称')
    """证券简称:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SpecialNotice', column_name='CompanyCode', column_type='int', nullable=False, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到港股的交易代码、简称等。"""

    NoticeStartDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SpecialNotice', column_name='NoticeStartDate', column_type='datetime', nullable=False, chn_name='提示起始日')
    """提示起始日:"""

    NoticeEndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SpecialNotice', column_name='NoticeEndDate', column_type='datetime', nullable=False, chn_name='提示截止日')
    """提示截止日:"""

    StartDateNotes: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SpecialNotice', column_name='StartDateNotes', column_type='varchar(50)', nullable=False, chn_name='起始日描述')
    """起始日描述:"""

    EndDateNotes: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SpecialNotice', column_name='EndDateNotes', column_type='varchar(50)', nullable=False, chn_name='截止日描述')
    """截止日描述:"""

