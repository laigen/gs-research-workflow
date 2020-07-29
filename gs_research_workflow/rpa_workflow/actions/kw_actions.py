# -*- coding: UTF-8 -*-

"""
提供一些 相对 High Level 的 Actions

High Level Action : 面向各类 Entity 的 Action ， 最终会被映射到各 Low Level 的 Action
                    如： twitter Search 的 Action 将被上一层封装为：
                                                search tweet from somebody(ies)
                                                search tweet with word / without word
                                                search tweet with min_retweet
    High Level Action 会提供一些基本的封装，包括：
        1) 接口业务意义的封装。 比如： 将 keyword combination 封装成  symbol + entity ,
                                                    symbol.full_name + entities (with query condition)
                                                    symbols( return from query condition) + twitter.user( return from query condition )
                            等多种形式的接口，这些接口最终调用的底层接口是同一个，都是 twitter search

        2) actions split 。 比如： 一个 kw search 的 batch 达到了 1k 个， 可能会拆分成 100（次） * 10 (Per Action) .
                            一个是为了并行，另一个是容错（如果出现局部错误，也能得到大部分的结果）

        3) sequential action ((rule based) mini workflow) 。比如：
                                                > google search 得到结果以后，将 abstract 的内容拿到 azure 上进行 txt analyse
                                                > twitter 的 search result 中，将新发现的 tweet poster 且
                                                            following - follower > 10K 的取一次他的 following

        4) 将 Action 接口，增加偏业务场景的 Input Parameter Typing， 比如：  Symbol ,  QueryCondition 等

"""
import itertools
from datetime import datetime
from typing import List, Tuple, Set

from gs_framework.utilities import generate_uuid

from gs_research_workflow.rpa_workflow.result_extraction.seeking_alpha import SeekingAlphaDataProcess

from gs_research_workflow.nlp.data.docs_in_mongo import UserInTwitter, FinancialInstrumentSymbol, \
    SearchingPhrase, Article, AuthorInSeekingAlpha
from gs_research_workflow.rpa_workflow.act_msg_data import RPAAction

from gs_research_workflow.common.mongo_resource import db_nlp, mongo_db_conn, used_db_position

from gs_research_workflow.common.serialization_utilities import cls_to_str

from gs_research_workflow.rpa_workflow.actions.action_doc_in_mongo import RPABatchAction, RPAActionDoc, ActionStatusFlag
from gs_research_workflow.rpa_workflow.result_extraction.azure import AzureDataProcess
from gs_research_workflow.rpa_workflow.result_extraction.google_news import GoogleNewsSearchProcess
from gs_research_workflow.rpa_workflow.result_extraction.twitter import TwitterDataProcess
from gs_research_workflow.rpa_workflow.result_extraction.utilities import upsert_document
from gs_research_workflow.rpa_workflow.uipath_actions_low_level import google_news_kws_search, twitter_kws_search, \
    twitter_users_following, AzureTxtAnaPara, azure_txt_analysis, seeking_alpha_symbols_info, seeking_alpha_authors_info
import pickle
import logging

logger = logging.getLogger(__name__)

MINI_BATCH_SIZE: int = 5

# region us stk

CHINA_ARD: Set[str] = {
    "YI", "VNET", "QFIN", "KRKR", "WBAI", "JOBS", "WUBA", "ATV", "AMCN", "BABA",
    "ACH", "AMBOY", "ATAI", "JG", "ATHM", "BIDU", "BZUN", "BGNE", "BSTI", "BILI",
    "BEDU", "CAN", "CANG", "CYOU", "CMCM", "STV", "DL", "CEA", "JRJC", "LFC",
    "HTHT", "CHL", "CEO", "COE", "SNP", "XRF", "ZNH", "CHA", "CHU", "XNY",
    "CCIH", "CNF", "CCM", "CTK", "DQ", "DOYU", "EH", "EHIC", "SFUN", "DUO",
    "FANH", "FEDU", "FUTU", "GDS", "GHG", "GSUM", "GSX", "GSH", "HLG", "HX",
    "HMI", "HNP", "HTHT", "HCM", "HUYA", "KANG", "IQ", "JD", "JT", "JFIN",
    "JKS", "JMU", "JMEI", "JP", "KZ", "LAIX", "LEJU", "LX", "LITB", "LKM",
    "LK", "MOGU", "MOMO", "NTES", "EDU", "NIO", "NIU", "NOAH", "NQ", "ONE",
    "OSN", "PTR", "FENG", "PDD", "PT", "PPDF", "PUYI", "QK", "QD", "QTT",
    "SOL", "RENN", "REDU", "RUHN", "RYB", "SECO", "SHI", "SKYS", "SY", "SOGO",
    "SOHU", "STG", "TAL", "TEDU", "TME", "NCTY", "TCOM", "TC", "TOUR", "TIGR",
    "UXIN", "VIOT", "VIPS", "WSG", "WB", "XYF", "XIN", "XNET", "YGE", "YIN",
    "YRD", "DAO", "YJ", "YY", "ZLAB", "ZPIN", "ZTO",
}

NASDAQ_100: Set[str] = {
    "ATVI", "ADBE", "AMD", "ALXN", "ALGN", "GOOG", "GOOGL", "AMZN", "AMGN", "ADI",
    "ANSS", "AAPL", "AMAT", "ASML", "ADSK", "ADP", "BIDU", "BIIB", "BMRN", "BKNG",
    "AVGO", "CDNS", "CDW", "CERN", "CHTR", "CHKP", "CTAS", "CSCO", "CTXS", "CTSH",
    "CMCSA", "CPRT", "CSGP", "COST", "CSX", "DXCM", "DLTR", "EBAY", "EA", "EXC",
    "EXPE", "FB", "FAST", "FISV", "FOX", "FOXA", "GILD", "IDXX", "ILMN", "INCY",
    "INTC", "INTU", "ISRG", "JD", "KLAC", "LRCX", "LBTYA", "LBTYK", "LULU", "MAR",
    "MXIM", "MELI", "MCHP", "MU", "MSFT", "MDLZ", "MNST", "NTAP", "NTES", "NFLX",
    "NVDA", "NXPI", "ORLY", "PCAR", "PAYX", "PYPL", "PEP", "QCOM", "REGN", "ROST",
    "SGEN", "SIRI", "SWKS", "SPLK", "SBUX", "SNPS", "TMUS", "TTWO", "TSLA", "TXN",
    "KHC", "TCOM", "ULTA", "UAL", "VRSN", "VRSK", "VRTX", "WBA", "WDC", "WDAY",
    "XEL", "XLNX", "ZM"
}

DOW_30: Set[str] = {
    "AXP", "AAPL", "BA", "CAT", "CSCO", "CVX", "XOM", "GS", "HD", "IBM",
    "INTC", "JNJ", "KO", "JPM", "MCD", "MMM", "MRK", "MSFT", "NKE", "PFE",
    "PG", "TRV", "UNH", "RTX", "VZ", "V", "WBA", "WMT", "DIS", "DOW",
}

