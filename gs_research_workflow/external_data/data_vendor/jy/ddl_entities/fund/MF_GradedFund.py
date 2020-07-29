# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_GradedFund(SQLTableEntity):
    name: str = 'MF_GradedFund'
    
    chn_name: str = '公募基金_分级基金主表'
    
    business_unique: str = 'InnerCode,InfoSource,InfoPublDate'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.本表记录分级基金的特有信息，包括A份额约定年基准收益表达式、定期/不定期份额折算说明等；
2.历史数据：2007年7月起-至今。
3.数据来源：基金产品招募说明书。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GradedFund', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GradedFund', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GradedFund', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GradedFund', column_name='InnerCode', column_type='int', nullable=True, chn_name='基金内部编码')
    """基金内部编码:基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GradedFund', column_name='InfoSource', column_type='varchar(100)', nullable=True, chn_name='信息来源')
    """信息来源:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GradedFund', column_name='InfoPublDate', column_type='datetime', nullable=True, chn_name='信息发布日期')
    """信息发布日期:"""

    OperCycle: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GradedFund', column_name='OperCycle', column_type='int', nullable=False, chn_name='运作周期长度')
    """运作周期长度:运作周期长度(OperCycle)与(CT_SystemConst)表中的DM字段关联，令LB=1087，得到运作周期长度的具体描述：1-一个月，2-两个月，3-季度，6-半年，12-年度，24-两年，36-三年，60-五年，99-成立至今，990-期内，993-截止时点，995-周，996-日，999-期末。"""

    AnnualEarningExp: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GradedFund', column_name='AnnualEarningExp', column_type='varchar(1000)', nullable=False, chn_name='A份额约定年基准收益表达式')
    """A份额约定年基准收益表达式:"""

    AnnualEarningRemark: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GradedFund', column_name='AnnualEarningRemark', column_type='varchar(1000)', nullable=False, chn_name='A份额约定年基准收益表达式备注')
    """A份额约定年基准收益表达式备注:"""

    RegularShareCon: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GradedFund', column_name='RegularShareCon', column_type='varchar(1000)', nullable=False, chn_name='定期份额折算说明')
    """定期份额折算说明:"""

    TrampShareCon: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_GradedFund', column_name='TrampShareCon', column_type='varchar(1000)', nullable=False, chn_name='不定份额折算说明')
    """不定份额折算说明:"""

