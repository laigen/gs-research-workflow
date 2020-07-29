# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_SharesChange(SQLTableEntity):
    name: str = 'MF_SharesChange'
    
    chn_name: str = '公募基金份额变动'
    
    business_unique: str = 'InnerCode,EndDate,StatPeriod'
    
    refresh_freq: str = """交易所上市基金（如ETF、LOF）日更新，其他基金季更新"""
    
    comment: str = """1.本表记录基金份额变动情况，包括期初份额，本期申购或赎回，期末份额等数据，份额变化的绝对值、变化率等数据。
2.历史数据：1998年3月起-至今。
3.数据来源：基金公司披露的定期报告。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_SharesChange', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    EndShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_SharesChange', column_name='EndShares', column_type='decimal(18,4)', nullable=False, chn_name='期末份额(份)')
    """期末份额(份):"""

    SharesChange: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_SharesChange', column_name='SharesChange', column_type='decimal(18,4)', nullable=False, chn_name='基金份额变化(申购赎回净额)(份)')
    """基金份额变化(申购赎回净额)(份):基金份额变化（SharesChange）：即申购赎回净额，由“本期末基金份额-上期末基金份额”计算得到。"""

    RateOfSharesChange: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_SharesChange', column_name='RateOfSharesChange', column_type='decimal(18,6)', nullable=False, chn_name='基金份额变化率(%)')
    """基金份额变化率(%):基金份额变化率（RateOfSharesChange）=（本期末基金份额-上期末基金份额）/上期末基金份额*100%"""

    FloatShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_SharesChange', column_name='FloatShares', column_type='decimal(18,4)', nullable=False, chn_name='流通份额(份)')
    """流通份额(份):流通份额（FloatShares）：当“统计区间（StatPeriod）”等于996-日，为交易所公布每日场内份额数据当“统计区间（StatPeriod）”不等于996-日，针对封闭式基金，等于基金总份额减去发起人持有份额。"""

    DividendReinvestment: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_SharesChange', column_name='DividendReinvestment', column_type='decimal(18,4)', nullable=False, chn_name='红利再投资(份)')
    """红利再投资(份):"""

    ShgiftIn: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_SharesChange', column_name='ShgiftIn', column_type='decimal(18,4)', nullable=False, chn_name='同系基金转入(份)')
    """同系基金转入(份):"""

    ShiftOut: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_SharesChange', column_name='ShiftOut', column_type='decimal(18,4)', nullable=False, chn_name='同系基金转出(份)')
    """同系基金转出(份):"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_SharesChange', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新日期')
    """更新日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_SharesChange', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    IfCombine: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_SharesChange', column_name='IfCombine', column_type='int', nullable=False, chn_name='是否合并披露')
    """是否合并披露:是否合并披露（IfCombine），该字段固定以下常量：1-是； 0-否"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_SharesChange', column_name='InnerCode', column_type='int', nullable=True, chn_name='基金内部编码')
    """基金内部编码:基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_SharesChange', column_name='InfoSource', column_type='varchar(100)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    StatPeriod: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_SharesChange', column_name='StatPeriod', column_type='varchar(20)', nullable=False, chn_name='统计区间')
    """统计区间:统计区间(StatPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 1087 AND DM IN (3,6,12,993,995,996)，得到统计区间的具体描述：3-季度，6-半年，12-年度，993-截止时点，995-周，996-日。"""

    StartDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_SharesChange', column_name='StartDate', column_type='datetime', nullable=False, chn_name='起始日期')
    """起始日期:"""

    EndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_SharesChange', column_name='EndDate', column_type='datetime', nullable=False, chn_name='截止日期')
    """截止日期:"""

    StartShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_SharesChange', column_name='StartShares', column_type='decimal(18,4)', nullable=False, chn_name='期初份额(份)')
    """期初份额(份):"""

    ApplyingShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_SharesChange', column_name='ApplyingShares', column_type='decimal(18,4)', nullable=False, chn_name='加:本期申购(份)')
    """加:本期申购(份):"""

    RedeemShares: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_SharesChange', column_name='RedeemShares', column_type='decimal(18,4)', nullable=False, chn_name='减:本期赎回(份)')
    """减:本期赎回(份):"""

