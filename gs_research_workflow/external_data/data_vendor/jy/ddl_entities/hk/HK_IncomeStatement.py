# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_IncomeStatement(SQLTableEntity):
    name: str = 'HK_IncomeStatement'
    
    chn_name: str = '港股利润分配表'
    
    business_unique: str = 'CompanyCode,EndDate,PeriodMark,IfMerged,IfAdjusted,ProjectName'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.介绍港股利润分配表中各项指标，该表是利润分配表的竖表，数据内容和财报一致。
2.数据范围：1998年至今。
3.数据来源：港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatement', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    AccountingStandards: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatement', column_name='AccountingStandards', column_type='int', nullable=False, chn_name='会计准则')
    """会计准则:会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 1357，得到会计准则的具体描述：7-国际会计准则，110-香港会计准则，502-美国会计准则，503-新加坡会计准则，510-国际会计准则及香港会计准则，520-中国会计准则。"""

    IfMerged: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatement', column_name='IfMerged', column_type='int', nullable=False, chn_name='合并标志')
    """合并标志:合并标志(IfMerged)与(CT_SystemConst)表中的DM字段关联，令LB = 1189 AND DM IN (1,2)，得到合并标志的具体描述：1-合并，2-母公司。"""

    IfAdjusted: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatement', column_name='IfAdjusted', column_type='int', nullable=False, chn_name='调整标志')
    """调整标志:调整标志(IfAdjusted)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM IN (1,2)，得到调整标志的具体描述：1-是，2-否。"""

    CurrencyUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatement', column_name='CurrencyUnit', column_type='int', nullable=False, chn_name='货币单位')
    """货币单位:货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068，得到货币单位的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，1170-约旦第纳尔，1180-科..."""

    ProjectName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatement', column_name='ProjectName', column_type='varchar(200)', nullable=False, chn_name='明细科目名称')
    """明细科目名称:"""

    ItemType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatement', column_name='ItemType', column_type='int', nullable=False, chn_name='明细科目类别')
    """明细科目类别:明细科目代码（ItemType）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，当AccountingStandards会计准则不为520中国会计准则,公司性质为1一般公司时，令LB=“1378”；当AccountingStandards会计准则不为520-中国会计准则,公司性质为2金融时，令LB=“1379”,得到明细科目类别的..."""

    LastPeriodAccount: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatement', column_name='LastPeriodAccount', column_type='decimal(22,6)', nullable=False, chn_name='同期金额(元)')
    """同期金额(元):"""

    ThisPeriodAccount: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatement', column_name='ThisPeriodAccount', column_type='decimal(22,6)', nullable=False, chn_name='本期金额(元)')
    """本期金额(元):"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatement', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatement', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatement', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到港股的交易代码、简称等。"""

    InsertTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatement', column_name='InsertTime', column_type='datetime', nullable=False, chn_name='发布时间')
    """发布时间:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatement', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatement', column_name='InfoSource', column_type='varchar(100)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    SN: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatement', column_name='SN', column_type='int', nullable=False, chn_name='序号')
    """序号:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatement', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    PeriodMark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatement', column_name='PeriodMark', column_type='int', nullable=False, chn_name='日期标志')
    """日期标志:日期标志(PeriodMark)与(CT_SystemConst)表中的DM字段关联，令LB = 1314，得到日期标志的具体描述：1-1个月，2-2个月，3-3个月，4-4个月，5-5个月，6-半年度，7-7个月，8-8个月，9-9个月，10-10个月，11-11个月，12-年度，13-13个月，14-14个月，15-15个月，16-16个月，17-17个..."""

    FiscalYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatement', column_name='FiscalYear', column_type='datetime', nullable=False, chn_name='财政年度')
    """财政年度:"""

    CompanyNature: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatement', column_name='CompanyNature', column_type='int', nullable=False, chn_name='公司性质')
    """公司性质:公司性质(CompanyNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1356，得到公司性质的具体描述：1-普通，2-金融，3-保险，4-房地产，5-银行。"""

