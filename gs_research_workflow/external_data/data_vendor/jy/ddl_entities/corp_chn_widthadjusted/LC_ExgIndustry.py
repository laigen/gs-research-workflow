# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_ExgIndustry(SQLTableEntity):
    name: str = 'LC_ExgIndustry'
    
    chn_name: str = '公司行业划分表'
    
    business_unique: str = 'CompanyCode,InfoPublDate,Standard,Industry,IfPerformed'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """收录上市公司在证监会行业划分、中信行业划分、GICS行业划分、申万行业划分、中信建投、中银(BOCI)行业分类、中证指数行业分类、聚源行业划分等各种划分标准下的所属行业情况。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ExgIndustry', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    FirstIndustryName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ExgIndustry', column_name='FirstIndustryName', column_type='varchar(100)', nullable=False, chn_name='一级行业名称')
    """一级行业名称:"""

    SecondIndustryCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ExgIndustry', column_name='SecondIndustryCode', column_type='varchar(20)', nullable=False, chn_name='二级行业代码')
    """二级行业代码:"""

    SecondIndustryName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ExgIndustry', column_name='SecondIndustryName', column_type='varchar(100)', nullable=False, chn_name='二级行业名称')
    """二级行业名称:"""

    ThirdIndustryCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ExgIndustry', column_name='ThirdIndustryCode', column_type='varchar(20)', nullable=False, chn_name='三级行业代码')
    """三级行业代码:"""

    ThirdIndustryName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ExgIndustry', column_name='ThirdIndustryName', column_type='varchar(100)', nullable=False, chn_name='三级行业名称')
    """三级行业名称:"""

    FourthIndustryCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ExgIndustry', column_name='FourthIndustryCode', column_type='varchar(20)', nullable=False, chn_name='四级行业代码')
    """四级行业代码:"""

    FourthIndustryName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ExgIndustry', column_name='FourthIndustryName', column_type='varchar(100)', nullable=False, chn_name='四级行业名称')
    """四级行业名称:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ExgIndustry', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='修改日期')
    """修改日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ExgIndustry', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ExgIndustry', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ExgIndustry', column_name='InfoPublDate', column_type='datetime', nullable=True, chn_name='信息发布日期')
    """信息发布日期:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ExgIndustry', column_name='InfoSource', column_type='varchar(100)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    Standard: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ExgIndustry', column_name='Standard', column_type='int', nullable=True, chn_name='行业划分标准')
    """行业划分标准:行业划分标准（Standard）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令“LB=1081”，得到行业划分的具体标准：1-证监会行业分类(不更新)，3-中信行业分类，5-上交所行业分类(不更新)，6-GICS行业分类(不更新)，7-SSE-GICS行业分类(不更新)，8-聚源行业分类(不更新)，9-申万行业分类(不更新)，..."""

    Industry: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ExgIndustry', column_name='Industry', column_type='int', nullable=False, chn_name='所属行业')
    """所属行业:所属行业（Industry）：
       当Standard＝1、8或18时，与“行业表（CT_Industry）”中的“行业编码（IndustryNum）”关联；
       当Standard＝3或5时，与“系统常量表（CT_SystemConst）”的“代码（DM）”关联，“LB=1082”；
       当Standard＝6或13时，与“系..."""

    IfPerformed: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ExgIndustry', column_name='IfPerformed', column_type='int', nullable=True, chn_name='是否执行')
    """是否执行:是否执行（IfPerformed），该字段固定以下常量：1-是；2-否"""

    CancelDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ExgIndustry', column_name='CancelDate', column_type='datetime', nullable=False, chn_name='取消日期')
    """取消日期:"""

    FirstIndustryCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ExgIndustry', column_name='FirstIndustryCode', column_type='varchar(20)', nullable=False, chn_name='一级行业代码')
    """一级行业代码:"""

