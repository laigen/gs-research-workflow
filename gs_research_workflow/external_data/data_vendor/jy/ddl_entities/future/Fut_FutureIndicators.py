# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class Fut_FutureIndicators(SQLTableEntity):
    name: str = 'Fut_FutureIndicators'
    
    chn_name: str = '期货合约指标变动'
    
    business_unique: str = 'ContractInnerCode,EffectiveDate,CancleDate,IndicatorCode'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.收录商品期货和金融期货合约中涉及的各类指标的历史变动数据，包括：最低交易保证金比率、合约乘数、最小变动价位、交易手续费、交割手续费等指标。
2.信息来源：中国金融期货交易所、上海期货交易所、大连商品交易所和郑州商品交易所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FutureIndicators', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    DataValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FutureIndicators', column_name='DataValue', column_type='decimal(19,4)', nullable=False, chn_name='指标数据_金额')
    """指标数据_金额:"""

    RatioValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FutureIndicators', column_name='RatioValue', column_type='decimal(18,10)', nullable=False, chn_name='指标数据_比率(%)')
    """指标数据_比率(%):"""

    RemarkDesc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FutureIndicators', column_name='RemarkDesc', column_type='varchar(500)', nullable=False, chn_name='备注说明')
    """备注说明:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FutureIndicators', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FutureIndicators', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    ContractInnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FutureIndicators', column_name='ContractInnerCode', column_type='int', nullable=True, chn_name='合约内部编码')
    """合约内部编码:当IndicatorCode=1时，合约内部编码（ContractInnerCode）与期货品种（Fut_FuturesContract）中的合约内部编码（ContractInnerCode）关联，得到该期货品种的基本信息。
当IndicatorCode  in(2,3,4,5,6,12,13)时,合约内部编码（ContractInnerCode）：与“期货..."""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FutureIndicators', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FutureIndicators', column_name='InfoSource', column_type='varchar(200)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    EffectiveDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FutureIndicators', column_name='EffectiveDate', column_type='datetime', nullable=True, chn_name='生效日期')
    """生效日期:"""

    CancleDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FutureIndicators', column_name='CancleDate', column_type='datetime', nullable=False, chn_name='截止日期')
    """截止日期:"""

    IndicatorCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FutureIndicators', column_name='IndicatorCode', column_type='int', nullable=True, chn_name='指标代码')
    """指标代码:指标代码(IndicatorCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1578 AND DM IN (1,2,3,4,5,6,12,13)，得到指标代码的具体描述：1-合约乘数，2-最小变动价位，3-最低交易保证金，4-交易手续费，5-交割手续费，6-平今仓收取率，12-交易单位，13-交易代码。"""

    IndicatorName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FutureIndicators', column_name='IndicatorName', column_type='varchar(50)', nullable=False, chn_name='指标名称')
    """指标名称:"""

    IndicatorUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='Fut_FutureIndicators', column_name='IndicatorUnit', column_type='int', nullable=False, chn_name='指标单位')
    """指标单位:指标单位（IndicatorUnit）：：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令“LB=1225”，得到该指标的单位描述。3-% 9-点 15-吨/手 16-元/手"""

