# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class Fut_MemberRankByContract(SQLTableEntity):
    name: str = 'Fut_MemberRankByContract'
    
    chn_name: str = '期货会员交易排名_按交易合约'
    
    business_unique: str = 'EndDate,ExchangeCode,ContractInnerCode,ReportPeriod,MemberInnerCode,IndicatorCode'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.收录国内期货交易所会员以交易合约为维度，日度的按照成交量统计、持买单量统计和持卖单量统计3种统计方式统计的会员成交持仓排名数据。
2.数据范围：2009-07-01——至今。
3.信息来源：上海期货交易所、大连商品交易所、郑州商品交易所和中国金融期货交易所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_MemberRankByContract', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    MemberAbbr: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_MemberRankByContract', column_name='MemberAbbr', column_type='varchar(200)', nullable=False, chn_name='会员简称')
    """会员简称:"""

    IndicatorCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_MemberRankByContract', column_name='IndicatorCode', column_type='int', nullable=True, chn_name='指标代码')
    """指标代码:指标代码（IndicatorCode）：与系统常量表（CT_SystemConst）中的代码（DM）字段进行关联，令LB=1580，得到统计指标的具体描述。1-成交量统计、3-持买仓量统计、4-持卖仓量统计。"""

    IndicatorName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_MemberRankByContract', column_name='IndicatorName', column_type='varchar(50)', nullable=False, chn_name='指标名称')
    """指标名称:"""

    IndicatorVolume: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_MemberRankByContract', column_name='IndicatorVolume', column_type='decimal(18,4)', nullable=False, chn_name='指标数量(手)')
    """指标数量(手):"""

    ChangeVolume: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_MemberRankByContract', column_name='ChangeVolume', column_type='decimal(18,4)', nullable=False, chn_name='较上期增减量(手)')
    """较上期增减量(手):"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_MemberRankByContract', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_MemberRankByContract', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_MemberRankByContract', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    ExchangeCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_MemberRankByContract', column_name='ExchangeCode', column_type='int', nullable=True, chn_name='交易所')
    """交易所:交易所(ExchangeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1324 AND DM IN (10,13,15,20)，得到交易所的具体描述：10-上海期货交易所，13-大连商品交易所，15-郑州商品交易所，20-中国金融期货交易所。"""

    ContractInnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_MemberRankByContract', column_name='ContractInnerCode', column_type='int', nullable=True, chn_name='合约内部编码')
    """合约内部编码:合约内部编码（ContractInnerCode）：与期货合约（Fut_ContractMain）表中的合约内部编码（ContractInnerCode）字段进行关联，得到该期货合约的基础信息。"""

    ContractCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_MemberRankByContract', column_name='ContractCode', column_type='varchar(10)', nullable=False, chn_name='合约代码')
    """合约代码:"""

    ReportPeriod: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_MemberRankByContract', column_name='ReportPeriod', column_type='int', nullable=True, chn_name='数据统计期间')
    """数据统计期间:数据统计期间(ReportPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 1074 AND DM = 5，得到数据统计期间的具体描述：5-日。"""

    RankNumber: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_MemberRankByContract', column_name='RankNumber', column_type='int', nullable=False, chn_name='名次')
    """名次:"""

    MemberInnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_MemberRankByContract', column_name='MemberInnerCode', column_type='int', nullable=False, chn_name='会员内部编码')
    """会员内部编码:会员内部编码（MemberInnerCode）：与机构基本资料（LC_InstiArchive）表中的企业编号（CompanyCode）字段进行关联，得到会员的其他基本资料。"""

    MemberCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_MemberRankByContract', column_name='MemberCode', column_type='varchar(20)', nullable=False, chn_name='会员号')
    """会员号:"""

