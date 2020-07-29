# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_AssetAllocation(SQLTableEntity):
    name: str = 'MF_AssetAllocation'
    
    chn_name: str = '公募基金资产配置'
    
    business_unique: str = 'InnerCode,ReportDate,AssetTypeCode'
    
    refresh_freq: str = """季更新"""
    
    comment: str = """1.本表记录基金资产的大类配置情况，包括股票、债券、银行存款和清算备付金、其他资产、买入返售证券、卖出回购证券、国债及货币资金、可转换债券等。
2.历史数据：1998年6月起-至今。
3.数据来源：基金公司披露的定期报告。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AssetAllocation', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AssetAllocation', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新日期')
    """更新日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AssetAllocation', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AssetAllocation', column_name='InnerCode', column_type='int', nullable=True, chn_name='基金内部编码')
    """基金内部编码:基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AssetAllocation', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    ReportDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AssetAllocation', column_name='ReportDate', column_type='datetime', nullable=True, chn_name='报告期')
    """报告期:"""

    AssetTypeCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AssetAllocation', column_name='AssetTypeCode', column_type='int', nullable=False, chn_name='资产种类代码')
    """资产种类代码:资产种类代码(AssetTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 302，得到资产种类代码的具体描述：10-权益类投资，30-固定收益类投资，40-金融衍生品投资，50-买入返售金融资产，10001-行业投资合计，10002-国债及货币资金，10003-非国债债券，10004-指数投资，10005-积极投资，1000..."""

    AssetType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AssetAllocation', column_name='AssetType', column_type='varchar(50)', nullable=True, chn_name='资产种类')
    """资产种类:"""

    MarketValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AssetAllocation', column_name='MarketValue', column_type='decimal(19,4)', nullable=False, chn_name='资产市值(元)')
    """资产市值(元):"""

    RatioInTotalAsset: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AssetAllocation', column_name='RatioInTotalAsset', column_type='decimal(18,6)', nullable=False, chn_name='占资产总值比例')
    """占资产总值比例:"""

    RatioInNV: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_AssetAllocation', column_name='RatioInNV', column_type='decimal(18,6)', nullable=False, chn_name='占资产净值比例')
    """占资产净值比例:"""

