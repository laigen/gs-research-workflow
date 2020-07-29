# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_SecuMain(SQLTableEntity):
    name: str = 'HK_SecuMain'
    
    chn_name: str = '港股证券主表'
    
    business_unique: str = '港股常量表单'
    
    refresh_freq: str = """日处理，不定时更新"""
    
    comment: str = """本表收录港股单个证券品种的简称、上市交易所等基础信息。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SecuMain', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    ChiSpelling: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SecuMain', column_name='ChiSpelling', column_type='varchar(10)', nullable=False, chn_name='拼音证券简称')
    """拼音证券简称:"""

    SecuMarket: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SecuMain', column_name='SecuMarket', column_type='int', nullable=False, chn_name='证券市场')
    """证券市场:证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB = 201 AND DM IN (57,66,67,68,72,77,78,84)，得到证券市场的具体描述：57-马来西亚吉隆坡证券交易所，66-泰国证券交易所，67-韩国首尔证券交易所，68-东京证券交易所，72-香港联交所，77-美国纳斯达克证券交易所，78-纽..."""

    SecuCategory: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SecuMain', column_name='SecuCategory', column_type='int', nullable=False, chn_name='证券类别')
    """证券类别:证券类别(SecuCategory)与(CT_SystemConst)表中的DM字段关联，令LB = 1177，得到证券类别的具体描述：1-A股，2-B股，3-H股，4-大盘，5-国债回购，6-国债现货，7-金融债券，8-开放式基金，9-可转换债券，10-其他，11-企业债券，12-企业债券回购，13-投资基金，14-央行票据，15-深市代理沪市股票，16-..."""

    ListedDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SecuMain', column_name='ListedDate', column_type='datetime', nullable=False, chn_name='上市日期')
    """上市日期:"""

    ListedSector: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SecuMain', column_name='ListedSector', column_type='int', nullable=False, chn_name='上市板块')
    """上市板块:上市板块(ListedSector)与(CT_SystemConst)表中的DM字段关联，令LB = 207，得到上市板块的具体描述：1-主板，2-中小企业板，3-三板，4-其他，5-大宗交易系统，6-创业板，101-纳斯达克全球精选市场（NASDAQ-GS），102-纳斯达克全球市场（NASDAQ-GM），103-纳斯达克资本市场（NASDAQ-CM）。"""

    ListedState: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SecuMain', column_name='ListedState', column_type='int', nullable=False, chn_name='上市状态')
    """上市状态:上市状态(ListedState)与(CT_SystemConst)表中的DM字段关联，令LB = 1176 AND DM IN (1,3,5,9)，得到上市状态的具体描述：1-上市，3-暂停，5-终止，9-其他。"""

    FormerName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SecuMain', column_name='FormerName', column_type='varchar(200)', nullable=False, chn_name='曾用名')
    """曾用名:"""

    DelistingDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SecuMain', column_name='DelistingDate', column_type='datetime', nullable=False, chn_name='退市日期')
    """退市日期:"""

    TradingUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SecuMain', column_name='TradingUnit', column_type='decimal(18,4)', nullable=False, chn_name='买卖单位(股/手)')
    """买卖单位(股/手):"""

    TraCurrUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SecuMain', column_name='TraCurrUnit', column_type='int', nullable=False, chn_name='交易货币单位')
    """交易货币单位:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SecuMain', column_name='InnerCode', column_type='int', nullable=True, chn_name='证券内部编码')
    """证券内部编码:"""

    ISIN: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SecuMain', column_name='ISIN', column_type='varchar(20)', nullable=False, chn_name='ISIN代码')
    """ISIN代码:"""

    InsertTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SecuMain', column_name='InsertTime', column_type='datetime', nullable=False, chn_name='发布时间')
    """发布时间:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SecuMain', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SecuMain', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SecuMain', column_name='CompanyCode', column_type='int', nullable=False, chn_name='公司代码')
    """公司代码:"""

    SecuCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SecuMain', column_name='SecuCode', column_type='varchar(10)', nullable=False, chn_name='证券代码')
    """证券代码:"""

    ChiName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SecuMain', column_name='ChiName', column_type='varchar(200)', nullable=False, chn_name='中文名称')
    """中文名称:"""

    ChiNameAbbr: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SecuMain', column_name='ChiNameAbbr', column_type='varchar(100)', nullable=False, chn_name='中文名称缩写')
    """中文名称缩写:"""

    EngName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SecuMain', column_name='EngName', column_type='varchar(200)', nullable=False, chn_name='英文名称')
    """英文名称:"""

    EngNameAbbr: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SecuMain', column_name='EngNameAbbr', column_type='varchar(50)', nullable=False, chn_name='英文名称缩写')
    """英文名称缩写:"""

    SecuAbbr: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SecuMain', column_name='SecuAbbr', column_type='varchar(20)', nullable=False, chn_name='证券简称')
    """证券简称:"""

