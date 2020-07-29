# -*- coding: UTF-8 -*-

"""
general web app 的资源情况
"""
from enum import IntFlag, Enum
from typing import Optional, Callable

from dataclasses import dataclass

# region 提供一些财经类站点，有关 symbol 的生成规则映射函数

def symbol_to_xueqiu(symbol: str) -> str:
    """雪球的代码规则"""
    if symbol.endswith(".SS"):
        return "SH" + symbol.split(".")[0]
    elif symbol.endswith(".SZ"):
        return "SZ" + symbol.split(".")[0]
    elif symbol.endswith(".HK"):
        return symbol.split(".")[0]
    return symbol

# endregion


class EquityMarket(IntFlag):
    """ 支持的股票市场 """
    us_market = 0x01
    hk_market = 0x02
    cn_market = 0x04
    all_market = us_market | hk_market | cn_market


class SupportLanguage(IntFlag):
    """kw 所支持的语言，比如： 搜狗指数 只支持中文"""
    eng = 0x01
    chn = 0x02
    all = eng | chn


@dataclass
class WebAppConfig:
    """ 设置一个 web config 的信息 """
    category: str
    cfg_name: str
    """ use AllGeneralWebApp.value """
    kw_is_symbol: bool = False
    """标记 kw 是否为 symbol 对象"""
    symbol_func: Optional[Callable[[str], str]] = None
    """symbol 的转换函数，用于适配各种网站自定义的 symbol 规则 """
    accept_symbol_market: Optional[int] = None
    """所接受的市场"""
    additional_kw_available: bool = False
    """是否支持 additional kw"""
    kw_lang: int = SupportLanguage.all.value

    def __repr__(self):
        return str(self.__dict__)

    @property
    def full_cfg_name(self):
        return f"{self.category}/{self.cfg_name}"

# NOTE : 两部分信息暂时先分开，还没考虑好使用 submodule 的方式把两部分内容合并起来


class AllGeneralWebApp(Enum):
    """所有有效的 general web app """
    GOOGLE_NEWS_TAB = WebAppConfig(category="utility", cfg_name="google_news_tab")

    XUEQIU_NEWS = WebAppConfig(category="us_fin_web", cfg_name="xueqiu_by_symbol", kw_is_symbol=True,
                               symbol_func=symbol_to_xueqiu, accept_symbol_market=EquityMarket.all_market.value,
                               additional_kw_available=True)

