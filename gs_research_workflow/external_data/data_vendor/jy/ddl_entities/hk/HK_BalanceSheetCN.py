# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_BalanceSheetCN(SQLTableEntity):
    name: str = 'HK_BalanceSheetCN'
    
    chn_name: str = '港股资产负债表(中国会计准则)'
    
    business_unique: str = 'CompanyCode,EndDate,PeriodMark,Mark,CurrencyUnit'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.介绍按中国会计准则披露的港股资产负债表中各项指标，该表为资产负债表的横表，标准会计科目与A股基本相同。
2.数据范围：2001年至今。
3.数据来源：港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    CashEquivalents: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='CashEquivalents', column_type='decimal(19,4)', nullable=False, chn_name='货币资金(元)')
    """货币资金(元):"""

    SpecAccPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='SpecAccPayable', column_type='decimal(19,4)', nullable=False, chn_name='专项应付款')
    """专项应付款:"""

    EstimateLia: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='EstimateLia', column_type='decimal(19,4)', nullable=False, chn_name='预计负债')
    """预计负债:"""

    DefTaxLia: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='DefTaxLia', column_type='decimal(19,4)', nullable=False, chn_name='递延所得税负债')
    """递延所得税负债:"""

    DefIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='DefIncome', column_type='decimal(19,4)', nullable=False, chn_name='递延收益')
    """递延收益:"""

    OtherNonCurLia: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='OtherNonCurLia', column_type='decimal(19,4)', nullable=False, chn_name='其他非流动负债')
    """其他非流动负债:"""

    NCLExcepItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='NCLExcepItems', column_type='decimal(19,4)', nullable=False, chn_name='非流动负债特殊项目')
    """非流动负债特殊项目:"""

    NCLAdjItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='NCLAdjItems', column_type='decimal(19,4)', nullable=False, chn_name='非流动负债调整项目')
    """非流动负债调整项目:"""

    TotalNonCurLia: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='TotalNonCurLia', column_type='decimal(19,4)', nullable=False, chn_name='非流动负债合计')
    """非流动负债合计:若非流动负债合计为空，则以长期借款+应付债券+长期应付款+长期应付职工薪酬+专项应付款+预计负债+递延所得税负债+递延收益+其他非流动负债+非流动负债特殊项目+非流动负债调整项目填充。"""

    BorFromCB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='BorFromCB', column_type='decimal(19,4)', nullable=False, chn_name='向中央银行借款')
    """向中央银行借款:"""

    DepOfInterbank: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='DepOfInterbank', column_type='decimal(19,4)', nullable=False, chn_name='同业及其他金融机构存放款项')
    """同业及其他金融机构存放款项:"""

    ClientDeposit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='ClientDeposit', column_type='decimal(19,4)', nullable=False, chn_name='其中:客户资金存款')
    """其中:客户资金存款:"""

    BorCapital: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='BorCapital', column_type='decimal(19,4)', nullable=False, chn_name='拆入资金')
    """拆入资金:"""

    DeriLia: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='DeriLia', column_type='decimal(19,4)', nullable=False, chn_name='衍生金融负债')
    """衍生金融负债:"""

    SBbackSecuPros: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='SBbackSecuPros', column_type='decimal(19,4)', nullable=False, chn_name='卖出回购金融资产款')
    """卖出回购金融资产款:"""

    Deposit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='Deposit', column_type='decimal(19,4)', nullable=False, chn_name='吸收存款')
    """吸收存款:"""

    ProSecuPros: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='ProSecuPros', column_type='decimal(19,4)', nullable=False, chn_name='代理买卖证券款')
    """代理买卖证券款:"""

    SubIssSecuPros: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='SubIssSecuPros', column_type='decimal(19,4)', nullable=False, chn_name='代理承销证券款')
    """代理承销证券款:"""

    DepReceived: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='DepReceived', column_type='decimal(19,4)', nullable=False, chn_name='存入保证金')
    """存入保证金:"""

    AdvInsurance: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='AdvInsurance', column_type='decimal(19,4)', nullable=False, chn_name='预收保费')
    """预收保费:"""

    CommiPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='CommiPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付手续费及佣金')
    """应付手续费及佣金:"""

    ReinPayables: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='ReinPayables', column_type='decimal(19,4)', nullable=False, chn_name='应付分保账款')
    """应付分保账款:"""

    TradingAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='TradingAssets', column_type='decimal(19,4)', nullable=False, chn_name='交易性金融资产')
    """交易性金融资产:"""

    CompPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='CompPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付赔付款')
    """应付赔付款:"""

    PolDivPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='PolDivPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付保单红利')
    """应付保单红利:"""

    InsDepInvest: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='InsDepInvest', column_type='decimal(19,4)', nullable=False, chn_name='保户储金及投资款')
    """保户储金及投资款:"""

    UnePreReserve: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='UnePreReserve', column_type='decimal(19,4)', nullable=False, chn_name='未到期责任准备金')
    """未到期责任准备金:"""

    OutingClaRes: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='OutingClaRes', column_type='decimal(19,4)', nullable=False, chn_name='未决赔款准备金')
    """未决赔款准备金:"""

    LifeInsReserve: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='LifeInsReserve', column_type='decimal(19,4)', nullable=False, chn_name='寿险责任准备金')
    """寿险责任准备金:"""

    LTHealInsLR: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='LTHealInsLR', column_type='decimal(19,4)', nullable=False, chn_name='长期健康险责任准备金')
    """长期健康险责任准备金:"""

    IndLiab: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='IndLiab', column_type='decimal(19,4)', nullable=False, chn_name='独立账户负债')
    """独立账户负债:"""

    OtherLiab: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='OtherLiab', column_type='decimal(19,4)', nullable=False, chn_name='其他负债')
    """其他负债:"""

    LExcepItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='LExcepItems', column_type='decimal(19,4)', nullable=False, chn_name='负债特殊项目')
    """负债特殊项目:"""

    BillReceivable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='BillReceivable', column_type='decimal(19,4)', nullable=False, chn_name='应收票据')
    """应收票据:"""

    LAdjuItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='LAdjuItems', column_type='decimal(19,4)', nullable=False, chn_name='负债调整项目')
    """负债调整项目:"""

    TotalLiab: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='TotalLiab', column_type='decimal(19,4)', nullable=False, chn_name='负债合计')
    """负债合计:若负债合计为空，则以流动负债合计+非流动负债合计+向中央银行借款+同业及其他金融机构存放款项+拆入资金+衍生金融负债+卖出回购金融资产款+吸收存款+代理买卖证券款+代理承销证券款+存入保证金+预收保费+应付手续费及佣金+应付分保账款+应付赔付款+应付保单红利+保户储金及投资款+未到期责任准备金+未决赔款准备金+寿险责任准备金+长期健康险责任准备金+独立账户负..."""

    PaidInCapital: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='PaidInCapital', column_type='decimal(19,4)', nullable=False, chn_name='实收资本(或股本)')
    """实收资本(或股本):"""

    OtherEqu: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='OtherEqu', column_type='decimal(19,4)', nullable=False, chn_name='其他权益工具')
    """其他权益工具:"""

    EPreferStock: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='EPreferStock', column_type='decimal(19,4)', nullable=False, chn_name='其中:优先股(其他权益工具)')
    """其中:优先股(其他权益工具):"""

    EPerpDebt: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='EPerpDebt', column_type='decimal(19,4)', nullable=False, chn_name='其中:永续债(其他权益工具)')
    """其中:永续债(其他权益工具):"""

    CapResFund: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='CapResFund', column_type='decimal(19,4)', nullable=False, chn_name='资本公积')
    """资本公积:"""

    TreaStock: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='TreaStock', column_type='decimal(19,4)', nullable=False, chn_name='减:库存股')
    """减:库存股:"""

    SplusResFund: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='SplusResFund', column_type='decimal(19,4)', nullable=False, chn_name='盈余公积')
    """盈余公积:"""

    RetaProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='RetaProfit', column_type='decimal(19,4)', nullable=False, chn_name='未分配利润')
    """未分配利润:"""

    DivReceivable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='DivReceivable', column_type='decimal(19,4)', nullable=False, chn_name='应收股利')
    """应收股利:"""

    OtherCompIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='OtherCompIncome', column_type='decimal(19,4)', nullable=False, chn_name='其他综合收益')
    """其他综合收益:"""

    OrdRiskResFund: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='OrdRiskResFund', column_type='decimal(19,4)', nullable=False, chn_name='一般风险准备')
    """一般风险准备:"""

    ForCurRepCDiff: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='ForCurRepCDiff', column_type='decimal(19,4)', nullable=False, chn_name='外币报表折算差额')
    """外币报表折算差额:"""

    UncInvLoss: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='UncInvLoss', column_type='decimal(19,4)', nullable=False, chn_name='未确认投资损失')
    """未确认投资损失:"""

    OtherRes: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='OtherRes', column_type='decimal(19,4)', nullable=False, chn_name='其他储备(公允价值变动储备)')
    """其他储备(公允价值变动储备):"""

    SpecReserves: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='SpecReserves', column_type='decimal(19,4)', nullable=False, chn_name='专项储备')
    """专项储备:"""

    SEExcepItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='SEExcepItems', column_type='decimal(19,4)', nullable=False, chn_name='归属母公司所有者权益特殊项目')
    """归属母公司所有者权益特殊项目:"""

    SEAdjItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='SEAdjItems', column_type='decimal(19,4)', nullable=False, chn_name='归属母公司所有者权益调整项目')
    """归属母公司所有者权益调整项目:"""

    SEWithoutMI: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='SEWithoutMI', column_type='decimal(19,4)', nullable=False, chn_name='归属母公司所有者权益合计')
    """归属母公司所有者权益合计:若归属母公司所有者权益合计为空，则以实收资本（或股本）+其他权益工具+资本公积+盈余公积+未分配利润+其他综合收益+一般风险准备+外币报表折算差额+未确认投资损失+其他储备（公允价值变动储备）+专项储备+归属母公司所有者权益特殊项目+归属母公司所有者权益调整项目填充。"""

    MinInterests: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='MinInterests', column_type='decimal(19,4)', nullable=False, chn_name='少数股东权益')
    """少数股东权益:"""

    IntReceivable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='IntReceivable', column_type='decimal(19,4)', nullable=False, chn_name='应收利息')
    """应收利息:"""

    OtherItemsEffSE: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='OtherItemsEffSE', column_type='decimal(19,4)', nullable=False, chn_name='所有者权益调整项目')
    """所有者权益调整项目:"""

    TotalShEquity: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='TotalShEquity', column_type='decimal(19,4)', nullable=False, chn_name='所有者权益(或股东权益)合计')
    """所有者权益(或股东权益)合计:若所有者权益（或股东权益）合计为空，则以归属母公司所有者权益合计+少数股东权益+所有者权益调整项目填充。"""

    LEExcepItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='LEExcepItems', column_type='decimal(19,4)', nullable=False, chn_name='负债和权益特殊项目')
    """负债和权益特殊项目:"""

    LEAdjItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='LEAdjItems', column_type='decimal(19,4)', nullable=False, chn_name='负债和权益调整项目')
    """负债和权益调整项目:"""

    TotalLiaAndEqu: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='TotalLiaAndEqu', column_type='decimal(19,4)', nullable=False, chn_name='负债和所有者(或股东权益)总计')
    """负债和所有者(或股东权益)总计:若负债和所有者（或股东权益）总计为空，则以负债合计+所有者权益（或股东权益）合计+负债和权益特殊项目+负债和权益调整项目填充。"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    FiscalYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='FiscalYear', column_type='datetime', nullable=False, chn_name='财政年度')
    """财政年度:"""

    InsertTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='InsertTime', column_type='datetime', nullable=False, chn_name='发布时间')
    """发布时间:"""

    AccReceivable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='AccReceivable', column_type='decimal(19,4)', nullable=False, chn_name='应收账款')
    """应收账款:"""

    OtherReceivable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='OtherReceivable', column_type='decimal(19,4)', nullable=False, chn_name='其他应收款')
    """其他应收款:"""

    AdvancePayment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='AdvancePayment', column_type='decimal(19,4)', nullable=False, chn_name='预付账款')
    """预付账款:"""

    Inventories: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='Inventories', column_type='decimal(19,4)', nullable=False, chn_name='存货')
    """存货:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到所属公司股票的交易代码、简称等。"""

    BearerBiolAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='BearerBiolAssets', column_type='decimal(19,4)', nullable=False, chn_name='其中:消耗性生物资产')
    """其中:消耗性生物资产:"""

    DefExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='DefExpense', column_type='decimal(19,4)', nullable=False, chn_name='待摊费用')
    """待摊费用:"""

    HoldAndFSAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='HoldAndFSAssets', column_type='decimal(19,4)', nullable=False, chn_name='划分为持有待售的资产')
    """划分为持有待售的资产:"""

    NonCurAssetIn1Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='NonCurAssetIn1Y', column_type='decimal(19,4)', nullable=False, chn_name='一年内到期的非流动资产')
    """一年内到期的非流动资产:"""

    OtherCurAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='OtherCurAssets', column_type='decimal(19,4)', nullable=False, chn_name='其他流动资产')
    """其他流动资产:"""

    CAExcepItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='CAExcepItems', column_type='decimal(19,4)', nullable=False, chn_name='流动资产特殊项目')
    """流动资产特殊项目:"""

    CAAdjItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='CAAdjItems', column_type='decimal(19,4)', nullable=False, chn_name='流动资产调整项目')
    """流动资产调整项目:"""

    TotalCurAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='TotalCurAssets', column_type='decimal(19,4)', nullable=False, chn_name='流动资产合计')
    """流动资产合计:若流动资产合计为空，则以货币资金+交易性金融资产+应收票据+应收股利+应收利息+应收账款+其他应收款+预付账款+存货+待摊费用+划分为持有待售的资产+一年内到期的非流动资产+其他流动资产+流动资产特殊项目+流动资产调整项目填充。"""

    HForSaleAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='HForSaleAssets', column_type='decimal(19,4)', nullable=False, chn_name='可供出售金融资产')
    """可供出售金融资产:"""

    HoldToMatInv: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='HoldToMatInv', column_type='decimal(19,4)', nullable=False, chn_name='持有至到期投资')
    """持有至到期投资:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    InvProperty: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='InvProperty', column_type='decimal(19,4)', nullable=False, chn_name='投资性房地产')
    """投资性房地产:"""

    LtermEquInvest: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='LtermEquInvest', column_type='decimal(19,4)', nullable=False, chn_name='长期股权投资')
    """长期股权投资:"""

    LtermReceAcc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='LtermReceAcc', column_type='decimal(19,4)', nullable=False, chn_name='长期应收款')
    """长期应收款:"""

    FixedAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='FixedAssets', column_type='decimal(19,4)', nullable=False, chn_name='固定资产')
    """固定资产:"""

    ConsMaterials: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='ConsMaterials', column_type='decimal(19,4)', nullable=False, chn_name='工程物资')
    """工程物资:"""

    ConsInProcess: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='ConsInProcess', column_type='decimal(19,4)', nullable=False, chn_name='在建工程')
    """在建工程:"""

    FixedAssetsLiq: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='FixedAssetsLiq', column_type='decimal(19,4)', nullable=False, chn_name='固定资产清理')
    """固定资产清理:"""

    BiolAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='BiolAssets', column_type='decimal(19,4)', nullable=False, chn_name='生产性生物资产')
    """生产性生物资产:"""

    OilGasAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='OilGasAssets', column_type='decimal(19,4)', nullable=False, chn_name='油气资产')
    """油气资产:"""

    IntAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='IntAssets', column_type='decimal(19,4)', nullable=False, chn_name='无形资产')
    """无形资产:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='InfoSource', column_type='varchar(100)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    SeatCosts: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='SeatCosts', column_type='decimal(19,4)', nullable=False, chn_name='其中:交易席位费')
    """其中:交易席位费:"""

    DeveExpenditure: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='DeveExpenditure', column_type='decimal(19,4)', nullable=False, chn_name='开发支出')
    """开发支出:"""

    GoodWill: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='GoodWill', column_type='decimal(19,4)', nullable=False, chn_name='商誉')
    """商誉:"""

    LongDefExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='LongDefExpense', column_type='decimal(19,4)', nullable=False, chn_name='长期待摊费用')
    """长期待摊费用:"""

    DefTaxAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='DefTaxAssets', column_type='decimal(19,4)', nullable=False, chn_name='递延所得税资产')
    """递延所得税资产:"""

    OtherNonCurAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='OtherNonCurAssets', column_type='decimal(19,4)', nullable=False, chn_name='其他非流动资产')
    """其他非流动资产:"""

    NCAExcepItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='NCAExcepItems', column_type='decimal(19,4)', nullable=False, chn_name='非流动资产特殊项目')
    """非流动资产特殊项目:"""

    NCAAdjItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='NCAAdjItems', column_type='decimal(19,4)', nullable=False, chn_name='非流动资产调整项目')
    """非流动资产调整项目:"""

    TotNonCurAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='TotNonCurAssets', column_type='decimal(19,4)', nullable=False, chn_name='非流动资产合计')
    """非流动资产合计:若非流动资产合计为空，则以可供出售金融资产+持有至到期投资+投资性房地产+长期股权投资+长期应收款+固定资产+工程物资+在建工程+固定资产清理+生产性生物资产+油气资产+无形资产+开发支出+商誉+长期待摊费用+递延所得税资产+其他非流动资产+非流动资产特殊项目+非流动资产调整项目填充。"""

    LoanAndAccRece: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='LoanAndAccRece', column_type='decimal(19,4)', nullable=False, chn_name='投资-贷款及应收账款(应收账款类投资)')
    """投资-贷款及应收账款(应收账款类投资):"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    SettlProvi: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='SettlProvi', column_type='decimal(19,4)', nullable=False, chn_name='结算备付金')
    """结算备付金:"""

    ClientProvi: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='ClientProvi', column_type='decimal(19,4)', nullable=False, chn_name='其中:客户备付金')
    """其中:客户备付金:"""

    DepInInterbank: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='DepInInterbank', column_type='decimal(19,4)', nullable=False, chn_name='存放同业款项')
    """存放同业款项:"""

    Rmetal: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='Rmetal', column_type='decimal(19,4)', nullable=False, chn_name='贵金属')
    """贵金属:"""

    LendCapital: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='LendCapital', column_type='decimal(19,4)', nullable=False, chn_name='拆出资金')
    """拆出资金:"""

    DerAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='DerAssets', column_type='decimal(19,4)', nullable=False, chn_name='衍生金融资产')
    """衍生金融资产:"""

    BSbackAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='BSbackAssets', column_type='decimal(19,4)', nullable=False, chn_name='买入返售金融资产')
    """买入返售金融资产:"""

    LoanAndAdvance: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='LoanAndAdvance', column_type='decimal(19,4)', nullable=False, chn_name='发放贷款和垫款')
    """发放贷款和垫款:"""

    InsReceivables: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='InsReceivables', column_type='decimal(19,4)', nullable=False, chn_name='应收保费')
    """应收保费:"""

    ReceSubFee: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='ReceSubFee', column_type='decimal(19,4)', nullable=False, chn_name='应收代位追偿款')
    """应收代位追偿款:"""

    PeriodMark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='PeriodMark', column_type='int', nullable=True, chn_name='日期标志')
    """日期标志:日期标志(PeriodMark)与(CT_SystemConst)表中的DM字段关联，令LB=1314，得到日期标志的具体描述：1-1个月，2-2个月，3-3个月，4-4个月，5-5个月，6-半年度，7-7个月，8-8个月，9-9个月，10-10个月，11-11个月，12-年度，13-13个月，14-14个月，15-15个月，16-16个月，17-17个月，..."""

    ReinRece: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='ReinRece', column_type='decimal(19,4)', nullable=False, chn_name='应收分保账款')
    """应收分保账款:"""

    ReceUnearnedR: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='ReceUnearnedR', column_type='decimal(19,4)', nullable=False, chn_name='应收分保未到期责任准备金')
    """应收分保未到期责任准备金:"""

    ReceClaimsR: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='ReceClaimsR', column_type='decimal(19,4)', nullable=False, chn_name='应收分保未决赔款准备金')
    """应收分保未决赔款准备金:"""

    ReceLifeR: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='ReceLifeR', column_type='decimal(19,4)', nullable=False, chn_name='应收分保寿险责任准备金')
    """应收分保寿险责任准备金:"""

    ReceLTHealthR: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='ReceLTHealthR', column_type='decimal(19,4)', nullable=False, chn_name='应收分保长期健康险责任准备金')
    """应收分保长期健康险责任准备金:"""

    InsImpawnLoan: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='InsImpawnLoan', column_type='decimal(19,4)', nullable=False, chn_name='保户质押贷款')
    """保户质押贷款:"""

    FixedDeposit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='FixedDeposit', column_type='decimal(19,4)', nullable=False, chn_name='定期存款')
    """定期存款:"""

    RefDeposit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='RefDeposit', column_type='decimal(19,4)', nullable=False, chn_name='存出保证金')
    """存出保证金:"""

    RefCapDeposit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='RefCapDeposit', column_type='decimal(19,4)', nullable=False, chn_name='存出资本保证金')
    """存出资本保证金:"""

    IndepAccAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='IndepAccAssets', column_type='decimal(19,4)', nullable=False, chn_name='独立账户资产')
    """独立账户资产:"""

    CompanyNature: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='CompanyNature', column_type='int', nullable=False, chn_name='公司性质')
    """公司性质:公司性质(CompanyNature)与(CT_SystemConst)表中的DM字段关联，令LB=1356，得到公司性质的具体描述：1-普通，2-金融，3-保险，4-房地产，5-银行。"""

    OtherAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='OtherAssets', column_type='decimal(19,4)', nullable=False, chn_name='其他资产')
    """其他资产:"""

    AExcepItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='AExcepItems', column_type='decimal(19,4)', nullable=False, chn_name='资产特殊项目')
    """资产特殊项目:"""

    AAdjItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='AAdjItems', column_type='decimal(19,4)', nullable=False, chn_name='资产调整项目')
    """资产调整项目:"""

    TotalAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='TotalAssets', column_type='decimal(19,4)', nullable=False, chn_name='资产总计')
    """资产总计:若资产总计为空，则以流动资产合计+非流动资产合计+应收账款类投资+结算备付金+存放同业款项+贵金属+拆出资金+衍生金融资产+买入返售金融资产+发放贷款和垫款+应收保费+应收代位追偿款+应收分保账款+应收分保未到期责任准备金+应收分保未决赔款准备金+应收分保寿险责任准备金+应收分保长期健康险责任准备金+保户质押贷款+定期存款+存出保证金+存出资本保证金+独立账..."""

    ShortTermLoan: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='ShortTermLoan', column_type='decimal(19,4)', nullable=False, chn_name='短期借款')
    """短期借款:"""

    ImpawnedLoan: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='ImpawnedLoan', column_type='decimal(19,4)', nullable=False, chn_name='其中:质押借款')
    """其中:质押借款:"""

    STBPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='STBPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付短期债券')
    """应付短期债券:"""

    TradingLia: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='TradingLia', column_type='decimal(19,4)', nullable=False, chn_name='交易性金融负债')
    """交易性金融负债:"""

    NotesPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='NotesPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付票据')
    """应付票据:"""

    AccPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='AccPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付账款')
    """应付账款:"""

    Mark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='Mark', column_type='int', nullable=True, chn_name='合并调整标志')
    """合并调整标志:合并调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB=1511，得到合并调整标志的具体描述：1-合并调整，2-合并未调整，3-母公司调整，4-母公司未调整，5-专项合并调整，6-专项合并未调整。"""

    AdvanceRece: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='AdvanceRece', column_type='decimal(19,4)', nullable=False, chn_name='预收账款')
    """预收账款:"""

    SalaPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='SalaPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付职工薪酬')
    """应付职工薪酬:"""

    DiviPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='DiviPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付股利')
    """应付股利:"""

    TaxsPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='TaxsPayable', column_type='decimal(19,4)', nullable=False, chn_name='应交税费')
    """应交税费:"""

    IntePayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='IntePayable', column_type='decimal(19,4)', nullable=False, chn_name='应付利息')
    """应付利息:"""

    OtherPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='OtherPayable', column_type='decimal(19,4)', nullable=False, chn_name='其他应付款')
    """其他应付款:"""

    AccrExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='AccrExpense', column_type='decimal(19,4)', nullable=False, chn_name='预提费用')
    """预提费用:"""

    DefProceeds: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='DefProceeds', column_type='decimal(19,4)', nullable=False, chn_name='递延收益')
    """递延收益:"""

    HoldAndFSLi: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='HoldAndFSLi', column_type='decimal(19,4)', nullable=False, chn_name='划分为持有待售的负债')
    """划分为持有待售的负债:"""

    NonCurLiaIn1Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='NonCurLiaIn1Y', column_type='decimal(19,4)', nullable=False, chn_name='一年内到期的非流动负债')
    """一年内到期的非流动负债:"""

    CurrencyUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='CurrencyUnit', column_type='int', nullable=True, chn_name='货币单位')
    """货币单位:货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB=1068，得到货币单位的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，1170-约旦第纳尔，1180-科威特..."""

    OtherCurLia: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='OtherCurLia', column_type='decimal(19,4)', nullable=False, chn_name='其他流动负债')
    """其他流动负债:"""

    CLExcepItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='CLExcepItems', column_type='decimal(19,4)', nullable=False, chn_name='流动负债特殊项目')
    """流动负债特殊项目:"""

    CLAdjItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='CLAdjItems', column_type='decimal(19,4)', nullable=False, chn_name='流动负债调整项目')
    """流动负债调整项目:"""

    TotalCurLia: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='TotalCurLia', column_type='decimal(19,4)', nullable=False, chn_name='流动负债合计')
    """流动负债合计:若流动负债合计为空，则以短期借款+应付短期债券+交易性金融负债+应付票据+应付账款+预收账款+应付职工薪酬+应付股利+应交税费+应付利息+其他应付款+预提费用+递延收益+划分为持有待售的负债+一年内到期的非流动负债+其他流动负债+流动负债特殊项目+流动负债调整项目填充。"""

    LongtermLoan: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='LongtermLoan', column_type='decimal(19,4)', nullable=False, chn_name='长期借款')
    """长期借款:"""

    BondsPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='BondsPayable', column_type='decimal(19,4)', nullable=False, chn_name='应付债券')
    """应付债券:"""

    LPreferStock: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='LPreferStock', column_type='decimal(19,4)', nullable=False, chn_name='其中:优先股(应付债券)')
    """其中:优先股(应付债券):"""

    LPerpDebt: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='LPerpDebt', column_type='decimal(19,4)', nullable=False, chn_name='其中:永续债(应付债券)')
    """其中:永续债(应付债券):"""

    LTAccPayable: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='LTAccPayable', column_type='decimal(19,4)', nullable=False, chn_name='长期应付款')
    """长期应付款:"""

    LongSalaPay: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_BalanceSheetCN', column_name='LongSalaPay', column_type='decimal(19,4)', nullable=False, chn_name='长期应付职工薪酬')
    """长期应付职工薪酬:"""

