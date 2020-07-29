# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_ReserveReportDate(SQLTableEntity):
    name: str = 'LC_ReserveReportDate'
    
    chn_name: str = '财务报告预约披露日'
    
    business_unique: str = 'InnerCode,InfoPublDate,NoticeStartDate,NoticeType'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.收录上市公司定期报告预约披露日信息，包括公告类别、预约披露起始与截止日和实际披露日期等内容。
2.数据范围：1990-12-28至今"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ReserveReportDate', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    NoticeType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ReserveReportDate', column_name='NoticeType', column_type='int', nullable=True, chn_name='提示信息类别')
    """提示信息类别:提示信息类别(NoticeType)与(CT_SystemConst)表中的DM字段关联，令LB = 204 AND DM IN (50,51,52,53)，得到提示信息类别的具体描述：50-中报预约披露日，51-年报预约披露日，52-第一季报预约披露日，53-第三季报预约披露日。"""

    NoticeContent: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ReserveReportDate', column_name='NoticeContent', column_type='text', nullable=False, chn_name='提示信息内容')
    """提示信息内容:"""

    InsertTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ReserveReportDate', column_name='InsertTime', column_type='datetime', nullable=False, chn_name='发布时间')
    """发布时间:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ReserveReportDate', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ReserveReportDate', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ReserveReportDate', column_name='InnerCode', column_type='int', nullable=True, chn_name='证券内部编码')
    """证券内部编码:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ReserveReportDate', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ReserveReportDate', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    BulletinType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ReserveReportDate', column_name='BulletinType', column_type='int', nullable=False, chn_name='公告类别')
    """公告类别:公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311，得到公告类别的具体描述：10-发行上市书，20-定期报告，30-业绩快报，50-章程制度，70-临时公告，90-交易所通报，91-交易所临时停(复)牌公告，99-其他。"""

    BulletinTypeName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ReserveReportDate', column_name='BulletinTypeName', column_type='varchar(200)', nullable=False, chn_name='公告类别名称')
    """公告类别名称:"""

    NoticeStartDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ReserveReportDate', column_name='NoticeStartDate', column_type='datetime', nullable=True, chn_name='预约披露起始日')
    """预约披露起始日:"""

    NoticeEndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ReserveReportDate', column_name='NoticeEndDate', column_type='datetime', nullable=False, chn_name='预约披露截止日')
    """预约披露截止日:"""

    ActualDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ReserveReportDate', column_name='ActualDate', column_type='datetime', nullable=False, chn_name='实际披露日期')
    """实际披露日期:"""

