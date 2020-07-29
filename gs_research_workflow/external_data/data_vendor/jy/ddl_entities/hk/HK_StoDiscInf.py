# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_StoDiscInf(SQLTableEntity):
    name: str = 'HK_StoDiscInf'
    
    chn_name: str = '港股披露权益信息'
    
    business_unique: str = '无'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.记录港股披露权益的基础信息，包括股份类型、持有人名称、持有性质、事件日期、持有人知悉日期等数据内容。该表为港股披露权益系列表的主表。
2.数据范围：1997年至今。
3.信息来源：港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscInf', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    EventDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscInf', column_name='EventDate', column_type='datetime', nullable=True, chn_name='事件日期')
    """事件日期:"""

    HolderNotcDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscInf', column_name='HolderNotcDate', column_type='datetime', nullable=False, chn_name='持有人知悉日期')
    """持有人知悉日期:"""

    SN: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscInf', column_name='SN', column_type='int', nullable=True, chn_name='序号')
    """序号:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscInf', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscInf', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    Companyode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscInf', column_name='Companyode', column_type='int', nullable=False, chn_name='公司代码')
    """公司代码:"""

    CompanyName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscInf', column_name='CompanyName', column_type='varchar(200)', nullable=False, chn_name='公司名称')
    """公司名称:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscInf', column_name='InnerCode', column_type='int', nullable=True, chn_name='港股内部代码')
    """港股内部代码:港股内部代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。"""

    SecuCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscInf', column_name='SecuCode', column_type='varchar(10)', nullable=False, chn_name='证券代码')
    """证券代码:"""

    ShareCategory: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscInf', column_name='ShareCategory', column_type='varchar(200)', nullable=False, chn_name='股份类型')
    """股份类型:"""

    IssuedShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscInf', column_name='IssuedShares', column_type='decimal(18,2)', nullable=False, chn_name='已发行股份(股)')
    """已发行股份(股):"""

    ChiHolderName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscInf', column_name='ChiHolderName', column_type='varchar(200)', nullable=False, chn_name='持有人姓名')
    """持有人姓名:"""

    HolderCharacter: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_StoDiscInf', column_name='HolderCharacter', column_type='int', nullable=True, chn_name='持有人性质')
    """持有人性质:持有人性质(HolderCharacter)与(CT_SystemConst)表中的DM字段关联，令LB=1700，得到持有人性质的具体描述：101-董事，102-大股东，103-其他（含最高行政人員），104-个人大股东，105-法团大股东，106-董事-上市法团股份，107-董事-相联法团股份，108-董事-上市法团债券证，109-董事-相联法团债券证。"""

