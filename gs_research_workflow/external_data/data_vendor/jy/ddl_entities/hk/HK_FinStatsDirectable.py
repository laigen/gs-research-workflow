# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_FinStatsDirectable(SQLTableEntity):
    name: str = 'HK_FinStatsDirectable'
    
    chn_name: str = '港股财报目录表'
    
    business_unique: str = 'CompanyCode,EndDate,DateTypeCode,ReportType'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.介绍港股财报的基础信息 ,包括一份财报披露的表单信息，单季度数据和常规数据，是否包含母公司报表，财报披露遵循的会计准则，财报披露适用的一般格式，财报中是否使用有两个以上货币单位等信息。
2.数据范围：1998年至今。
3.数据来源：港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    BeginDateBS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='BeginDateBS', column_type='datetime', nullable=False, chn_name='期初日期-资产负债表')
    """期初日期-资产负债表:"""

    CompanyNatureBS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='CompanyNatureBS', column_type='int', nullable=False, chn_name='公司性质-资产负债表')
    """公司性质-资产负债表:公司性质-资产负债表(CompanyNatureBS)与(CT_SystemConst)表中的DM字段关联，令LB=1356，得到公司性质-资产负债表的具体描述：1-普通，2-金融，3-保险。"""

    AccountingStandardsBS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='AccountingStandardsBS', column_type='int', nullable=False, chn_name='会计准则-资产负债表')
    """会计准则-资产负债表:会计准则-资产负债表(AccountingStandardsBS)与(CT_SystemConst)表中的DM字段关联，令LB=1357，得到会计准则-资产负债表的具体描述：7-国际会计准则，110-香港会计准则，502-美国会计准则，503-新加坡会计准则，510-国际会计准则及香港会计准则，520-中国会计准则。"""

    MajoyCurrencyUnitBS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='MajoyCurrencyUnitBS', column_type='int', nullable=False, chn_name='主货币类别-资产负债表')
    """主货币类别-资产负债表:主货币类别-资产负债表(MajoyCurrencyUnitBS)与(CT_SystemConst)表中的DM字段关联，令LB=1068，得到主货币类别-资产负债表的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸..."""

    HasTwoCurrencyBS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='HasTwoCurrencyBS', column_type='int', nullable=False, chn_name='是否有两个以上货币-资产负债表')
    """是否有两个以上货币-资产负债表:是否有两个以上货币-资产负债表（HasTwoCurrencyBS）：与系统常量表（CT_SystemConst）中的DM字段关联，令LB=999，得到是否有两个以上货币-资产负债表的描述：1-是；2-否。"""

    HasCashFlowStatement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='HasCashFlowStatement', column_type='int', nullable=False, chn_name='是否有现金流量表')
    """是否有现金流量表:是否有现金流量表（HasCashFlowStatement）：与系统常量表（CT_SystemConst）中的DM字段关联，令LB=999，得到是否有现金流量表的描述：1-是；2-否。"""

    HasPCCashFlowStatement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='HasPCCashFlowStatement', column_type='int', nullable=False, chn_name='是否有母公司现金流量表')
    """是否有母公司现金流量表:是否有母公司现金流量表（HasPCCashFlowStatement）：与系统常量表（CT_SystemConst）中的DM字段关联，令LB=999，得到是否有母公司现金流量表的描述：1-是；2-否。"""

    InfoPublDateCS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='InfoPublDateCS', column_type='datetime', nullable=False, chn_name='信息发布日期-现金流量表')
    """信息发布日期-现金流量表:"""

    InfoSourceCS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='InfoSourceCS', column_type='varchar(100)', nullable=False, chn_name='信息来源-现金流量表')
    """信息来源-现金流量表:"""

    FiscalYearCS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='FiscalYearCS', column_type='datetime', nullable=False, chn_name='财政年度-现金流量表')
    """财政年度-现金流量表:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到所属公司股票的交易代码、简称等。"""

    BeginDateCS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='BeginDateCS', column_type='datetime', nullable=False, chn_name='起始日期-现金流量表')
    """起始日期-现金流量表:"""

    CompanyNatureCS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='CompanyNatureCS', column_type='int', nullable=False, chn_name='公司性质-现金流量表')
    """公司性质-现金流量表:公司性质-现金流量表(CompanyNatureCS)与(CT_SystemConst)表中的DM字段关联，令LB=1356，得到公司性质-现金流量表的具体描述：1-普通，2-金融，3-保险。"""

    AccountingStandardsCS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='AccountingStandardsCS', column_type='int', nullable=False, chn_name='会计准则-现金流量表')
    """会计准则-现金流量表:会计准则-现金流量表(AccountingStandardsCS)与(CT_SystemConst)表中的DM字段关联，令LB=1357，得到会计准则-现金流量表的具体描述：7-国际会计准则，110-香港会计准则，502-美国会计准则，503-新加坡会计准则，510-国际会计准则及香港会计准则，520-中国会计准则。"""

    MajoyCurrencyUnitCS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='MajoyCurrencyUnitCS', column_type='int', nullable=False, chn_name='主货币单位-现金流量表')
    """主货币单位-现金流量表:主货币单位-现金流量表(MajoyCurrencyUnitCS)与(CT_SystemConst)表中的DM字段关联，令LB=1068，得到主货币单位-现金流量表的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸..."""

    HasTwoCurrencyCS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='HasTwoCurrencyCS', column_type='int', nullable=False, chn_name='是否有两个以上货币-现金流量表')
    """是否有两个以上货币-现金流量表:是否有两个以上货币-现金流量表（HasTwoCurrencyCS）：与系统常量表（CT_SystemConst）中的DM字段关联，令LB=999，得到是否有两个以上货币-现金流量表的描述：1-是；2-否。"""

    HasIncomeStatement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='HasIncomeStatement', column_type='int', nullable=False, chn_name='是否有利润分配表')
    """是否有利润分配表:是否有利润分配表（HasIncomeStatement）：与系统常量表（CT_SystemConst）中的DM字段关联，令LB=999，得到是否有利润分配表的描述：1-是；2-否。"""

    HasPCIncomeStatement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='HasPCIncomeStatement', column_type='int', nullable=False, chn_name='是否有母公司利润分配表')
    """是否有母公司利润分配表:是否有母公司利润分配表（HasPCIncomeStatement）：与系统常量表（CT_SystemConst）中的DM字段关联，令LB=999，得到是否有母公司利润分配表的描述：1-是；2-否。"""

    InfoPublDateIS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='InfoPublDateIS', column_type='datetime', nullable=False, chn_name='信息发布日期-利润分配表')
    """信息发布日期-利润分配表:"""

    InfoSourceIS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='InfoSourceIS', column_type='varchar(100)', nullable=False, chn_name='信息来源-利润分配表')
    """信息来源-利润分配表:"""

    FiscalYearIS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='FiscalYearIS', column_type='datetime', nullable=False, chn_name='财政年度-利润分配表')
    """财政年度-利润分配表:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    BeginDateIS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='BeginDateIS', column_type='datetime', nullable=False, chn_name='起始日期-利润分配表')
    """起始日期-利润分配表:"""

    CompanyNatureIS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='CompanyNatureIS', column_type='int', nullable=False, chn_name='公司性质-利润分配表')
    """公司性质-利润分配表:公司性质-利润分配表(CompanyNatureIS)与(CT_SystemConst)表中的DM字段关联，令LB=1356，得到公司性质-利润分配表的具体描述：1-普通，2-金融，3-保险。"""

    AccountingStandardsIS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='AccountingStandardsIS', column_type='int', nullable=False, chn_name='会计准则-利润分配表')
    """会计准则-利润分配表:会计准则-利润分配表(AccountingStandardsIS)与(CT_SystemConst)表中的DM字段关联，令LB=1357，得到会计准则-利润分配表的具体描述：7-国际会计准则，110-香港会计准则，502-美国会计准则，503-新加坡会计准则，510-国际会计准则及香港会计准则，520-中国会计准则。"""

    MajoyCurrencyUnitIS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='MajoyCurrencyUnitIS', column_type='int', nullable=False, chn_name='主货币单位-利润分配表')
    """主货币单位-利润分配表:主货币单位-利润分配表(MajoyCurrencyUnitIS)与(CT_SystemConst)表中的DM字段关联，令LB=1068，得到主货币单位-利润分配表的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸..."""

    HasTwoCurrencyIS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='HasTwoCurrencyIS', column_type='int', nullable=False, chn_name='是否有两个以上货币-利润分配表')
    """是否有两个以上货币-利润分配表:是否有两个以上货币-利润分配表（HasTwoCurrencyIS）：与系统常量表（CT_SystemConst）中的DM字段关联，令LB=999，得到是否有两个以上货币-利润分配表的描述：1-是；2-否。"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    DateTypeCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='DateTypeCode', column_type='int', nullable=True, chn_name='日期标识')
    """日期标识:日期标识(DateTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB=1314，得到日期标识的具体描述：1-1个月，2-2个月，3-3个月，4-4个月，5-5个月，6-半年度，7-7个月，8-8个月，9-9个月，10-10个月，11-11个月，12-年度，13-13个月，14-14个月，15-15个月，16-16个月，17-17个..."""

    ReportType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='ReportType', column_type='int', nullable=True, chn_name='报告类型')
    """报告类型:报告类型（ReportType）：1-单季度报告；2-常规报表。"""

    HasBalanceSheet: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='HasBalanceSheet', column_type='int', nullable=False, chn_name='是否有资产负债表')
    """是否有资产负债表:是否有资产负债表（HasBalanceSheet）：与系统常量表（CT_SystemConst）中的DM字段关联，令LB=999，得到是否有资产负债表的描述：1-是；2-否。"""

    HasPCBalanceSheet: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='HasPCBalanceSheet', column_type='int', nullable=False, chn_name='是否有母公司资产负债表')
    """是否有母公司资产负债表:是否有母公司资产负债表（HasPCBalanceSheet）：与系统常量表（CT_SystemConst）中的DM字段关联，令LB=999，得到是否有母公司资产负债表的描述：1-是；2-否。"""

    InfoPublDateBS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='InfoPublDateBS', column_type='datetime', nullable=False, chn_name='信息发布日期-资产负债表')
    """信息发布日期-资产负债表:"""

    InfoSourceBS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_FinStatsDirectable', column_name='InfoSourceBS', column_type='varchar(100)', nullable=False, chn_name='信息来源-资产负债表')
    """信息来源-资产负债表:"""

