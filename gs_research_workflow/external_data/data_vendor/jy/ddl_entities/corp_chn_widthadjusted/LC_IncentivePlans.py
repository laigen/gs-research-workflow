# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_IncentivePlans(SQLTableEntity):
    name: str = 'LC_IncentivePlans'
    
    chn_name: str = '激励计划'
    
    business_unique: str = 'CompanyCode,InitialInfoPublDate,IncentiveModeCode'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.收录公告中披露的公司实行股权激励计划方案的要素信息，包括股东大会公告日期、授予日、事件进程、方案说明、激励模式、行权条件等指标。
2.数据范围：2005-至今
3.信息来源：上市公司公告"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlans', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    ProjectStatement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlans', column_name='ProjectStatement', column_type='text', nullable=False, chn_name='方案说明')
    """方案说明:"""

    IncentiveModeCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlans', column_name='IncentiveModeCode', column_type='int', nullable=False, chn_name='激励模式代码')
    """激励模式代码:激励模式代码(IncentiveModeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1400，得到激励模式代码的具体描述：10-限制性股票，13-业绩股票，15-管理层持股，21-股票期权，23-股票增值权，25-虚拟股票，31-激励基金，90-未明确，99-其他。"""

    IncentiveMode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlans', column_name='IncentiveMode', column_type='varchar(50)', nullable=False, chn_name='激励模式')
    """激励模式:"""

    StockType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlans', column_name='StockType', column_type='varchar(50)', nullable=False, chn_name='股票种类')
    """股票种类:"""

    StockSourceCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlans', column_name='StockSourceCode', column_type='int', nullable=False, chn_name='股票来源代码')
    """股票来源代码:股票来源代码(StockSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1402，得到股票来源代码的具体描述：11-发行股份，13-回购股份，15-存量股份，99-其他来源。"""

    StockSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlans', column_name='StockSource', column_type='varchar(50)', nullable=False, chn_name='股票来源')
    """股票来源:"""

    PricingMethod: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlans', column_name='PricingMethod', column_type='varchar(2000)', nullable=False, chn_name='价格确定方法')
    """价格确定方法:"""

    PeriodOfValidity: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlans', column_name='PeriodOfValidity', column_type='int', nullable=False, chn_name='有效期(年)')
    """有效期(年):"""

    AuthorizationTimes: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlans', column_name='AuthorizationTimes', column_type='int', nullable=False, chn_name='授权次数')
    """授权次数:"""

    ExercisedCondition: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlans', column_name='ExercisedCondition', column_type='varchar(2000)', nullable=False, chn_name='行权条件')
    """行权条件:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlans', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlans', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlans', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InitialInfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlans', column_name='InitialInfoPublDate', column_type='datetime', nullable=False, chn_name='首次信息发布日期')
    """首次信息发布日期:"""

    DMAnnounceDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlans', column_name='DMAnnounceDate', column_type='datetime', nullable=False, chn_name='董事会公告日期')
    """董事会公告日期:"""

    SMAnnounceDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlans', column_name='SMAnnounceDate', column_type='datetime', nullable=False, chn_name='股东大会公告日期')
    """股东大会公告日期:"""

    InitialawardPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlans', column_name='InitialawardPublDate', column_type='datetime', nullable=False, chn_name='首次授予确定公告日')
    """首次授予确定公告日:"""

    InitialawardDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlans', column_name='InitialawardDate', column_type='datetime', nullable=False, chn_name='首次授予日')
    """首次授予日:"""

    EventProcedureCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlans', column_name='EventProcedureCode', column_type='int', nullable=False, chn_name='事件进程代码')
    """事件进程代码:事件进程代码(EventProcedureCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1059，得到事件进程代码的具体描述：1000-意向，1001-预案，1004-决案，1007-否决，1010-申请，1013-批准，1016-未实施终止，1019-实施中，1022-实施完成，1025-解除，1028-到期，1041-续签，..."""

    EventProcedure: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlans', column_name='EventProcedure', column_type='varchar(50)', nullable=False, chn_name='事件进程')
    """事件进程:"""

