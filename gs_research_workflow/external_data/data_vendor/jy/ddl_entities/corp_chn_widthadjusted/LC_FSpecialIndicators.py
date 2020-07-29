# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_FSpecialIndicators(SQLTableEntity):
    name: str = 'LC_FSpecialIndicators'
    
    chn_name: str = '金融类特有指标(新)'
    
    business_unique: str = 'CompanyCode,EndDate,Mark,IndicatorCode'
    
    refresh_freq: str = """季更新"""
    
    comment: str = """1.反映银行、证券公司、保险公司等特有的指标数据，包括指标名称、金额、比率等内容。
2.数据范围：1998-12-31至今
3.信息来源：定期报告、跟踪评级报告等"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FSpecialIndicators', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    Amount: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FSpecialIndicators', column_name='Amount', column_type='decimal(19,4)', nullable=False, chn_name='金额(元)')
    """金额(元):"""

    RatioEOP: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FSpecialIndicators', column_name='RatioEOP', column_type='decimal(18,9)', nullable=False, chn_name='比率-期末(%)')
    """比率-期末(%):"""

    RatioAVG: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FSpecialIndicators', column_name='RatioAVG', column_type='decimal(18,9)', nullable=False, chn_name='比率-平均(%)')
    """比率-平均(%):"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FSpecialIndicators', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新日期')
    """更新日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FSpecialIndicators', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FSpecialIndicators', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FSpecialIndicators', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FSpecialIndicators', column_name='InfoSource', column_type='varchar(50)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FSpecialIndicators', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    Mark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FSpecialIndicators', column_name='Mark', column_type='int', nullable=True, chn_name='合并调整标志')
    """合并调整标志:合并调整标志（Mark），该字段固定以下常量：1-合并调整；2-合并未调整；3-母公司调整；4-母公司未调整"""

    IndicatorType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FSpecialIndicators', column_name='IndicatorType', column_type='int', nullable=True, chn_name='指标类别')
    """指标类别:指标类别（IndicatorType）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令“LB=1467”，得到金融指标的具体类别。10-银行类专项指标，11-银行贷款五级分类，20-证券类专项指标，30-保险类专项指标"""

    IndicatorName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FSpecialIndicators', column_name='IndicatorName', column_type='varchar(200)', nullable=False, chn_name='指标名称')
    """指标名称:"""

    IndicatorCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FSpecialIndicators', column_name='IndicatorCode', column_type='int', nullable=False, chn_name='指标代码')
    """指标代码:指标代码（IndicatorCode）：与“系统常量表(CT_SystemConst)”中的“代码(DM)”关联，令“LB=1468”，得到具体的指标名称。当IndicatorCode=15000时，代表《商业银行资本充足率管理办法》下披露的资本净额；当 IndicatorCode=20000时，代表《商业银行资本充足率管理办法》下披露的资本充足率。"""

