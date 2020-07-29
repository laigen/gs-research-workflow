# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_IndexPrepComponent(SQLTableEntity):
    name: str = 'LC_IndexPrepComponent'
    
    chn_name: str = '指数备选成份'
    
    business_unique: str = 'IndexCode,EndDate,InnerCode'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.主要收录了上交所上海证券交易所和中证指数公司发布的部分指数的备选成份证券名单信息，包括生效日期、备选顺序。
2.历史数据：2007年1月至今
3.数据源：中证指数有限公司、上海证券交易所等"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexPrepComponent', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    IndexCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexPrepComponent', column_name='IndexCode', column_type='int', nullable=True, chn_name='指数内部编码')
    """指数内部编码:指数内部编码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称等。"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexPrepComponent', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexPrepComponent', column_name='EndDate', column_type='datetime', nullable=True, chn_name='生效日期')
    """生效日期:"""

    RankNo: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexPrepComponent', column_name='RankNo', column_type='int', nullable=False, chn_name='备选顺序')
    """备选顺序:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexPrepComponent', column_name='InnerCode', column_type='int', nullable=True, chn_name='备选成分股内部编码')
    """备选成分股内部编码:备选成分股内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到备选成份股的交易代码、简称等。"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexPrepComponent', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexPrepComponent', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

