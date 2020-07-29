# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class MF_ChargeRateNew(SQLTableEntity):
    name: str = 'MF_ChargeRateNew'
    
    chn_name: str = '公募基金费率(新)'
    
    business_unique: str = 'InnerCode,ExcuteDate,ChargeRateType,ClientType,ShiftInTarget,ChargeRateDiv'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.本表记录基金的相关费率数据及执行情况，包括认购费、申购费、赎回费、管理费、托管费等详细费用。
2.历史数据：1998年3月起-至今。
3.信息来源：基金公司官网披露的产品说明书。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    ChargeRateCur: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='ChargeRateCur', column_type='int', nullable=False, chn_name='费率币种')
    """费率币种:费率币种(ChargeRateCur)与(CT_SystemConst)表中的DM字段关联，令LB=1068 AND DM IN (1000,1100,1420)，得到费率币种的具体描述：1000-美元，1100-港元，1420-人民币元。"""

    ClientType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='ClientType', column_type='int', nullable=True, chn_name='适用客户类型')
    """适用客户类型:适用客户类型(ClientType)与(CT_SystemConst)表中的DM字段关联，令LB=1807，得到适用客户类型的具体描述：10-一般投资者，20-养老金客户，30-住房公积金客户，40-机构投资者，50-一般投资者+养老金客户，99-其他特定客户。"""

    ShiftInInnCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='ShiftInInnCode', column_type='int', nullable=False, chn_name='转入基金代码')
    """转入基金代码:"""

    ShiftInTarget: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='ShiftInTarget', column_type='int', nullable=True, chn_name='转入基金范围')
    """转入基金范围:转入基金范围(ShiftInTarget)与(CT_SystemConst)表中的DM字段关联，令LB = 1899，得到转入基金范围的具体描述：1-基金范围1，2-基金范围2，3-基金范围3，4-基金范围4，5-基金范围5，6-基金范围6。"""

    MinChargeRate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='MinChargeRate', column_type='decimal(19,9)', nullable=False, chn_name='费率最低值')
    """费率最低值:"""

    MaxChargeRate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='MaxChargeRate', column_type='decimal(19,9)', nullable=False, chn_name='费率最高值')
    """费率最高值:"""

    FloChargeRate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='FloChargeRate', column_type='varchar(1000)', nullable=False, chn_name='费率计算方式')
    """费率计算方式:"""

    ChargeRateUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='ChargeRateUnit', column_type='int', nullable=False, chn_name='费率单位')
    """费率单位:费率单位(ChargeRateUnit)与(CT_SystemConst)表中的DM字段关联，令LB=1208 AND DM IN (6,7)，得到费率单位的具体描述：6-%，7-元。"""

    DivIntervalDes: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='DivIntervalDes', column_type='varchar(1000)', nullable=False, chn_name='费率划分区间描述')
    """费率划分区间描述:"""

    ChargeRateDes: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='ChargeRateDes', column_type='varchar(1000)', nullable=False, chn_name='费率描述')
    """费率描述:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='InnerCode', column_type='int', nullable=True, chn_name='基金内部编码')
    """基金内部编码:基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。"""

    ChargeRateDiv: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='ChargeRateDiv', column_type='int', nullable=True, chn_name='费率划分')
    """费率划分:费率划分(ChargeRateDiv)与(CT_SystemConst)表中的DM字段关联，令LB=1898，得到费率划分的具体描述：111000000-申购金额1，111131000-申购金额1持有期限1，111131141-申购金额1持有期限1转换次数1，111131142-申购金额1持有期限1转换次数2，111132000-申购金额1持有期限2，111..."""

    DivStand1: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='DivStand1', column_type='int', nullable=False, chn_name='费率划分标准Ⅰ')
    """费率划分标准Ⅰ:费率划分标准Ⅰ(DivStand1)与(CT_SystemConst)表中的DM字段关联，令LB=1897，得到费率划分标准Ⅰ的具体描述：110-申购金额类，111-申购金额1，112-申购金额2，113-申购金额3，114-申购金额4，115-申购金额5，116-申购金额6，120-申购份额类，121-申购份额1，122-申购份额2，123-申购份额3，1..."""

    DivStandUnit1: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='DivStandUnit1', column_type='int', nullable=False, chn_name='费率划分标准Ⅰ单位')
    """费率划分标准Ⅰ单位:费率划分标准Ⅰ单位(DivStandUnit1)与(CT_SystemConst)表中的DM字段关联，令LB=1208 AND DM IN (1,2,3,4,5,9)，得到费率划分标准Ⅰ单位的具体描述：1-年，2-月，3-日，4-万元，5-万份，6-%,7-元,8-亿美元,9-次,10-亿元,11-万美元,12-万港元,13-个。"""

    StDivStand1: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='StDivStand1', column_type='decimal(19,4)', nullable=False, chn_name='费率划分标准范围Ⅰ起始数值')
    """费率划分标准范围Ⅰ起始数值:"""

    EnDivStand1: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='EnDivStand1', column_type='decimal(19,4)', nullable=False, chn_name='费率划分标准范围Ⅰ截止数值')
    """费率划分标准范围Ⅰ截止数值:"""

    IfApplyStart1: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='IfApplyStart1', column_type='int', nullable=False, chn_name='是否包含范围Ⅰ起始点')
    """是否包含范围Ⅰ起始点:是否包含范围起始点/截止点:该字段固定一下常量, 1-〉是   0-〉否"""

    IfApplyEnd1: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='IfApplyEnd1', column_type='int', nullable=False, chn_name='是否包含范围Ⅰ截止点')
    """是否包含范围Ⅰ截止点:是否包含范围起始点/截止点:该字段固定一下常量, 1-〉是   0-〉否"""

    DivStand2: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='DivStand2', column_type='int', nullable=False, chn_name='费率划分标准Ⅱ')
    """费率划分标准Ⅱ:费率划分标准Ⅱ(DivStand2)与(CT_SystemConst)表中的DM字段关联，令LB = 1897，得到费率划分标准Ⅱ的具体描述：110-申购金额类，111-申购金额1，112-申购金额2，113-申购金额3，114-申购金额4，115-申购金额5，116-申购金额6，120-申购份额类，121-申购份额1，122-申购份额2，123-申购份额3..."""

    DivStandUnit2: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='DivStandUnit2', column_type='int', nullable=False, chn_name='费率划分标准Ⅱ单位')
    """费率划分标准Ⅱ单位:费率划分标准Ⅱ单位(DivStandUnit2)与(CT_SystemConst)表中的DM字段关联，令LB = 1208，得到费率划分标准Ⅱ单位的具体描述：1-年，2-月，3-日，4-万元，5-万份，6-%，7-元，8-亿美元，9-次，10-亿元，11-万美元，12-万港元，13-个，14-美元，15-港元。"""

    StDivStand2: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='StDivStand2', column_type='decimal(19,4)', nullable=False, chn_name='费率划分标准范围Ⅱ起始数值')
    """费率划分标准范围Ⅱ起始数值:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    EnDivStand2: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='EnDivStand2', column_type='decimal(19,4)', nullable=False, chn_name='费率划分标准范围Ⅱ截止数值')
    """费率划分标准范围Ⅱ截止数值:"""

    IfApplyStart2: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='IfApplyStart2', column_type='int', nullable=False, chn_name='是否包含范围Ⅱ起始点')
    """是否包含范围Ⅱ起始点:是否包含范围起始点/截止点:该字段固定一下常量, 1-〉是   0-〉否"""

    IfApplyEnd2: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='IfApplyEnd2', column_type='int', nullable=False, chn_name='是否包含范围Ⅱ截止点')
    """是否包含范围Ⅱ截止点:是否包含范围起始点/截止点:该字段固定一下常量, 1-〉是   0-〉否"""

    DivStand3: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='DivStand3', column_type='int', nullable=False, chn_name='费率划分标准Ⅲ')
    """费率划分标准Ⅲ:费率划分标准Ⅲ(DivStand3)与(CT_SystemConst)表中的DM字段关联，令LB = 1897，得到费率划分标准Ⅲ的具体描述：110-申购金额类，111-申购金额1，112-申购金额2，113-申购金额3，114-申购金额4，115-申购金额5，116-申购金额6，120-申购份额类，121-申购份额1，122-申购份额2，123-申购份额3..."""

    DivStandUnit3: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='DivStandUnit3', column_type='int', nullable=False, chn_name='费率划分标准Ⅲ单位')
    """费率划分标准Ⅲ单位:费率划分标准Ⅲ单位(DivStandUnit3)与(CT_SystemConst)表中的DM字段关联，令LB = 1208，得到费率划分标准Ⅲ单位的具体描述：1-年，2-月，3-日，4-万元，5-万份，6-%，7-元，8-亿美元，9-次，10-亿元，11-万美元，12-万港元，13-个，14-美元，15-港元。"""

    StDivStand3: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='StDivStand3', column_type='decimal(19,4)', nullable=False, chn_name='费率划分标准范围Ⅲ起始数值')
    """费率划分标准范围Ⅲ起始数值:是否包含范围起始点/截止点:该字段固定一下常量, 1-〉是   0-〉否"""

    EnDivStand3: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='EnDivStand3', column_type='decimal(19,4)', nullable=False, chn_name='费率划分标准范围Ⅲ截止数值')
    """费率划分标准范围Ⅲ截止数值:"""

    IfApplyStart3: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='IfApplyStart3', column_type='int', nullable=False, chn_name='是否包含范围Ⅲ起始点')
    """是否包含范围Ⅲ起始点:"""

    IfApplyEnd3: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='IfApplyEnd3', column_type='int', nullable=False, chn_name='是否包含范围Ⅲ截止点')
    """是否包含范围Ⅲ截止点:是否包含范围起始点/截止点:该字段固定一下常量, 1-〉是   0-〉否"""

    Notes: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='Notes', column_type='varchar(1000)', nullable=False, chn_name='备注说明')
    """备注说明:"""

    InfoSource: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='InfoSource', column_type='varchar(100)', nullable=False, chn_name='信息来源')
    """信息来源:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    IfExecuted: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='IfExecuted', column_type='int', nullable=False, chn_name='是否执行')
    """是否执行:是否执行(IfExecuted)与(CT_SystemConst)表中的DM字段关联，令LB=999 AND DM IN (1,2)，得到是否执行的具体描述：1-是，2-否。"""

    ExcuteDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='ExcuteDate', column_type='datetime', nullable=False, chn_name='执行日期')
    """执行日期:"""

    CancelDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='CancelDate', column_type='datetime', nullable=False, chn_name='取消日期')
    """取消日期:"""

    ChargeRateType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='ChargeRateType', column_type='int', nullable=True, chn_name='费率类别')
    """费率类别:费率类别(ChargeRateType)与(CT_SystemConst)表中的DM字段关联，令LB=1896，得到费率类别的具体描述：10010-认购费前端，10011-认购费前端直销网上交易，10012-认购费前端直销柜台，10020-认购费后端，10110-认购费场内前端，10120-认购费场内后端，10210-认购费场外前端，10220-认购费场外后..."""

    ChargeRateTyDes: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='MF_ChargeRateNew', column_name='ChargeRateTyDes', column_type='varchar(300)', nullable=False, chn_name='费率类别描述')
    """费率类别描述:"""

