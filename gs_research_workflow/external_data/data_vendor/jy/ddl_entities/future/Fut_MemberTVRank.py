# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class Fut_MemberTVRank(SQLTableEntity):
    name: str = 'Fut_MemberTVRank'
    
    chn_name: str = '会员期货交易排名'
    
    business_unique: str = 'EndDate,ReportPeriod,Exchange,MemberCode,RankType'
    
    refresh_freq: str = """月更新和年更新"""
    
    comment: str = """1.目前主要为国内三大商品期货交易所会员按成交金额、成交量的排名情况。其中：上海期货交易所只有年度数据数据,统计区间为期末累计；大连商品交易所、郑州商品交易所有按月统计的数据.
2.数据范围：2007——2012
3.信息来源：上海期货交易所、郑州商品交易所、大连商品交易所"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_MemberTVRank', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    RankType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_MemberTVRank', column_name='RankType', column_type='int', nullable=True, chn_name='统计类型')
    """统计类型:统计类型(RankType)与(CT_SystemConst)表中的DM字段关联，令LB = 1403 AND DM IN (1301,1303)，得到统计类型的具体描述：1301-期货会员成交量，1303-期货会员成交金额。"""

    Rank: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_MemberTVRank', column_name='Rank', column_type='int', nullable=False, chn_name='成交排名')
    """成交排名:"""

    TurnoverVolume: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_MemberTVRank', column_name='TurnoverVolume', column_type='decimal(18,2)', nullable=False, chn_name='成交量(手)')
    """成交量(手):"""

    TurnoverValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_MemberTVRank', column_name='TurnoverValue', column_type='decimal(19,4)', nullable=False, chn_name='成交金额(万元)')
    """成交金额(万元):"""

    Proportion: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_MemberTVRank', column_name='Proportion', column_type='decimal(9,6)', nullable=False, chn_name='比例(%)')
    """比例(%):若统计类型（RankType）的值等于1301(期货会员成交量)，则比例是指会员成交量占总成交量的比例，若统计类型（RankType）的值等于1303(期货会员成交金额)，则比例是指会员成交金额占总成金额的比例"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_MemberTVRank', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_MemberTVRank', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_MemberTVRank', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    InfoSources: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_MemberTVRank', column_name='InfoSources', column_type='varchar(100)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_MemberTVRank', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    ReportPeriod: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_MemberTVRank', column_name='ReportPeriod', column_type='int', nullable=True, chn_name='数据统计期间')
    """数据统计期间:数据统计期间(ReportPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 1074 AND DM IN (1,3)，得到数据统计期间的具体描述：1-月份，3-期末累计。"""

    Exchange: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_MemberTVRank', column_name='Exchange', column_type='int', nullable=True, chn_name='交易所')
    """交易所:交易所(Exchange)与(CT_SystemConst)表中的DM字段关联，令LB = 1324 AND DM IN (10,13,15)，得到交易所的具体描述：10-上海期货交易所，13-大连商品交易所，15-郑州商品交易所。"""

    MemberCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_MemberTVRank', column_name='MemberCode', column_type='varchar(50)', nullable=True, chn_name='会员号')
    """会员号:"""

    MemberName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_MemberTVRank', column_name='MemberName', column_type='varchar(200)', nullable=False, chn_name='会员名称')
    """会员名称:"""

    CorpCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_MemberTVRank', column_name='CorpCode', column_type='int', nullable=False, chn_name='企业编号')
    """企业编号:企业编号（CorpCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到会员机构的其他信息。"""

