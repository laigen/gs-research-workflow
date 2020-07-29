# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_CodeRelationship(SQLTableEntity):
    name: str = 'HK_CodeRelationship'
    
    chn_name: str = '港股代码关联表'
    
    business_unique: str = 'CodeDefine,IfEffected,InnerCode,RelatedInnerCode'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.记录香港上市公司对应的A股公司，美国预托证券（ADR）关联代码，以及港股转板公司转板前后的代码对应信息的信息。                           2.信息来源：港交所等。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CodeRelationship', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    RelatedInnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CodeRelationship', column_name='RelatedInnerCode', column_type='int', nullable=True, chn_name='关联代码内部编码')
    """关联代码内部编码:关联代码内部编码（RelatedInnerCode）：与“证券主表（SecuMain）”或者“美股证券主表（US_SecuMain）”中的“公司代码（InnerCode）”关联。"""

    RelatedCompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CodeRelationship', column_name='RelatedCompanyCode', column_type='int', nullable=True, chn_name='关联代码公司代码')
    """关联代码公司代码:关联代码公司代码（RelatedCompanyCode）：与“证券主表（SecuMain）”或者“美股证券主表（US_SecuMain）”中的“公司代码（CompanyCode）”关联。"""

    Market: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CodeRelationship', column_name='Market', column_type='int', nullable=True, chn_name='所属市场')
    """所属市场:所属市场（Market）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令“LB=201”， 得到
      证券市场的具体描述。
      90-深圳证券交易所，83-上海证券交易所，76-美国证券交易所，77-美国纳斯达克证券交易所"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CodeRelationship', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CodeRelationship', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    CodeDefine: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CodeRelationship', column_name='CodeDefine', column_type='int', nullable=True, chn_name='代码关联方式')
    """代码关联方式:代码关联方式(CodeDefine)与(CT_SystemConst)表中的DM字段关联，令LB=1350 AND DM =10，得到代码关联方式的具体描述：10-跨市场公司关联，201-ADR代码对应，202-港股创业板转主板。"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CodeRelationship', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    EffectiveDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CodeRelationship', column_name='EffectiveDate', column_type='datetime', nullable=False, chn_name='生效日期')
    """生效日期:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CodeRelationship', column_name='EndDate', column_type='datetime', nullable=False, chn_name='终止日期')
    """终止日期:"""

    IfEffected: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CodeRelationship', column_name='IfEffected', column_type='int', nullable=True, chn_name='是否有效')
    """是否有效:是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB=999 AND IN (1，2)，得到是否有效的具体描述："""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CodeRelationship', column_name='InnerCode', column_type='int', nullable=True, chn_name='内部代码')
    """内部代码:内部代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CodeRelationship', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到所属公司股票的交易代码、简称等。"""

    SecuMarket: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CodeRelationship', column_name='SecuMarket', column_type='int', nullable=True, chn_name='证券市场')
    """证券市场:证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB=201 AND DM=72，得到证券市场的具体描述：72-香港联交所。"""

