# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_SplitCombinationShare(SQLTableEntity):
    name: str = 'HK_SplitCombinationShare'
    
    chn_name: str = '港股拆股并股'
    
    business_unique: str = 'InnerCode,DirDeciPublDate'
    
    refresh_freq: str = """不定时更新"""
    
    comment: str = """1.记录港股拆股并股的方案描述、重组方案、变更数据、临时交易柜台安排和买卖零碎股之安排。
2.数据范围：1999年至今。
3.信息来源：港交所。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    SupplementaryType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='SupplementaryType', column_type='int', nullable=False, chn_name='配套方案类别')
    """配套方案类别:配套方案类别(SupplementaryType)与(CT_SystemConst)表中的DM字段关联，令LB = 1348，得到配套方案类别的具体描述：10-增发，20-分红。"""

    Process: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='Process', column_type='int', nullable=False, chn_name='事件进程')
    """事件进程:事件进程(Process)与(CT_SystemConst)表中的DM字段关联，令LB = 1059，得到事件进程的具体描述：1000-意向，1001-预案，1004-决案，1007-否决，1010-申请，1013-批准，1016-未实施终止，1019-实施中，1022-实施完成，1025-解除，1028-到期，1041-续签，1043-部分续签，1051-..."""

    ReformType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='ReformType', column_type='int', nullable=False, chn_name='重组方式')
    """重组方式:重组方式(ReformType)与(CT_SystemConst)表中的DM字段关联，令LB = 1346，得到重组方式的具体描述：10-并股，15-拆股，20-先并后拆，25-先拆后并。"""

    CombinationX: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='CombinationX', column_type='int', nullable=False, chn_name='合并(X合Y)-X')
    """合并(X合Y)-X:"""

    CombinationY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='CombinationY', column_type='int', nullable=False, chn_name='合并(X合Y)-Y')
    """合并(X合Y)-Y:"""

    SplitX: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='SplitX', column_type='int', nullable=False, chn_name='拆细(X拆Y)-X')
    """拆细(X拆Y)-X:"""

    SplitY: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='SplitY', column_type='int', nullable=False, chn_name='拆细(X拆Y)-Y')
    """拆细(X拆Y)-Y:"""

    CurrencyUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='CurrencyUnit', column_type='int', nullable=False, chn_name='面值单位')
    """面值单位:面值单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068，得到面值单位的具体描述：1000-美元，1100-港元，1110-印度卢比，1120-印度尼西亚卢比，1130-伊朗里亚尔，1140-波兰兹罗提，1150-匈牙利福林，1160-日本元，1161-欧洲日元(离岸)，1170-约旦第纳尔，1180-科..."""

    OldParValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='OldParValue', column_type='decimal(18,8)', nullable=False, chn_name='旧面值')
    """旧面值:"""

    NewParValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='NewParValue', column_type='decimal(18,8)', nullable=False, chn_name='新面值')
    """新面值:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='InnerCode', column_type='int', nullable=True, chn_name='内部编码')
    """内部编码:内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。"""

    WriteOffBase: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='WriteOffBase', column_type='int', nullable=False, chn_name='注销基准')
    """注销基准:注销基准(WriteOffBase)与(CT_SystemConst)表中的DM字段关联，令LB = 1347，得到注销基准的具体描述：1-旧面值，2-新面值。"""

    WriteOffParValue: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='WriteOffParValue', column_type='decimal(18,8)', nullable=False, chn_name='注销面值(元/股)')
    """注销面值(元/股):"""

    OldTradeUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='OldTradeUnit', column_type='int', nullable=False, chn_name='旧买卖单位(股/手)')
    """旧买卖单位(股/手):"""

    NewTradeUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='NewTradeUnit', column_type='int', nullable=False, chn_name='新买卖单位(股/手)')
    """新买卖单位(股/手):"""

    SharesIssued: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='SharesIssued', column_type='decimal(18,2)', nullable=False, chn_name='已发行股数')
    """已发行股数:"""

    SharesAfterEffect: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='SharesAfterEffect', column_type='decimal(18,2)', nullable=False, chn_name='生效后股数')
    """生效后股数:"""

    TempShareCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='TempShareCode', column_type='varchar(10)', nullable=False, chn_name='临时证券代码')
    """临时证券代码:"""

    TempShareAbbrName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='TempShareAbbrName', column_type='varchar(50)', nullable=False, chn_name='临时证券简称')
    """临时证券简称:"""

    TempTradeUnit: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='TempTradeUnit', column_type='int', nullable=False, chn_name='临时买卖单位(股/手)')
    """临时买卖单位(股/手):"""

    TempTradeBeginDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='TempTradeBeginDate', column_type='datetime', nullable=False, chn_name='临时买卖开始日')
    """临时买卖开始日:"""

    DirDeciPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='DirDeciPublDate', column_type='datetime', nullable=False, chn_name='董事会公告日')
    """董事会公告日:"""

    SimulTradeBeginDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='SimulTradeBeginDate', column_type='datetime', nullable=False, chn_name='并行买卖开始日')
    """并行买卖开始日:"""

    SimulTradeEndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='SimulTradeEndDate', column_type='datetime', nullable=False, chn_name='并行买卖结束日')
    """并行买卖结束日:"""

    OddLotsTradeAgent: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='OddLotsTradeAgent', column_type='varchar(200)', nullable=False, chn_name='买卖零碎股代理人')
    """买卖零碎股代理人:"""

    AgentCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='AgentCode', column_type='int', nullable=False, chn_name='代理人编号')
    """代理人编号:代理人编号（AgentCode）：与机构基本资料(LC_InstiArchive)中的企业编号(CompanyCode)关联，得到具体的代理人编号和名称。"""

    AgentTel: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='AgentTel', column_type='varchar(50)', nullable=False, chn_name='代理人电话')
    """代理人电话:"""

    AgentAddr: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='AgentAddr', column_type='varchar(200)', nullable=False, chn_name='代理人地址')
    """代理人地址:"""

    OddLotsTradeBeginDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='OddLotsTradeBeginDate', column_type='datetime', nullable=False, chn_name='零碎股买卖开始日')
    """零碎股买卖开始日:"""

    OddLotsTradeEndDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='OddLotsTradeEndDate', column_type='datetime', nullable=False, chn_name='零碎股买卖截至日')
    """零碎股买卖截至日:"""

    Statement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='Statement', column_type='varchar(500)', nullable=False, chn_name='备注')
    """备注:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='修改日期')
    """修改日期:"""

    DirDeciSignDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='DirDeciSignDate', column_type='datetime', nullable=False, chn_name='董事会公告签署日')
    """董事会公告签署日:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    SMDeciDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='SMDeciDate', column_type='datetime', nullable=False, chn_name='股东大会决议日')
    """股东大会决议日:"""

    CircularPunlDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='CircularPunlDate', column_type='datetime', nullable=False, chn_name='通函公布日')
    """通函公布日:"""

    ExpirePublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='ExpirePublDate', column_type='datetime', nullable=False, chn_name='终止实施公告日')
    """终止实施公告日:"""

    EffectDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='EffectDate', column_type='datetime', nullable=False, chn_name='生效日期')
    """生效日期:"""

    SchemeStatement: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_SplitCombinationShare', column_name='SchemeStatement', column_type='varchar(1000)', nullable=False, chn_name='方案说明')
    """方案说明:"""

