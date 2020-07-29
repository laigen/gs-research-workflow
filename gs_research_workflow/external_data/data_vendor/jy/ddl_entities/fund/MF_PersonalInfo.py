# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_PersonalInfo(SQLTableEntity):
    name: str = 'MF_PersonalInfo'
    
    chn_name: str = '公募基金经理基本资料'
    
    business_unique: str = '与公募基金经理(新) MF_FundManagerNew一起开'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.本表基金经理的基本资料包括学历、证券从业经验、背景介绍等信息。可以通过所属人员代码关联MF_FundManagerNew，配合使用。
2.历史数据：1998年3月起-至今。
3.信息来源：基金公司官网披露的产品说明书、其他公开信息源。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PersonalInfo', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    Education: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PersonalInfo', column_name='Education', column_type='int', nullable=False, chn_name='最高学历')
    """最高学历:最高学历(Education)与(CT_SystemConst)表中的DM字段关联，令LB=1154，得到最高学历的具体描述：1-博士后，2-博士，3-硕士，4-本科，5-大专，6-高中，7-中专，8-其他。"""

    IDCardNum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PersonalInfo', column_name='IDCardNum', column_type='varchar(50)', nullable=False, chn_name='身份证')
    """身份证:"""

    PassportNum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PersonalInfo', column_name='PassportNum', column_type='varchar(100)', nullable=False, chn_name='护照')
    """护照:"""

    PracticeDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PersonalInfo', column_name='PracticeDate', column_type='datetime', nullable=False, chn_name='证券从业日期')
    """证券从业日期:"""

    ExperienceTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PersonalInfo', column_name='ExperienceTime', column_type='decimal(4,1)', nullable=False, chn_name='证券从业经历（年）')
    """证券从业经历（年）:"""

    ProQualifi: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PersonalInfo', column_name='ProQualifi', column_type='varchar(100)', nullable=False, chn_name='专业资格')
    """专业资格:"""

    Background: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PersonalInfo', column_name='Background', column_type='text', nullable=False, chn_name='背景介绍')
    """背景介绍:"""

    PersonalData: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PersonalInfo', column_name='PersonalData', column_type='blob', nullable=False, chn_name='个人资料')
    """个人资料:"""

    FileType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PersonalInfo', column_name='FileType', column_type='int', nullable=False, chn_name='文件格式')
    """文件格式:文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB = 1309，得到文件格式的具体描述：1-PDF，2-DOC，3-TXT，4-XLS，5-HTML，6-RTF，7-MHT，8-RAR，9-PPT，10-JPG，11-DOCX，12-XLSX，13-PPTX，14-EML，15-ZIP，16-DOCM，17-XLSM，..."""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PersonalInfo', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    PersonalCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PersonalInfo', column_name='PersonalCode', column_type='bigint', nullable=True, chn_name='所属人员编码')
    """所属人员编码:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PersonalInfo', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    ChineseName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PersonalInfo', column_name='ChineseName', column_type='varchar(30)', nullable=False, chn_name='姓名')
    """姓名:"""

    OtherName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PersonalInfo', column_name='OtherName', column_type='varchar(30)', nullable=False, chn_name='曾用名')
    """曾用名:"""

    EnglishName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PersonalInfo', column_name='EnglishName', column_type='varchar(30)', nullable=False, chn_name='英文名')
    """英文名:"""

    Gender: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PersonalInfo', column_name='Gender', column_type='int', nullable=False, chn_name='性别')
    """性别:性别(Gender)与(CT_SystemConst)表中的DM字段关联，令LB=1234，得到性别的具体描述：1-男，2-女。"""

    Nationality: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PersonalInfo', column_name='Nationality', column_type='int', nullable=False, chn_name='国籍')
    """国籍:国籍(Nationality)与(CT_SystemConst)表中的DM字段关联，令LB=1023 AND DM IN (142,110,143,502)，得到国籍的具体描述：110-中国香港，142-中国，143-中国台湾，502-美国。"""

    BirthDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PersonalInfo', column_name='BirthDate', column_type='datetime', nullable=False, chn_name='出生日期')
    """出生日期:"""

    BirthYMInfo: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_PersonalInfo', column_name='BirthYMInfo', column_type='varchar(20)', nullable=False, chn_name='出生年月（文本）')
    """出生年月（文本）:"""

