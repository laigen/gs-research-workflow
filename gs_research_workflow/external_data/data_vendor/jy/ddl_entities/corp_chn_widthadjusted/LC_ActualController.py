# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_ActualController(SQLTableEntity):
    name: str = 'LC_ActualController'
    
    chn_name: str = '公司实际控制人'
    
    business_unique: str = 'CompanyCode,InfoPublDate,EndDate,ControllerName'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.收录根据上市公司在招投说明书、定期报告、及临时公告中披露的实际控制人结构图判断的上市公司实际控制人信息。
2.目前只处理实际控制人有变动的数据，下期和本期相比如无变化，则不做处理。
3.数据范围：2004-12-31至今
4.信息来源：招股说明书、上市公告书、定报、临时公告等。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ActualController', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    PermanentResidency: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ActualController', column_name='PermanentResidency', column_type='varchar(100)', nullable=False, chn_name='永久境外居留权')
    """永久境外居留权:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ActualController', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ActualController', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ActualController', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ActualController', column_name='InfoPublDate', column_type='datetime', nullable=True, chn_name='信息发布日期')
    """信息发布日期:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ActualController', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    ControllerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ActualController', column_name='ControllerCode', column_type='int', nullable=False, chn_name='实际控制人代码')
    """实际控制人代码:实际控制人代码（ControllerCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到实际控制人的名称，企业性质等信息。"""

    ControllerName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ActualController', column_name='ControllerName', column_type='varchar(120)', nullable=True, chn_name='实际控制人')
    """实际控制人:"""

    EconomicNature: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ActualController', column_name='EconomicNature', column_type='int', nullable=False, chn_name='实际控制人经济性质')
    """实际控制人经济性质:实际控制人经济性质(EconomicNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1581，得到实际控制人经济性质的具体描述：1-中央企业，2-地方国有企业，3-民营企业，4-集体企业，5-大学，6-外资，7-工会，99-其它。"""

    NationalityCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ActualController', column_name='NationalityCode', column_type='int', nullable=False, chn_name='国籍代码')
    """国籍代码:国籍代码(NationalityCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1023，得到国籍代码的具体描述：3-港澳台，4-中东地区，7-国际，100-亚洲，101-阿富汗，102-巴林，103-孟加拉国，104-不丹，105-文莱，106-缅甸，107-柬埔寨，108-塞浦路斯，109-朝鲜，110-中国香港，111-印度..."""

    NationalityDesc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ActualController', column_name='NationalityDesc', column_type='varchar(50)', nullable=False, chn_name='国籍描述')
    """国籍描述:"""

