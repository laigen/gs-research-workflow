# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_Dividend(SQLTableEntity):
    name: str = 'LC_Dividend'
    
    chn_name: str = '公司分红'
    
    business_unique: str = 'InnerCode,EndDate'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.该表包括上市公司历次分红预案及实施进展，以及下年分配次数、方式等，以分红事件为维度，一次分红做一条记录。
2.数据范围：证券上市起-至今
3.信息来源：上市公司公告"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    EPS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='EPS', column_type='decimal(9,4)', nullable=False, chn_name='每股收益(元)')
    """每股收益(元):"""

    BonusShareRatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='BonusShareRatio', column_type='decimal(18,8)', nullable=False, chn_name='送股比例(10送X)')
    """送股比例(10送X):"""

    TranAddShareRaio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='TranAddShareRaio', column_type='decimal(18,8)', nullable=False, chn_name='转增股比例(10转增X)')
    """转增股比例(10转增X):"""

    PriceUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='PriceUnit', column_type='int', nullable=False, chn_name='派现外币单位')
    """派现外币单位:派现外币单位（PriceUnit）：与“系统常量表（CT_SystemConst）”中的“常量代码（DM）”关联，令“LB=1068”，得到派现外币单位的具体描述。1000-美元，1100-港元。该字段主要记录B股分红涉及的外币单位，A股分红因通常单位都是人民币，故派现外币单位为NULL。"""

    CashDiviRMB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='CashDiviRMB', column_type='decimal(18,8)', nullable=False, chn_name='派现(含税/人民币元)')
    """派现(含税/人民币元):"""

    ActualCashDiviRMB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='ActualCashDiviRMB', column_type='decimal(18,8)', nullable=False, chn_name='实派(税后/人民币元)')
    """实派(税后/人民币元):"""

    CashDiviFC: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='CashDiviFC', column_type='decimal(18,8)', nullable=False, chn_name='派现(含税/外币)')
    """派现(含税/外币):"""

    ActualCashDiviFC: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='ActualCashDiviFC', column_type='decimal(18,8)', nullable=False, chn_name='实派(税后/外币)')
    """实派(税后/外币):"""

    RightRegDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='RightRegDate', column_type='datetime', nullable=False, chn_name='股权登记日')
    """股权登记日:"""

    ExDiviDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='ExDiviDate', column_type='datetime', nullable=False, chn_name='除权除息日')
    """除权除息日:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='InnerCode', column_type='int', nullable=True, chn_name='证券内部编码')
    """证券内部编码:"""

    BonusShareListDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='BonusShareListDate', column_type='datetime', nullable=False, chn_name='送转股上市日')
    """送转股上市日:"""

    ToAccountDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='ToAccountDate', column_type='datetime', nullable=False, chn_name='股息到帐日期/红利发放日')
    """股息到帐日期/红利发放日:"""

    FinalTradingDay: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='FinalTradingDay', column_type='datetime', nullable=False, chn_name='最后交易日')
    """最后交易日:"""

    DiviBase: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='DiviBase', column_type='decimal(16,0)', nullable=False, chn_name='分红股本基数(股)')
    """分红股本基数(股):"""

    SharesAfterDivi: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='SharesAfterDivi', column_type='decimal(16,0)', nullable=False, chn_name='送转后总股本(股)')
    """送转后总股本(股):"""

    DiviObject: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='DiviObject', column_type='int', nullable=False, chn_name='分红对象')
    """分红对象:分红对象(DiviObject)与(CT_SystemConst)表中的DM字段关联，令LB = 1197，得到分红对象的具体描述：1-全体股东，2-发行前股东，3-部分股东。"""

    TotalCashDiviComRMB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='TotalCashDiviComRMB', column_type='decimal(19,4)', nullable=False, chn_name='公司合计派现金额(人民币元)')
    """公司合计派现金额(人民币元):"""

    TotalCashDiviComFC: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='TotalCashDiviComFC', column_type='decimal(19,4)', nullable=False, chn_name='公司合计派现金额(外币元)')
    """公司合计派现金额(外币元):"""

    CashDiviAShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='CashDiviAShare', column_type='decimal(19,4)', nullable=False, chn_name='其中:A股派现金额(元)')
    """其中:A股派现金额(元):"""

    CashDiviBShareRMB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='CashDiviBShareRMB', column_type='decimal(19,4)', nullable=False, chn_name='B股派现金额(人民币元)')
    """B股派现金额(人民币元):"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    CashDiviBShareFC: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='CashDiviBShareFC', column_type='decimal(19,4)', nullable=False, chn_name='B股派现金额(外币元)')
    """B股派现金额(外币元):"""

    DiviStartDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='DiviStartDate', column_type='datetime', nullable=False, chn_name='红利发放起始日')
    """红利发放起始日:"""

    DiviEndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='DiviEndDate', column_type='datetime', nullable=False, chn_name='红利发放截止日')
    """红利发放截止日:"""

    IFSchemeChange: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='IFSchemeChange', column_type='int', nullable=False, chn_name='方案是否变更')
    """方案是否变更:方案是否变更（IFSchemeChange），该字段固定以下常量：1-是；0-否"""

    ChangeStatement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='ChangeStatement', column_type='varchar(255)', nullable=False, chn_name='方案变更说明')
    """方案变更说明:"""

    ChangeType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='ChangeType', column_type='int', nullable=False, chn_name='方案变更类型')
    """方案变更类型:"""

    IfDiviBeforeChange: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='IfDiviBeforeChange', column_type='int', nullable=False, chn_name='变更前是否分红')
    """变更前是否分红:变更前是否分红（IfDiviBeforeChange），该字段固定以下常量：1-是；0-否；8-由股权分置产生的分红。"""

    BonusShareRatioBeforeChange: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='BonusShareRatioBeforeChange', column_type='decimal(9,4)', nullable=False, chn_name='变更前送股比例(10送X)')
    """变更前送股比例(10送X):"""

    TranAddShareRatioBeforeChange: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='TranAddShareRatioBeforeChange', column_type='decimal(9,4)', nullable=False, chn_name='变更前转增股比例(10转增X)')
    """变更前转增股比例(10转增X):"""

    CashDiviBeforeChangeRMB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='CashDiviBeforeChangeRMB', column_type='decimal(19,4)', nullable=False, chn_name='变更前派现(含税/人民币元)')
    """变更前派现(含税/人民币元):"""

    EventProcedure: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='EventProcedure', column_type='int', nullable=False, chn_name='事件进程')
    """事件进程:事件进程(EventProcedure)与(CT_SystemConst)表中的DM字段关联，令LB = 1059，得到事件进程的具体描述：1000-意向，1001-预案，1004-决案，1007-否决，1010-申请，1013-批准，1016-未实施终止，1019-实施中，1022-实施完成，1025-解除，1028-到期，1041-续签，1043-部分续..."""

    CashDiviBeforeChangeFC: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='CashDiviBeforeChangeFC', column_type='decimal(19,4)', nullable=False, chn_name='变更前派现(含税/外币)')
    """变更前派现(含税/外币):"""

    DiviBaseBeforeChange: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='DiviBaseBeforeChange', column_type='decimal(16,0)', nullable=False, chn_name='变更前分红股本基数(股)')
    """变更前分红股本基数(股):"""

    Notes: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='Notes', column_type='varchar(255)', nullable=False, chn_name='备注')
    """备注:"""

    SchemeStatement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='SchemeStatement', column_type='varchar(500)', nullable=False, chn_name='方案补充说明')
    """方案补充说明:"""

    UndistributeStatement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='UndistributeStatement', column_type='varchar(255)', nullable=False, chn_name='利润不分配说明')
    """利润不分配说明:"""

    DistributeTimes: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='DistributeTimes', column_type='varchar(10)', nullable=False, chn_name='利润分配次数')
    """利润分配次数:"""

    CeilingNext: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='CeilingNext', column_type='decimal(9,6)', nullable=False, chn_name='下限')
    """下限:"""

    FloorNext: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='FloorNext', column_type='decimal(9,6)', nullable=False, chn_name='上限')
    """上限:"""

    Ceiling: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='Ceiling', column_type='decimal(9,6)', nullable=False, chn_name='下限')
    """下限:"""

    Floor: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='Floor', column_type='decimal(9,6)', nullable=False, chn_name='上限')
    """上限:"""

    EventProcedureDesc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='EventProcedureDesc', column_type='varchar(50)', nullable=False, chn_name='事件进程描述')
    """事件进程描述:"""

    MainForm: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='MainForm', column_type='int', nullable=False, chn_name='主要分配形式')
    """主要分配形式:"""

    CashDiviCeiling: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='CashDiviCeiling', column_type='decimal(9,6)', nullable=False, chn_name='下限')
    """下限:"""

    CashDiviFloor: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='CashDiviFloor', column_type='decimal(9,6)', nullable=False, chn_name='上限')
    """上限:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新日期')
    """更新日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    IfDividend: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='IfDividend', column_type='int', nullable=False, chn_name='是否分红')
    """是否分红:是否分红(IfDividend)固定以下常量：0-否，1-是，8-对价，24-重整计划，25-特殊分红，99-其他分红。"""

    AdvanceDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='AdvanceDate', column_type='datetime', nullable=False, chn_name='预案公布日')
    """预案公布日:"""

    SMDeciPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='SMDeciPublDate', column_type='datetime', nullable=False, chn_name='决案公布日(股东大会决议公告日)')
    """决案公布日(股东大会决议公告日):"""

    DividendImplementDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Dividend', column_name='DividendImplementDate', column_type='datetime', nullable=False, chn_name='分红实施公告日')
    """分红实施公告日:"""

