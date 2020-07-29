# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_CodeRelationshipNew(SQLTableEntity):
    name: str = 'MF_CodeRelationshipNew'
    
    chn_name: str = '公募基金代码关联(新)'
    
    business_unique: str = 'InnerCode,CodeDefine,RelatedInnerCode,StartDate'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.本表收录了聚源整理的分级基金的关联代码、复制型基金的关联代码、封转开基金代码对应关系、基金与其收益线对应关系等信息。
2.历史数据：2001年9月起-至今。
3.信息来源：基金公司官网披露的产品说明书、临时公告等。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_CodeRelationshipNew', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    IfEffected: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_CodeRelationshipNew', column_name='IfEffected', column_type='int', nullable=False, chn_name='是否有效')
    """是否有效:是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否有效的具体描述：1-是，2-否。"""

    Remarks: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_CodeRelationshipNew', column_name='Remarks', column_type='varchar(500)', nullable=False, chn_name='备注说明')
    """备注说明:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_CodeRelationshipNew', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_CodeRelationshipNew', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_CodeRelationshipNew', column_name='InnerCode', column_type='int', nullable=True, chn_name='内部编码')
    """内部编码:内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    CodeDefine: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_CodeRelationshipNew', column_name='CodeDefine', column_type='int', nullable=True, chn_name='代码关联方式')
    """代码关联方式:代码关联方式（CodeDefine）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令“LB=1350”，得到具体关联方式。10-跨市场公司关联，21-同一基金分级关联，22-母子基金分级关联，23-复制型基金关联，24-联接基金关联，25-封转开基金对应，26-同一基金保本期关联，27-基金与收益线对应，28-开转封基金对应，2..."""

    SndCodeDefine: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_CodeRelationshipNew', column_name='SndCodeDefine', column_type='int', nullable=False, chn_name='二级关联方式')
    """二级关联方式:二级关联方式(SndCodeDefine)与(CT_SystemConst)表中的DM字段关联，令LB=1350，得到二级关联方式的具体描述：2101-同一基金杠杆分级关联，2102-同一基金母子子代码关联，2103-同一基金按不同结转方式关联，2104-同一基金按份额赎回不同处理方式关联，2105-同一基金按份额登记机构不同关联，2106-同一基金按费用不..."""

    TrdCodeDefine: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_CodeRelationshipNew', column_name='TrdCodeDefine', column_type='int', nullable=False, chn_name='三级关联方式')
    """三级关联方式:三级关联方式(TrdCodeDefine)与(CT_SystemConst)表中的DM字段关联，令LB=1350，得到三级关联方式的具体描述：210601-因不同赎回费率关联，210602-因不同申购份额或持有累计份额关联，210603-因不同申购费率关联，210604-因不同持有期限关联，210605-因不同销售渠道关联。"""

    RelatedInnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_CodeRelationshipNew', column_name='RelatedInnerCode', column_type='int', nullable=False, chn_name='关联代码内部编码')
    """关联代码内部编码:关联代码内部编码（RelatedInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得基金的交易代码、简称等。"""

    RelatedCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_CodeRelationshipNew', column_name='RelatedCode', column_type='varchar(10)', nullable=False, chn_name='对应代码')
    """对应代码:"""

    StartDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_CodeRelationshipNew', column_name='StartDate', column_type='datetime', nullable=False, chn_name='启用日期')
    """启用日期:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_CodeRelationshipNew', column_name='EndDate', column_type='datetime', nullable=False, chn_name='终止日期')
    """终止日期:"""

