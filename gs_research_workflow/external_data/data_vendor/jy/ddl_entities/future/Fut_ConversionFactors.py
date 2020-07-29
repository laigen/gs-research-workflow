# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class Fut_ConversionFactors(SQLTableEntity):
    name: str = 'Fut_ConversionFactors'
    
    chn_name: str = '期货交割转换因子'
    
    business_unique: str = 'InfoPublDate,ContractInnerCode,IBMarketInnerCode'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.收录期货(包括金融期货)交易的转换因子。可查询该期货的合约信息和转换债券的相关信息。包括票面利率(%)、转换因子等指标信息。
2.数据范围：2014-01-07——至今。
3.信息来源：中国金融金融期货交易所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ConversionFactors', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    ConversionFactors: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ConversionFactors', column_name='ConversionFactors', column_type='decimal(19,8)', nullable=False, chn_name='转换因子')
    """转换因子:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ConversionFactors', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='修改时间')
    """修改时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ConversionFactors', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ConversionFactors', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    IssuanceOrg: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ConversionFactors', column_name='IssuanceOrg', column_type='int', nullable=False, chn_name='发布机构')
    """发布机构:发布机构(IssuanceOrg)与(CT_SystemConst)表中的DM字段关联，令LB = 1324 AND DM = 20，得到发布机构的具体描述：20-中国金融期货交易所。"""

    ContractInnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ConversionFactors', column_name='ContractInnerCode', column_type='int', nullable=False, chn_name='合约内部编码')
    """合约内部编码:合约内部编码（ContractInnerCode）：与“期货合约主表（Fut_ContractMain）”中的“合约内部编码（ContractInnerCode）”关联，得到该期货合约的基础信息。"""

    SerialNumber: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ConversionFactors', column_name='SerialNumber', column_type='int', nullable=False, chn_name='序号')
    """序号:"""

    IBMarketInnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ConversionFactors', column_name='IBMarketInnerCode', column_type='int', nullable=False, chn_name='银行间债券市场内部编码')
    """银行间债券市场内部编码:银行间债券市场内部编码(IBMarketInnerCode)：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。"""

    SHExchangeInnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ConversionFactors', column_name='SHExchangeInnerCode', column_type='int', nullable=False, chn_name='上海证券交易所内部编码')
    """上海证券交易所内部编码:上海证券交易所内部编码(SHExchangeInnerCode)：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。"""

    SZExchangeInnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ConversionFactors', column_name='SZExchangeInnerCode', column_type='int', nullable=False, chn_name='深圳证券交易所内部编码')
    """深圳证券交易所内部编码:深圳证券交易所内部编码(SZExchangeInnerCode)：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。"""

    CouponRate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_ConversionFactors', column_name='CouponRate', column_type='decimal(19,8)', nullable=False, chn_name='票面利率(%)')
    """票面利率(%):"""