IMPORTANT_SYMBOLS: Set[str] = {
    "BYND", "GILD", "GSX", "PDD", "FB", "SPX", "TSLA", "USO", "IWM", "IQ",
    "MAR", "DRI", "CMG", "AMZN", "BABA", "GOOG", "AAPL"
}

ALL_US_SYMBOLS: List[str] = sorted(list(CHINA_ARD.union(NASDAQ_100).union(DOW_30).union(IMPORTANT_SYMBOLS)))

# endregion

# region hk stk

H_SHARES_WITH_NAME: List[Tuple[str, str]] = [("00038.HK", "第一拖拉机股份"), ("00042.HK", "东北电气"), ("00107.HK", "四川成渝高速公路"),
                                             ("00151.HK", "中国旺旺"), ("00168.HK", "青岛啤酒股份"), ("00175.HK", "吉利汽车"),
                                             ("00177.HK", "江苏宁沪高速公路"), ("00187.HK", "京城机电股份"), ("00267.HK", "中信股份"),
                                             ("00270.HK", "粤海投资"), ("00291.HK", "华润啤酒"), ("00317.HK", "中船防务"),
                                             ("00323.HK", "马鞍山钢铁股份"), ("00338.HK", "上海石油化工股份"), ("00347.HK", "鞍钢股份"),
                                             ("00357.HK", "美兰空港"), ("00358.HK", "江西铜业股份"), ("00384.HK", "中国燃气"),
                                             ("00386.HK", "中国石油化工股份"), ("00390.HK", "中国中铁"), ("00416.HK", "锦州银行"),
                                             ("00438.HK", "彩虹新能源"), ("00489.HK", "东风集团股份"), ("00525.HK", "广深铁路股份"),
                                             ("00548.HK", "深圳高速公路股份"), ("00552.HK", "中国通信服务"), ("00553.HK", "南京熊猫电子股份"),
                                             ("00564.HK", "郑煤机"), ("00568.HK", "山东墨龙"), ("00576.HK", "浙江沪杭甬"),
                                             ("00579.HK", "京能清洁能源"), ("00586.HK", "海螺创业"), ("00588.HK", "北京北辰实业股份"),
                                             ("00598.HK", "中国外运"), ("00656.HK", "复星国际"), ("00670.HK", "中国东方航空股份"),
                                             ("00694.HK", "北京首都机场股份"), ("00696.HK", "中国民航信息网络"), ("00700.HK", "腾讯控股"),
                                             ("00719.HK", "山东新华制药股份"), ("00728.HK", "中国电信"), ("00747.HK", "沈阳公用发展股份"),
                                             ("00753.HK", "中国国航"), ("00762.HK", "中国联通"), ("00763.HK", "中兴通讯"),
                                             ("00788.HK", "中国铁塔"), ("00811.HK", "新华文轩"), ("00813.HK", "世茂房地产"),
                                             ("00814.HK", "北京京客隆"), ("00816.HK", "华电福新"), ("00840.HK", "天业节水"),
                                             ("00857.HK", "中国石油股份"), ("00874.HK", "白云山"), ("00883.HK", "中国海洋石油"),
                                             ("00895.HK", "东江环保"), ("00902.HK", "华能国际电力股份"), ("00914.HK", "海螺水泥"),
                                             ("00916.HK", "龙源电力"), ("00921.HK", "海信家电"), ("00939.HK", "建设银行"),
                                             ("00941.HK", "中国移动"), ("00954.HK", "常茂生​​物"), ("00956.HK", "新天绿色能源"),
                                             ("00960.HK", "龙湖集团"), ("00966.HK", "中国太平"), ("00980.HK", "联华超市"),
                                             ("00991.HK", "大唐发电"), ("00995.HK", "安徽皖通高速公路"), ("00998.HK", "中信银行"),
                                             ("01000.HK", "北青传媒"), ("01033.HK", "中石化油服"), ("01044.HK", "恒安国际"),
                                             ("01053.HK", "重庆钢铁股份"), ("01055.HK", "中国南方航空股份"), ("01057.HK", "浙江世宝"),
                                             ("01065.HK", "天津创业环保股份"), ("01066.HK", "威高股份"), ("01071.HK", "华电国际电力股份"),
                                             ("01072.HK", "东方电气"), ("01075.HK", "首都信息"), ("01088.HK", "中国神华"),
                                             ("01093.HK", "石药集团"), ("01099.HK", "国药控股"), ("01103.HK", "大生农业金融"),
                                             ("01108.HK", "洛阳玻璃股份"), ("01109.HK", "华润置地"), ("01122.HK", "庆铃汽车股份"),
                                             ("01133.HK", "哈尔滨电气"), ("01138.HK", "中远海能"), ("01157.HK", "中联重科"),
                                             ("01158.HK", "开元酒店"), ("01171.HK", "兖州煤业股份"), ("01177.HK", "中国生物制药"),
                                             ("01186.HK", "中国铁建"), ("01193.HK", "华润燃气"), ("01202.HK", "成都普天电缆股份"),
                                             ("01211.HK", "比亚迪股份"), ("01216.HK", "中原银行"), ("01265.HK", "天津津燃公用"),
                                             ("01272.HK", "大唐环境"), ("01288.HK", "农业银行"), ("01289.HK", "盛力达科技"),
                                             ("01292.HK", "长安民生物流"), ("01296.HK", "国电科环"), ("01330.HK", "绿色动力环保"),
                                             ("01336.HK", "新华保险"), ("01339.HK", "中国人民保险集团"), ("01349.HK", "复旦张江"),
                                             ("01353.HK", "诺奇"), ("01359.HK", "中国信达"), ("01375.HK", "中州证券"),
                                             ("01385.HK", "上海复旦"), ("01398.HK", "工商银行"), ("01456.HK", "国联证券"),
                                             ("01459.HK", "巨匠建设"), ("01461.HK", "鲁证期货"), ("01476.HK", "恒投证券"),
                                             ("01501.HK", "康德莱医械"), ("01508.HK", "中国再保险"), ("01513.HK", "丽珠医药"),
                                             ("01527.HK", "天洁环境"), ("01528.HK", "红星美凯龙"), ("01533.HK", "庄园牧场"),
                                             ("01542.HK", "台州水务"), ("01543.HK", "中盈盛达融资担保"), ("01551.HK", "广州农商银行"),
                                             ("01558.HK", "东阳光药"), ("01576.HK", "齐鲁高速"), ("01577.HK", "汇鑫小贷"),
                                             ("01578.HK", "天津银行"), ("01588.HK", "畅捷通"), ("01596.HK", "翼辰实业"),
                                             ("01599.HK", "城建设计"), ("01601.HK", "中关村科技租赁"), ("01606.HK", "国银租赁"),
                                             ("01618.HK", "中国中冶"), ("01635.HK", "大众公用"), ("01649.HK", "内蒙古能建"),
                                             ("01658.HK", "邮储银行"), ("01666.HK", "同仁堂科技"), ("01671.HK", "天保能源"),
                                             ("01697.HK", "山东国信"), ("01708.HK", "三宝科技"), ("01713.HK", "四川能投发展"),
                                             ("01727.HK", "河北建设"), ("01743.HK", "苍南仪表"), ("01749.HK", "杉杉品牌"),
                                             ("01763.HK", "中国同辐"), ("01766.HK", "中国中车"), ("01772.HK", "赣锋锂业"),
                                             ("01776.HK", "广发证券"), ("01785.HK", "成都高速"), ("01786.HK", "铁建装备"),
                                             ("01787.HK", "山东黄金"), ("01798.HK", "大唐新能源"), ("01799.HK", "新特能源"),
                                             ("01800.HK", "中国交通建设"), ("01812.HK", "晨鸣纸业"), ("01816.HK", "中广核电力"),
                                             ("01818.HK", "招金矿业"), ("01829.HK", "中国机械工程"), ("01835.HK", "瑞威资管"),
                                             ("01839.HK", "中集车辆"), ("01847.HK", "云南建投混凝土"), ("01853.HK", "春城热力"),
                                             ("01858.HK", "春立医疗"), ("01877.HK", "君实生物－Ｂ"), ("01898.HK", "中煤能源"),
                                             ("01905.HK", "海通恒信"), ("01915.HK", "泰和小贷"), ("01916.HK", "江西银行"),
                                             ("01918.HK", "融创中国"), ("01919.HK", "中远海控"), ("01958.HK", "北京汽车"),
                                             ("01963.HK", "重庆银行"), ("01983.HK", "泸州银行"), ("01988.HK", "民生银行"),
                                             ("02006.HK", "锦江资本"), ("02007.HK", "碧桂园"), ("02009.HK", "金隅集团"),
                                             ("02016.HK", "浙商银行"), ("02020.HK", "安踏体育"), ("02039.HK", "中集集团"),
                                             ("02066.HK", "盛京银行"), ("02068.HK", "中铝国际"), ("02120.HK", "康宁医院"),
                                             ("02139.HK", "甘肃银行"), ("02163.HK", "远大住工"), ("02196.HK", "复星医药"),
                                             ("02202.HK", "万科企业"), ("02208.HK", "金风科技"), ("02218.HK", "安德利果汁"),
                                             ("02238.HK", "广汽集团"), ("02281.HK", "兴泸水务"), ("02289.HK", "创美药业"),
                                             ("02308.HK", "研祥智能"), ("02313.HK", "申洲国际"), ("02318.HK", "中国平安"),
                                             ("02319.HK", "蒙牛乳业"), ("02328.HK", "中国财险"), ("02333.HK", "长城汽车"),
                                             ("02338.HK", "潍柴动力"), ("02345.HK", "上海集优"), ("02355.HK", "宝业集团"),
                                             ("02357.HK", "中航科工"), ("02359.HK", "药明康德"), ("02382.HK", "舜宇光学科技"),
                                             ("02386.HK", "中石化炼化工程"), ("02488.HK", "元征科技"), ("02500.HK", "启明医疗－Ｂ"),
                                             ("02558.HK", "晋商银行"), ("02600.HK", "中国铝业"), ("02601.HK", "中国太保"),
                                             ("02606.HK", "蓝光嘉宝服务"), ("02607.HK", "上海医药"), ("02611.HK", "国泰君安"),
                                             ("02628.HK", "中国人寿"), ("02688.HK", "新奥能源"), ("02696.HK", "复宏汉霖－Ｂ"),
                                             ("02698.HK", "魏桥纺织"), ("02718.HK", "东正金融"), ("02722.HK", "重庆机电"),
                                             ("02727.HK", "上海电气"), ("02777.HK", "富力地产"), ("02799.HK", "中国华融"),
                                             ("02866.HK", "中远海发"), ("02868.HK", "首创置业"), ("02880.HK", "大连港"),
                                             ("02883.HK", "中海油田服务"), ("02899.HK", "紫金矿业"), ("03319.HK", "雅生活服务"),
                                             ("03323.HK", "中国建材"), ("03328.HK", "交通银行"), ("03330.HK", "灵宝黄金"),
                                             ("03332.HK", "中生联合"), ("03369.HK", "秦港股份"), ("03378.HK", "厦门港务"),
                                             ("03396.HK", "联想控股"), ("03399.HK", "粤运交通"), ("03606.HK", "福耀玻璃"),
                                             ("03618.HK", "重庆农村商业银行"), ("03636.HK", "保利文化"), ("03678.HK", "弘业期货"),
                                             ("03689.HK", "康华医疗"), ("03698.HK", "徽商银行"), ("03759.HK", "康龙化成"),
                                             ("03768.HK", "滇池水务"), ("03833.HK", "新疆新鑫矿业"), ("03866.HK", "青岛银行"),
                                             ("03898.HK", "中车时代电气"), ("03903.HK", "瀚华金控"), ("03908.HK", "中金公司"),
                                             ("03948.HK", "伊泰煤炭"), ("03958.HK", "东方证券"), ("03968.HK", "招商银行"),
                                             ("03969.HK", "中国通号"), ("03983.HK", "中海石油化学"), ("03988.HK", "中国银行"),
                                             ("03993.HK", "洛阳钼业"), ("03996.HK", "中国能源建设"), ("04610.HK", "CZB 17US"),
                                             ("04616.HK", "BCQ 17US"), ("06030.HK", "中信证券"), ("06049.HK", "保利物业"),
                                             ("06060.HK", "众安在线"), ("06066.HK", "中信建投证券"), ("06099.HK", "招商证券"),
                                             ("06116.HK", "拉夏贝尔"), ("06117.HK", "日照港裕廊"), ("06122.HK", "九台农商银行"),
                                             ("06138.HK", "哈尔滨银行"), ("06178.HK", "光大证券"), ("06185.HK", "康希诺生物－Ｂ"),
                                             ("06188.HK", "迪信通"), ("06189.HK", "爱得威建设集团"), ("06190.HK", "九江银行"),
                                             ("06196.HK", "郑州银行"), ("06198.HK", "青岛港"), ("06199.HK", "贵州银行"),
                                             ("06806.HK", "申万宏源"), ("06818.HK", "中国光大银行"), ("06826.HK", "昊海生物科技"),
                                             ("06837.HK", "海通证券"), ("06839.HK", "云南水务"), ("06865.HK", "福莱特玻璃"),
                                             ("06866.HK", "佐力小贷"), ("06869.HK", "长飞光纤光缆"), ("06881.HK", "中国银河"),
                                             ("06885.HK", "金马能源"), ("06886.HK", "HTSC"), ("08045.HK", "南大苏富特"),
                                             ("08049.HK", "吉林长龙药业"), ("08095.HK", "北大青鸟环宇"), ("08106.HK", "升华兰德"),
                                             ("08115.HK", "上海青浦消防"), ("08139.HK", "长安仁恒"), ("08189.HK", "泰达生物"),
                                             ("08205.HK", "交大慧谷"), ("08211.HK", "浙江永安"), ("08227.HK", "海天天线"),
                                             ("08235.HK", "赛迪顾问"), ("08236.HK", "宝德科技集团"), ("08247.HK", "中生北控生物科技"),
                                             ("08249.HK", "瑞远智控"), ("08258.HK", "西北实业"), ("08286.HK", "长城微光"),
                                             ("08301.HK", "明华科技"), ("08329.HK", "海王英特龙"), ("08348.HK", "滨海泰达物流"),
                                             ("08452.HK", "富银融资股份")]

