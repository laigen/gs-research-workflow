# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_SWSIndexCW(SQLTableEntity):
    name: str = 'LC_SWSIndexCW'
    
    chn_name: str = '申万指数成份股权重'
    
    business_unique: str = '申万授权'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.收录了申银万国研究所发布的各指数成份证券的权重信息，通过与证券主表进行关联，可以获取指数以及成份股的基本信息。
2.历史数据：2012年1月至今
3.数据源：申银万国研究所"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SWSIndexCW', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    IndexCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SWSIndexCW', column_name='IndexCode', column_type='int', nullable=True, chn_name='指数内部编码')
    """指数内部编码:指数内部编码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称等。"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SWSIndexCW', column_name='InnerCode', column_type='int', nullable=True, chn_name='成份股内部编码')
    """成份股内部编码:成份股内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到成份股的交易代码、简称等。"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SWSIndexCW', column_name='InfoSource', column_type='varchar(200)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SWSIndexCW', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    Weight: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SWSIndexCW', column_name='Weight', column_type='decimal(18,6)', nullable=True, chn_name='权重(%)')
    """权重(%):"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SWSIndexCW', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SWSIndexCW', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

