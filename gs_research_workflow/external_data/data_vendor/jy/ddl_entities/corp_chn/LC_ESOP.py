# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_ESOP(SQLTableEntity):
    name: str = 'LC_ESOP'
    
    chn_name: str = '员工持股计划'
    
    business_unique: str = 'InnerCode,SerialNumber,Period'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.主要记录员工持股计划当期的情况：包括相关日期、事件进程、事件说明、资金来源、资金总额、股票来源、股票规模、实施是否分期、存续期、锁定期等一些情况。
2.数据范围：2014.6-至今
3.信息来源：上市公司公告"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOP', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    Period: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOP', column_name='Period', column_type='int', nullable=False, chn_name='分期实施期次')
    """分期实施期次:"""

    PeriodSituation: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOP', column_name='PeriodSituation', column_type='varchar(50)', nullable=False, chn_name='分期情况')
    """分期情况:"""

    InitialImpleDay: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOP', column_name='InitialImpleDay', column_type='datetime', nullable=False, chn_name='首次实施公告日')
    """首次实施公告日:"""

    ShareSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOP', column_name='ShareSource', column_type='varchar(2000)', nullable=False, chn_name='股票来源方式')
    """股票来源方式:"""

    ShareCelling: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOP', column_name='ShareCelling', column_type='decimal(19,2)', nullable=False, chn_name='股票规模上限(万股)')
    """股票规模上限(万股):"""

    ShareFloor: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOP', column_name='ShareFloor', column_type='decimal(19,2)', nullable=False, chn_name='股票规模下限(万股)')
    """股票规模下限(万股):"""

    FundCelling: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOP', column_name='FundCelling', column_type='decimal(19,4)', nullable=False, chn_name='资金总额上限(万元)')
    """资金总额上限(万元):"""

    FundFloor: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOP', column_name='FundFloor', column_type='decimal(19,4)', nullable=False, chn_name='资金总额下限(万元)')
    """资金总额下限(万元):"""

    Duration: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOP', column_name='Duration', column_type='decimal(19,2)', nullable=False, chn_name='存续期(月)')
    """存续期(月):"""

    LockDuration: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOP', column_name='LockDuration', column_type='decimal(19,2)', nullable=False, chn_name='锁定期(月)')
    """锁定期(月):"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOP', column_name='InnerCode', column_type='int', nullable=False, chn_name='内部编码')
    """内部编码:内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到股票的交易代码、简称等。"""

    ReleaseDuration: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOP', column_name='ReleaseDuration', column_type='decimal(19,2)', nullable=False, chn_name='释放期(月)')
    """释放期(月):"""

    FundSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOP', column_name='FundSource', column_type='varchar(2000)', nullable=False, chn_name='资金来源')
    """资金来源:"""

    Participant: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOP', column_name='Participant', column_type='varchar(2000)', nullable=False, chn_name='参加对象')
    """参加对象:"""

    Management: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOP', column_name='Management', column_type='varchar(2000)', nullable=False, chn_name='管理模式')
    """管理模式:"""

    ManageInsitute: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOP', column_name='ManageInsitute', column_type='varchar(2000)', nullable=False, chn_name='管理机构')
    """管理机构:"""

    PlanName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOP', column_name='PlanName', column_type='varchar(2000)', nullable=False, chn_name='资产管理计划全称')
    """资产管理计划全称:"""

    PlanRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOP', column_name='PlanRatio', column_type='varchar(50)', nullable=False, chn_name='资产管理计划杠杆比例')
    """资产管理计划杠杆比例:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOP', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOP', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOP', column_name='CompanyCode', column_type='int', nullable=False, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。"""

    IniInfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOP', column_name='IniInfoPublDate', column_type='datetime', nullable=False, chn_name='首次信息发布日期')
    """首次信息发布日期:"""

    DMAnnounceDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOP', column_name='DMAnnounceDate', column_type='datetime', nullable=False, chn_name='董事会公告日期')
    """董事会公告日期:"""

    SMAnnounceDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOP', column_name='SMAnnounceDate', column_type='datetime', nullable=False, chn_name='股东大会公告日期')
    """股东大会公告日期:"""

    Process: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOP', column_name='Process', column_type='int', nullable=False, chn_name='事件进程')
    """事件进程:事件进程(Process)与(CT_SystemConst)表中的DM字段关联，令LB = 1059，得到事件进程的具体描述：1000-意向，1001-预案，1004-决案，1007-否决，1010-申请，1013-批准，1016-未实施终止，1019-实施中，1022-实施完成，1025-解除，1028-到期，1041-续签，1043-部分续签，1051-..."""

    SerialNumber: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOP', column_name='SerialNumber', column_type='int', nullable=True, chn_name='序号')
    """序号:"""

    IfPeriod: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOP', column_name='IfPeriod', column_type='int', nullable=False, chn_name='是否分期实施')
    """是否分期实施:是否分期实施(IfPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否分期实施的具体描述：1-是，2-否。"""