BLUE_CHIP_SHARE_WITH_NAME: List[Tuple[str, str]] = [("00001.HK", "长和"), ("00002.HK", "中电控股"), ("00003.HK", "香港中华煤气"),
                                                    ("00005.HK", "汇丰控股"), ("00006.HK", "电能实业"), ("00011.HK", "恒生银行"),
                                                    ("00012.HK", "恒基地产"), ("00016.HK", "新鸿基地产"), ("00017.HK", "新世界发展"),
                                                    ("00019.HK", "太古股份公司Ａ"), ("00027.HK", "银河娱乐"), ("00066.HK", "港铁公司"),
                                                    ("00083.HK", "信和置业"), ("00101.HK", "恒隆地产"), ("00151.HK", "中国旺旺"),
                                                    ("00175.HK", "吉利汽车"), ("00267.HK", "中信股份"), ("00288.HK", "万洲国际"),
                                                    ("00386.HK", "中国石油化工股份"), ("00388.HK", "香港交易所"),
                                                    ("00669.HK", "创科实业"), ("00688.HK", "中国海外发展"), ("00700.HK", "腾讯控股"),
                                                    ("00762.HK", "中国联通"), ("00823.HK", "领展房产基金"),
                                                    ("00857.HK", "中国石油股份"), ("00883.HK", "中国海洋石油"),
                                                    ("00939.HK", "建设银行"), ("00941.HK", "中国移动"), ("01038.HK", "长江基建集团"),
                                                    ("01044.HK", "恒安国际"), ("01088.HK", "中国神华"), ("01093.HK", "石药集团"),
                                                    ("01109.HK", "华润置地"), ("01113.HK", "长实集团"), ("01177.HK", "中国生物制药"),
                                                    ("01299.HK", "友邦保险"), ("01398.HK", "工商银行"),
                                                    ("01928.HK", "金沙中国有限公司"), ("01997.HK", "九龙仓置业"),
                                                    ("02007.HK", "碧桂园"), ("02018.HK", "瑞声科技"), ("02313.HK", "申洲国际"),
                                                    ("02318.HK", "中国平安"), ("02319.HK", "蒙牛乳业"), ("02382.HK", "舜宇光学科技"),
                                                    ("02388.HK", "中银香港"), ("02628.HK", "中国人寿"), ("03328.HK", "交通银行"),
                                                    ("03988.HK", "中国银行")]

