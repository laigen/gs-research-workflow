# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_AshareIPOBid(SQLTableEntity):
    name: str = 'LC_AshareIPOBid'
    
    chn_name: str = 'A股询价明细'
    
    business_unique: str = 'InnerCode,SerialNumber,InvestorName,BidderName'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.收录新上市A股询价、网下配售明细，包括投资者名称、配售对象名称、申报价格、拟申购股数、总实际申购股数和总获配售股数等内容。
2.信息来源：上交所、深交所"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIPOBid', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    PriceUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIPOBid', column_name='PriceUnit', column_type='decimal(19,4)', nullable=False, chn_name='申报价格')
    """申报价格:"""

    PlannedBidVol: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIPOBid', column_name='PlannedBidVol', column_type='decimal(19,2)', nullable=False, chn_name='拟申购股数(股)')
    """拟申购股数(股):"""

    PremiumRate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIPOBid', column_name='PremiumRate', column_type='decimal(19,4)', nullable=False, chn_name='申报价折溢价比率')
    """申报价折溢价比率:申报价折溢价比率(PremiumRate)=申报价格/每股发行价格。"""

    BidVolEx: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIPOBid', column_name='BidVolEx', column_type='decimal(19,2)', nullable=False, chn_name='被剔除申购股数(股)')
    """被剔除申购股数(股):"""

    ActualBidVol: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIPOBid', column_name='ActualBidVol', column_type='decimal(19,2)', nullable=False, chn_name='总实际申购股数(股)')
    """总实际申购股数(股):"""

    ActualAllotment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIPOBid', column_name='ActualAllotment', column_type='decimal(19,2)', nullable=False, chn_name='总获配售股数(股)')
    """总获配售股数(股):"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIPOBid', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIPOBid', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIPOBid', column_name='InnerCode', column_type='int', nullable=True, chn_name='证券内部编码')
    """证券内部编码:证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIPOBid', column_name='CompanyCode', column_type='int', nullable=False, chn_name='公司代码')
    """公司代码:"""

    SerialNumber: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIPOBid', column_name='SerialNumber', column_type='int', nullable=True, chn_name='序号')
    """序号:"""

    InvestorCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIPOBid', column_name='InvestorCode', column_type='int', nullable=False, chn_name='投资者编码')
    """投资者编码:"""

    InvestorName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIPOBid', column_name='InvestorName', column_type='varchar(200)', nullable=False, chn_name='投资者名称')
    """投资者名称:"""

    BidderCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIPOBid', column_name='BidderCode', column_type='int', nullable=False, chn_name='配售对象代码')
    """配售对象代码:"""

    BidderName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIPOBid', column_name='BidderName', column_type='varchar(200)', nullable=True, chn_name='配售对象名称')
    """配售对象名称:"""

    BidderCategory: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_AshareIPOBid', column_name='BidderCategory', column_type='int', nullable=False, chn_name='配售对象类别')
    """配售对象类别:配售对象类别(BidderCategory)与(CT_SystemConst)表中的DM字段关联，令LB = 1825，得到配售对象类别的具体描述：1-公募基金，2-社保基金或社保基金组合，3-个人或个人自有资金投资账户，4-其他，5-企业年金计划，6-机构自营投资账户，7-证券公司集合资产管理计划，8-基金公司或其资产管理子公司一对一，9-保险资金投资账户..."""

