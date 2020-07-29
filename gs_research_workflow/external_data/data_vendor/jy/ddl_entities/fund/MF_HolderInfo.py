# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_HolderInfo(SQLTableEntity):
    name: str = 'MF_HolderInfo'
    
    chn_name: str = '公募基金持有人结构信息'
    
    business_unique: str = 'InnerCode,EndDate'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.本表记录基金份额持有人户数、持有人结构，包括机构、个人持有份额的详细数据、占比等。前十大持有的持有份额合计、占比等数据。
2.历史数据：2004年6月起-至今。
3.数据来源：基金公司披露的临时报告。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_HolderInfo', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    IndividualHoldRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_HolderInfo', column_name='IndividualHoldRatio', column_type='decimal(18,6)', nullable=False, chn_name='个人持有比例(%)')
    """个人持有比例(%):"""

    UndefinedHoldShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_HolderInfo', column_name='UndefinedHoldShares', column_type='decimal(18,4)', nullable=False, chn_name='未明确投资者持有份额(份)')
    """未明确投资者持有份额(份):"""

    UndefinedHoldRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_HolderInfo', column_name='UndefinedHoldRatio', column_type='decimal(18,6)', nullable=False, chn_name='未明确投资者持有比例(%)')
    """未明确投资者持有比例(%):"""

    Top10HolderAmount: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_HolderInfo', column_name='Top10HolderAmount', column_type='decimal(18,4)', nullable=False, chn_name='前十大持有人持有份额合计(份)')
    """前十大持有人持有份额合计(份):"""

    Top10HoldersProportion: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_HolderInfo', column_name='Top10HoldersProportion', column_type='decimal(18,4)', nullable=False, chn_name='前十大持有人持有比例合计(%)')
    """前十大持有人持有比例合计(%):前十大持有人持有比例合计（Top10HoldersProportion）=（前十大持有人持有份额合计/基金总份额）*100%"""

    ProfessionalHoldShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_HolderInfo', column_name='ProfessionalHoldShares', column_type='decimal(18,4)', nullable=False, chn_name='基金从业人员持有份额(份)')
    """基金从业人员持有份额(份):"""

    ProfessionalHoldRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_HolderInfo', column_name='ProfessionalHoldRatio', column_type='decimal(18,6)', nullable=False, chn_name='基金从业人员持有比例(%)')
    """基金从业人员持有比例(%):"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_HolderInfo', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新日期')
    """更新日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_HolderInfo', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_HolderInfo', column_name='InnerCode', column_type='int', nullable=True, chn_name='基金内部编码')
    """基金内部编码:基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_HolderInfo', column_name='InfoSource', column_type='varchar(100)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_HolderInfo', column_name='EndDate', column_type='datetime', nullable=False, chn_name='截止日期')
    """截止日期:"""

    HolderAccountNumber: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_HolderInfo', column_name='HolderAccountNumber', column_type='int', nullable=False, chn_name='持有人户数')
    """持有人户数:"""

    AverageHoldShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_HolderInfo', column_name='AverageHoldShares', column_type='decimal(18,4)', nullable=False, chn_name='户均持有份额(份)')
    """户均持有份额(份):"""

    InstitutionHoldShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_HolderInfo', column_name='InstitutionHoldShares', column_type='decimal(18,4)', nullable=False, chn_name='机构持有份额(份)')
    """机构持有份额(份):"""

    InstitutionHoldRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_HolderInfo', column_name='InstitutionHoldRatio', column_type='decimal(18,6)', nullable=False, chn_name='机构持有比例(%)')
    """机构持有比例(%):"""

    IndividualHoldshares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_HolderInfo', column_name='IndividualHoldshares', column_type='decimal(18,4)', nullable=False, chn_name='个人持有份额(份)')
    """个人持有份额(份):"""

