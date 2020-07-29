# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_Merger(SQLTableEntity):
    name: str = 'LC_Merger'
    
    chn_name: str = '重大事项吸收合并'
    
    business_unique: str = 'CompanyCode,InitialInfoPublDate,MergedParty'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.收录上市公司公告中披露的公司吸收合并其他公司的事项，包括吸收合并日期进程、被合并公司代码及名称、主营、吸收合并股数、换股明细、被合并公司最新财务状况等指标。
2.数据范围：2006-至今
3.信息来源：上市公司公告"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    FoundedDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='FoundedDate', column_type='datetime', nullable=False, chn_name='成立日期')
    """成立日期:"""

    RegiCapital: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='RegiCapital', column_type='decimal(19,4)', nullable=False, chn_name='注册资本(元)')
    """注册资本(元):"""

    MainBusinesses: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='MainBusinesses', column_type='varchar(200)', nullable=False, chn_name='主营业务')
    """主营业务:"""

    Industry: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='Industry', column_type='int', nullable=False, chn_name='所属行业')
    """所属行业:"""

    MergeBaseDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='MergeBaseDate', column_type='datetime', nullable=False, chn_name='合并基准日')
    """合并基准日:"""

    AgreementDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='AgreementDate', column_type='datetime', nullable=False, chn_name='合并协议签署日')
    """合并协议签署日:"""

    ExchangeRateNumerator: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='ExchangeRateNumerator', column_type='float', nullable=False, chn_name='折股比例分子')
    """折股比例分子:"""

    ExchangeRateDenominator: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='ExchangeRateDenominator', column_type='float', nullable=False, chn_name='折股比例分母')
    """折股比例分母:"""

    ContraShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='ContraShares', column_type='decimal(18,2)', nullable=False, chn_name='合并抵消股份')
    """合并抵消股份:"""

    IssueShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='IssueShares', column_type='decimal(18,2)', nullable=False, chn_name='发行股数')
    """发行股数:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。"""

    StateSharesAdded: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='StateSharesAdded', column_type='decimal(18,2)', nullable=False, chn_name='其中：合并增加国家股(万股)')
    """其中：合并增加国家股(万股):"""

    LegalPersonSharesAdded: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='LegalPersonSharesAdded', column_type='decimal(18,2)', nullable=False, chn_name='其中：合并增加法人股(万股)')
    """其中：合并增加法人股(万股):"""

    IndividualSharesAdded: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='IndividualSharesAdded', column_type='decimal(18,2)', nullable=False, chn_name='其中：合并增加个人股(万股)')
    """其中：合并增加个人股(万股):"""

    ISharesAddedHoldingPeriod: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='ISharesAddedHoldingPeriod', column_type='decimal(19,8)', nullable=False, chn_name='合并增加个人股持股年限(年)')
    """合并增加个人股持股年限(年):"""

    ShareExchangeBeginDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='ShareExchangeBeginDate', column_type='datetime', nullable=False, chn_name='换股起始日')
    """换股起始日:"""

    ShareExchangeEndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='ShareExchangeEndDate', column_type='datetime', nullable=False, chn_name='换股截止日')
    """换股截止日:"""

    ExchangeRightRegDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='ExchangeRightRegDate', column_type='datetime', nullable=False, chn_name='换股实施股权登记日')
    """换股实施股权登记日:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='EndDate', column_type='datetime', nullable=False, chn_name='截至日期')
    """截至日期:"""

    TotalAsset: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='TotalAsset', column_type='decimal(19,4)', nullable=False, chn_name='资产总额(元)')
    """资产总额(元):"""

    ShareholderEquity: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='ShareholderEquity', column_type='decimal(19,4)', nullable=False, chn_name='股东权益(元)')
    """股东权益(元):"""

    InitialInfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='InitialInfoPublDate', column_type='datetime', nullable=True, chn_name='首次信息发布日期')
    """首次信息发布日期:"""

    MainBusinessIncome: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='MainBusinessIncome', column_type='decimal(19,4)', nullable=False, chn_name='主营业务收入(元)')
    """主营业务收入(元):"""

    NetProfit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='NetProfit', column_type='decimal(19,4)', nullable=False, chn_name='净利润(元)')
    """净利润(元):"""

    ShareChangePublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='ShareChangePublDate', column_type='datetime', nullable=False, chn_name='股份变动公告日')
    """股份变动公告日:"""

    ShareCapitalBeforeMerge: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='ShareCapitalBeforeMerge', column_type='decimal(18,2)', nullable=False, chn_name='合并前上市公司总股本(万股)')
    """合并前上市公司总股本(万股):"""

    ShareListDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='ShareListDate', column_type='datetime', nullable=False, chn_name='新增股份上市日')
    """新增股份上市日:"""

    ShareCustodyDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='ShareCustodyDate', column_type='datetime', nullable=False, chn_name='股份托管确认日/股份托管日')
    """股份托管确认日/股份托管日:"""

    ICChangeRegiDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='ICChangeRegiDate', column_type='datetime', nullable=False, chn_name='工商变更登记日')
    """工商变更登记日:"""

    ChangeStatement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='ChangeStatement', column_type='varchar(255)', nullable=False, chn_name='方案变动说明')
    """方案变动说明:"""

    ChangeType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='ChangeType', column_type='int', nullable=False, chn_name='方案变动类型')
    """方案变动类型:方案变动类型(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1194，得到方案变动类型的具体描述：1-否，2-是，3-放弃或股东大会否决，4-可转债改增发，5-可转债改配股，6-增发改配股，7-增发改可转债，8-配股改可转债，9-配股改增发，10-未核准，11-更改发行规模，12-延长有效期，13-其他，14-回拨后..."""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='修改日期')
    """修改日期:"""

    PreSchemePublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='PreSchemePublDate', column_type='datetime', nullable=False, chn_name='吸收合并预案说明发布日')
    """吸收合并预案说明发布日:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    SMDeciPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='SMDeciPublDate', column_type='datetime', nullable=False, chn_name='股东大会决议公告日期')
    """股东大会决议公告日期:"""

    AnouncementPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='AnouncementPublDate', column_type='datetime', nullable=False, chn_name='吸收合并公告书发布日')
    """吸收合并公告书发布日:"""

    MergedCompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='MergedCompanyCode', column_type='int', nullable=False, chn_name='被合并公司代码')
    """被合并公司代码:被合并公司代码（MergedCompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到被合并公司的名称等基本信息。"""

    MergedInnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='MergedInnerCode', column_type='int', nullable=False, chn_name='所属股票内部编码')
    """所属股票内部编码:所属股票内部编码（MergedInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到所属股票的交易代码、简称等。"""

    MergedParty: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Merger', column_name='MergedParty', column_type='varchar(50)', nullable=True, chn_name='被合并公司名称')
    """被合并公司名称:"""

