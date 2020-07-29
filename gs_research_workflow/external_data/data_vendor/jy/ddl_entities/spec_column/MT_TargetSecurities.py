# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MT_TargetSecurities(SQLTableEntity):
    name: str = 'MT_TargetSecurities'
    
    chn_name: str = '融资融券标的证券'
    
    business_unique: str = 'InnerCode,InDate,OutDate,TargetCategory,TargetFlag'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.收录国内交易所公布的融资融券标的清单，包括融资买入标的和融券卖出标的；同时还收录了有披露起证券历次入选和剔除融资（融券）标的变化情况。
2.历史数据：交易所披露数据最早记录可追溯至2006年8月
3.数据来源：聚源按照上交所、深交所原始披露整理"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TargetSecurities', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TargetSecurities', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    SecuMarket: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TargetSecurities', column_name='SecuMarket', column_type='int', nullable=False, chn_name='证券市场')
    """证券市场:证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB = 201 AND DM IN (83,90)，得到证券市场的具体描述：83-上海证券交易所，90-深圳证券交易所。"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TargetSecurities', column_name='InnerCode', column_type='int', nullable=True, chn_name='证券内部编码')
    """证券内部编码:证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到标的证券的交易代码、简称等。"""

    TargetCategory: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TargetSecurities', column_name='TargetCategory', column_type='int', nullable=True, chn_name='标的类别')
    """标的类别:标的类别(TargetCategory)与(CT_SystemConst)表中的DM字段关联，令LB = 1575 AND DM IN (10,20)，得到标的类别的具体描述：10-融资买入标的，20-融券卖出标的。"""

    InDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TargetSecurities', column_name='InDate', column_type='datetime', nullable=True, chn_name='入选日期')
    """入选日期:"""

    OutDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TargetSecurities', column_name='OutDate', column_type='datetime', nullable=False, chn_name='剔除日期')
    """剔除日期:"""

    TargetFlag: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TargetSecurities', column_name='TargetFlag', column_type='int', nullable=False, chn_name='标的标志')
    """标的标志:标的标志（TargetFlag），该字段固定以下常量（通过剔除日期判断）：1-是标的证券；0-不是标的证券"""

    ChangeReasonDesc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TargetSecurities', column_name='ChangeReasonDesc', column_type='varchar(2000)', nullable=False, chn_name='变更原因描述')
    """变更原因描述:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MT_TargetSecurities', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

