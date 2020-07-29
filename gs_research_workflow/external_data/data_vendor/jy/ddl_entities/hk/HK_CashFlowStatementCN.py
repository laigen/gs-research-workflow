# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_CashFlowStatementCN(SQLTableEntity):
    name: str = 'HK_CashFlowStatementCN'
    
    chn_name: str = '港股现金流量表(中国会计准则)'
    
    business_unique: str = 'CompanyCode,EndDate,PeriodMark,Mark,CurrencyUnit'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.介绍按中国会计准则披露的港股现金流量表中各项指标，该表为现金流量表的横表，标准会计科目与A股基本相同。
2.数据范围：2003年至今。
3.数据来源：港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    CurrencyUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='CurrencyUnit', column_type='int', nullable=True, chn_name='货币单位')
    """货币单位:货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB=1068，得到货币单位的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，1170-约旦第纳尔，1180-科威特..."""

    CurrencyUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='CurrencyUnit', column_type='int', nullable=True, chn_name='货币单位')
    """货币单位:货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB=1068，得到货币单位的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，1170-约旦第纳尔，1180-科威特..."""

    DefTaxLiaInc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='DefTaxLiaInc', column_type='decimal(19,4)', nullable=False, chn_name='递延所得税负债增加')
    """递延所得税负债增加:"""

    DefTaxLiaInc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='DefTaxLiaInc', column_type='decimal(19,4)', nullable=False, chn_name='递延所得税负债增加')
    """递延所得税负债增加:"""

    InvDec: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='InvDec', column_type='decimal(19,4)', nullable=False, chn_name='存货的减少')
    """存货的减少:"""

    InvDec: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='InvDec', column_type='decimal(19,4)', nullable=False, chn_name='存货的减少')
    """存货的减少:"""

    OpeRecDec: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='OpeRecDec', column_type='decimal(19,4)', nullable=False, chn_name='经营性应收项目的减少')
    """经营性应收项目的减少:"""

    OpeRecDec: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='OpeRecDec', column_type='decimal(19,4)', nullable=False, chn_name='经营性应收项目的减少')
    """经营性应收项目的减少:"""

    OpePayableInc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='OpePayableInc', column_type='decimal(19,4)', nullable=False, chn_name='经营性应付项目的增加')
    """经营性应付项目的增加:"""

    OpePayableInc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='OpePayableInc', column_type='decimal(19,4)', nullable=False, chn_name='经营性应付项目的增加')
    """经营性应付项目的增加:"""

    Others: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='Others', column_type='decimal(19,4)', nullable=False, chn_name='其他')
    """其他:"""

    Others: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='Others', column_type='decimal(19,4)', nullable=False, chn_name='其他')
    """其他:"""

    SpeItemsNOCF1: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='SpeItemsNOCF1', column_type='decimal(19,4)', nullable=False, chn_name='(附注)经营活动现金流量净额特殊项目')
    """(附注)经营活动现金流量净额特殊项目:"""

    SpeItemsNOCF1: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='SpeItemsNOCF1', column_type='decimal(19,4)', nullable=False, chn_name='(附注)经营活动现金流量净额特殊项目')
    """(附注)经营活动现金流量净额特殊项目:"""

    AdjItemsNOCF1: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='AdjItemsNOCF1', column_type='decimal(19,4)', nullable=False, chn_name='(附注)经营活动现金流量净额调整项目')
    """(附注)经营活动现金流量净额调整项目:"""

    AdjItemsNOCF1: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='AdjItemsNOCF1', column_type='decimal(19,4)', nullable=False, chn_name='(附注)经营活动现金流量净额调整项目')
    """(附注)经营活动现金流量净额调整项目:"""

    NetOpeCFNotes: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetOpeCFNotes', column_type='decimal(19,4)', nullable=False, chn_name='(附注)经营活动产生的现金流量净额')
    """(附注)经营活动产生的现金流量净额:"""

    NetOpeCFNotes: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetOpeCFNotes', column_type='decimal(19,4)', nullable=False, chn_name='(附注)经营活动产生的现金流量净额')
    """(附注)经营活动产生的现金流量净额:"""

    ConAdjNOCF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='ConAdjNOCF', column_type='decimal(19,4)', nullable=False, chn_name='加:经营流量净额前后对比调整项目')
    """加:经营流量净额前后对比调整项目:"""

    ConAdjNOCF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='ConAdjNOCF', column_type='decimal(19,4)', nullable=False, chn_name='加:经营流量净额前后对比调整项目')
    """加:经营流量净额前后对比调整项目:"""

    DebtToCap: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='DebtToCap', column_type='decimal(19,4)', nullable=False, chn_name='债务转为资本')
    """债务转为资本:"""

    DebtToCap: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='DebtToCap', column_type='decimal(19,4)', nullable=False, chn_name='债务转为资本')
    """债务转为资本:"""

    GdSaSeReCash: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='GdSaSeReCash', column_type='decimal(19,4)', nullable=False, chn_name='销售商品、提供劳务收到的现金')
    """销售商品、提供劳务收到的现金:"""

    GdSaSeReCash: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='GdSaSeReCash', column_type='decimal(19,4)', nullable=False, chn_name='销售商品、提供劳务收到的现金')
    """销售商品、提供劳务收到的现金:"""

    CBsExpWithin1Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='CBsExpWithin1Y', column_type='decimal(19,4)', nullable=False, chn_name='一年内到期的可转换公司债券')
    """一年内到期的可转换公司债券:"""

    CBsExpWithin1Y: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='CBsExpWithin1Y', column_type='decimal(19,4)', nullable=False, chn_name='一年内到期的可转换公司债券')
    """一年内到期的可转换公司债券:"""

    FixedAFinLeases: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='FixedAFinLeases', column_type='decimal(19,4)', nullable=False, chn_name='融资租入固定资产')
    """融资租入固定资产:"""

    FixedAFinLeases: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='FixedAFinLeases', column_type='decimal(19,4)', nullable=False, chn_name='融资租入固定资产')
    """融资租入固定资产:"""

    CashAtEndOfYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='CashAtEndOfYear', column_type='decimal(19,4)', nullable=False, chn_name='现金的期末余额')
    """现金的期末余额:"""

    CashAtEndOfYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='CashAtEndOfYear', column_type='decimal(19,4)', nullable=False, chn_name='现金的期末余额')
    """现金的期末余额:"""

    CashAtBOfYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='CashAtBOfYear', column_type='decimal(19,4)', nullable=False, chn_name='减:现金的期初余额')
    """减:现金的期初余额:"""

    CashAtBOfYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='CashAtBOfYear', column_type='decimal(19,4)', nullable=False, chn_name='减:现金的期初余额')
    """减:现金的期初余额:"""

    CEquAtEOfYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='CEquAtEOfYear', column_type='decimal(19,4)', nullable=False, chn_name='加:现金等价物的期末余额')
    """加:现金等价物的期末余额:"""

    CEquAtEOfYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='CEquAtEOfYear', column_type='decimal(19,4)', nullable=False, chn_name='加:现金等价物的期末余额')
    """加:现金等价物的期末余额:"""

    CEquAtBeginning: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='CEquAtBeginning', column_type='decimal(19,4)', nullable=False, chn_name='减:现金等价物的期初余额')
    """减:现金等价物的期初余额:"""

    CEquAtBeginning: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='CEquAtBeginning', column_type='decimal(19,4)', nullable=False, chn_name='减:现金等价物的期初余额')
    """减:现金等价物的期初余额:"""

    ConAdjNC: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='ConAdjNC', column_type='decimal(19,4)', nullable=False, chn_name='加:现金净额前后对比调整项目')
    """加:现金净额前后对比调整项目:"""

    ConAdjNC: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='ConAdjNC', column_type='decimal(19,4)', nullable=False, chn_name='加:现金净额前后对比调整项目')
    """加:现金净额前后对比调整项目:"""

    SpeItemsC: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='SpeItemsC', column_type='decimal(19,4)', nullable=False, chn_name='(附注)现金特殊项目')
    """(附注)现金特殊项目:"""

    SpeItemsC: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='SpeItemsC', column_type='decimal(19,4)', nullable=False, chn_name='(附注)现金特殊项目')
    """(附注)现金特殊项目:"""

    AdjItemsC: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='AdjItemsC', column_type='decimal(19,4)', nullable=False, chn_name='(附注)现金调整项目')
    """(附注)现金调整项目:"""

    AdjItemsC: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='AdjItemsC', column_type='decimal(19,4)', nullable=False, chn_name='(附注)现金调整项目')
    """(附注)现金调整项目:"""

    NetIncrInCEqu: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetIncrInCEqu', column_type='decimal(19,4)', nullable=False, chn_name='(附注)现金及现金等价物净增加额')
    """(附注)现金及现金等价物净增加额:"""

    NetIncrInCEqu: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetIncrInCEqu', column_type='decimal(19,4)', nullable=False, chn_name='(附注)现金及现金等价物净增加额')
    """(附注)现金及现金等价物净增加额:"""

    TaxLeRefund: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='TaxLeRefund', column_type='decimal(19,4)', nullable=False, chn_name='收到的税费返还')
    """收到的税费返还:"""

    TaxLeRefund: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='TaxLeRefund', column_type='decimal(19,4)', nullable=False, chn_name='收到的税费返还')
    """收到的税费返还:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    NetDepInce: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetDepInce', column_type='decimal(19,4)', nullable=False, chn_name='客户存款和同业存放款项净增加额')
    """客户存款和同业存放款项净增加额:"""

    NetDepInce: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetDepInce', column_type='decimal(19,4)', nullable=False, chn_name='客户存款和同业存放款项净增加额')
    """客户存款和同业存放款项净增加额:"""

    NetBorFromCB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetBorFromCB', column_type='decimal(19,4)', nullable=False, chn_name='向中央银行借款净增加额')
    """向中央银行借款净增加额:"""

    NetBorFromCB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetBorFromCB', column_type='decimal(19,4)', nullable=False, chn_name='向中央银行借款净增加额')
    """向中央银行借款净增加额:"""

    NetBorFromFinCo: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetBorFromFinCo', column_type='decimal(19,4)', nullable=False, chn_name='向其他金融机构拆入资金净增加额')
    """向其他金融机构拆入资金净增加额:"""

    NetBorFromFinCo: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetBorFromFinCo', column_type='decimal(19,4)', nullable=False, chn_name='向其他金融机构拆入资金净增加额')
    """向其他金融机构拆入资金净增加额:"""

    DrBaLoansCanc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='DrBaLoansCanc', column_type='decimal(19,4)', nullable=False, chn_name='收回已核销贷款')
    """收回已核销贷款:"""

    DrBaLoansCanc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='DrBaLoansCanc', column_type='decimal(19,4)', nullable=False, chn_name='收回已核销贷款')
    """收回已核销贷款:"""

    IntAndComCashIn: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='IntAndComCashIn', column_type='decimal(19,4)', nullable=False, chn_name='收取利息、手续费及佣金的现金')
    """收取利息、手续费及佣金的现金:"""

    IntAndComCashIn: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='IntAndComCashIn', column_type='decimal(19,4)', nullable=False, chn_name='收取利息、手续费及佣金的现金')
    """收取利息、手续费及佣金的现金:"""

    NDealTradAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NDealTradAssets', column_type='decimal(19,4)', nullable=False, chn_name='处置交易性金融资产净增加额')
    """处置交易性金融资产净增加额:"""

    NDealTradAssets: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NDealTradAssets', column_type='decimal(19,4)', nullable=False, chn_name='处置交易性金融资产净增加额')
    """处置交易性金融资产净增加额:"""

    NetBuyBack: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetBuyBack', column_type='decimal(19,4)', nullable=False, chn_name='回购业务资金净增加额')
    """回购业务资金净增加额:"""

    NetBuyBack: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetBuyBack', column_type='decimal(19,4)', nullable=False, chn_name='回购业务资金净增加额')
    """回购业务资金净增加额:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到所属公司股票的交易代码、简称等。"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到所属公司股票的交易代码、简称等。"""

    NetOriInsCash: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetOriInsCash', column_type='decimal(19,4)', nullable=False, chn_name='收到原保险合同保费取得的现金')
    """收到原保险合同保费取得的现金:"""

    NetOriInsCash: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetOriInsCash', column_type='decimal(19,4)', nullable=False, chn_name='收到原保险合同保费取得的现金')
    """收到原保险合同保费取得的现金:"""

    NetReinCash: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetReinCash', column_type='decimal(19,4)', nullable=False, chn_name='收到再保业务现金净额')
    """收到再保业务现金净额:"""

    NetReinCash: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetReinCash', column_type='decimal(19,4)', nullable=False, chn_name='收到再保业务现金净额')
    """收到再保业务现金净额:"""

    NetInsDepInv: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetInsDepInv', column_type='decimal(19,4)', nullable=False, chn_name='保户储金及投资款净增加额')
    """保户储金及投资款净增加额:"""

    NetInsDepInv: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetInsDepInv', column_type='decimal(19,4)', nullable=False, chn_name='保户储金及投资款净增加额')
    """保户储金及投资款净增加额:"""

    OthCashInRelOpe: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='OthCashInRelOpe', column_type='decimal(19,4)', nullable=False, chn_name='收到其他与经营活动有关的现金')
    """收到其他与经营活动有关的现金:"""

    OthCashInRelOpe: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='OthCashInRelOpe', column_type='decimal(19,4)', nullable=False, chn_name='收到其他与经营活动有关的现金')
    """收到其他与经营活动有关的现金:"""

    SpeItemsOCIF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='SpeItemsOCIF', column_type='decimal(19,4)', nullable=False, chn_name='经营活动现金流入特殊项目')
    """经营活动现金流入特殊项目:"""

    SpeItemsOCIF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='SpeItemsOCIF', column_type='decimal(19,4)', nullable=False, chn_name='经营活动现金流入特殊项目')
    """经营活动现金流入特殊项目:"""

    AdjItemsOCIF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='AdjItemsOCIF', column_type='decimal(19,4)', nullable=False, chn_name='经营活动现金流入调整项目')
    """经营活动现金流入调整项目:"""

    AdjItemsOCIF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='AdjItemsOCIF', column_type='decimal(19,4)', nullable=False, chn_name='经营活动现金流入调整项目')
    """经营活动现金流入调整项目:"""

    SuOpCashInflow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='SuOpCashInflow', column_type='decimal(19,4)', nullable=False, chn_name='经营活动现金流入小计')
    """经营活动现金流入小计:若经营活动现金流入小计为空，则以销售商品、提供劳务收到的现金+收到的税费返还+客户存款和同业存放款项净增加额+向中央银行借款净增加额+向其他金融机构拆入资金净增加额+收回已核销贷款+收取利息、手续费及佣金的现金+处置交易性金融资产净增加额+回购业务资金净增加额+收到原保险合同保费取得的现金+收到再保业务现金净额+保户储金及投资款净增加额+收到其他与经营活动有..."""

    SuOpCashInflow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='SuOpCashInflow', column_type='decimal(19,4)', nullable=False, chn_name='经营活动现金流入小计')
    """经营活动现金流入小计:若经营活动现金流入小计为空，则以销售商品、提供劳务收到的现金+收到的税费返还+客户存款和同业存放款项净增加额+向中央银行借款净增加额+向其他金融机构拆入资金净增加额+收回已核销贷款+收取利息、手续费及佣金的现金+处置交易性金融资产净增加额+回购业务资金净增加额+收到原保险合同保费取得的现金+收到再保业务现金净额+保户储金及投资款净增加额+收到其他与经营活动有..."""

    GdSerCashPaid: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='GdSerCashPaid', column_type='decimal(19,4)', nullable=False, chn_name='购买商品、接受劳务支付的现金')
    """购买商品、接受劳务支付的现金:"""

    GdSerCashPaid: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='GdSerCashPaid', column_type='decimal(19,4)', nullable=False, chn_name='购买商品、接受劳务支付的现金')
    """购买商品、接受劳务支付的现金:"""

    StaBehalfPaid: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='StaBehalfPaid', column_type='decimal(19,4)', nullable=False, chn_name='支付给职工以及为职工支付的现金')
    """支付给职工以及为职工支付的现金:"""

    StaBehalfPaid: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='StaBehalfPaid', column_type='decimal(19,4)', nullable=False, chn_name='支付给职工以及为职工支付的现金')
    """支付给职工以及为职工支付的现金:"""

    AllTaxesPaid: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='AllTaxesPaid', column_type='decimal(19,4)', nullable=False, chn_name='支付的各项税费')
    """支付的各项税费:"""

    AllTaxesPaid: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='AllTaxesPaid', column_type='decimal(19,4)', nullable=False, chn_name='支付的各项税费')
    """支付的各项税费:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    NetLAdvInc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetLAdvInc', column_type='decimal(19,4)', nullable=False, chn_name='客户贷款及垫款净增加额')
    """客户贷款及垫款净增加额:"""

    NetLAdvInc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetLAdvInc', column_type='decimal(19,4)', nullable=False, chn_name='客户贷款及垫款净增加额')
    """客户贷款及垫款净增加额:"""

    NetDepInCBAndIB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetDepInCBAndIB', column_type='decimal(19,4)', nullable=False, chn_name='存放中央银行和同业款项净增加额')
    """存放中央银行和同业款项净增加额:"""

    NetDepInCBAndIB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetDepInCBAndIB', column_type='decimal(19,4)', nullable=False, chn_name='存放中央银行和同业款项净增加额')
    """存放中央银行和同业款项净增加额:"""

    NetLendCap: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetLendCap', column_type='decimal(19,4)', nullable=False, chn_name='拆出资金净增加额')
    """拆出资金净增加额:"""

    NetLendCap: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetLendCap', column_type='decimal(19,4)', nullable=False, chn_name='拆出资金净增加额')
    """拆出资金净增加额:"""

    ComCashPaid: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='ComCashPaid', column_type='decimal(19,4)', nullable=False, chn_name='支付利息、手续费及佣金的现金')
    """支付利息、手续费及佣金的现金:"""

    ComCashPaid: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='ComCashPaid', column_type='decimal(19,4)', nullable=False, chn_name='支付利息、手续费及佣金的现金')
    """支付利息、手续费及佣金的现金:"""

    OriCompPaid: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='OriCompPaid', column_type='decimal(19,4)', nullable=False, chn_name='支付原保险合同赔付款项的现金')
    """支付原保险合同赔付款项的现金:"""

    OriCompPaid: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='OriCompPaid', column_type='decimal(19,4)', nullable=False, chn_name='支付原保险合同赔付款项的现金')
    """支付原保险合同赔付款项的现金:"""

    NetCashForRein: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetCashForRein', column_type='decimal(19,4)', nullable=False, chn_name='支付再保业务现金净额')
    """支付再保业务现金净额:"""

    NetCashForRein: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetCashForRein', column_type='decimal(19,4)', nullable=False, chn_name='支付再保业务现金净额')
    """支付再保业务现金净额:"""

    PolDivCashPaid: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='PolDivCashPaid', column_type='decimal(19,4)', nullable=False, chn_name='支付保单红利的现金')
    """支付保单红利的现金:"""

    PolDivCashPaid: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='PolDivCashPaid', column_type='decimal(19,4)', nullable=False, chn_name='支付保单红利的现金')
    """支付保单红利的现金:"""

    OtherOpCashPaid: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='OtherOpCashPaid', column_type='decimal(19,4)', nullable=False, chn_name='支付其他与经营活动有关的现金')
    """支付其他与经营活动有关的现金:"""

    OtherOpCashPaid: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='OtherOpCashPaid', column_type='decimal(19,4)', nullable=False, chn_name='支付其他与经营活动有关的现金')
    """支付其他与经营活动有关的现金:"""

    SpeItemsOCOF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='SpeItemsOCOF', column_type='decimal(19,4)', nullable=False, chn_name='经营活动现金流出特殊项目')
    """经营活动现金流出特殊项目:"""

    SpeItemsOCOF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='SpeItemsOCOF', column_type='decimal(19,4)', nullable=False, chn_name='经营活动现金流出特殊项目')
    """经营活动现金流出特殊项目:"""

    AdjItemsOCOF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='AdjItemsOCOF', column_type='decimal(19,4)', nullable=False, chn_name='经营活动现金流出调整项目')
    """经营活动现金流出调整项目:"""

    AdjItemsOCOF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='AdjItemsOCOF', column_type='decimal(19,4)', nullable=False, chn_name='经营活动现金流出调整项目')
    """经营活动现金流出调整项目:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='InfoSource', column_type='varchar(100)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='InfoSource', column_type='varchar(100)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    SubOpCOutflow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='SubOpCOutflow', column_type='decimal(19,4)', nullable=False, chn_name='经营活动现金流出小计')
    """经营活动现金流出小计:若经营活动现金流出小计为空，则以购买商品、接受劳务支付的现金+支付给职工以及为职工支付的现金+支付的各项税费+客户贷款及垫款净增加额+存放中央银行和同业款项净增加额+拆出资金净增加额+支付利息、手续费及佣金的现金+支付原保险合同赔付款项的现金+支付再保业务现金净额+支付保单红利的现金+支付其他与经营活动有关的现金+经营活动现金流出特殊项目+经营活动现金流出调..."""

    SubOpCOutflow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='SubOpCOutflow', column_type='decimal(19,4)', nullable=False, chn_name='经营活动现金流出小计')
    """经营活动现金流出小计:若经营活动现金流出小计为空，则以购买商品、接受劳务支付的现金+支付给职工以及为职工支付的现金+支付的各项税费+客户贷款及垫款净增加额+存放中央银行和同业款项净增加额+拆出资金净增加额+支付利息、手续费及佣金的现金+支付原保险合同赔付款项的现金+支付再保业务现金净额+支付保单红利的现金+支付其他与经营活动有关的现金+经营活动现金流出特殊项目+经营活动现金流出调..."""

    AdjItemsNOCF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='AdjItemsNOCF', column_type='decimal(19,4)', nullable=False, chn_name='经营活动现金流量净额调整项目')
    """经营活动现金流量净额调整项目:"""

    AdjItemsNOCF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='AdjItemsNOCF', column_type='decimal(19,4)', nullable=False, chn_name='经营活动现金流量净额调整项目')
    """经营活动现金流量净额调整项目:"""

    NetOpeCFlow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetOpeCFlow', column_type='decimal(19,4)', nullable=False, chn_name='经营活动产生的现金流量净额')
    """经营活动产生的现金流量净额:若经营活动产生的现金流量净额为空，则经营活动现金流入小计-经营活动现金流出小计+经营活动现金流量净额调整项目填充。"""

    NetOpeCFlow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetOpeCFlow', column_type='decimal(19,4)', nullable=False, chn_name='经营活动产生的现金流量净额')
    """经营活动产生的现金流量净额:若经营活动产生的现金流量净额为空，则经营活动现金流入小计-经营活动现金流出小计+经营活动现金流量净额调整项目填充。"""

    InvWithdCash: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='InvWithdCash', column_type='decimal(19,4)', nullable=False, chn_name='收回投资收到的现金')
    """收回投资收到的现金:"""

    InvWithdCash: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='InvWithdCash', column_type='decimal(19,4)', nullable=False, chn_name='收回投资收到的现金')
    """收回投资收到的现金:"""

    Invproceeds: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='Invproceeds', column_type='decimal(19,4)', nullable=False, chn_name='取得投资收益收到的现金')
    """取得投资收益收到的现金:"""

    Invproceeds: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='Invproceeds', column_type='decimal(19,4)', nullable=False, chn_name='取得投资收益收到的现金')
    """取得投资收益收到的现金:"""

    FixInOtADisCash: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='FixInOtADisCash', column_type='decimal(19,4)', nullable=False, chn_name='处置固定资产、无形资产和其他长期资产收回的现金净额')
    """处置固定资产、无形资产和其他长期资产收回的现金净额:"""

    FixInOtADisCash: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='FixInOtADisCash', column_type='decimal(19,4)', nullable=False, chn_name='处置固定资产、无形资产和其他长期资产收回的现金净额')
    """处置固定资产、无形资产和其他长期资产收回的现金净额:"""

    NCashDealSComp: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NCashDealSComp', column_type='decimal(19,4)', nullable=False, chn_name='处置子公司及其他营业单位收到的现金净额')
    """处置子公司及其他营业单位收到的现金净额:"""

    NCashDealSComp: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NCashDealSComp', column_type='decimal(19,4)', nullable=False, chn_name='处置子公司及其他营业单位收到的现金净额')
    """处置子公司及其他营业单位收到的现金净额:"""

    OthCaFromInvAct: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='OthCaFromInvAct', column_type='decimal(19,4)', nullable=False, chn_name='收到其他与投资活动有关的现金')
    """收到其他与投资活动有关的现金:"""

    OthCaFromInvAct: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='OthCaFromInvAct', column_type='decimal(19,4)', nullable=False, chn_name='收到其他与投资活动有关的现金')
    """收到其他与投资活动有关的现金:"""

    SpeItemsICIF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='SpeItemsICIF', column_type='decimal(19,4)', nullable=False, chn_name='投资活动现金流入特殊项目')
    """投资活动现金流入特殊项目:"""

    SpeItemsICIF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='SpeItemsICIF', column_type='decimal(19,4)', nullable=False, chn_name='投资活动现金流入特殊项目')
    """投资活动现金流入特殊项目:"""

    AdjItemsICIF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='AdjItemsICIF', column_type='decimal(19,4)', nullable=False, chn_name='投资活动现金流入调整项目')
    """投资活动现金流入调整项目:"""

    AdjItemsICIF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='AdjItemsICIF', column_type='decimal(19,4)', nullable=False, chn_name='投资活动现金流入调整项目')
    """投资活动现金流入调整项目:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    SubInvCaInflow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='SubInvCaInflow', column_type='decimal(19,4)', nullable=False, chn_name='投资活动现金流入小计')
    """投资活动现金流入小计:若投资活动现金流入小计为空，则以收回投资收到的现金+取得投资收益收到的现金+处置固定资产、无形资产和其他长期资产收回的现金净额+处置子公司及其他营业单位收到的现金净额+收到其他与投资活动有关的现金+投资活动现金流入特殊项目+投资活动现金流入调整项目填充。"""

    SubInvCaInflow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='SubInvCaInflow', column_type='decimal(19,4)', nullable=False, chn_name='投资活动现金流入小计')
    """投资活动现金流入小计:若投资活动现金流入小计为空，则以收回投资收到的现金+取得投资收益收到的现金+处置固定资产、无形资产和其他长期资产收回的现金净额+处置子公司及其他营业单位收到的现金净额+收到其他与投资活动有关的现金+投资活动现金流入特殊项目+投资活动现金流入调整项目填充。"""

    FixInOAsAcCash: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='FixInOAsAcCash', column_type='decimal(19,4)', nullable=False, chn_name='购建固定资产、无形资产和其他长期资产支付的现金')
    """购建固定资产、无形资产和其他长期资产支付的现金:"""

    FixInOAsAcCash: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='FixInOAsAcCash', column_type='decimal(19,4)', nullable=False, chn_name='购建固定资产、无形资产和其他长期资产支付的现金')
    """购建固定资产、无形资产和其他长期资产支付的现金:"""

    InvCashPaid: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='InvCashPaid', column_type='decimal(19,4)', nullable=False, chn_name='投资支付的现金')
    """投资支付的现金:"""

    InvCashPaid: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='InvCashPaid', column_type='decimal(19,4)', nullable=False, chn_name='投资支付的现金')
    """投资支付的现金:"""

    NCashFromSComp: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NCashFromSComp', column_type='decimal(19,4)', nullable=False, chn_name='取得子公司及其他营业单位支付的现金净额')
    """取得子公司及其他营业单位支付的现金净额:"""

    NCashFromSComp: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NCashFromSComp', column_type='decimal(19,4)', nullable=False, chn_name='取得子公司及其他营业单位支付的现金净额')
    """取得子公司及其他营业单位支付的现金净额:"""

    ImLoanNetInc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='ImLoanNetInc', column_type='decimal(19,4)', nullable=False, chn_name='质押贷款净增加额')
    """质押贷款净增加额:"""

    ImLoanNetInc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='ImLoanNetInc', column_type='decimal(19,4)', nullable=False, chn_name='质押贷款净增加额')
    """质押贷款净增加额:"""

    OthCashToInvAct: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='OthCashToInvAct', column_type='decimal(19,4)', nullable=False, chn_name='支付其他与投资活动有关的现金')
    """支付其他与投资活动有关的现金:"""

    OthCashToInvAct: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='OthCashToInvAct', column_type='decimal(19,4)', nullable=False, chn_name='支付其他与投资活动有关的现金')
    """支付其他与投资活动有关的现金:"""

    SpeItemsICOF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='SpeItemsICOF', column_type='decimal(19,4)', nullable=False, chn_name='投资活动现金流出特殊项目')
    """投资活动现金流出特殊项目:"""

    SpeItemsICOF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='SpeItemsICOF', column_type='decimal(19,4)', nullable=False, chn_name='投资活动现金流出特殊项目')
    """投资活动现金流出特殊项目:"""

    AdjItemsICOF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='AdjItemsICOF', column_type='decimal(19,4)', nullable=False, chn_name='投资活动现金流出调整项目')
    """投资活动现金流出调整项目:"""

    AdjItemsICOF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='AdjItemsICOF', column_type='decimal(19,4)', nullable=False, chn_name='投资活动现金流出调整项目')
    """投资活动现金流出调整项目:"""

    SubInvCashOflow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='SubInvCashOflow', column_type='decimal(19,4)', nullable=False, chn_name='投资活动现金流出小计')
    """投资活动现金流出小计:若投资活动现金流出小计为空，则以购建固定资产、无形资产和其他长期资产支付的现金+投资支付的现金+取得子公司及其他营业单位支付的现金净额+质押贷款净增加额+支付其他与投资活动有关的现金+投资活动现金流出特殊项目+投资活动现金流出调整项目填充。"""

    SubInvCashOflow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='SubInvCashOflow', column_type='decimal(19,4)', nullable=False, chn_name='投资活动现金流出小计')
    """投资活动现金流出小计:若投资活动现金流出小计为空，则以购建固定资产、无形资产和其他长期资产支付的现金+投资支付的现金+取得子公司及其他营业单位支付的现金净额+质押贷款净增加额+支付其他与投资活动有关的现金+投资活动现金流出特殊项目+投资活动现金流出调整项目填充。"""

    AdjItemsNICF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='AdjItemsNICF', column_type='decimal(19,4)', nullable=False, chn_name='投资活动现金流量净额调整项目')
    """投资活动现金流量净额调整项目:"""

    AdjItemsNICF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='AdjItemsNICF', column_type='decimal(19,4)', nullable=False, chn_name='投资活动现金流量净额调整项目')
    """投资活动现金流量净额调整项目:"""

    PeriodMark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='PeriodMark', column_type='int', nullable=True, chn_name='日期标志')
    """日期标志:日期标志(PeriodMark)与(CT_SystemConst)表中的DM字段关联，令LB=1314，得到日期标志的具体描述：1-1个月，2-2个月，3-3个月，4-4个月，5-5个月，6-半年度，7-7个月，8-8个月，9-9个月，10-10个月，11-11个月，12-年度，13-13个月，14-14个月，15-15个月，16-16个月，17-17个月，..."""

    PeriodMark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='PeriodMark', column_type='int', nullable=True, chn_name='日期标志')
    """日期标志:日期标志(PeriodMark)与(CT_SystemConst)表中的DM字段关联，令LB=1314，得到日期标志的具体描述：1-1个月，2-2个月，3-3个月，4-4个月，5-5个月，6-半年度，7-7个月，8-8个月，9-9个月，10-10个月，11-11个月，12-年度，13-13个月，14-14个月，15-15个月，16-16个月，17-17个月，..."""

    NetInvCashFlow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetInvCashFlow', column_type='decimal(19,4)', nullable=False, chn_name='投资活动产生的现金流量净额')
    """投资活动产生的现金流量净额:若投资活动产生的现金流量净额为空，则以投资活动现金流入小计-投资活动现金流出小计+投资活动现金流量净额调整项目填充。"""

    NetInvCashFlow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetInvCashFlow', column_type='decimal(19,4)', nullable=False, chn_name='投资活动产生的现金流量净额')
    """投资活动产生的现金流量净额:若投资活动产生的现金流量净额为空，则以投资活动现金流入小计-投资活动现金流出小计+投资活动现金流量净额调整项目填充。"""

    CashFromInv: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='CashFromInv', column_type='decimal(19,4)', nullable=False, chn_name='吸收投资收到的现金')
    """吸收投资收到的现金:"""

    CashFromInv: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='CashFromInv', column_type='decimal(19,4)', nullable=False, chn_name='吸收投资收到的现金')
    """吸收投资收到的现金:"""

    CFMinoSInvSub: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='CFMinoSInvSub', column_type='decimal(19,4)', nullable=False, chn_name='其中:子公司吸收少数股东投资收到的现金')
    """其中:子公司吸收少数股东投资收到的现金:"""

    CFMinoSInvSub: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='CFMinoSInvSub', column_type='decimal(19,4)', nullable=False, chn_name='其中:子公司吸收少数股东投资收到的现金')
    """其中:子公司吸收少数股东投资收到的现金:"""

    CFBondsIssue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='CFBondsIssue', column_type='decimal(19,4)', nullable=False, chn_name='发行债券收到的现金')
    """发行债券收到的现金:"""

    CFBondsIssue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='CFBondsIssue', column_type='decimal(19,4)', nullable=False, chn_name='发行债券收到的现金')
    """发行债券收到的现金:"""

    CFBorrowing: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='CFBorrowing', column_type='decimal(19,4)', nullable=False, chn_name='取得借款收到的现金')
    """取得借款收到的现金:"""

    CFBorrowing: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='CFBorrowing', column_type='decimal(19,4)', nullable=False, chn_name='取得借款收到的现金')
    """取得借款收到的现金:"""

    OthFinActCash: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='OthFinActCash', column_type='decimal(19,4)', nullable=False, chn_name='收到其他与筹资活动有关的现金')
    """收到其他与筹资活动有关的现金:"""

    OthFinActCash: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='OthFinActCash', column_type='decimal(19,4)', nullable=False, chn_name='收到其他与筹资活动有关的现金')
    """收到其他与筹资活动有关的现金:"""

    SpeItemsFCIF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='SpeItemsFCIF', column_type='decimal(19,4)', nullable=False, chn_name='筹资活动现金流入特殊项目')
    """筹资活动现金流入特殊项目:"""

    SpeItemsFCIF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='SpeItemsFCIF', column_type='decimal(19,4)', nullable=False, chn_name='筹资活动现金流入特殊项目')
    """筹资活动现金流入特殊项目:"""

    AdjItemsFCIF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='AdjItemsFCIF', column_type='decimal(19,4)', nullable=False, chn_name='筹资活动现金流入调整项目')
    """筹资活动现金流入调整项目:"""

    AdjItemsFCIF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='AdjItemsFCIF', column_type='decimal(19,4)', nullable=False, chn_name='筹资活动现金流入调整项目')
    """筹资活动现金流入调整项目:"""

    SubFinCashInfl: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='SubFinCashInfl', column_type='decimal(19,4)', nullable=False, chn_name='筹资活动现金流入小计')
    """筹资活动现金流入小计:若筹资活动现金流入小计为空，则以吸收投资收到的现金+发行债券收到的现金+取得借款收到的现金+收到其他与筹资活动有关的现金+筹资活动现金流入特殊项目+筹资活动现金流入调整项目填充。"""

    SubFinCashInfl: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='SubFinCashInfl', column_type='decimal(19,4)', nullable=False, chn_name='筹资活动现金流入小计')
    """筹资活动现金流入小计:若筹资活动现金流入小计为空，则以吸收投资收到的现金+发行债券收到的现金+取得借款收到的现金+收到其他与筹资活动有关的现金+筹资活动现金流入特殊项目+筹资活动现金流入调整项目填充。"""

    BorRepayment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='BorRepayment', column_type='decimal(19,4)', nullable=False, chn_name='偿还债务支付的现金')
    """偿还债务支付的现金:"""

    BorRepayment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='BorRepayment', column_type='decimal(19,4)', nullable=False, chn_name='偿还债务支付的现金')
    """偿还债务支付的现金:"""

    FiscalYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='FiscalYear', column_type='datetime', nullable=False, chn_name='财政年度')
    """财政年度:"""

    FiscalYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='FiscalYear', column_type='datetime', nullable=False, chn_name='财政年度')
    """财政年度:"""

    DivIntPayment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='DivIntPayment', column_type='decimal(19,4)', nullable=False, chn_name='分配股利、利润或偿付利息支付的现金')
    """分配股利、利润或偿付利息支付的现金:"""

    DivIntPayment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='DivIntPayment', column_type='decimal(19,4)', nullable=False, chn_name='分配股利、利润或偿付利息支付的现金')
    """分配股利、利润或偿付利息支付的现金:"""

    ProFromSubTMiS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='ProFromSubTMiS', column_type='decimal(19,4)', nullable=False, chn_name='其中:子公司支付给少数股东的股利、利润或偿付的利息')
    """其中:子公司支付给少数股东的股利、利润或偿付的利息:"""

    ProFromSubTMiS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='ProFromSubTMiS', column_type='decimal(19,4)', nullable=False, chn_name='其中:子公司支付给少数股东的股利、利润或偿付的利息')
    """其中:子公司支付给少数股东的股利、利润或偿付的利息:"""

    OthFinActP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='OthFinActP', column_type='decimal(19,4)', nullable=False, chn_name='支付其他与筹资活动有关的现金')
    """支付其他与筹资活动有关的现金:"""

    OthFinActP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='OthFinActP', column_type='decimal(19,4)', nullable=False, chn_name='支付其他与筹资活动有关的现金')
    """支付其他与筹资活动有关的现金:"""

    SpeItemsFCOF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='SpeItemsFCOF', column_type='decimal(19,4)', nullable=False, chn_name='筹资活动现金流出特殊项目')
    """筹资活动现金流出特殊项目:"""

    SpeItemsFCOF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='SpeItemsFCOF', column_type='decimal(19,4)', nullable=False, chn_name='筹资活动现金流出特殊项目')
    """筹资活动现金流出特殊项目:"""

    AdjItemsFCOF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='AdjItemsFCOF', column_type='decimal(19,4)', nullable=False, chn_name='筹资活动现金流出调整项目')
    """筹资活动现金流出调整项目:"""

    AdjItemsFCOF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='AdjItemsFCOF', column_type='decimal(19,4)', nullable=False, chn_name='筹资活动现金流出调整项目')
    """筹资活动现金流出调整项目:"""

    SubFinCOflow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='SubFinCOflow', column_type='decimal(19,4)', nullable=False, chn_name='筹资活动现金流出小计')
    """筹资活动现金流出小计:若筹资活动现金流出小计为空，则以偿还债务支付的现金+分配股利、利润或偿付利息支付的现金+支付其他与筹资活动有关的现金+筹资活动现金流出特殊项目+筹资活动现金流出调整项目填充。"""

    SubFinCOflow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='SubFinCOflow', column_type='decimal(19,4)', nullable=False, chn_name='筹资活动现金流出小计')
    """筹资活动现金流出小计:若筹资活动现金流出小计为空，则以偿还债务支付的现金+分配股利、利润或偿付利息支付的现金+支付其他与筹资活动有关的现金+筹资活动现金流出特殊项目+筹资活动现金流出调整项目填充。"""

    AdjItemsNFCF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='AdjItemsNFCF', column_type='decimal(19,4)', nullable=False, chn_name='筹资活动流量现金净额调整项目')
    """筹资活动流量现金净额调整项目:"""

    AdjItemsNFCF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='AdjItemsNFCF', column_type='decimal(19,4)', nullable=False, chn_name='筹资活动流量现金净额调整项目')
    """筹资活动流量现金净额调整项目:"""

    NetFinCashFlow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetFinCashFlow', column_type='decimal(19,4)', nullable=False, chn_name='筹资活动产生的现金流量净额')
    """筹资活动产生的现金流量净额:若筹资活动产生的现金流量净额为空，则以筹资活动现金流入小计-筹资活动现金流出小计+筹资活动流量现金净额调整项目填充。"""

    NetFinCashFlow: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetFinCashFlow', column_type='decimal(19,4)', nullable=False, chn_name='筹资活动产生的现金流量净额')
    """筹资活动产生的现金流量净额:若筹资活动产生的现金流量净额为空，则以筹资活动现金流入小计-筹资活动现金流出小计+筹资活动流量现金净额调整项目填充。"""

    ExRateChgEffect: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='ExRateChgEffect', column_type='decimal(19,4)', nullable=False, chn_name='汇率变动对现金的影响')
    """汇率变动对现金的影响:"""

    ExRateChgEffect: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='ExRateChgEffect', column_type='decimal(19,4)', nullable=False, chn_name='汇率变动对现金的影响')
    """汇率变动对现金的影响:"""

    OthItemsEffCE: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='OthItemsEffCE', column_type='decimal(19,4)', nullable=False, chn_name='影响现金及现金等价物的其他科目')
    """影响现金及现金等价物的其他科目:"""

    OthItemsEffCE: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='OthItemsEffCE', column_type='decimal(19,4)', nullable=False, chn_name='影响现金及现金等价物的其他科目')
    """影响现金及现金等价物的其他科目:"""

    CompanyNature: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='CompanyNature', column_type='int', nullable=False, chn_name='公司性质')
    """公司性质:公司性质(CompanyNature)与(CT_SystemConst)表中的DM字段关联，令LB=1356，得到公司性质的具体描述：1-普通，2-金融，3-保险，4-房地产，5-银行。"""

    CompanyNature: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='CompanyNature', column_type='int', nullable=False, chn_name='公司性质')
    """公司性质:公司性质(CompanyNature)与(CT_SystemConst)表中的DM字段关联，令LB=1356，得到公司性质的具体描述：1-普通，2-金融，3-保险，4-房地产，5-银行。"""

    AdjItemsCE: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='AdjItemsCE', column_type='decimal(19,4)', nullable=False, chn_name='影响现金及现金等价物的调整项目')
    """影响现金及现金等价物的调整项目:"""

    AdjItemsCE: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='AdjItemsCE', column_type='decimal(19,4)', nullable=False, chn_name='影响现金及现金等价物的调整项目')
    """影响现金及现金等价物的调整项目:"""

    CEquInc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='CEquInc', column_type='decimal(19,4)', nullable=False, chn_name='现金及现金等价物净增加额')
    """现金及现金等价物净增加额:若现金及现金等价物净增加额为空，则以经营活动产生的现金流量净额+投资活动产生的现金流量净额+筹资活动产生的现金流量净额+汇率变动对现金的影响+影响现金及现金等价物的其他科目+影响现金及现金等价物的调整项目填充。"""

    CEquInc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='CEquInc', column_type='decimal(19,4)', nullable=False, chn_name='现金及现金等价物净增加额')
    """现金及现金等价物净增加额:若现金及现金等价物净增加额为空，则以经营活动产生的现金流量净额+投资活动产生的现金流量净额+筹资活动产生的现金流量净额+汇率变动对现金的影响+影响现金及现金等价物的其他科目+影响现金及现金等价物的调整项目填充。"""

    BeginPeriodCash: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='BeginPeriodCash', column_type='decimal(19,4)', nullable=False, chn_name='期初现金及现金等价物余额')
    """期初现金及现金等价物余额:"""

    BeginPeriodCash: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='BeginPeriodCash', column_type='decimal(19,4)', nullable=False, chn_name='期初现金及现金等价物余额')
    """期初现金及现金等价物余额:"""

    AdjItemsCEI: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='AdjItemsCEI', column_type='decimal(19,4)', nullable=False, chn_name='现金及现金等价物净增加额的调整项目')
    """现金及现金等价物净增加额的调整项目:"""

    AdjItemsCEI: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='AdjItemsCEI', column_type='decimal(19,4)', nullable=False, chn_name='现金及现金等价物净增加额的调整项目')
    """现金及现金等价物净增加额的调整项目:"""

    OtherItemEffCEI: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='OtherItemEffCEI', column_type='decimal(19,4)', nullable=False, chn_name='现金及现金等价物净增加额的特殊项目')
    """现金及现金等价物净增加额的特殊项目:"""

    OtherItemEffCEI: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='OtherItemEffCEI', column_type='decimal(19,4)', nullable=False, chn_name='现金及现金等价物净增加额的特殊项目')
    """现金及现金等价物净增加额的特殊项目:"""

    EndPerCEqu: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='EndPerCEqu', column_type='decimal(19,4)', nullable=False, chn_name='期末现金及现金等价物余额')
    """期末现金及现金等价物余额:若期末现金及现金等价物余额为空，则以现金及现金等价物净增加额+期初现金及现金等价物余额+现金及现金等价物净增加额的调整项目+现金及现金等价物净增加额的特殊项目填充。"""

    EndPerCEqu: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='EndPerCEqu', column_type='decimal(19,4)', nullable=False, chn_name='期末现金及现金等价物余额')
    """期末现金及现金等价物余额:若期末现金及现金等价物余额为空，则以现金及现金等价物净增加额+期初现金及现金等价物余额+现金及现金等价物净增加额的调整项目+现金及现金等价物净增加额的特殊项目填充。"""

    NetProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetProfit', column_type='decimal(19,4)', nullable=False, chn_name='净利润')
    """净利润:"""

    NetProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='NetProfit', column_type='decimal(19,4)', nullable=False, chn_name='净利润')
    """净利润:"""

    MinoProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='MinoProfit', column_type='decimal(19,4)', nullable=False, chn_name='加:少数股东损益')
    """加:少数股东损益:"""

    MinoProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='MinoProfit', column_type='decimal(19,4)', nullable=False, chn_name='加:少数股东损益')
    """加:少数股东损益:"""

    ADepreReserves: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='ADepreReserves', column_type='decimal(19,4)', nullable=False, chn_name='加:资产减值准备')
    """加:资产减值准备:"""

    ADepreReserves: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='ADepreReserves', column_type='decimal(19,4)', nullable=False, chn_name='加:资产减值准备')
    """加:资产减值准备:"""

    FAssetDep: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='FAssetDep', column_type='decimal(19,4)', nullable=False, chn_name='固定资产折旧、油气资产折耗、生产性生物资产折旧')
    """固定资产折旧、油气资产折耗、生产性生物资产折旧:"""

    FAssetDep: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='FAssetDep', column_type='decimal(19,4)', nullable=False, chn_name='固定资产折旧、油气资产折耗、生产性生物资产折旧')
    """固定资产折旧、油气资产折耗、生产性生物资产折旧:"""

    Mark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='Mark', column_type='int', nullable=True, chn_name='合并调整标志')
    """合并调整标志:合并调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB=1511，得到合并调整标志的具体描述：1-合并调整，2-合并未调整，3-母公司调整，4-母公司未调整，5-专项合并调整，6-专项合并未调整。"""

    Mark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='Mark', column_type='int', nullable=True, chn_name='合并调整标志')
    """合并调整标志:合并调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB=1511，得到合并调整标志的具体描述：1-合并调整，2-合并未调整，3-母公司调整，4-母公司未调整，5-专项合并调整，6-专项合并未调整。"""

    IntAAmort: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='IntAAmort', column_type='decimal(19,4)', nullable=False, chn_name='无形资产摊销')
    """无形资产摊销:"""

    IntAAmort: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='IntAAmort', column_type='decimal(19,4)', nullable=False, chn_name='无形资产摊销')
    """无形资产摊销:"""

    DefExpAmort: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='DefExpAmort', column_type='decimal(19,4)', nullable=False, chn_name='长期待摊费用摊销')
    """长期待摊费用摊销:"""

    DefExpAmort: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='DefExpAmort', column_type='decimal(19,4)', nullable=False, chn_name='长期待摊费用摊销')
    """长期待摊费用摊销:"""

    DefExpDecd: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='DefExpDecd', column_type='decimal(19,4)', nullable=False, chn_name='待摊费用减少(减:增加)')
    """待摊费用减少(减:增加):"""

    DefExpDecd: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='DefExpDecd', column_type='decimal(19,4)', nullable=False, chn_name='待摊费用减少(减:增加)')
    """待摊费用减少(减:增加):"""

    AccExpenseAdded: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='AccExpenseAdded', column_type='decimal(19,4)', nullable=False, chn_name='预提费用增加(减:减少)')
    """预提费用增加(减:减少):"""

    AccExpenseAdded: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='AccExpenseAdded', column_type='decimal(19,4)', nullable=False, chn_name='预提费用增加(减:减少)')
    """预提费用增加(减:减少):"""

    FixInOthADLoss: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='FixInOthADLoss', column_type='decimal(19,4)', nullable=False, chn_name='处置固定资产、无形资产和其他长期资产的损失')
    """处置固定资产、无形资产和其他长期资产的损失:"""

    FixInOthADLoss: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='FixInOthADLoss', column_type='decimal(19,4)', nullable=False, chn_name='处置固定资产、无形资产和其他长期资产的损失')
    """处置固定资产、无形资产和其他长期资产的损失:"""

    FixedAssetSLoss: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='FixedAssetSLoss', column_type='decimal(19,4)', nullable=False, chn_name='固定资产报废损失')
    """固定资产报废损失:"""

    FixedAssetSLoss: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='FixedAssetSLoss', column_type='decimal(19,4)', nullable=False, chn_name='固定资产报废损失')
    """固定资产报废损失:"""

    LFromFValueChg: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='LFromFValueChg', column_type='decimal(19,4)', nullable=False, chn_name='公允价值变动损失')
    """公允价值变动损失:"""

    LFromFValueChg: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='LFromFValueChg', column_type='decimal(19,4)', nullable=False, chn_name='公允价值变动损失')
    """公允价值变动损失:"""

    FinExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='FinExpense', column_type='decimal(19,4)', nullable=False, chn_name='财务费用')
    """财务费用:"""

    FinExpense: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='FinExpense', column_type='decimal(19,4)', nullable=False, chn_name='财务费用')
    """财务费用:"""

    InvestLoss: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='InvestLoss', column_type='decimal(19,4)', nullable=False, chn_name='投资损失')
    """投资损失:"""

    InvestLoss: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='InvestLoss', column_type='decimal(19,4)', nullable=False, chn_name='投资损失')
    """投资损失:"""

    DefTaxAssetDec: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='DefTaxAssetDec', column_type='decimal(19,4)', nullable=False, chn_name='递延所得税资产减少')
    """递延所得税资产减少:"""

    DefTaxAssetDec: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_CashFlowStatementCN', column_name='DefTaxAssetDec', column_type='decimal(19,4)', nullable=False, chn_name='递延所得税资产减少')
    """递延所得税资产减少:"""

