# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_IncomeStatementCN(SQLTableEntity):
    name: str = 'HK_IncomeStatementCN'
    
    chn_name: str = '港股利润分配表(中国会计准则)'
    
    business_unique: str = 'CompanyCode,EndDate,PeriodMark,Mark,CurrencyUnit'
    
    refresh_freq: str = """滚动更新"""
    
    comment: str = """1.介绍按中国会计准则披露的港股利润分配表中各项指标，该表为利润分配表的横表，标准会计科目与A股基本相同。
2.数据范围：2002年至今。
3.数据来源：港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    CurrencyUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='CurrencyUnit', column_type='int', nullable=True, chn_name='货币单位')
    """货币单位:货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB=1068，得到货币单位的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，1170-约旦第纳尔，1180-科威特..."""

    TotOpeRev: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='TotOpeRev', column_type='decimal(19,4)', nullable=False, chn_name='一、营业总收入')
    """一、营业总收入:若营业总收入为空，则以营业收入+利息净收入+手续费及佣金净收入+已赚保费+其他业务收入+营业收入特殊项目+营业收入调整项目更新。"""

    OpeRev: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='OpeRev', column_type='decimal(19,4)', nullable=False, chn_name='营业收入')
    """营业收入:"""

    NetIntInc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='NetIntInc', column_type='decimal(19,4)', nullable=False, chn_name='利息净收入')
    """利息净收入:若利息净收入为空，则以利息收入+利息支出更新"""

    IntInc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='IntInc', column_type='decimal(19,4)', nullable=False, chn_name='其中:利息收入')
    """其中:利息收入:"""

    IntExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='IntExpense', column_type='decimal(19,4)', nullable=False, chn_name='其中:利息支出')
    """其中:利息支出:"""

    NetComInc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='NetComInc', column_type='decimal(19,4)', nullable=False, chn_name='手续费及佣金净收入')
    """手续费及佣金净收入:若手续费及佣金净收入为空，则以手续费及佣金收入+手续费及佣金支出+代理买卖证券业务净收入+证券承销业务净收入+受托客户资产管理业务净收入更新。"""

    ComIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='ComIncome', column_type='decimal(19,4)', nullable=False, chn_name='其中:手续费及佣金收入')
    """其中:手续费及佣金收入:"""

    ComExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='ComExpense', column_type='decimal(19,4)', nullable=False, chn_name='其中:手续费及佣金支出')
    """其中:手续费及佣金支出:"""

    NetProSecuInc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='NetProSecuInc', column_type='decimal(19,4)', nullable=False, chn_name='其中:代理买卖证券业务净收入')
    """其中:代理买卖证券业务净收入:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到所属公司股票的交易代码、简称等。"""

    NetSubSecuInc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='NetSubSecuInc', column_type='decimal(19,4)', nullable=False, chn_name='其中:证券承销业务净收入')
    """其中:证券承销业务净收入:"""

    NetTrustInc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='NetTrustInc', column_type='decimal(19,4)', nullable=False, chn_name='其中:受托客户资产管理业务净收入')
    """其中:受托客户资产管理业务净收入:"""

    PremiEarned: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='PremiEarned', column_type='decimal(19,4)', nullable=False, chn_name='已赚保费')
    """已赚保费:若已赚保费为空，则以利息收入+利息支出更新。"""

    PremiIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='PremiIncome', column_type='decimal(19,4)', nullable=False, chn_name='保险业务收入')
    """保险业务收入:"""

    ReinIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='ReinIncome', column_type='decimal(19,4)', nullable=False, chn_name='其中:分保费收入')
    """其中:分保费收入:"""

    Reinsurance: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='Reinsurance', column_type='decimal(19,4)', nullable=False, chn_name='减:分出保费')
    """减:分出保费:"""

    UneaPremRes: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='UneaPremRes', column_type='decimal(19,4)', nullable=False, chn_name='减:提取未到期责任准备金')
    """减:提取未到期责任准备金:"""

    OtherOpeRev: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='OtherOpeRev', column_type='decimal(19,4)', nullable=False, chn_name='其他业务收入')
    """其他业务收入:"""

    SpeItemsOR: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='SpeItemsOR', column_type='decimal(19,4)', nullable=False, chn_name='营业收入特殊项目')
    """营业收入特殊项目:"""

    AdjItemsOR: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='AdjItemsOR', column_type='decimal(19,4)', nullable=False, chn_name='营业收入调整项目')
    """营业收入调整项目:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    TotOpeCost: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='TotOpeCost', column_type='decimal(19,4)', nullable=False, chn_name='二、营业总成本')
    """二、营业总成本:若营业总成本为空，则以营业支出+退保金+赔付支出-减：摊回赔付支出+提取保险责任准备金-减：摊回保险责任准备金+保单红利支出+分保费用+业务及管理费-减：摊回分保费用+保险手续费及佣金支出+其他业务成本-减：营业成本+营业税费/营业税金及附加+销售费用+管理费用+财务费用+资产减值损失+营业支出特殊项目+营业支出调整项目更新。"""

    OpeCost: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='OpeCost', column_type='decimal(19,4)', nullable=False, chn_name='营业支出')
    """营业支出:"""

    RefPrem: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='RefPrem', column_type='decimal(19,4)', nullable=False, chn_name='退保金')
    """退保金:"""

    CompExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='CompExpense', column_type='decimal(19,4)', nullable=False, chn_name='赔付支出')
    """赔付支出:"""

    AmorExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='AmorExpense', column_type='decimal(19,4)', nullable=False, chn_name='减:摊回赔付支出')
    """减:摊回赔付支出:"""

    PremReserve: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='PremReserve', column_type='decimal(19,4)', nullable=False, chn_name='提取保险责任准备金')
    """提取保险责任准备金:"""

    AmorPremRes: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='AmorPremRes', column_type='decimal(19,4)', nullable=False, chn_name='减:摊回保险责任准备金')
    """减:摊回保险责任准备金:"""

    PolDivPayout: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='PolDivPayout', column_type='decimal(19,4)', nullable=False, chn_name='保单红利支出')
    """保单红利支出:"""

    ReinCost: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='ReinCost', column_type='decimal(19,4)', nullable=False, chn_name='分保费用')
    """分保费用:"""

    OpeAndAdmExp: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='OpeAndAdmExp', column_type='decimal(19,4)', nullable=False, chn_name='业务及管理费')
    """业务及管理费:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='InfoSource', column_type='varchar(100)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    AmorReinCost: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='AmorReinCost', column_type='decimal(19,4)', nullable=False, chn_name='减:摊回分保费用')
    """减:摊回分保费用:"""

    InsComExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='InsComExpense', column_type='decimal(19,4)', nullable=False, chn_name='保险手续费及佣金支出')
    """保险手续费及佣金支出:"""

    OtherOpeCost: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='OtherOpeCost', column_type='decimal(19,4)', nullable=False, chn_name='其他业务成本')
    """其他业务成本:"""

    OpeaCost: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='OpeaCost', column_type='decimal(19,4)', nullable=False, chn_name='减:营业成本')
    """减:营业成本:"""

    OpeTaxSurcha: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='OpeTaxSurcha', column_type='decimal(19,4)', nullable=False, chn_name='营业税费/营业税金及附加')
    """营业税费/营业税金及附加:"""

    OpeExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='OpeExpense', column_type='decimal(19,4)', nullable=False, chn_name='销售费用')
    """销售费用:"""

    AdmExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='AdmExpense', column_type='decimal(19,4)', nullable=False, chn_name='管理费用')
    """管理费用:"""

    FinExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='FinExpense', column_type='decimal(19,4)', nullable=False, chn_name='财务费用')
    """财务费用:"""

    AssetImpLoss: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='AssetImpLoss', column_type='decimal(19,4)', nullable=False, chn_name='资产减值损失')
    """资产减值损失:"""

    SpeItemsOP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='SpeItemsOP', column_type='decimal(19,4)', nullable=False, chn_name='营业支出特殊项目')
    """营业支出特殊项目:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    AdjItemsOP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='AdjItemsOP', column_type='decimal(19,4)', nullable=False, chn_name='营业支出调整项目')
    """营业支出调整项目:"""

    FairValChaInc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='FairValChaInc', column_type='decimal(19,4)', nullable=False, chn_name='加:公允价值变动净收益')
    """加:公允价值变动净收益:"""

    InvInc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='InvInc', column_type='decimal(19,4)', nullable=False, chn_name='加:投资净收益')
    """加:投资净收益:"""

    InvIncAsso: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='InvIncAsso', column_type='decimal(19,4)', nullable=False, chn_name='其中:对联营合营企业的投资收益')
    """其中:对联营合营企业的投资收益:"""

    ExcIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='ExcIncome', column_type='decimal(19,4)', nullable=False, chn_name='汇兑收益')
    """汇兑收益:"""

    OtherItemsEffOP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='OtherItemsEffOP', column_type='decimal(19,4)', nullable=False, chn_name='加:影响营业利润的其他科目')
    """加:影响营业利润的其他科目:"""

    AdjItemsEffOP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='AdjItemsEffOP', column_type='decimal(19,4)', nullable=False, chn_name='加:影响营业利润的调整项目')
    """加:影响营业利润的调整项目:"""

    OpeProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='OpeProfit', column_type='decimal(19,4)', nullable=False, chn_name='三、营业利润')
    """三、营业利润:若营业利润为空，则以营业总收入-营业总成本+公允价值变动净收益+投资净收益+汇兑收益+影响营业利润的其他科目+影响营业利润的调整项目更新。"""

    NonopeIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='NonopeIncome', column_type='decimal(19,4)', nullable=False, chn_name='加:营业外收入')
    """加:营业外收入:"""

    NonCurAsDEarn: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='NonCurAsDEarn', column_type='decimal(19,4)', nullable=False, chn_name='其中:非流动资产处置净利得')
    """其中:非流动资产处置净利得:"""

    PeriodMark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='PeriodMark', column_type='int', nullable=True, chn_name='日期标志')
    """日期标志:日期标志(PeriodMark)与(CT_SystemConst)表中的DM字段关联，令LB=1314，得到日期标志的具体描述：1-1个月，2-2个月，3-3个月，4-4个月，5-5个月，6-半年度，7-7个月，8-8个月，9-9个月，10-10个月，11-11个月，12-年度，13-13个月，14-14个月，15-15个月，16-16个月，17-17个月，..."""

    NonopeExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='NonopeExpense', column_type='decimal(19,4)', nullable=False, chn_name='减:营业外支出')
    """减:营业外支出:"""

    NonCurAssDLoss: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='NonCurAssDLoss', column_type='decimal(19,4)', nullable=False, chn_name='其中:非流动资产处置净损失')
    """其中:非流动资产处置净损失:"""

    OtherItemsEffTP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='OtherItemsEffTP', column_type='decimal(19,4)', nullable=False, chn_name='加:影响利润总额的其他科目')
    """加:影响利润总额的其他科目:"""

    AdjItemsEffTP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='AdjItemsEffTP', column_type='decimal(19,4)', nullable=False, chn_name='加:影响利润总额的调整项目')
    """加:影响利润总额的调整项目:"""

    TotalProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='TotalProfit', column_type='decimal(19,4)', nullable=False, chn_name='四、利润总额')
    """四、利润总额:若利润总额为空，则以营业利润+营业外收入-减：营业外支出+影响利润总额的其他科目+影响利润总额的调整项目更新。"""

    IncTaxCost: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='IncTaxCost', column_type='decimal(19,4)', nullable=False, chn_name='减:所得税')
    """减:所得税:"""

    UncerInvLosses: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='UncerInvLosses', column_type='decimal(19,4)', nullable=False, chn_name='加:未确认的投资损失')
    """加:未确认的投资损失:"""

    OtherItemsEffNP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='OtherItemsEffNP', column_type='decimal(19,4)', nullable=False, chn_name='加:影响净利润的其他科目')
    """加:影响净利润的其他科目:"""

    AdjItemsEffNP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='AdjItemsEffNP', column_type='decimal(19,4)', nullable=False, chn_name='加:影响净利润的调整项目')
    """加:影响净利润的调整项目:"""

    NetProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='NetProfit', column_type='decimal(19,4)', nullable=False, chn_name='五、净利润')
    """五、净利润:若净利润为空，则以利润总额-所得税+未确认的投资损失+影响净利润的其他科目+影响净利润的调整项目更新。"""

    FiscalYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='FiscalYear', column_type='datetime', nullable=False, chn_name='财政年度')
    """财政年度:"""

    NPPCompOwners: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='NPPCompOwners', column_type='decimal(19,4)', nullable=False, chn_name='归属于母公司所有者的净利润')
    """归属于母公司所有者的净利润:"""

    MinoProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='MinoProfit', column_type='decimal(19,4)', nullable=False, chn_name='少数股东损益')
    """少数股东损益:"""

    OthItemsEffNPP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='OthItemsEffNPP', column_type='decimal(19,4)', nullable=False, chn_name='加:影响母公司净利润的特殊项目')
    """加:影响母公司净利润的特殊项目:"""

    AdjItemsEffNPP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='AdjItemsEffNPP', column_type='decimal(19,4)', nullable=False, chn_name='加:影响母公司净利润的调整项目')
    """加:影响母公司净利润的调整项目:"""

    OCIAfterTax: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='OCIAfterTax', column_type='decimal(19,4)', nullable=False, chn_name='六、其他综合收益的税后净额')
    """六、其他综合收益的税后净额:"""

    OCIATPComOWNR: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='OCIATPComOWNR', column_type='decimal(19,4)', nullable=False, chn_name='归属于母公司所有者的其他综合收益的税后净额')
    """归属于母公司所有者的其他综合收益的税后净额:"""

    OCINotInIS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='OCINotInIS', column_type='decimal(19,4)', nullable=False, chn_name='(一)以后不能重分类进损益的其他综合收益')
    """(一)以后不能重分类进损益的其他综合收益:"""

    OCIReMearsure: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='OCIReMearsure', column_type='decimal(19,4)', nullable=False, chn_name='1.1重新计量设定收益计划净负债或净资产的变动')
    """1.1重新计量设定收益计划净负债或净资产的变动:"""

    OCIEquitNotInIS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='OCIEquitNotInIS', column_type='decimal(19,4)', nullable=False, chn_name='1.2权益法下在被投资单位不能重分类进损益的其他综合')
    """1.2权益法下在被投资单位不能重分类进损益的其他综合:"""

    OCIInIS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='OCIInIS', column_type='decimal(19,4)', nullable=False, chn_name='(二)以后将重分类进损益的其他综合收益')
    """(二)以后将重分类进损益的其他综合收益:"""

    CompanyNature: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='CompanyNature', column_type='int', nullable=False, chn_name='公司性质')
    """公司性质:公司性质(CompanyNature)与(CT_SystemConst)表中的DM字段关联，令LB=1356，得到公司性质的具体描述：1-普通，2-金融，3-保险，4-房地产，5-银行。"""

    OCIEquityInIS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='OCIEquityInIS', column_type='decimal(19,4)', nullable=False, chn_name='2.1权益法下在被投资单位以后将重分类进损益的其他综合')
    """2.1权益法下在被投资单位以后将重分类进损益的其他综合:"""

    OCIFairValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='OCIFairValue', column_type='decimal(19,4)', nullable=False, chn_name='2.2可供出售金融资产公允价值变动损益')
    """2.2可供出售金融资产公允价值变动损益:"""

    OCIToMaturityFA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='OCIToMaturityFA', column_type='decimal(19,4)', nullable=False, chn_name='2.3持有至到期投资重分类为可供出售金融资产损益')
    """2.3持有至到期投资重分类为可供出售金融资产损益:"""

    OCICFLoss: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='OCICFLoss', column_type='decimal(19,4)', nullable=False, chn_name='2.4现金流量套期损益的有效部分')
    """2.4现金流量套期损益的有效部分:"""

    OCIFGNCurFSA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='OCIFGNCurFSA', column_type='decimal(19,4)', nullable=False, chn_name='2.5外币财务报表折算差额')
    """2.5外币财务报表折算差额:"""

    OCIOthers: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='OCIOthers', column_type='decimal(19,4)', nullable=False, chn_name='2.6其他(以后能重分类进损益表的其他综合收益)')
    """2.6其他(以后能重分类进损益表的其他综合收益):"""

    OCIATMinorOwner: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='OCIATMinorOwner', column_type='decimal(19,4)', nullable=False, chn_name='归属于少数股东的其他综合收益的税后净额')
    """归属于少数股东的其他综合收益的税后净额:"""

    AdjItemsEffCI: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='AdjItemsEffCI', column_type='decimal(19,4)', nullable=False, chn_name='加:影响综合收益总额的调整项目')
    """加:影响综合收益总额的调整项目:"""

    TotCompoIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='TotCompoIncome', column_type='decimal(19,4)', nullable=False, chn_name='七、综合收益总额')
    """七、综合收益总额:"""

    CIPCompOwners: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='CIPCompOwners', column_type='decimal(19,4)', nullable=False, chn_name='归属于母公司所有者的综合收益总额')
    """归属于母公司所有者的综合收益总额:"""

    Mark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='Mark', column_type='int', nullable=True, chn_name='合并调整标志')
    """合并调整标志:合并调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB=1511，得到合并调整标志的具体描述：1-合并调整，2-合并未调整，3-母公司调整，4-母公司未调整，5-专项合并调整，6-专项合并未调整。"""

    CIMinoOwners: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='CIMinoOwners', column_type='decimal(19,4)', nullable=False, chn_name='归属于少数股东的综合收益总额')
    """归属于少数股东的综合收益总额:"""

    AdjItemsEffPCI: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='AdjItemsEffPCI', column_type='decimal(19,4)', nullable=False, chn_name='加:影响母公司综合收益总额的调整项目')
    """加:影响母公司综合收益总额的调整项目:"""

    BasicEPS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='BasicEPS', column_type='decimal(18,6)', nullable=False, chn_name='基本每股收益')
    """基本每股收益:"""

    DilutedEPS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='DilutedEPS', column_type='decimal(18,6)', nullable=False, chn_name='稀释每股收益')
    """稀释每股收益:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_IncomeStatementCN', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

