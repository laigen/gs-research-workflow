# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_ExgIndustry(SQLTableEntity):
    name: str = 'HK_ExgIndustry'
    
    chn_name: str = '港股公司行业划分表'
    
    business_unique: str = 'CompanyCode,Standard,IndustryNum,ExcuteDate'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.描述香港联交所上市的公司的行业分类，主要有恒生行业分类、恒生聚源行业分类、中国证监会行业分类、申万行业分类等，该表记录港股上市公司的行业分类。                                       
2.信息来源：港交所、恒生聚源等。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExgIndustry', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExgIndustry', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司内码')
    """公司内码:公司内码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到港股的交易代码、简称等。"""

    Standard: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExgIndustry', column_name='Standard', column_type='int', nullable=True, chn_name='行业划分标准')
    """行业划分标准:行业划分标准(Standard)与(CT_SystemConst)表中的DM字段关联，令LB=1081，得到行业划分标准的具体描述：1-CSRC行业分类，2-非CSRC行业分类，3-中信行业分类，5-SSE行业分类，6-GICS行业分类，7-SSE-GICS行业分类，8-聚源行业分类，9-申万行业分类，10-聚源板块分类，11-中银(BOCI)行业分类，12..."""

    IndustryNum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExgIndustry', column_name='IndustryNum', column_type='int', nullable=True, chn_name='行业编码')
    """行业编码:行业编码（IndustryNum）：与“港股行业分类表（HK_IndustryCategory）”中的“行业编码（行业编码）”关联，得到行业的名称及相关信息。"""

    ExcuteDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExgIndustry', column_name='ExcuteDate', column_type='datetime', nullable=True, chn_name='生效日期')
    """生效日期:"""

    CancelDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExgIndustry', column_name='CancelDate', column_type='datetime', nullable=False, chn_name='取消日期')
    """取消日期:"""

    IfExecuted: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExgIndustry', column_name='IfExecuted', column_type='tinyint', nullable=False, chn_name='是否执行')
    """是否执行:是否执行（IfExecuted）：该字段固定以下常量1-是，2-否"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExgIndustry', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='修改时间')
    """修改时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExgIndustry', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

