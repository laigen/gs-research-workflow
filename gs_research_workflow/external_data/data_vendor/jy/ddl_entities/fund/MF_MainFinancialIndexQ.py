# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_MainFinancialIndexQ(SQLTableEntity):
    name: str = 'MF_MainFinancialIndexQ'
    
    chn_name: str = '公募基金主要财务指标(季报)'
    
    business_unique: str = 'InnerCode,EndDate'
    
    refresh_freq: str = """季更新"""
    
    comment: str = """1.收录基金季报披露的基金主要财务指标，主要有基金的本期利润、期末单位净值、期末净资产值等数据。
2.历史数据：2004年6月起-至今。
3.信息来源：基金公司披露的定期报告。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndexQ', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    NetIncomePerShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndexQ', column_name='NetIncomePerShare', column_type='decimal(18,6)', nullable=False, chn_name='份额净收益')
    """份额净收益:"""

    NetAssetsValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndexQ', column_name='NetAssetsValue', column_type='decimal(19,4)', nullable=False, chn_name='期末基金资产净值')
    """期末基金资产净值:"""

    NVPerShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndexQ', column_name='NVPerShare', column_type='decimal(19,4)', nullable=False, chn_name='期末基金份额净值')
    """期末基金份额净值:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndexQ', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新日期')
    """更新日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndexQ', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndexQ', column_name='InnerCode', column_type='int', nullable=True, chn_name='基金内部编码')
    """基金内部编码:基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndexQ', column_name='InfoSource', column_type='int', nullable=False, chn_name='信息来源')
    """信息来源:信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB = 1032，得到信息来源的具体描述：1-招股说明书，2-招股意向书，3-配股说明书，4-上市公告书，5-年度报告，6-中期报告，7-公司章程，8-增发新股招股说明书，9-增发新股招股意向书，10-增发新股上市公告书，11-可转换债券募集说明书，12-可转换债券上市..."""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndexQ', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndexQ', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    TotalProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndexQ', column_name='TotalProfit', column_type='decimal(19,4)', nullable=False, chn_name='基金本期利润')
    """基金本期利润:"""

    NetIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndexQ', column_name='NetIncome', column_type='decimal(19,4)', nullable=False, chn_name='本期利润扣除本期公允价值变动损益后的净额')
    """本期利润扣除本期公允价值变动损益后的净额:"""

    FairValueChangeIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndexQ', column_name='FairValueChangeIncome', column_type='decimal(19,4)', nullable=False, chn_name='公允价值变动损益')
    """公允价值变动损益:"""

    TotalProfitPerShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndexQ', column_name='TotalProfitPerShare', column_type='decimal(19,4)', nullable=False, chn_name='加权平均基金份额本期利润')
    """加权平均基金份额本期利润:"""