ALL_HK_SYMBOLS: List[str] = sorted(list(set([x[0] for x in H_SHARES_WITH_NAME + BLUE_CHIP_SHARE_WITH_NAME])))

ALL_HK_SYMBOLS_WITH_NAME: List[Tuple[str, str]] = H_SHARES_WITH_NAME + BLUE_CHIP_SHARE_WITH_NAME

# endregion

# region chn stk
HS_300_WITH_NAME: List[Tuple[str, str]] = [("600000.SS", "浦发银行"), ("600004.SS", "白云机场"), ("600009.SS", "上海机场"),
                                           ("600010.SS", "包钢股份"), ("600011.SS", "华能国际"), ("600015.SS", "华夏银行"),
                                           ("600016.SS", "民生银行"), ("600018.SS", "上港集团"), ("600019.SS", "宝钢股份"),
                                           ("600023.SS", "浙能电力"), ("600025.SS", "华能水电"), ("600027.SS", "华电国际"),
                                           ("600028.SS", "中国石化"), ("600029.SS", "南方航空"), ("600030.SS", "中信证券"),
                                           ("600031.SS", "三一重工"), ("600036.SS", "招商银行"), ("600038.SS", "中直股份"),
                                           ("600048.SS", "保利地产"), ("600050.SS", "中国联通"), ("600061.SS", "国投资本"),
                                           ("600066.SS", "宇通客车"), ("600068.SS", "葛洲坝"), ("600085.SS", "同仁堂"),
                                           ("600089.SS", "特变电工"), ("600100.SS", "同方股份"), ("600104.SS", "上汽集团"),
                                           ("600109.SS", "国金证券"), ("600111.SS", "北方稀土"), ("600115.SS", "东方航空"),
                                           ("600118.SS", "中国卫星"), ("600153.SS", "建发股份"), ("600170.SS", "上海建工"),
                                           ("600176.SS", "中国巨石"), ("600177.SS", "雅戈尔"), ("600183.SS", "生益科技"),
                                           ("600188.SS", "兖州煤业"), ("600196.SS", "复星医药"), ("600208.SS", "新湖中宝"),
                                           ("600219.SS", "南山铝业"), ("600221.SS", "海航控股"), ("600233.SS", "圆通速递"),
                                           ("600271.SS", "航天信息"), ("600276.SS", "恒瑞医药"), ("600297.SS", "广汇汽车"),
                                           ("600299.SS", "安迪苏"), ("600309.SS", "万华化学"), ("600332.SS", "白云山"),
                                           ("600340.SS", "华夏幸福"), ("600346.SS", "恒力石化"), ("600352.SS", "浙江龙盛"),
                                           ("600362.SS", "江西铜业"), ("600369.SS", "西南证券"), ("600372.SS", "中航电子"),
                                           ("600383.SS", "金地集团"), ("600390.SS", "五矿资本"), ("600398.SS", "海澜之家"),
                                           ("600406.SS", "国电南瑞"), ("600436.SS", "片仔癀"), ("600438.SS", "通威股份"),
                                           ("600482.SS", "中国动力"), ("600487.SS", "亨通光电"), ("600489.SS", "中金黄金"),
                                           ("600498.SS", "烽火通信"), ("600516.SS", "方大炭素"), ("600519.SS", "贵州茅台"),
                                           ("600522.SS", "中天科技"), ("600535.SS", "天士力"), ("600547.SS", "山东黄金"),
                                           ("600566.SS", "济川药业"), ("600570.SS", "恒生电子"), ("600583.SS", "海油工程"),
                                           ("600585.SS", "海螺水泥"), ("600588.SS", "用友网络"), ("600606.SS", "绿地控股"),
                                           ("600637.SS", "东方明珠"), ("600655.SS", "豫园股份"), ("600660.SS", "福耀玻璃"),
                                           ("600663.SS", "陆家嘴"), ("600674.SS", "川投能源"), ("600690.SS", "海尔智家"),
                                           ("600703.SS", "三安光电"), ("600705.SS", "中航资本"), ("600733.SS", "北汽蓝谷"),
                                           ("600741.SS", "华域汽车"), ("600760.SS", "中航沈飞"), ("600795.SS", "国电电力"),
                                           ("600809.SS", "山西汾酒"), ("600816.SS", "*ST安信"), ("600837.SS", "海通证券"),
                                           ("600848.SS", "上海临港"), ("600867.SS", "通化东宝"), ("600886.SS", "国投电力"),
                                           ("600887.SS", "伊利股份"), ("600893.SS", "航发动力"), ("600900.SS", "长江电力"),
                                           ("600919.SS", "江苏银行"), ("600926.SS", "杭州银行"), ("600928.SS", "西安银行"),
                                           ("600958.SS", "东方证券"), ("600968.SS", "海油发展"), ("600977.SS", "中国电影"),
                                           ("600989.SS", "宝丰能源"), ("600998.SS", "九州通"), ("600999.SS", "招商证券"),
                                           ("601006.SS", "大秦铁路"), ("601009.SS", "南京银行"), ("601012.SS", "隆基股份"),
                                           ("601018.SS", "宁波港"), ("601021.SS", "春秋航空"), ("601066.SS", "中信建投"),
                                           ("601088.SS", "中国神华"), ("601108.SS", "财通证券"), ("601111.SS", "中国国航"),
                                           ("601117.SS", "中国化学"), ("601138.SS", "工业富联"), ("601155.SS", "新城控股"),
                                           ("601162.SS", "天风证券"), ("601166.SS", "兴业银行"), ("601169.SS", "北京银行"),
                                           ("601186.SS", "中国铁建"), ("601198.SS", "东兴证券"), ("601211.SS", "国泰君安"),
                                           ("601212.SS", "白银有色"), ("601216.SS", "君正集团"), ("601225.SS", "陕西煤业"),
                                           ("601229.SS", "上海银行"), ("601236.SS", "红塔证券"), ("601238.SS", "广汽集团"),
                                           ("601288.SS", "农业银行"), ("601298.SS", "青岛港"), ("601318.SS", "中国平安"),
                                           ("601319.SS", "中国人保"), ("601328.SS", "交通银行"), ("601336.SS", "新华保险"),
                                           ("601360.SS", "三六零"), ("601377.SS", "兴业证券"), ("601390.SS", "中国中铁"),
                                           ("601398.SS", "工商银行"), ("601555.SS", "东吴证券"), ("601577.SS", "长沙银行"),
                                           ("601600.SS", "中国铝业"), ("601601.SS", "中国太保"), ("601607.SS", "上海医药"),
                                           ("601618.SS", "中国中冶"), ("601628.SS", "中国人寿"), ("601633.SS", "长城汽车"),
                                           ("601668.SS", "中国建筑"), ("601669.SS", "中国电建"), ("601688.SS", "华泰证券"),
                                           ("601698.SS", "中国卫通"), ("601727.SS", "上海电气"), ("601766.SS", "中国中车"),
                                           ("601788.SS", "光大证券"), ("601800.SS", "中国交建"), ("601808.SS", "中海油服"),
                                           ("601818.SS", "光大银行"), ("601828.SS", "美凯龙"), ("601838.SS", "成都银行"),
                                           ("601857.SS", "中国石油"), ("601877.SS", "正泰电器"), ("601878.SS", "浙商证券"),
                                           ("601881.SS", "中国银河"), ("601888.SS", "中国国旅"), ("601898.SS", "中煤能源"),
                                           ("601899.SS", "紫金矿业"), ("601901.SS", "方正证券"), ("601919.SS", "中远海控"),
                                           ("601933.SS", "永辉超市"), ("601939.SS", "建设银行"), ("601985.SS", "中国核电"),
                                           ("601988.SS", "中国银行"), ("601989.SS", "中国重工"), ("601992.SS", "金隅集团"),
                                           ("601997.SS", "贵阳银行"), ("601998.SS", "中信银行"), ("603019.SS", "中科曙光"),
                                           ("603156.SS", "养元饮品"), ("603160.SS", "汇顶科技"), ("603259.SS", "药明康德"),
                                           ("603260.SS", "合盛硅业"), ("603288.SS", "海天味业"), ("603501.SS", "韦尔股份"),
                                           ("603799.SS", "华友钴业"), ("603833.SS", "欧派家居"), ("603899.SS", "晨光文具"),
                                           ("603986.SS", "兆易创新"), ("603993.SS", "洛阳钼业"), ("000001.SZ", "平安银行"),
                                           ("000002.SZ", "万科A"), ("000063.SZ", "中兴通讯"), ("000069.SZ", "华侨城A"),
                                           ("000100.SZ", "TCL科技"), ("000157.SZ", "中联重科"), ("000166.SZ", "申万宏源"),
                                           ("000333.SZ", "美的集团"), ("000338.SZ", "潍柴动力"), ("000413.SZ", "东旭光电"),
                                           ("000415.SZ", "渤海租赁"), ("000423.SZ", "东阿阿胶"), ("000425.SZ", "徐工机械"),
                                           ("000538.SZ", "云南白药"), ("000568.SZ", "泸州老窖"), ("000596.SZ", "古井贡酒"),
                                           ("000625.SZ", "长安汽车"), ("000627.SZ", "天茂集团"), ("000629.SZ", "攀钢钒钛"),
                                           ("000630.SZ", "铜陵有色"), ("000651.SZ", "格力电器"), ("000656.SZ", "金科股份"),
                                           ("000661.SZ", "长春高新"), ("000671.SZ", "阳光城"), ("000703.SZ", "恒逸石化"),
                                           ("000709.SZ", "河钢股份"), ("000723.SZ", "美锦能源"), ("000725.SZ", "京东方A"),
                                           ("000728.SZ", "国元证券"), ("000768.SZ", "中航飞机"), ("000776.SZ", "广发证券"),
                                           ("000783.SZ", "长江证券"), ("000786.SZ", "北新建材"), ("000858.SZ", "五 粮 液"),
                                           ("000876.SZ", "新 希 望"), ("000895.SZ", "双汇发展"), ("000898.SZ", "鞍钢股份"),
                                           ("000938.SZ", "紫光股份"), ("000961.SZ", "中南建设"), ("000963.SZ", "华东医药"),
                                           ("001979.SZ", "招商蛇口"), ("002001.SZ", "新和成"), ("002007.SZ", "华兰生物"),
                                           ("002008.SZ", "大族激光"), ("002010.SZ", "传化智联"), ("002024.SZ", "苏宁易购"),
                                           ("002027.SZ", "分众传媒"), ("002032.SZ", "苏泊尔"), ("002044.SZ", "美年健康"),
                                           ("002050.SZ", "三花智控"), ("002081.SZ", "金螳螂"), ("002120.SZ", "韵达股份"),
                                           ("002142.SZ", "宁波银行"), ("002146.SZ", "荣盛发展"), ("002153.SZ", "石基信息"),
                                           ("002179.SZ", "中航光电"), ("002202.SZ", "金风科技"), ("002230.SZ", "科大讯飞"),
                                           ("002236.SZ", "大华股份"), ("002241.SZ", "歌尔股份"), ("002252.SZ", "上海莱士"),
                                           ("002271.SZ", "东方雨虹"), ("002294.SZ", "信立泰"), ("002304.SZ", "洋河股份"),
                                           ("002311.SZ", "海大集团"), ("002352.SZ", "顺丰控股"), ("002410.SZ", "广联达"),
                                           ("002411.SZ", "延安必康"), ("002415.SZ", "海康威视"), ("002422.SZ", "科伦药业"),
                                           ("002456.SZ", "欧菲光"), ("002460.SZ", "赣锋锂业"), ("002466.SZ", "天齐锂业"),
                                           ("002468.SZ", "申通快递"), ("002475.SZ", "立讯精密"), ("002493.SZ", "荣盛石化"),
                                           ("002508.SZ", "老板电器"), ("002555.SZ", "三七互娱"), ("002558.SZ", "巨人网络"),
                                           ("002594.SZ", "比亚迪"), ("002601.SZ", "龙蟒佰利"), ("002602.SZ", "世纪华通"),
                                           ("002607.SZ", "中公教育"), ("002624.SZ", "完美世界"), ("002673.SZ", "西部证券"),
                                           ("002714.SZ", "牧原股份"), ("002736.SZ", "国信证券"), ("002739.SZ", "万达电影"),
                                           ("002773.SZ", "康弘药业"), ("002841.SZ", "视源股份"), ("002916.SZ", "深南电路"),
                                           ("002938.SZ", "鹏鼎控股"), ("002939.SZ", "长城证券"), ("002945.SZ", "华林证券"),
                                           ("002958.SZ", "青农商行"), ("300003.SZ", "乐普医疗"), ("300015.SZ", "爱尔眼科"),
                                           ("300017.SZ", "网宿科技"), ("300024.SZ", "机器人"), ("300033.SZ", "同花顺"),
                                           ("300059.SZ", "东方财富"), ("300070.SZ", "碧水源"), ("300122.SZ", "智飞生物"),
                                           ("300124.SZ", "汇川技术"), ("300136.SZ", "信维通信"), ("300142.SZ", "沃森生物"),
                                           ("300144.SZ", "宋城演艺"), ("300347.SZ", "泰格医药"), ("300408.SZ", "三环集团"),
                                           ("300413.SZ", "芒果超媒"), ("300433.SZ", "蓝思科技"), ("300498.SZ", "温氏股份")]

