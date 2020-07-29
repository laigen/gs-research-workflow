# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_StoDiscHoldIdtity(SQLTableEntity):
    name: str = 'HK_StoDiscHoldIdtity'
    
    chn_name: str = '港股披露权益持有身份'
    
    business_unique: str = 'RID,PosCharacter,HoldStatus'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.记录港股披露权益权益人已何种身份持有相关权益信息，包括内容有：持股类型、切合身份、股份数目等内容。该表为港股披露权益系列表的附表之一。
2.数据范围：1997年至今。
3.数据来源：港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscHoldIdtity', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    RID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscHoldIdtity', column_name='RID', column_type='bigint', nullable=True, chn_name='RID')
    """RID:RID：与“港股披露权益信息（HK_StoDiscInf）”表的ID字段关联"""

    PosCharacter: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscHoldIdtity', column_name='PosCharacter', column_type='int', nullable=True, chn_name='持仓类型')
    """持仓类型:持仓类型(PosCharacter)与(CT_SystemConst)表中的DM字段关联，令LB=1342，得到持仓类型的具体描述：1-好仓，3-淡仓，9-可供借出股份。"""

    HoldStatus: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscHoldIdtity', column_name='HoldStatus', column_type='int', nullable=True, chn_name='切合身份')
    """切合身份:切合身份（HoldStatus）与“系统常量表（CT_SystemConst）”中的“常量代码（DM）”关联，令“LB=1701”，得到切合身份的具体描述。因港交所网页内容做过优化，在2017年7月3日前后使用的权益身份编码不一致。其中：2017年7月3日前，201-实益拥有人，202-投资经理，203-对股分持有保证权益的人，204-你未满18岁的子女或配..."""

    ShareAmount: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscHoldIdtity', column_name='ShareAmount', column_type='decimal(18,2)', nullable=False, chn_name='股份数目(股)')
    """股份数目(股):"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscHoldIdtity', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscHoldIdtity', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

