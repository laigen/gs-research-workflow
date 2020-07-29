# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class CT_Keywords(SQLTableEntity):
    name: str = 'CT_Keywords'
    
    chn_name: str = '系统关键词表'
    
    business_unique: str = '无'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """本表收录证券新闻等中用到的关键词"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Keywords', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    Type: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Keywords', column_name='Type', column_type='int', nullable=False, chn_name='类别')
    """类别:类别(Type)与(CT_SystemConst)表中的DM字段关联，令LB = 2，得到类别的具体描述：10-内部编码，11-公司代码，205-证券信托公司，206-省市表，301-行业表，311-临时公告关键词，312-非公告关键词，313-法律法规关键词，314-研究报告关键词，315-数据解读关键词，316-专题关键词，320-常规产品分类，321-..."""

    Content: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Keywords', column_name='Content', column_type='varchar(50)', nullable=False, chn_name='内容词组')
    """内容词组:"""

    Keyword: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Keywords', column_name='Keyword', column_type='varchar(50)', nullable=False, chn_name='关键词组')
    """关键词组:"""

    Code: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Keywords', column_name='Code', column_type='int', nullable=False, chn_name='代码')
    """代码:"""

    ChiSpelling: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Keywords', column_name='ChiSpelling', column_type='varchar(50)', nullable=False, chn_name='关键词拼音简称')
    """关键词拼音简称:"""

    InfoLevel: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Keywords', column_name='InfoLevel', column_type='tinyint', nullable=False, chn_name='级别')
    """级别:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Keywords', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='修改日期')
    """修改日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Keywords', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

