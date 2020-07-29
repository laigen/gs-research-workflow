# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_SuspendResumption(SQLTableEntity):
    name: str = 'LC_SuspendResumption'
    
    chn_name: str = '停牌复牌表'
    
    business_unique: str = 'InnerCode,SuspendDate,SuspendTime'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.收录上市公司/基金/债券停牌复牌信息，如停牌日期、停牌时间、停牌原因、停牌事项说明、停牌期限、复牌日期、复牌时间、复牌事项说明等，包括盘中临时停牌。
2.数据范围：2008.04-至今
2.信息来源：上海证券交易所、深圳证券交易所"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SuspendResumption', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    ResumptionDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SuspendResumption', column_name='ResumptionDate', column_type='datetime', nullable=False, chn_name='复牌日期')
    """复牌日期:"""

    ResumptionTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SuspendResumption', column_name='ResumptionTime', column_type='varchar(30)', nullable=False, chn_name='复牌时间')
    """复牌时间:"""

    ResumptionStatement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SuspendResumption', column_name='ResumptionStatement', column_type='varchar(110)', nullable=False, chn_name='复牌事项说明')
    """复牌事项说明:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SuspendResumption', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SuspendResumption', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SuspendResumption', column_name='InnerCode', column_type='int', nullable=True, chn_name='内部编码')
    """内部编码:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SuspendResumption', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SuspendResumption', column_name='InfoSource', column_type='int', nullable=False, chn_name='信息来源')
    """信息来源:"""

    SuspendDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SuspendResumption', column_name='SuspendDate', column_type='datetime', nullable=True, chn_name='停牌日期')
    """停牌日期:"""

    SuspendTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SuspendResumption', column_name='SuspendTime', column_type='varchar(30)', nullable=True, chn_name='停牌时间')
    """停牌时间:"""

    SuspendReason: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SuspendResumption', column_name='SuspendReason', column_type='varchar(110)', nullable=False, chn_name='停牌原因')
    """停牌原因:"""

    SuspendStatement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SuspendResumption', column_name='SuspendStatement', column_type='int', nullable=False, chn_name='停牌事项说明')
    """停牌事项说明:停牌事项说明(SuspendStatement)与(CT_SystemConst)表中的DM字段关联，令LB = 1654，得到停牌事项说明的具体描述：101-临时停牌，102-召开股东大会，103-重大事项，104-其它公告（停牌），105-交易异常波动，106-澄清公告，107-撤销其他特别处理公告，108-盘中临时停牌，109-撤销退市风险警示公告，1..."""

    SuspendTerm: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SuspendResumption', column_name='SuspendTerm', column_type='varchar(60)', nullable=False, chn_name='停牌期限')
    """停牌期限:"""

