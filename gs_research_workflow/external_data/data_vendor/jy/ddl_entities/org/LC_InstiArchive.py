# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_InstiArchive(SQLTableEntity):
    name: str = 'LC_InstiArchive'
    
    chn_name: str = '机构基本资料'
    
    business_unique: str = '由于“所属行业（Industry）”之前的数据源已不再维护，现更改相关的行业标准以“国民经济行业分类(2017)-32”为准，具体行业数据后续数据补充中。'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.收录市场上重要机构的基本资料情况，如证券公司、信托公司、保险公司等；包含机构名称、机构信息、联系方式、机构背景等信息
2.数据源：国家企业信用信息公示系统等"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    EngName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='EngName', column_type='varchar(100)', nullable=False, chn_name='英文名称')
    """英文名称:"""

    AbbrEngName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='AbbrEngName', column_type='varchar(100)', nullable=False, chn_name='英文简称')
    """英文简称:"""

    OrganizationCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='OrganizationCode', column_type='varchar(20)', nullable=False, chn_name='组织机构代码')
    """组织机构代码:"""

    CreditCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='CreditCode', column_type='varchar(20)', nullable=False, chn_name='统一社会信用代码')
    """统一社会信用代码:"""

    RegCapital: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='RegCapital', column_type='decimal(19,4)', nullable=False, chn_name='注册资本(元)')
    """注册资本(元):"""

    CurrencyUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='CurrencyUnit', column_type='int', nullable=False, chn_name='货币单位')
    """货币单位:货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068，得到货币单位的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，1170-约旦第纳尔，1180-科..."""

    EstablishmentDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='EstablishmentDate', column_type='datetime', nullable=False, chn_name='成立日期')
    """成立日期:"""

    EconomicNature: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='EconomicNature', column_type='int', nullable=False, chn_name='经济性质')
    """经济性质:经济性质（EconomicNature）：已废弃，停止维护，相关信息请参考“公司属性（CompanyCval）”。"""

    CompanyNature: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='CompanyNature', column_type='int', nullable=False, chn_name='企业性质')
    """企业性质:企业性质(CompanyNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1133，得到企业性质的具体描述：100-内资企业，110-国有企业，120-集体企业，130-股份合作企业，140-联营企业，141-国有联营企业，142-集体联营企业，143-国有与集体联营企业，149-其他联营企业，150-有限责任公司，151-国有..."""

    CompanyType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='CompanyType', column_type='int', nullable=False, chn_name='企业类别')
    """企业类别:企业类别(CompanyType)与(CT_SystemConst)表中的DM字段关联，令LB = 1222，得到企业类别的具体描述：1110-综合类券商，1130-经纪类券商，1140-证券分公司，1150-证券营业部，1190-其他证券公司，1199-证券交易所，1300-信托投资公司，1301-信托担保人，1510-证券咨询公司，2100-基金管理公司..."""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='CompanyCode', column_type='int', nullable=False, chn_name='企业编号')
    """企业编号:"""

    CompanyCval: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='CompanyCval', column_type='int', nullable=False, chn_name='公司属性')
    """公司属性:公司属性(CompanyCval)：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令“LB=1096”，得到公司属性的具体描述。1-国家单位，4-中外合资，5-外资独资，6-民营，7-集体企业，8-自然人，9-其他，10-中央国有企业，11-国有企业，12-地方国有企业，13-其他外资企业。"""

    RegAddr: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='RegAddr', column_type='varchar(200)', nullable=False, chn_name='注册地址')
    """注册地址:"""

    RegZip: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='RegZip', column_type='char(6)', nullable=False, chn_name='注册地址邮编')
    """注册地址邮编:"""

    RegCity: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='RegCity', column_type='int', nullable=False, chn_name='注册所在城市')
    """注册所在城市:注册所在城市(RegCity)与(CT_SystemConst)表中的DM字段关联，令LB = 1145，得到注册所在城市的具体描述：1-华北，2-东北，3-华东，4-中南，5-西南，6-西北，11-东部，13-中部，14-中西部，15-西部，16-珠三角，17-长三角，18-环渤海，19-港口中转，20-北方七港，21-外贸，110000-北京，11010..."""

    RegArea: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='RegArea', column_type='int', nullable=False, chn_name='注册所在区县')
    """注册所在区县:注册所在区县（RegArea）：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCode）”关联，得到注册地城市所在区县的具体信息。"""

    OfficeAddr: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='OfficeAddr', column_type='varchar(200)', nullable=False, chn_name='办公地址')
    """办公地址:"""

    ContactAddr: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='ContactAddr', column_type='varchar(200)', nullable=False, chn_name='联系地址')
    """联系地址:"""

    ContactZip: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='ContactZip', column_type='char(6)', nullable=False, chn_name='联系地址邮编')
    """联系地址邮编:"""

    ContactCity: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='ContactCity', column_type='int', nullable=False, chn_name='联系所在城市')
    """联系所在城市:联系所在城市(ContactCity)与(CT_SystemConst)表中的DM字段关联，令LB = 1145，得到联系所在城市的具体描述：1-华北，2-东北，3-华东，4-中南，5-西南，6-西北，11-东部，13-中部，14-中西部，15-西部，16-珠三角，17-长三角，18-环渤海，19-港口中转，20-北方七港，21-外贸，110000-北京，1..."""

    Email: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='Email', column_type='varchar(50)', nullable=False, chn_name='电子邮箱')
    """电子邮箱:"""

    ParentCompany: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='ParentCompany', column_type='int', nullable=False, chn_name='所属公司')
    """所属公司:所属公司（ParentCompany）：与本表中的“企业编号（CompanyCode）”关联，得到所属公司的基础信息。"""

    Website: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='Website', column_type='varchar(50)', nullable=False, chn_name='网址')
    """网址:"""

    LegalPersonRepr: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='LegalPersonRepr', column_type='varchar(50)', nullable=False, chn_name='法人代表')
    """法人代表:"""

    GeneralManager: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='GeneralManager', column_type='varchar(50)', nullable=False, chn_name='总经理')
    """总经理:"""

    OtherManager: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='OtherManager', column_type='varchar(50)', nullable=False, chn_name='其它负责人')
    """其它负责人:"""

    Contactman: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='Contactman', column_type='varchar(50)', nullable=False, chn_name='联系人')
    """联系人:"""

    Tel: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='Tel', column_type='varchar(50)', nullable=False, chn_name='联系电话')
    """联系电话:"""

    Fax: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='Fax', column_type='varchar(50)', nullable=False, chn_name='传真')
    """传真:"""

    BriefIntroText: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='BriefIntroText', column_type='text', nullable=False, chn_name='公司简介')
    """公司简介:"""

    BusinessMajor: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='BusinessMajor', column_type='text', nullable=False, chn_name='主营业务')
    """主营业务:"""

    Industry: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='Industry', column_type='int', nullable=False, chn_name='所属行业')
    """所属行业:所属行业（Industry）：与“行业类别表(CT_IndustryType)”中的“行业内部编码[IndustryNum]”关联，令“行业分类标准[Standard]=32”,得到“国民经济行业分类(2017)”的具体描述。"""

    ListedCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='ListedCode', column_type='int', nullable=False, chn_name='上市公司代码')
    """上市公司代码:上市公司代码（ListedCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到相应的上市公司的交易代码、证券简称等信息。"""

    StartDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='StartDate', column_type='datetime', nullable=False, chn_name='存续起始日')
    """存续起始日:"""

    CloseDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='CloseDate', column_type='datetime', nullable=False, chn_name='存续截止日')
    """存续截止日:"""

    CloseReason: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='CloseReason', column_type='int', nullable=False, chn_name='存续截止原因')
    """存续截止原因:存续截止原因（CloseReason）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令“LB=1254”，得到编码类型具体描述：11-撤销，13-解散，15-破产，21-合并重组，51-更名，53-迁址，99-其他。"""

    IfExisted: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='IfExisted', column_type='int', nullable=False, chn_name='是否存在')
    """是否存在:是否存在（IfExisted）：该字段固定常量以下常量：1-有；0-无"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    RegOrg: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='RegOrg', column_type='varchar(100)', nullable=False, chn_name='登记机构')
    """登记机构:"""

    RegStatus: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='RegStatus', column_type='int', nullable=False, chn_name='登记状态')
    """登记状态:登记状态(RegStatus):与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令“LB=2122”，得到编码类型具体描述：1-在营（开业）,2-注销,3-吊销,4-撤销,5-迁出,99-其他"""

    InvestAdvisorName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='InvestAdvisorName', column_type='int', nullable=False, chn_name='基金管理人名称')
    """基金管理人名称:基金管理人名称（InvestAdvisorName）：与“基金管理人概况（MF_InvestAdvisorOutline）“中的“基金管理人编码（InvestAdvisorCode）”关联，得到相应的基金管理人的基础信息。"""

    TrusteeName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='TrusteeName', column_type='int', nullable=False, chn_name='基金托管人名称')
    """基金托管人名称:基金托管人名称（TrusteeName）：与“基金托管人概况（MF_TrusteeOutline）”中的“基金托管人编号（TrusteeCode）”关联，得到相应的基金托管人的基础信息。"""

    ChiName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='ChiName', column_type='varchar(100)', nullable=False, chn_name='中文名称')
    """中文名称:"""

    AbbrChiName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='AbbrChiName', column_type='varchar(100)', nullable=False, chn_name='中文简称')
    """中文简称:"""

    NameChiSpelling: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InstiArchive', column_name='NameChiSpelling', column_type='varchar(100)', nullable=False, chn_name='中文拼音简称')
    """中文拼音简称:"""

