# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class C_RR_GoalPriceRate(SQLTableEntity):
    name: str = 'C_RR_GoalPriceRate'
    
    chn_name: str = '研究报告_目标价与评级'
    
    business_unique: str = 'OID,Title,InnerCode,IndustryName'
    
    refresh_freq: str = """工作日更新"""
    
    comment: str = """1.本表主要收录各研究机构对市场上流通股票的目标价预测和评级，以及对行业的预测评级等数据信息。
2.数据范围：2004年至今
3.信息来源：各机构发布的研究报告"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_GoalPriceRate', column_name='ID', column_type='bigint', nullable=False, chn_name='ID')
    """ID:"""

    SecuCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_GoalPriceRate', column_name='SecuCode', column_type='varchar(20)', nullable=False, chn_name='证券代码')
    """证券代码:"""

    SecuAbbr: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_GoalPriceRate', column_name='SecuAbbr', column_type='varchar(20)', nullable=False, chn_name='证券简称')
    """证券简称:"""

    IndustryName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_GoalPriceRate', column_name='IndustryName', column_type='varchar(100)', nullable=False, chn_name='行业名称')
    """行业名称:"""

    IndustryCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_GoalPriceRate', column_name='IndustryCode', column_type='int', nullable=False, chn_name='行业代码')
    """行业代码:行业代码（Industry）：用该表原文ID（OID）与 研究报告（C_RR_ResearchReport）的ID关联，取研究报告表的InfoPublDate判断。当InfoPublDate>=2012-10-27时，行业分类标准为证监会行业分类2012版，对应系统常量表(CT_SystemConst)中的类别为LB=1755；当InfoPublDate<2..."""

    IndustrySW: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_GoalPriceRate', column_name='IndustrySW', column_type='int', nullable=False, chn_name='行业代码(申万)')
    """行业代码(申万):行业代码(申万)(IndustrySW)与(CT_SystemConst)表中的DM字段关联，令LB=1804，得到行业代码(申万)的具体描述：110000-农林牧渔，110100-种植业，110101-种子生产，110102-粮食种植，110103-其他种植业，110200-渔业，110201-海洋捕捞，110202-水产养殖，110300-林业，1103..."""

    MoneyUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_GoalPriceRate', column_name='MoneyUnit', column_type='int', nullable=False, chn_name='货币单位')
    """货币单位:货币单位(MoneyUnit)与(CT_SystemConst)表中的DM字段关联，令LB=1068，得到货币单位的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，1170-约旦第纳尔，1180-科威特第纳尔..."""

    FirstDayPriceMax: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_GoalPriceRate', column_name='FirstDayPriceMax', column_type='decimal(19,4)', nullable=False, chn_name='首日价格上限')
    """首日价格上限:"""

    FirstDayPriceMin: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_GoalPriceRate', column_name='FirstDayPriceMin', column_type='decimal(19,4)', nullable=False, chn_name='首日价格下限')
    """首日价格下限:"""

    GoalPriceMax: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_GoalPriceRate', column_name='GoalPriceMax', column_type='decimal(19,4)', nullable=False, chn_name='目标价格上限')
    """目标价格上限:"""

    GoalPriceMin: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_GoalPriceRate', column_name='GoalPriceMin', column_type='decimal(19,4)', nullable=False, chn_name='目标价格下限')
    """目标价格下限:"""

    OID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_GoalPriceRate', column_name='OID', column_type='bigint', nullable=False, chn_name='原文ID')
    """原文ID:原文ID（OID）：与研究报告（C_RR_ResearchReport）表的ID关联，得到对应研究报告的详细信息。"""

    GoalPriceStartDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_GoalPriceRate', column_name='GoalPriceStartDate', column_type='datetime', nullable=False, chn_name='目标价格有效起始期')
    """目标价格有效起始期:"""

    GoalPriceEndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_GoalPriceRate', column_name='GoalPriceEndDate', column_type='datetime', nullable=False, chn_name='目标价格有效结束期')
    """目标价格有效结束期:"""

    ForecastValidate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_GoalPriceRate', column_name='ForecastValidate', column_type='int', nullable=False, chn_name='预测有效期(月)')
    """预测有效期(月):"""

    Notes: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_GoalPriceRate', column_name='Notes', column_type='varchar(1000)', nullable=False, chn_name='备注说明')
    """备注说明:"""

    ExRightGoalPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_GoalPriceRate', column_name='ExRightGoalPrice', column_type='decimal(19,4)', nullable=False, chn_name='除权目标价格(元)')
    """除权目标价格(元):"""

    CurrentRatingDesc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_GoalPriceRate', column_name='CurrentRatingDesc', column_type='varchar(100)', nullable=False, chn_name='本期评级描述')
    """本期评级描述:"""

    CurrentRating: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_GoalPriceRate', column_name='CurrentRating', column_type='int', nullable=False, chn_name='本期评级')
    """本期评级:本期评级(CurrentRating)与(CT_SystemConst)表中的DM字段关联，令LB=1335，得到本期评级的具体描述：10-买入，13-增持，20-中性，30-减持，33-卖出，99-未评级。"""

    LastRatingDesc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_GoalPriceRate', column_name='LastRatingDesc', column_type='varchar(100)', nullable=False, chn_name='上期评级描述')
    """上期评级描述:"""

    LastRating: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_GoalPriceRate', column_name='LastRating', column_type='int', nullable=False, chn_name='上期评级')
    """上期评级:上期评级(LastRating)与(CT_SystemConst)表中的DM字段关联，令LB=1335，得到上期评级的具体描述：10-买入，13-增持，20-中性，30-减持，33-卖出，99-未评级。"""

    Attention: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_GoalPriceRate', column_name='Attention', column_type='int', nullable=False, chn_name='关注度')
    """关注度:关注度（Attention），该字段固定以下常量：0-非首次覆盖；1-首次关注（首次覆盖但未评级）；2-首次评级（首次覆盖且评级）；"""

    Title: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_GoalPriceRate', column_name='Title', column_type='varchar(200)', nullable=False, chn_name='标题')
    """标题:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_GoalPriceRate', column_name='UpdateTime', column_type='datetime', nullable=False, chn_name='更新时间')
    """更新时间:"""

    ReleaseTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_GoalPriceRate', column_name='ReleaseTime', column_type='datetime', nullable=False, chn_name='发布时间')
    """发布时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_GoalPriceRate', column_name='JSID', column_type='bigint', nullable=False, chn_name='JSID')
    """JSID:"""

    OrgCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_GoalPriceRate', column_name='OrgCode', column_type='int', nullable=False, chn_name='撰写机构')
    """撰写机构:"""

    OrgName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_GoalPriceRate', column_name='OrgName', column_type='varchar(100)', nullable=False, chn_name='撰写机构名称')
    """撰写机构名称:"""

    WritingDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_GoalPriceRate', column_name='WritingDate', column_type='datetime', nullable=False, chn_name='撰写日期')
    """撰写日期:"""

    ObjectCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_GoalPriceRate', column_name='ObjectCode', column_type='int', nullable=False, chn_name='信息对象')
    """信息对象:信息对象(ObjectCode)与(CT_SystemConst)表中的DM字段关联，令LB=1008，得到信息对象的具体描述：1000-股票，1001-A股，1003-B股，1004-H股，1005-红筹股，1006-个股期权，1007-权证，1009-股指期货，1010-中国存托凭证，1300-基金，1301-封闭式基金，1303-开放式基金，1500-..."""

    AreaCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_GoalPriceRate', column_name='AreaCode', column_type='int', nullable=False, chn_name='信息地域划分')
    """信息地域划分:信息地域划分(AreaCode)与(CT_SystemConst)表中的DM字段关联，令LB=1023，得到信息地域划分的具体描述：3-港澳台，4-中东地区，7-国际，100-亚洲，101-阿富汗，102-巴林，103-孟加拉国，104-不丹，105-文莱，106-缅甸，107-柬埔寨，108-塞浦路斯，109-朝鲜，110-中国香港，111-印度，112-..."""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_GoalPriceRate', column_name='InnerCode', column_type='int', nullable=False, chn_name='证券内部编码')
    """证券内部编码:证券内部编码(InnerCode)：当股票在主板、创业板和三板上市时，与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联，得到对应股票的证券代码、简称等；当股票在香港上市时，与“港股证券主表（HK_SecuMain）”中的“证券内部编码(InnerCode)”关联，得到对应股票的证券代码、简称等。"""

