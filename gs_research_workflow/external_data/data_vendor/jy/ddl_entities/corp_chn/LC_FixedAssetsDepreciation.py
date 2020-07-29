# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class LC_FixedAssetsDepreciation(SQLTableEntity):
    name: str = 'LC_FixedAssetsDepreciation'
    
    chn_name: str = '资产负债表附注_固定资产及折旧明细'
    
    business_unique: str = 'CompanyCode,EndDate,Mark,FixedAssetName'
    
    refresh_freq: str = """季更新"""
    
    comment: str = """1.描述新会计准则下，上市公司固定资产及折旧的明细情况，包括固定资产的原值、累计折旧、减值准备、账面价值、净值等各项的期初、期间变化和期末数据。
2.对于公告原文披露的项目名称，收录在“固定资产名称（FixedAssetName）”中；“固定资产分类（FixedAssetType）”则对披露的科目进行了归类，以便于横向比较。
3.数据范围：2000-12-31至今
4.信息来源：招股说明书、定报、审计报告等"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FixedAssetsDepreciation', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    CurrentIncreaseOC: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FixedAssetsDepreciation', column_name='CurrentIncreaseOC', column_type='decimal(19,4)', nullable=False, chn_name='原值本期增加(元)')
    """原值本期增加(元):"""

    CurrentDecreaseOC: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FixedAssetsDepreciation', column_name='CurrentDecreaseOC', column_type='decimal(19,4)', nullable=False, chn_name='原值本期减少(元)')
    """原值本期减少(元):"""

    EndingOriginalCost: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FixedAssetsDepreciation', column_name='EndingOriginalCost', column_type='decimal(19,4)', nullable=False, chn_name='原值期末数(元)')
    """原值期末数(元):"""

    OpeningAccuDepreciation: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FixedAssetsDepreciation', column_name='OpeningAccuDepreciation', column_type='decimal(19,4)', nullable=False, chn_name='累计折旧期初数(元)')
    """累计折旧期初数(元):"""

    CurrentIncreaseAD: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FixedAssetsDepreciation', column_name='CurrentIncreaseAD', column_type='decimal(19,4)', nullable=False, chn_name='累计折旧本期增加(元)')
    """累计折旧本期增加(元):"""

    CurrentDecreaseAD: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FixedAssetsDepreciation', column_name='CurrentDecreaseAD', column_type='decimal(19,4)', nullable=False, chn_name='累计折旧本期减少(元)')
    """累计折旧本期减少(元):"""

    EndingAccuDepreciation: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FixedAssetsDepreciation', column_name='EndingAccuDepreciation', column_type='decimal(19,4)', nullable=False, chn_name='累计折旧期末数(元)')
    """累计折旧期末数(元):"""

    OpeningDepreReserves: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FixedAssetsDepreciation', column_name='OpeningDepreReserves', column_type='decimal(19,4)', nullable=False, chn_name='减值准备期初数(元)')
    """减值准备期初数(元):"""

    CurrentIncreaseDR: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FixedAssetsDepreciation', column_name='CurrentIncreaseDR', column_type='decimal(19,4)', nullable=False, chn_name='减值准备本期增加(元)')
    """减值准备本期增加(元):"""

    CurrentDecreaseDR: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FixedAssetsDepreciation', column_name='CurrentDecreaseDR', column_type='decimal(19,4)', nullable=False, chn_name='减值准备本期减少(元)')
    """减值准备本期减少(元):"""

    CompanyCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FixedAssetsDepreciation', column_name='CompanyCode', column_type='int', nullable=True, chn_name='公司代码')
    """公司代码:公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。"""

    EndingDepreReserves: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FixedAssetsDepreciation', column_name='EndingDepreReserves', column_type='decimal(19,4)', nullable=False, chn_name='减值准备期末数(元)')
    """减值准备期末数(元):"""

    OpeningBookValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FixedAssetsDepreciation', column_name='OpeningBookValue', column_type='decimal(19,4)', nullable=False, chn_name='账面价值期初数(元)')
    """账面价值期初数(元):"""

    CurrentIncreaseBV: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FixedAssetsDepreciation', column_name='CurrentIncreaseBV', column_type='decimal(19,4)', nullable=False, chn_name='账面价值本期增加(元)')
    """账面价值本期增加(元):"""

    CurrentDecreaseBV: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FixedAssetsDepreciation', column_name='CurrentDecreaseBV', column_type='decimal(19,4)', nullable=False, chn_name='账面价值本期减少(元)')
    """账面价值本期减少(元):"""

    EndingBookValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FixedAssetsDepreciation', column_name='EndingBookValue', column_type='decimal(19,4)', nullable=False, chn_name='账面价值期末数(元)')
    """账面价值期末数(元):"""

    OpeningNetValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FixedAssetsDepreciation', column_name='OpeningNetValue', column_type='decimal(19,4)', nullable=False, chn_name='净值期初数(元)')
    """净值期初数(元):"""

    CurrentIncreaseNV: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FixedAssetsDepreciation', column_name='CurrentIncreaseNV', column_type='decimal(19,4)', nullable=False, chn_name='净值本期增加(元)')
    """净值本期增加(元):"""

    CurrentDecreaseNV: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FixedAssetsDepreciation', column_name='CurrentDecreaseNV', column_type='decimal(19,4)', nullable=False, chn_name='净值本期减少(元)')
    """净值本期减少(元):"""

    EndingNetValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FixedAssetsDepreciation', column_name='EndingNetValue', column_type='decimal(19,4)', nullable=False, chn_name='净值期末数(元)')
    """净值期末数(元):"""

    Remarks: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FixedAssetsDepreciation', column_name='Remarks', column_type='varchar(500)', nullable=False, chn_name='备注')
    """备注:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FixedAssetsDepreciation', column_name='EndDate', column_type='datetime', nullable=True, chn_name='截止日期')
    """截止日期:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FixedAssetsDepreciation', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FixedAssetsDepreciation', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FixedAssetsDepreciation', column_name='InfoSource', column_type='varchar(50)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    Mark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FixedAssetsDepreciation', column_name='Mark', column_type='int', nullable=False, chn_name='合并调整标志')
    """合并调整标志:合并调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1511，得到合并调整标志的具体描述：1-合并调整，2-合并未调整，3-母公司调整，4-母公司未调整，5-专项合并调整，6-专项合并未调整。"""

    FixedAssetName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FixedAssetsDepreciation', column_name='FixedAssetName', column_type='varchar(100)', nullable=False, chn_name='固定资产名称')
    """固定资产名称:"""

    FixedAssetType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FixedAssetsDepreciation', column_name='FixedAssetType', column_type='int', nullable=False, chn_name='固定资产分类')
    """固定资产分类:固定资产分类(FixedAssetType)与(CT_SystemConst)表中的DM字段关联，令LB = 1027，得到固定资产分类的具体描述：10-土地、房屋及建筑物，13-机器机械设备，15-运输设备，16-电气设备，17-电子设备，19-计算机及辅助设备，21-通讯设备，22-仪器仪表、计量标准器具及量具、衡器，23-办公设备，25-通用设备，27..."""

    FixedAssetNo: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FixedAssetsDepreciation', column_name='FixedAssetNo', column_type='int', nullable=False, chn_name='序号')
    """序号:序号（FixedAssetNo）：本字段描述各固定资产在公告原文上的排列序号，以方便展示。"""

    OpeningOriginalCost: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='LC_FixedAssetsDepreciation', column_name='OpeningOriginalCost', column_type='decimal(19,4)', nullable=False, chn_name='原值期初数(元)')
    """原值期初数(元):"""

