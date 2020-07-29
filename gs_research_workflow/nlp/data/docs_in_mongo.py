# -*- coding: UTF-8 -*-

"""
在 mongo 中的数据结构定义

使用 MongoEngine 方式定义的与 keyword search 有关的 documents
有关 Mongo Engine 的 documents : https://mongoengine-odm.readthedocs.io/guide/defining-documents.html

"""

from mongoengine import Document, StringField, DateTimeField, ListField, EmbeddedDocument, IntField, \
    FloatField, EmbeddedDocumentField, EmbeddedDocumentListField, LazyReferenceField, BooleanField


class Sentiment(EmbeddedDocument):
    sentiment = IntField()
    """ 1:positive , 0:neutral , -1:negative ，需要做一下 str 2 val 转换 """
    positive_score = FloatField()
    neutral_score = FloatField()
    negative_score = FloatField()
    offset = IntField()
    """仅 sentences sentiment 中有效"""
    length = IntField()
    """仅 sentences sentiment 中有效"""


class EntityInDoc(EmbeddedDocument):
    text = StringField()
    type = StringField()
    subtype = StringField()
    offset = IntField()
    length = IntField()
    score = FloatField()


class GlobalEntity(Document):
    """全局的 entity """
    entity_id = StringField(primary_key=True)
    """eg: Vladimir Putin"""
    name = StringField()
    language = StringField()
    url = StringField()
    data_source = StringField()
    """eg: Wikipedia"""

    batch_action_uuid = StringField()

    meta = {
        "indexes": [
            "$name",
            "#batch_action_uuid",
        ]
    }


class GlobalEntityLinking(EmbeddedDocument):
    entity = LazyReferenceField(GlobalEntity)
    text = StringField()
    offset = IntField()
    length = IntField()
    score = FloatField()


class AzureTextAna(EmbeddedDocument):
    """azure 接口对于文本数据分析的结果"""
    detected_language = StringField()
    """ 取 languageDetection.documents.detectedLanguages.iso6391Name ， eg:  'en' """
    detected_language_score = FloatField()
    """ 取 languageDetection.documents.detectedLanguages.score , eg: 1.0 """
    key_phrases = ListField(StringField(), default=None)
    """ 取 keyPhrases.documents.keyPhrases """
    doc_sentiment = EmbeddedDocumentField(Sentiment)
    """ 取 sentiment.documents 下的内容"""
    sentences_sentiment = EmbeddedDocumentListField(Sentiment, default=None)
    """ 取 sentiment.documents.sentences 下的内容"""
    entities = EmbeddedDocumentListField(EntityInDoc, default=None)
    """取 entities.documents.entities """
    entity_linking = EmbeddedDocumentListField(GlobalEntityLinking, default=None)
    """取 entityLinking.documents.entities """
    entity_pii = EmbeddedDocumentListField(EntityInDoc, default=None)


class SymbolInfoBySeekingAlpha(EmbeddedDocument):
    followers = IntField()
    high_52wk = FloatField()
    low_52wk = FloatField()
    eps_fwd = FloatField()
    pe_fwd = FloatField()
    yield_fwd = FloatField()
    div_rate_fwd = FloatField()
    mkt_cap = FloatField()
    volume = FloatField()
    mtime = DateTimeField()


