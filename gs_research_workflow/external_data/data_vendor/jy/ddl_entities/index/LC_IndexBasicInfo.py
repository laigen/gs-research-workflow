# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_IndexBasicInfo(SQLTableEntity):
    name: str = 'LC_IndexBasicInfo'
    
    chn_name: str = '指数基本情况'
    
    business_unique: str = '此表与指数与行业对应 LC_CorrIndexIndustry关联，开通需要一起开'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.收录了市场上主要指数的基本情况，包括指数类别、成份证券类别、发布机构、发布日期、基期基点、指数发布的币种等信息。
2.数据源：中证指数有限公司、上海证券交易所、深圳证券交易所、中央国债登记结算有限责任公司、申银万国研究所、标普道琼斯指数公司等"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexBasicInfo', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    BaseDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexBasicInfo', column_name='BaseDate', column_type='datetime', nullable=False, chn_name='基日')
    """基日:"""

    BasePoint: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexBasicInfo', column_name='BasePoint', column_type='decimal(16,4)', nullable=False, chn_name='基点(点)')
    """基点(点):"""

    WAMethod: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexBasicInfo', column_name='WAMethod', column_type='int', nullable=False, chn_name='加权方式')
    """加权方式:加权方式(WAMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1265，得到加权方式的具体描述：10-流通股加权，13-流通股比例分级靠档加权，30-总股本加权，33-债券发行量加权，34-债券流通托管量加权，40-调整流通股本加权，41-调整流通市值加权，42-流通市值加权，43-总市值加权，44-风格评分加权法，45-基本..."""

    IndexType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexBasicInfo', column_name='IndexType', column_type='int', nullable=False, chn_name='指数类别')
    """指数类别:指数类别（IndexType）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令“LB=1266”，得到“指数类别”的具体描述。10-综合类指数，20-成份类指数，30-行业类指数，40-地区类指数42-策略类指数，43-风格类指数，44-主题类指数，45-基金类指数46-债券类指数，47-规模类指数，48-海外类指数，49-客户..."""

    IndexPriceType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexBasicInfo', column_name='IndexPriceType', column_type='int', nullable=False, chn_name='指数计算类别')
    """指数计算类别:指数计算类别（IndexPriceType）与(CT_SystemConst)表中的DM字段关联，令LB = 2012，得到指数计算类别的具体描述：1-价格指数，2-全收益指数，3-净收益指数，4-股息点指数，5-成交量指数。"""

    IndexDesignType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexBasicInfo', column_name='IndexDesignType', column_type='int', nullable=False, chn_name='指数设计类别')
    """指数设计类别:指数设计类别（IndexDesignType）与(CT_SystemConst)表中的DM字段关联，令LB = 2013，得到指数设计类别的具体描述：1-主指数，2-衍生指数。"""

    Relationship: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexBasicInfo', column_name='Relationship', column_type='int', nullable=False, chn_name='与主指数关系')
    """与主指数关系:与主指数关系（Relationship）与(CT_SystemConst)表中的DM字段关联，令LB = 2014，得到该指数与主指数关联关系的具体描述：1-币种不同，2-分红规则不同，3-分红规则和币种都不同，4-税后分红，5-主指数。"""

    RelaMainIndexCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexBasicInfo', column_name='RelaMainIndexCode', column_type='varchar(20)', nullable=False, chn_name='对应主指数代码')
    """对应主指数代码:"""

    RelaMainCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexBasicInfo', column_name='RelaMainCode', column_type='int', nullable=False, chn_name='对应主指数内码')
    """对应主指数内码:对应主指数内码（RelaMainCode）：当个数小于7位时，与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称；反之与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称。"""

    ComponentType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexBasicInfo', column_name='ComponentType', column_type='int', nullable=False, chn_name='成份证券类别')
    """成份证券类别:成份证券类别(ComponentType)与(CT_SystemConst)表中的DM字段关联，令LB = 1008，得到成份证券类别的具体描述：1000-股票，1001-A股，1003-B股，1004-H股，1005-红筹股，1006-个股期权，1007-权证，1009-股指期货，1010-中国存托凭证，1300-基金，1301-封闭式基金，1303-开放..."""

    IndexCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexBasicInfo', column_name='IndexCode', column_type='int', nullable=True, chn_name='指数内部代码')
    """指数内部代码:指数内部代码（IndexCode）：当个数小于7位时，与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称；反之与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称。"""

    SecuMarket: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexBasicInfo', column_name='SecuMarket', column_type='int', nullable=False, chn_name='成份证券市场')
    """成份证券市场:成份证券市场（SecuMarket）与(CT_SystemConst)表中的DM字段关联，令LB = 2015，得到成份证券市场的具体描述。"""

    ComponentSum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexBasicInfo', column_name='ComponentSum', column_type='int', nullable=False, chn_name='成份证券数量')
    """成份证券数量:"""

    ComponentAdPeriod: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexBasicInfo', column_name='ComponentAdPeriod', column_type='int', nullable=False, chn_name='成份证券调整周期')
    """成份证券调整周期:成份证券调整周期(ComponentAdPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 1264，得到成份证券调整周期的具体描述：1-每日，30-一个月，90-三个月，120-四个月，183-半年，365-一年，997-自动调整，998-不定期调整，999-其他。"""

    CurrencyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexBasicInfo', column_name='CurrencyCode', column_type='int', nullable=False, chn_name='币种')
    """币种:币种（Currency）与(CT_SystemConst)表中的DM字段关联，令LB = 1548，得到币种的具体描述。"""

    IndexAbstract: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexBasicInfo', column_name='IndexAbstract', column_type='varchar(1000)', nullable=False, chn_name='指数摘要')
    """指数摘要:"""

    IndexRemark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexBasicInfo', column_name='IndexRemark', column_type='text', nullable=False, chn_name='指数简介')
    """指数简介:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexBasicInfo', column_name='EndDate', column_type='datetime', nullable=False, chn_name='停用日期')
    """停用日期:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexBasicInfo', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexBasicInfo', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    IndustryStandard: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexBasicInfo', column_name='IndustryStandard', column_type='int', nullable=False, chn_name='行业标准')
    """行业标准:行业标准(IndustryStandard)与(CT_SystemConst)表中的DM字段关联，令LB = 1081，得到行业标准的具体描述：1-CSRC行业分类，2-非CSRC行业分类，3-中信行业分类，5-SSE行业分类，6-GICS行业分类，7-SSE-GICS行业分类，8-聚源行业分类，9-申万行业分类，10-聚源板块分类，11-中银(BOCI)行..."""

    IndustryType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexBasicInfo', column_name='IndustryType', column_type='int', nullable=False, chn_name='行业类别')
    """行业类别:行业类别（IndustryType）：
当IndustryStandard＝1或8时，与“CT_Industry”的“行业编码（ndustryNum”关联；
当IndustryStandard＝20时，与“行业类别表（CT_IndustryType）”的“行业编码（IndustryNum）”关联；
当IndustryStandard＝3或5时，与“CT_Sy..."""

    PubOrgCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexBasicInfo', column_name='PubOrgCode', column_type='int', nullable=False, chn_name='发布机构代码')
    """发布机构代码:发布机构代码（PubOrgCode）：与机构基本资料（LC_InstiArchive）中的企业编号（CompanyCode）关联。"""

    PubOrgName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexBasicInfo', column_name='PubOrgName', column_type='varchar(200)', nullable=False, chn_name='发布机构名称')
    """发布机构名称:"""

    CreatIndexOrgCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexBasicInfo', column_name='CreatIndexOrgCode', column_type='int', nullable=False, chn_name='编制机构代码')
    """编制机构代码:编制机构代码（CreatIndexOrgCode）：与机构基本资料（LC_InstiArchive）中的企业编号（CompanyCode）关联。"""

    CreatIndexOrgName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexBasicInfo', column_name='CreatIndexOrgName', column_type='varchar(200)', nullable=False, chn_name='编制机构名称')
    """编制机构名称:"""

    PubDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_IndexBasicInfo', column_name='PubDate', column_type='datetime', nullable=False, chn_name='发布日期')
    """发布日期:"""

