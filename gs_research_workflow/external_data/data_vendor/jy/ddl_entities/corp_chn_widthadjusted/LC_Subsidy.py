# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_Subsidy(SQLTableEntity):
    name: str = 'LC_Subsidy'
    
    chn_name: str = '公司非常补贴明细'
    
    business_unique: str = '无'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.收录上市公司公告中披露的非常补贴等重大事项描述说明。
2.数据范围：2001年-至今
3.信息来源：上市公司公告"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Subsidy', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    NewestAdvance: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Subsidy', column_name='NewestAdvance', column_type='varchar(200)', nullable=False, chn_name='最新进展状态描述')
    """最新进展状态描述:"""

    EventSubject: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Subsidy', column_name='EventSubject', column_type='int', nullable=False, chn_name='事件主体')
    """事件主体:事件主体(EventSubject)与(CT_SystemConst)表中的DM字段关联，令LB = 1246，得到事件主体的具体描述：1-上市公司，2-下属公司，3-公司股东，4-债券发行人。"""

    EventProcedure: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Subsidy', column_name='EventProcedure', column_type='int', nullable=False, chn_name='事件进程')
    """事件进程:事件进程(EventProcedure)与(CT_SystemConst)表中的DM字段关联，令LB = 1059，得到事件进程的具体描述：1000-意向，1001-预案，1004-决案，1007-否决，1010-申请，1013-批准，1016-未实施终止，1019-实施中，1022-实施完成，1025-解除，1028-到期，1041-续签，1043-部分续..."""

    ActionWays: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Subsidy', column_name='ActionWays', column_type='int', nullable=False, chn_name='行为方式')
    """行为方式:行为方式(ActionWays)与(CT_SystemConst)表中的DM字段关联，令LB = 1063，得到行为方式的具体描述：1001-借入，1003-贷出，1005-银行授信，1007-借入计划额度，1009-承兑汇票，1011-票据贴现，1013-进出口押汇，1099-其他借贷，1201-提供担保，1203-接受担保，1204-提供反担保，1205..."""

    CurrencyUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Subsidy', column_name='CurrencyUnit', column_type='int', nullable=False, chn_name='货币单位')
    """货币单位:货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068，得到货币单位的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，1170-约旦第纳尔，1180-科..."""

    SubjectName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Subsidy', column_name='SubjectName', column_type='varchar(100)', nullable=False, chn_name='事件主体名称')
    """事件主体名称:"""

    SubjectCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Subsidy', column_name='SubjectCode', column_type='int', nullable=False, chn_name='事件主体企业编号')
    """事件主体企业编号:事件主体企业编号(SubjectCode)和机构基本资料表(CompanyCode)关联"""

    SubjectAssociation: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Subsidy', column_name='SubjectAssociation', column_type='int', nullable=False, chn_name='与上市公司关联关系')
    """与上市公司关联关系:与上市公司关联关系(SubjectAssociation)与(CT_SystemConst)表中的DM字段关联，令LB = 1036，得到与上市公司关联关系的具体描述：1-本公司，2-母公司，3-控股股东，4-非控股股东，5-兄弟企业，8-间接非控股股东，9-同一领导人、亲属关系，10-下属子公司、参股公司，11-项目合作合资方，12-其他关联关系，51-间..."""

    ObjectName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Subsidy', column_name='ObjectName', column_type='varchar(100)', nullable=False, chn_name='交易对象名称')
    """交易对象名称:"""

    ObjectCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Subsidy', column_name='ObjectCode', column_type='int', nullable=False, chn_name='交易对象企业编号')
    """交易对象企业编号:交易对象企业编号(ObjectCode)和机构基本资料表(CompanyCode)关联"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Subsidy', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。"""

    ObjectAssociation: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Subsidy', column_name='ObjectAssociation', column_type='int', nullable=False, chn_name='与上市公司关联关系')
    """与上市公司关联关系:与上市公司关联关系(ObjectAssociation)与(CT_SystemConst)表中的DM字段关联，令LB = 1036，得到与上市公司关联关系的具体描述：1-本公司，2-母公司，3-控股股东，4-非控股股东，5-兄弟企业，8-间接非控股股东，9-同一领导人、亲属关系，10-下属子公司、参股公司，11-项目合作合资方，12-其他关联关系，51-间接..."""

    AgreementDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Subsidy', column_name='AgreementDate', column_type='datetime', nullable=False, chn_name='协议签署日期')
    """协议签署日期:"""

    IfEnded: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Subsidy', column_name='IfEnded', column_type='int', nullable=False, chn_name='是否终止')
    """是否终止:是否终止（IfEnded），该字段固定以下常量：0-否；1-是"""

    Note: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Subsidy', column_name='Note', column_type='varchar(300)', nullable=False, chn_name='备注')
    """备注:"""

    SubsidyTaxType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Subsidy', column_name='SubsidyTaxType', column_type='int', nullable=False, chn_name='税负类别')
    """税负类别:"""

    SubsidySum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Subsidy', column_name='SubsidySum', column_type='decimal(19,4)', nullable=False, chn_name='补贴总金额(元)')
    """补贴总金额(元):"""

    ApportionTerm: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Subsidy', column_name='ApportionTerm', column_type='decimal(18,4)', nullable=False, chn_name='分摊年限(年)')
    """分摊年限(年):"""

    SubsidyBeginDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Subsidy', column_name='SubsidyBeginDate', column_type='datetime', nullable=False, chn_name='补贴实现起始日')
    """补贴实现起始日:"""

    SunsidyEndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Subsidy', column_name='SunsidyEndDate', column_type='datetime', nullable=False, chn_name='补贴实现截止日')
    """补贴实现截止日:"""

    LatestReceivedSubsidySum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Subsidy', column_name='LatestReceivedSubsidySum', column_type='decimal(19,4)', nullable=False, chn_name='本次收到补贴金额(元)')
    """本次收到补贴金额(元):"""

    InitialInfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Subsidy', column_name='InitialInfoPublDate', column_type='datetime', nullable=False, chn_name='首次信息发布日期')
    """首次信息发布日期:"""

    TotalReceivedSubsidySum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Subsidy', column_name='TotalReceivedSubsidySum', column_type='decimal(19,4)', nullable=False, chn_name='累计收到补贴金额(元)')
    """累计收到补贴金额(元):"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Subsidy', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='修改日期')
    """修改日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Subsidy', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Subsidy', column_name='InfoPublDate', column_type='datetime', nullable=True, chn_name='信息发布日期')
    """信息发布日期:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Subsidy', column_name='InfoSource', column_type='varchar(50)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    AnnouncementType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Subsidy', column_name='AnnouncementType', column_type='int', nullable=False, chn_name='公告类型')
    """公告类型:公告类型(AnnouncementType)与(CT_SystemConst)表中的DM字段关联，令LB = 1109，得到公告类型的具体描述：1-董事会公告，2-股东大会公告，3-监事会公告，4-公司公告，5-法律意见书，6-财务报告，7-中国证监会公告，8-交易所公告，9-中介机构公告，10-基金投资组合公告，11-回访报告，12-独立董事声明，13-债..."""

    DisclosureMethod: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Subsidy', column_name='DisclosureMethod', column_type='int', nullable=False, chn_name='披露方式')
    """披露方式:披露方式(DisclosureMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1221，得到披露方式的具体描述：1-正常披露，2-事后披露。"""

    EventContent: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Subsidy', column_name='EventContent', column_type='text', nullable=False, chn_name='事件内容')
    """事件内容:"""

    ActionDesc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_Subsidy', column_name='ActionDesc', column_type='varchar(200)', nullable=False, chn_name='行为描述')
    """行为描述:"""

