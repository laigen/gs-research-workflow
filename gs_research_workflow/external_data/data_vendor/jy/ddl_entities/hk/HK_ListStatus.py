# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_ListStatus(SQLTableEntity):
    name: str = 'HK_ListStatus'
    
    chn_name: str = '港股上市状态变动表'
    
    business_unique: str = 'InnerCode,ChangeDate,ChangeType'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.记录港股公司上市流程的变动历史记录数据，包括上市、暂停上市（长期暂停）、恢复上市、终止上市等的变动情况。                       
2.数据范围：1999年至今。
3.信息来源：港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ListStatus', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ListStatus', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ListStatus', column_name='InnerCode', column_type='int', nullable=True, chn_name='证券内部编码')
    """证券内部编码:证券内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ListStatus', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ListStatus', column_name='InfoSource', column_type='int', nullable=False, chn_name='信息来源')
    """信息来源:信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB=1926，得到信息来源的具体描述：1-审计报告，2-第一季报，3-中期报告，4-第三季报，5-年度报告，6-第二季报，7-第四季报，8-第五季报，9-定期报告，10-申请版本，11-聆讯后资料集，12-招股章程，13-临时公告，14-审计报告(申报稿)，15-公开转..."""

    SMAnnounceDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ListStatus', column_name='SMAnnounceDate', column_type='datetime', nullable=False, chn_name='股东大会公告日期')
    """股东大会公告日期:"""

    IfEffected: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ListStatus', column_name='IfEffected', column_type='int', nullable=True, chn_name='是否有效')
    """是否有效:是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB=999 and DM in (1,2)，得到是否有效的具体描述：1-是，2-否。"""

    ChangeType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ListStatus', column_name='ChangeType', column_type='int', nullable=True, chn_name='变更类型')
    """变更类型:变更类型(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB=1184，得到变更类型的具体描述：1-上市，2-暂停上市，3-恢复上市，4-终止上市，5-摘牌，6-退市整理期，9-其它，11-开放日常申购，12-开放日常赎回，13-暂停日常申购(前端)，14-暂停日常赎回，15-恢复日常申购(前端)，16-恢复日常赎回，17-开..."""

    ChangeDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ListStatus', column_name='ChangeDate', column_type='datetime', nullable=True, chn_name='变更日期')
    """变更日期:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ListStatus', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