class SymbolDataFromYahoo(EmbeddedDocument):
    zip = StringField()
    sector = StringField()
    fullTimeEmployees = IntField()
    longBusinessSummary = StringField()
    city = StringField()
    phone = StringField()
    country = StringField()
    website = StringField()
    maxAge = IntField()
    address1 = StringField()
    industry = StringField()
    address2 = StringField()
    previousClose = FloatField()
    regularMarketOpen = FloatField()
    twoHundredDayAverage = FloatField()
    trailingAnnualDividendYield = FloatField()
    payoutRatio = FloatField()
    volume24Hr = FloatField()
    regularMarketDayHigh = FloatField()
    navPrice = FloatField()
    averageDailyVolume10Day = IntField()
    totalAssets = FloatField()
    regularMarketPreviousClose = FloatField()
    fiftyDayAverage = FloatField()
    trailingAnnualDividendRate = FloatField()
    open = FloatField()
    toCurrency = StringField()
    averageVolume10days = IntField()
    expireDate = StringField()
    yieldVal = FloatField()
    algorithm = StringField()  # ???
    dividendRate = FloatField()
    exDividendDate = IntField()
    beta = FloatField()
    circulatingSupply = StringField()
    startDate = IntField()
    regularMarketDayLow = FloatField()
    priceHint = IntField()
    currency = StringField()
    regularMarketVolume = IntField()
    lastMarket = StringField()  # ???
    maxSupply = StringField()  # ???
    openInterest = FloatField()
    marketCap = IntField()
    volumeAllCurrencies = FloatField()
    strikePrice = FloatField()
    averageVolume = IntField()
    priceToSalesTrailing12Months = FloatField()
    dayLow = FloatField()
    ask = FloatField()
    ytdReturn = FloatField()
    askSize = IntField()
    volume = IntField()
    fiftyTwoWeekHigh = FloatField()
    forwardPE = FloatField()
    fromCurrency = StringField()  # ???
    fiveYearAvgDividendYield = FloatField()
    fiftyTwoWeekLow = FloatField()
    bid = FloatField()
    tradeable = IntField()
    dividendYield = FloatField()
    bidSize = IntField()
    dayHigh = FloatField()
    exchange = StringField()
    shortName = StringField()
    longName = StringField()
    exchangeTimezoneName = StringField()
    exchangeTimezoneShortName = StringField()
    isEsgPopulated = IntField()
    gmtOffSetMilliseconds = StringField()
    quoteType = StringField()
    messageBoardId = StringField()
    market = StringField()
    annualHoldingsTurnover = FloatField()
    enterpriseToRevenue = FloatField()
    beta3Year = FloatField()
    profitMargins = FloatField()
    enterpriseToEbitda = FloatField()
    WeekChange = FloatField()
    morningStarRiskRating = FloatField()
    forwardEps = FloatField()
    revenueQuarterlyGrowth = FloatField()
    sharesOutstanding = IntField()
    fundInceptionDate = IntField()
    annualReportExpenseRatio = FloatField()
    bookValue = FloatField()
    sharesShort = IntField()
    sharesPercentSharesOut = FloatField()
    fundFamily = StringField()
    lastFiscalYearEnd = IntField()
    heldPercentInstitutions = FloatField()
    netIncomeToCommon = IntField()
    trailingEps = FloatField()
    lastDividendValue = FloatField()
    SandP52WeekChange = FloatField()
    priceToBook = FloatField()
    heldPercentInsiders = FloatField()
    nextFiscalYearEnd = IntField()
    mostRecentQuarter = IntField()
    shortRatio = FloatField()
    sharesShortPreviousMonthDate = IntField()
    floatShares = IntField()
    enterpriseValue = IntField()
    threeYearAverageReturn = FloatField()
    lastSplitDate = IntField()
    lastSplitFactor = StringField()
    legalType = StringField()
    morningStarOverallRating = FloatField()
    earningsQuarterlyGrowth = FloatField()
    dateShortInterest = IntField()
    pegRatio = FloatField()
    lastCapGain = FloatField()
    shortPercentOfFloat = FloatField()
    sharesShortPriorMonth = IntField()
    category = StringField()
    fiveYearAverageReturn = FloatField()
    regularMarketPrice = FloatField()
    logo_url = StringField()
    trailingPE = FloatField()
    fiftyTwoWeekChange = FloatField()
    state = StringField()
    fax = StringField()
    mtime = DateTimeField()


class FinancialInstrumentSymbol(Document):
    """
    美国市场的金融产品工具，
    """
    symbol = StringField(primary_key=True)
    """ 这里 symbol 暂时全部使用大写，并且暂时只有美国市场的symbol """
    full_name = StringField()
    """" 全称，一般为该股票上市地点语言的版本 """
    chn_name = StringField()
    """ 中文名，数据一般来自于 sina 等站点，有部分情况下，该字段也可能填入的是 英文，多半是没有做过相关的翻译 """
    eng_name = StringField()
    """ 英文名， """

    info_from_seeking_alpha = EmbeddedDocumentField(SymbolInfoBySeekingAlpha)
    info_from_yahoo = EmbeddedDocumentField(SymbolDataFromYahoo)
    important = BooleanField()
    """暂时的简化处理，ZT关注的股票，都设置 important 的标记"""

    batch_action_uuid = StringField()

    meta = {
        "indexes": [
            "$full_name",  # text index
            "#batch_action_uuid",
            "#chn_name",
            "#eng_name"
        ]
    }


