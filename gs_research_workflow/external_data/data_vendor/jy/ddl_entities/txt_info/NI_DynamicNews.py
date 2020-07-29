# -*- coding: utf-8 -*-
# Auto Generated Code .  DO NOT EDIT!

from gs_research_workflow.external_data.table_declaration_base import SQLTableEntity, TableColumnDeclarationEntity


class NI_DynamicNews(SQLTableEntity):
    name: str = 'NI_DynamicNews'
    
    chn_name: str = '新闻动态表'
    
    business_unique: str = '需媒体版权'
    
    refresh_freq: str = """滚动更新"""
    
    comment: str = """1.收录市场及公司重大新闻资讯，主要特色为新闻都配有图片，可用于APP或网站展示，每日数据更新量50条左右。
2.数据范围：2012-至今"""

    ID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_DynamicNews', column_name='ID', column_type='bigint', nullable=True, chn_name='ID')
    """ID:"""

    Flag: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_DynamicNews', column_name='Flag', column_type='int', nullable=False, chn_name='资讯级别')
    """资讯级别:资讯级别（Flag）：10最高，1最低"""

    PictureContent: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_DynamicNews', column_name='PictureContent', column_type='blob', nullable=False, chn_name='图片内容')
    """图片内容:"""

    PictureType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_DynamicNews', column_name='PictureType', column_type='int', nullable=False, chn_name='图片格式')
    """图片格式:图片格式(PictureType)与(CT_SystemConst)表中的DM字段关联，令LB = 1388，得到图片格式的具体描述：1-JPG，2-BMP，3-GIF，4-SWF，5-JPEG，6-PNG。"""

    PictureURL: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_DynamicNews', column_name='PictureURL', column_type='varchar(200)', nullable=False, chn_name='图片链接')
    """图片链接:"""

    CompanyTag: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_DynamicNews', column_name='CompanyTag', column_type='int', nullable=False, chn_name='公司标签')
    """公司标签:"""

    IndustryTag: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_DynamicNews', column_name='IndustryTag', column_type='int', nullable=False, chn_name='所属行业标签')
    """所属行业标签:"""

    UpdateTime: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_DynamicNews', column_name='UpdateTime', column_type='datetime', nullable=True, chn_name='更新时间')
    """更新时间:"""

    JSID: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_DynamicNews', column_name='JSID', column_type='bigint', nullable=True, chn_name='JSID')
    """JSID:"""

    InfoPublDate: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_DynamicNews', column_name='InfoPublDate', column_type='datetime', nullable=True, chn_name='信息发布时间')
    """信息发布时间:"""

    InfoTitle: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_DynamicNews', column_name='InfoTitle', column_type='varchar(250)', nullable=True, chn_name='新闻标题')
    """新闻标题:"""

    Category: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_DynamicNews', column_name='Category', column_type='int', nullable=False, chn_name='新闻分类')
    """新闻分类:新闻分类(Category)与(CT_SystemConst)表中的DM字段关联，令LB = 1007，得到新闻分类的具体描述：1-证券市场动态，2-证券市场研究，3-股市评论，4-个股推荐，5-公司研究，6-公司动态，7-新股发行介绍，8-新股上市定位，9-板块分析，10-财经时事，11-宏观分析，12-行业动态，13-行业分析，14-行业政策，15-证券..."""

    NewsType: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_DynamicNews', column_name='NewsType', column_type='int', nullable=True, chn_name='资讯类型')
    """资讯类型:资讯类型(NewsType)与(CT_SystemConst)表中的DM字段关联，令LB = 1831，得到资讯类型的具体描述：1-网站URL链接，2-手机类url链接，3-文本类资讯，4-图文类资讯。"""

    MediaCode: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_DynamicNews', column_name='MediaCode', column_type='int', nullable=False, chn_name='媒体代码')
    """媒体代码:媒体代码(MediaCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1183，得到媒体代码的具体描述：1-中国证券报，2-证券时报，3-上海证券报，4-证券日报，5-大众证券，6-第一财经日报，7-证券市场周刊，8-财经时报，9-东方财富，10-金融时报，11-金融投资报，12-英国《金融时报》，13-财华社，14-和讯，15-网..."""

    Media: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_DynamicNews', column_name='Media', column_type='varchar(40)', nullable=False, chn_name='媒体名称')
    """媒体名称:"""

    InfoURL: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_DynamicNews', column_name='InfoURL', column_type='varchar(400)', nullable=False, chn_name='新闻链接')
    """新闻链接:"""

    Content: TableColumnDeclarationEntity = TableColumnDeclarationEntity(tbl_name='NI_DynamicNews', column_name='Content', column_type='text', nullable=False, chn_name='新闻内容')
    """新闻内容:"""

