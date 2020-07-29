# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_SHNumber(SQLTableEntity):
    name: str = 'LC_SHNumber'
    
    chn_name: str = '股东户数'
    
    business_unique: str = 'CompanyCode,EndDate'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.反映公司全体股东、A股股东、B股东、H股东的持股情况及其历史变动情况等。
2.指标计算公式：
  1)户均持股比例＝户均持股数量/股本*100%（公式中分子分母描述同一股票类型）
  2)相对上一期报告期户均持股比例变化＝本报告期户均持股比例－上一报告期户均持股比例
  3)户均持股数季度增长率＝(本季度户均持股数量/上一季度户均持股数量－1)*100%
  4)户均持股比例季度增长率=(本季度户均持股比例/上一季度户均持股比例-1)*100% 
  5)户均持股数半年增长率=(本报告期户均持股数量/前推两季度户均持股数量-1)*100% 
  6)户均持股比例季度增长率 = (本报告期户均持股比例/ 前推两个季度户均持股比例-1)*100%
2.数据范围：1992-12-31至今
3.信息来源：招股说明书、上市公告书、定报、临时公告等。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    AvgHoldSumGRQuarter: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='AvgHoldSumGRQuarter', column_type='decimal(18,4)', nullable=False, chn_name='户均持股数季度增长率(%)')
    """户均持股数季度增长率(%):"""

    ProportionGRQuarter: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='ProportionGRQuarter', column_type='float', nullable=False, chn_name='户均持股比例季度增长率(%)')
    """户均持股比例季度增长率(%):"""

    AvgHoldSumGRHalfAYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='AvgHoldSumGRHalfAYear', column_type='decimal(18,4)', nullable=False, chn_name='户均持股数半年增长率(%)')
    """户均持股数半年增长率(%):"""

    ProportionGRHalfAYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='ProportionGRHalfAYear', column_type='float', nullable=False, chn_name='户均持股比例半年增长率(%)')
    """户均持股比例半年增长率(%):"""

    ASHNum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='ASHNum', column_type='int', nullable=False, chn_name='A股股东户数(户)')
    """A股股东户数(户):"""

    AAverageHoldSum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='AAverageHoldSum', column_type='decimal(18,2)', nullable=False, chn_name='A股股东户均持股数(股/户)')
    """A股股东户均持股数(股/户):A股股东户均持股数（AAverageHoldSum）＝A股股本/A股股东户数"""

    AHoldProportionPAccount: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='AHoldProportionPAccount', column_type='float', nullable=False, chn_name='A股户均持股比例(%)')
    """A股户均持股比例(%):"""

    AProportionChange: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='AProportionChange', column_type='float', nullable=False, chn_name='A股相对上一期报告期户均持股比例变化(百分点)')
    """A股相对上一期报告期户均持股比例变化(百分点):"""

    AAvgHoldSumGRQuarter: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='AAvgHoldSumGRQuarter', column_type='decimal(18,4)', nullable=False, chn_name='A股户均持股数季度增长率(%)')
    """A股户均持股数季度增长率(%):"""

    AProportionGRQuarter: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='AProportionGRQuarter', column_type='float', nullable=False, chn_name='A股户均持股比例季度增长率(%)')
    """A股户均持股比例季度增长率(%):"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。"""

    AAvgHoldSumGRHalfAYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='AAvgHoldSumGRHalfAYear', column_type='decimal(18,4)', nullable=False, chn_name='A股户均持股数半年增长率(%)')
    """A股户均持股数半年增长率(%):"""

    AProportionGRHalfAYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='AProportionGRHalfAYear', column_type='float', nullable=False, chn_name='A股户均持股比例半年增长率(%)')
    """A股户均持股比例半年增长率(%):"""

    StaffSHNum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='StaffSHNum', column_type='int', nullable=False, chn_name='职工股户数(户)')
    """职工股户数(户):"""

    AFAverageHoldSum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='AFAverageHoldSum', column_type='int', nullable=False, chn_name='无限售A股股东户均持股数(股/户)')
    """无限售A股股东户均持股数(股/户):无限售A股股东户均持股数（AFAverageHoldSum）＝无限售A股/A股股东户数"""

    AFHoldPropTA: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='AFHoldPropTA', column_type='int', nullable=False, chn_name='无限售A股/股东总户数(股/户)')
    """无限售A股/股东总户数(股/户):"""

    AFHoldProportionPAccount: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='AFHoldProportionPAccount', column_type='float', nullable=False, chn_name='无限售A股户均持股比例(%)')
    """无限售A股户均持股比例(%):"""

    AFProportionChange: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='AFProportionChange', column_type='float', nullable=False, chn_name='无限售A股相对上一期报告期户均持股比例变化(百分点')
    """无限售A股相对上一期报告期户均持股比例变化(百分点:"""

    AFAvgHoldSumGRQuarter: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='AFAvgHoldSumGRQuarter', column_type='decimal(18,4)', nullable=False, chn_name='无限售A股户均持股数季度增长率(%)')
    """无限售A股户均持股数季度增长率(%):"""

    AFProportionGRQuarter: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='AFProportionGRQuarter', column_type='float', nullable=False, chn_name='无限售A股户均持股比例季度增长率(%)')
    """无限售A股户均持股比例季度增长率(%):"""

    AFAvgHoldSumGRHalfAYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='AFAvgHoldSumGRHalfAYear', column_type='decimal(18,4)', nullable=False, chn_name='无限售A股户均持股数半年增长率(%)')
    """无限售A股户均持股数半年增长率(%):"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布时间')
    """信息发布时间:"""

    AFProportionGRHalfAYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='AFProportionGRHalfAYear', column_type='float', nullable=False, chn_name='无限售A股户均持股比例半年增长率(%)')
    """无限售A股户均持股比例半年增长率(%):"""

    BSHNum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='BSHNum', column_type='int', nullable=False, chn_name='B股股东户数(户)')
    """B股股东户数(户):"""

    BAverageHoldSum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='BAverageHoldSum', column_type='decimal(18,2)', nullable=False, chn_name='B股股东户均持股数(股/户)')
    """B股股东户均持股数(股/户):B股股东户均持股数（BAverageHoldSum）＝B股股本/B股股东户数"""

    BHoldProportionPAccount: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='BHoldProportionPAccount', column_type='float', nullable=False, chn_name='B股户均持股比例(%)')
    """B股户均持股比例(%):"""

    BProportionChange: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='BProportionChange', column_type='float', nullable=False, chn_name='B股相对上一期报告期户均持股比例变化(百分点)')
    """B股相对上一期报告期户均持股比例变化(百分点):"""

    BAvgHoldSumGRQuarter: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='BAvgHoldSumGRQuarter', column_type='decimal(18,4)', nullable=False, chn_name='B股户均持股数季度增长率(%)')
    """B股户均持股数季度增长率(%):"""

    BProportionGRQuarter: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='BProportionGRQuarter', column_type='float', nullable=False, chn_name='B股户均持股比例季度增长率(%)')
    """B股户均持股比例季度增长率(%):"""

    BAvgHoldSumGRHalfAYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='BAvgHoldSumGRHalfAYear', column_type='decimal(18,4)', nullable=False, chn_name='B股户均持股数半年增长率(%)')
    """B股户均持股数半年增长率(%):"""

    BProportionGRHalfAYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='BProportionGRHalfAYear', column_type='float', nullable=False, chn_name='B股户均持股比例半年增长率(%)')
    """B股户均持股比例半年增长率(%):"""

    HSHNum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='HSHNum', column_type='int', nullable=False, chn_name='H股股东户数(户)')
    """H股股东户数(户):"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='InfoSource', column_type='varchar(50)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    HAverageHoldSum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='HAverageHoldSum', column_type='decimal(18,2)', nullable=False, chn_name='H股股东户均持股数(股/户)')
    """H股股东户均持股数(股/户):H股股东户均持股数（HAverageHoldSum）＝H股股本/H股股东户数"""

    HHoldProportionPAccount: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='HHoldProportionPAccount', column_type='float', nullable=False, chn_name='H股户均持股比例(%)')
    """H股户均持股比例(%):"""

    HProportionChange: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='HProportionChange', column_type='float', nullable=False, chn_name='H股相对上一期报告期户均持股比例变化(百分点)')
    """H股相对上一期报告期户均持股比例变化(百分点):"""

    HAvgHoldSumGRQuarter: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='HAvgHoldSumGRQuarter', column_type='decimal(18,4)', nullable=False, chn_name='H股户均持股数季度增长率(%)')
    """H股户均持股数季度增长率(%):"""

    HProportionGRQuarter: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='HProportionGRQuarter', column_type='float', nullable=False, chn_name='H股户均持股比例季度增长率(%)')
    """H股户均持股比例季度增长率(%):"""

    HAvgHoldSumGRHalfAYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='HAvgHoldSumGRHalfAYear', column_type='decimal(18,4)', nullable=False, chn_name='H股户均持股数半年增长率(%)')
    """H股户均持股数半年增长率(%):"""

    HProportionGRHalfAYear: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='HProportionGRHalfAYear', column_type='float', nullable=False, chn_name='H股户均持股比例半年增长率(%)')
    """H股户均持股比例半年增长率(%):"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    SHNum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='SHNum', column_type='int', nullable=False, chn_name='股东总户数(户)')
    """股东总户数(户):"""

    AverageHoldSum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='AverageHoldSum', column_type='decimal(18,2)', nullable=False, chn_name='户均持股数(股/户)')
    """户均持股数(股/户):户均持股数（AverageHoldSum）＝总股本/股东总户数"""

    HoldProportionPAccount: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='HoldProportionPAccount', column_type='float', nullable=False, chn_name='户均持股比例(%)')
    """户均持股比例(%):"""

    ProportionChange: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_SHNumber', column_name='ProportionChange', column_type='float', nullable=False, chn_name='相对上一期报告期户均持股比例变化(百分点)')
    """相对上一期报告期户均持股比例变化(百分点):"""