class FinancialInstrumentDailyMarketData(Document):
    uid = StringField(primary_key=True)
    """symbol + date 计算得到的 uid"""
    symbol = LazyReferenceField(FinancialInstrumentSymbol, default=None)
    t = DateTimeField()
    open = FloatField()
    high = FloatField()
    low = FloatField()
    close = FloatField()
    volume = FloatField()
    dividends = FloatField()
    splits = FloatField()
    fifty_two_week_high = FloatField()
    fifty_two_week_low = FloatField()
    meta = {
        "indexes": [
            "#symbol",
            "-t"
        ]
    }


class FinancialInstrumentRecommendInYahoo(Document):
    uid = StringField(primary_key=True)
    """t+symbol+firm 获得"""
    symbol = LazyReferenceField(FinancialInstrumentSymbol, default=None)
    firm = LazyReferenceField(GlobalEntity, default=None)
    t = DateTimeField()
    to_grade = StringField()
    from_grade = StringField()
    action = StringField()
    meta = {
        "indexes": [
            "#symbol",
            "#firm",
            "#to_grade",
            "#from_grade",
            "#action",
            "-t"
        ]
    }


class FinancialInstrumentCalendarFromYahoo(Document):
    """
    see https://finance.yahoo.com/quote/MSFT/analysis?p=MSFT
    其中的一部分数据
    """
    uid = StringField(primary_key=True)
    """t+symbol+firm 获得"""
    symbol = LazyReferenceField(FinancialInstrumentSymbol, default=None)
    t = DateTimeField()
    """Earnings Date"""
    earnings_average = FloatField()
    earnings_low = FloatField()
    earnings_high = FloatField()
    revenue_average = FloatField()
    revenue_low = FloatField()
    revenue_high = FloatField()


class FinancialInstrumentDividends(Document):
    uid = StringField(primary_key=True)
    """symbol + date 计算得到的 uid"""
    symbol = LazyReferenceField(FinancialInstrumentSymbol, default=None)
    t = DateTimeField()
    divident = FloatField()
    split = FloatField()
    meta = {
        "indexes": [
            "#symbol",
            "-t"
        ]
    }


class FinancialInstrumentHolders(Document):
    uid = StringField(primary_key=True)
    """holder + symbol + date 计算得到的 uid """
    symbol = LazyReferenceField(FinancialInstrumentSymbol, default=None)
    t = DateTimeField()
    """date reported"""
    holder = LazyReferenceField(GlobalEntity, default=None)
    shares = FloatField()
    value = FloatField()
    percentage_out = FloatField()
    meta = {
        "indexes": [
            "#symbol",
            "#holder",
            "-t"
        ]
    }


class AuthorInSeekingAlpha(Document):
    """seeking alpha中的一个author的信息 """

    author_id = StringField(primary_key=True)
    """author uuid in seeking alpha"""

    url = StringField()

    author_name = StringField()

    intro = StringField()
    """ author_intro  """

    intro_ana = EmbeddedDocumentField(AzureTextAna)

    articles = IntField()
    """总共发布的文章数 , articles """
    picks = IntField()
    """被seeking alpha编辑选中的文章数 , authors_picks """
    blog_posts = IntField()
    """ 发布的blog个数， instablogs  """
    comments = IntField()
    """ 收到的 comments 数， comments  """
    stock_talks = IntField()
    """ stocktalks """
    likes = IntField()
    """ likes """
    followers = IntField()
    """ followers """

    following = IntField()
    mtime = DateTimeField()
    """ extract_t """
    batch_action_uuid = StringField()


    meta = {
        "indexes": [
            "$intro",  # text index
            "#batch_action_uuid",
            "-followers",  # follower 降序
            "-articles"
        ]
    }


class UserInTwitter(Document):
    user_id = StringField(primary_key=True)
    name = StringField()
    intro = StringField()
    intro_ana = EmbeddedDocumentField(AzureTextAna)
    follower = IntField()
    following = IntField()
    arr_following = ListField(LazyReferenceField('self'), default=None)
    batch_action_uuid = StringField()

    mtime = DateTimeField()
    meta = {
        "indexes": [
            "$intro",
            "#batch_action_uuid",
            "-follower",
            "-following"
        ]
    }