ALL_CN_SYMBOLS: List[str] = sorted(list(set([x[0] for x in HS_300_WITH_NAME])))


# endregion

def split_mini_batch(v: List[str], mini_batch_size: int = MINI_BATCH_SIZE) -> List[List[str]]:
    ls_rlt = list()
    batch_count = len(v) // mini_batch_size
    if len(v) % mini_batch_size != 0:
        batch_count += 1
    return [v[i * mini_batch_size: (i + 1) * mini_batch_size] for i in range(batch_count)]


def _save_batch_action_2_mongo(from_function: str, func_paras: dict, parser_func: str, actions: List[RPAAction],
                               batch_additional_description: str = None,
                               per_action_description: List[str] = None) -> str:
    batch_action = RPABatchAction(batch_id=generate_uuid())
    batch_action.from_function = from_function
    batch_action.function_paras = pickle.dumps(func_paras, protocol=4)
    batch_action.extract_parser_func = parser_func
    batch_action.real_action_count = len(actions)
    batch_action.ctime = datetime.now()
    batch_action.status = ActionStatusFlag.WaitingForRun.value
    ls_rpa_action: List[RPAActionDoc] = list()
    for i, action in enumerate(actions):
        action_doc = RPAActionDoc(act_id=generate_uuid())
        action_doc.act_ctime = datetime.now()
        act_additional_description = ""
        if per_action_description is not None and len(per_action_description) > i:
            act_additional_description = per_action_description[i]
        elif batch_additional_description is not None:
            act_additional_description = batch_additional_description
        action_doc.act_description = f"{from_function} - " \
                                     f"{batch_action.batch_id} - {i + 1} / {len(actions)} - " \
                                     f"{act_additional_description}"
        action.description = action_doc.act_description
        action_doc.result_process_function = batch_action.extract_parser_func
        action_doc.status_flag = ActionStatusFlag.WaitingForRun.value
        action_doc.batch_id = batch_action.batch_id
        action_doc.idx_in_batch = i
        action_doc.act = pickle.dumps(action, protocol=4)
        action_doc.save()
        ls_rpa_action.append(action_doc)
    batch_action.real_actions = ls_rpa_action
    batch_action.save()
    return batch_action.batch_id


