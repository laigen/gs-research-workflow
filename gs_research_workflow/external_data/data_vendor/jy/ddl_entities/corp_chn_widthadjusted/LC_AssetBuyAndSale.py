# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_AssetBuyAndSale(SQLTableEntity):
    name: str = 'LC_AssetBuyAndSale'
    
    chn_name: str = '公司资产收购与出售明细'
    
    business_unique: str = '表结构不适应最新定报披露格式'
    
    refresh_freq: str = """停止更新"""
    
    comment: str = """1.年报和半年报中报告的资产收购与出售情况，包括时间主体/交易对象名称、企业编号、与上市公司关联关系、涉及资产、交易日期、交易价格、贡献利润、损益等指标。
2.数据范围：2004-2015
2.信息来源：上市公司公告"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AssetBuyAndSale', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    ObjectName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AssetBuyAndSale', column_name='ObjectName', column_type='varchar(200)', nullable=False, chn_name='交易对象名称')
    """交易对象名称:"""

    ObjectCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AssetBuyAndSale', column_name='ObjectCode', column_type='int', nullable=False, chn_name='交易对象企业编号')
    """交易对象企业编号:"""

    ObjectAssociation: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AssetBuyAndSale', column_name='ObjectAssociation', column_type='int', nullable=False, chn_name='与上市公司关联关系')
    """与上市公司关联关系:与上市公司关联关系(ObjectAssociation)与(CT_SystemConst)表中的DM字段关联，令LB = 1036，得到与上市公司关联关系的具体描述：1-本公司，2-母公司，3-控股股东，4-非控股股东，5-兄弟企业，8-间接非控股股东，9-同一领导人、亲属关系，10-下属子公司、参股公司，11-项目合作合资方，12-其他关联关系，51-间接..."""

    TargetAsset: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AssetBuyAndSale', column_name='TargetAsset', column_type='varchar(500)', nullable=False, chn_name='涉及资产')
    """涉及资产:"""

    CounterPartyAsset: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AssetBuyAndSale', column_name='CounterPartyAsset', column_type='varchar(1000)', nullable=False, chn_name='交易对方及涉及资产')
    """交易对方及涉及资产:"""

    TradingDay: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AssetBuyAndSale', column_name='TradingDay', column_type='datetime', nullable=False, chn_name='交易日期')
    """交易日期:"""

    CurrencyUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AssetBuyAndSale', column_name='CurrencyUnit', column_type='int', nullable=False, chn_name='交易货币单位')
    """交易货币单位:交易货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068，得到交易货币单位的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，1170-约旦第纳尔，11..."""

    Price: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AssetBuyAndSale', column_name='Price', column_type='decimal(19,4)', nullable=False, chn_name='交易价格')
    """交易价格:"""

    ProfitToReportPeriod: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AssetBuyAndSale', column_name='ProfitToReportPeriod', column_type='decimal(19,4)', nullable=False, chn_name='报告期贡献利润')
    """报告期贡献利润:"""

    TradeProfitOrLoss: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AssetBuyAndSale', column_name='TradeProfitOrLoss', column_type='decimal(19,4)', nullable=False, chn_name='交易产生的损益')
    """交易产生的损益:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AssetBuyAndSale', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。"""

    IfConnectedTransaction: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AssetBuyAndSale', column_name='IfConnectedTransaction', column_type='int', nullable=False, chn_name='是否为关联交易')
    """是否为关联交易:是否为关联交易（IfConnectedTransaction）：该字段固定以下常量：0->否1->是"""

    PricingRule: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AssetBuyAndSale', column_name='PricingRule', column_type='varchar(500)', nullable=False, chn_name='定价原则')
    """定价原则:"""

    IfOwnershipTransfered: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AssetBuyAndSale', column_name='IfOwnershipTransfered', column_type='int', nullable=False, chn_name='涉及资产产权是否全部过户')
    """涉及资产产权是否全部过户:涉及资产产权是否全部过户（IfOwnershipTransfered）：该字段固定以下常量：0->否1->是"""

    IfDebtTransfered: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AssetBuyAndSale', column_name='IfDebtTransfered', column_type='int', nullable=False, chn_name='涉及债权债务是否全部转移')
    """涉及债权债务是否全部转移:涉及债权债务是否全部转移（IfDebtTransfered）：该字段固定以下常量：0->否1->是"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AssetBuyAndSale', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='修改日期')
    """修改日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AssetBuyAndSale', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AssetBuyAndSale', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AssetBuyAndSale', column_name='InfoSource', column_type='varchar(100)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AssetBuyAndSale', column_name='EndDate', column_type='datetime', nullable=False, chn_name='截止日期')
    """截止日期:"""

    EventType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AssetBuyAndSale', column_name='EventType', column_type='int', nullable=False, chn_name='事项类型')
    """事项类型:事项类型(EventType)与(CT_SystemConst)表中的DM字段关联，令LB = 1162，得到事项类型的具体描述：10-募集资金使用，13-重大担保，15-关联债权债务，17-委托理财，19-关联交易，21-关联销售和采购，31-应收帐款，32-其他应收款，33-预付帐款，41-收购资产，43-出售资产，99-其他事项，1001-募集资金总额..."""

    SubjectName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AssetBuyAndSale', column_name='SubjectName', column_type='varchar(200)', nullable=False, chn_name='事件主体名称')
    """事件主体名称:"""

    SubjectCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AssetBuyAndSale', column_name='SubjectCode', column_type='int', nullable=False, chn_name='事件主体企业编号')
    """事件主体企业编号:"""

    SubjectAssociation: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AssetBuyAndSale', column_name='SubjectAssociation', column_type='int', nullable=False, chn_name='与上市公司关联关系')
    """与上市公司关联关系:与上市公司关联关系(SubjectAssociation)与(CT_SystemConst)表中的DM字段关联，令LB = 1036，得到与上市公司关联关系的具体描述：1-本公司，2-母公司，3-控股股东，4-非控股股东，5-兄弟企业，8-间接非控股股东，9-同一领导人、亲属关系，10-下属子公司、参股公司，11-项目合作合资方，12-其他关联关系，51-间..."""

