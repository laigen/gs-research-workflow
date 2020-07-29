# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_BShareIPO(SQLTableEntity):
    name: str = 'LC_BShareIPO'
    
    chn_name: str = 'B股首次发行与上市'
    
    business_unique: str = 'InnerCode'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.收录B股首次发行上市的明细情况，包括发行概况、配售日期、承配缴款日、承销日期、发行结果等内容。
2.数据范围：1991-10-31至今
3.信息来源：招股意向书、招股说明书、上市公告书等"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    PriceUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='PriceUnit', column_type='int', nullable=False, chn_name='计价单位')
    """计价单位:计价单位(PriceUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068，得到计价单位的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，1170-约旦第纳尔，1180-科威特第..."""

    IssuePriceRMB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='IssuePriceRMB', column_type='decimal(19,4)', nullable=False, chn_name='每股发行价(人民币元)')
    """每股发行价(人民币元):"""

    IssuePriceFC: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='IssuePriceFC', column_type='decimal(19,4)', nullable=False, chn_name='每股发行价(外币元)')
    """每股发行价(外币元):"""

    WeightedPERatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='WeightedPERatio', column_type='real', nullable=False, chn_name='加权平均发行市盈率(倍)')
    """加权平均发行市盈率(倍):"""

    DilutedPERatio: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='DilutedPERatio', column_type='real', nullable=False, chn_name='全面摊薄发行市盈率(倍)')
    """全面摊薄发行市盈率(倍):"""

    StraInvestorPlaPriceFC: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='StraInvestorPlaPriceFC', column_type='decimal(19,4)', nullable=False, chn_name='战略投资者配售价(外币元)')
    """战略投资者配售价(外币元):"""

    IssueVolPlanned: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='IssueVolPlanned', column_type='decimal(16,0)', nullable=False, chn_name='计划发行量(股)')
    """计划发行量(股):"""

    OverAllotmentOption: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='OverAllotmentOption', column_type='decimal(16,0)', nullable=False, chn_name='超额配售权(股)')
    """超额配售权(股):"""

    IssueMethod: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='IssueMethod', column_type='int', nullable=False, chn_name='发行方式')
    """发行方式:"""

    IssueObject: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='IssueObject', column_type='varchar(255)', nullable=False, chn_name='发行对象')
    """发行对象:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='InnerCode', column_type='int', nullable=True, chn_name='证券内部编码')
    """证券内部编码:"""

    PlaStartDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='PlaStartDate', column_type='datetime', nullable=False, chn_name='配售起始日')
    """配售起始日:"""

    PlaEndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='PlaEndDate', column_type='datetime', nullable=False, chn_name='配售截止日')
    """配售截止日:"""

    PayStartDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='PayStartDate', column_type='datetime', nullable=False, chn_name='承配缴款起始日')
    """承配缴款起始日:"""

    PayEndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='PayEndDate', column_type='datetime', nullable=False, chn_name='承配缴款截止日')
    """承配缴款截止日:"""

    UnderwritingStartDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='UnderwritingStartDate', column_type='datetime', nullable=False, chn_name='承销起始日')
    """承销起始日:"""

    UnderwritingEndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='UnderwritingEndDate', column_type='datetime', nullable=False, chn_name='承销截止日')
    """承销截止日:"""

    PreparedListExchange: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='PreparedListExchange', column_type='int', nullable=False, chn_name='拟上市地')
    """拟上市地:拟上市地(PreparedListExchange)与(CT_SystemConst)表中的DM字段关联，令LB = 201 AND DM IN (83,90)，得到拟上市地的具体描述：83-上海证券交易所，90-深圳证券交易所。"""

    DividendPolicy: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='DividendPolicy', column_type='varchar(100)', nullable=False, chn_name='股利分配政策')
    """股利分配政策:"""

    EstimatedFirstDiviDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='EstimatedFirstDiviDate', column_type='varchar(50)', nullable=False, chn_name='预计首次分配时间')
    """预计首次分配时间:"""

    UnderwritingMode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='UnderwritingMode', column_type='int', nullable=False, chn_name='承销方式')
    """承销方式:承销方式(UnderwritingMode)和系统常量表关联，LB=1017"""

    InitialInfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='InitialInfoPublDate', column_type='datetime', nullable=True, chn_name='首次信息发布日期')
    """首次信息发布日期:"""

    ActualIssueVol: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='ActualIssueVol', column_type='decimal(16,0)', nullable=False, chn_name='实际发行量(股)')
    """实际发行量(股):"""

    TotalIssueMVRMB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='TotalIssueMVRMB', column_type='decimal(19,4)', nullable=False, chn_name='发行总市值(人民币元)')
    """发行总市值(人民币元):"""

    IssueCostRMB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='IssueCostRMB', column_type='decimal(19,4)', nullable=False, chn_name='发行费用总额(人民币元)')
    """发行费用总额(人民币元):"""

    IPOProceedsRMB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='IPOProceedsRMB', column_type='decimal(19,4)', nullable=False, chn_name='募集资金总额(人民币元)')
    """募集资金总额(人民币元):"""

    IPONetProceedsRMB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='IPONetProceedsRMB', column_type='decimal(19,4)', nullable=False, chn_name='募集资金净额(人民币元)')
    """募集资金净额(人民币元):"""

    IssueCostPerShareRMB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='IssueCostPerShareRMB', column_type='decimal(19,4)', nullable=False, chn_name='每股发行费用(人民币元)')
    """每股发行费用(人民币元):"""

    TotalIssueMVFC: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='TotalIssueMVFC', column_type='decimal(19,4)', nullable=False, chn_name='发行总市值(外币元)')
    """发行总市值(外币元):"""

    IssueCostFC: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='IssueCostFC', column_type='decimal(19,4)', nullable=False, chn_name='发行费用总额(外币元)')
    """发行费用总额(外币元):"""

    IPOProceedsFC: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='IPOProceedsFC', column_type='decimal(19,4)', nullable=False, chn_name='募集资金总额(外币元)')
    """募集资金总额(外币元):"""

    IPONetProceedsFC: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='IPONetProceedsFC', column_type='decimal(19,4)', nullable=False, chn_name='募集资金净额(外币元)')
    """募集资金净额(外币元):"""

    IntentLetterPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='IntentLetterPublDate', column_type='datetime', nullable=False, chn_name='招股意向书发布日期')
    """招股意向书发布日期:"""

    IssueCostPerShareFC: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='IssueCostPerShareFC', column_type='decimal(19,4)', nullable=False, chn_name='每股发行费用(外币元)')
    """每股发行费用(外币元):"""

    DateToAccount: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='DateToAccount', column_type='datetime', nullable=False, chn_name='募集资金到帐时间')
    """募集资金到帐时间:"""

    ListDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='ListDate', column_type='datetime', nullable=False, chn_name='上市日期')
    """上市日期:"""

    OutstandingShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='OutstandingShares', column_type='decimal(16,0)', nullable=False, chn_name='本次上市流通股数(股)')
    """本次上市流通股数(股):"""

    StraInvestorPlaVol: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='StraInvestorPlaVol', column_type='decimal(16,0)', nullable=False, chn_name='战略投资者配售股数(股)')
    """战略投资者配售股数(股):"""

    PlaNum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='PlaNum', column_type='int', nullable=False, chn_name='配售户数(户)')
    """配售户数(户):"""

    UnderwriterBoughtVol: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='UnderwriterBoughtVol', column_type='decimal(16,0)', nullable=False, chn_name='余股包销数量(股)')
    """余股包销数量(股):"""

    FirstOpenPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='FirstOpenPrice', column_type='decimal(19,4)', nullable=False, chn_name='上市首日开盘价(外币元)')
    """上市首日开盘价(外币元):"""

    FirstClosePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='FirstClosePrice', column_type='decimal(19,4)', nullable=False, chn_name='上市首日收盘价(外币元)')
    """上市首日收盘价(外币元):"""

    FirstTurnover: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='FirstTurnover', column_type='decimal(9,6)', nullable=False, chn_name='上市首日换手率')
    """上市首日换手率:"""

    ProspectusPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='ProspectusPublDate', column_type='datetime', nullable=False, chn_name='招股说明书发布日期')
    """招股说明书发布日期:"""

    EarningForecastYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='EarningForecastYear', column_type='datetime', nullable=False, chn_name='盈利预测年度')
    """盈利预测年度:"""

    MainIncomeForecast: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='MainIncomeForecast', column_type='decimal(19,4)', nullable=False, chn_name='主营业务收入预测(人民币元)')
    """主营业务收入预测(人民币元):"""

    NetProfitForecast: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='NetProfitForecast', column_type='decimal(19,4)', nullable=False, chn_name='净利润预测(人民币元)')
    """净利润预测(人民币元):"""

    DilutedEPSForecast: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='DilutedEPSForecast', column_type='decimal(19,4)', nullable=False, chn_name='全面摊薄每股盈利预测(人民币元)')
    """全面摊薄每股盈利预测(人民币元):"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    ListAnnouncementDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='ListAnnouncementDate', column_type='datetime', nullable=False, chn_name='上市公告书发布日期')
    """上市公告书发布日期:"""

    RaisingMethod: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='RaisingMethod', column_type='int', nullable=False, chn_name='募资方式')
    """募资方式:募资方式(RaisingMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1021，得到募资方式的具体描述：1-新股发行，2-历史遗留，3-增发新股，4-配股，5-发行可转换债券，6-发行企业债券，7-募资改投，8-非募集资金，9-发行权证，10-吸收合并，11-发行分离可转债，12-发行金融债，13-老股转让，14-老股转让+..."""

    StockType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='StockType', column_type='int', nullable=False, chn_name='发行股票类型')
    """发行股票类型:发行股票类型(StockType)与(CT_SystemConst)表中的DM字段关联，令LB = 1177，得到发行股票类型的具体描述：1-A股，2-B股，3-H股，4-大盘，5-国债回购，6-国债现货，7-金融债券，8-开放式基金，9-可转换债券，10-其他，11-企业债券，12-企业债券回购，13-投资基金，14-央行票据，15-深市代理沪市股票，16..."""

    ParValueRMB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_BShareIPO', column_name='ParValueRMB', column_type='decimal(19,4)', nullable=False, chn_name='每股面值(人民币元)')
    """每股面值(人民币元):"""

