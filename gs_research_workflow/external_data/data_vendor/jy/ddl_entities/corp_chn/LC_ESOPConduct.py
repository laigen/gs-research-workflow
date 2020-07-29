# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_ESOPConduct(SQLTableEntity):
    name: str = 'LC_ESOPConduct'
    
    chn_name: str = '员工持股计划实施情况'
    
    business_unique: str = 'InnerCode,InitialImpleDay,ImplementDate'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.主要记录员工持股计划当期实施情况：包括相关日期、实施股份、实施价格等指标。
2.数据范围：2014.6-至今
3.信息来源：上市公司公告"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOPConduct', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    ImpleEndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOPConduct', column_name='ImpleEndDate', column_type='datetime', nullable=False, chn_name='实施截止日')
    """实施截止日:"""

    ShareSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOPConduct', column_name='ShareSource', column_type='varchar(2000)', nullable=False, chn_name='本次实施股票来源')
    """本次实施股票来源:"""

    PriceCelling: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOPConduct', column_name='PriceCelling', column_type='decimal(19,4)', nullable=False, chn_name='本次实施价格上限(元)')
    """本次实施价格上限(元):"""

    PriceFloor: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOPConduct', column_name='PriceFloor', column_type='decimal(19,4)', nullable=False, chn_name='本次实施价格下限(元)')
    """本次实施价格下限(元):"""

    ShareCelling: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOPConduct', column_name='ShareCelling', column_type='decimal(19,2)', nullable=False, chn_name='本次实施股份上限(万股)')
    """本次实施股份上限(万股):"""

    ShareFloor: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOPConduct', column_name='ShareFloor', column_type='decimal(19,2)', nullable=False, chn_name='本次实施股份下限(万股)')
    """本次实施股份下限(万股):"""

    Proportion: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOPConduct', column_name='Proportion', column_type='decimal(9,6)', nullable=False, chn_name='本次实施占总股本比例')
    """本次实施占总股本比例:"""

    LockDuration: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOPConduct', column_name='LockDuration', column_type='decimal(19,2)', nullable=False, chn_name='锁定期(月)')
    """锁定期(月):"""

    Counterpart: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOPConduct', column_name='Counterpart', column_type='varchar(2000)', nullable=False, chn_name='股票实施赠与方')
    """股票实施赠与方:"""

    AccumulateShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOPConduct', column_name='AccumulateShare', column_type='decimal(19,2)', nullable=False, chn_name='累计实施股份(万股)')
    """累计实施股份(万股):"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOPConduct', column_name='InnerCode', column_type='int', nullable=False, chn_name='内部编码')
    """内部编码:内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到股票的交易代码、简称等。"""

    AccuProportion: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOPConduct', column_name='AccuProportion', column_type='decimal(9,6)', nullable=False, chn_name='累计占总股本比例')
    """累计占总股本比例:"""

    Statement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOPConduct', column_name='Statement', column_type='varchar(4000)', nullable=False, chn_name='实施情况说明')
    """实施情况说明:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOPConduct', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOPConduct', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOPConduct', column_name='CompanyCode', column_type='int', nullable=False, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。"""

    IniInfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOPConduct', column_name='IniInfoPublDate', column_type='datetime', nullable=False, chn_name='首次信息发布日期')
    """首次信息发布日期:"""

    SerialNumber: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOPConduct', column_name='SerialNumber', column_type='int', nullable=False, chn_name='序号')
    """序号:"""

    IfPeriod: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOPConduct', column_name='IfPeriod', column_type='int', nullable=False, chn_name='是否分期实施')
    """是否分期实施:是否分期实施(IfPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否分期实施的具体描述：1-是，2-否。"""

    Period: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOPConduct', column_name='Period', column_type='int', nullable=False, chn_name='分期实施期次')
    """分期实施期次:"""

    InitialImpleDay: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOPConduct', column_name='InitialImpleDay', column_type='datetime', nullable=False, chn_name='首次实施公告日')
    """首次实施公告日:"""

    ImplementDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ESOPConduct', column_name='ImplementDate', column_type='datetime', nullable=False, chn_name='实施公告日')
    """实施公告日:"""

