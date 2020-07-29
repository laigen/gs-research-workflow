# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_DividendProgress(SQLTableEntity):
    name: str = 'LC_DividendProgress'
    
    chn_name: str = '公司分红进度'
    
    business_unique: str = 'InnerCode,EndDate,SchemeNo,InfoPubType,Process,InfoPubDate'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.收录上市公司分红的详细信息，以事件进程为维度，一次分红根据不同的进程，分多条记录展示，主要进程包括：意向、预案、决案、方案实施等。
2.数据范围：2012-至今
3.信息来源：上市公司公告"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    BonusShareRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='BonusShareRatio', column_type='decimal(19,8)', nullable=False, chn_name='送股比例(10送X)')
    """送股比例(10送X):"""

    TranAddShareRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='TranAddShareRatio', column_type='decimal(19,8)', nullable=False, chn_name='转增股比例(10转增X)')
    """转增股比例(10转增X):"""

    CashDiviRMB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='CashDiviRMB', column_type='decimal(19,8)', nullable=False, chn_name='派现(含税10派X元)')
    """派现(含税10派X元):"""

    ActualCashDiviRMB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='ActualCashDiviRMB', column_type='decimal(19,8)', nullable=False, chn_name='实派(税后10派X元)')
    """实派(税后10派X元):"""

    QFIIAcCashDiviRMB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='QFIIAcCashDiviRMB', column_type='decimal(19,8)', nullable=False, chn_name='QFII实派(税后10派X元)')
    """QFII实派(税后10派X元):"""

    RSHolderAcCashDiviRMB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='RSHolderAcCashDiviRMB', column_type='decimal(19,8)', nullable=False, chn_name='限售股持有人实派(税后10派X元)')
    """限售股持有人实派(税后10派X元):"""

    FSHolderAcCashDiviRMB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='FSHolderAcCashDiviRMB', column_type='decimal(19,8)', nullable=False, chn_name='流通股持有人实派(税后10派X元)')
    """流通股持有人实派(税后10派X元):"""

    DiviBase: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='DiviBase', column_type='decimal(19,2)', nullable=False, chn_name='分红股本基数(股)')
    """分红股本基数(股):"""

    DiviObject: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='DiviObject', column_type='int', nullable=False, chn_name='分红对象')
    """分红对象:分红对象(DiviObject)与(CT_SystemConst)表中的DM字段关联，令LB = 1197，得到分红对象的具体描述：1-全体股东，2-发行前股东，3-部分股东。"""

    SharesAfterDivi: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='SharesAfterDivi', column_type='decimal(19,2)', nullable=False, chn_name='送转后总股本')
    """送转后总股本:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='InnerCode', column_type='int', nullable=True, chn_name='内部编码')
    """内部编码:"""

    TotalCashDivi: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='TotalCashDivi', column_type='decimal(19,4)', nullable=False, chn_name='合计派现金额(元)')
    """合计派现金额(元):"""

    CashDiviAShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='CashDiviAShare', column_type='decimal(19,4)', nullable=False, chn_name='A股派现金额(元)')
    """A股派现金额(元):"""

    RegisterDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='RegisterDate', column_type='datetime', nullable=False, chn_name='股权登记日')
    """股权登记日:"""

    ExDiviDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='ExDiviDate', column_type='datetime', nullable=False, chn_name='除权除息日')
    """除权除息日:"""

    BonusShareArrivalDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='BonusShareArrivalDate', column_type='datetime', nullable=False, chn_name='送转股到账日')
    """送转股到账日:"""

    BonusShareListDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='BonusShareListDate', column_type='datetime', nullable=False, chn_name='送转股上市日')
    """送转股上市日:"""

    ToAccountDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='ToAccountDate', column_type='datetime', nullable=False, chn_name='股息到帐日期/红利发放日')
    """股息到帐日期/红利发放日:"""

    SchemeStatement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='SchemeStatement', column_type='varchar(500)', nullable=False, chn_name='方案补充说明')
    """方案补充说明:"""

    ChangeStatement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='ChangeStatement', column_type='varchar(255)', nullable=False, chn_name='方案变更说明')
    """方案变更说明:"""

    ChangeType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='ChangeType', column_type='int', nullable=False, chn_name='方案变更类型')
    """方案变更类型:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    UndistributeStatement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='UndistributeStatement', column_type='varchar(255)', nullable=False, chn_name='利润不分配说明')
    """利润不分配说明:"""

    Notes: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='Notes', column_type='varchar(255)', nullable=False, chn_name='备注')
    """备注:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    SchemeNo: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='SchemeNo', column_type='int', nullable=True, chn_name='方案序号')
    """方案序号:方案序号(SchemeNo)与(CT_SystemConst)表中的DM字段关联，令LB = 103，得到方案序号的具体描述：1-1，2-2，3-3，4-4，5-5，6-6，7-7，8-8，9-9，10-10，11-11，12-12，13-13，14-14，15-15，16-16，17-17，18-18，19-19，20-20，21-21，22-22，23-..."""

    InfoPubDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='InfoPubDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    InfoPubType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='InfoPubType', column_type='int', nullable=True, chn_name='信息发布日期类型')
    """信息发布日期类型:信息发布日期类型(InfoPubType)与(CT_SystemConst)表中的DM字段关联，令LB = 1740，得到信息发布日期类型的具体描述：10-预披露公告日，20-预案公告日，30-决案公告日，40-分红实施公告日，50-方案变更公告日，60-更正公告日，99-其他公告日。"""

    SchemeType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='SchemeType', column_type='int', nullable=False, chn_name='方案类型')
    """方案类型:方案类型(SchemeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1739，得到方案类型的具体描述：10-公司提出方案，20-股东提出方案，99-其它。"""

    Process: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='Process', column_type='int', nullable=True, chn_name='事件进程')
    """事件进程:事件进程(Process)与(CT_SystemConst)表中的DM字段关联，令LB = 1059，得到事件进程的具体描述：1000-意向，1001-预案，1004-决案，1007-否决，1010-申请，1013-批准，1016-未实施终止，1019-实施中，1022-实施完成，1025-解除，1028-到期，1041-续签，1043-部分续签，1051-..."""

    IfDividend: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_DividendProgress', column_name='IfDividend', column_type='int', nullable=False, chn_name='是否分红')
    """是否分红:是否分红(IfDividend)与(CT_SystemConst)表中的DM字段关联，令LB=999 AND DM IN (1,2,8,24,25,99)，得到是否分红的具体描述：1-是，2-否，8-对价，24-重整计划，25-特殊分红，99-其他分红。"""

