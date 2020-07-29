# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_SharesFloatingSchedule(SQLTableEntity):
    name: str = 'LC_SharesFloatingSchedule'
    
    chn_name: str = '限售股票解禁时间表'
    
    business_unique: str = 'CompanyCode,StartDateForFloating'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.收录上市公司因为股权分置改革、定向增发、公开增发等原因所限售的股票的具体解禁时间，以上市公司为维度，不区分具体股东，主要包括可流通起始日、本次新增可售股份、已流通股份、待流通股份、总股本、股本变动原因说明等指标。
2.数据范围：2006-至今
3.信息来源：上市公司公告"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SharesFloatingSchedule', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    NonMarketableAShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SharesFloatingSchedule', column_name='NonMarketableAShares', column_type='decimal(18,4)', nullable=False, chn_name='待流通A股(万股)')
    """待流通A股(万股):"""

    TotalAShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SharesFloatingSchedule', column_name='TotalAShares', column_type='decimal(18,4)', nullable=False, chn_name='A股总数(万股)')
    """A股总数(万股):"""

    Proportion2: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SharesFloatingSchedule', column_name='Proportion2', column_type='decimal(18,4)', nullable=False, chn_name='已流通A股占A股总数比例(%)')
    """已流通A股占A股总数比例(%):"""

    TotalShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SharesFloatingSchedule', column_name='TotalShares', column_type='decimal(18,4)', nullable=False, chn_name='总股本(万股)')
    """总股本(万股):"""

    NewMarketableSharesSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SharesFloatingSchedule', column_name='NewMarketableSharesSource', column_type='varchar(100)', nullable=False, chn_name='本次解禁股票来源')
    """本次解禁股票来源:"""

    SourceType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SharesFloatingSchedule', column_name='SourceType', column_type='int', nullable=False, chn_name='本次解禁股票来源代码')
    """本次解禁股票来源代码:本次解禁股票来源代码(SourceType)与(CT_SystemConst)表中的DM字段关联，令LB = 1022，得到本次解禁股票来源代码的具体描述：1-A股发行，2-B股发行，3-A股发行基金配售上市，4-A股发行法人配售上市，6-A股上市，7-B股上市，8-送转股，10-配股除权，11-配股上市，12-转配股上市，17-非公开增发A股上市，18-非..."""

    ChangeReason: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SharesFloatingSchedule', column_name='ChangeReason', column_type='varchar(255)', nullable=False, chn_name='本次股本变动说明')
    """本次股本变动说明:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SharesFloatingSchedule', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SharesFloatingSchedule', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SharesFloatingSchedule', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SharesFloatingSchedule', column_name='InnerCode', column_type='int', nullable=False, chn_name='A股内部编码')
    """A股内部编码:A股内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到股票的交易代码、简称等。"""

    InitialInfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SharesFloatingSchedule', column_name='InitialInfoPublDate', column_type='datetime', nullable=False, chn_name='首次信息发布日期')
    """首次信息发布日期:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SharesFloatingSchedule', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    StartDateForFloating: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SharesFloatingSchedule', column_name='StartDateForFloating', column_type='datetime', nullable=True, chn_name='可流通起始日')
    """可流通起始日:"""

    NewMarketableAShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SharesFloatingSchedule', column_name='NewMarketableAShares', column_type='decimal(18,4)', nullable=False, chn_name='本次新增可售A股(万股)')
    """本次新增可售A股(万股):"""

    Proportion1: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SharesFloatingSchedule', column_name='Proportion1', column_type='decimal(18,4)', nullable=False, chn_name='本次新增可售A股占上期末已流通A股比例(%)')
    """本次新增可售A股占上期末已流通A股比例(%):"""

    AccuMarketableAShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SharesFloatingSchedule', column_name='AccuMarketableAShares', column_type='decimal(18,4)', nullable=False, chn_name='已流通A股(万股)')
    """已流通A股(万股):"""

