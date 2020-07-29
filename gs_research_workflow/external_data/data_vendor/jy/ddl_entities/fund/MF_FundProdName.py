# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_FundProdName(SQLTableEntity):
    name: str = 'MF_FundProdName'
    
    chn_name: str = '公募基金产品名称'
    
    business_unique: str = 'InnerCode,InfoType,EffectiveDate'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.本表记录基金的交易所披露简称、集中申购简称、ETF申购赎回简称等基金相关的名称类信息。
2.历史数据：1998年3月起-至今。
3.信息来源：基金公司官网披露的产品说明书。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundProdName', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    IfEffected: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundProdName', column_name='IfEffected', column_type='int', nullable=False, chn_name='是否有效')
    """是否有效:是否有效（IfEffected），该字段固定以下常量：0-否；1-是"""

    Remark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundProdName', column_name='Remark', column_type='varchar(500)', nullable=False, chn_name='备注说明')
    """备注说明:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundProdName', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundProdName', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundProdName', column_name='InnerCode', column_type='int', nullable=False, chn_name='基金内部编码')
    """基金内部编码:基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundProdName', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundProdName', column_name='InfoSource', column_type='varchar(100)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    InfoType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundProdName', column_name='InfoType', column_type='int', nullable=False, chn_name='信息类别')
    """信息类别:信息类别(InfoType)与(CT_SystemConst)表中的DM字段关联，令LB = 1850，得到信息类别的具体描述：1-证券交易所简称，2-集中申购简称，3-ETF申购赎回简称。"""

    DisclName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundProdName', column_name='DisclName', column_type='varchar(200)', nullable=False, chn_name='披露名称')
    """披露名称:"""

    ChiSpelling: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundProdName', column_name='ChiSpelling', column_type='varchar(20)', nullable=False, chn_name='拼音证券简称')
    """拼音证券简称:"""

    EffectiveDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundProdName', column_name='EffectiveDate', column_type='datetime', nullable=False, chn_name='生效日期')
    """生效日期:"""

    ExpiryDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundProdName', column_name='ExpiryDate', column_type='datetime', nullable=False, chn_name='失效日期')
    """失效日期:"""

