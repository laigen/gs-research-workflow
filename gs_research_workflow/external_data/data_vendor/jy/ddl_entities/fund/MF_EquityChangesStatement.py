# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_EquityChangesStatement(SQLTableEntity):
    name: str = 'MF_EquityChangesStatement'
    
    chn_name: str = '公募基金所有者权益(基金净值)变动表'
    
    business_unique: str = 'InnerCode,EndDate,Mark,ItemsType'
    
    refresh_freq: str = """半年更新"""
    
    comment: str = """1.包含依据2007年新会计准则披露的基金净值变动表数据；并跟据新旧会计准则的科目对应关系，收录了主要科目的历史对应数据。
2.收录同一基金在报告期末的两种财务报告，即未调整报表和调整后报表。若某个报告期的数据有多次调整，则该表展示最新调整数据；若某报告期暂未披露调整后数据，则已调整类别下的数据与调整前的数据一致。
3.带“##”的特殊项目为单个基金披露的非标准化的科目，对应的“特殊字段说明”字段将对其作出说明；带“##”的调整项目是为了让报表的各个小项借贷平衡而设置的，便于客户对报表的遗漏和差错进行。
4.历史数据：2001年6月起-至今。
5.信息来源：基金公司披露的定期报告。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_EquityChangesStatement', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    AccountingStandards: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_EquityChangesStatement', column_name='AccountingStandards', column_type='int', nullable=False, chn_name='会计准则')
    """会计准则:会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 1455，得到会计准则的具体描述：1-新会计准则(2007)，9-旧会计准则。"""

    ItemsName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_EquityChangesStatement', column_name='ItemsName', column_type='varchar(100)', nullable=True, chn_name='项目名称')
    """项目名称:"""

    ItemsType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_EquityChangesStatement', column_name='ItemsType', column_type='int', nullable=True, chn_name='所属类别')
    """所属类别:所属类别(ItemsType)与(CT_SystemConst)表中的DM字段关联，令LB = 1495，得到所属类别的具体描述：1-实收基金，2-未分配利润，9-所有者权益合计。"""

    OpeningNV: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_EquityChangesStatement', column_name='OpeningNV', column_type='decimal(19,4)', nullable=False, chn_name='一、期初基金净值(所有者权益)')
    """一、期初基金净值(所有者权益):"""

    NVChangeByoOperating: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_EquityChangesStatement', column_name='NVChangeByoOperating', column_type='decimal(19,4)', nullable=False, chn_name='二、经营活动产生的净值变动数(净利润)')
    """二、经营活动产生的净值变动数(净利润):"""

    NVChangeByUnitTransaction: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_EquityChangesStatement', column_name='NVChangeByUnitTransaction', column_type='decimal(19,4)', nullable=False, chn_name='三、基金份额交易产生的净值变动数')
    """三、基金份额交易产生的净值变动数:"""

    ApplyingSum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_EquityChangesStatement', column_name='ApplyingSum', column_type='decimal(19,4)', nullable=False, chn_name='其中：基金申购款')
    """其中：基金申购款:"""

    DividendReinvestmentSum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_EquityChangesStatement', column_name='DividendReinvestmentSum', column_type='decimal(19,4)', nullable=False, chn_name='基金申购款中包含的分红再投资款')
    """基金申购款中包含的分红再投资款:"""

    RedemptionSum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_EquityChangesStatement', column_name='RedemptionSum', column_type='decimal(19,4)', nullable=False, chn_name='基金赎回款')
    """基金赎回款:"""

    NVChangeByDistribution: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_EquityChangesStatement', column_name='NVChangeByDistribution', column_type='decimal(19,4)', nullable=False, chn_name='四、向持有人分配收益产生的净值变动数')
    """四、向持有人分配收益产生的净值变动数:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_EquityChangesStatement', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    NVChangeExceptionalItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_EquityChangesStatement', column_name='NVChangeExceptionalItems', column_type='decimal(19,4)', nullable=False, chn_name='##变动特殊项目')
    """##变动特殊项目:"""

    NVChangeAdjustmentItems: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_EquityChangesStatement', column_name='NVChangeAdjustmentItems', column_type='decimal(19,4)', nullable=False, chn_name='##变动调整项目')
    """##变动调整项目:"""

    EndingNV: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_EquityChangesStatement', column_name='EndingNV', column_type='decimal(19,4)', nullable=False, chn_name='五、期末基金净值(所有者权益)')
    """五、期末基金净值(所有者权益):"""

    SpecialFieldRemark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_EquityChangesStatement', column_name='SpecialFieldRemark', column_type='varchar(1000)', nullable=False, chn_name='特殊字段说明')
    """特殊字段说明:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_EquityChangesStatement', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新日期')
    """更新日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_EquityChangesStatement', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_EquityChangesStatement', column_name='InfoSource', column_type='varchar(100)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    BulletinType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_EquityChangesStatement', column_name='BulletinType', column_type='int', nullable=False, chn_name='公告类别')
    """公告类别:公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311，得到公告类别的具体描述：10-发行上市书，20-定期报告，30-业绩快报，50-章程制度，70-临时公告，90-交易所通报，91-交易所临时停(复)牌公告，99-其他。"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_EquityChangesStatement', column_name='InnerCode', column_type='int', nullable=True, chn_name='基金内部编码')
    """基金内部编码:基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_EquityChangesStatement', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到基金公司的交易代码、简称等。"""

    StartDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_EquityChangesStatement', column_name='StartDate', column_type='datetime', nullable=False, chn_name='开始日期')
    """开始日期:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_EquityChangesStatement', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    Mark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_EquityChangesStatement', column_name='Mark', column_type='int', nullable=True, chn_name='调整标志')
    """调整标志:调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM IN (1,2)，得到调整标志的具体描述：1-是，2-否。"""

