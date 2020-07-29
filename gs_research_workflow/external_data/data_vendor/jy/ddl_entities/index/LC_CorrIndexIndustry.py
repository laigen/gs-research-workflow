# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_CorrIndexIndustry(SQLTableEntity):
    name: str = 'LC_CorrIndexIndustry'
    
    chn_name: str = '指数与行业对应'
    
    business_unique: str = '此表与指数基本情况 LC_IndexBasicInfo关联，开通需要一起开'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.收录了行业指数与所属行业的对应关系，包括行业分类标准，行业分类信息；通过与系统常量表等相关联，能获取具体的行业分类标准和所属行业信息。
2.数据源：申银万国研究所、中证指数有限公司、中信证券股份有限公司等"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CorrIndexIndustry', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    IndexCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CorrIndexIndustry', column_name='IndexCode', column_type='int', nullable=True, chn_name='指数内码')
    """指数内码:指数内码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称等。"""

    IndustryStandard: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CorrIndexIndustry', column_name='IndustryStandard', column_type='int', nullable=True, chn_name='行业分类标准')
    """行业分类标准:行业分类标准(IndustryStandard)与(CT_SystemConst)表中的DM字段关联，令LB = 1081，得到行业分类标准的具体描述：1-CSRC行业分类，2-非CSRC行业分类，3-中信行业分类，5-SSE行业分类，6-GICS行业分类，7-SSE-GICS行业分类，8-聚源行业分类，9-申万行业分类，10-聚源板块分类，11-中银(BO..."""

    IndustryCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CorrIndexIndustry', column_name='IndustryCode', column_type='int', nullable=False, chn_name='所属行业')
    """所属行业:所属行业（IndustryCode）：
当IndustryStandard＝1、8或18时，与“行业表（CT_Industry）”中的“行业编码（IndustryNum）”关联； 当IndustryStandard＝3或5时，与“系统常量表（CT_SystemConst）”的“代码（DM）”关联，“LB=1082”； 当IndustryStandard＝6或..."""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CorrIndexIndustry', column_name='EndDate', column_type='datetime', nullable=False, chn_name='截止日期')
    """截止日期:"""

    IndexState: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CorrIndexIndustry', column_name='IndexState', column_type='int', nullable=False, chn_name='指数状态')
    """指数状态:指数状态（IndexState），该字段定为固定常量：1-新增；2-延用；3-停用"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CorrIndexIndustry', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CorrIndexIndustry', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

