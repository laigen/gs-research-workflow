# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_MainFinancialIndex(SQLTableEntity):
    name: str = 'MF_MainFinancialIndex'
    
    chn_name: str = '公募基金报告期主要财务指标'
    
    business_unique: str = 'InnerCode,EndDate'
    
    refresh_freq: str = """半年更新"""
    
    comment: str = """1.本表记录包含新会计准则下，基金在年报或半年报中披露的基金主要财务指标，并跟据新旧会计准则的科目对应关系，收录了指标的历史对应数据。
2.若某个报告期的数据有多次调整，则该表展示最新调整数据。
3.该表中各财务指标下数据对应的货币单位均为人民币元。
4.历史数据：1998年3月起-至今。
5.信息来源：基金公司披露的定期报告。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndex', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    TotalProfitPerShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndex', column_name='TotalProfitPerShare', column_type='decimal(18,6)', nullable=False, chn_name='加权平均份额本期利润(元)')
    """加权平均份额本期利润(元):"""

    DistributableProfits: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndex', column_name='DistributableProfits', column_type='decimal(19,4)', nullable=False, chn_name='期末可供分配利润(元)')
    """期末可供分配利润(元):"""

    DistriProfitsPShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndex', column_name='DistriProfitsPShare', column_type='decimal(18,6)', nullable=False, chn_name='期末可供分配份额利润(元)')
    """期末可供分配份额利润(元):"""

    NetAssetsValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndex', column_name='NetAssetsValue', column_type='decimal(19,4)', nullable=False, chn_name='期末基金资产净值(元)')
    """期末基金资产净值(元):"""

    NVPerShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndex', column_name='NVPerShare', column_type='decimal(18,6)', nullable=False, chn_name='期末基金份额净值(元)')
    """期末基金份额净值(元):"""

    WANVProfitRate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndex', column_name='WANVProfitRate', column_type='decimal(18,6)', nullable=False, chn_name='加权平均净值利润率(%)')
    """加权平均净值利润率(%):"""

    UnitNVGrowthRate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndex', column_name='UnitNVGrowthRate', column_type='decimal(18,6)', nullable=False, chn_name='本期份额净值增长率(%)')
    """本期份额净值增长率(%):"""

    UnitAccumulativeNVGR: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndex', column_name='UnitAccumulativeNVGR', column_type='decimal(18,6)', nullable=False, chn_name='份额累计净值增长率(%)')
    """份额累计净值增长率(%):"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndex', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新日期')
    """更新日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndex', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndex', column_name='InnerCode', column_type='int', nullable=True, chn_name='基金内部编码')
    """基金内部编码:基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndex', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndex', column_name='InfoSource', column_type='varchar(100)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    BulletinType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndex', column_name='BulletinType', column_type='int', nullable=False, chn_name='公告类别')
    """公告类别:公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311，得到公告类别的具体描述：10-发行上市书，20-定期报告，30-业绩快报，50-章程制度，70-临时公告，90-交易所通报，91-交易所临时停(复)牌公告，99-其他。"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndex', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    AccountingStandards: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndex', column_name='AccountingStandards', column_type='int', nullable=False, chn_name='会计准则')
    """会计准则:会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 1455，得到会计准则的具体描述：1-新会计准则(2007)，9-旧会计准则。"""

    TotalProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndex', column_name='TotalProfit', column_type='decimal(19,4)', nullable=False, chn_name='本期利润(元)')
    """本期利润(元):"""

    NetIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_MainFinancialIndex', column_name='NetIncome', column_type='decimal(19,4)', nullable=False, chn_name='本期利润扣减本期公允价值变动损益后的净额(元)')
    """本期利润扣减本期公允价值变动损益后的净额(元):"""

