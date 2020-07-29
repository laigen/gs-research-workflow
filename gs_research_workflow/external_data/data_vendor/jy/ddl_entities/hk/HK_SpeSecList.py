# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_SpeSecList(SQLTableEntity):
    name: str = 'HK_SpeSecList'
    
    chn_name: str = '港股特别证券名单表'
    
    business_unique: str = 'InnerCode,ListType,InDate,IfEffected'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.记录港股市价调节机制（VCM）,收市竞价（CAS）等名单。包含字段有：名单类型、信息发布时间、入选时间、剔除时间等。
2.数据范围：2016-09至今。
3.数据来源：港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SpeSecList', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SpeSecList', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SpeSecList', column_name='InnerCode', column_type='int', nullable=True, chn_name='内部代码')
    """内部代码:内部代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。"""

    ListType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SpeSecList', column_name='ListType', column_type='int', nullable=True, chn_name='名单类型')
    """名单类型:名单类型(ListType)与(CT_SystemConst)表中的DM字段关联，令LB=1943，得到名单类型的具体描述：1-收市竞价，2-市调机制。"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SpeSecList', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    InDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SpeSecList', column_name='InDate', column_type='datetime', nullable=True, chn_name='入选日期')
    """入选日期:"""

    OutDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SpeSecList', column_name='OutDate', column_type='datetime', nullable=False, chn_name='剔除日期')
    """剔除日期:"""

    IfEffected: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SpeSecList', column_name='IfEffected', column_type='int', nullable=True, chn_name='是否有效')
    """是否有效:是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB=999 AND DM IN (1,2)，得到是否有效的具体描述：1-是，2-否。"""

    Mark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SpeSecList', column_name='Mark', column_type='varchar(200)', nullable=False, chn_name='备注')
    """备注:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SpeSecList', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

