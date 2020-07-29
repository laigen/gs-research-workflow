# -*- coding: UTF-8 -*-
from datetime import date
from typing import Tuple, Optional, Dict

from gs_research_workflow.time_series.gs_steps.predefined_step_fields import TSPortfolioWeightInputStep
from gs_research_workflow.time_series.gs_steps.ts_data_steps import SymbolMultipleTSStep

from gs_research_workflow.time_series.gs_steps.local_context_step import GetContextStep

from gs_research_workflow.common.serialization_utilities import cls_to_str
from gs_research_workflow.time_series.data.tushare_wrapper import TuShareProData
from gs_research_workflow.time_series.gs_steps.ts_portfolio_ds_steps import TSPortfolioWeightTFDSStep

EQUITY_TS_FEATURES_CONTEXT = {"LOCAL":
    {
        # x 的 feature 的数据，来自于哪个 class
        "x_feature_query_class": cls_to_str(TuShareProData),
        # 与股票直接相关的 features
        "x_features_per_symbol": {
            # 个股每日基本行情
            "equity_quotation_daily": ("_daily", ["open", "high", "low", "close", "pre_close",
                                                  "change", "pct_chg", "vol", "amount"]),
            # 个股每日指标
            "equity_basic_daily": ("_fin_ind", ["turnover_rate", "turnover_rate_f",
                                                "volume_ratio", "pe", "pe_ttm", "pb", "ps",
                                                "ps_ttm", "dv_ratio", "dv_ttm",
                                                "total_share", "free_share", "total_mv", "circ_mv"]),
            # 复权因子
            "equity_adj_factor_daily": ("_adj", ["adj_factor"]),
            # 个股后复权行情
            "equity_backward_adjust_daily": ("_backward_adj", ["open", "high", "low", "close", "pre_close",
                                                               "change", "pct_chg", "vol", "amount"]),
            # 个股每日资金流向
            "equity_moneyflow_daily": ("_moneyflow", ["buy_sm_vol", "buy_sm_amount", "sell_sm_vol",
                                                      "sell_sm_amount", "buy_md_vol", "buy_md_amount",
                                                      "sell_md_vol", "sell_md_amount", "buy_lg_vol",
                                                      "buy_lg_amount", "sell_lg_vol", "sell_lg_amount",
                                                      "buy_elg_vol", "buy_elg_amount", "sell_elg_vol",
                                                      "sell_elg_amount", "net_mf_vol", "net_mf_amount"])
        },
        "train_val_ds_pip": "lambda ds: ds.repeat().batch(20)",
        "test_ds_pip": "lambda ds: ds.batch(10)",  # ALERT : test_ds 不能加 repeat，需要是一个有限集。如果是无限集，则需要加 steps 参数
    }
}