# region google


def google_kw_combination_news_search(kws: List[Tuple[List[str], List[str]]], pg_count: int = 3) -> str:
    """
    google keywords combination search

    return 为 batch action gid

    Examples:
    --------
        kws : [(
                ["Xi", "Trump", "State Union", "China Standing Committee"],
                ["Speech", "Visiting", "Meeting", "Hiring", "Firing", "Election", "Trade War"]
               ),
                (
                ["CDC", "Foreign Affairs", "Central Bank", "Statistics"],
                ["Speech", "Visiting", "Meeting", "Hiring", "Firing", "Election", "Trade War"]
                )]
    """
    search_kws = list()
    for kw_comb in kws:
        for curr_kws in itertools.product(*kw_comb):
            search_kws.append(" ".join([k for k in curr_kws]))
    kw_batch = split_mini_batch(search_kws)
    actions = [google_news_kws_search(minibatch_kw, pg_count) for minibatch_kw in kw_batch]
    _save_batch_action_2_mongo(from_function=cls_to_str(google_kw_combination_news_search),
                               func_paras={"kws": kws, "pg_count": pg_count},
                               parser_func=cls_to_str(GoogleNewsSearchProcess.kw_news_search),
                               actions=actions)


def google_news_search_from_symbol_company_name(symbols: List[str], pg_count: int = 5,
                                                with_quotation_mark: bool = False):
    objs = FinancialInstrumentSymbol.objects(symbol__in=symbols, info_from_yahoo__exists=True,
                                             info_from_yahoo__shortName__exists=True).only("symbol",
                                                                                           "info_from_yahoo__shortName")
    ls_search_phase: List[str] = list()
    for x in objs:
        kw = x.info_from_yahoo.shortName
        if with_quotation_mark:
            kw = f"\"{kw}\""
        search_phase = SearchingPhrase(searching_phrase=kw,
                                       related_symbols=[FinancialInstrumentSymbol(symbol=x.symbol)])
        upsert_document(search_phase, False)
        ls_search_phase.append(kw)

    mini_batch_size = 1
    kw_batch = split_mini_batch(ls_search_phase, mini_batch_size)

    actions = [google_news_kws_search(minibatch_kw, pg_count) for minibatch_kw in kw_batch]
    per_action_description = [",".join(minibatch_kw) for minibatch_kw in kw_batch]

    _save_batch_action_2_mongo(from_function=cls_to_str(google_news_search_from_symbol_company_name),
                               func_paras={"symbols": symbols, "pg_count": pg_count},
                               parser_func=cls_to_str(GoogleNewsSearchProcess.kw_news_search),
                               actions=actions,
                               per_action_description=per_action_description)


# endregion

# region tweet

