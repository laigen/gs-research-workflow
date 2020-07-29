# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_ExchgShare(SQLTableEntity):
    name: str = 'HK_ExchgShare'
    
    chn_name: str = '港股换股合并分拆'
    
    business_unique: str = 'InnerCode,InfoPublDate,ExchgFinishDate'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.本表记录港股换股、吸收合并、分拆的信息，存储吸收合并及分拆业务独立上市的数据。主要包括三类相关数据：1.吸收合并；2.被吸收合并；3.分拆上市。                                           
2.数据范围：2002年至今。
3.信息来源：港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    SupplementType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='SupplementType', column_type='int', nullable=False, chn_name='配套方案类别')
    """配套方案类别:配套方案类别(SupplementType)与(CT_SystemConst)表中的DM字段关联，令LB = 1348，得到配套方案类别的具体描述：10-增发，20-分红。"""

    Process: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='Process', column_type='int', nullable=False, chn_name='事件进程')
    """事件进程:事件进程(Process)与(CT_SystemConst)表中的DM字段关联，令LB = 1059，得到事件进程的具体描述：1000-意向，1001-预案，1004-决案，1007-否决，1010-申请，1013-批准，1016-未实施终止，1019-实施中，1022-实施完成，1025-解除，1028-到期，1041-续签，1043-部分续签，1051-..."""

    ExchangeType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='ExchangeType', column_type='int', nullable=False, chn_name='换股方式')
    """换股方式:换股方式(ExchangeType)，该字段固定以下常量：1-吸收合并；2-被吸收合并；3-分拆上市"""

    ExchgNumerator: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='ExchgNumerator', column_type='decimal(18,4)', nullable=False, chn_name='换股比例分子(数值)')
    """换股比例分子(数值):"""

    ExchDenominator: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='ExchDenominator', column_type='decimal(18,4)', nullable=False, chn_name='换股比例分母(数值)')
    """换股比例分母(数值):"""

    NewShareTradeD: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='NewShareTradeD', column_type='datetime', nullable=False, chn_name='新股份开始交易日')
    """新股份开始交易日:"""

    WriteOffDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='WriteOffDate', column_type='datetime', nullable=False, chn_name='合并后注销日')
    """合并后注销日:"""

    MergedParty: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='MergedParty', column_type='varchar(200)', nullable=False, chn_name='(被)合并公司名称')
    """(被)合并公司名称:"""

    MergedShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='MergedShare', column_type='int', nullable=False, chn_name='所属股票')
    """所属股票:"""

    IssuedShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='IssuedShare', column_type='decimal(18,2)', nullable=False, chn_name='已发行股本数目')
    """已发行股本数目:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='InnerCode', column_type='int', nullable=False, chn_name='内部编码')
    """内部编码:内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。"""

    MainBusiness: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='MainBusiness', column_type='varchar(200)', nullable=False, chn_name='主营业务')
    """主营业务:"""

    NewCompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='NewCompanyCode', column_type='int', nullable=False, chn_name='合并后公司代码')
    """合并后公司代码:"""

    NewCompanyName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='NewCompanyName', column_type='varchar(200)', nullable=False, chn_name='合并后公司名称')
    """合并后公司名称:"""

    NewTotalShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='NewTotalShare', column_type='decimal(18,2)', nullable=False, chn_name='合并后股数')
    """合并后股数:"""

    RegAbbr: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='RegAbbr', column_type='int', nullable=False, chn_name='注册地')
    """注册地:注册地(RegAbbr)与(CT_SystemConst)表中的DM字段关联，令LB = 1023，得到注册地的具体描述：3-港澳台，4-中东地区，7-国际，100-亚洲，101-阿富汗，102-巴林，103-孟加拉国，104-不丹，105-文莱，106-缅甸，107-柬埔寨，108-塞浦路斯，109-朝鲜，110-中国香港，111-印度，112-印度尼西亚..."""

    CurrencyUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='CurrencyUnit', column_type='int', nullable=False, chn_name='面值单位')
    """面值单位:面值单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068，得到面值单位的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，1170-约旦第纳尔，1180-科..."""

    ParValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='ParValue', column_type='decimal(18,8)', nullable=False, chn_name='面值')
    """面值:"""

    NewTradeUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='NewTradeUnit', column_type='int', nullable=False, chn_name='新买卖单位')
    """新买卖单位:"""

    Currency: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='Currency', column_type='int', nullable=False, chn_name='货币单位')
    """货币单位:货币单位(Currency)与(CT_SystemConst)表中的DM字段关联，令LB = 1068，得到货币单位的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，1170-约旦第纳尔，1180-科威特第纳..."""

    OptionPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='OptionPrice', column_type='decimal(18,8)', nullable=False, chn_name='选择权价格')
    """选择权价格:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    ExcuteEndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='ExcuteEndDate', column_type='datetime', nullable=False, chn_name='行使截止日期')
    """行使截止日期:"""

    ExcutePublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='ExcutePublDate', column_type='datetime', nullable=False, chn_name='行使结果公布日期')
    """行使结果公布日期:"""

    ExcuteDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='ExcuteDate', column_type='datetime', nullable=False, chn_name='选择权实施日')
    """选择权实施日:"""

    TransferDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='TransferDate', column_type='datetime', nullable=False, chn_name='转权日')
    """转权日:"""

    SplitFirmName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='SplitFirmName', column_type='varchar(200)', nullable=False, chn_name='分拆公司名称')
    """分拆公司名称:"""

    SplitFirmCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='SplitFirmCode', column_type='int', nullable=False, chn_name='分拆股票代码')
    """分拆股票代码:"""

    TotalShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='TotalShare', column_type='decimal(18,2)', nullable=False, chn_name='发行股本数目')
    """发行股本数目:"""

    SplitBusiness: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='SplitBusiness', column_type='varchar(200)', nullable=False, chn_name='分拆业务')
    """分拆业务:"""

    LastTradeDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='LastTradeDate', column_type='datetime', nullable=False, chn_name='最后买卖日(优先配额)')
    """最后买卖日(优先配额):"""

    ExDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='ExDate', column_type='datetime', nullable=False, chn_name='除净日(优先配额)')
    """除净日(优先配额):"""

    ContractDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='ContractDate', column_type='datetime', nullable=False, chn_name='协议签署日')
    """协议签署日:"""

    RecordDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='RecordDate', column_type='datetime', nullable=False, chn_name='股权登记日(优先配额)')
    """股权登记日(优先配额):"""

    StopTran1stDay: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='StopTran1stDay', column_type='datetime', nullable=False, chn_name='暂停过户首日(优先配额)')
    """暂停过户首日(优先配额):"""

    StopTranLastDay: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='StopTranLastDay', column_type='datetime', nullable=False, chn_name='暂停过户末日(优先配额)')
    """暂停过户末日(优先配额):"""

    ShareDeliverDay: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='ShareDeliverDay', column_type='datetime', nullable=False, chn_name='分拆公司股票寄发日')
    """分拆公司股票寄发日:"""

    ShareListDay: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='ShareListDay', column_type='datetime', nullable=False, chn_name='分拆公司股票上市日')
    """分拆公司股票上市日:"""

    Statement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='Statement', column_type='varchar(500)', nullable=False, chn_name='备注')
    """备注:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='JSID', column_type='bigint', nullable=False, chn_name='JSID')
    """JSID:"""

    SMDeciDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='SMDeciDate', column_type='datetime', nullable=False, chn_name='股东大会决议日')
    """股东大会决议日:"""

    CircularPubDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='CircularPubDate', column_type='datetime', nullable=False, chn_name='通函公布日')
    """通函公布日:"""

    ExpirePublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='ExpirePublDate', column_type='datetime', nullable=False, chn_name='终止实施公告日')
    """终止实施公告日:"""

    ExchgFinishDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='ExchgFinishDate', column_type='datetime', nullable=False, chn_name='换股完成日期')
    """换股完成日期:"""

    SchemeStatement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ExchgShare', column_name='SchemeStatement', column_type='varchar(1000)', nullable=False, chn_name='方案说明')
    """方案说明:"""

