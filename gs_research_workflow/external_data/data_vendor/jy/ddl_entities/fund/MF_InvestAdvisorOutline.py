# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_InvestAdvisorOutline(SQLTableEntity):
    name: str = 'MF_InvestAdvisorOutline'
    
    chn_name: str = '公募基金管理人概况'
    
    business_unique: str = 'InvestAdvisorCode'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.本表记录了基金管理人的基本情况介绍，包括成立日期、注册资本、法人代表、联系方式、背景简介等。
2.历史数据：1998年3月起-至今。
3.信息来源：基金公司官网。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestAdvisorOutline', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    RegCapital: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestAdvisorOutline', column_name='RegCapital', column_type='decimal(18,4)', nullable=False, chn_name='注册资本(元)')
    """注册资本(元):"""

    RegAddr: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestAdvisorOutline', column_name='RegAddr', column_type='varchar(100)', nullable=False, chn_name='注册地址')
    """注册地址:"""

    OfficeAddr: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestAdvisorOutline', column_name='OfficeAddr', column_type='varchar(100)', nullable=False, chn_name='办公地址')
    """办公地址:"""

    ZipCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestAdvisorOutline', column_name='ZipCode', column_type='varchar(6)', nullable=False, chn_name='邮编')
    """邮编:"""

    Email: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestAdvisorOutline', column_name='Email', column_type='varchar(50)', nullable=False, chn_name='邮箱')
    """邮箱:"""

    ContactAddr: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestAdvisorOutline', column_name='ContactAddr', column_type='varchar(100)', nullable=False, chn_name='联系地址')
    """联系地址:"""

    Tel: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestAdvisorOutline', column_name='Tel', column_type='varchar(50)', nullable=False, chn_name='联系电话')
    """联系电话:"""

    Fax: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestAdvisorOutline', column_name='Fax', column_type='varchar(50)', nullable=False, chn_name='传真')
    """传真:"""

    WebSite: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestAdvisorOutline', column_name='WebSite', column_type='varchar(50)', nullable=False, chn_name='公司网址')
    """公司网址:"""

    LinkMan: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestAdvisorOutline', column_name='LinkMan', column_type='varchar(50)', nullable=False, chn_name='联系人')
    """联系人:"""

    InvestAdvisorCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestAdvisorOutline', column_name='InvestAdvisorCode', column_type='int', nullable=True, chn_name='基金管理人编码')
    """基金管理人编码:基金管理人编码(InvestAdvisorCode)：与机构基本资料(LC_InstiArchive)表的企业编号(CompanyCode)字段关联，可查询基金管理人中文名称、英文名称、组织机构代码等基本信息。"""

    ServiceLine: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestAdvisorOutline', column_name='ServiceLine', column_type='varchar(50)', nullable=False, chn_name='客服热线')
    """客服热线:"""

    Region: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestAdvisorOutline', column_name='Region', column_type='int', nullable=False, chn_name='所属地区')
    """所属地区:所属地区(Region)与(CT_SystemConst)表中的DM字段关联，令LB=1145，得到所属地区的具体描述：1-华北，2-东北，3-华东，4-中南，5-西南，6-西北，11-东部，13-中部，14-中西部，15-西部，16-珠三角，17-长三角，18-环渤海，19-港口中转，20-北方七港，21-外贸，110000-北京，110101-东城区，1..."""

    TACode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestAdvisorOutline', column_name='TACode', column_type='varchar(20)', nullable=False, chn_name='注册登记代码')
    """注册登记代码:"""

    CSRCCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestAdvisorOutline', column_name='CSRCCode', column_type='varchar(20)', nullable=False, chn_name='证监会标识码')
    """证监会标识码:"""

    Background: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestAdvisorOutline', column_name='Background', column_type='text', nullable=False, chn_name='背景介绍')
    """背景介绍:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestAdvisorOutline', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新日期')
    """更新日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestAdvisorOutline', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InvestAdvisorName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestAdvisorOutline', column_name='InvestAdvisorName', column_type='varchar(100)', nullable=True, chn_name='基金管理人名称')
    """基金管理人名称:"""

    InvestAdvisorAbbrName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestAdvisorOutline', column_name='InvestAdvisorAbbrName', column_type='varchar(50)', nullable=False, chn_name='基金管理人简称')
    """基金管理人简称:"""

    LegalRepr: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestAdvisorOutline', column_name='LegalRepr', column_type='varchar(50)', nullable=False, chn_name='法人代表')
    """法人代表:"""

    GeneralManager: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestAdvisorOutline', column_name='GeneralManager', column_type='varchar(50)', nullable=False, chn_name='总经理')
    """总经理:"""

    EstablishmentDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestAdvisorOutline', column_name='EstablishmentDate', column_type='datetime', nullable=False, chn_name='成立日期')
    """成立日期:"""

    MaturityEndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestAdvisorOutline', column_name='MaturityEndDate', column_type='datetime', nullable=False, chn_name='存续截止日')
    """存续截止日:"""

    OrganizationForm: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_InvestAdvisorOutline', column_name='OrganizationForm', column_type='varchar(50)', nullable=False, chn_name='组织形式')
    """组织形式:组织形式(OrganizationForm)与(CT_SystemConst)表中的DM字段关联，令LB=1133 and DM in (100,160,210,310,900)，得到组织形式的具体描述：100-内资企业，160-股份有限公司，210-港澳台合资经营企业，310-中外合资经营企业，900-其他性质。"""