def tweet_kw_combination_search_with_min_retwitter_filter(kws: List[Tuple[List[str], List[str]]],
                                                          min_retweets: int = 100, pg_count: int = 3):
    search_kws = list()
    for kw_comb in kws:
        for curr_kws in itertools.product(*kw_comb):
            search_kws.append(" ".join([k for k in curr_kws]))
    # 叠加最少 twitter 数字的限制
    real_search_kws = [f"{x} min_retweets:{min_retweets}" for x in search_kws]
    kw_batch = split_mini_batch(real_search_kws)

    actions = [twitter_kws_search(minibatch_kw, pg_count) for minibatch_kw in kw_batch]  # 这里需要换
    _save_batch_action_2_mongo(from_function=cls_to_str(tweet_kw_combination_search_with_min_retwitter_filter),
                               # !!! 这里需要换
                               func_paras={"kws": kws, "min_retweets": min_retweets, "pg_count": pg_count},  # !!! 这里需要换
                               parser_func=cls_to_str(TwitterDataProcess.kw_search),  # !!! 这里需要换
                               actions=actions)


def tweet_advance_search(search_phase: List[str], pg_count: int = 3, mini_batch_size: int = MINI_BATCH_SIZE):
    """适用于自行拼出的tweet advance search """
    mini_batch = split_mini_batch(search_phase, mini_batch_size)

    actions = [twitter_kws_search(minibatch_kw, pg_count) for minibatch_kw in mini_batch]  # 这里需要换
    per_action_description = [",".join(minibatch_kw) for minibatch_kw in mini_batch]
    _save_batch_action_2_mongo(from_function=cls_to_str(tweet_advance_search),
                               # !!! 这里需要换
                               func_paras={"search_phase": search_phase, "pg_count": pg_count},  # !!! 这里需要换
                               parser_func=cls_to_str(TwitterDataProcess.kw_search),  # !!! 这里需要换
                               actions=actions,
                               per_action_description=per_action_description)


def tweet_search_by_symbols(symbols: List[str], pg_count: int = 20):
    objs = FinancialInstrumentSymbol.objects(symbol__in=symbols, info_from_yahoo__exists=True,
                                             info_from_yahoo__shortName__exists=True).only("symbol",
                                                                                           "info_from_yahoo__shortName")
    ls_search_phase: List[str] = list()
    for x in objs:
        search_word_company_name = f"{x.info_from_yahoo.shortName} min_retweets:10"
        search_word_symbol = f"${x.symbol} min_retweets:10"
        for word in [search_word_company_name, search_word_symbol]:
            search_phase = SearchingPhrase(searching_phrase=word,
                                           related_symbols=[FinancialInstrumentSymbol(symbol=x.symbol)])
            upsert_document(search_phase, False)
            ls_search_phase.append(word)
    return tweet_advance_search(ls_search_phase, pg_count=pg_count, mini_batch_size=1)


def tweet_kol_following(min_follower: int = 100e3, only_not_queried: bool = True, max_count: int = 100,
                        pg_count: int = 10):
    filter_cond = {"follower__gte": min_follower}
    if only_not_queried:
        filter_cond["arr_following__exists"] = False
    tw_user = UserInTwitter.objects(**filter_cond).only("user_id").order_by('-follower')[:max_count]
    ls_uids = [x.user_id for x in tw_user]
    # 取 KOL 数据很耗时，所以这里 batch size 不能大，并且建议 pg_count 也不能大
    uid_batch = split_mini_batch(ls_uids, mini_batch_size=1)

    actions = [twitter_users_following(minibatch, pg_count) for minibatch in uid_batch]  # 这里需要换
    _save_batch_action_2_mongo(from_function=cls_to_str(tweet_kol_following),
                               # !!! 这里需要换
                               func_paras={"min_follower": min_follower, "pg_count": pg_count},  # !!! 这里需要换
                               parser_func=cls_to_str(TwitterDataProcess.twitter_user_following),  # !!! 这里需要换
                               actions=actions)


def tweet_account_following(ls_uids: List[str], pg_count: int = 10):
    # 取 KOL 数据很耗时，所以这里 batch size 不能大，并且建议 pg_count 也不能大
    uid_batch = split_mini_batch(ls_uids, mini_batch_size=1)

    actions = [twitter_users_following(minibatch, pg_count) for minibatch in uid_batch]  # 这里需要换
    _save_batch_action_2_mongo(from_function=cls_to_str(tweet_account_following),
                               # !!! 这里需要换
                               func_paras={"ls_uids": ls_uids, "pg_count": pg_count},  # !!! 这里需要换
                               parser_func=cls_to_str(TwitterDataProcess.twitter_user_following),  # !!! 这里需要换
                               actions=actions)


def search_tweet_from_someone_following_kol(ls_uids: List[str], min_follower: int = 1e4, pg_count: int = 50):
    s = ls_uids[0]
    for s in ls_uids:
        following_user = UserInTwitter.objects(user_id=s).first().arr_following
        ls_query = []
        set_added = set()
        for u in following_user:
            u = u.fetch()
            if u.follower and u.follower >= min_follower:
                if u.user_id not in set_added:
                    ls_query.append(f"(from:{u.user_id})")
                    set_added.add(u.user_id)
    tweet_advance_search(ls_query, pg_count, 1)


def tweet_add_nlp_by_search_kw(search_kw: str, force_refresh: bool = False):
    pk_field = "uuid"
    sort_field = "-publish_time"
    limit = 10000
    doc_cls = Article

    for field_name in ["title", "abstract"]:
        filter_cond = {f"{field_name}_ana__exists": False, f"{field_name}__exists": True}
        if force_refresh:
            filter_cond = {f"{field_name}__exists": True}
        filter_cond["from_searching_phase"] = search_kw
        docs = doc_cls.objects(**filter_cond).only(pk_field, field_name).order_by(sort_field)[:limit]
        ls_query = [
            AzureTxtAnaPara(doc=doc_cls.__name__, pk_field=pk_field, pk_val=getattr(x, pk_field), txt_field=field_name,
                            txt_value=getattr(x, field_name)) for x in docs]
        query_batch = split_mini_batch(ls_query, mini_batch_size=30)

        actions = [azure_txt_analysis(minibatch) for minibatch in query_batch]  # 这里需要换

        _save_batch_action_2_mongo(from_function=cls_to_str(tweet_add_nlp_by_search_kw),
                                   # !!! 这里需要换
                                   func_paras={"search_kw": search_kw},  # !!! 这里需要换
                                   parser_func=cls_to_str(AzureDataProcess.txt_analyse),  # !!! 这里需要换
                                   actions=actions,
                                   batch_additional_description=f"search_kw:{search_kw}, field_name:{field_name}")

    # print([x.pk_val for x in ls_query])


def azure_txt_ana(doc_cls, pk_field: str, field_name: str, sort_field: str, limit=200):
    filter_cond = {f"{field_name}_ana__exists": False, f"{field_name}__exists": True}
    docs = doc_cls.objects(**filter_cond).only(pk_field, field_name).order_by(sort_field)[:limit]

    ls_query = [
        AzureTxtAnaPara(doc=doc_cls.__name__, pk_field=pk_field, pk_val=getattr(x, pk_field), txt_field=field_name,
                        txt_value=getattr(x, field_name)) for x in docs]

    query_batch = split_mini_batch(ls_query, mini_batch_size=20)

    actions = [azure_txt_analysis(minibatch) for minibatch in query_batch]  # 这里需要换

    _save_batch_action_2_mongo(from_function=cls_to_str(azure_txt_ana),
                               # !!! 这里需要换
                               func_paras={"doc_cls": doc_cls.__name__, "field_name": field_name},  # !!! 这里需要换
                               parser_func=cls_to_str(AzureDataProcess.txt_analyse),  # !!! 这里需要换
                               actions=actions)


