# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_InvestIndustry(SQLTableEntity):
    name: str = 'MF_InvestIndustry'
    
    chn_name: str = '公募基金行业投资'
    
    business_unique: str = 'InnerCode,ReportDate,InvestType,IndustryCode'
    
    refresh_freq: str = """季更新"""
    
    comment: str = """1.本表记录基金行业投资分布信息，包括行业的名称、代码、行业市值、该行业市值占基金净资产的比例等。
2.历史数据：1998年6月起-至今。
3.数据来源：基金公司披露的定期报告。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestIndustry', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    MarketValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestIndustry', column_name='MarketValue', column_type='decimal(19,4)', nullable=False, chn_name='行业市值(元)')
    """行业市值(元):"""

    RatioInNV: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestIndustry', column_name='RatioInNV', column_type='decimal(18,6)', nullable=False, chn_name='占资产净值比例')
    """占资产净值比例:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestIndustry', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新日期')
    """更新日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestIndustry', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestIndustry', column_name='InnerCode', column_type='int', nullable=True, chn_name='基金内部编码')
    """基金内部编码:基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestIndustry', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    ReportDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestIndustry', column_name='ReportDate', column_type='datetime', nullable=True, chn_name='报告期')
    """报告期:"""

    InvestType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestIndustry', column_name='InvestType', column_type='int', nullable=True, chn_name='投资类型')
    """投资类型:投资类型(InvestType)与(CT_SystemConst)表中的DM字段关联，令LB = 1090，得到投资类型的具体描述：1-综合投资，2-积极投资，3-指数投资，4-境内投资，5-沪港通投资。"""

    InduStandard: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestIndustry', column_name='InduStandard', column_type='int', nullable=False, chn_name='行业划分标准')
    """行业划分标准:行业划分标准(InduStandard)与(CT_SystemConst)表中的DM字段关联，令LB = 1081，得到行业划分标准的具体描述：1-CSRC行业分类，2-非CSRC行业分类，3-中信行业分类，5-SSE行业分类，6-GICS行业分类，7-SSE-GICS行业分类，8-聚源行业分类，9-申万行业分类，10-聚源板块分类，11-中银(BOCI)行..."""

    IndustryCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestIndustry', column_name='IndustryCode', column_type='int', nullable=False, chn_name='行业代码')
    """行业代码:行业代码(IndustryCode)：当InduStandard=22时，与“系统常量表（CT_SystemConst）”的“代码（DM）”关联，“LB=1755”；当InduStandardISNULL时，和行业表(CT_Industry)中字段行业编码(IndustryNum)关联。"""

    InduDiscCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestIndustry', column_name='InduDiscCode', column_type='varchar(10)', nullable=False, chn_name='行业代码(公布)')
    """行业代码(公布):"""

    IndustryName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestIndustry', column_name='IndustryName', column_type='varchar(50)', nullable=True, chn_name='行业名称')
    """行业名称:"""

