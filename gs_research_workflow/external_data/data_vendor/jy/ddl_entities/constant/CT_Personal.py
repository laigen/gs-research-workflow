# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class CT_Personal(SQLTableEntity):
    name: str = 'CT_Personal'
    
    chn_name: str = '人员表'
    
    business_unique: str = 'PersonalNum'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """本表收录与证券市场相关人员的基本信息"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Personal', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    BirthY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Personal', column_name='BirthY', column_type='varchar(4)', nullable=False, chn_name='出生年份')
    """出生年份:"""

    Education: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Personal', column_name='Education', column_type='varchar(50)', nullable=False, chn_name='最高学历')
    """最高学历:"""

    ProfessionalTitle: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Personal', column_name='ProfessionalTitle', column_type='varchar(200)', nullable=False, chn_name='职称名称')
    """职称名称:"""

    Tel: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Personal', column_name='Tel', column_type='varchar(100)', nullable=False, chn_name='电话')
    """电话:"""

    Fax: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Personal', column_name='Fax', column_type='varchar(100)', nullable=False, chn_name='传真')
    """传真:"""

    Email: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Personal', column_name='Email', column_type='varchar(200)', nullable=False, chn_name='邮箱')
    """邮箱:"""

    Background: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Personal', column_name='Background', column_type='text', nullable=False, chn_name='简历')
    """简历:"""

    MajorName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Personal', column_name='MajorName', column_type='varchar(100)', nullable=False, chn_name='专业')
    """专业:"""

    PositionName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Personal', column_name='PositionName', column_type='varchar(200)', nullable=False, chn_name='职位名称')
    """职位名称:"""

    Remark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Personal', column_name='Remark', column_type='varchar(1000)', nullable=False, chn_name='备注')
    """备注:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Personal', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Personal', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Personal', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Personal', column_name='InfoSource', column_type='varchar(50)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    PersonalType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Personal', column_name='PersonalType', column_type='int', nullable=False, chn_name='类别所属类别')
    """类别所属类别:类别所属类别(PersonalType)与(CT_SystemConst)表中的DM字段关联，令LB = 1366，得到类别所属类别的具体描述：10-基金管理，20-机构研究，30-证监会从属机构委员。"""

    PersonalNum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Personal', column_name='PersonalNum', column_type='int', nullable=True, chn_name='人员编号')
    """人员编号:"""

    PersonalName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Personal', column_name='PersonalName', column_type='varchar(100)', nullable=False, chn_name='姓名')
    """姓名:"""

    WorkPlace: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Personal', column_name='WorkPlace', column_type='varchar(200)', nullable=False, chn_name='单位名称')
    """单位名称:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Personal', column_name='CompanyCode', column_type='int', nullable=False, chn_name='在任单位公司编号')
    """在任单位公司编号:在任单位公司编号（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到人员所在机构的基本信息"""

    Gender: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='CT_Personal', column_name='Gender', column_type='varchar(2)', nullable=False, chn_name='性别')
    """性别:"""

