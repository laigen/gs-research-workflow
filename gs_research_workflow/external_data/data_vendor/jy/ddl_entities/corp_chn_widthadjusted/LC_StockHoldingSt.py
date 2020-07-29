# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_StockHoldingSt(SQLTableEntity):
    name: str = 'LC_StockHoldingSt'
    
    chn_name: str = '股东持股统计'
    
    business_unique: str = 'CompanyCode,EndDate'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.收录报告期末，各类机构投资者对每只股票的持仓情况，以及前十大（无限售条件）股东合计持股情况等。
2.机构持股统计中，基金持股综合考虑了上市公司披露的十大股东数据以及基金报告中披露的基金持股数据；机构持股合计包含上市公司披露的股东持股以及在同一截止时点上基金披露的所持股票数据。
3.计算公式：
1)机构持有无限售流通股数量＝机构持有无限售流通A股之和 
2)机构持有无限售流通股比例＝(机构持有无限售流通股数量/无限售A股)*100% 
3)机构持有A股数量＝机构持有A股之和 
4)机构持有A股比例＝(机构持有A股数量/A股总数)*100% 
5)机构持有股票数量＝机构持有股票之和 
6)机构持有股票比例＝(机构持有股票数量/总股本)*100%
4.数据范围：2001-03-31至今
5.信息来源：招股说明书、上市公告书、定报、临时公告等"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    QFIIHoldings: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='QFIIHoldings', column_type='decimal(18,2)', nullable=False, chn_name='QFII持有无限售流通A股数量(股)')
    """QFII持有无限售流通A股数量(股):"""

    InsuranceCorpsHoldings: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='InsuranceCorpsHoldings', column_type='decimal(18,2)', nullable=False, chn_name='保险公司持有无限售流通A股数量(股)')
    """保险公司持有无限售流通A股数量(股):"""

    SocialSecurityFundHold: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='SocialSecurityFundHold', column_type='decimal(18,2)', nullable=False, chn_name='社保基金持有无限售流通A股数量(股)')
    """社保基金持有无限售流通A股数量(股):"""

    EnterpriseAnnuitiesHold: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='EnterpriseAnnuitiesHold', column_type='decimal(18,2)', nullable=False, chn_name='企业年金持有无限售流通A股数量(股)')
    """企业年金持有无限售流通A股数量(股):"""

    TrustCompaniesHoldings: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='TrustCompaniesHoldings', column_type='decimal(18,2)', nullable=False, chn_name='信托公司持有无限售流通A股数量(股)')
    """信托公司持有无限售流通A股数量(股):"""

    FinanceCompaniesHoldings: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='FinanceCompaniesHoldings', column_type='decimal(18,2)', nullable=False, chn_name='财务公司持有无限售流通A股数量(股)')
    """财务公司持有无限售流通A股数量(股):"""

    OtherInstitutionHoldings: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='OtherInstitutionHoldings', column_type='decimal(18,2)', nullable=False, chn_name='其它机构持有无限售流通A股数量(股)')
    """其它机构持有无限售流通A股数量(股):"""

    InstitutionsHoldProp: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='InstitutionsHoldProp', column_type='decimal(18,4)', nullable=False, chn_name='机构持有无限售流通A股比例合计(%)')
    """机构持有无限售流通A股比例合计(%):"""

    FundsHoldProp: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='FundsHoldProp', column_type='decimal(18,4)', nullable=False, chn_name='基金持有无限售流通A股比例(%)')
    """基金持有无限售流通A股比例(%):"""

    SecuritiesCorpsHoldProp: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='SecuritiesCorpsHoldProp', column_type='decimal(18,4)', nullable=False, chn_name='券商持有无限售流通A股比例(%)')
    """券商持有无限售流通A股比例(%):"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='InnerCode', column_type='int', nullable=True, chn_name='证券内部编码')
    """证券内部编码:证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。"""

    FinancingProductsHoldProp: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='FinancingProductsHoldProp', column_type='decimal(18,4)', nullable=False, chn_name='券商理财产品持有无限售流通A股比例(%)')
    """券商理财产品持有无限售流通A股比例(%):"""

    QFIIHoldProp: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='QFIIHoldProp', column_type='decimal(18,4)', nullable=False, chn_name='QFII持有无限售流通A股比例(%)')
    """QFII持有无限售流通A股比例(%):"""

    InsuranceCorpsHoldProp: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='InsuranceCorpsHoldProp', column_type='decimal(18,4)', nullable=False, chn_name='保险公司持有无限售流通A股比例(%)')
    """保险公司持有无限售流通A股比例(%):"""

    SocialSecuFundHoldProp: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='SocialSecuFundHoldProp', column_type='decimal(18,4)', nullable=False, chn_name='社保基金持有无限售流通A股比例(%)')
    """社保基金持有无限售流通A股比例(%):"""

    CorpAnnuitiesHoldProp: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='CorpAnnuitiesHoldProp', column_type='decimal(18,4)', nullable=False, chn_name='企业年金持有无限售流通A股比例(%)')
    """企业年金持有无限售流通A股比例(%):"""

    TrustCompaniesHoldProp: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='TrustCompaniesHoldProp', column_type='decimal(18,4)', nullable=False, chn_name='信托公司持有无限售流通A股比例(%)')
    """信托公司持有无限售流通A股比例(%):"""

    FinanceCompaniesHoldProp: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='FinanceCompaniesHoldProp', column_type='decimal(18,4)', nullable=False, chn_name='财务公司持有无限售流通A股比例(%)')
    """财务公司持有无限售流通A股比例(%):"""

    OtherInstitutionHoldProp: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='OtherInstitutionHoldProp', column_type='decimal(18,4)', nullable=False, chn_name='其它机构持有无限售流通A股比例(%)')
    """其它机构持有无限售流通A股比例(%):"""

    InstitutionsHoldingsA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='InstitutionsHoldingsA', column_type='decimal(18,2)', nullable=False, chn_name='机构持有A股数量合计(股)')
    """机构持有A股数量合计(股):"""

    FundsHoldingsA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='FundsHoldingsA', column_type='decimal(18,2)', nullable=False, chn_name='基金持有A股数量(股)')
    """基金持有A股数量(股):"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。"""

    SecuritiesCorpsHoldingsA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='SecuritiesCorpsHoldingsA', column_type='decimal(18,2)', nullable=False, chn_name='券商持有A股数量(股)')
    """券商持有A股数量(股):"""

    FinanceProductsHoldingsA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='FinanceProductsHoldingsA', column_type='decimal(18,2)', nullable=False, chn_name='券商理财产品持有A股数量(股)')
    """券商理财产品持有A股数量(股):"""

    QFIIHoldingsA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='QFIIHoldingsA', column_type='decimal(18,2)', nullable=False, chn_name='QFII持有A股数量(股)')
    """QFII持有A股数量(股):"""

    InsuranceCorpsHoldingsA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='InsuranceCorpsHoldingsA', column_type='decimal(18,2)', nullable=False, chn_name='保险公司持有A股数量(股)')
    """保险公司持有A股数量(股):"""

    SocialSecurityFundHoldA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='SocialSecurityFundHoldA', column_type='decimal(18,2)', nullable=False, chn_name='社保基金持有A股数量(股)')
    """社保基金持有A股数量(股):"""

    EnterpriseAnnuitiesHoldA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='EnterpriseAnnuitiesHoldA', column_type='decimal(18,2)', nullable=False, chn_name='企业年金持有A股数量(股)')
    """企业年金持有A股数量(股):"""

    TrustCompaniesHoldingsA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='TrustCompaniesHoldingsA', column_type='decimal(18,2)', nullable=False, chn_name='信托公司持有A股数量(股)')
    """信托公司持有A股数量(股):"""

    FinanceCompHoldingsA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='FinanceCompHoldingsA', column_type='decimal(18,2)', nullable=False, chn_name='财务公司持有A股数量(股)')
    """财务公司持有A股数量(股):"""

    OtherInstiHoldingsA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='OtherInstiHoldingsA', column_type='decimal(18,2)', nullable=False, chn_name='其它机构持有A股数量(股)')
    """其它机构持有A股数量(股):"""

    InstitutionsHoldPropA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='InstitutionsHoldPropA', column_type='decimal(18,4)', nullable=False, chn_name='机构持有A股比例合计(%)')
    """机构持有A股比例合计(%):"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    FundsHoldPropA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='FundsHoldPropA', column_type='decimal(18,4)', nullable=False, chn_name='基金持有A股比例(%)')
    """基金持有A股比例(%):"""

    SecuritiesCorpsHoldPropA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='SecuritiesCorpsHoldPropA', column_type='decimal(18,4)', nullable=False, chn_name='券商持有A股比例(%)')
    """券商持有A股比例(%):"""

    FinanceProductsHoldPropA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='FinanceProductsHoldPropA', column_type='decimal(18,4)', nullable=False, chn_name='券商理财产品持有A股比例(%)')
    """券商理财产品持有A股比例(%):"""

    QFIIHoldPropA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='QFIIHoldPropA', column_type='decimal(18,4)', nullable=False, chn_name='QFII持有A股比例(%)')
    """QFII持有A股比例(%):"""

    InsuranceCorpsHoldPropA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='InsuranceCorpsHoldPropA', column_type='decimal(18,4)', nullable=False, chn_name='保险公司持有A股比例(%)')
    """保险公司持有A股比例(%):"""

    SocialSecuFundHoldPropA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='SocialSecuFundHoldPropA', column_type='decimal(18,4)', nullable=False, chn_name='社保基金持有A股比例(%)')
    """社保基金持有A股比例(%):"""

    CorpAnnuitiesHoldPropA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='CorpAnnuitiesHoldPropA', column_type='decimal(18,4)', nullable=False, chn_name='企业年金持有A股比例(%)')
    """企业年金持有A股比例(%):"""

    TrustCompaniesHoldPropA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='TrustCompaniesHoldPropA', column_type='decimal(18,4)', nullable=False, chn_name='信托公司持有A股比例(%)')
    """信托公司持有A股比例(%):"""

    FinanceCompHoldPropA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='FinanceCompHoldPropA', column_type='decimal(18,4)', nullable=False, chn_name='财务公司持有A股比例(%)')
    """财务公司持有A股比例(%):"""

    OtherInstiHoldPropA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='OtherInstiHoldPropA', column_type='decimal(18,4)', nullable=False, chn_name='其它机构持有A股比例(%)')
    """其它机构持有A股比例(%):"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='InfoSource', column_type='varchar(50)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    InstitutionsHoldingsT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='InstitutionsHoldingsT', column_type='decimal(18,2)', nullable=False, chn_name='机构持股数量合计(股)')
    """机构持股数量合计(股):"""

    FundsHoldingsT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='FundsHoldingsT', column_type='decimal(18,2)', nullable=False, chn_name='基金持股数量(股)')
    """基金持股数量(股):"""

    SecuritiesCorpsHoldingsT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='SecuritiesCorpsHoldingsT', column_type='decimal(18,2)', nullable=False, chn_name='券商持股数量(股)')
    """券商持股数量(股):"""

    FinanceProductsHoldingsT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='FinanceProductsHoldingsT', column_type='decimal(18,2)', nullable=False, chn_name='券商理财产品持股数量(股)')
    """券商理财产品持股数量(股):"""

    QFIIHoldingsT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='QFIIHoldingsT', column_type='decimal(18,2)', nullable=False, chn_name='QFII持股数量(股)')
    """QFII持股数量(股):"""

    InsuranceCorpsHoldingsT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='InsuranceCorpsHoldingsT', column_type='decimal(18,2)', nullable=False, chn_name='保险公司持股数量(股)')
    """保险公司持股数量(股):"""

    SocialSecurityFundHoldT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='SocialSecurityFundHoldT', column_type='decimal(18,2)', nullable=False, chn_name='社保基金持股数量(股)')
    """社保基金持股数量(股):"""

    EnterpriseAnnuitiesHoldT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='EnterpriseAnnuitiesHoldT', column_type='decimal(18,2)', nullable=False, chn_name='企业年金持股数量(股)')
    """企业年金持股数量(股):"""

    TrustCompaniesHoldingsT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='TrustCompaniesHoldingsT', column_type='decimal(18,2)', nullable=False, chn_name='信托公司持股数量(股)')
    """信托公司持股数量(股):"""

    FinanceCompHoldingsT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='FinanceCompHoldingsT', column_type='decimal(18,2)', nullable=False, chn_name='财务公司持股数量(股)')
    """财务公司持股数量(股):"""

    InstitutionsHoldings: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='InstitutionsHoldings', column_type='decimal(18,2)', nullable=False, chn_name='机构持有无限售流通A股数量合计(股)')
    """机构持有无限售流通A股数量合计(股):"""

    OtherInstiHoldingsT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='OtherInstiHoldingsT', column_type='decimal(18,2)', nullable=False, chn_name='其它机构持股数量(股)')
    """其它机构持股数量(股):"""

    InstitutionsHoldPropT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='InstitutionsHoldPropT', column_type='decimal(18,4)', nullable=False, chn_name='机构持股比例合计(%)')
    """机构持股比例合计(%):"""

    FundsHoldPropT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='FundsHoldPropT', column_type='decimal(18,4)', nullable=False, chn_name='基金持股比例(%)')
    """基金持股比例(%):"""

    SecuritiesCorpsHoldPropT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='SecuritiesCorpsHoldPropT', column_type='decimal(18,4)', nullable=False, chn_name='券商持股比例(%)')
    """券商持股比例(%):"""

    FinanceProductsHoldPropT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='FinanceProductsHoldPropT', column_type='decimal(18,4)', nullable=False, chn_name='券商理财产品持股比例(%)')
    """券商理财产品持股比例(%):"""

    QFIIHoldPropT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='QFIIHoldPropT', column_type='decimal(18,4)', nullable=False, chn_name='QFII持股比例(%)')
    """QFII持股比例(%):"""

    InsuranceCorpsHoldPropT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='InsuranceCorpsHoldPropT', column_type='decimal(18,4)', nullable=False, chn_name='保险公司持股比例(%)')
    """保险公司持股比例(%):"""

    SocialSecuFundHoldPropT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='SocialSecuFundHoldPropT', column_type='decimal(18,4)', nullable=False, chn_name='社保基金持股比例(%)')
    """社保基金持股比例(%):"""

    CorpAnnuitiesHoldPropT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='CorpAnnuitiesHoldPropT', column_type='decimal(18,4)', nullable=False, chn_name='企业年金持股比例(%)')
    """企业年金持股比例(%):"""

    TrustCompaniesHoldPropT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='TrustCompaniesHoldPropT', column_type='decimal(18,4)', nullable=False, chn_name='信托公司持股比例(%)')
    """信托公司持股比例(%):"""

    FundsHoldings: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='FundsHoldings', column_type='decimal(18,2)', nullable=False, chn_name='基金持有无限售流通A股数量(股)')
    """基金持有无限售流通A股数量(股):由于基金披露的持股数中，没有明确给出无限售部分是多少，故该“基金持有无限售流通A股数量”及“基金持有无限售流通A股比例”的值暂时不计算，为空值"""

    FinanceCompHoldPropT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='FinanceCompHoldPropT', column_type='decimal(18,4)', nullable=False, chn_name='财务公司持股比例(%)')
    """财务公司持股比例(%):"""

    OtherInstiHoldPropT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='OtherInstiHoldPropT', column_type='decimal(18,4)', nullable=False, chn_name='其它机构持股比例(%)')
    """其它机构持股比例(%):"""

    Top10StockholdersAmount: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='Top10StockholdersAmount', column_type='decimal(18,2)', nullable=False, chn_name='前十大股东持股数量合计(股)')
    """前十大股东持股数量合计(股):"""

    Top10StockholdersProp: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='Top10StockholdersProp', column_type='decimal(18,4)', nullable=False, chn_name='前十大股东持股比例合计(%)')
    """前十大股东持股比例合计(%):"""

    Top10NRStockholdersAmount: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='Top10NRStockholdersAmount', column_type='decimal(18,2)', nullable=False, chn_name='前十大无限售股东持股数量合计(股)')
    """前十大无限售股东持股数量合计(股):"""

    Top10NRHoldersAmountToNRS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='Top10NRHoldersAmountToNRS', column_type='decimal(18,4)', nullable=False, chn_name='前十大无限售股东持股数占无限售股本比例(%)')
    """前十大无限售股东持股数占无限售股本比例(%):"""

    Top10NRHoldersAmountToTS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='Top10NRHoldersAmountToTS', column_type='decimal(18,4)', nullable=False, chn_name='前十大无限售股东持股数占总股本的比例(%)')
    """前十大无限售股东持股数占总股本的比例(%):"""

    NRAFromTop10NRHolders: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='NRAFromTop10NRHolders', column_type='decimal(18,2)', nullable=False, chn_name='前十大无限售股东持有无限售A股数量合计(股)')
    """前十大无限售股东持有无限售A股数量合计(股):"""

    NRAFromTop10ToNRA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='NRAFromTop10ToNRA', column_type='decimal(18,4)', nullable=False, chn_name='前十大无限售股东持有无限售A股数占无限售A股比例(%)')
    """前十大无限售股东持有无限售A股数占无限售A股比例(%):"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    SecuritiesCorpsHoldings: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='SecuritiesCorpsHoldings', column_type='decimal(18,2)', nullable=False, chn_name='券商持有无限售流通A股数量(股)')
    """券商持有无限售流通A股数量(股):"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    FinancingProductsHoldings: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_StockHoldingSt', column_name='FinancingProductsHoldings', column_type='decimal(18,2)', nullable=False, chn_name='券商理财产品持有无限售流通A股数量(股)')
    """券商理财产品持有无限售流通A股数量(股):"""

