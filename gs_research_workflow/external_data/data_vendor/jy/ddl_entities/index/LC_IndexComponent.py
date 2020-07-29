# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_IndexComponent(SQLTableEntity):
    name: str = 'LC_IndexComponent'
    
    chn_name: str = '指数成份'
    
    business_unique: str = 'IndexInnerCode,SecuInnerCode,InDate'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.收录了市场上主要指数的成份证券构成情况，包括成份证券的市场代码、入选日期、删除日期以及成份标志等信息。
2.该表仅收录主指数成份信息，不收录与主指数关系（Relationship）为“1-币种不同，2-分红规则不同，3-分红规则和币种都不同，4-税后分红”的衍生指数的信息。
3.历史数据：1990年12月至今
4.数据源：中证指数有限公司、上海证券交易所、深圳证券交易所、中央国债登记结算有限责任公司、申银万国研究所等"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexComponent', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    IndexInnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexComponent', column_name='IndexInnerCode', column_type='int', nullable=True, chn_name='指数内部编码')
    """指数内部编码:指数内部编码（IndexInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称等。"""

    SecuInnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexComponent', column_name='SecuInnerCode', column_type='int', nullable=True, chn_name='证券内部编码')
    """证券内部编码:证券内部编码（SecuInnerCode）：当SecuMarket=83、90或89时，与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联；当SecuMarket=72时，与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联。"""

    SecuMarket: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexComponent', column_name='SecuMarket', column_type='int', nullable=False, chn_name='成份股市场代码')
    """成份股市场代码:成份股市场代码(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB = 201，得到成份股市场代码的具体描述：10-上海期货交易所，11-上海国际能源交易中心，12-中国银行间外汇市场，13-大连商品交易所，14-上海黄金交易所，15-郑州商品交易所，49-澳大利亚证券交易所，50-新西兰证券交易所，51-中国金融期货交易所，..."""

    InDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexComponent', column_name='InDate', column_type='datetime', nullable=False, chn_name='入选日期')
    """入选日期:"""

    OutDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexComponent', column_name='OutDate', column_type='datetime', nullable=False, chn_name='剔除日期')
    """剔除日期:"""

    Flag: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexComponent', column_name='Flag', column_type='int', nullable=True, chn_name='成份标志')
    """成份标志:成份标志（Flag），该字段固定常量以下常量：1-是；0-否"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexComponent', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexComponent', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

