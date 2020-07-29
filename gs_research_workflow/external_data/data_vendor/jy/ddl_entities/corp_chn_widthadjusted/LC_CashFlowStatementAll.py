# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_CashFlowStatementAll(SQLTableEntity):
    name: str = 'LC_CashFlowStatementAll'
    
    chn_name: str = '现金流量表_新会计准则'
    
    business_unique: str = 'InfoPublDate,CompanyCode,EndDate,IfAdjusted,IfMerged'
    
    refresh_freq: str = """季更新"""
    
    comment: str = """1.反映上市公司依据2007年新会计准则在年报、中报、季报中披露的现金流量表数据；并依据新旧会计准则的科目对应关系，收录了主要科目的历史对应数据。
2.收录同一公司在报告期末的四种财务报告，即未调整的合并报表、未调整的母公司报表、调整后的合并报表以及调整后的母公司报表。
3.若某个报告期的数据有多次调整，则该表展示历次调整数据。
4.该表中各财务科目的单位均为人民币元。
5.带“##”的特殊项目为单个公司披露的非标准化的科目，对应的“特殊字段说明”字段将对其作出说明；带“##”的调整项目是为了让报表的各个小项借贷平衡而设置的，便于客户对报表的遗漏和差错进行判断。
6.数据范围：1998-06-30至今
7.信息来源：招股说明书、定报、审计报告等"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    EnterpriseType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='EnterpriseType', column_type='int', nullable=True, chn_name='企业性质')
    """企业性质:企业性质(EnterpriseType)与(CT_SystemConst)表中的DM字段关联，令LB = 1414 AND DM IN (13,31,33,35,39,99)，得到企业性质的具体描述：13-商业银行，31-证券公司，33-信托公司，35-保险公司，39-其他非银行金融机构，99-一般企业。"""

    InvestLoss: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='InvestLoss', column_type='decimal(19,4)', nullable=False, chn_name='投资损失')
    """投资损失:"""

    DeferedTaxAssetDecrease: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='DeferedTaxAssetDecrease', column_type='decimal(19,4)', nullable=False, chn_name='递延所得税资产减少')
    """递延所得税资产减少:"""

    DeferedTaxLiabilityIncrease: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='DeferedTaxLiabilityIncrease', column_type='decimal(19,4)', nullable=False, chn_name='递延所得税负债增加')
    """递延所得税负债增加:"""

    InventoryDecrease: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='InventoryDecrease', column_type='decimal(19,4)', nullable=False, chn_name='存货的减少')
    """存货的减少:"""

    OperateReceivableDecrease: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='OperateReceivableDecrease', column_type='decimal(19,4)', nullable=False, chn_name='经营性应收项目的减少')
    """经营性应收项目的减少:"""

    OperatePayableIncrease: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='OperatePayableIncrease', column_type='decimal(19,4)', nullable=False, chn_name='经营性应付项目的增加')
    """经营性应付项目的增加:"""

    Others: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='Others', column_type='decimal(19,4)', nullable=False, chn_name='其他')
    """其他:"""

    SpecialItemsNOCF1: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='SpecialItemsNOCF1', column_type='decimal(19,4)', nullable=False, chn_name='##(附注)经营活动现金流量净额特殊项目')
    """##(附注)经营活动现金流量净额特殊项目:"""

    AdjustmentItemsNOCF1: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='AdjustmentItemsNOCF1', column_type='decimal(19,4)', nullable=False, chn_name='##(附注)经营活动现金流量净额调整项目')
    """##(附注)经营活动现金流量净额调整项目:"""

    NetOperateCashFlowNotes: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='NetOperateCashFlowNotes', column_type='decimal(19,4)', nullable=False, chn_name='(附注)经营活动产生的现金流量净额')
    """(附注)经营活动产生的现金流量净额:"""

    IfComplete: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='IfComplete', column_type='int', nullable=False, chn_name='完整标志')
    """完整标志:完整标志(IfComplete)与(CT_SystemConst)表中的DM字段关联，令LB = 1444，得到完整标志的具体描述：1-完整报表，2-简表，3-个别字段修正报表。"""

    ContrastAdjutmentNOCF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='ContrastAdjutmentNOCF', column_type='decimal(19,4)', nullable=False, chn_name='##加:经营流量净额前后对比调整项目')
    """##加:经营流量净额前后对比调整项目:"""

    DebtToCaptical: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='DebtToCaptical', column_type='decimal(19,4)', nullable=False, chn_name='债务转为资本')
    """债务转为资本:"""

    CBsExpiringWithin1Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='CBsExpiringWithin1Y', column_type='decimal(19,4)', nullable=False, chn_name='一年内到期的可转换公司债券')
    """一年内到期的可转换公司债券:"""

    FixedAssetsFinanceLeases: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='FixedAssetsFinanceLeases', column_type='decimal(19,4)', nullable=False, chn_name='融资租入固定资产')
    """融资租入固定资产:"""

    CashAtEndOfYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='CashAtEndOfYear', column_type='decimal(19,4)', nullable=False, chn_name='现金的期末余额')
    """现金的期末余额:"""

    CashAtBeginningOfYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='CashAtBeginningOfYear', column_type='decimal(19,4)', nullable=False, chn_name='减:现金的期初余额')
    """减:现金的期初余额:"""

    CashEquivalentsAtEndOfYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='CashEquivalentsAtEndOfYear', column_type='decimal(19,4)', nullable=False, chn_name='加:现金等价物的期末余额')
    """加:现金等价物的期末余额:"""

    CashEquivalentsAtBeginning: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='CashEquivalentsAtBeginning', column_type='decimal(19,4)', nullable=False, chn_name='减:现金等价物的期初余额')
    """减:现金等价物的期初余额:"""

    SpecialItemsC: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='SpecialItemsC', column_type='decimal(19,4)', nullable=False, chn_name='##(附注)现金特殊项目')
    """##(附注)现金特殊项目:"""

    AdjustmentItemsC: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='AdjustmentItemsC', column_type='decimal(19,4)', nullable=False, chn_name='##(附注)现金调整项目')
    """##(附注)现金调整项目:"""

    GoodsSaleServiceRenderCash: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='GoodsSaleServiceRenderCash', column_type='decimal(19,4)', nullable=False, chn_name='销售商品、提供劳务收到的现金')
    """销售商品、提供劳务收到的现金:"""

    NetIncrInCashAndEquivalents: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='NetIncrInCashAndEquivalents', column_type='decimal(19,4)', nullable=False, chn_name='(附注)现金及现金等价物净增加额')
    """(附注)现金及现金等价物净增加额:"""

    ContrastAdjutmentNC: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='ContrastAdjutmentNC', column_type='decimal(19,4)', nullable=False, chn_name='##加:现金净额前后对比调整项目')
    """##加:现金净额前后对比调整项目:"""

    SpecialFieldRemark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='SpecialFieldRemark', column_type='varchar(1000)', nullable=False, chn_name='特殊字段说明')
    """特殊字段说明:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新日期')
    """更新日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    TaxLevyRefund: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='TaxLevyRefund', column_type='decimal(19,4)', nullable=False, chn_name='收到的税费返还')
    """收到的税费返还:"""

    NetDepositIncrease: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='NetDepositIncrease', column_type='decimal(19,4)', nullable=False, chn_name='客户存款和同业存放款项净增加额')
    """客户存款和同业存放款项净增加额:"""

    NetBorrowingFromCentralBank: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='NetBorrowingFromCentralBank', column_type='decimal(19,4)', nullable=False, chn_name='向中央银行借款净增加额')
    """向中央银行借款净增加额:"""

    NetBorrowingFromFinanceCo: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='NetBorrowingFromFinanceCo', column_type='decimal(19,4)', nullable=False, chn_name='向其他金融机构拆入资金净增加额')
    """向其他金融机构拆入资金净增加额:"""

    DrawBackLoansCanceled: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='DrawBackLoansCanceled', column_type='decimal(19,4)', nullable=False, chn_name='收回已核销贷款')
    """收回已核销贷款:"""

    InterestAndCommissionCashIn: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='InterestAndCommissionCashIn', column_type='decimal(19,4)', nullable=False, chn_name='收取利息、手续费及佣金的现金')
    """收取利息、手续费及佣金的现金:"""

    NetDealTradingAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='NetDealTradingAssets', column_type='decimal(19,4)', nullable=False, chn_name='处置交易性金融资产净增加额')
    """处置交易性金融资产净增加额:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='InfoPublDate', column_type='datetime', nullable=True, chn_name='信息发布日期')
    """信息发布日期:"""

    NetBuyBack: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='NetBuyBack', column_type='decimal(19,4)', nullable=False, chn_name='回购业务资金净增加额')
    """回购业务资金净增加额:"""

    NetOriginalInsuranceCash: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='NetOriginalInsuranceCash', column_type='decimal(19,4)', nullable=False, chn_name='收到原保险合同保费取得的现金')
    """收到原保险合同保费取得的现金:"""

    NetReinsuranceCash: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='NetReinsuranceCash', column_type='decimal(19,4)', nullable=False, chn_name='收到再保业务现金净额')
    """收到再保业务现金净额:"""

    NetInsurerDepositInvestment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='NetInsurerDepositInvestment', column_type='decimal(19,4)', nullable=False, chn_name='保户储金及投资款净增加额')
    """保户储金及投资款净增加额:"""

    OtherCashInRelatedOperate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='OtherCashInRelatedOperate', column_type='decimal(19,4)', nullable=False, chn_name='收到其他与经营活动有关的现金')
    """收到其他与经营活动有关的现金:"""

    SpecialItemsOCIF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='SpecialItemsOCIF', column_type='decimal(19,4)', nullable=False, chn_name='##经营活动现金流入特殊项目')
    """##经营活动现金流入特殊项目:"""

    AdjustmentItemsOCIF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='AdjustmentItemsOCIF', column_type='decimal(19,4)', nullable=False, chn_name='##经营活动现金流入调整项目')
    """##经营活动现金流入调整项目:"""

    SubtotalOperateCashInflow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='SubtotalOperateCashInflow', column_type='decimal(19,4)', nullable=False, chn_name='经营活动现金流入小计')
    """经营活动现金流入小计:"""

    GoodsServicesCashPaid: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='GoodsServicesCashPaid', column_type='decimal(19,4)', nullable=False, chn_name='购买商品、接受劳务支付的现金')
    """购买商品、接受劳务支付的现金:"""

    StaffBehalfPaid: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='StaffBehalfPaid', column_type='decimal(19,4)', nullable=False, chn_name='支付给职工以及为职工支付的现金')
    """支付给职工以及为职工支付的现金:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='InfoSource', column_type='varchar(100)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    AllTaxesPaid: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='AllTaxesPaid', column_type='decimal(19,4)', nullable=False, chn_name='支付的各项税费')
    """支付的各项税费:"""

    NetLoanAndAdvanceIncrease: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='NetLoanAndAdvanceIncrease', column_type='decimal(19,4)', nullable=False, chn_name='客户贷款及垫款净增加额')
    """客户贷款及垫款净增加额:"""

    NetDepositInCBAndIB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='NetDepositInCBAndIB', column_type='decimal(19,4)', nullable=False, chn_name='存放中央银行和同业款项净增加额')
    """存放中央银行和同业款项净增加额:"""

    NetLendCapital: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='NetLendCapital', column_type='decimal(19,4)', nullable=False, chn_name='拆出资金净增加额')
    """拆出资金净增加额:"""

    CommissionCashPaid: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='CommissionCashPaid', column_type='decimal(19,4)', nullable=False, chn_name='支付手续费及佣金的现金')
    """支付手续费及佣金的现金:"""

    OriginalCompensationPaid: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='OriginalCompensationPaid', column_type='decimal(19,4)', nullable=False, chn_name='支付原保险合同赔付款项的现金')
    """支付原保险合同赔付款项的现金:"""

    NetCashForReinsurance: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='NetCashForReinsurance', column_type='decimal(19,4)', nullable=False, chn_name='支付再保业务现金净额')
    """支付再保业务现金净额:"""

    PolicyDividendCashPaid: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='PolicyDividendCashPaid', column_type='decimal(19,4)', nullable=False, chn_name='支付保单红利的现金')
    """支付保单红利的现金:"""

    OtherOperateCashPaid: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='OtherOperateCashPaid', column_type='decimal(19,4)', nullable=False, chn_name='支付其他与经营活动有关的现金')
    """支付其他与经营活动有关的现金:"""

    SpecialItemsOCOF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='SpecialItemsOCOF', column_type='decimal(19,4)', nullable=False, chn_name='##经营活动现金流出特殊项目')
    """##经营活动现金流出特殊项目:"""

    BulletinType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='BulletinType', column_type='int', nullable=False, chn_name='公告类别')
    """公告类别:公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311，得到公告类别的具体描述：10-发行上市书，20-定期报告，30-业绩快报，50-章程制度，70-临时公告，90-交易所通报，91-交易所临时停(复)牌公告，99-其他。"""

    AdjustmentItemsOCOF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='AdjustmentItemsOCOF', column_type='decimal(19,4)', nullable=False, chn_name='##经营活动现金流出调整项目')
    """##经营活动现金流出调整项目:"""

    SubtotalOperateCashOutflow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='SubtotalOperateCashOutflow', column_type='decimal(19,4)', nullable=False, chn_name='经营活动现金流出小计')
    """经营活动现金流出小计:"""

    AdjustmentItemsNOCF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='AdjustmentItemsNOCF', column_type='decimal(19,4)', nullable=False, chn_name='##经营活动现金流量净额调整项目')
    """##经营活动现金流量净额调整项目:"""

    NetOperateCashFlow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='NetOperateCashFlow', column_type='decimal(19,4)', nullable=False, chn_name='经营活动产生的现金流量净额')
    """经营活动产生的现金流量净额:"""

    InvestWithdrawalCash: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='InvestWithdrawalCash', column_type='decimal(19,4)', nullable=False, chn_name='收回投资收到的现金')
    """收回投资收到的现金:"""

    Investproceeds: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='Investproceeds', column_type='decimal(19,4)', nullable=False, chn_name='取得投资收益收到的现金')
    """取得投资收益收到的现金:"""

    FixIntanOtherAssetDispoCash: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='FixIntanOtherAssetDispoCash', column_type='decimal(19,4)', nullable=False, chn_name='处置固定资产、无形资产和其他长期资产收回的现金净额')
    """处置固定资产、无形资产和其他长期资产收回的现金净额:"""

    NetCashDealSubCompany: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='NetCashDealSubCompany', column_type='decimal(19,4)', nullable=False, chn_name='处置子公司及其他营业单位收到的现金净额')
    """处置子公司及其他营业单位收到的现金净额:"""

    OtherCashFromInvestAct: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='OtherCashFromInvestAct', column_type='decimal(19,4)', nullable=False, chn_name='收到其他与投资活动有关的现金')
    """收到其他与投资活动有关的现金:"""

    SpecialItemsICIF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='SpecialItemsICIF', column_type='decimal(19,4)', nullable=False, chn_name='##投资活动现金流入特殊项目')
    """##投资活动现金流入特殊项目:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。"""

    AdjustmentItemsICIF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='AdjustmentItemsICIF', column_type='decimal(19,4)', nullable=False, chn_name='##投资活动现金流入调整项目')
    """##投资活动现金流入调整项目:"""

    SubtotalInvestCashInflow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='SubtotalInvestCashInflow', column_type='decimal(19,4)', nullable=False, chn_name='投资活动现金流入小计')
    """投资活动现金流入小计:"""

    FixIntanOtherAssetAcquiCash: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='FixIntanOtherAssetAcquiCash', column_type='decimal(19,4)', nullable=False, chn_name='购建固定资产、无形资产和其他长期资产支付的现金')
    """购建固定资产、无形资产和其他长期资产支付的现金:"""

    InvestCashPaid: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='InvestCashPaid', column_type='decimal(19,4)', nullable=False, chn_name='投资支付的现金')
    """投资支付的现金:"""

    NetCashFromSubCompany: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='NetCashFromSubCompany', column_type='decimal(19,4)', nullable=False, chn_name='取得子公司及其他营业单位支付的现金净额')
    """取得子公司及其他营业单位支付的现金净额:"""

    ImpawnedLoanNetIncrease: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='ImpawnedLoanNetIncrease', column_type='decimal(19,4)', nullable=False, chn_name='质押贷款净增加额')
    """质押贷款净增加额:"""

    OtherCashToInvestAct: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='OtherCashToInvestAct', column_type='decimal(19,4)', nullable=False, chn_name='支付其他与投资活动有关的现金')
    """支付其他与投资活动有关的现金:"""

    SpecialItemsICOF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='SpecialItemsICOF', column_type='decimal(19,4)', nullable=False, chn_name='##投资活动现金流出特殊项目')
    """##投资活动现金流出特殊项目:"""

    AdjustmentItemsICOF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='AdjustmentItemsICOF', column_type='decimal(19,4)', nullable=False, chn_name='##投资活动现金流出调整项目')
    """##投资活动现金流出调整项目:"""

    SubtotalInvestCashOutflow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='SubtotalInvestCashOutflow', column_type='decimal(19,4)', nullable=False, chn_name='投资活动现金流出小计')
    """投资活动现金流出小计:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    AdjustmentItemsNICF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='AdjustmentItemsNICF', column_type='decimal(19,4)', nullable=False, chn_name='##投资活动现金流量净额调整项目')
    """##投资活动现金流量净额调整项目:"""

    NetInvestCashFlow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='NetInvestCashFlow', column_type='decimal(19,4)', nullable=False, chn_name='投资活动产生的现金流量净额')
    """投资活动产生的现金流量净额:"""

    CashFromInvest: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='CashFromInvest', column_type='decimal(19,4)', nullable=False, chn_name='吸收投资收到的现金')
    """吸收投资收到的现金:"""

    CashFromMinoSInvestSub: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='CashFromMinoSInvestSub', column_type='decimal(19,4)', nullable=False, chn_name='其中:子公司吸收少数股东投资收到的现金')
    """其中:子公司吸收少数股东投资收到的现金:"""

    CashFromBondsIssue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='CashFromBondsIssue', column_type='decimal(19,4)', nullable=False, chn_name='发行债券收到的现金')
    """发行债券收到的现金:"""

    CashFromBorrowing: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='CashFromBorrowing', column_type='decimal(19,4)', nullable=False, chn_name='取得借款收到的现金')
    """取得借款收到的现金:"""

    OtherFinanceActCash: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='OtherFinanceActCash', column_type='decimal(19,4)', nullable=False, chn_name='收到其他与筹资活动有关的现金')
    """收到其他与筹资活动有关的现金:"""

    SpecialItemsFCIF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='SpecialItemsFCIF', column_type='decimal(19,4)', nullable=False, chn_name='##筹资活动现金流入特殊项目')
    """##筹资活动现金流入特殊项目:"""

    AdjustmentItemsFCIF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='AdjustmentItemsFCIF', column_type='decimal(19,4)', nullable=False, chn_name='##筹资活动现金流入调整项目')
    """##筹资活动现金流入调整项目:"""

    SubtotalFinanceCashInflow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='SubtotalFinanceCashInflow', column_type='decimal(19,4)', nullable=False, chn_name='筹资活动现金流入小计')
    """筹资活动现金流入小计:"""

    IfAdjusted: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='IfAdjusted', column_type='int', nullable=True, chn_name='是否调整')
    """是否调整:是否调整(IfAdjusted)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM IN (1,2,4,5)，得到是否调整的具体描述：1-是，2-否，4-否(7-9月)，5-是(7-9月)。"""

    BorrowingRepayment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='BorrowingRepayment', column_type='decimal(19,4)', nullable=False, chn_name='偿还债务支付的现金')
    """偿还债务支付的现金:"""

    DividendInterestPayment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='DividendInterestPayment', column_type='decimal(19,4)', nullable=False, chn_name='分配股利、利润或偿付利息支付的现金')
    """分配股利、利润或偿付利息支付的现金:"""

    ProceedsFromSubToMinoS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='ProceedsFromSubToMinoS', column_type='decimal(19,4)', nullable=False, chn_name='其中:子公司支付给少数股东的股利、利润或偿付的利息')
    """其中:子公司支付给少数股东的股利、利润或偿付的利息:"""

    OtherFinanceActPayment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='OtherFinanceActPayment', column_type='decimal(19,4)', nullable=False, chn_name='支付其他与筹资活动有关的现金')
    """支付其他与筹资活动有关的现金:"""

    SpecialItemsFCOF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='SpecialItemsFCOF', column_type='decimal(19,4)', nullable=False, chn_name='##筹资活动现金流出特殊项目')
    """##筹资活动现金流出特殊项目:"""

    AdjustmentItemsFCOF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='AdjustmentItemsFCOF', column_type='decimal(19,4)', nullable=False, chn_name='##筹资活动现金流出调整项目')
    """##筹资活动现金流出调整项目:"""

    SubtotalFinanceCashOutflow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='SubtotalFinanceCashOutflow', column_type='decimal(19,4)', nullable=False, chn_name='筹资活动现金流出小计')
    """筹资活动现金流出小计:"""

    AdjustmentItemsNFCF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='AdjustmentItemsNFCF', column_type='decimal(19,4)', nullable=False, chn_name='##筹资活动流量现金净额调整项目')
    """##筹资活动流量现金净额调整项目:"""

    NetFinanceCashFlow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='NetFinanceCashFlow', column_type='decimal(19,4)', nullable=False, chn_name='筹资活动产生的现金流量净额')
    """筹资活动产生的现金流量净额:"""

    ExchanRateChangeEffect: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='ExchanRateChangeEffect', column_type='decimal(19,4)', nullable=False, chn_name='汇率变动对现金及现金等价物的影响')
    """汇率变动对现金及现金等价物的影响:"""

    IfMerged: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='IfMerged', column_type='int', nullable=True, chn_name='是否合并')
    """是否合并:是否合并(IfMerged)与(CT_SystemConst)表中的DM字段关联，令LB = 1189 AND DM IN (1,2)，得到是否合并的具体描述：1-合并，2-母公司。"""

    OtherItemsEffectingCE: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='OtherItemsEffectingCE', column_type='decimal(19,4)', nullable=False, chn_name='##影响现金及现金等价物的其他科目')
    """##影响现金及现金等价物的其他科目:"""

    AdjustmentItemsCE: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='AdjustmentItemsCE', column_type='decimal(19,4)', nullable=False, chn_name='##影响现金及现金等价物的调整项目')
    """##影响现金及现金等价物的调整项目:"""

    CashEquivalentIncrease: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='CashEquivalentIncrease', column_type='decimal(19,4)', nullable=False, chn_name='现金及现金等价物净增加额')
    """现金及现金等价物净增加额:"""

    BeginPeriodCash: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='BeginPeriodCash', column_type='decimal(19,4)', nullable=False, chn_name='加:期初现金及现金等价物余额')
    """加:期初现金及现金等价物余额:"""

    OtherItemsEffectingCEI: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='OtherItemsEffectingCEI', column_type='decimal(19,4)', nullable=False, chn_name='##现金及现金等价物净增加额的特殊项目')
    """##现金及现金等价物净增加额的特殊项目:"""

    AdjustmentItemsCEI: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='AdjustmentItemsCEI', column_type='decimal(19,4)', nullable=False, chn_name='##现金及现金等价物净增加额的调整项目')
    """##现金及现金等价物净增加额的调整项目:"""

    EndPeriodCashEquivalent: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='EndPeriodCashEquivalent', column_type='decimal(19,4)', nullable=False, chn_name='期末现金及现金等价物余额')
    """期末现金及现金等价物余额:"""

    NetProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='NetProfit', column_type='decimal(19,4)', nullable=False, chn_name='净利润')
    """净利润:"""

    MinorityProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='MinorityProfit', column_type='decimal(19,4)', nullable=False, chn_name='加:少数股东损益')
    """加:少数股东损益:"""

    AssetsDepreciationReserves: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='AssetsDepreciationReserves', column_type='decimal(19,4)', nullable=False, chn_name='加:资产减值准备')
    """加:资产减值准备:"""

    AccountingStandards: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='AccountingStandards', column_type='int', nullable=True, chn_name='会计准则')
    """会计准则:会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 1455，得到会计准则的具体描述：1-新会计准则(2007)，9-旧会计准则。"""

    FixedAssetDepreciation: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='FixedAssetDepreciation', column_type='decimal(19,4)', nullable=False, chn_name='固定资产折旧')
    """固定资产折旧:"""

    InvestPropertyDA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='InvestPropertyDA', column_type='decimal(19,4)', nullable=False, chn_name='投资性房地产折旧/摊销')
    """投资性房地产折旧/摊销:"""

    IntangibleAssetAmortization: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='IntangibleAssetAmortization', column_type='decimal(19,4)', nullable=False, chn_name='无形资产摊销')
    """无形资产摊销:"""

    DeferredExpenseAmort: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='DeferredExpenseAmort', column_type='decimal(19,4)', nullable=False, chn_name='长期待摊费用摊销')
    """长期待摊费用摊销:"""

    DeferredExpenseDecreased: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='DeferredExpenseDecreased', column_type='decimal(19,4)', nullable=False, chn_name='待摊费用减少(减:增加)')
    """待摊费用减少(减:增加):"""

    AccruedExpenseAdded: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='AccruedExpenseAdded', column_type='decimal(19,4)', nullable=False, chn_name='预提费用增加(减:减少)')
    """预提费用增加(减:减少):"""

    FixIntanOtherAssetDispoLoss: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='FixIntanOtherAssetDispoLoss', column_type='decimal(19,4)', nullable=False, chn_name='处置固定资产、无形资产和其他长期资产的损失')
    """处置固定资产、无形资产和其他长期资产的损失:"""

    FixedAssetScrapLoss: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='FixedAssetScrapLoss', column_type='decimal(19,4)', nullable=False, chn_name='固定资产报废损失')
    """固定资产报废损失:"""

    LossFromFairValueChanges: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='LossFromFairValueChanges', column_type='decimal(19,4)', nullable=False, chn_name='公允价值变动损失')
    """公允价值变动损失:"""

    FinancialExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_CashFlowStatementAll', column_name='FinancialExpense', column_type='decimal(19,4)', nullable=False, chn_name='财务费用')
    """财务费用:"""

