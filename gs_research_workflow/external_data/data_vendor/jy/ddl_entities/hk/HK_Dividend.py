# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_Dividend(SQLTableEntity):
    name: str = 'HK_Dividend'
    
    chn_name: str = '港股分红'
    
    business_unique: str = '无'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.记录港股分红方案、数据以及日期安排等信息，包含主要字段有：股息期间、财政年度、是否分红、每股股息、送红股比例、送红利认股证比例、派实物比例、转股比例等。
2.数据范围：1999年至今。
3.数据来源：港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    DividendPeriod: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='DividendPeriod', column_type='int', nullable=False, chn_name='股息期间')
    """股息期间:股息期间(DividendPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 1314，得到股息期间的具体描述：1-1个月，2-2个月，3-3个月，4-4个月，5-5个月，6-半年度，7-7个月，8-8个月，9-9个月，10-10个月，11-11个月，12-年度，13-13个月，14-14个月，15-15个月，16-16个月，17..."""

    FiscalYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='FiscalYear', column_type='datetime', nullable=False, chn_name='财政年度')
    """财政年度:"""

    IfDividend: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='IfDividend', column_type='int', nullable=False, chn_name='是否分红')
    """是否分红:是否分红（IfDividend）：0->否；1->是"""

    DividendType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='DividendType', column_type='int', nullable=False, chn_name='分红方式')
    """分红方式:"""

    DividendUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='DividendUnit', column_type='int', nullable=False, chn_name='股息单位')
    """股息单位:股息单位(DividendUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068，得到股息单位的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，1170-约旦第纳尔，1180-科..."""

    CashDividendPS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='CashDividendPS', column_type='decimal(18,8)', nullable=False, chn_name='1)每股股息(1派X元)')
    """1)每股股息(1派X元):"""

    OtherOption: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='OtherOption', column_type='int', nullable=False, chn_name='nan')
    """nan:-其他选择方式(OtherOption)与(CT_SystemConst)表中的DM字段关联，令LB = 1326 AND DM IN (101)，得到-其他选择方式的具体描述：101-以股代息。"""

    SpecialDividendPS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='SpecialDividendPS', column_type='decimal(18,8)', nullable=False, chn_name='每股特别股息(1派X元)')
    """每股特别股息(1派X元):"""

    SpecialDividendSubstitute: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='SpecialDividendSubstitute', column_type='int', nullable=False, chn_name='nan')
    """nan:-特别股息替代方式(SpecialDividendSubstitute)与(CT_SystemConst)表中的DM字段关联，令LB = 1326 AND DM IN (30,101)，得到-特别股息替代方式的具体描述：30-实物分派，101-以股代息。"""

    ShareDividendRateX: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='ShareDividendRateX', column_type='int', nullable=False, chn_name='2)送红股比例(X送Y)-X')
    """2)送红股比例(X送Y)-X:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='InnerCode', column_type='int', nullable=True, chn_name='内部编码')
    """内部编码:内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。"""

    ShareDividendRateY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='ShareDividendRateY', column_type='int', nullable=False, chn_name='nan')
    """nan:"""

    WarrantDividendRateX: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='WarrantDividendRateX', column_type='int', nullable=False, chn_name='3)送红利认股证比例(X送Y)-X')
    """3)送红利认股证比例(X送Y)-X:"""

    WarrantDividendRateY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='WarrantDividendRateY', column_type='int', nullable=False, chn_name='nan')
    """nan:"""

    PhysicalDividendRateX: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='PhysicalDividendRateX', column_type='int', nullable=False, chn_name='4)派实物比例(X送Y)-X')
    """4)派实物比例(X送Y)-X:"""

    PhysicalDividendRateY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='PhysicalDividendRateY', column_type='int', nullable=False, chn_name='nan')
    """nan:"""

    Statement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='Statement', column_type='varchar(500)', nullable=False, chn_name='方案说明')
    """方案说明:"""

    TotalCashDividend: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='TotalCashDividend', column_type='decimal(19,4)', nullable=False, chn_name='派现总额(元)')
    """派现总额(元):"""

    TotCashDivUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='TotCashDivUnit', column_type='int', nullable=False, chn_name='派现总额币种')
    """派现总额币种:派现总额币种(TotCashDivUnit)与(CT_SystemConst)表中的DM字段关联，令LB=1068，得到派现总额币种的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，1170-约旦第纳尔，11..."""

    DividendBase: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='DividendBase', column_type='int', nullable=False, chn_name='派发基准')
    """派发基准:派发基准(DividendBase)与(CT_SystemConst)表中的DM字段关联，令LB = 1327，得到派发基准的具体描述：10-已发行股份，20-供股之新股份，22-公开发售之新股份，30-拆细后之新股份，32-合并后之新股份，33-配售之新股份。"""

    DividendBaseShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='DividendBaseShares', column_type='decimal(18,2)', nullable=False, chn_name='派发基准股数(股)')
    """派发基准股数(股):"""

    InitialInfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='InitialInfoPublDate', column_type='datetime', nullable=False, chn_name='首次信息发布日期')
    """首次信息发布日期:"""

    TotalShareDividend: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='TotalShareDividend', column_type='decimal(18,2)', nullable=False, chn_name='红股总股数(股)')
    """红股总股数(股):"""

    TotalWarrantDividend: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='TotalWarrantDividend', column_type='decimal(18,2)', nullable=False, chn_name='红利认股证总份数(股)')
    """红利认股证总份数(股):"""

    LastTradeDay: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='LastTradeDay', column_type='datetime', nullable=False, chn_name='最后买卖日')
    """最后买卖日:"""

    ExDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='ExDate', column_type='datetime', nullable=False, chn_name='除净日')
    """除净日:"""

    RecordDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='RecordDate', column_type='datetime', nullable=False, chn_name='股权登记日(递交过户截止日)')
    """股权登记日(递交过户截止日):"""

    TransferBeginDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='TransferBeginDate', column_type='datetime', nullable=False, chn_name='截止过户首日')
    """截止过户首日:"""

    TransferEndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='TransferEndDate', column_type='datetime', nullable=False, chn_name='截止过户末日')
    """截止过户末日:"""

    DividendPayableDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='DividendPayableDate', column_type='datetime', nullable=False, chn_name='股息应付日(派息日)')
    """股息应付日(派息日):"""

    PayoutDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='PayoutDate', column_type='datetime', nullable=False, chn_name='红股寄发日')
    """红股寄发日:"""

    ShareDiviListingDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='ShareDiviListingDate', column_type='datetime', nullable=False, chn_name='红股买卖日(上市日)')
    """红股买卖日(上市日):"""

    Process: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='Process', column_type='int', nullable=False, chn_name='事件进程')
    """事件进程:事件进程(Process)与(CT_SystemConst)表中的DM字段关联，令LB = 1059，得到事件进程的具体描述：1000-意向，1001-预案，1004-决案，1007-否决，1010-申请，1013-批准，1016-未实施终止，1019-实施中，1022-实施完成，1025-解除，1028-到期，1041-续签，1043-部分续签，1051-..."""

    ScripDividendIssuePrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='ScripDividendIssuePrice', column_type='decimal(19,4)', nullable=False, chn_name='以股代息发行价格(元)')
    """以股代息发行价格(元):"""

    ScripDividendPayoutDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='ScripDividendPayoutDate', column_type='datetime', nullable=False, chn_name='以股代息股份寄发日')
    """以股代息股份寄发日:"""

    ScripDividendListingDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='ScripDividendListingDate', column_type='datetime', nullable=False, chn_name='以股代息股份上市日')
    """以股代息股份上市日:"""

    ScripDividendSum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='ScripDividendSum', column_type='decimal(18,2)', nullable=False, chn_name='发行以股代息股数(股)')
    """发行以股代息股数(股):"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='修改日期')
    """修改日期:"""

    CashDividendPSHKD: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='CashDividendPSHKD', column_type='decimal(18,10)', nullable=False, chn_name='每股股息(港元)')
    """每股股息(港元):"""

    SpecialDividendPSHKD: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='SpecialDividendPSHKD', column_type='decimal(18,10)', nullable=False, chn_name='每股特别股息(港元)')
    """每股特别股息(港元):"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    AssReportType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='AssReportType', column_type='int', nullable=False, chn_name='分配报告类型')
    """分配报告类型:"""

    TransferRatX: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='TransferRatX', column_type='int', nullable=False, chn_name='5)转增比例(X转增Y)-X')
    """5)转增比例(X转增Y)-X:"""

    DMPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='DMPublDate', column_type='datetime', nullable=False, chn_name='董事会公告日')
    """董事会公告日:"""

    TransferRatY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='TransferRatY', column_type='int', nullable=False, chn_name='nan')
    """nan:"""

    TransferTotShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='TransferTotShares', column_type='decimal(18,2)', nullable=False, chn_name='转增总股数(股)')
    """转增总股数(股):"""

    InsertTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='InsertTime', column_type='datetime', nullable=False, chn_name='发布时间')
    """发布时间:"""

    DMSignDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='DMSignDate', column_type='datetime', nullable=False, chn_name='董事会公告签署日')
    """董事会公告签署日:"""

    SMDeciPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='SMDeciPublDate', column_type='datetime', nullable=False, chn_name='股东大会公告日')
    """股东大会公告日:"""

    ListingPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='ListingPublDate', column_type='datetime', nullable=False, chn_name='上市文件通告日(通函)')
    """上市文件通告日(通函):"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Dividend', column_name='EndDate', column_type='datetime', nullable=False, chn_name='截止日期')
    """截止日期:"""

