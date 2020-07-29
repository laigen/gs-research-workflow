# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_FundManagerNew(SQLTableEntity):
    name: str = 'MF_FundManagerNew'
    
    chn_name: str = '公募基金经理(新)'
    
    business_unique: str = '与公募基金经理基本资料 MF_PersonalInfo一起开'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.本表记录历任基金经理、基金经理助理的任职起止日期、任职期间最新的净值增长率等。可以通过所属人员代码关联MF_PersonalInfo，配合使用。
2.历史数据：1998年3月起-至今。
3.信息来源：基金公司官网披露的产品说明书。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundManagerNew', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    DimissionDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundManagerNew', column_name='DimissionDate', column_type='datetime', nullable=False, chn_name='离职日期')
    """离职日期:"""

    ManagementTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundManagerNew', column_name='ManagementTime', column_type='int', nullable=False, chn_name='任职天数')
    """任职天数:"""

    Performance: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundManagerNew', column_name='Performance', column_type='decimal(18,6)', nullable=False, chn_name='任职期间基金净值增长率')
    """任职期间基金净值增长率:任职期间基金净值增长率（Performance）：
       任职期间基金净值增长率=Pt/P0∏（Pi/（Pi-Di））*100，该指标假设以权益登记日作为分红再投资日。
       其中：Pt－为离任前一次公布单位基金净值（已离职）或最新1次公布单位基金净值（现任），
             P0－为到任日期后最近1次公布单位基金净值，
    ..."""

    Notes: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundManagerNew', column_name='Notes', column_type='varchar(250)', nullable=False, chn_name='备注说明')
    """备注说明:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundManagerNew', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新日期')
    """更新日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundManagerNew', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundManagerNew', column_name='InnerCode', column_type='int', nullable=True, chn_name='基金内部编码')
    """基金内部编码:基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundManagerNew', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundManagerNew', column_name='InfoSource', column_type='varchar(100)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    PersonalCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundManagerNew', column_name='PersonalCode', column_type='bigint', nullable=True, chn_name='所属人员代码')
    """所属人员代码:所属人员代码（PersonalCode）：与“基金自然人基本资料表（MF_PersonalInfo）”中的“所属人员编码（PersonalCode）”关联，得到基金经理的基本资料。"""

    Name: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundManagerNew', column_name='Name', column_type='varchar(30)', nullable=False, chn_name='姓名')
    """姓名:"""

    PostName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundManagerNew', column_name='PostName', column_type='int', nullable=False, chn_name='职位名称')
    """职位名称:职位名称(PostName)与(CT_SystemConst)表中的DM字段关联，令LB=1209，得到职位名称的具体描述：1-基金经理，2-基金经理助理。"""

    Incumbent: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundManagerNew', column_name='Incumbent', column_type='tinyint', nullable=False, chn_name='在任与否')
    """在任与否:在任与否（Incumbent），该字段固定以下常量： 1-在任；0-离任"""

    AccessionDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_FundManagerNew', column_name='AccessionDate', column_type='datetime', nullable=True, chn_name='到任日期')
    """到任日期:"""

