# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_StoDiscDerRights(SQLTableEntity):
    name: str = 'HK_StoDiscDerRights'
    
    chn_name: str = '港股披露衍生权益'
    
    business_unique: str = 'RID,PosCharacter,HoldStatus,EDay,EndDateOfExercise'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.记录港股披露权益持有人持有衍生权益的进一步信息，包含内容有：持仓类型、切合身份、行权日期、行权价格、转让价格、授予价格、股份数目等。该表为港股披露权益系列表的附表之一。
2.数据范围：1997年至今。
3.数据来源：港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscDerRights', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    ShareAmount: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscDerRights', column_name='ShareAmount', column_type='bigint', nullable=False, chn_name='股份数目(股)')
    """股份数目(股):"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscDerRights', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscDerRights', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    RID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscDerRights', column_name='RID', column_type='bigint', nullable=True, chn_name='RID')
    """RID:RID：与“港股披露权益信息（HK_StoDiscInf）”表的ID字段关联"""

    PosCharacter: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscDerRights', column_name='PosCharacter', column_type='int', nullable=True, chn_name='持仓类型')
    """持仓类型:持仓类型(PosCharacter)与(CT_SystemConst)表中的DM字段关联，令LB=1342，得到持仓类型的具体描述：1-好仓，3-淡仓，9-可供借出股份。"""

    HoldStatus: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscDerRights', column_name='HoldStatus', column_type='int', nullable=True, chn_name='切合身份')
    """切合身份:切合身份（HoldStatus）与“系统常量表（CT_SystemConst）”中的“常量代码（DM）”关联，令“LB=1701”，得到切合身份的具体描述。因港交所网页内容做过优化，在2017年7月3日前后使用的权益身份编码不一致。其中：2017年7月3日前，201-实益拥有人，202-投资经理，203-对股分持有保证权益的人，204-你未满18岁的子女或配..."""

    EDay: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscDerRights', column_name='EDay', column_type='datetime', nullable=False, chn_name='行权起始日')
    """行权起始日:"""

    EndDateOfExercise: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscDerRights', column_name='EndDateOfExercise', column_type='datetime', nullable=False, chn_name='行权截止日')
    """行权截止日:"""

    ExercisePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscDerRights', column_name='ExercisePrice', column_type='decimal(18,9)', nullable=False, chn_name='行权价格(元)')
    """行权价格(元):"""

    TransferPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscDerRights', column_name='TransferPrice', column_type='decimal(18,9)', nullable=False, chn_name='转让价格(元)')
    """转让价格(元):"""

    GrantPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscDerRights', column_name='GrantPrice', column_type='decimal(18,9)', nullable=False, chn_name='授予价格(元)')
    """授予价格(元):"""