class SeekingAlphaArticleExtra(EmbeddedDocument):
    comments = IntField()
    """评论数"""

    meta = {
        "indexes": [
            "-comments",  # comment 降序
        ]
    }


class TweetExtra(EmbeddedDocument):
    comments = IntField()
    retweet = IntField()
    like = IntField()

    meta = {
        "indexes": [
            "-comments",
            "-retweet",
            "-like",
        ]
    }


class SearchingPhrase(Document):
    """ 适用于 普通的 keyword search 组合，也适用于特定网站中 Advance Search 的 特定语法 """

    searching_phrase = StringField(primary_key=True)
    batch_action_uuid = StringField()

    related_symbols = ListField(LazyReferenceField('FinancialInstrumentSymbol'), default=None)

    """适用于有几个 kw 来自于 symbol """

    # --- twitter advance search 的一些条件
    # 这些字段暂时都可以不需要
    # kws_from_symbol = ListField(LazyReferenceField('FinancialInstrumentSymbol'), default=None)
    # twitter_user = ListField(LazyReferenceField(UserInTwitter), default=None)  # 来自于 twitter 的一个或者多个用户
    # min_retweet = IntField()
    # min_tweet_like = IntField()
    # min_tweet_reply = IntField()


    meta = {
        "indexes": [
            "$searching_phrase",  # text index
            "#batch_action_uuid",
            # "-min_retweet",
            # "-min_tweet_like",
            # "-min_tweet_reply",
        ]
    }


class Article(Document):
    """ 一篇文章内容，可以是 seeking alpha 中的一篇专栏文章，也可以是 twitter 上的一篇 post，
    也可以是 google news search 的一篇结果等 """

    uuid = StringField(max_length=32, primary_key=True)
    """各采编的数据处理函数自行决定该 hash 算法，只要全局不冲撞即可"""

    title = StringField(required=True)
    """文章的标题，或者是 post 的贴文等"""

    title_ana = EmbeddedDocumentField(AzureTextAna)

    abstract = StringField()
    """新闻的摘要，或 搜索，或者 twitter 的短文内容 """

    abstract_ana = EmbeddedDocumentField(AzureTextAna)

    full_text_url = StringField()
    """全文的访问地址"""
    
    related_image_url = StringField()
    """如果是 twitter ， 可能会有关联的图片 """

    rating = IntField()
    """一些站点，如 seeking alpha 是有 rating 数的，这里记录该 rating 值"""

    rating_change = IntField()
    """评级变动"""

    pred_ret_this_yr = FloatField()
    """当年度return预测"""

    pred_pe_this_yr = FloatField()
    """当年度pe预测"""

    pred_ret_next_yr = FloatField()
    """下一年度return预测"""

    pred_pe_next_yr = FloatField()
    """下一年度pe预测"""

    publish_time = DateTimeField()

    related_symbols = ListField(LazyReferenceField(FinancialInstrumentSymbol), default=None)

    engine_site = StringField()
    """ 数据来自于， SeekingAlpha / GoogleNews / Twitter """

    channel_in_site = StringField()
    """ 文章属于站点中的哪个栏目下的 ， 包括可以使用 Search """

    batch_action_uuid = StringField()
    action_uuid = StringField()

    from_searching_phase = LazyReferenceField(SearchingPhrase)
    """如果文章来源于一个搜索结果，则这里提供其中的一个搜索词"""

    seeking_alpha_author = LazyReferenceField(AuthorInSeekingAlpha)
    """ 文章如果来自于 seeking alpha ， 则这里是 seeking alpha 的作者信息 """

    seeking_alpha_extra = EmbeddedDocumentField(SeekingAlphaArticleExtra)
    """ 文章如果来自于 seeking alpha ， 是一些 comments 等信息 """

    twitter_poster = LazyReferenceField(UserInTwitter)
    """article如果来自于 twitter , 则 填入"""

    tweet_extra = EmbeddedDocumentField(TweetExtra)
    """tweet 的 comment / like / follow 等数据"""

    meta = {
        "indexes": [
            "$title",  # text index
            "#batch_action_uuid",
            "#action_uuid",
            "-publish_time",  # follower 降序
            "-rating",  # follower 降序
            "#engine_site",  # hash index site 可以快速的选择不同的源
            "#channel_in_site",  # 用于快速过滤来源
        ]
    }
