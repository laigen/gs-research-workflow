# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_IncentivePlanImplement(SQLTableEntity):
    name: str = 'LC_IncentivePlanImplement'
    
    chn_name: str = '激励计划实施'
    
    business_unique: str = 'CompanyCode,IncentiveMode,InitialInfoPublDate,EffectiveDate'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.收录上市公司激励计划的实施结果信息，包括实施日期、激励权益数量、兑换比例、激励股票数量、激励价格、激励金额等指标。
2.数据范围：2005-至今
3.信息来源：上市公司公告"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlanImplement', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    SharesNum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlanImplement', column_name='SharesNum', column_type='decimal(18,9)', nullable=False, chn_name='激励股票数量(万股)')
    """激励股票数量(万股):"""

    IncentiveStockProportion: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlanImplement', column_name='IncentiveStockProportion', column_type='decimal(18,9)', nullable=False, chn_name='激励股本占总股本比例(%)')
    """激励股本占总股本比例(%):"""

    IncentivePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlanImplement', column_name='IncentivePrice', column_type='decimal(19,4)', nullable=False, chn_name='激励价格(元)')
    """激励价格(元):"""

    IncentiveSum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlanImplement', column_name='IncentiveSum', column_type='decimal(18,9)', nullable=False, chn_name='激励金额(万元)')
    """激励金额(万元):"""

    ChangeStatement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlanImplement', column_name='ChangeStatement', column_type='int', nullable=False, chn_name='变动原因类别')
    """变动原因类别:变动原因类别(ChangeStatement)与(CT_SystemConst)表中的DM字段关联，令LB = 1323 AND DM IN (1,2,3,31,33,35)，得到变动原因类别的具体描述：1-标的派现，2-标的送转，3-标的送转派，31-方案变更，33-激励基金购股，35-方案实施。"""

    ChangeType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlanImplement', column_name='ChangeType', column_type='varchar(200)', nullable=False, chn_name='变动原因说明')
    """变动原因说明:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlanImplement', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='修改日期')
    """修改日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlanImplement', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlanImplement', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlanImplement', column_name='InnerCode', column_type='int', nullable=False, chn_name='证券内部编码')
    """证券内部编码:证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到股票的交易代码、简称等。"""

    IncentiveMode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlanImplement', column_name='IncentiveMode', column_type='int', nullable=True, chn_name='激励模式')
    """激励模式:激励模式(IncentiveMode)与(CT_SystemConst)表中的DM字段关联，令LB = 1400，得到激励模式的具体描述：10-限制性股票，13-业绩股票，15-管理层持股，21-股票期权，23-股票增值权，25-虚拟股票，31-激励基金，90-未明确，99-其他。"""

    InitialInfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlanImplement', column_name='InitialInfoPublDate', column_type='datetime', nullable=True, chn_name='首次信息发布日期')
    """首次信息发布日期:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlanImplement', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    EffectiveDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlanImplement', column_name='EffectiveDate', column_type='datetime', nullable=True, chn_name='实施日期')
    """实施日期:"""

    RightsNum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlanImplement', column_name='RightsNum', column_type='decimal(18,9)', nullable=False, chn_name='激励权益数量(万份)')
    """激励权益数量(万份):"""

    ShareRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncentivePlanImplement', column_name='ShareRatio', column_type='decimal(18,9)', nullable=False, chn_name='兑换比例(1份：X股)')
    """兑换比例(1份：X股):"""

