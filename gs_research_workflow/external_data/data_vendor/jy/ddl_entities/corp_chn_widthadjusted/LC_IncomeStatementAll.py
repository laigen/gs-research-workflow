# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_IncomeStatementAll(SQLTableEntity):
    name: str = 'LC_IncomeStatementAll'
    
    chn_name: str = '利润分配表_新会计准则'
    
    business_unique: str = 'InfoPublDate,CompanyCode,EndDate,IfAdjusted,IfMerged'
    
    refresh_freq: str = """季更新"""
    
    comment: str = """1.反映上市公司依据2007年新会计准则在在年报、中报、季报中披露的利润表数据；并依据新旧会计准则的科目对应关系，收录了主要科目的历史对应数据。
2.收录同一公司在报告期末的四种财务报告，即未调整的合并报表、未调整的母公司报表、调整后的合并报表以及调整后的母公司报表。
3.若某个报告期的数据有多次调整，则该表展示历次调整数据。
4.该表中各财务科目的单位均为人民币元。
5.带“##”的特殊项目为单个公司披露的非标准化的科目，对应的“特殊字段说明”字段将对其作出说明；带“##”的调整项目是为了让报表的各个小项借贷平衡而设置的，便于客户对报表的遗漏和差错进行判断。
6.数据范围：1989-12-31至今
7.信息来源：招股说明书、定报、审计报告等"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    EnterpriseType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='EnterpriseType', column_type='int', nullable=True, chn_name='企业性质')
    """企业性质:企业性质(EnterpriseType)与(CT_SystemConst)表中的DM字段关联，令LB = 1414 AND DM IN (13,31,33,35,39,99)，得到企业性质的具体描述：13-商业银行，31-证券公司，33-信托公司，35-保险公司，39-其他非银行金融机构，99-一般企业。"""

    OthDebtInvesChange: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OthDebtInvesChange', column_type='decimal(19,4)', nullable=False, chn_name='2.7其他债权投资公允价值变动')
    """2.7其他债权投资公允价值变动:"""

    FinAssetROtherCI: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='FinAssetROtherCI', column_type='decimal(19,4)', nullable=False, chn_name='2.8金融资产重分类计入其他综合收益的金额')
    """2.8金融资产重分类计入其他综合收益的金额:"""

    OtherDebtInvestCIP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OtherDebtInvestCIP', column_type='decimal(19,4)', nullable=False, chn_name='2.9其他债权投资信用减值准备')
    """2.9其他债权投资信用减值准备:"""

    OCIMinorityOwners: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OCIMinorityOwners', column_type='decimal(19,4)', nullable=False, chn_name='归属于少数股东的其他综合收益总额')
    """归属于少数股东的其他综合收益总额:"""

    AdjustedItemsEffectingCI: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='AdjustedItemsEffectingCI', column_type='decimal(19,4)', nullable=False, chn_name='加:##影响综合收益总额的调整项目')
    """加:##影响综合收益总额的调整项目:"""

    TotalCompositeIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='TotalCompositeIncome', column_type='decimal(19,4)', nullable=False, chn_name='八、综合收益总额')
    """八、综合收益总额:"""

    CIParentCompanyOwners: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='CIParentCompanyOwners', column_type='decimal(19,4)', nullable=False, chn_name='归属于母公司所有者的综合收益总额')
    """归属于母公司所有者的综合收益总额:"""

    CIMinorityOwners: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='CIMinorityOwners', column_type='decimal(19,4)', nullable=False, chn_name='归属于少数股东的综合收益总额')
    """归属于少数股东的综合收益总额:"""

    AdjustedItemsEffectingPCI: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='AdjustedItemsEffectingPCI', column_type='decimal(19,4)', nullable=False, chn_name='加:##影响母公司综合收益总额的调整项目')
    """加:##影响母公司综合收益总额的调整项目:"""

    BasicEPS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='BasicEPS', column_type='decimal(19,4)', nullable=False, chn_name='基本每股收益')
    """基本每股收益:"""

    IfComplete: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='IfComplete', column_type='int', nullable=False, chn_name='完整标志')
    """完整标志:完整标志(IfComplete)与(CT_SystemConst)表中的DM字段关联，令LB = 1444，得到完整标志的具体描述：1-完整报表，2-简表，3-个别字段修正报表。"""

    DilutedEPS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='DilutedEPS', column_type='decimal(19,4)', nullable=False, chn_name='稀释每股收益')
    """稀释每股收益:"""

    SpecialFieldRemark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='SpecialFieldRemark', column_type='varchar(1000)', nullable=False, chn_name='特殊字段说明')
    """特殊字段说明:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    TotalOperatingRevenue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='TotalOperatingRevenue', column_type='decimal(19,4)', nullable=False, chn_name='一、营业总收入')
    """一、营业总收入:营业总收入（TotalOperatingRevenue）：对非金融类公司（企业性质=99），营业总收入=营业收入＋金融类特殊收入项目＋其他业务收入，注：“金融类特殊收入项目”包括：利息收入、手续费及佣金收入、已赚保费、营业收入特殊项目、调整项目；对金融类公司（企业性质不等于99），营业总收入=营业收入"""

    OperatingRevenue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OperatingRevenue', column_type='decimal(19,4)', nullable=False, chn_name='营业收入')
    """营业收入:"""

    NetInterestIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='NetInterestIncome', column_type='decimal(19,4)', nullable=False, chn_name='利息净收入')
    """利息净收入:"""

    InterestIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='InterestIncome', column_type='decimal(19,4)', nullable=False, chn_name='其中:利息收入')
    """其中:利息收入:"""

    InterestExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='InterestExpense', column_type='decimal(19,4)', nullable=False, chn_name='其中:利息支出')
    """其中:利息支出:"""

    NetCommissionIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='NetCommissionIncome', column_type='decimal(19,4)', nullable=False, chn_name='手续费及佣金净收入')
    """手续费及佣金净收入:"""

    CommissionIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='CommissionIncome', column_type='decimal(19,4)', nullable=False, chn_name='其中:手续费及佣金收入')
    """其中:手续费及佣金收入:"""

    CommissionExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='CommissionExpense', column_type='decimal(19,4)', nullable=False, chn_name='其中:手续费及佣金支出')
    """其中:手续费及佣金支出:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='InfoPublDate', column_type='datetime', nullable=True, chn_name='信息发布日期')
    """信息发布日期:"""

    NetProxySecuIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='NetProxySecuIncome', column_type='decimal(19,4)', nullable=False, chn_name='其中:代理买卖证券业务净收入')
    """其中:代理买卖证券业务净收入:"""

    NetSubIssueSecuIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='NetSubIssueSecuIncome', column_type='decimal(19,4)', nullable=False, chn_name='其中:证券承销业务净收入')
    """其中:证券承销业务净收入:"""

    NetTrustIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='NetTrustIncome', column_type='decimal(19,4)', nullable=False, chn_name='其中:受托客户资产管理业务净收入')
    """其中:受托客户资产管理业务净收入:"""

    PremiumsEarned: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='PremiumsEarned', column_type='decimal(19,4)', nullable=False, chn_name='已赚保费')
    """已赚保费:"""

    PremiumsIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='PremiumsIncome', column_type='decimal(19,4)', nullable=False, chn_name='保险业务收入')
    """保险业务收入:"""

    ReinsuranceIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='ReinsuranceIncome', column_type='decimal(19,4)', nullable=False, chn_name='其中:分保费收入')
    """其中:分保费收入:"""

    Reinsurance: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='Reinsurance', column_type='decimal(19,4)', nullable=False, chn_name='减:分出保费')
    """减:分出保费:"""

    UnearnedPremiumReserve: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='UnearnedPremiumReserve', column_type='decimal(19,4)', nullable=False, chn_name='提取未到期责任准备金')
    """提取未到期责任准备金:"""

    OtherOperatingRevenue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OtherOperatingRevenue', column_type='decimal(19,4)', nullable=False, chn_name='其他营业收入')
    """其他营业收入:"""

    SpecialItemsOR: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='SpecialItemsOR', column_type='decimal(19,4)', nullable=False, chn_name='##营业收入特殊项目')
    """##营业收入特殊项目:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='InfoSource', column_type='varchar(100)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    AdjustmentItemsOR: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='AdjustmentItemsOR', column_type='decimal(19,4)', nullable=False, chn_name='##营业收入调整项目')
    """##营业收入调整项目:"""

    TotalOperatingCost: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='TotalOperatingCost', column_type='decimal(19,4)', nullable=False, chn_name='二、营业总成本')
    """二、营业总成本:营业总成本（TotalOperatingCost）：对非金融类公司（企业性质=99），营业总成本=营业成本＋营业税金及附加＋销售费用＋管理费用＋财务费用＋资产减值损失＋金融类特殊成本项目注：“金融类特殊成本项目”包括：利息支出、手续费及佣金支出、退保金、赔付支出、提取保险责任准备金、保单红利支出、分保费用、保险手续费及佣金支出、营业总成本特殊项目＋调整项目；..."""

    OperatingPayout: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OperatingPayout', column_type='decimal(19,4)', nullable=False, chn_name='营业支出')
    """营业支出:"""

    RefundedPremiums: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='RefundedPremiums', column_type='decimal(19,4)', nullable=False, chn_name='退保金')
    """退保金:"""

    CompensationExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='CompensationExpense', column_type='decimal(19,4)', nullable=False, chn_name='赔付支出')
    """赔付支出:"""

    AmortizationExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='AmortizationExpense', column_type='decimal(19,4)', nullable=False, chn_name='减:摊回赔付支出')
    """减:摊回赔付支出:"""

    PremiumReserve: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='PremiumReserve', column_type='decimal(19,4)', nullable=False, chn_name='提取保险责任准备金')
    """提取保险责任准备金:"""

    AmortizationPremiumReserve: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='AmortizationPremiumReserve', column_type='decimal(19,4)', nullable=False, chn_name='减:摊回保险责任准备金')
    """减:摊回保险责任准备金:"""

    PolicyDividendPayout: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='PolicyDividendPayout', column_type='decimal(19,4)', nullable=False, chn_name='保单红利支出')
    """保单红利支出:"""

    ReinsuranceCost: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='ReinsuranceCost', column_type='decimal(19,4)', nullable=False, chn_name='分保费用')
    """分保费用:"""

    BulletinType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='BulletinType', column_type='int', nullable=False, chn_name='公告类别')
    """公告类别:公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311，得到公告类别的具体描述：10-发行上市书，20-定期报告，30-业绩快报，50-章程制度，70-临时公告，90-交易所通报，91-交易所临时停(复)牌公告，99-其他。"""

    OperatingAndAdminExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OperatingAndAdminExpense', column_type='decimal(19,4)', nullable=False, chn_name='业务及管理费')
    """业务及管理费:"""

    AmortizationReinsuranceCost: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='AmortizationReinsuranceCost', column_type='decimal(19,4)', nullable=False, chn_name='减:摊回分保费用')
    """减:摊回分保费用:"""

    InsuranceCommissionExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='InsuranceCommissionExpense', column_type='decimal(19,4)', nullable=False, chn_name='保险手续费及佣金支出')
    """保险手续费及佣金支出:"""

    OtherOperatingCost: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OtherOperatingCost', column_type='decimal(19,4)', nullable=False, chn_name='其他营业成本')
    """其他营业成本:"""

    OperatingCost: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OperatingCost', column_type='decimal(19,4)', nullable=False, chn_name='营业成本')
    """营业成本:"""

    OperatingTaxSurcharges: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OperatingTaxSurcharges', column_type='decimal(19,4)', nullable=False, chn_name='营业税金及附加')
    """营业税金及附加:"""

    OperatingExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OperatingExpense', column_type='decimal(19,4)', nullable=False, chn_name='销售费用')
    """销售费用:"""

    AdministrationExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='AdministrationExpense', column_type='decimal(19,4)', nullable=False, chn_name='管理费用')
    """管理费用:"""

    FinancialExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='FinancialExpense', column_type='decimal(19,4)', nullable=False, chn_name='财务费用')
    """财务费用:"""

    InterestFinExp: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='InterestFinExp', column_type='decimal(19,4)', nullable=False, chn_name='其中:利息费用(财务费用)')
    """其中:利息费用(财务费用):"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。"""

    InterestIncomeFin: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='InterestIncomeFin', column_type='decimal(19,4)', nullable=False, chn_name='其中:利息收入(财务费用)')
    """其中:利息收入(财务费用):"""

    RAndD: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='RAndD', column_type='decimal(19,4)', nullable=False, chn_name='研发费用')
    """研发费用:"""

    CreditImpairmentL: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='CreditImpairmentL', column_type='decimal(19,4)', nullable=False, chn_name='信用减值损失')
    """信用减值损失:"""

    AssetImpairmentLoss: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='AssetImpairmentLoss', column_type='decimal(19,4)', nullable=False, chn_name='资产减值损失')
    """资产减值损失:"""

    SpecialItemsTOC: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='SpecialItemsTOC', column_type='decimal(19,4)', nullable=False, chn_name='##营业总成本特殊项目')
    """##营业总成本特殊项目:"""

    AdjustmentItemsTOC: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='AdjustmentItemsTOC', column_type='decimal(19,4)', nullable=False, chn_name='##营业总成本调整项目')
    """##营业总成本调整项目:"""

    OtherNetRevenue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OtherNetRevenue', column_type='decimal(19,4)', nullable=False, chn_name='三、非经营性净收益')
    """三、非经营性净收益:非经营性净收益（OtherNetRevenue）：聚源计算合计项，仅针对非金融类公司。计算公式=公允价值变动净收益＋投资净收益＋汇兑收益＋非经营性净收益特殊项目＋调整项目注：对金融类公司，“特别收益/收入”下列示的项目：公允价值变动净收益、投资净收益、汇兑收益、非经营性净收益特殊项目、调整项目属于“营业收入”的子项目"""

    FairValueChangeIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='FairValueChangeIncome', column_type='decimal(19,4)', nullable=False, chn_name='公允价值变动净收益')
    """公允价值变动净收益:"""

    InvestIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='InvestIncome', column_type='decimal(19,4)', nullable=False, chn_name='投资净收益')
    """投资净收益:"""

    InvestIncomeAssociates: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='InvestIncomeAssociates', column_type='decimal(19,4)', nullable=False, chn_name='其中:对联营合营企业的投资收益')
    """其中:对联营合营企业的投资收益:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    NetOpenHedgeIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='NetOpenHedgeIncome', column_type='decimal(19,4)', nullable=False, chn_name='净敞口套期收益')
    """净敞口套期收益:"""

    ExchangeIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='ExchangeIncome', column_type='decimal(19,4)', nullable=False, chn_name='汇兑收益')
    """汇兑收益:"""

    AssetDealIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='AssetDealIncome', column_type='decimal(19,4)', nullable=False, chn_name='资产处置收益')
    """资产处置收益:"""

    OtherRevenue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OtherRevenue', column_type='decimal(19,4)', nullable=False, chn_name='其他收益')
    """其他收益:"""

    OtherItemsEffectingOP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OtherItemsEffectingOP', column_type='decimal(19,4)', nullable=False, chn_name='##非经营性净收益特殊项目')
    """##非经营性净收益特殊项目:"""

    AdjustedItemsEffectingOP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='AdjustedItemsEffectingOP', column_type='decimal(19,4)', nullable=False, chn_name='##非经营性净收益调整项目')
    """##非经营性净收益调整项目:"""

    OperatingProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OperatingProfit', column_type='decimal(19,4)', nullable=False, chn_name='四、营业利润')
    """四、营业利润:"""

    NonoperatingIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='NonoperatingIncome', column_type='decimal(19,4)', nullable=False, chn_name='加:营业外收入')
    """加:营业外收入:"""

    NonoperatingExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='NonoperatingExpense', column_type='decimal(19,4)', nullable=False, chn_name='减:营业外支出')
    """减:营业外支出:"""

    NonCurrentAssetssDealLoss: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='NonCurrentAssetssDealLoss', column_type='decimal(19,4)', nullable=False, chn_name='其中:非流动资产处置净损失')
    """其中:非流动资产处置净损失:"""

    IfAdjusted: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='IfAdjusted', column_type='int', nullable=True, chn_name='是否调整')
    """是否调整:是否调整（IfAdjusted），该字段固定以下常量：1-调整；2-未调整；4-季度未调整；5-季度调整 注：季度数据是第三季度财务数据"""

    OtherItemsEffectingTP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OtherItemsEffectingTP', column_type='decimal(19,4)', nullable=False, chn_name='加:##影响利润总额的其他科目')
    """加:##影响利润总额的其他科目:"""

    AdjustedItemsEffectingTP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='AdjustedItemsEffectingTP', column_type='decimal(19,4)', nullable=False, chn_name='加:##影响利润总额的调整项目')
    """加:##影响利润总额的调整项目:"""

    TotalProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='TotalProfit', column_type='decimal(19,4)', nullable=False, chn_name='五、利润总额')
    """五、利润总额:"""

    IncomeTaxCost: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='IncomeTaxCost', column_type='decimal(19,4)', nullable=False, chn_name='减:所得税费用')
    """减:所得税费用:"""

    UncertainedInvestmentLosses: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='UncertainedInvestmentLosses', column_type='decimal(19,4)', nullable=False, chn_name='加:未确认的投资损失')
    """加:未确认的投资损失:"""

    OtherItemsEffectingNP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OtherItemsEffectingNP', column_type='decimal(19,4)', nullable=False, chn_name='加:##影响净利润的其他科目')
    """加:##影响净利润的其他科目:"""

    AdjustedItemsEffectingNP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='AdjustedItemsEffectingNP', column_type='decimal(19,4)', nullable=False, chn_name='加:##影响净利润的调整项目')
    """加:##影响净利润的调整项目:"""

    NetProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='NetProfit', column_type='decimal(19,4)', nullable=False, chn_name='六、净利润')
    """六、净利润:"""

    OperSustCateg: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OperSustCateg', column_type='decimal(19,4)', nullable=False, chn_name='(一)按经营持续性分类')
    """(一)按经营持续性分类:"""

    OperSustNetP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OperSustNetP', column_type='decimal(19,4)', nullable=False, chn_name='持续经营净利润')
    """持续经营净利润:"""

    IfMerged: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='IfMerged', column_type='int', nullable=True, chn_name='是否合并')
    """是否合并:是否合并（IfMerged），该字段固定以下常量：1-合并报表；2-母公司报表"""

    DisconOperNetP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='DisconOperNetP', column_type='decimal(19,4)', nullable=False, chn_name='终止经营净利润')
    """终止经营净利润:"""

    OwnershipCateg: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OwnershipCateg', column_type='decimal(19,4)', nullable=False, chn_name='(二)按所有权归属分类')
    """(二)按所有权归属分类:"""

    NPParentCompanyOwners: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='NPParentCompanyOwners', column_type='decimal(19,4)', nullable=False, chn_name='归属于母公司所有者的净利润')
    """归属于母公司所有者的净利润:"""

    MinorityProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='MinorityProfit', column_type='decimal(19,4)', nullable=False, chn_name='少数股东损益')
    """少数股东损益:"""

    OtherItemsEffectingNPP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OtherItemsEffectingNPP', column_type='decimal(19,4)', nullable=False, chn_name='##加:影响母公司净利润的特殊项目')
    """##加:影响母公司净利润的特殊项目:"""

    AdjustedItemsEffectingNPP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='AdjustedItemsEffectingNPP', column_type='decimal(19,4)', nullable=False, chn_name='##加:影响母公司净利润的调整项目')
    """##加:影响母公司净利润的调整项目:"""

    OtherCompositeIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OtherCompositeIncome', column_type='decimal(19,4)', nullable=False, chn_name='七、其他综合收益')
    """七、其他综合收益:"""

    OCIParentCompanyOwners: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OCIParentCompanyOwners', column_type='decimal(19,4)', nullable=False, chn_name='归属于母公司所有者的其他综合收益总额')
    """归属于母公司所有者的其他综合收益总额:"""

    OCINotInIncomeStatement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OCINotInIncomeStatement', column_type='decimal(19,4)', nullable=False, chn_name='(一)以后不能重分类进损益表的其他综合收益')
    """(一)以后不能重分类进损益表的其他综合收益:"""

    OCIReMearsure: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OCIReMearsure', column_type='decimal(19,4)', nullable=False, chn_name='1.1重新计量设定收益计划净负债或净资产的变动')
    """1.1重新计量设定收益计划净负债或净资产的变动:"""

    AccountingStandards: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='AccountingStandards', column_type='int', nullable=True, chn_name='会计准则')
    """会计准则:会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 1455，得到会计准则的具体描述：1-新会计准则(2007)，9-旧会计准则。"""

    OCIEquityNotInIS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OCIEquityNotInIS', column_type='decimal(19,4)', nullable=False, chn_name='1.2权益法下在被投资单位不能重分类进损益表的其他综合收益中享有的份额')
    """1.2权益法下在被投资单位不能重分类进损益表的其他综合收益中享有的份额:"""

    OthEquFVChange: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OthEquFVChange', column_type='decimal(19,4)', nullable=False, chn_name='1.3其他权益工具投资公允价值变动')
    """1.3其他权益工具投资公允价值变动:"""

    CorporateCRChange: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='CorporateCRChange', column_type='decimal(19,4)', nullable=False, chn_name='1.4企业自身信用风险公允价值变动')
    """1.4企业自身信用风险公允价值变动:"""

    OCIInIncomeStatement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OCIInIncomeStatement', column_type='decimal(19,4)', nullable=False, chn_name='(二)以后能重分类进损益表的其他综合收益')
    """(二)以后能重分类进损益表的其他综合收益:"""

    OCIEquityInIS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OCIEquityInIS', column_type='decimal(19,4)', nullable=False, chn_name='2.1权益法下在被投资单位能重分类进损益表的其他综合收益中享有的份额')
    """2.1权益法下在被投资单位能重分类进损益表的其他综合收益中享有的份额:"""

    OCIFairValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OCIFairValue', column_type='decimal(19,4)', nullable=False, chn_name='2.2可供出售金融资产公允价值变动损益')
    """2.2可供出售金融资产公允价值变动损益:"""

    OCIToMaturityFA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OCIToMaturityFA', column_type='decimal(19,4)', nullable=False, chn_name='2.3持有至到期投资重分类为可供出售金融资产损益')
    """2.3持有至到期投资重分类为可供出售金融资产损益:"""

    OCICFLoss: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OCICFLoss', column_type='decimal(19,4)', nullable=False, chn_name='2.4现金流量套期损益的有效部分')
    """2.4现金流量套期损益的有效部分:"""

    OCIForeignCurrencyFSA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OCIForeignCurrencyFSA', column_type='decimal(19,4)', nullable=False, chn_name='2.5外币财务报表分析折算差额')
    """2.5外币财务报表分析折算差额:"""

    OCIOthers: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IncomeStatementAll', column_name='OCIOthers', column_type='decimal(19,4)', nullable=False, chn_name='2.6其他')
    """2.6其他:"""

