# -*- coding: UTF-8 -*-

"""
定义一些与股票有关的通用 workflow 内容
"""
from datetime import datetime
from typing import List, Callable, Set, Optional

from gs_framework.utilities import generate_uuid

from gs_research_workflow.rpa_workflow.browser_workflow.allen_nlp_process import gs_nlp_process
from gs_research_workflow.rpa_workflow.result_extraction.utilities import upsert_document

from gs_research_workflow.rpa_workflow.result_extraction.general_browser_backend import GeneralBrowserBackendProcess

from gs_research_workflow.rpa_workflow.actions.action_doc_operation import append_actions_into_dynamic_batch_action
from gs_research_workflow.rpa_workflow.uipath_actions_low_level import general_desktop_browser_backend_action

from gs_research_workflow.common.serialization_utilities import cls_to_str
from gs_research_workflow.nlp.data.general_browser_workflow_docs import GeneralBrowserActionInstance, \
    TriggeredWebPagesCrawlWorkflow, EntityType

from gs_research_workflow.nlp.data.docs_in_mongo import FinancialInstrumentSymbol, FinancialInstrumentRecommendInYahoo, \
    FinancialInstrumentHolders

from gs_research_workflow.rpa_workflow.browser_workflow.web_app_resource import AllGeneralWebApp, WebAppConfig


def corp_name_remove_stop_words(orig_corp_name: str) -> str:
    """ 公司名称去掉一些常见词，这些词一般加入到搜索并没有意义 """
    s = orig_corp_name
    return s.replace(", Inc.", "").replace("Corp.", "").replace("Ltd.", "").replace("Inc.", "").replace(", LLC",
                                                                                                        "").replace(
        " LLC", "").strip()

# ---- 一些 kw combination 的生成函数 ---------


def google_kws_or(ls_kws: List[str]) -> str:
    ls_kw_to_combine = []
    for kw in ls_kws:
        if kw:
            ls_kw_to_combine.append(f'"{kw}"')
    return " | ".join(ls_kw_to_combine)


def google_kws_and(ls_kws: List[str]) -> str:
    ls_kw_to_combine = []
    for kw in ls_kws:
        if kw:
            ls_kw_to_combine.append(f'"{kw}"')
    return " ".join(ls_kw_to_combine)


# -------------------------------------------


def add_one_equity_search_action(act_uuid: str, batch_action_uuid: str,
                                 generate_func: Callable,
                                 finished_triggered_func: Optional[Callable],
                                 equity_symbol: FinancialInstrumentSymbol,
                                 webapp_cfg: WebAppConfig,
                                 kw: str,
                                 additional_kw: str,
                                 category: str,
                                 sub_category: str,
                                 action_description: str) -> str:
    browser_action = GeneralBrowserActionInstance(
        uuid=act_uuid,
        from_workflow=TriggeredWebPagesCrawlWorkflow(uuid=batch_action_uuid),
        main_entity_type=EntityType.Equity.value,
        fin_instrument=equity_symbol,
        action_gen_func=cls_to_str(generate_func),
        gwa_cfg_name=webapp_cfg.full_cfg_name,
        gwa_kw=kw,
        gwa_additional_kw=additional_kw,
        action_category=category,
        action_sub_category=sub_category,
        action_description=action_description,
        ctime=datetime.now()
    )
    upsert_document(browser_action, False)

    act_obj = general_desktop_browser_backend_action(browser_action.gwa_cfg_name, browser_action.gwa_kw,
                                                     browser_action.gwa_additional_kw)
    str_finished_triggered_func = ""
    if finished_triggered_func:
        str_finished_triggered_func = cls_to_str(finished_triggered_func)
    append_actions_into_dynamic_batch_action(batch_action_uuid,
                                             cls_to_str(GeneralBrowserBackendProcess.process_action_result),
                                             finished_triggered_func=str_finished_triggered_func,
                                             actions=[(act_obj, act_uuid, browser_action.action_description)])
    return act_uuid


CHN_KW_EQUITY_RELATED: List[str] = ["质量", "造假", "产品", "服务", "虚构", "回应", "做多", "做空", "分析"]
"""中文有关股票的若干核心关键词"""


