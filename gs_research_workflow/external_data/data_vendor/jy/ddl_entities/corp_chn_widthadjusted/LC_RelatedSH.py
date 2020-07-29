# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_RelatedSH(SQLTableEntity):
    name: str = 'LC_RelatedSH'
    
    chn_name: str = '企业之间参股情况'
    
    business_unique: str = 'EndDate,Relationship,CompanyName,SHName,RelationshipStartDate,RelationshipEndDate,RelatedWay'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.收录上市公司与其股东之间的关联关系，权益形成方式，关联股东持股情况等。
2.数据范围：2004-12-31至今
3.信息来源：招股说明书、定报、临时公告等。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_RelatedSH', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_RelatedSH', column_name='CompanyCode', column_type='int', nullable=False, chn_name='企业所属证券')
    """企业所属证券:企业所属证券（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。"""

    SN: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_RelatedSH', column_name='SN', column_type='int', nullable=False, chn_name='排序序号')
    """排序序号:"""

    SHName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_RelatedSH', column_name='SHName', column_type='varchar(200)', nullable=False, chn_name='股东名称')
    """股东名称:"""

    SHNameAbbr: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_RelatedSH', column_name='SHNameAbbr', column_type='varchar(100)', nullable=False, chn_name='股东简称')
    """股东简称:"""

    SHNumber: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_RelatedSH', column_name='SHNumber', column_type='int', nullable=False, chn_name='股东编号')
    """股东编号:股东编号（SHNumber）与机构基本资料(LC_InstiArchive)中的企业编号(CompanyCode)关联"""

    SHCompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_RelatedSH', column_name='SHCompanyCode', column_type='int', nullable=False, chn_name='股东所属证券')
    """股东所属证券:股东所属证券（SHCompanyCode）与证券主表(SecuMain)中的公司代码(CompanyCode)关联"""

    SHSN: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_RelatedSH', column_name='SHSN', column_type='smallint', nullable=False, chn_name='股东序号')
    """股东序号:"""

    SHInvestSum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_RelatedSH', column_name='SHInvestSum', column_type='decimal(19,4)', nullable=False, chn_name='股东投资金额')
    """股东投资金额:"""

    Currency: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_RelatedSH', column_name='Currency', column_type='int', nullable=False, chn_name='货币单位')
    """货币单位:货币单位(Currency)与(CT_SystemConst)表中的DM字段关联，令LB = 1068，得到货币单位的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，1170-约旦第纳尔，1180-科威特第纳..."""

    HoldingSum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_RelatedSH', column_name='HoldingSum', column_type='decimal(18,2)', nullable=False, chn_name='股东持股数量')
    """股东持股数量:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_RelatedSH', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    SHInvestSumEnd: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_RelatedSH', column_name='SHInvestSumEnd', column_type='decimal(19,4)', nullable=False, chn_name='投资期末余额')
    """投资期末余额:"""

    HoldingPCT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_RelatedSH', column_name='HoldingPCT', column_type='decimal(9,8)', nullable=False, chn_name='股东持股比例')
    """股东持股比例:"""

    HoldingShareType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_RelatedSH', column_name='HoldingShareType', column_type='int', nullable=False, chn_name='股东持股类别')
    """股东持股类别:股东持股类别(HoldingShareType)与(CT_SystemConst)表中的DM字段关联，令LB = 1024，得到股东持股类别的具体描述：1-流通A股，2-H股，3-B股，4-国家股，5-法人股，6-境外法人股，7-职工股，8-转配股，9-个人持股，10-S股，11-限售流通A股，12-境内优先股，13-境外优先股，15-N股，16-D股，43..."""

    IndirectHoldingPCT: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_RelatedSH', column_name='IndirectHoldingPCT', column_type='decimal(9,6)', nullable=False, chn_name='持股比例(间接)')
    """持股比例(间接):"""

    FormationOfEquity: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_RelatedSH', column_name='FormationOfEquity', column_type='int', nullable=False, chn_name='权益形成方式')
    """权益形成方式:权益形成方式(FormationOfEquity)与(CT_SystemConst)表中的DM字段关联，令LB = 1263，得到权益形成方式的具体描述：11-发起投资，13-后期投资，21-权益受让，23-权益增持，25-权益减持，29-权益转让，51-权益托管，99-其他方式。"""

    RelationshipStartDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_RelatedSH', column_name='RelationshipStartDate', column_type='datetime', nullable=False, chn_name='关联起始日')
    """关联起始日:"""

    RelationshipEndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_RelatedSH', column_name='RelationshipEndDate', column_type='datetime', nullable=False, chn_name='关联截止日')
    """关联截止日:"""

    RelatedWay: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_RelatedSH', column_name='RelatedWay', column_type='int', nullable=False, chn_name='关联方式')
    """关联方式:关联方式(RelatedWay)与(CT_SystemConst)表中的DM字段关联，令LB = 1131，得到关联方式的具体描述：1-直接关联，2-潜在关联。"""

    Process: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_RelatedSH', column_name='Process', column_type='varchar(500)', nullable=False, chn_name='关联进程说明')
    """关联进程说明:"""

    IfEffected: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_RelatedSH', column_name='IfEffected', column_type='int', nullable=False, chn_name='是否有效')
    """是否有效:是否有效（IfEffected），该字段固定以下常量：0-否；1-是"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_RelatedSH', column_name='InfoSource', column_type='varchar(50)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_RelatedSH', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='修改日期')
    """修改日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_RelatedSH', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    AnnouncementType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_RelatedSH', column_name='AnnouncementType', column_type='int', nullable=False, chn_name='公告类别')
    """公告类别:公告类别(AnnouncementType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311，得到公告类别的具体描述：10-发行上市书，20-定期报告，30-业绩快报，50-章程制度，70-临时公告，90-交易所通报，91-交易所临时停(复)牌公告，99-其他。"""

    InfoType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_RelatedSH', column_name='InfoType', column_type='int', nullable=False, chn_name='信息类别')
    """信息类别:信息类别(InfoType)与(CT_SystemConst)表中的DM字段关联，令LB = 1457，得到信息类别的具体描述：1-上市公司控股及合营企业，2-上市公司长期股权投资企业，3-上市公司直接股东，9-其他。"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_RelatedSH', column_name='EndDate', column_type='datetime', nullable=False, chn_name='截止日期')
    """截止日期:"""

    Relationship: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_RelatedSH', column_name='Relationship', column_type='int', nullable=False, chn_name='关联类型')
    """关联类型:关联类型(Relationship)与(CT_SystemConst)表中的DM字段关联，令LB = 1132，得到关联类型的具体描述：11-从属关联，13-受托关联，90-其他关联，93-领导人关联，95-亲属关联，97-行政监管关联。"""

    CompanyNum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_RelatedSH', column_name='CompanyNum', column_type='int', nullable=True, chn_name='企业编号')
    """企业编号:企业编号（CompanyNum）与机构基本资料(LC_InstiArchive)中的企业编号(CompanyCode)关联"""

    CompanyName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_RelatedSH', column_name='CompanyName', column_type='varchar(200)', nullable=False, chn_name='企业名称')
    """企业名称:"""

