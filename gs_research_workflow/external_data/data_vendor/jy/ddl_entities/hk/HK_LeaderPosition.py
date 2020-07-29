# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_LeaderPosition(SQLTableEntity):
    name: str = 'HK_LeaderPosition'
    
    chn_name: str = '港股领导人任职变动'
    
    business_unique: str = 'CompanyCode,LeaderID,PositionName,InDate'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.记录港股领导人的任职与变动情况，包含主要字段有：信息发布日期、领导人ID、姓名、职位、任职起始日期、任职截止日期、变动原因等。
2.数据范围：2000年至今。 
3.数据来源：港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_LeaderPosition', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    OffDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_LeaderPosition', column_name='OffDate', column_type='datetime', nullable=False, chn_name='任职截止日')
    """任职截止日:"""

    ChangeType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_LeaderPosition', column_name='ChangeType', column_type='int', nullable=False, chn_name='变动原因')
    """变动原因:变动原因(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1338，得到变动原因的具体描述：10-委任，11-调任，21-辞职，23-辞退，25-退休，27-离职，30-逝世，40-换届，43-控股权变动，45-完善治理结构，50-违规或涉案，53-健康原因，60-结束代理，63-股东大会否决，90-其他原因，99-未..."""

    ChangeReason: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_LeaderPosition', column_name='ChangeReason', column_type='varchar(500)', nullable=False, chn_name='变动原因说明')
    """变动原因说明:"""

    IfIn: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_LeaderPosition', column_name='IfIn', column_type='int', nullable=False, chn_name='在任与否')
    """在任与否:在任与否（IfIn）：本字段是固定字段0->否，1->在任"""

    Statement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_LeaderPosition', column_name='Statement', column_type='varchar(500)', nullable=False, chn_name='备注')
    """备注:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_LeaderPosition', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='修改日期')
    """修改日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_LeaderPosition', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_LeaderPosition', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到港股的交易代码、简称等。"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_LeaderPosition', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    LeaderID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_LeaderPosition', column_name='LeaderID', column_type='int', nullable=False, chn_name='领导人ID')
    """领导人ID:"""

    LeaderName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_LeaderPosition', column_name='LeaderName', column_type='varchar(100)', nullable=False, chn_name='姓名')
    """姓名:"""

    PositionName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_LeaderPosition', column_name='PositionName', column_type='varchar(100)', nullable=False, chn_name='职位名称')
    """职位名称:"""

    Position: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_LeaderPosition', column_name='Position', column_type='int', nullable=False, chn_name='职位')
    """职位:职位(Position)与(CT_SystemConst)表中的DM字段关联，令LB = 1344，得到职位的具体描述：1101-执行董事，1103-常务董事，1105-非执行董事，1106-非常务董事，1107-副常务董事，1109-独立非执行董事，1110-独立非常务董事，1113-替任执行董事，1117-替任非执行董事，1121-替任独立非执行董事，1..."""

    PositionType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_LeaderPosition', column_name='PositionType', column_type='int', nullable=False, chn_name='职位类别')
    """职位类别:职位类别(PositionType)与(CT_SystemConst)表中的DM字段关联，令LB = 1420，得到职位类别的具体描述：10-董事会，20-监事会，30-经营层，40-集团，90-其他。"""

    InDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_LeaderPosition', column_name='InDate', column_type='datetime', nullable=False, chn_name='任职起始日')
    """任职起始日:"""

