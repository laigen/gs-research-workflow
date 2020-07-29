# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_UmbrellaFunds(SQLTableEntity):
    name: str = 'MF_UmbrellaFunds'
    
    chn_name: str = '公募基金伞形系列关系'
    
    business_unique: str = 'InnerCode,UmbrellaFundCode'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.本表记录了基金之间的伞形关系，包括招商安泰系列、国泰金龙系列、鹏华普天系列、银河银联系列等。
2.历史数据：1998年3月起-至今。
3.信息来源：基金公司官网披露的产品说明书。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_UmbrellaFunds', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_UmbrellaFunds', column_name='InnerCode', column_type='int', nullable=True, chn_name='基金内部编码')
    """基金内部编码:基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_UmbrellaFunds', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到基金公司的交易代码、简称等。"""

    UmbrellaFund: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_UmbrellaFunds', column_name='UmbrellaFund', column_type='varchar(200)', nullable=True, chn_name='伞形系列名称')
    """伞形系列名称:"""

    UmbrellaFundCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_UmbrellaFunds', column_name='UmbrellaFundCode', column_type='int', nullable=True, chn_name='伞形代码')
    """伞形代码:伞形代码(UmbrellaFundCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1418，得到伞形代码的具体描述：1101-招商安泰系列，1201-国泰金龙系列，1301-鹏华普天系列，1401-嘉实理财通系列，1501-银河银联系列，1601-融通通利系列，1701-泰达荷银系列，1801-华宝兴业宝康系列，1901-景顺长城..."""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_UmbrellaFunds', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_UmbrellaFunds', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

