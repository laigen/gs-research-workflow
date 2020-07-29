# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_IndustryCategory(SQLTableEntity):
    name: str = 'HK_IndustryCategory'
    
    chn_name: str = '港股行业分类表'
    
    business_unique: str = 'Standard,IndustryNum,ExcuteDate'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.记录香港证券市场主要公司行业分类标准及分类信息，包括行业的历史变更情况，包含的行业分类有恒生行业分类、恒生聚源行业分类、中国证监会行业分类、申万行业分类等。                              
2.信息来源：港交所、MSCI、中国证监会、申万官网等。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IndustryCategory', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    IndustryNameAbbr: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IndustryCategory', column_name='IndustryNameAbbr', column_type='varchar(50)', nullable=False, chn_name='行业名称简称')
    """行业名称简称:"""

    ChiSpelling: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IndustryCategory', column_name='ChiSpelling', column_type='varchar(50)', nullable=False, chn_name='行业拼音简称')
    """行业拼音简称:"""

    IndustryCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IndustryCategory', column_name='IndustryCode', column_type='varchar(10)', nullable=False, chn_name='行业代码')
    """行业代码:"""

    FatherIndustryCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IndustryCategory', column_name='FatherIndustryCode', column_type='varchar(10)', nullable=False, chn_name='父类行业代码')
    """父类行业代码:"""

    Classification: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IndustryCategory', column_name='Classification', column_type='int', nullable=False, chn_name='行业级别')
    """行业级别:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IndustryCategory', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='修改时间')
    """修改时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IndustryCategory', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    Standard: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IndustryCategory', column_name='Standard', column_type='int', nullable=True, chn_name='行业分类标准')
    """行业分类标准:行业分类标准(Standard)与(CT_SystemConst)表中的DM字段关联，令LB=1081，得到行业分类标准的具体描述：1-CSRC行业分类，2-非CSRC行业分类，3-中信行业分类，5-SSE行业分类，6-GICS行业分类，7-SSE-GICS行业分类，8-聚源行业分类，9-申万行业分类，10-聚源板块分类，11-中银(BOCI)行业分类，12..."""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IndustryCategory', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='发布日期')
    """发布日期:"""

    ExcuteDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IndustryCategory', column_name='ExcuteDate', column_type='datetime', nullable=True, chn_name='生效日期')
    """生效日期:"""

    CancelDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IndustryCategory', column_name='CancelDate', column_type='datetime', nullable=False, chn_name='取消日期')
    """取消日期:"""

    IfExecuted: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IndustryCategory', column_name='IfExecuted', column_type='tinyint', nullable=False, chn_name='是否有效')
    """是否有效:是否执行（IfExecuted）：本字段是固定字段1-是，2-否"""

    PubOrgCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IndustryCategory', column_name='PubOrgCode', column_type='int', nullable=False, chn_name='发布机构代码')
    """发布机构代码:发布机构代码（PubOrgCode）：“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到发布机构的具体名称、基本信息等。"""

    IndustryNum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IndustryCategory', column_name='IndustryNum', column_type='int', nullable=True, chn_name='行业编码')
    """行业编码:"""

    IndustryName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IndustryCategory', column_name='IndustryName', column_type='varchar(50)', nullable=False, chn_name='行业名称')
    """行业名称:"""

