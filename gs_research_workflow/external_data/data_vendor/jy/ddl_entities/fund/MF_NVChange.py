# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_NVChange(SQLTableEntity):
    name: str = 'MF_NVChange'
    
    chn_name: str = '公募基金净值变动'
    
    business_unique: str = 'InnerCode,ReportDate'
    
    refresh_freq: str = """半年更新"""
    
    comment: str = """1.本表记录中报、年报中披露的基金基金净值、基金净收益、报告期内基金申购赎回、利益分配等情况。
2.历史数据：2001年6月起-至今。
3.数据来源：基金公司披露的定期报告。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_NVChange', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    NVChangeDueToUnitTrade: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_NVChange', column_name='NVChangeDueToUnitTrade', column_type='decimal(19,4)', nullable=False, chn_name='基金单位交易产生的基金净值变动数(元)')
    """基金单位交易产生的基金净值变动数(元):"""

    DistributedProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_NVChange', column_name='DistributedProfit', column_type='decimal(19,4)', nullable=False, chn_name='本期向持有人分配收益(元)')
    """本期向持有人分配收益(元):"""

    NVAtEnd: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_NVChange', column_name='NVAtEnd', column_type='decimal(19,4)', nullable=False, chn_name='期末基金净值(元)')
    """期末基金净值(元):"""

    PriorYearProfitAdjust: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_NVChange', column_name='PriorYearProfitAdjust', column_type='decimal(19,4)', nullable=False, chn_name='以前年度损益调整')
    """以前年度损益调整:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_NVChange', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新日期')
    """更新日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_NVChange', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_NVChange', column_name='InnerCode', column_type='int', nullable=True, chn_name='基金内部编码')
    """基金内部编码:基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    ReportDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_NVChange', column_name='ReportDate', column_type='datetime', nullable=True, chn_name='报告期')
    """报告期:"""

    NVAtBegin: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_NVChange', column_name='NVAtBegin', column_type='decimal(19,4)', nullable=False, chn_name='期初基金净值(元)')
    """期初基金净值(元):"""

    NetProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_NVChange', column_name='NetProfit', column_type='decimal(19,4)', nullable=False, chn_name='基金净收益(元)')
    """基金净收益(元):"""

    UnrealizedProfitChange: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_NVChange', column_name='UnrealizedProfitChange', column_type='decimal(19,4)', nullable=False, chn_name='未实现估值增值变动数(元)')
    """未实现估值增值变动数(元):"""

    NVChangeDueToOperating: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_NVChange', column_name='NVChangeDueToOperating', column_type='decimal(19,4)', nullable=False, chn_name='经营活动产生的基金净值变动数(元)')
    """经营活动产生的基金净值变动数(元):"""

    ApplyingMoney: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_NVChange', column_name='ApplyingMoney', column_type='decimal(19,4)', nullable=False, chn_name='基金申购款(元)')
    """基金申购款(元):"""

    RedemptionMoney: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_NVChange', column_name='RedemptionMoney', column_type='decimal(19,4)', nullable=False, chn_name='基金赎回款(元)')
    """基金赎回款(元):"""

