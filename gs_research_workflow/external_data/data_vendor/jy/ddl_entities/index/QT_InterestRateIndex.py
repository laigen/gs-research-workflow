# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class QT_InterestRateIndex(SQLTableEntity):
    name: str = 'QT_InterestRateIndex'
    
    chn_name: str = '利率指数行情'
    
    business_unique: str = 'EndDate'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.收录了以1000点为基数，按照人民币利率，计算活期存款、三个月定存、半年定存、一年定存、二年定存、三年定存、五年定存以及七天通知存款的收益。
2.历史数据：1998年3月至今
3.数据源：中国人民银行"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_InterestRateIndex', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    IndexTD5Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_InterestRateIndex', column_name='IndexTD5Y', column_type='decimal(18,6)', nullable=False, chn_name='五年')
    """五年:"""

    IndexND7D: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_InterestRateIndex', column_name='IndexND7D', column_type='decimal(18,6)', nullable=False, chn_name='七天')
    """七天:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_InterestRateIndex', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='修改日期')
    """修改日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_InterestRateIndex', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_InterestRateIndex', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    BaseDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_InterestRateIndex', column_name='BaseDate', column_type='datetime', nullable=False, chn_name='基日')
    """基日:"""

    IndexDD: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_InterestRateIndex', column_name='IndexDD', column_type='decimal(18,6)', nullable=False, chn_name='活期存款')
    """活期存款:"""

    IndexTD3M: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_InterestRateIndex', column_name='IndexTD3M', column_type='decimal(18,6)', nullable=False, chn_name='三个月')
    """三个月:"""

    IndexTD6M: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_InterestRateIndex', column_name='IndexTD6M', column_type='decimal(18,6)', nullable=False, chn_name='半年')
    """半年:"""

    IndexTD1Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_InterestRateIndex', column_name='IndexTD1Y', column_type='decimal(18,6)', nullable=False, chn_name='一年')
    """一年:"""

    IndexTD2Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_InterestRateIndex', column_name='IndexTD2Y', column_type='decimal(18,6)', nullable=False, chn_name='二年')
    """二年:"""

    IndexTD3Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='QT_InterestRateIndex', column_name='IndexTD3Y', column_type='decimal(18,6)', nullable=False, chn_name='三年')
    """三年:"""

