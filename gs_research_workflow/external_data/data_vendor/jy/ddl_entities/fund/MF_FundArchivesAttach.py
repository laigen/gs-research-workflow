# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_FundArchivesAttach(SQLTableEntity):
    name: str = 'MF_FundArchivesAttach'
    
    chn_name: str = '公募基金概况附表'
    
    business_unique: str = 'InnerCode,TypeCode,StartDate'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.本表主要记录了证监会基金分类、银河证券基金分类、基金运作方式、封闭期、货币基金收益分配方式等数据内容。
2.历史数据：1998年3月起-至今。
3.信息来源：基金公司官网披露的产品说明书、临时公告，还有证监会官网等。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchivesAttach', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    StartDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchivesAttach', column_name='StartDate', column_type='datetime', nullable=False, chn_name='生效日期')
    """生效日期:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchivesAttach', column_name='EndDate', column_type='datetime', nullable=False, chn_name='取消日期')
    """取消日期:"""

    Remark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchivesAttach', column_name='Remark', column_type='varchar(500)', nullable=False, chn_name='备注说明')
    """备注说明:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchivesAttach', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='修改时间')
    """修改时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchivesAttach', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchivesAttach', column_name='InnerCode', column_type='int', nullable=True, chn_name='基金代码')
    """基金代码:基金代码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchivesAttach', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到基金的交易代码、简称等。"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchivesAttach', column_name='InfoSource', column_type='varchar(50)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    TypeCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchivesAttach', column_name='TypeCode', column_type='int', nullable=True, chn_name='类别代码')
    """类别代码:类别代码(TypeCode)与(CT_SystemConst)表中的DM字段关联，令LB=1252，得到类别代码的具体描述：10-证监会基金分类，11-晨星基金分类，12-国金基金分类，13-国金基金类别，14-基金类别，15-银河基金分类，16-上海证券基金分类，17-蚂蚁金服基金分类，18-银河证券分类2017版，20-基金运作方式，31-货币基金收益分..."""

    TypeName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchivesAttach', column_name='TypeName', column_type='varchar(50)', nullable=False, chn_name='类别')
    """类别:"""

    DataCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchivesAttach', column_name='DataCode', column_type='int', nullable=False, chn_name='数据代码')
    """数据代码:数据代码（DataCode）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，得到“数据代码”的具体描述，关联条件如下：当TypeCode=10，LB=1737；当TypeCode=11，LB=1093；当TypeCode=12，LB=1565 AND DM < 100；当TypeCode=13，LB=1565 AND DM >= ..."""

    DataName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchivesAttach', column_name='DataName', column_type='varchar(50)', nullable=False, chn_name='数据')
    """数据:"""

    DataValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundArchivesAttach', column_name='DataValue', column_type='int', nullable=False, chn_name='数值')
    """数值:"""

