# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class NI_News(SQLTableEntity):
    name: str = 'NI_News'
    
    chn_name: str = '新闻资讯'
    
    business_unique: str = '需媒体版权'
    
    refresh_freq: str = """滚动更新"""
    
    comment: str = """1.收录各主流媒体发布的新闻资讯，包括公司新闻、行业新闻、市场动态、行业政策、财经时事、宏观分析、财经简评等栏目。
2.数据范围：2001-至今"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    Writer: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='Writer', column_type='varchar(50)', nullable=False, chn_name='撰写机构')
    """撰写机构:"""

    Author: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='Author', column_type='varchar(50)', nullable=False, chn_name='撰写作者')
    """撰写作者:"""

    InvolvedStock: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='InvolvedStock', column_type='int', nullable=False, chn_name='相关股票')
    """相关股票:"""

    Keyword: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='Keyword', column_type='int', nullable=False, chn_name='关键词')
    """关键词:"""

    ObjectCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='ObjectCode', column_type='int', nullable=False, chn_name='信息对象')
    """信息对象:信息对象(ObjectCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1008，得到信息对象的具体描述：1000-股票，1001-A股，1003-B股，1004-H股，1005-红筹股，1006-个股期权，1007-权证，1009-股指期货，1010-中国存托凭证，1300-基金，1301-封闭式基金，1303-开放式基金，150..."""

    AreaCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='AreaCode', column_type='int', nullable=False, chn_name='信息地域划分')
    """信息地域划分:信息地域划分(AreaCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1023，得到信息地域划分的具体描述：3-港澳台，4-中东地区，7-国际，100-亚洲，101-阿富汗，102-巴林，103-孟加拉国，104-不丹，105-文莱，106-缅甸，107-柬埔寨，108-塞浦路斯，109-朝鲜，110-中国香港，111-印度，11..."""

    Province: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='Province', column_type='int', nullable=False, chn_name='省市')
    """省市:省市(Province)与(CT_SystemConst)表中的DM字段关联，令LB = 1145，得到省市的具体描述：1-华北，2-东北，3-华东，4-中南，5-西南，6-西北，11-东部，13-中部，14-中西部，15-西部，16-珠三角，17-长三角，18-环渤海，19-港口中转，20-北方七港，21-外贸，110000-北京，110101-东城区，1..."""

    Industry: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='Industry', column_type='int', nullable=False, chn_name='行业')
    """行业:"""

    MarketCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='MarketCode', column_type='int', nullable=False, chn_name='信息涉及市场')
    """信息涉及市场:信息涉及市场(MarketCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1009，得到信息涉及市场的具体描述：1001-主板，1004-中小企业板，1005-创业板，1007-三板市场，1010-银行间市场，1013-柜台市场。"""

    InvolvedInstitution: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='InvolvedInstitution', column_type='int', nullable=False, chn_name='涉及机构')
    """涉及机构:涉及机构（InvolvedInstitution）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，取公司中文名称(ChiName)得到涉及机构的具体说明。"""

    InfoType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='InfoType', column_type='varchar(50)', nullable=False, chn_name='信息类别')
    """信息类别:"""

    MarketOpinionCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='MarketOpinionCode', column_type='int', nullable=False, chn_name='股市评论意见类型')
    """股市评论意见类型:股市评论意见类型(MarketOpinionCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1053，得到股市评论意见类型的具体描述：501-看空，502-看多，503-看平，504-其它。"""

    MarketOpinionDesc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='MarketOpinionDesc', column_type='varchar(50)', nullable=False, chn_name='股市评论意见类型描述')
    """股市评论意见类型描述:"""

    StockOpinionCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='StockOpinionCode', column_type='int', nullable=False, chn_name='个股推荐意见类型')
    """个股推荐意见类型:个股推荐意见类型(StockOpinionCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1031，得到个股推荐意见类型的具体描述：301-买入，302-卖出，303-持有，304-关注，305-其它。"""

    StockOpinionDesc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='StockOpinionDesc', column_type='varchar(50)', nullable=False, chn_name='个股推荐意见类型描述')
    """个股推荐意见类型描述:"""

    Conclusion: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='Conclusion', column_type='varchar(500)', nullable=False, chn_name='个股推荐/股市评论结论')
    """个股推荐/股市评论结论:"""

    ForecastLowestPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='ForecastLowestPrice', column_type='decimal(19,4)', nullable=False, chn_name='预测价位最低价(元)')
    """预测价位最低价(元):"""

    ForecastHighestPrice: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='ForecastHighestPrice', column_type='decimal(19,4)', nullable=False, chn_name='预测价位最高价(元)')
    """预测价位最高价(元):"""

    ContentType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='ContentType', column_type='int', nullable=False, chn_name='证券知识内容类别')
    """证券知识内容类别:证券知识内容类别(ContentType)与(CT_SystemConst)表中的DM字段关联，令LB = 1179，得到证券知识内容类别的具体描述：1-投资技巧，2-知识问答，3-股市文化，4-炒股经验，5-技术讲座，6-历史回顾，100-其它。"""

    ContentTypeDesc: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='ContentTypeDesc', column_type='varchar(50)', nullable=False, chn_name='证券知识内容类别描述')
    """证券知识内容类别描述:"""

    SpecialCategory: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='SpecialCategory', column_type='int', nullable=False, chn_name='所属专题')
    """所属专题:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='InfoPublDate', column_type='datetime', nullable=False, chn_name='信息发布日期')
    """信息发布日期:"""

    InfoLevel: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='InfoLevel', column_type='int', nullable=False, chn_name='信息级别')
    """信息级别:"""

    PageName: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='PageName', column_type='varchar(50)', nullable=False, chn_name='版面名称')
    """版面名称:"""

    PageNumnber: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='PageNumnber', column_type='varchar(20)', nullable=False, chn_name='版面标识号')
    """版面标识号:"""

    RecordDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='RecordDate', column_type='datetime', nullable=False, chn_name='记录录入时间')
    """记录录入时间:"""

    InsertTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='InsertTime', column_type='datetime', nullable=False, chn_name='发布时间')
    """发布时间:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    MediaCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='MediaCode', column_type='int', nullable=False, chn_name='媒体出处代码')
    """媒体出处代码:媒体出处代码(MediaCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1183，得到媒体出处代码的具体描述：1-中国证券报，2-证券时报，3-上海证券报，4-证券日报，5-大众证券，6-第一财经日报，7-证券市场周刊，8-财经时报，9-东方财富，10-金融时报，11-金融投资报，12-英国《金融时报》，13-财华社，14-和讯，..."""

    Media: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='Media', column_type='varchar(50)', nullable=False, chn_name='媒体出处')
    """媒体出处:"""

    Category: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='Category', column_type='int', nullable=False, chn_name='栏目选择')
    """栏目选择:栏目选择(Category)与(CT_SystemConst)表中的DM字段关联，令LB = 1007，得到栏目选择的具体描述：1-证券市场动态，2-证券市场研究，3-股市评论，4-个股推荐，5-公司研究，6-公司动态，7-新股发行介绍，8-新股上市定位，9-板块分析，10-财经时事，11-宏观分析，12-行业动态，13-行业分析，14-行业政策，15-证券..."""

    InfoTitle: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='InfoTitle', column_type='varchar(255)', nullable=False, chn_name='标题')
    """标题:"""

    Content: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='Content', column_type='text', nullable=False, chn_name='内容')
    """内容:"""

    URL: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_News', column_name='URL', column_type='varchar(300)', nullable=False, chn_name='链接地址')
    """链接地址:"""

