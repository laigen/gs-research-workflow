# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_FundAnEarning(SQLTableEntity):
    name: str = 'MF_FundAnEarning'
    
    chn_name: str = '公募基金_分级基金约定收益率'
    
    business_unique: str = 'InnerCode,BeginDate'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.本表记录分级基金的约定收益率的表达式和具体值，及相应的起始日期和截止日期等。
2.历史数据：2007年7月起-至今。
3.数据来源：基金产品招募说明书。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundAnEarning', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    YieldBenchmarkType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundAnEarning', column_name='YieldBenchmarkType', column_type='int', nullable=False, chn_name='基准收益率类型')
    """基准收益率类型:基准收益率类型(YieldBenchmarkType)与(CT_SystemConst)表中的DM字段关联，令LB = 1012，得到基准收益率类型的具体描述：90-三个月整存整取定期存款利率，100-一年期整存整取定期存款利率，101-一年期定期存款利率(按付息日)，103-三年期定期存款利率，104-两年期定期存款利率，110-五年期定期存款利率，120..."""

    TaxRateType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundAnEarning', column_name='TaxRateType', column_type='int', nullable=False, chn_name='税率类型')
    """税率类型:税率类型(TaxRateType)与(CT_SystemConst)表中的DM字段关联，令LB = 1793，得到税率类型的具体描述：1-税前，2-税后。"""

    RelativeTaxRate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundAnEarning', column_name='RelativeTaxRate', column_type='decimal(19,9)', nullable=False, chn_name='相关税率')
    """相关税率:"""

    YieldBenchmarkDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundAnEarning', column_name='YieldBenchmarkDate', column_type='datetime', nullable=False, chn_name='收益率基准日')
    """收益率基准日:"""

    YieldBenchmarkDateExp: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundAnEarning', column_name='YieldBenchmarkDateExp', column_type='varchar(500)', nullable=False, chn_name='收益率基准日说明')
    """收益率基准日说明:"""

    YieldBenchmarkRate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundAnEarning', column_name='YieldBenchmarkRate', column_type='decimal(19,9)', nullable=False, chn_name='收益率基准利率(%)')
    """收益率基准利率(%):"""

    YieldCoefficient: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundAnEarning', column_name='YieldCoefficient', column_type='decimal(19,9)', nullable=False, chn_name='收益率系数')
    """收益率系数:"""

    MinExYield: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundAnEarning', column_name='MinExYield', column_type='decimal(19,9)', nullable=False, chn_name='额外最低收益率(%)')
    """额外最低收益率(%):"""

    MaxExYield: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundAnEarning', column_name='MaxExYield', column_type='decimal(19,9)', nullable=False, chn_name='额外最高收益率(%)')
    """额外最高收益率(%):"""

    MinPromisedYield: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundAnEarning', column_name='MinPromisedYield', column_type='decimal(19,9)', nullable=False, chn_name='约定最低收益率(%)')
    """约定最低收益率(%):"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundAnEarning', column_name='InnerCode', column_type='int', nullable=False, chn_name='基金内部编码')
    """基金内部编码:基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    MaxPromisedYield: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundAnEarning', column_name='MaxPromisedYield', column_type='decimal(19,9)', nullable=False, chn_name='约定最高收益率(%)')
    """约定最高收益率(%):"""

    MinPromisedYieldPeriod: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundAnEarning', column_name='MinPromisedYieldPeriod', column_type='decimal(19,9)', nullable=False, chn_name='本期约定最低收益率(%)')
    """本期约定最低收益率(%):"""

    MaxPromisedYieldPeriod: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundAnEarning', column_name='MaxPromisedYieldPeriod', column_type='decimal(19,9)', nullable=False, chn_name='本期约定最高收益率(%)')
    """本期约定最高收益率(%):"""

    Remark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundAnEarning', column_name='Remark', column_type='varchar(500)', nullable=False, chn_name='备注说明')
    """备注说明:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundAnEarning', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundAnEarning', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundAnEarning', column_name='CompanyCode', column_type='int', nullable=False, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到基金公司的交易代码、简称等。"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundAnEarning', column_name='InfoSource', column_type='varchar(100)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundAnEarning', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日')
    """信息发布日:"""

    FormulaDesc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundAnEarning', column_name='FormulaDesc', column_type='varchar(500)', nullable=False, chn_name='公式描述')
    """公式描述:"""

    YieldType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundAnEarning', column_name='YieldType', column_type='int', nullable=False, chn_name='收益率类型')
    """收益率类型:收益率类型(YieldType)与(CT_SystemConst)表中的DM字段关联，令LB = 1792，得到收益率类型的具体描述：1-浮动，2-固定。"""

    BeginDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundAnEarning', column_name='BeginDate', column_type='datetime', nullable=False, chn_name='起始日期')
    """起始日期:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundAnEarning', column_name='EndDate', column_type='datetime', nullable=False, chn_name='截止日期')
    """截止日期:"""

