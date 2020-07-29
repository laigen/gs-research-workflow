# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_AshareIssueCostPlaned(SQLTableEntity):
    name: str = 'LC_AshareIssueCostPlaned'
    
    chn_name: str = 'A股拟发行费用'
    
    business_unique: str = '与LC_AShareIPO表关联使用'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.收录即将上市的A股的招股意向书中的拟发行费用，包括费用总额、承销费用、承销费用比例、保荐费用、注册会计师费用等。
2.信息来源：招股意向书"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIssueCostPlaned', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    CPAFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIssueCostPlaned', column_name='CPAFee', column_type='decimal(19,4)', nullable=False, chn_name='注册会计师费用(元)')
    """注册会计师费用(元):"""

    AssetAppraisalFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIssueCostPlaned', column_name='AssetAppraisalFee', column_type='decimal(19,4)', nullable=False, chn_name='资产评估费用(元)')
    """资产评估费用(元):"""

    AttorneyFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIssueCostPlaned', column_name='AttorneyFee', column_type='decimal(19,4)', nullable=False, chn_name='律师费用(元)')
    """律师费用(元):"""

    DisclosureFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIssueCostPlaned', column_name='DisclosureFee', column_type='decimal(19,4)', nullable=False, chn_name='信息披露费用(元)')
    """信息披露费用(元):"""

    OtherFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIssueCostPlaned', column_name='OtherFee', column_type='decimal(19,4)', nullable=False, chn_name='其他费用(元)')
    """其他费用(元):"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIssueCostPlaned', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIssueCostPlaned', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    RID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIssueCostPlaned', column_name='RID', column_type='bigint', nullable=True, chn_name='RID')
    """RID:RID：与LC_AShareIPO（A股发行与上市）表ID字段关联。"""

    IPOProceeds: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIssueCostPlaned', column_name='IPOProceeds', column_type='decimal(19,4)', nullable=False, chn_name='募集资金总额(元)')
    """募集资金总额(元):"""

    IPONetProceeds: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIssueCostPlaned', column_name='IPONetProceeds', column_type='decimal(19,4)', nullable=False, chn_name='募集资金净额(元)')
    """募集资金净额(元):"""

    IssueCost: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIssueCostPlaned', column_name='IssueCost', column_type='decimal(19,4)', nullable=False, chn_name='费用总额(元)')
    """费用总额(元):"""

    UnderwritingFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIssueCostPlaned', column_name='UnderwritingFee', column_type='decimal(19,4)', nullable=False, chn_name='承销费用(元)')
    """承销费用(元):"""

    UnderwritingFeeRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIssueCostPlaned', column_name='UnderwritingFeeRatio', column_type='decimal(6,4)', nullable=False, chn_name='承销费用比例(%)')
    """承销费用比例(%):"""

    MinUnderwritingFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIssueCostPlaned', column_name='MinUnderwritingFee', column_type='decimal(19,4)', nullable=False, chn_name='承销费用下限(元)')
    """承销费用下限(元):"""

    SponsorFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIssueCostPlaned', column_name='SponsorFee', column_type='decimal(19,4)', nullable=False, chn_name='保荐费用(元)')
    """保荐费用(元):"""

