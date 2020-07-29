# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_IndexComponentsWeight(SQLTableEntity):
    name: str = 'LC_IndexComponentsWeight'
    
    chn_name: str = '指数成份股权重'
    
    business_unique: str = 'IndexCode,InnerCode,EndDate'
    
    refresh_freq: str = """日更新
月更新"""
    
    comment: str = """1.收录了市场上主要指数成份证券的权重信息，包括中证指数有限公司每月发布的“沪深300”指数的权重数据等。
2.该表仅收录主指数成份权重信息，不收录与主指数关系（Relationship）为“1-币种不同，2-分红规则不同，3-分红规则和币种都不同，4-税后分红”的衍生指数的信息。
3.历史数据：1970年1月至今
4.数据源：中证指数有限公司、上海证券交易所、深圳证券交易所等"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexComponentsWeight', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    IndexCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexComponentsWeight', column_name='IndexCode', column_type='int', nullable=True, chn_name='指数内部编码')
    """指数内部编码:指数内部编码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称等。"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexComponentsWeight', column_name='InnerCode', column_type='int', nullable=True, chn_name='成份股内部编码')
    """成份股内部编码:成份股内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到成份股的交易代码、简称等。"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexComponentsWeight', column_name='InfoSource', column_type='varchar(200)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexComponentsWeight', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    Weight: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexComponentsWeight', column_name='Weight', column_type='decimal(18,6)', nullable=True, chn_name='权重(%)')
    """权重(%):"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexComponentsWeight', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexComponentsWeight', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

