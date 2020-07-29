# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_InvestorRa(SQLTableEntity):
    name: str = 'LC_InvestorRa'
    
    chn_name: str = '投资者关系活动'
    
    business_unique: str = 'InnerCode,ReceptionDate,SerialNb'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.收录各调研机构对上市公司调研的详情，包括调研日期、参与单位、调研人员、调研主要内容等信息。
2.数据范围：2012-至今
3.信息来源：巨潮"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InvestorRa', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    Participant: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InvestorRa', column_name='Participant', column_type='varchar(4000)', nullable=False, chn_name='参与单位及人员')
    """参与单位及人员:"""

    Place: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InvestorRa', column_name='Place', column_type='varchar(500)', nullable=False, chn_name='地点')
    """地点:"""

    ListingCreper: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InvestorRa', column_name='ListingCreper', column_type='varchar(4000)', nullable=False, chn_name='上市公司接待人员')
    """上市公司接待人员:"""

    TmainContent: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InvestorRa', column_name='TmainContent', column_type='text', nullable=False, chn_name='主要内容')
    """主要内容:"""

    ArticleFile: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InvestorRa', column_name='ArticleFile', column_type='blob', nullable=False, chn_name='附件')
    """附件:"""

    FileType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InvestorRa', column_name='FileType', column_type='int', nullable=False, chn_name='附件格式')
    """附件格式:附件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB = 1309，得到附件格式的具体描述：1-PDF，2-DOC，3-TXT，4-XLS，5-HTML，6-RTF，7-MHT，8-RAR，9-PPT，10-JPG，11-DOCX，12-XLSX，13-PPTX，14-EML，15-ZIP，16-DOCM，17-XLSM，..."""

    InfoTitle: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InvestorRa', column_name='InfoTitle', column_type='varchar(200)', nullable=False, chn_name='标题')
    """标题:"""

    LinkAddress: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InvestorRa', column_name='LinkAddress', column_type='varchar(500)', nullable=False, chn_name='链接地址')
    """链接地址:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InvestorRa', column_name='UpdateTime', column_type='datetime', nullable=False, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InvestorRa', column_name='JSID', column_type='bigint', nullable=False, chn_name='JSID')
    """JSID:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InvestorRa', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InvestorRa', column_name='InnerCode', column_type='int', nullable=True, chn_name='证券内部编码')
    """证券内部编码:证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。"""

    Nbcode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InvestorRa', column_name='Nbcode', column_type='varchar(40)', nullable=False, chn_name='编号')
    """编号:"""

    ReceptionDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InvestorRa', column_name='ReceptionDate', column_type='datetime', nullable=True, chn_name='接待日期')
    """接待日期:"""

    ReceptionDateE: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InvestorRa', column_name='ReceptionDateE', column_type='datetime', nullable=True, chn_name='接待日期截止日')
    """接待日期截止日:"""

    ReceptionDaTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InvestorRa', column_name='ReceptionDaTime', column_type='varchar(100)', nullable=False, chn_name='接待时间')
    """接待时间:"""

    SerialNb: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InvestorRa', column_name='SerialNb', column_type='int', nullable=False, chn_name='序号')
    """序号:"""

    ActivitiesCate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_InvestorRa', column_name='ActivitiesCate', column_type='int', nullable=False, chn_name='活动类别')
    """活动类别:"""

