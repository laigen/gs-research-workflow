# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class HK_Information(SQLTableEntity):
    name: str = 'HK_Information'
    
    chn_name: str = '港股动态信息表'
    
    business_unique: str = '需媒体版权'
    
    refresh_freq: str = """日更新"""
    
    comment: str = """1.介绍港股的信息、涉及股市的评论以及证券知识等，该表新闻内容来自网页抓取，新闻内容丰富。
2.数据范围：2002年至今。
3.数据来源：新浪、腾讯、阿斯达克等。"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Information', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    InvolvedStock: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Information', column_name='InvolvedStock', column_type='int', nullable=False, chn_name='相关股票')
    """相关股票:"""

    Keyword: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Information', column_name='Keyword', column_type='int', nullable=False, chn_name='关键词')
    """关键词:"""

    ObjectCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Information', column_name='ObjectCode', column_type='int', nullable=False, chn_name='信息对象')
    """信息对象:信息对象(ObjectCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1008，得到信息对象的具体描述：1000-股票，1001-A股，1003-B股，1004-H股，1005-红筹股，1006-个股期权，1007-权证，1009-股指期货，1010-中国存托凭证，1300-基金，1301-封闭式基金，1303-开放式基金，150..."""

    AreaCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Information', column_name='AreaCode', column_type='int', nullable=False, chn_name='信息地域划分')
    """信息地域划分:信息地域划分(AreaCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1023，得到信息地域划分的具体描述：3-港澳台，4-中东地区，7-国际，100-亚洲，101-阿富汗，102-巴林，103-孟加拉国，104-不丹，105-文莱，106-缅甸，107-柬埔寨，108-塞浦路斯，109-朝鲜，110-中国香港，111-印度，11..."""

    Province: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Information', column_name='Province', column_type='int', nullable=False, chn_name='省市')
    """省市:"""

    Industry: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Information', column_name='Industry', column_type='int', nullable=False, chn_name='行业')
    """行业:"""

    MarketCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Information', column_name='MarketCode', column_type='int', nullable=False, chn_name='信息涉及市场')
    """信息涉及市场:"""

    InvolvedInstitution: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Information', column_name='InvolvedInstitution', column_type='int', nullable=False, chn_name='涉及机构')
    """涉及机构:涉及机构（InvolvedInstitution）：与“机构基本资料表(LC_InstiArchive)”中的“公司代码(CompanyCode)”关联，得到“涉及机构”的具体说明。"""

    MarketOpinionCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Information', column_name='MarketOpinionCode', column_type='int', nullable=False, chn_name='股市评论意见类型')
    """股市评论意见类型:"""

    StockOpinionCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Information', column_name='StockOpinionCode', column_type='int', nullable=False, chn_name='个股推荐意见类型')
    """个股推荐意见类型:"""

    InfoType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Information', column_name='InfoType', column_type='varchar(50)', nullable=False, chn_name='信息类别')
    """信息类别:"""

    Conclusion: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Information', column_name='Conclusion', column_type='varchar(500)', nullable=False, chn_name='个股推荐/股市评论结论')
    """个股推荐/股市评论结论:"""

    ForecastLowestPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Information', column_name='ForecastLowestPrice', column_type='decimal(19,4)', nullable=False, chn_name='预测价位最低价(元)')
    """预测价位最低价(元):"""

    ForecastHighestPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Information', column_name='ForecastHighestPrice', column_type='decimal(19,4)', nullable=False, chn_name='预测价位最高价(元)')
    """预测价位最高价(元):"""

    ContentType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Information', column_name='ContentType', column_type='int', nullable=False, chn_name='证券知识内容类别')
    """证券知识内容类别:"""

    SpecialCategory: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Information', column_name='SpecialCategory', column_type='int', nullable=False, chn_name='所属专题')
    """所属专题:"""

    InfoLevel: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Information', column_name='InfoLevel', column_type='int', nullable=False, chn_name='信息级别')
    """信息级别:信息级别（InfoLevel）取值为0、1、2，信息级别越高，内容的重要性等级越高。"""

    RecordDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Information', column_name='RecordDate', column_type='datetime', nullable=False, chn_name='记录录入时间')
    """记录录入时间:"""

    XGRQ: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Information', column_name='XGRQ', column_type='datetime', nullable=True, chn_name='修改日期')
    """修改日期:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Information', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Information', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    Media: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Information', column_name='Media', column_type='varchar(50)', nullable=False, chn_name='媒体出处')
    """媒体出处:"""

    Category: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Information', column_name='Category', column_type='int', nullable=False, chn_name='栏目选择')
    """栏目选择:栏目选择(Category)与(CT_SystemConst)表中的DM字段关联，令LB = 1007，得到栏目选择的具体描述：1-证券市场动态，2-证券市场研究，3-股市评论，4-个股推荐，5-公司研究，6-公司动态，7-新股发行介绍，8-新股上市定位，9-板块分析，10-财经时事，11-宏观分析，12-行业动态，13-行业分析，14-行业政策，15-证券..."""

    InfoTitle: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Information', column_name='InfoTitle', column_type='varchar(255)', nullable=False, chn_name='标题')
    """标题:"""

    Content: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Information', column_name='Content', column_type='text', nullable=False, chn_name='内容')
    """内容:"""

    Writer: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Information', column_name='Writer', column_type='varchar(50)', nullable=False, chn_name='撰写机构')
    """撰写机构:"""

    Author: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='HK_Information', column_name='Author', column_type='varchar(50)', nullable=False, chn_name='撰写作者')
    """撰写作者:"""

