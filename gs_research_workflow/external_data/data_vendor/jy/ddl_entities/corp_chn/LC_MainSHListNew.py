# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_MainSHListNew(SQLTableEntity):
    name: str = 'LC_MainSHListNew'
    
    chn_name: str = '股东名单(新)'
    
    business_unique: str = 'CompanyCode,EndDate,InfoTypeCode,SHSerial'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.收录公司主要股东构成及持股数量比例、持股性质等明细资料，包括发行前和上市后的历次变动记录。
2.数据范围：1992-06-30至今
3.信息来源：招股说明书、上市公告书、定报、临时公告等。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    SHList: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='SHList', column_type='varchar(200)', nullable=False, chn_name='股东名单')
    """股东名单:"""

    SHAttribute: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='SHAttribute', column_type='int', nullable=False, chn_name='股东属性')
    """股东属性:股东属性(SHAttribute)与(CT_SystemConst)表中的DM字段关联，令LB=1783，得到股东属性的具体描述：1-自然人，2-企业，3-证券品种，99-其他。"""

    SHKind: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='SHKind', column_type='varchar(50)', nullable=False, chn_name='股东性质')
    """股东性质:"""

    SHKindCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='SHKindCode', column_type='int', nullable=False, chn_name='股东性质编码')
    """股东性质编码:股东性质编码(SHKindCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1026，得到股东性质编码的具体描述：1-封闭式投资基金，2-开放式投资基金，3-金融机构—证券、信托公司，4-金融机构—保险公司，5-金融机构—期货公司，6-金融机构—银行，7-公益基金，8-投资、咨询公司，9-风险投资公司，10-金融机构—金融租赁公司，..."""

    SHTypeCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='SHTypeCode', column_type='int', nullable=False, chn_name='股东类别编码')
    """股东类别编码:股东类别编码(SHTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1368，得到股东类别编码的具体描述：10-国有股东，20-外资股东，90-其他股东。"""

    SHType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='SHType', column_type='varchar(50)', nullable=False, chn_name='股东类别')
    """股东类别:"""

    SecuCoBelongedCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='SecuCoBelongedCode', column_type='int', nullable=False, chn_name='归属机构编码')
    """归属机构编码:归属机构编码（SecuCoBelongedCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到归属机构的基本情况。"""

    SecuCoBelongedName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='SecuCoBelongedName', column_type='varchar(200)', nullable=False, chn_name='归属机构名称')
    """归属机构名称:"""

    SecuInnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='SecuInnerCode', column_type='int', nullable=False, chn_name='所属基金/股票内部编码')
    """所属基金/股票内部编码:所属基金/股票内部编码（SecuInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到所属基金/股票的交易代码、交易简称等"""

    SecuCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='SecuCode', column_type='varchar(10)', nullable=False, chn_name='所属基金/股票代码')
    """所属基金/股票代码:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。"""

    SecuAbbr: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='SecuAbbr', column_type='varchar(20)', nullable=False, chn_name='所属基金/股票简称')
    """所属基金/股票简称:"""

    HoldSum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='HoldSum', column_type='decimal(16,0)', nullable=False, chn_name='持股数(股)')
    """持股数(股):持股数（股）（HoldSum）：当“信息类别代码（InfoTypeCode）”=1时，持股数(股)=总股本当“信息类别代码（InfoTypeCode）”=2时，持股数(股)=无限售股数(股)"""

    RestrainedTShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='RestrainedTShare', column_type='decimal(16,0)', nullable=False, chn_name='其中:有限售股数(股)')
    """其中:有限售股数(股):"""

    UnstintedTShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='UnstintedTShare', column_type='decimal(16,0)', nullable=False, chn_name='其中:无限售股数(股)')
    """其中:无限售股数(股):"""

    HoldAShareSum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='HoldAShareSum', column_type='decimal(16,0)', nullable=False, chn_name='持有A股数量(股)')
    """持有A股数量(股):"""

    RestrainedAShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='RestrainedAShare', column_type='decimal(16,0)', nullable=False, chn_name='其中:有限售A股数(股)')
    """其中:有限售A股数(股):"""

    UnstintedAShare: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='UnstintedAShare', column_type='decimal(16,0)', nullable=False, chn_name='其中:无限售A股数(股)')
    """其中:无限售A股数(股):"""

    HoldBShareSum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='HoldBShareSum', column_type='decimal(16,0)', nullable=False, chn_name='持有B股数量(股)')
    """持有B股数量(股):"""

    HoldHShareSum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='HoldHShareSum', column_type='decimal(16,0)', nullable=False, chn_name='持有H股数量(股)')
    """持有H股数量(股):"""

    HoldOthterShareSum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='HoldOthterShareSum', column_type='decimal(16,0)', nullable=False, chn_name='持有其他股数量(股)')
    """持有其他股数量(股):"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    HoldSumChange: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='HoldSumChange', column_type='decimal(16,0)', nullable=False, chn_name='持股数量增减(股)')
    """持股数量增减(股):"""

    HoldSumChangeRate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='HoldSumChangeRate', column_type='decimal(16,6)', nullable=False, chn_name='持股数量增减幅度(%)')
    """持股数量增减幅度(%):"""

    PCTOfTotalShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='PCTOfTotalShares', column_type='decimal(10,6)', nullable=False, chn_name='占总股本比例(%)')
    """占总股本比例(%):占总股本比例（%）（PCTOfTotalShares）：当“信息类别代码（InfoTypeCode）”=1时，持股数(股)/总股本*100当“信息类别代码（InfoTypeCode）”=2时，无限售股数(股)/总股本*100"""

    PCTOfFloatShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='PCTOfFloatShares', column_type='decimal(10,6)', nullable=False, chn_name='占流通A股比例(%)')
    """占流通A股比例(%):占流通A股比例（%）（PCTOfFloatShares）=无限售流通A股/已上市流通A股（不含高管股）*100"""

    ShareCharacterStatement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='ShareCharacterStatement', column_type='varchar(50)', nullable=False, chn_name='股本性质描述')
    """股本性质描述:"""

    PledgeInvolvedSum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='PledgeInvolvedSum', column_type='decimal(16,0)', nullable=False, chn_name='股权质押涉及股数(股)')
    """股权质押涉及股数(股):"""

    FreezeInvolvedSum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='FreezeInvolvedSum', column_type='decimal(16,0)', nullable=False, chn_name='股权冻结涉及股数(股)')
    """股权冻结涉及股数(股):"""

    PFStatement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='PFStatement', column_type='varchar(200)', nullable=False, chn_name='股权质押冻结情况说明')
    """股权质押冻结情况说明:"""

    ConnectionRelation: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='ConnectionRelation', column_type='varchar(50)', nullable=False, chn_name='股东关联关系')
    """股东关联关系:"""

    ConnectionStatement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='ConnectionStatement', column_type='varchar(2000)', nullable=False, chn_name='与其他股东关联关系说明')
    """与其他股东关联关系说明:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    ActInConcertStatement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='ActInConcertStatement', column_type='varchar(2000)', nullable=False, chn_name='与其他股东同属一致行动人说明')
    """与其他股东同属一致行动人说明:"""

    Notes: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='Notes', column_type='varchar(255)', nullable=False, chn_name='备注')
    """备注:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='InfoSource', column_type='varchar(50)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    InfoTypeCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='InfoTypeCode', column_type='tinyint', nullable=True, chn_name='信息类别编码')
    """信息类别编码:信息类别编码(InfoTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1025，得到信息类别编码的具体描述：1-前十大股东，2-前十流通股东，3-前十大股东与流通股东，4-十大有限售条件股东，10-有限售股份，11-有限售股东。"""

    SHNo: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='SHNo', column_type='int', nullable=True, chn_name='股东排名')
    """股东排名:股东排名（SHNo）：当“信息类别代码（InfoTypeCode）”=1时，“股东排名（SHNo）”表示前十大股东排名；当“信息类别代码（InfoTypeCode）”=2时，“股东排名（SHNo）”表示前十大流通股东排名。"""

    SHSerial: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='SHSerial', column_type='int', nullable=True, chn_name='股东序号')
    """股东序号:"""

    GDID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_MainSHListNew', column_name='GDID', column_type='int', nullable=False, chn_name='股东ID')
    """股东ID:股东ID（GDID）：当股东属性（SHAttribute）=2时，与机构基本资料（LC_InstiArchive）中的企业编号（CompanyCode）关联；股东属性（SHAttribute）=3时，与理财产品主表（SF_PlanMain）或证券主表（SecuMain）中的内部编码（InnerCode）关联。"""

