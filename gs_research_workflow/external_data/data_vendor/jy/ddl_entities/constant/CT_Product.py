# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class CT_Product(SQLTableEntity):
    name: str = 'CT_Product'
    
    chn_name: str = '产品表'
    
    business_unique: str = 'ProductCategory,ProductCode'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """本表收录各种产品名称、代码、分类以及所属行业的情况。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Product', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    ProductCategory: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Product', column_name='ProductCategory', column_type='varchar(30)', nullable=True, chn_name='产品分类')
    """产品分类:产品分类(ProductCategory)与(CT_SystemConst)表中的DM字段关联，令LB = 2，得到产品分类的具体描述：10-内部编码，11-公司代码，205-证券信托公司，206-省市表，301-行业表，311-临时公告关键词，312-非公告关键词，313-法律法规关键词，314-研究报告关键词，315-数据解读关键词，316-专题关键词，..."""

    ProductName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Product', column_name='ProductName', column_type='varchar(50)', nullable=True, chn_name='产品名称')
    """产品名称:"""

    ProductCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Product', column_name='ProductCode', column_type='varchar(20)', nullable=True, chn_name='产品代码')
    """产品代码:"""

    IndustryCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Product', column_name='IndustryCode', column_type='char(20)', nullable=False, chn_name='所属行业代码')
    """所属行业代码:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Product', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Product', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