def add_equity_sentiment_actions(equity_symbol: FinancialInstrumentSymbol, batch_action_uuid: str) -> List[str]:
    assert equity_symbol is not None

    # NOTE: equity_symbol 的数据内容可能并不全，这里调用 reload 以便于能够加载全部数据
    equity_symbol.reload()

    ls_action_uuid_rlt: List[str] = list()

    # 以 company name 搜 google news
    kw = google_kws_or([corp_name_remove_stop_words(equity_symbol.chn_name), corp_name_remove_stop_words(equity_symbol.eng_name),equity_symbol.symbol])
    act_uuid = add_one_equity_search_action(act_uuid=generate_uuid(), batch_action_uuid=batch_action_uuid,
                                            generate_func=add_equity_sentiment_actions,
                                            finished_triggered_func=gs_nlp_process,
                                            equity_symbol=equity_symbol,
                                            webapp_cfg=AllGeneralWebApp.GOOGLE_NEWS_TAB.value,
                                            kw=kw, additional_kw="",
                                            category="CorpNews", sub_category="GoogleNews",
                                            action_description=f"直接搜索公司相关新闻，避免财经站点的新闻采编出现遗漏的情况,kw={kw}"
                                            )
    ls_action_uuid_rlt.append(act_uuid)

    # 有关评级的搜索
    ls_recommend = FinancialInstrumentRecommendInYahoo.objects(symbol=equity_symbol.symbol).order_by("-t")[:10]
    set_recommend_corp_name: Set[str] = set()
    for recommend in ls_recommend:
        firm = recommend.firm.fetch()
        recommend_corp_name = firm.name
        if not recommend_corp_name:
            recommend_corp_name = firm.entity_id
        if recommend_corp_name in set_recommend_corp_name:
            continue
        set_recommend_corp_name.add(recommend_corp_name)
        kw = google_kws_and([equity_symbol.symbol, corp_name_remove_stop_words(recommend_corp_name)])
        description = f"'{equity_symbol.symbol}' achieve grade '{recommend.to_grade}'(pre '{recommend.from_grade}') by '{recommend_corp_name}' at {recommend.t}"
        act_uuid = add_one_equity_search_action(act_uuid=generate_uuid(), batch_action_uuid=batch_action_uuid,
                                                generate_func=add_equity_sentiment_actions,
                                                finished_triggered_func=gs_nlp_process,
                                                equity_symbol=equity_symbol,
                                                webapp_cfg=AllGeneralWebApp.GOOGLE_NEWS_TAB.value,
                                                kw=kw, additional_kw="",
                                                category="CorpNews", sub_category="CorpRecommendation",
                                                action_description=description
                                                )
        ls_action_uuid_rlt.append(act_uuid)
        # print(f"create google news query : {recommend.firm} + {equity_symbol.symbol}")

    # 有关机构持有人的搜索
    ls_holders = FinancialInstrumentHolders.objects(symbol=equity_symbol.symbol).order_by("-t")[:10]
    set_holder_corp_name: Set[str] = set()
    for holder in ls_holders:
        holder_corp_name = holder.holder.pk
        if holder_corp_name in set_holder_corp_name:
            continue
        kw = google_kws_and([equity_symbol.symbol, corp_name_remove_stop_words(holder_corp_name)])
        description = f"{holder_corp_name} holds '{equity_symbol.symbol}' {holder.shares} shares , market_value={holder.value} , at {holder.t}"
        act_uuid = add_one_equity_search_action(act_uuid=generate_uuid(), batch_action_uuid=batch_action_uuid,
                                                generate_func=add_equity_sentiment_actions,
                                                finished_triggered_func=gs_nlp_process,
                                                equity_symbol=equity_symbol,
                                                webapp_cfg=AllGeneralWebApp.GOOGLE_NEWS_TAB.value,
                                                kw=kw, additional_kw="",
                                                category="CorpNews", sub_category="InstitutionHolderOpinion",
                                                action_description=description
                                                )
        ls_action_uuid_rlt.append(act_uuid)

    # 在雪球中用不同的关键词搜索
    # for additional_kw in [""] + CHN_KW_EQUITY_RELATED:  # 需叠加一个空白关键词，以便于拿到所有的新闻内容
    #     cfg_obj = AllGeneralWebApp.XUEQIU_NEWS.value
    #     act_uuid = add_one_equity_search_action(act_uuid=generate_uuid(), batch_action_uuid=batch_action_uuid,
    #                                             generate_func=add_equity_sentiment_actions,
    #                                             finished_triggered_func=gs_nlp_process,
    #                                             equity_symbol=equity_symbol,
    #                                             webapp_cfg=cfg_obj,
    #                                             kw=cfg_obj.symbol_func(equity_symbol.symbol),
    #                                             additional_kw=additional_kw,
    #                                             category="CorpNews", sub_category="ChnXueqiu",
    #                                             action_description=f"Search {equity_symbol.symbol} news with keyword '{additional_kw}' in xueqiu"
    #                                             )
    #     ls_action_uuid_rlt.append(act_uuid)
    return ls_action_uuid_rlt


if __name__ == "__main__":
    from gs_research_workflow.common.mongo_resource import mongo_db_conn, used_db_position, db_nlp

    mongo_db_conn(used_db_position, db_nlp)


    # print(corp_name_remove_stop_words(test_symbol.chn_name))
    # print(corp_name_remove_stop_words(test_symbol.eng_name))

    # symbol = FinancialInstrumentSymbol.objects(symbol="AAPL").first()
    # add_equity_sentiment_actions(symbol, "debug_batch")
    # print(symbol)

    # TODO - related kw , "质量" / "造假" / "产品" / "服务" / "虚构" / "回应" / "做多" / "做空" / "分析"
    # 语言版本判断
    # import cld3
    # print(cld3.get_language("ASIS International announces transitioning GSX 2020 to fully virtual-only event experience, Global Security Exchange Plus (GSX+)."))
    pass
