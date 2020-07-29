# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_StoDiscDetailInf(SQLTableEntity):
    name: str = 'HK_StoDiscDetailInf'
    
    chn_name: str = '港股披露权益详情'
    
    business_unique: str = 'RID,PosCharacter'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.记录港股披露权益相关事件的详细信息，包括内容有：持仓类型、持股变动原因、买卖涉及股数、买卖价格等。该表为港股披露权益系列表的附表之一。
2.数据范围：1997年至今。
3.信息来源：港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscDetailInf', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    AvePPSOnExchg: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscDetailInf', column_name='AvePPSOnExchg', column_type='decimal(18,9)', nullable=False, chn_name='场内每股平均价(元)')
    """场内每股平均价(元):"""

    AConPSOffExchg: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscDetailInf', column_name='AConPSOffExchg', column_type='decimal(18,9)', nullable=False, chn_name='场外每股平均代价(元)')
    """场外每股平均代价(元):"""

    CCodeOffExchg: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscDetailInf', column_name='CCodeOffExchg', column_type='int', nullable=False, chn_name='场外代价代号')
    """场外代价代号:场外代价代号（CCodeOffExchg）与“系统常量表（CT_SystemConst）”中的“常量代码（DM）”关联，令“LB=1701”，得到场外代价代号的具体描述。因港交所网页内容做过优化，在2017年7月3日前后使用的场外代价代号不一致。其中：2017年7月3日前，301-现金，302-现金以外的资产，303-交还股分或债权证权利，304-服务；20..."""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscDetailInf', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscDetailInf', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    RID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscDetailInf', column_name='RID', column_type='bigint', nullable=True, chn_name='RID')
    """RID:RID：与“港股披露权益信息（HK_StoDiscInf）”表的ID字段关联"""

    PosCharacter: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscDetailInf', column_name='PosCharacter', column_type='int', nullable=True, chn_name='持仓类型')
    """持仓类型:持仓类型(PosCharacter)与(CT_SystemConst)表中的DM字段关联，令LB=1342，得到持仓类型的具体描述：1-好仓，3-淡仓，9-可供借出股份。"""

    EventCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscDetailInf', column_name='EventCode', column_type='int', nullable=False, chn_name='事件代码')
    """事件代码:事件代码（EventCode）与“系统常量表（CT_SystemConst）”中的“常量代码（DM）”关联，令“LB = 1701”，得
       到事件代码的具体描述。因港交所网页内容做过优化，在2017年7月3日前后使用的事件代码不一致。其中： 2017年7月3日后， 1101-你买入了股份，1102-你获给予股份，1106-你成为了持有股份权益的信..."""

    BefEventStas: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscDetailInf', column_name='BefEventStas', column_type='int', nullable=False, chn_name='事件前身份')
    """事件前身份:事件前身份（BefEventStas）与“系统常量表（CT_SystemConst）”中的“常量代码（DM）”关联，令“LB = 1701”，得到事件前身份的具体描述。因港交所网页内容做过优化，在2017年7月3日前后使用的权益身份编码不一致。其中：2017年7月3日前，201-实益拥有人，202-投资经理，203-对股分持有保证权益的人，204-你未满18..."""

    AfEventStas: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscDetailInf', column_name='AfEventStas', column_type='int', nullable=False, chn_name='事件后身份')
    """事件后身份:事件后身份（AfEventStas）与“系统常量表（CT_SystemConst）”中的“常量代码（DM）”关联，令“LB=1701”，得到事件后身份的具体描述。因港交所网页内容做过优化，在2017年7月3日前后使用的权益身份编码不一致。其中：2017年7月3日前，201-实益拥有人，202-投资经理，203-对股分持有保证权益的人，204-你未满18岁的子..."""

    InvolvedShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscDetailInf', column_name='InvolvedShares', column_type='bigint', nullable=False, chn_name='买卖涉及股数(股)')
    """买卖涉及股数(股):"""

    Currency: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscDetailInf', column_name='Currency', column_type='int', nullable=False, chn_name='交易货币')
    """交易货币:交易货币(Currency)与(CT_SystemConst)表中的DM字段关联，令LB=1068 and DM in (1000,1100,1420)，得到交易货币的具体描述：1000-美元，1100-港元，1420-人民币元。"""

    HPriPSOnExchg: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscDetailInf', column_name='HPriPSOnExchg', column_type='decimal(18,9)', nullable=False, chn_name='场内每股最高价(元)')
    """场内每股最高价(元):"""

