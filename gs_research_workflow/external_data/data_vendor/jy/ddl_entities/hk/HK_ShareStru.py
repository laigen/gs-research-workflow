# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_ShareStru(SQLTableEntity):
    name: str = 'HK_ShareStru'
    
    chn_name: str = '港股股本结构'
    
    business_unique: str = 'CompanyCode,EndDate'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.介绍港股的具体股本结构信息，包括股票面值、普通股、优先股、股本变动原因等内容。记录有港股股本历次变动的信息，和其他市场存有的公司股票。
2.数据范围：1999年至今。
3.信息来源：港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    AuthorizedCapitalComShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='AuthorizedCapitalComShare', column_type='decimal(19,4)', nullable=False, chn_name='法定股本(元)')
    """法定股本(元):"""

    AuthorizedSharesComShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='AuthorizedSharesComShare', column_type='decimal(18,2)', nullable=False, chn_name='法定股数(股)')
    """法定股数(股):"""

    PaidUpCapitalComShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='PaidUpCapitalComShare', column_type='decimal(19,4)', nullable=False, chn_name='实收股本(元)')
    """实收股本(元):"""

    PaidUpSharesComShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='PaidUpSharesComShare', column_type='decimal(18,2)', nullable=False, chn_name='实收股数(股)')
    """实收股数(股):"""

    ListedShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='ListedShares', column_type='decimal(18,2)', nullable=False, chn_name='#已上市(股)')
    """#已上市(股):"""

    UnlistedShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='UnlistedShares', column_type='decimal(18,2)', nullable=False, chn_name='#待上市(股)')
    """#待上市(股):"""

    NotHKShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='NotHKShares', column_type='decimal(18,2)', nullable=False, chn_name='#非港股(股)')
    """#非港股(股):"""

    AuthorizedCapitalPreShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='AuthorizedCapitalPreShare', column_type='decimal(19,4)', nullable=False, chn_name='法定股本(元)')
    """法定股本(元):"""

    AuthorizedSharesPreShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='AuthorizedSharesPreShare', column_type='decimal(18,2)', nullable=False, chn_name='法定股数(股)')
    """法定股数(股):"""

    PaidUpCapitalPreShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='PaidUpCapitalPreShare', column_type='decimal(19,4)', nullable=False, chn_name='实收股本(元)')
    """实收股本(元):"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到港股的交易代码、简称等。"""

    PaidUpSharesPreShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='PaidUpSharesPreShare', column_type='decimal(18,2)', nullable=False, chn_name='实收股数(股)')
    """实收股数(股):"""

    AuthorizedCapitalTotal: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='AuthorizedCapitalTotal', column_type='decimal(19,4)', nullable=False, chn_name='法定股本(元)')
    """法定股本(元):"""

    AuthorizedSharesTotal: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='AuthorizedSharesTotal', column_type='decimal(18,2)', nullable=False, chn_name='法定股数(股)')
    """法定股数(股):"""

    PaidUpCapitalTotal: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='PaidUpCapitalTotal', column_type='decimal(19,4)', nullable=False, chn_name='实收股本(元)')
    """实收股本(元):"""

    PaidUpSharesTotal: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='PaidUpSharesTotal', column_type='decimal(18,2)', nullable=False, chn_name='实收股数(股)')
    """实收股数(股):"""

    PaidUpSharesChgComShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='PaidUpSharesChgComShare', column_type='decimal(18,2)', nullable=False, chn_name='普通股实收变动股数(股)')
    """普通股实收变动股数(股):"""

    PaidUpSharesChgPreShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='PaidUpSharesChgPreShare', column_type='decimal(18,2)', nullable=False, chn_name='优先股实收变动股数(股)')
    """优先股实收变动股数(股):"""

    ChangeType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='ChangeType', column_type='int', nullable=False, chn_name='股本变动原因类别')
    """股本变动原因类别:"""

    ChangeReason: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='ChangeReason', column_type='varchar(500)', nullable=False, chn_name='股本变动原因说明')
    """股本变动原因说明:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='修改日期')
    """修改日期:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    AuthCapitalComShareA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='AuthCapitalComShareA', column_type='decimal(19,2)', nullable=False, chn_name='A类法定股本(元)')
    """A类法定股本(元):"""

    AuthCapitalComShareB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='AuthCapitalComShareB', column_type='decimal(19,2)', nullable=False, chn_name='B类法定股本(元)')
    """B类法定股本(元):"""

    AuthSharesComShareA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='AuthSharesComShareA', column_type='decimal(18,0)', nullable=False, chn_name='A类法定股数(股)')
    """A类法定股数(股):"""

    AuthSharesComShareB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='AuthSharesComShareB', column_type='decimal(18,0)', nullable=False, chn_name='B类法定股数(股)')
    """B类法定股数(股):"""

    PaidUpCapitalComShareA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='PaidUpCapitalComShareA', column_type='decimal(19,2)', nullable=False, chn_name='A类实收股本(元)')
    """A类实收股本(元):"""

    PaidUpCapitalComShareB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='PaidUpCapitalComShareB', column_type='decimal(19,2)', nullable=False, chn_name='B类实收股本(元)')
    """B类实收股本(元):"""

    PaidUpSharesComShareA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='PaidUpSharesComShareA', column_type='decimal(18,0)', nullable=False, chn_name='A类实收股数(股)')
    """A类实收股数(股):"""

    PaidUpSharesComShareB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='PaidUpSharesComShareB', column_type='decimal(18,0)', nullable=False, chn_name='B类实收股数(股)')
    """B类实收股数(股):"""

    ListedSharesA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='ListedSharesA', column_type='decimal(18,0)', nullable=False, chn_name='#A类已上市(股)')
    """#A类已上市(股):"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='InfoSource', column_type='varchar(100)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    ListedSharesB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='ListedSharesB', column_type='decimal(18,0)', nullable=False, chn_name='#B类已上市(股)')
    """#B类已上市(股):"""

    UnlistedSharesA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='UnlistedSharesA', column_type='decimal(18,0)', nullable=False, chn_name='#A类待上市(股)')
    """#A类待上市(股):"""

    UnlistedSharesB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='UnlistedSharesB', column_type='decimal(18,0)', nullable=False, chn_name='#B类待上市(股)')
    """#B类待上市(股):"""

    PaidUpShChgComShareA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='PaidUpShChgComShareA', column_type='decimal(18,0)', nullable=False, chn_name='A类普通股实收变动股数(股)')
    """A类普通股实收变动股数(股):"""

    PaidUpShChgComShareB: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='PaidUpShChgComShareB', column_type='decimal(18,0)', nullable=False, chn_name='B类普通股实收变动股数(股)')
    """B类普通股实收变动股数(股):"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='EndDate', column_type='datetime', nullable=False, chn_name='截止日期')
    """截止日期:"""

    ParValueUnitComShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='ParValueUnitComShare', column_type='int', nullable=False, chn_name='普通股面值单位')
    """普通股面值单位:普通股面值单位(ParValueUnitComShare)与(CT_SystemConst)表中的DM字段关联，令LB = 1068，得到普通股面值单位的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，117..."""

    ParValueComShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='ParValueComShare', column_type='decimal(19,10)', nullable=False, chn_name='普通股面值(元/股)')
    """普通股面值(元/股):"""

    ParValueUnitPreShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='ParValueUnitPreShare', column_type='int', nullable=False, chn_name='优先股面值单位')
    """优先股面值单位:优先股面值单位(ParValueUnitPreShare)与(CT_SystemConst)表中的DM字段关联，令LB = 1068，得到优先股面值单位的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，117..."""

    ParValuePreShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_ShareStru', column_name='ParValuePreShare', column_type='decimal(19,10)', nullable=False, chn_name='优先股面值(元/股)')
    """优先股面值(元/股):"""