def generate_portfolio_ts_datas(workflow_context: Dict = EQUITY_TS_FEATURES_CONTEXT,
                                # 这里通过取 不同时间段的 portfolio 数据来区分 train / val
                                train_start_t: date = date(2017, 1, 1), train_end_t: date = date(2019, 7, 1),
                                val_start_t: date = date(2019, 7, 2), val_end_t: date = date(2019, 10, 1),
                                eval_start_t: date = date(2019, 10, 2), eval_end_t: date = date(2019, 12, 31),
                                false_sample_ratio: float = 1.,
                                lookback_period: int = 72,
                                use_ssh_index: bool = True, use_szse_index: bool = True, use_csi_index: bool = True,
                                use_fund_in_otc: bool = True, use_fund_in_exchange: bool = True,
                                random_state: Optional[int] = 100,
                                time_steps_as_last_dimension: bool = False) \
        -> Tuple[TSPortfolioWeightTFDSStep, TSPortfolioWeightTFDSStep, TSPortfolioWeightTFDSStep]:
    all_context_step = {k: GetContextStep(k) for k in workflow_context["LOCAL"].keys()}
    for k, v in all_context_step.items():
        v.SET_CONTEXT(workflow_context)
    equity_data_step = SymbolMultipleTSStep(
        _input_steps=[(all_context_step["x_feature_query_class"], "data_query_class"),
                      (all_context_step["x_features_per_symbol"], "apis_and_columns")])

    pre_define_train_data_step = TSPortfolioWeightInputStep(use_ssh_index=use_ssh_index, use_szse_index=use_szse_index,
                                                            use_csi_index=use_csi_index,
                                                            use_fund_in_otc=use_fund_in_otc,
                                                            use_fund_in_exchange=use_fund_in_exchange,
                                                            query_start_t=train_start_t,
                                                            query_end_t=train_end_t)

    pre_define_val_data_step = TSPortfolioWeightInputStep(use_ssh_index=use_ssh_index, use_szse_index=use_szse_index,
                                                          use_csi_index=use_csi_index,
                                                          use_fund_in_otc=use_fund_in_otc,
                                                          use_fund_in_exchange=use_fund_in_exchange,
                                                          query_start_t=val_start_t,
                                                          query_end_t=val_end_t)

    pre_define_eval_data_step = TSPortfolioWeightInputStep(use_ssh_index=use_ssh_index, use_szse_index=use_szse_index,
                                                           use_csi_index=use_csi_index,
                                                           use_fund_in_otc=use_fund_in_otc,
                                                           use_fund_in_exchange=use_fund_in_exchange,
                                                           query_start_t=eval_start_t,
                                                           query_end_t=eval_end_t)

    portfolio_weight_train_ds_step = TSPortfolioWeightTFDSStep(
        random_state=random_state,
        false_sample_ratio=false_sample_ratio,
        # ALERT： lookback_period 这个参数不能随意取，在 Bert model 中，该值必须为 num_attention_heads * head_size，即 hidden_size 值相同
        lookback_period=lookback_period,
        time_steps_as_last_dimension=time_steps_as_last_dimension,
        # 目前同一个step 的多个 Property 传入 多个 Fields 会出错，所以用 rule_name 的方式，在 list 中 repeat
        _input_steps=[pre_define_train_data_step, (pre_define_train_data_step, "market_indicator"),
                      (equity_data_step, "equity_ts_callable"), (all_context_step["train_val_ds_pip"], "ds_pip")]
    )

    portfolio_weight_val_ds_step = TSPortfolioWeightTFDSStep(
        random_state=random_state,
        false_sample_ratio=false_sample_ratio,
        # ALERT： lookback_period 这个参数不能随意取，在 Bert model 中，该值必须为 num_attention_heads * head_size，即 hidden_size 值相同
        lookback_period=lookback_period,
        time_steps_as_last_dimension=time_steps_as_last_dimension,
        # 目前同一个step 的多个 Property 传入 多个 Fields 会出错，所以用 rule_name 的方式，在 list 中 repeat
        _input_steps=[pre_define_val_data_step, (pre_define_val_data_step, "market_indicator"),
                      (equity_data_step, "equity_ts_callable"), (all_context_step["train_val_ds_pip"], "ds_pip")]
    )

    portfolio_weight_eval_ds_step = TSPortfolioWeightTFDSStep(
        random_state=random_state,
        false_sample_ratio=false_sample_ratio,
        # ALERT： lookback_period 这个参数不能随意取，在 Bert model 中，该值必须为 num_attention_heads * head_size，即 hidden_size 值相同
        lookback_period=lookback_period,
        time_steps_as_last_dimension=time_steps_as_last_dimension,
        # 目前同一个step 的多个 Property 传入 多个 Fields 会出错，所以用 rule_name 的方式，在 list 中 repeat
        _input_steps=[pre_define_eval_data_step, (pre_define_eval_data_step, "market_indicator"),
                      (equity_data_step, "equity_ts_callable"), (all_context_step["test_ds_pip"], "ds_pip")]
    )
    return portfolio_weight_train_ds_step, portfolio_weight_val_ds_step, portfolio_weight_eval_ds_step
