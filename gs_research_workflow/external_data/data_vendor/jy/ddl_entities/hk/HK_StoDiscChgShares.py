# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_StoDiscChgShares(SQLTableEntity):
    name: str = 'HK_StoDiscChgShares'
    
    chn_name: str = '港股披露权益变动股数'
    
    business_unique: str = 'RID,PosCharacter'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.记录港股权益事件变动前后持股数量信息，包括内容有：持仓类型、事件前持股总数、事件前持股占比、事件后持股总数、事件后持股总数等。该表为港股披露权益系列表的附表之一。 
2.数据范围：1997年至今。
3.数据来源:港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscChgShares', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    RID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscChgShares', column_name='RID', column_type='bigint', nullable=True, chn_name='RID')
    """RID:RID：与“港股披露权益信息（HK_StoDiscInf）”表的ID字段关联"""

    PosCharacter: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscChgShares', column_name='PosCharacter', column_type='int', nullable=True, chn_name='持仓类型')
    """持仓类型:持仓类型(PosCharacter)与(CT_SystemConst)表中的DM字段关联，令LB = 1342，得到持仓类型的具体描述：1-好仓，3-淡仓，9-可供借出股份。"""

    HoldSumBefEvent: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscChgShares', column_name='HoldSumBefEvent', column_type='decimal(18,2)', nullable=False, chn_name='事件前持股总数(股)')
    """事件前持股总数(股):"""

    HRatioBefEvent: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscChgShares', column_name='HRatioBefEvent', column_type='decimal(18,9)', nullable=False, chn_name='事件前持股占比')
    """事件前持股占比:"""

    HoldSumAfEvent: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscChgShares', column_name='HoldSumAfEvent', column_type='decimal(18,2)', nullable=False, chn_name='事件后持股总数(股)')
    """事件后持股总数(股):"""

    HRatioAfEvent: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscChgShares', column_name='HRatioAfEvent', column_type='decimal(18,9)', nullable=False, chn_name='事件后持股占比')
    """事件后持股占比:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscChgShares', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscChgShares', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

