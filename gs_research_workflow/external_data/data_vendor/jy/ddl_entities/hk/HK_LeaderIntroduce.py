# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_LeaderIntroduce(SQLTableEntity):
    name: str = 'HK_LeaderIntroduce'
    
    chn_name: str = '港股领导人背景介绍'
    
    business_unique: str = 'CompanyCode,LeaderID'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.介绍港股领导人的个人资料、职称和背景，包含的主要字段有：信息发布日期、姓名、年龄、最高学历、背景介绍等。
2.数据范围：2003年至今。
3.数据来源：港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_LeaderIntroduce', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    LeaderTitle: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_LeaderIntroduce', column_name='LeaderTitle', column_type='int', nullable=False, chn_name='职称')
    """职称:"""

    EarliestInDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_LeaderIntroduce', column_name='EarliestInDate', column_type='datetime', nullable=False, chn_name='最早任职年月')
    """最早任职年月:"""

    Background: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_LeaderIntroduce', column_name='Background', column_type='text', nullable=False, chn_name='背景介绍')
    """背景介绍:"""

    Statement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_LeaderIntroduce', column_name='Statement', column_type='varchar(500)', nullable=False, chn_name='备注')
    """备注:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_LeaderIntroduce', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='修改日期')
    """修改日期:"""

    BirthYMInfo: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_LeaderIntroduce', column_name='BirthYMInfo', column_type='varchar(20)', nullable=False, chn_name='出生年月(文本)')
    """出生年月(文本):"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_LeaderIntroduce', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_LeaderIntroduce', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到港股的交易代码、简称等。"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_LeaderIntroduce', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    LeaderID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_LeaderIntroduce', column_name='LeaderID', column_type='int', nullable=False, chn_name='领导人ID')
    """领导人ID:"""

    LeaderName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_LeaderIntroduce', column_name='LeaderName', column_type='varchar(100)', nullable=False, chn_name='姓名')
    """姓名:"""

    LeaderGender: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_LeaderIntroduce', column_name='LeaderGender', column_type='int', nullable=False, chn_name='性别')
    """性别:性别(LeaderGender)与(CT_SystemConst)表中的DM字段关联，令LB = 1234，得到性别的具体描述：1-男，2-女。"""

    BirthYM: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_LeaderIntroduce', column_name='BirthYM', column_type='datetime', nullable=False, chn_name='出生年月')
    """出生年月:"""

    Age: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_LeaderIntroduce', column_name='Age', column_type='int', nullable=False, chn_name='年龄(岁)')
    """年龄(岁):"""

    LeaderDegree: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_LeaderIntroduce', column_name='LeaderDegree', column_type='int', nullable=False, chn_name='最高学历')
    """最高学历:最高学历(LeaderDegree)与(CT_SystemConst)表中的DM字段关联，令LB = 1154，得到最高学历的具体描述：1-博士后，2-博士，3-硕士，4-本科，5-大专，6-高中，7-中专，8-其他。"""

