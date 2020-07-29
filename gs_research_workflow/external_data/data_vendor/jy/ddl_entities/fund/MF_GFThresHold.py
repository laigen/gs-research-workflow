# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_GFThresHold(SQLTableEntity):
    name: str = 'MF_GFThresHold'
    
    chn_name: str = '公募基金_分级基金阀值'
    
    business_unique: str = 'InnerCode,BeginDate,ThresHoldType,ReLation'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.记录分级基金不定期折算的阀值，即达到这个值，分级基金将进行上折或下折的操作。尤其是下折的操作，会对投资者产生较大的影响。
2.历史数据：2007年7月起-至今。
3.数据来源：基金产品招募说明书。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GFThresHold', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    SplitType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GFThresHold', column_name='SplitType', column_type='int', nullable=False, chn_name='阀值折算方式')
    """阀值折算方式:"""

    RelatedInnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GFThresHold', column_name='RelatedInnerCode', column_type='int', nullable=False, chn_name='比较基金代码')
    """比较基金代码:比较基金代码（RelatedInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    TrampShareCon: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GFThresHold', column_name='TrampShareCon', column_type='varchar(1000)', nullable=False, chn_name='份额折算说明')
    """份额折算说明:"""

    IfEffected: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GFThresHold', column_name='IfEffected', column_type='int', nullable=True, chn_name='是否有效')
    """是否有效:是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否有效的具体描述：1-是，2-否。"""

    Remark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GFThresHold', column_name='Remark', column_type='varchar(1000)', nullable=False, chn_name='备注')
    """备注:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GFThresHold', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GFThresHold', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GFThresHold', column_name='InnerCode', column_type='int', nullable=True, chn_name='基金内部编码')
    """基金内部编码:基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GFThresHold', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='公告日期')
    """公告日期:"""

    BeginDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GFThresHold', column_name='BeginDate', column_type='datetime', nullable=True, chn_name='起始日期')
    """起始日期:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GFThresHold', column_name='EndDate', column_type='datetime', nullable=False, chn_name='截止日期')
    """截止日期:"""

    ThresHoldType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GFThresHold', column_name='ThresHoldType', column_type='int', nullable=False, chn_name='阀值类型')
    """阀值类型:阀值类型（ThresHoldType）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，“LB=1873”，得到“阀值类型”描述等。1-固定净值，2-倍数"""

    ReLation: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GFThresHold', column_name='ReLation', column_type='int', nullable=False, chn_name='条件关系')
    """条件关系:条件关系(ReLation)与(CT_SystemConst)表中的DM字段关联，令LB = 1872，得到条件关系的具体描述：1-大于等于，2-大于，3-小于等于，4-小于。"""

    ThresHold: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GFThresHold', column_name='ThresHold', column_type='decimal(9,6)', nullable=False, chn_name='阀值')
    """阀值:"""

    TriggerDays: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GFThresHold', column_name='TriggerDays', column_type='int', nullable=False, chn_name='触发所需天数(日)')
    """触发所需天数(日):"""

