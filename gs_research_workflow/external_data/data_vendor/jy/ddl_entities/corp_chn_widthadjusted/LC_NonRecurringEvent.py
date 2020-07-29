# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_NonRecurringEvent(SQLTableEntity):
    name: str = 'LC_NonRecurringEvent'
    
    chn_name: str = '公司非经常性损益'
    
    business_unique: str = 'CompanyCode,InfoPublDate,EndDate,IfAdjusted,ItemName,ReportPeriord'
    
    refresh_freq: str = """季更新"""
    
    comment: str = """1.收录定期报告中的非经常性损益数据，包括项目名称、项目类别、金额、计价货币等内容。
2.数据范围：2003-12-31至今
3.信息来源：招股意向书、定报、审计报告等"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_NonRecurringEvent', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    ItemCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_NonRecurringEvent', column_name='ItemCode', column_type='int', nullable=False, chn_name='项目类别')
    """项目类别:项目类别(ItemCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1041，得到项目类别的具体描述：10100-货币资金，10110-现金，10130-银行存款，10150-非银行存款，10190-其他货币资金，10200-短期投资，10210-短期股票投资，10211-上市股票投资，10213-非上市股票投资，10220-短期债..."""

    CurrencyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_NonRecurringEvent', column_name='CurrencyCode', column_type='int', nullable=False, chn_name='计价货币')
    """计价货币:计价货币(CurrencyCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1068，得到计价货币的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，1170-约旦第纳尔，1180-科..."""

    Value: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_NonRecurringEvent', column_name='Value', column_type='decimal(19,4)', nullable=False, chn_name='金额(元)')
    """金额(元):"""

    Note: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_NonRecurringEvent', column_name='Note', column_type='text', nullable=False, chn_name='附注(如适用)')
    """附注(如适用):"""

    Remark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_NonRecurringEvent', column_name='Remark', column_type='varchar(400)', nullable=False, chn_name='备注说明')
    """备注说明:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_NonRecurringEvent', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_NonRecurringEvent', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_NonRecurringEvent', column_name='InfoPublDate', column_type='datetime', nullable=True, chn_name='信息发布日期')
    """信息发布日期:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_NonRecurringEvent', column_name='InfoSource', column_type='varchar(50)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    BulletinType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_NonRecurringEvent', column_name='BulletinType', column_type='int', nullable=False, chn_name='公告类别')
    """公告类别:公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311，得到公告类别的具体描述：10-发行上市书，20-定期报告，30-业绩快报，50-章程制度，70-临时公告，90-交易所通报，91-交易所临时停(复)牌公告，99-其他。"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_NonRecurringEvent', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_NonRecurringEvent', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    ReportPeriord: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_NonRecurringEvent', column_name='ReportPeriord', column_type='int', nullable=False, chn_name='报告期类别')
    """报告期类别:报告期类别(ReportPeriord)与(CT_SystemConst)表中的DM字段关联，令LB = 1188，得到报告期类别的具体描述：1-是，2-否，3-前，4-否(7-9月)，5-是(7-9月)，6-一季末调整，7-二季末调整，8-三季末调整，9-年报调整，10-三季末调整（7~9月），11-调整前，21-本期，22-上期，23-上上期。"""

    IfAdjusted: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_NonRecurringEvent', column_name='IfAdjusted', column_type='int', nullable=True, chn_name='是否调整')
    """是否调整:是否调整(IfAdjusted)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM IN (1,2)，得到是否调整的具体描述：1-是，2-否。"""

    ItemName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_NonRecurringEvent', column_name='ItemName', column_type='varchar(250)', nullable=True, chn_name='项目名称')
    """项目名称:"""

