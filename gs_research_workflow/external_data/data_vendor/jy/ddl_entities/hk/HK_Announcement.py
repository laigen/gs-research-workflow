# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_Announcement(SQLTableEntity):
    name: str = 'HK_Announcement'
    
    chn_name: str = '港股公司公告'
    
    business_unique: str = 'ArticleID,InnerCode,InfoPublDate,AnnounceTypeT,ContentType'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.本表记录港股公司公告及通告，以文本的形式提供公告内容。
该表可与港股公告原文表通过原文ID关联，获取完整的公告内容。
2.数据范围：2014年8月至今。                  3.数据来源：港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Announcement', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    Content: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Announcement', column_name='Content', column_type='text', nullable=False, chn_name='详细内容')
    """详细内容:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Announcement', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新日期')
    """更新日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Announcement', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    ArticleID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Announcement', column_name='ArticleID', column_type='bigint', nullable=False, chn_name='原文ID')
    """原文ID:原文ID（ArticleID）与港股公告原文（HK_NotTextAnnouncement）表ID关联，获取港股公告原文的信息。"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Announcement', column_name='InnerCode', column_type='int', nullable=False, chn_name='证券内部编码')
    """证券内部编码:证券内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Announcement', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    AnnounceTypeF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Announcement', column_name='AnnounceTypeF', column_type='int', nullable=False, chn_name='一级公告类别')
    """一级公告类别:一级公告类别(AnnounceTypeF),二级公告类别(AnnounceTypeS),三级公告类别(AnnounceTypeT):与“港股公告类别结构表(HK_AnnounceStru)”中的“公告类别编码(TypeCode)”关联，得到公告类别的具体描述。"""

    AnnounceTypeS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Announcement', column_name='AnnounceTypeS', column_type='int', nullable=False, chn_name='二级公告类别')
    """二级公告类别:一级公告类别(AnnounceTypeF),二级公告类别(AnnounceTypeS),三级公告类别(AnnounceTypeT):与“港股公告类别结构表(HK_AnnounceStru)”中的“公告类别编码(TypeCode)”关联，得到公告类别的具体描述。"""

    AnnounceTypeT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Announcement', column_name='AnnounceTypeT', column_type='int', nullable=False, chn_name='三级公告类别')
    """三级公告类别:一级公告类别(AnnounceTypeF),二级公告类别(AnnounceTypeS),三级公告类别(AnnounceTypeT):与“港股公告类别结构表(HK_AnnounceStru)”中的“公告类别编码(TypeCode)”关联，得到公告类别的具体描述。"""

    InfoTitle: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Announcement', column_name='InfoTitle', column_type='varchar(600)', nullable=False, chn_name='公告标题')
    """公告标题:"""

    ContentType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Announcement', column_name='ContentType', column_type='int', nullable=False, chn_name='内容类别')
    """内容类别:内容类别(ContentType)与(CT_SystemConst)表中的DM字段关联，令LB = 1855，得到内容类别的具体描述：1-公告正文，2-公告摘要。"""

