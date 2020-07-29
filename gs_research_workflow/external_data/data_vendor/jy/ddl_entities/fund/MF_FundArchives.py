# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_FundArchives(SQLTableEntity):
    name: str = 'MF_FundArchives'
    
    chn_name: str = '公募基金概况'
    
    business_unique: str = 'InnerCode'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.本表记录了基金基本情况，包括基金规模、成立日期、投资类型、管理人、托管人、存续期、历史简介等。
2.历史数据：1998年3月起-至今。
3.信息来源：基金公司官网披露的产品说明书。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    Type: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='Type', column_type='int', nullable=False, chn_name='基金运作方式')
    """基金运作方式:基金运作方式(Type)与(CT_SystemConst)表中的DM字段关联，令LB = 1210，得到基金运作方式的具体描述：1-契约型封闭式，2-开放式，3-LOF，4-ETF，6-创新型封闭式，7-开放式(带固定封闭期)，8-ETF联接基金，9-半开放式。"""

    FundNature: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='FundNature', column_type='int', nullable=False, chn_name='基金性质')
    """基金性质:基金性质(FundNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1485，得到基金性质的具体描述：1-常规基金，2-QDII基金，3-互认基金。"""

    InvestmentType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='InvestmentType', column_type='int', nullable=False, chn_name='基金投资类型')
    """基金投资类型:基金投资类型(InvestmentType)与(CT_SystemConst)表中的DM字段关联，令LB = 1094，得到基金投资类型的具体描述：1-成长型—积极成长型，2-成长型—稳健成长型，3-成长型—中小企业成长型，4-平衡型，5-资产重组型，6-科技型，7-指数型，8-优化指数型，9-价值型，10-债券型，11-收益型，15-现金型，20-内需增长..."""

    InvestStyle: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='InvestStyle', column_type='int', nullable=False, chn_name='基金投资风格')
    """基金投资风格:基金投资风格(InvestStyle)与(CT_SystemConst)表中的DM字段关联，令LB = 1093，得到基金投资风格的具体描述：1-股票型，2-指数型，3-配置型，4-现金型，5-激进债券型，6-债券型，7-普通债券型，8-短期债券型，9-保本型，10-激进配置型，11-保守混合型，12-偏股型，13-偏债型，14-中短债型，15-特殊策略型，..."""

    FundType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='FundType', column_type='varchar(100)', nullable=False, chn_name='基金类别')
    """基金类别:"""

    FundTypeCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='FundTypeCode', column_type='int', nullable=True, chn_name='基金类别代码')
    """基金类别代码:基金类别代码(FundTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB=1249，得到基金类别代码的具体描述：1101-股票型，1103-混合型，1105-债券型，1107-保本型，1109-货币型，1199-其他型。"""

    RegInstCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='RegInstCode', column_type='int', nullable=False, chn_name='注册登记机构')
    """注册登记机构:注册登记机构（RegInstCode）：与“机构基本资料（LC_InstiArchive）”中“企业编号（CompanyCode）”关联，得到注册登记机构基本信息。"""

    InvestOrientation: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='InvestOrientation', column_type='varchar(1000)', nullable=False, chn_name='基金投资方向')
    """基金投资方向:"""

    InvestTarget: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='InvestTarget', column_type='varchar(1000)', nullable=False, chn_name='基金投资目标')
    """基金投资目标:"""

    InvestField: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='InvestField', column_type='varchar(2000)', nullable=False, chn_name='基金投资范围')
    """基金投资范围:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='InnerCode', column_type='int', nullable=True, chn_name='基金内部编码')
    """基金内部编码:基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    PerformanceBenchMark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='PerformanceBenchMark', column_type='varchar(500)', nullable=False, chn_name='业绩比较基准')
    """业绩比较基准:"""

    RiskReturncharacter: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='RiskReturncharacter', column_type='varchar(500)', nullable=False, chn_name='风险收益特征')
    """风险收益特征:"""

    ProfitDistributionRule: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='ProfitDistributionRule', column_type='varchar(1000)', nullable=False, chn_name='收益分配原则')
    """收益分配原则:"""

    ExProfitDistri: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='ExProfitDistri', column_type='int', nullable=False, chn_name='场内收益分配方式')
    """场内收益分配方式:场内收益分配方式(ExProfitDistri)与(CT_SystemConst)表中的DM字段关联，令LB=1989，得到场内收益分配方式的具体描述：1-现金分红，2-红利再投资，3-现金分红或红利再投资，4-不分配。"""

    OTCProfitDistri: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='OTCProfitDistri', column_type='int', nullable=False, chn_name='场外收益分配方式')
    """场外收益分配方式:场外收益分配方式(OTCProfitDistri)与(CT_SystemConst)表中的DM字段关联，令LB=1989，得到场外收益分配方式的具体描述：1-现金分红，2-红利再投资，3-现金分红或红利再投资，4-不分配。"""

    BriefIntro: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='BriefIntro', column_type='text', nullable=False, chn_name='基金简介')
    """基金简介:"""

    FloatType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='FloatType', column_type='int', nullable=False, chn_name='发售方式')
    """发售方式:发售方式(FloatType)与(CT_SystemConst)表中的DM字段关联，令LB=1652，得到发售方式的具体描述：1-场内，2-场外，3-场内和场外。"""

    FoundedSize: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='FoundedSize', column_type='decimal(18,2)', nullable=False, chn_name='基金设立规模(份)')
    """基金设立规模(份):"""

    EstablishmentDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='EstablishmentDate', column_type='datetime', nullable=False, chn_name='设立日期')
    """设立日期:"""

    ListedDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='ListedDate', column_type='datetime', nullable=False, chn_name='上市日期')
    """上市日期:"""

    ApplyingCodeFront: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='ApplyingCodeFront', column_type='varchar(10)', nullable=False, chn_name='前端申购代码')
    """前端申购代码:"""

    Duration: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='Duration', column_type='decimal(18,2)', nullable=False, chn_name='存续年限(年)')
    """存续年限(年):"""

    StartDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='StartDate', column_type='datetime', nullable=False, chn_name='存续期起始日')
    """存续期起始日:"""

    ExpireDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='ExpireDate', column_type='datetime', nullable=False, chn_name='存续期截止日')
    """存续期截止日:"""

    StClearingDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='StClearingDate', column_type='datetime', nullable=False, chn_name='清算起始日')
    """清算起始日:"""

    EnClearingDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='EnClearingDate', column_type='datetime', nullable=False, chn_name='清算截止日')
    """清算截止日:"""

    GuaranteedPeriod: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='GuaranteedPeriod', column_type='decimal(18,2)', nullable=False, chn_name='保本型基金保本期(月)')
    """保本型基金保本期(月):"""

    CarryOverDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='CarryOverDate', column_type='int', nullable=False, chn_name='货币基金结转日')
    """货币基金结转日:货币基金结转日(CarryOverDate)与(CT_SystemConst)表中的DM字段关联，令LB=1250，得到货币基金结转日的具体描述：1-每月1日，2-每月2日，3-每月3日，4-每月4日，5-每月5日，6-每月6日，7-每月7日，8-每月8日，9-每月9日，10-每月10日，11-每月11日，12-每月12日，13-每月13日，14-每月14日..."""

    CarryOverDateRemark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='CarryOverDateRemark', column_type='varchar(100)', nullable=False, chn_name='货币基金结转日说明')
    """货币基金结转日说明:"""

    CarryOverType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='CarryOverType', column_type='int', nullable=False, chn_name='货币基金收益分配方式(份额结转方式)')
    """货币基金收益分配方式(份额结转方式):货币基金收益分配方式(份额结转方式)(CarryOverType)与(CT_SystemConst)表中的DM字段关联，令LB=1273，得到货币基金收益分配方式(份额结转方式)的具体描述：1-按日结转，30-按月结转，99-按期结转。"""

    ClassificationFundType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='ClassificationFundType', column_type='int', nullable=False, chn_name='分级基金类别')
    """分级基金类别:"""

    ApplyingCodeBack: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='ApplyingCodeBack', column_type='varchar(10)', nullable=False, chn_name='后端申购代码')
    """后端申购代码:"""

    AgrBenchmkRateOfShareA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='AgrBenchmkRateOfShareA', column_type='varchar(200)', nullable=False, chn_name='A份额约定年基准收益率表达式')
    """A份额约定年基准收益率表达式:A份额约定年基准收益率表达式（AgrBenchmkRateOfShareA）：本表该字段已停止维护，此信息在分级基金主表（MF_GradedFund）中“A份额约定年基准收益表达式（AnnualEarningExp）”字段维护。"""

    AgrBenchmkRateOfShareANotes: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='AgrBenchmkRateOfShareANotes', column_type='varchar(1000)', nullable=False, chn_name='A份额约定年基准收益率表达式备注')
    """A份额约定年基准收益率表达式备注:A份额约定年基准收益率表达式备注（AgrBenchmkRateOfShareANotes）：本表该字段已停止维护，此信息在分级基金主表（MF_GradedFund）中“A份额约定年基准收益表达式备注（AnnualEarningRemark）”字段维护。"""

    ShareProperties: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='ShareProperties', column_type='int', nullable=False, chn_name='份额属性')
    """份额属性:份额属性(ShareProperties)与(CT_SystemConst)表中的DM字段关联，令LB=1651，得到份额属性的具体描述：1-稳健型，2-进取型。"""

    RegularShareConversionNotes: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='RegularShareConversionNotes', column_type='varchar(1000)', nullable=False, chn_name='定期份额折算说明')
    """定期份额折算说明:定期份额折算说明（RegularShareConversionNotes）：本表该字段已停止维护，此信息在分级基金主表（MF_GradedFund）中“定期份额折算说明（RegularShareCon）”字段维护。"""

    NonRegularShareConversionNotes: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='NonRegularShareConversionNotes', column_type='varchar(1000)', nullable=False, chn_name='不定期份额折算说明')
    """不定期份额折算说明:不定期份额折算说明（NonRegularShareConversionNotes）：本表该字段已停止维护，此信息在分级基金主表（MF_GradedFund）中“不定份额折算说明（TrampShareCon）”字段维护。"""

    Manager: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='Manager', column_type='varchar(50)', nullable=False, chn_name='基金经理')
    """基金经理:"""

    InvestAdvisorCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='InvestAdvisorCode', column_type='int', nullable=False, chn_name='基金管理人')
    """基金管理人:基金管理人代码（InvestAdvisorCode）：与“基金管理人概况表（MF_InvestAdvisorOutline）”中的“基金管理人名称编号（InvestAdvisorCode）”关联，得到基金管理人的具体名称。"""

    TrusteeCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='TrusteeCode', column_type='int', nullable=False, chn_name='基金托管人')
    """基金托管人:基金托管人代码（TrusteeCode）：与“基金托管人概况表（MF_TrusteeOutline）”中的“基金托管人名称编号（TrusteeCode）”关联，得到基金托管人的具体名称。"""

    Warrantor: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='Warrantor', column_type='varchar(250)', nullable=False, chn_name='保本担保机构')
    """保本担保机构:"""

    LowestSumSubscribing: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='LowestSumSubscribing', column_type='varchar(500)', nullable=False, chn_name='最低认购申购金额描述')
    """最低认购申购金额描述:"""

    SecurityCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='SecurityCode', column_type='varchar(10)', nullable=False, chn_name='基金交易代码(交易所交易代码)')
    """基金交易代码(交易所交易代码):"""

    LowestSumSubLL: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='LowestSumSubLL', column_type='decimal(19,4)', nullable=False, chn_name='最低认购金额下限(元)')
    """最低认购金额下限(元):最低认购金额下限（元）（LowestSumSubLL）：取值为不同认购平台最低认购金额的最小值。"""

    LowestSumPurLL: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='LowestSumPurLL', column_type='decimal(19,4)', nullable=False, chn_name='最低申购金额下限(元)')
    """最低申购金额下限(元):最低申购金额下限（元）（LowestSumPurLL）：取值为不同申购平台最低申购金额的最小值。"""

    LowestSumRedemption: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='LowestSumRedemption', column_type='decimal(16,6)', nullable=False, chn_name='最低赎回份额(份)')
    """最低赎回份额(份):"""

    LSFRDescription: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='LSFRDescription', column_type='varchar(200)', nullable=False, chn_name='最低赎回份额描述')
    """最低赎回份额描述:"""

    LowestSumForHolding: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='LowestSumForHolding', column_type='decimal(16,6)', nullable=False, chn_name='最低持有份额(份)')
    """最低持有份额(份):"""

    LSFHDescription: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='LSFHDescription', column_type='varchar(200)', nullable=False, chn_name='最低持有份额描述')
    """最低持有份额描述:"""

    DeliveryDays: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='DeliveryDays', column_type='int', nullable=False, chn_name='赎回款到账天数')
    """赎回款到账天数:"""

    RiskReturnCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='RiskReturnCode', column_type='int', nullable=False, chn_name='风险收益特征代码')
    """风险收益特征代码:风险收益特征代码(RiskReturnCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1651，得到风险收益特征代码的具体描述：1-稳健型，2-进取型。"""

    CustodyMarket: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='CustodyMarket', column_type='int', nullable=False, chn_name='转托管市场')
    """转托管市场:转托管市场(CustodyMarket)与(CT_SystemConst)表中的DM字段关联，令LB=201 AND DM IN (83，90)，得到转托管市场的具体描述："""

    OperationPeriod: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='OperationPeriod', column_type='decimal(9,2)', nullable=False, chn_name='运作期')
    """运作期:"""

    MainCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='MainCode', column_type='varchar(10)', nullable=False, chn_name='基金主代码')
    """基金主代码:基金主代码（MainCode）：与“证券主表（SecuMain）”中的“证券代码（SecuCode）”关联，得到基金的交易简称等信息。该字段记录基金季报中公布的基金主代码信息，当基金为非分级基金或分级基金主代码时，该字段与基金交易代码（交易所交易代码）（SecurityCode）一致。"""

    OperationPDUnitCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='OperationPDUnitCode', column_type='int', nullable=False, chn_name='运作期单位代码')
    """运作期单位代码:"""

    OperationPDUnitName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='OperationPDUnitName', column_type='varchar(20)', nullable=False, chn_name='运作期单位名称')
    """运作期单位名称:"""

    IfInitiatingFund: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='IfInitiatingFund', column_type='int', nullable=False, chn_name='是否发起式基金')
    """是否发起式基金:是否发起式基金（IfInitiatingFund），该字段固定以下常量：1-否；2-是"""

    IfPensionTarget: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='IfPensionTarget', column_type='int', nullable=False, chn_name='是否养老目标基金')
    """是否养老目标基金:是否养老目标基金(IfPensionTarget)该字段固定以下常量：1-是；   2-否"""

    IfFOF: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='IfFOF', column_type='int', nullable=False, chn_name='是否FOF')
    """是否FOF:是否FOF（IfFOF），该字段固定以下常量：1-是；   2-否"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新日期')
    """更新日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    ExApplyingMarket: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='ExApplyingMarket', column_type='int', nullable=False, chn_name='场内申购赎回场所')
    """场内申购赎回场所:场内申购赎回场所(ExApplyingMarket)：与“系统常量表（CT_SystemConst）”中“代码（DM）”关联，令“LB=201”，得到证券市场具体描述：71-柜台交易市场，81-三板市场，83-上海证券交易所，84-其他市场，89-银行间债券市场，90-深圳证券交易所"""

    ExApplyingCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='ExApplyingCode', column_type='varchar(10)', nullable=False, chn_name='场内申购赎回代码')
    """场内申购赎回代码:"""

    ExApplyingAbbr: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchives', column_name='ExApplyingAbbr', column_type='varchar(100)', nullable=False, chn_name='场内申购赎回简称')
    """场内申购赎回简称:"""

