# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_StockArchives(SQLTableEntity):
    name: str = 'HK_StockArchives'
    
    chn_name: str = '港股公司概况'
    
    business_unique: str = 'CompanyCode'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.收录港股上市公司的基础信息，包括名称、成立日期、注册地点、注册资本、公司业务、所属行业分类、主席、公司秘书、联系方式等信息。
2.信息来源：港交所等。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StockArchives', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    InduCHS: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StockArchives', column_name='InduCHS', column_type='int', nullable=False, chn_name='所属行业-恒生')
    """所属行业-恒生:所属行业-恒生（InduCHS）：目前字段在该表已经不维护，可以在
港股公司行业划分表HK_ExgIndustry获取到对应的行业分类。"""

    Chairman: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StockArchives', column_name='Chairman', column_type='varchar(100)', nullable=False, chn_name='主席')
    """主席:"""

    CompanySecretary: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StockArchives', column_name='CompanySecretary', column_type='varchar(100)', nullable=False, chn_name='公司秘书')
    """公司秘书:"""

    CertifiedAccountant: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StockArchives', column_name='CertifiedAccountant', column_type='varchar(100)', nullable=False, chn_name='合资格会计师')
    """合资格会计师:"""

    RegisteredOffice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StockArchives', column_name='RegisteredOffice', column_type='varchar(200)', nullable=False, chn_name='注册办事处')
    """注册办事处:"""

    GeneralOffice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StockArchives', column_name='GeneralOffice', column_type='varchar(200)', nullable=False, chn_name='总办事处及主要营业地点')
    """总办事处及主要营业地点:"""

    Registrars: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StockArchives', column_name='Registrars', column_type='varchar(200)', nullable=False, chn_name='股份过户处(香港)')
    """股份过户处(香港):"""

    Tel: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StockArchives', column_name='Tel', column_type='varchar(50)', nullable=False, chn_name='电话')
    """电话:"""

    Fax: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StockArchives', column_name='Fax', column_type='varchar(50)', nullable=False, chn_name='传真')
    """传真:"""

    Eail: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StockArchives', column_name='Eail', column_type='varchar(50)', nullable=False, chn_name='邮箱')
    """邮箱:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StockArchives', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到港股的交易代码、简称等。"""

    Website: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StockArchives', column_name='Website', column_type='varchar(200)', nullable=False, chn_name='网址')
    """网址:"""

    AuditInstitution: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StockArchives', column_name='AuditInstitution', column_type='varchar(500)', nullable=False, chn_name='审计机构')
    """审计机构:"""

    RegCapital: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StockArchives', column_name='RegCapital', column_type='decimal(19,4)', nullable=False, chn_name='注册资本(万元)')
    """注册资本(万元):"""

    RegCapitalCurrency: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StockArchives', column_name='RegCapitalCurrency', column_type='int', nullable=False, chn_name='注册资本货币单位')
    """注册资本货币单位:注册资本货币单位(RegCapitalCurrency)与(CT_SystemConst)表中的DM字段关联，令LB = 1548，得到注册资本货币单位的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1160-日本元，1161-欧洲日元(离岸)，1170-约旦第纳尔，1180-科威特第纳尔，11..."""

    BriefIntroduction: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StockArchives', column_name='BriefIntroduction', column_type='text', nullable=False, chn_name='公司简介')
    """公司简介:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StockArchives', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='修改日期')
    """修改日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StockArchives', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    ChiName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StockArchives', column_name='ChiName', column_type='varchar(200)', nullable=False, chn_name='公司名称')
    """公司名称:"""

    EstablishmentDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StockArchives', column_name='EstablishmentDate', column_type='datetime', nullable=False, chn_name='成立日期')
    """成立日期:"""

    RegAbbr: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StockArchives', column_name='RegAbbr', column_type='int', nullable=False, chn_name='注册地点')
    """注册地点:注册地点(RegAbbr)与(CT_SystemConst)表中的DM字段关联，令LB = 1023，得到注册地点的具体描述：3-港澳台，4-中东地区，7-国际，100-亚洲，101-阿富汗，102-巴林，103-孟加拉国，104-不丹，105-文莱，106-缅甸，107-柬埔寨，108-塞浦路斯，109-朝鲜，110-中国香港，111-印度，112-印度尼..."""

    CompanyType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StockArchives', column_name='CompanyType', column_type='int', nullable=False, chn_name='公司类别')
    """公司类别:公司类别(CompanyType)与(CT_SystemConst)表中的DM字段关联，令LB = 1501，得到公司类别的具体描述：1-境内注册内地国资控制，2-境内注册内地个人控制，5-境外注册内地国资控制，6-境外注册内地个人控制，9-其他。"""

    CompanyTypeDesc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StockArchives', column_name='CompanyTypeDesc', column_type='varchar(50)', nullable=False, chn_name='公司类别描述')
    """公司类别描述:"""

    Business: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StockArchives', column_name='Business', column_type='varchar(1000)', nullable=False, chn_name='公司业务')
    """公司业务:"""

    InduCHKE: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StockArchives', column_name='InduCHKE', column_type='int', nullable=False, chn_name='所属行业-港交所')
    """所属行业-港交所:所属行业-港交所（InduCHKE）:目前字段在该表已经不维护，可以在
港股公司行业划分表HK_ExgIndustry获取到对应的行业分类。"""

