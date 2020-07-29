# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_MainOperIncome(SQLTableEntity):
    name: str = 'LC_MainOperIncome'
    
    chn_name: str = '公司主营业务构成'
    
    business_unique: str = 'CompanyCode,EndDate,DateType,IfMerged,IfAdjusted,Classification,Project'
    
    refresh_freq: str = """季更新"""
    
    comment: str = """1收录公司主营业务的收入来源、成本构成；主营业务收入、成本和利润与上年同期的对比较。
2.数据范围：1998-12-31至今
3.信息来源：招股说明书、定报、审计报告等"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainOperIncome', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    Project: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainOperIncome', column_name='Project', column_type='varchar(255)', nullable=False, chn_name='经营项目名称')
    """经营项目名称:"""

    Industry: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainOperIncome', column_name='Industry', column_type='int', nullable=False, chn_name='所属行业')
    """所属行业:"""

    RegionAndBusiness: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainOperIncome', column_name='RegionAndBusiness', column_type='int', nullable=False, chn_name='地区与业务性质')
    """地区与业务性质:地区与业务性质(RegionAndBusiness)与(CT_SystemConst)表中的DM字段关联，令LB = 1042，得到地区与业务性质的具体描述：11-国内，12-港澳台，13-国外，19-其他地区，30-进出口，31-进口，33-出口，51-内部抵减抵销，52-关联交易，59-其他性质，99-合计。"""

    MainOperIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainOperIncome', column_name='MainOperIncome', column_type='decimal(19,4)', nullable=False, chn_name='主营业务收入(元)')
    """主营业务收入(元):"""

    MainOperCost: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainOperIncome', column_name='MainOperCost', column_type='decimal(19,4)', nullable=False, chn_name='主营业务成本(元)')
    """主营业务成本(元):"""

    MainOperProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainOperIncome', column_name='MainOperProfit', column_type='decimal(19,4)', nullable=False, chn_name='主营业务利润(元)')
    """主营业务利润(元):"""

    MainOperIncomeFormerYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainOperIncome', column_name='MainOperIncomeFormerYear', column_type='decimal(19,4)', nullable=False, chn_name='上年同期主营业务收入(元)')
    """上年同期主营业务收入(元):"""

    MainOperCostFormerYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainOperIncome', column_name='MainOperCostFormerYear', column_type='decimal(19,4)', nullable=False, chn_name='上年同期主营业务成本(元)')
    """上年同期主营业务成本(元):"""

    MainOperProfitFormerYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainOperIncome', column_name='MainOperProfitFormerYear', column_type='decimal(19,4)', nullable=False, chn_name='上年同期主营业务利润(元)')
    """上年同期主营业务利润(元):"""

    MainIncomeGrowRateYOY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainOperIncome', column_name='MainIncomeGrowRateYOY', column_type='decimal(18,4)', nullable=False, chn_name='主营业务收入同比')
    """主营业务收入同比:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainOperIncome', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。"""

    MainICostGrowRateYOY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainOperIncome', column_name='MainICostGrowRateYOY', column_type='decimal(18,4)', nullable=False, chn_name='主营业务成本同比')
    """主营业务成本同比:"""

    MainProfitGrowRateYOY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainOperIncome', column_name='MainProfitGrowRateYOY', column_type='decimal(18,4)', nullable=False, chn_name='主营业务利润同比')
    """主营业务利润同比:"""

    GrossProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainOperIncome', column_name='GrossProfit', column_type='decimal(10,8)', nullable=False, chn_name='毛利率')
    """毛利率:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainOperIncome', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='修改日期')
    """修改日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainOperIncome', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainOperIncome', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    DateType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainOperIncome', column_name='DateType', column_type='int', nullable=False, chn_name='日期类型')
    """日期类型:日期类型(DateType)与(CT_SystemConst)表中的DM字段关联，令LB = 1074，得到日期类型的具体描述：1-月份，2-季度，3-期末累计，4-当月及累计，5-日，6-周，7-旬，8-半月，9-年度，11-上年同月，12-上年同期，13-上年同季，14-期末，21-上月=100，22-2005年=100，23-2005年=100（季度）..."""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainOperIncome', column_name='InfoSource', column_type='varchar(100)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    IfMerged: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainOperIncome', column_name='IfMerged', column_type='int', nullable=False, chn_name='合并标志')
    """合并标志:合并标志(IfMerged)与(CT_SystemConst)表中的DM字段关联，令LB = 1189，得到合并标志的具体描述：1-合并，2-母公司，3-合并调整，4-母公司调整，5-合并修正前，6-母公司修正前，7-专项合并。"""

    IfAdjusted: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainOperIncome', column_name='IfAdjusted', column_type='int', nullable=False, chn_name='调整标志')
    """调整标志:调整标志(IfAdjusted)：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令“LB=1188”，得到财务报表“调整标志”的具体描述。1-是，2-否，3-前，其中3-前代表数据更正的时候，会把之前的数据的调整标志改成前，此处理2010年开始废弃。"""

    Classification: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainOperIncome', column_name='Classification', column_type='int', nullable=False, chn_name='分类方式')
    """分类方式:分类方式(Classification)与(CT_SystemConst)表中的DM字段关联，令LB = 1046，得到分类方式的具体描述：10-按行业，20-按产品，30-按地区，50-按业务。"""

    SN: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainOperIncome', column_name='SN', column_type='int', nullable=False, chn_name='序号')
    """序号:"""

