# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_IndexRelationship(SQLTableEntity):
    name: str = 'LC_IndexRelationship'
    
    chn_name: str = '指数代码关联'
    
    business_unique: str = '指数常量表单'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.收录了同一指数在不同的证券发布市场上的代码之间的关联信息；以及同一指数在不同证券主表中的关联内码信息。
2.数据源：深圳证券交易所、上海证券交易所等"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexRelationship', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    RelatedSecuCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexRelationship', column_name='RelatedSecuCode', column_type='varchar(20)', nullable=False, chn_name='关联对应指数代码')
    """关联对应指数代码:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexRelationship', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexRelationship', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexRelationship', column_name='InnerCode', column_type='int', nullable=True, chn_name='内部编码')
    """内部编码:内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称等。"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexRelationship', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:"""

    SecuCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexRelationship', column_name='SecuCode', column_type='varchar(20)', nullable=False, chn_name='指数代码')
    """指数代码:"""

    SecuMarket: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexRelationship', column_name='SecuMarket', column_type='int', nullable=True, chn_name='证券市场/主表')
    """证券市场/主表:证券市场/主表（SecuMarket）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令“LB=201”，得到该字段的具体描述。
当代码关联方式=30（同一指数不同代码关联），这里的描述即为指数所属的市场。83-上海证券交易所，90-深圳证券交易所,84-其他市场，72-香港联交所
当代码关联方式=56（同一指数不同内码关联），这..."""

    CodeDefine: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexRelationship', column_name='CodeDefine', column_type='int', nullable=True, chn_name='关联方式')
    """关联方式:关联方式(CodeDefine)与(CT_SystemConst)表中的DM字段关联，令LB = 1350 AND DM IN (30,56)，得到关联方式的具体描述：30-同一指数代码关联，56-同一指数内码关联。"""

    Market: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexRelationship', column_name='Market', column_type='int', nullable=True, chn_name='关联对应证券市场/主表')
    """关联对应证券市场/主表:关联对应证券市场/主表（Market）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令“LB=201”，得到该字段的具体描述。
当代码关联方式=30（同一指数不同代码关联），这里的描述即为指数所属的市场。83-上海证券交易所，90-深圳证券交易所,84-其他市场，72-香港联交所
当代码关联方式=56（同一指数不同内码关联），这..."""

    RelatedInnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexRelationship', column_name='RelatedInnerCode', column_type='int', nullable=True, chn_name='关联对应内部编码')
    """关联对应内部编码:关联对应内部编码（RelatedInnerCode）：当个数小于7位时，与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称；反之与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称。"""

    RelatedCompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexRelationship', column_name='RelatedCompanyCode', column_type='int', nullable=True, chn_name='关联对应公司代码')
    """关联对应公司代码:"""