# endregion

# region seeking alpha


def seeking_alpha_symbol_info(symbols: List[str], pg_count: int = 3):
    act_batch = split_mini_batch(symbols, mini_batch_size=1)

    actions = [seeking_alpha_symbols_info(minibatch, pages=pg_count) for minibatch in act_batch]  # 这里需要换
    per_action_description = [",".join(minibatch) for minibatch in act_batch]
    _save_batch_action_2_mongo(from_function=cls_to_str(seeking_alpha_symbol_info),
                               # !!! 这里需要换
                               func_paras={"symbols": symbols, "pg_count": pg_count},  # !!! 这里需要换
                               parser_func=cls_to_str(SeekingAlphaDataProcess.symbol_summary),  # !!! 这里需要换
                               actions=actions,
                               per_action_description=per_action_description
                               )


def seeking_alpha_author_info(limit: int = 100):
    authors = AuthorInSeekingAlpha.objects(articles__exists=False,
                                           url__istartswith="https://seekingalpha.com/author/").only(
        "author_id").order_by("author_id")[:limit]
    if authors:
        author_ids = [x.author_id for x in authors]
        act_batch = split_mini_batch(author_ids, mini_batch_size=5)

        actions = [seeking_alpha_authors_info(minibatch) for minibatch in act_batch]  # 这里需要换
        per_action_description = [",".join(minibatch) for minibatch in act_batch]
        _save_batch_action_2_mongo(from_function=cls_to_str(seeking_alpha_symbol_info),
                                   # !!! 这里需要换
                                   func_paras={"authors": author_ids[:10]},  # !!! 这里需要换
                                   parser_func=cls_to_str(SeekingAlphaDataProcess.author_detail),  # !!! 这里需要换
                                   actions=actions,
                                   per_action_description=per_action_description
                                   )


# endregion


def remove_batch_action_result(batch_action_gid: str):
    articles = Article.objects(batch_action_uuid=batch_action_gid)
    for obj in articles:
        obj.delete()

    acts = RPAActionDoc.objects(batch_id=batch_action_gid)
    for obj in acts:
        obj.delete()

    batch_acts = RPABatchAction.objects(batch_id=batch_action_gid)
    for obj in batch_acts:
        obj.delete()


if __name__ == "__main__":
    mongo_db_conn(used_db_position, db_nlp)
    # remove_batch_action_result("C56E3841D643440590806F57D064477B")
    # print(all_chn_symbols())

    # upsert_chn_stock_info_in_yahoo()

    # google_news_search_from_symbol_company_name(ALL_SYMBOLS)
    # google_news_search_from_symbol_company_name(["GSX"])
    # google_news_search_from_symbol_company_name(ALL_HK_SYMBOLS, with_quotation_mark=True)
    # google_news_search_from_symbol_company_name(ALL_CN_SYMBOLS, with_quotation_mark=True)
    # google_news_search_from_symbol_company_name(ALL_US_SYMBOLS, with_quotation_mark=True)

    # seeking_alpha_symbol_info(list(CHINA_ARD.union(NASDAQ_100).union(DOW_30)), 8)
    # seeking_alpha_author_info(1000)

    # for i, symbol in enumerate(ALL_SYMBOLS):
    #     logger.info(f"[{i}] upsert '{symbol}' yahoo info")
    #     upsert_yahoo_financial_instrument_info(symbol)

    # tweet_search_by_symbols(ALL_SYMBOLS, 20)
    # tweet_search_by_symbols(["GSX"], 2)

    # region twitter related

    # batch_action = RPABatchAction.objects(batch_id="7A0DFD6022D541D1BED1064317BA961D").first()
    # batch_action.delete()
    # print(batch_action.from_function)

    # print(RPAActionDoc.objects(batch_id="1F7C4D86DB834F8180077133FC475C58", status_flag__in=[3, 4]).count())
    # print(RPAActionDoc.objects(status_flag=1).order_by("act_ctime").first())
    # print(RPAActionDoc.collection)

    # tweet_kol_following(max_count=50, only_not_queried=True, pg_count=5)
    # tweet_account_following(ls_uids=["ztongztong"], pg_count=100)

    # azure_txt_ana(Article, pk_field="uuid", field_name="title", sort_field="-publish_time", limit=50000)
    # azure_txt_ana(Article, pk_field="uuid", field_name="abstract", sort_field="-publish_time", limit=50000)
    # azure_txt_ana(UserInTwitter, pk_field="user_id", field_name="intro", sort_field="-follower", limit=7000)
    # search_tweet_from_someone_following_kol(["ztongztong"], min_follower=100e3, pg_count=100)

    # search_kws = ["(from:CitronResearch)", "(from:muddywatersre)", "(from:TheStreet)", "(from:TruthGundlach)",
    #               "(from:ResearchGrizzly)", "(from:HedgeyeUSA)", "(from:DougKass)"]
    # for s in search_kws:
    #     # tweet_advance_search([s], 300)
    #     # tweet_add_nlp_by_search_kw(s)
    #     pass

    # tweet_add_nlp_by_search_kw("$SPX min_retweets:10", force_refresh=True)

    # tweet_add_nlp_by_search_kw("(from:IMFNews)")

    # tweet_advance_search(["$GSX min_retweets:1"], 50)
    # tweet_advance_search(["moderna min_replies:5"], 50)
    # tweet_advance_search([f"{symbol} min_replies:5" for symbol in
    #                       ["$LK", "$SPX", "$GILD", "$SHOP", "$BYND", "$PDD", "$USO", "$GLD", "$TSLA"]], 50)

    # $GSX until:2020-01-31 since:2020-01-01 min_replies:10
    # print(get_month_periods_in_range(datetime(2018, 1, 1), datetime.now(),1))
    # ls_search = [f"$GSX until:{end.strftime('%Y-%m-%d')} since:{start.strftime('%Y-%m-%d')} min_replies:10" for
    #              (start, end) in get_month_periods_in_range(datetime(2018, 1, 1), datetime.now(), 1)]
    # ls_search.append(f"$GSX until:{datetime.now().strftime('%Y-%m-%d')} since:{datetime(2020,5,1).strftime('%Y-%m-%d')} min_replies:10")
    # tweet_advance_search(ls_search, 10)
    # print(ls_search)
    # import pandas as pd
    # pd.time

    # $GSX min_retweets:10
    # symbol = FinancialInstrumentSymbol(symbol="GSX")
    # upsert_document(symbol)
    # search = SearchingPhrase(searching_phrase="$GSX min_replies:10", kws_from_symbol=[symbol], min_tweet_reply=10)
    # upsert_document(search)

    # endregion
