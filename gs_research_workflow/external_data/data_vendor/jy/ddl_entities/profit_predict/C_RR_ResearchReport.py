# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class C_RR_ResearchReport(SQLTableEntity):
    name: str = 'C_RR_ResearchReport'
    
    chn_name: str = '研究报告'
    
    business_unique: str = '无'
    
    refresh_freq: str = """工作日更新"""
    
    comment: str = """1.本表收录了包括近200家证券、期货、银行等国内外金融机构发布的各类研究报告标题、摘要、作者等相关信息
2.数据范围：2004年至今"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ResearchReport', column_name='ID', column_type='bigint', nullable=False, chn_name='ID')
    """ID:"""

    ObjectCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ResearchReport', column_name='ObjectCode', column_type='int', nullable=False, chn_name='信息对象')
    """信息对象:信息对象(ObjectCode)与(CT_SystemConst)表中的DM字段关联，令LB=1008，得到信息对象的具体描述：1000-股票，1001-A股，1003-B股，1004-H股，1005-红筹股，1006-个股期权，1007-权证，1009-股指期货，1010-中国存托凭证，1300-基金，1301-封闭式基金，1303-开放式基金，1500-..."""

    AreaCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ResearchReport', column_name='AreaCode', column_type='int', nullable=False, chn_name='信息地域划分')
    """信息地域划分:信息地域划分(AreaCode)与(CT_SystemConst)表中的DM字段关联，令LB=1023，得到信息地域划分的具体描述：3-港澳台，4-中东地区，7-国际，100-亚洲，101-阿富汗，102-巴林，103-孟加拉国，104-不丹，105-文莱，106-缅甸，107-柬埔寨，108-塞浦路斯，109-朝鲜，110-中国香港，111-印度，112-..."""

    MarketCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ResearchReport', column_name='MarketCode', column_type='int', nullable=False, chn_name='信息涉及市场')
    """信息涉及市场:信息涉及市场(MarketCode)与(CT_SystemConst)表中的DM字段关联，令LB=1009，得到信息涉及市场的具体描述：1001-主板，1004-中小企业板，1005-创业板，1007-三板市场，1010-银行间市场，1013-柜台市场。"""

    Author: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ResearchReport', column_name='Author', column_type='varchar(200)', nullable=False, chn_name='撰写作者')
    """撰写作者:"""

    Contacts: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ResearchReport', column_name='Contacts', column_type='varchar(100)', nullable=False, chn_name='联系人')
    """联系人:"""

    WritingDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ResearchReport', column_name='WritingDate', column_type='datetime', nullable=False, chn_name='撰写日期')
    """撰写日期:"""

    InnerCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ResearchReport', column_name='InnerCode', column_type='int', nullable=False, chn_name='证券内码')
    """证券内码:"""

    Industry: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ResearchReport', column_name='Industry', column_type='int', nullable=False, chn_name='所属行业')
    """所属行业:"""

    IndustrySW: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ResearchReport', column_name='IndustrySW', column_type='int', nullable=False, chn_name='所属行业(申万)')
    """所属行业(申万):"""

    Conclusion: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ResearchReport', column_name='Conclusion', column_type='text', nullable=False, chn_name='报告结论')
    """报告结论:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ResearchReport', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    InvestAdvice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ResearchReport', column_name='InvestAdvice', column_type='int', nullable=False, chn_name='投资建议')
    """投资建议:"""

    RatingDescription: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ResearchReport', column_name='RatingDescription', column_type='varchar(100)', nullable=False, chn_name='投资评级描述')
    """投资评级描述:该字段已停止维护，评级信息可参考“研究报告-目标价与评级（C_RR_GoalPriceRate）”中评级相关字段。"""

    RatingCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ResearchReport', column_name='RatingCode', column_type='int', nullable=False, chn_name='投资评级')
    """投资评级:该字段已停止维护，评级信息可参考“研究报告-目标价与评级（C_RR_GoalPriceRate）”中评级相关字段。"""

    Language: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ResearchReport', column_name='Language', column_type='int', nullable=False, chn_name='语言')
    """语言:语言(Language)与(CT_SystemConst)表中的DM字段关联，令LB=1638，得到语言的具体描述：1-中文，2-英文。"""

    PageNum: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ResearchReport', column_name='PageNum', column_type='int', nullable=False, chn_name='页数')
    """页数:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ResearchReport', column_name='UpdateTime', column_type='datetime', nullable=False, chn_name='修改时间')
    """修改时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ResearchReport', column_name='JSID', column_type='bigint', nullable=False, chn_name='JSID')
    """JSID:"""

    ReportType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ResearchReport', column_name='ReportType', column_type='int', nullable=False, chn_name='研究报告类别')
    """研究报告类别:研究报告类别(ReportType)与(CT_SystemConst)表中的DM字段关联，令LB=1584，得到研究报告类别的具体描述：1-晨报，2-市场动态，3-宏观，4-策略，5-行业，6-公司，7-港股，8-创业板，9-基金，10-债券，11-金融工程，12-主题概念，13-英文报告。"""

    ResearchDepth: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ResearchReport', column_name='ResearchDepth', column_type='int', nullable=False, chn_name='研究深度')
    """研究深度:研究深度(ResearchDepth)与(CT_SystemConst)表中的DM字段关联，令LB=1585，得到研究深度的具体描述：1-点评，2-年度，3-半年度，4-季度，5-月度，6-周报，7-深度，8-境外经济，9-境外金融，10-策略专题，11-行业（年度），12-行业（半年度），13-行业（季度），14-行业（月度），15-行业策略（年度），16..."""

    Colume: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ResearchReport', column_name='Colume', column_type='int', nullable=False, chn_name='栏目选择')
    """栏目选择:栏目选择(Colume)与(CT_SystemConst)表中的DM字段关联，令LB=1312，得到栏目选择的具体描述：1000-经济简评，1030-经济定期研究，1050-经济深度研究，2010-市场短期评论，2030-市场投资策略，2040-市场简要分析，2050-市场定期研究，2070-市场深度研究，2110-板块简评，2130-板块投资策略，2150..."""

    OrgCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ResearchReport', column_name='OrgCode', column_type='int', nullable=False, chn_name='撰写机构')
    """撰写机构:"""

    OrgName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ResearchReport', column_name='OrgName', column_type='varchar(100)', nullable=False, chn_name='撰写机构名称')
    """撰写机构名称:"""

    OrgNameDisc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ResearchReport', column_name='OrgNameDisc', column_type='varchar(100)', nullable=False, chn_name='撰写机构名称(信息来源)')
    """撰写机构名称(信息来源):"""

    Title: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='C_RR_ResearchReport', column_name='Title', column_type='varchar(200)', nullable=False, chn_name='标题')
    """标题:"""

