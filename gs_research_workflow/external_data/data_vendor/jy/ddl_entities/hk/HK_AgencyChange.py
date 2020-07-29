# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_AgencyChange(SQLTableEntity):
    name: str = 'HK_AgencyChange'
    
    chn_name: str = '港股中介机构变动表'
    
    business_unique: str = 'InnerCode,EffectiveDate,EventType,AgenBeforeChange,AgenAfterChange'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.记录港股公司中介机构的变动历史记录数据，包括公司法律顾问、核数师、主要往来银行、股份过户处的变动情况。
2.数据范围：1999年至今。
3.信息来源：港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_AgencyChange', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    AgenAfterChange: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_AgencyChange', column_name='AgenAfterChange', column_type='varchar(200)', nullable=False, chn_name='变更后机构名称')
    """变更后机构名称:"""

    ExpiryDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_AgencyChange', column_name='ExpiryDate', column_type='datetime', nullable=False, chn_name='失效日期')
    """失效日期:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_AgencyChange', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_AgencyChange', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_AgencyChange', column_name='InnerCode', column_type='int', nullable=True, chn_name='证券内部编码')
    """证券内部编码:证券内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_AgencyChange', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_AgencyChange', column_name='InfoSource', column_type='int', nullable=False, chn_name='信息来源')
    """信息来源:信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB=1926，得到信息来源的具体描述：1-审计报告，2-第一季报，3-中期报告，4-第三季报，5-年度报告，6-第二季报，7-第四季报，8-第五季报，9-定期报告，10-申请版本，11-聆讯后资料集，12-招股章程，13-临时公告，14-审计报告(申报稿)，15-公开转..."""

    SMAnnounceDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_AgencyChange', column_name='SMAnnounceDate', column_type='datetime', nullable=False, chn_name='股东大会公告日期')
    """股东大会公告日期:"""

    IfEffected: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_AgencyChange', column_name='IfEffected', column_type='int', nullable=True, chn_name='是否有效')
    """是否有效:是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB =999 and DM in (1,2)，得到是否有效的具体描述：1-是，2-否。"""

    EffectiveDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_AgencyChange', column_name='EffectiveDate', column_type='datetime', nullable=True, chn_name='生效日期')
    """生效日期:"""

    EventType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_AgencyChange', column_name='EventType', column_type='int', nullable=True, chn_name='事项类别')
    """事项类别:事项类别(EventType)与(CT_SystemConst)表中的DM字段关联，令LB=1334，得到事项类别的具体描述：1101-经办人，1106-副经办人，1111-牵头经办人，1116-副牵头经办人，1121-联席经办人，1126-联席牵头经办人，1131-联席副牵头经办人，1136-共同牵头经办人，1141-共同经办人，1146-高级副经办人，1..."""

    AgenBeforeChange: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_AgencyChange', column_name='AgenBeforeChange', column_type='varchar(200)', nullable=False, chn_name='变更前机构名称')
    """变更前机构名称:"""

