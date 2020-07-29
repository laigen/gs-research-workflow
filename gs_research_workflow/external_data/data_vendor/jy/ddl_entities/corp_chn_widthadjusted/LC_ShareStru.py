# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_ShareStru(SQLTableEntity):
    name: str = 'LC_ShareStru'
    
    chn_name: str = '公司股本结构变动'
    
    business_unique: str = 'CompanyCode,EndDate'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.收录上市公司股本结构历史变动情况。其中：标注“披露”的字段为公司公告原始披露，标注“计算”的字段为聚源依据股权登记日，并且考虑高管股锁定的实际情况计算所得的股本结构。
2.数据范围：1990-12-10至今
3.信息来源：招股说明书、上市公告书、定报、临时公告等。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    RestrictedAShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='RestrictedAShares', column_type='decimal(16,0)', nullable=False, chn_name='1.1)有限售条件的流通A股(股)(计算)')
    """1.1)有限售条件的流通A股(股)(计算):"""

    NonResiSharesJY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='NonResiSharesJY', column_type='decimal(16,0)', nullable=False, chn_name='1.2)无限售条件流通A股(股)(计算)')
    """1.2)无限售条件流通A股(股)(计算):"""

    RestrictAShareP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='RestrictAShareP', column_type='decimal(16,0)', nullable=False, chn_name='1.3)有限售条件的流通A股(股)(披露)')
    """1.3)有限售条件的流通A股(股)(披露):"""

    NonRestrictedShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='NonRestrictedShares', column_type='decimal(16,0)', nullable=False, chn_name='1.4)无限售条件流通A股(股)(披露)')
    """1.4)无限售条件流通A股(股)(披露):"""

    NonListedShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='NonListedShares', column_type='decimal(16,0)', nullable=False, chn_name='2)未流通A股(股)')
    """2)未流通A股(股):"""

    BsharesTotal: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='BsharesTotal', column_type='decimal(16,0)', nullable=False, chn_name='2.B股(股)')
    """2.B股(股):"""

    ListedBShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='ListedBShares', column_type='decimal(16,0)', nullable=False, chn_name='1)流通B股(股)')
    """1)流通B股(股):"""

    NonResiBShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='NonResiBShares', column_type='decimal(16,0)', nullable=False, chn_name='其中:无限售流通B股')
    """其中:无限售流通B股:"""

    NonListedRestrictedBShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='NonListedRestrictedBShares', column_type='decimal(16,0)', nullable=False, chn_name='2)未流通B股(股)')
    """2)未流通B股(股):"""

    Hshares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='Hshares', column_type='decimal(16,0)', nullable=False, chn_name='3.H股(股)')
    """3.H股(股):"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。"""

    OtherFloatShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='OtherFloatShares', column_type='decimal(16,0)', nullable=False, chn_name='4.海外上市股(股)')
    """4.海外上市股(股):"""

    Sshares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='Sshares', column_type='decimal(16,0)', nullable=False, chn_name='1)S股(股)')
    """1)S股(股):"""

    Nshares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='Nshares', column_type='decimal(16,0)', nullable=False, chn_name='2)N股(股)')
    """2)N股(股):"""

    Dshares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='Dshares', column_type='decimal(16,0)', nullable=False, chn_name='3)D股(股)')
    """3)D股(股):"""

    SRUnlistedShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='SRUnlistedShare', column_type='decimal(16,0)', nullable=False, chn_name='增发、配股未上市股份(股)(披露)')
    """增发、配股未上市股份(股)(披露):"""

    RestrictedShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='RestrictedShares', column_type='decimal(16,0)', nullable=False, chn_name='有限售条件的流通股(股)')
    """有限售条件的流通股(股):"""

    StateHolding: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='StateHolding', column_type='decimal(16,0)', nullable=False, chn_name='A.国家持股(股)')
    """A.国家持股(股):"""

    SLegalPersonHolding: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='SLegalPersonHolding', column_type='decimal(16,0)', nullable=False, chn_name='B.国有法人持股(股)')
    """B.国有法人持股(股):"""

    OtherDCapitalHolding: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='OtherDCapitalHolding', column_type='decimal(16,0)', nullable=False, chn_name='C.其他内资持股(股)')
    """C.其他内资持股(股):"""

    DLegalPersonHolding: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='DLegalPersonHolding', column_type='decimal(16,0)', nullable=False, chn_name='a.境内法人持股(股)')
    """a.境内法人持股(股):"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='InfoSource', column_type='varchar(50)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    DNaturalPersonHolding: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='DNaturalPersonHolding', column_type='decimal(16,0)', nullable=False, chn_name='b.境内自然人持股(股)')
    """b.境内自然人持股(股):"""

    ManagementShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='ManagementShares', column_type='decimal(16,0)', nullable=False, chn_name='##高管股(股)')
    """##高管股(股):"""

    ForeignHolding: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='ForeignHolding', column_type='decimal(16,0)', nullable=False, chn_name='D.外资持股(股)')
    """D.外资持股(股):"""

    FLegalPersonHolding: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='FLegalPersonHolding', column_type='decimal(16,0)', nullable=False, chn_name='其中:境外法人持股(股)')
    """其中:境外法人持股(股):"""

    FNaturalPersonHolding: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='FNaturalPersonHolding', column_type='decimal(16,0)', nullable=False, chn_name='其中:境外自然人持股(股)')
    """其中:境外自然人持股(股):"""

    OtherRestrictedShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='OtherRestrictedShares', column_type='decimal(16,0)', nullable=False, chn_name='E.其他有限售(股)')
    """E.其他有限售(股):"""

    PromoterShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='PromoterShares', column_type='decimal(16,0)', nullable=False, chn_name='1.发起人股(股)')
    """1.发起人股(股):"""

    StateShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='StateShares', column_type='decimal(16,0)', nullable=False, chn_name='国家股(股)')
    """国家股(股):"""

    SLegalPersonShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='SLegalPersonShares', column_type='decimal(16,0)', nullable=False, chn_name='其中:国有法人股(股)')
    """其中:国有法人股(股):"""

    DLegalPersonShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='DLegalPersonShares', column_type='decimal(16,0)', nullable=False, chn_name='境内法人股(股)')
    """境内法人股(股):"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    FLegalPersonShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='FLegalPersonShares', column_type='decimal(16,0)', nullable=False, chn_name='外资法人股(股)')
    """外资法人股(股):"""

    OtherPromoterShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='OtherPromoterShares', column_type='decimal(16,0)', nullable=False, chn_name='其它发起人股(股)')
    """其它发起人股(股):"""

    RaisedLPShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='RaisedLPShares', column_type='decimal(16,0)', nullable=False, chn_name='2.募集法人股(股)')
    """2.募集法人股(股):"""

    RaisedSLPShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='RaisedSLPShares', column_type='decimal(16,0)', nullable=False, chn_name='其中:募集国有法人股(股)')
    """其中:募集国有法人股(股):"""

    NaturalPersonHoldLPShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='NaturalPersonHoldLPShares', column_type='decimal(16,0)', nullable=False, chn_name='3.自然人法人股(股)')
    """3.自然人法人股(股):"""

    StaffShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='StaffShares', column_type='decimal(16,0)', nullable=False, chn_name='4.职工股(股)')
    """4.职工股(股):"""

    RightsIssueTransferred: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='RightsIssueTransferred', column_type='decimal(16,0)', nullable=False, chn_name='5.转配股(股)')
    """5.转配股(股):"""

    PreferredAndOtherShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='PreferredAndOtherShares', column_type='decimal(16,0)', nullable=False, chn_name='6.优先股及其他(股)')
    """6.优先股及其他(股):"""

    PreferredShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='PreferredShares', column_type='decimal(16,0)', nullable=False, chn_name='其中:优先股(股)')
    """其中:优先股(股):"""

    OtherFNonListedShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='OtherFNonListedShares', column_type='decimal(16,0)', nullable=False, chn_name='7.其他外资股(股)')
    """7.其他外资股(股):"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    FloatShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='FloatShare', column_type='decimal(16,0)', nullable=False, chn_name='流通股份(股)')
    """流通股份(股):"""

    AFloatListed: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='AFloatListed', column_type='decimal(16,0)', nullable=False, chn_name='1)已上市流通A股(包含高管股)(股)')
    """1)已上市流通A股(包含高管股)(股):"""

    StategicInvestorShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='StategicInvestorShares', column_type='decimal(16,0)', nullable=False, chn_name='2)战略投资者配售持股(股)')
    """2)战略投资者配售持股(股):"""

    CommonLPShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='CommonLPShares', column_type='decimal(16,0)', nullable=False, chn_name='3)一般法人配售持股(股)')
    """3)一般法人配售持股(股):"""

    MutualFundShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='MutualFundShares', column_type='decimal(16,0)', nullable=False, chn_name='4)基金配售持股(股)')
    """4)基金配售持股(股):"""

    AdditionalIssueUnlisted: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='AdditionalIssueUnlisted', column_type='decimal(16,0)', nullable=False, chn_name='5)增发未上市(股)')
    """5)增发未上市(股):"""

    RightsIssueUnlisted: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='RightsIssueUnlisted', column_type='decimal(16,0)', nullable=False, chn_name='6)配股未上市(股)')
    """6)配股未上市(股):"""

    OtherAFloatShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='OtherAFloatShares', column_type='decimal(16,0)', nullable=False, chn_name='7)其他流通股份(股)')
    """7)其他流通股份(股):"""

    RestrictedAFloatShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='RestrictedAFloatShares', column_type='decimal(16,0)', nullable=False, chn_name='8)有限售流通A股(股)')
    """8)有限售流通A股(股):"""

    RestrinctStaffShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='RestrinctStaffShares', column_type='decimal(16,0)', nullable=False, chn_name='其中:有限售流通股中职工股(股)')
    """其中:有限售流通股中职工股(股):"""

    PerValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='PerValue', column_type='decimal(19,4)', nullable=False, chn_name='每股面值(元)')
    """每股面值(元):"""

    Bshares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='Bshares', column_type='decimal(16,0)', nullable=False, chn_name='B股_旧(股)')
    """B股_旧(股):"""

    NonListedBShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='NonListedBShares', column_type='decimal(16,0)', nullable=False, chn_name='其中:未流通B股_旧')
    """其中:未流通B股_旧:"""

    RestrictedBFloatShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='RestrictedBFloatShares', column_type='decimal(16,0)', nullable=False, chn_name='有限售B股(股)')
    """有限售B股(股):"""

    ForeignHoldingAshares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='ForeignHoldingAshares', column_type='decimal(16,0)', nullable=False, chn_name='外资持A股(股)')
    """外资持A股(股):"""

    ChangeType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='ChangeType', column_type='int', nullable=False, chn_name='股本变动原因类别')
    """股本变动原因类别:股本变动原因类别(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1022，得到股本变动原因类别的具体描述：1-A股发行，2-B股发行，3-A股发行基金配售上市，4-A股发行法人配售上市，6-A股上市，7-B股上市，8-送转股，10-配股除权，11-配股上市，12-转配股上市，17-非公开增发A股上市，18-非公开增发..."""

    ChangeTypeDetail: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='ChangeTypeDetail', column_type='int', nullable=False, chn_name='股本变动原因类别明细')
    """股本变动原因类别明细:"""

    ChangeReason: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='ChangeReason', column_type='varchar(255)', nullable=False, chn_name='股本变动原因说明')
    """股本变动原因说明:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    TotalShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='TotalShares', column_type='decimal(16,0)', nullable=False, chn_name='总股本(股)')
    """总股本(股):"""

    Ashares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='Ashares', column_type='decimal(16,0)', nullable=False, chn_name='1.A股(股)')
    """1.A股(股):"""

    AFloats: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_ShareStru', column_name='AFloats', column_type='decimal(16,0)', nullable=False, chn_name='1)流通A股(股)')
    """1)流通A股(股):"""

