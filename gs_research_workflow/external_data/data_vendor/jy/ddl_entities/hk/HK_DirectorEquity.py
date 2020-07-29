# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_DirectorEquity(SQLTableEntity):
    name: str = 'HK_DirectorEquity'
    
    chn_name: str = '港股董事权益'
    
    business_unique: str = 'CompanyCode,EndDate,DirectorName,EquityType,EquityCharacter'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.记录港股董事的相关权益信息，包括董事名称、权益性质、股东身份、以不同身份持有的股票数量等内容。
2.数据范围：2001年至今。
3.信息来源：港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DirectorEquity', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    EquityStatus: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DirectorEquity', column_name='EquityStatus', column_type='int', nullable=False, chn_name='权益身份')
    """权益身份:"""

    EquityStatusDesc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DirectorEquity', column_name='EquityStatusDesc', column_type='varchar(200)', nullable=False, chn_name='权益身份描述')
    """权益身份描述:"""

    RelatingEquityStatus: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DirectorEquity', column_name='RelatingEquityStatus', column_type='int', nullable=False, chn_name='相关权益身份')
    """相关权益身份:"""

    RelatingEquityStatusDesc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DirectorEquity', column_name='RelatingEquityStatusDesc', column_type='varchar(200)', nullable=False, chn_name='相关权益身份描述')
    """相关权益身份描述:"""

    EquityVolume: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DirectorEquity', column_name='EquityVolume', column_type='decimal(18,2)', nullable=False, chn_name='权益总数(股)')
    """权益总数(股):"""

    RatioInTotalShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DirectorEquity', column_name='RatioInTotalShares', column_type='decimal(18,8)', nullable=False, chn_name='占已发行股份比例')
    """占已发行股份比例:"""

    HoldSum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DirectorEquity', column_name='HoldSum', column_type='decimal(18,2)', nullable=False, chn_name='1、股份权益总数(股)')
    """1、股份权益总数(股):"""

    HSInTotalShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DirectorEquity', column_name='HSInTotalShares', column_type='decimal(18,8)', nullable=False, chn_name='占已发行股份比例')
    """占已发行股份比例:"""

    PersonalEquity: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DirectorEquity', column_name='PersonalEquity', column_type='decimal(18,2)', nullable=False, chn_name='#个人权益(股)')
    """#个人权益(股):"""

    FamilyEquity: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DirectorEquity', column_name='FamilyEquity', column_type='decimal(18,2)', nullable=False, chn_name='#家族权益(股)')
    """#家族权益(股):"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DirectorEquity', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到港股的交易代码、简称等。"""

    CompanyEquity: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DirectorEquity', column_name='CompanyEquity', column_type='decimal(18,2)', nullable=False, chn_name='#公司权益(股)')
    """#公司权益(股):"""

    OtherEquity: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DirectorEquity', column_name='OtherEquity', column_type='decimal(18,2)', nullable=False, chn_name='#其他权益(股)')
    """#其他权益(股):"""

    RelatingEquityHoldSum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DirectorEquity', column_name='RelatingEquityHoldSum', column_type='decimal(18,2)', nullable=False, chn_name='2、相关股份权益总数(股)')
    """2、相关股份权益总数(股):"""

    REHSInTotalShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DirectorEquity', column_name='REHSInTotalShares', column_type='decimal(18,8)', nullable=False, chn_name='占已发行股份比例')
    """占已发行股份比例:"""

    StockrightEquity: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DirectorEquity', column_name='StockrightEquity', column_type='decimal(18,2)', nullable=False, chn_name='#购股权权益(股)')
    """#购股权权益(股):"""

    WarrantEquity: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DirectorEquity', column_name='WarrantEquity', column_type='decimal(18,2)', nullable=False, chn_name='#认股权证权益(股)')
    """#认股权证权益(股):"""

    ConvertibleBondEquity: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DirectorEquity', column_name='ConvertibleBondEquity', column_type='decimal(18,2)', nullable=False, chn_name='#可换股债券权益(股)')
    """#可换股债券权益(股):"""

    OtherRelatingEquity: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DirectorEquity', column_name='OtherRelatingEquity', column_type='decimal(18,2)', nullable=False, chn_name='#其他相关权益(股)')
    """#其他相关权益(股):"""

    Statement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DirectorEquity', column_name='Statement', column_type='text', nullable=False, chn_name='备注')
    """备注:"""

    InsertTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DirectorEquity', column_name='InsertTime', column_type='datetime', nullable=False, chn_name='发布时间')
    """发布时间:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DirectorEquity', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DirectorEquity', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='修改日期')
    """修改日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DirectorEquity', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DirectorEquity', column_name='EndDate', column_type='datetime', nullable=False, chn_name='截止日期')
    """截止日期:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DirectorEquity', column_name='InfoSource', column_type='varchar(100)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    DirectorName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DirectorEquity', column_name='DirectorName', column_type='varchar(200)', nullable=False, chn_name='董事名称')
    """董事名称:"""

    EquityType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DirectorEquity', column_name='EquityType', column_type='int', nullable=False, chn_name='权益类别')
    """权益类别:权益类别(EquityType)与(CT_SystemConst)表中的DM字段关联，令LB = 1341，得到权益类别的具体描述：10-普通股，20-优先股，30-债权证，40-普通股-A类，50-普通股-B类。"""

    EquityCharacter: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DirectorEquity', column_name='EquityCharacter', column_type='int', nullable=False, chn_name='权益性质')
    """权益性质:权益性质(EquityCharacter)与(CT_SystemConst)表中的DM字段关联，令LB = 1342，得到权益性质的具体描述：1-好仓，3-淡仓，9-可供借出股份。"""

    Unit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_DirectorEquity', column_name='Unit', column_type='int', nullable=False, chn_name='单位')
    """单位:单位(Unit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068，得到单位的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，1170-约旦第纳尔，1180-科威特第纳尔，1190-阿..."""

