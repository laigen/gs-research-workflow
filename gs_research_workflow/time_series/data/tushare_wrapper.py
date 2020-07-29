# -*- coding: utf-8 -*-
"""
tushare api 的封装类，以便于能够方便的与 tf.data 相关接口进行对接

"""
import logging
from datetime import date, datetime, timedelta
from functools import partial
from typing import Union, Optional, List, Dict, Tuple, Set, Any, Callable

import pandas as pd
import tushare as ts
from gs_framework.utilities import md5_str

from gs_research_workflow.time_series.data.arctic_and_local_cache import ArcticAndLocalCacheBySymbol, \
    SymbolTSRemoteSyncToArcticInfo, convert_column_as_datetime, CSApiRemoteSyncToArcticInfo, \
    convert_column_as_datetime_minus_one_day, convert_columns_as_datetime
from gs_research_workflow.time_series.data.arctic_version_storage import ArcticVersionStorageMixin
from gs_research_workflow.time_series.data.utilities import filter_df_by_t_and_cols, \
    arctic_daily_data_expired_default_strategy, arctic_non_ts_data_expired_default_strategy, \
    arctic_non_ts_data_expired_month_end

logger = logging.getLogger(__name__)

_TUSHARE_TOKEN_LAIGEN: str = "" # your tushare token
"""暂时先内置了一个用于调试的tushare pro token"""

_DATE_STRFTIME: str = "%Y%m%d"
"""tushare中对于时间的格式转换"""


def get_month_periods(start_t: datetime, period_month_count: int = 3) -> List[Tuple[date, date]]:
    max_periods = int((datetime.today() - start_t).days / (30 * period_month_count)) + 2
    date_index = pd.date_range(periods=max_periods, end=datetime.today(), freq=pd.offsets.MonthEnd(period_month_count))
    ls_month_period = date_index[date_index >= start_t].tolist()
    return [((dt1.date() + timedelta(days=1)), dt2.date()) for dt1, dt2 in zip(ls_month_period[0:-1], ls_month_period[1:])]


def get_month_periods_in_range(start_t: datetime, end_t: datetime, period_month_count: int = 3) -> List[
    Tuple[date, date]]:

    max_periods = int((end_t - start_t).days / (30*period_month_count)) + 2
    date_index = pd.date_range(periods=max_periods, end=end_t.date(), freq=pd.offsets.MonthEnd(period_month_count))
    ls_month_period = date_index[date_index >= (start_t-timedelta(days=1))].tolist()
    return [((dt1.date() + timedelta(days=1)), dt2.date()) for dt1, dt2 in zip(ls_month_period[0:-1], ls_month_period[1:])]


def _get_tushare_pro_api(token='', timeout=15):
    """
    从 tushare d  pro_api 函数修改而来，为了能够支持 timeout 的参数项
    """
    from tushare.util import upass
    from tushare.pro import client

    if token == '' or token is None:
        token = upass.get_token()
    if token is not None and token != '':
        pro = client.DataApi(token,timeout)
        return pro
    else:
        raise Exception('api init error.')


class TuShareProData(ArcticVersionStorageMixin, ArcticAndLocalCacheBySymbol):
    API_PROVIDER_NAME: str = "tushare_pro"
    lib_prefix: str = "tushare_"
    CS_LIB_NAME = "cs_from_tushare"

    DAILY_ALL_HISTORY_QUERY_PERIOD = [(date(1990, 1, 1), date(2005, 12, 31)),
                                      (date(2006, 1, 1), date(2015, 12, 31)),
                                      (date(2016, 1, 1), datetime.today().date())]
    """历史数据不能一次性取出，所以这里对 tushare 的数据做分段情况"""

    def __init__(self, token: str = _TUSHARE_TOKEN_LAIGEN, use_l3_cache: bool = True):
        super().__init__(use_l3_cache)
        self.ts_pro = _get_tushare_pro_api(token, 60)  # 使用自定义的 timeout 参数

        self._equity_concept = dict()

    @property
    def pro_api(self):
        return self.ts_pro

    def get_recommend_sync_info(self, f_query, symbol: str,
                                init_query_paras=DAILY_ALL_HISTORY_QUERY_PERIOD) -> SymbolTSRemoteSyncToArcticInfo:
        """提供一个适合于大多数情况的 sync_info 的数据内容，各接口可根据具体情况，进行细项目的调整
        NOTE: 这里假定 init_query_paras 是升序排列的，逆序调用接口时，只要找到第一条不符合内容的信息，则不再向前追溯
        """
        sync_info = SymbolTSRemoteSyncToArcticInfo()
        sync_info.f_init_query = lambda start, end: f_query(ts_code=symbol,
                                                            start_date=start.strftime(_DATE_STRFTIME),
                                                            end_date=end.strftime(_DATE_STRFTIME))

        sync_info.f_new_data_query = lambda last_t: f_query(ts_code=symbol,
                                                            start_date=(last_t + timedelta(days=1)).strftime(
                                                                _DATE_STRFTIME))
        sync_info.ls_init_query_paras = init_query_paras
        sync_info.f_check_arctic_need_update = arctic_daily_data_expired_default_strategy
        sync_info.chunk_size = "M"
        return sync_info

    def get_non_ts_sync_info(self, f_query, **kwargs) -> SymbolTSRemoteSyncToArcticInfo:
        """获取非 ts 类数据的更新数据结构"""
        sync_info = SymbolTSRemoteSyncToArcticInfo()
        sync_info.f_init_query = lambda: f_query(**kwargs)

        sync_info.f_new_data_query = None
        sync_info.ls_init_query_paras = None
        sync_info.f_check_arctic_need_update = arctic_non_ts_data_expired_default_strategy
        sync_info.chunk_size = None
        return sync_info

    def _run_get_data_and_return(self, lib_name: str, symbol: str, start, end, sync_info: SymbolTSRemoteSyncToArcticInfo, cols,
                                 re_init: bool) -> pd.DataFrame:
        full_lib_name = self.lib_prefix + lib_name

        if re_init:
            self.clean_up_symbol_data(full_lib_name, symbol)

        df = self._maybe_read_from_local_cache(full_lib_name, symbol, sync_info)
        if df is None:
            return df
        return filter_df_by_t_and_cols(df, start, end, cols)

    def _run_non_ts_get_data_and_return(self, lib_name: str, symbol: str, sync_info: SymbolTSRemoteSyncToArcticInfo, cols,
                                        re_init: bool) -> pd.DataFrame:
        full_lib_name = self.lib_prefix + lib_name

        if re_init:
            self.clean_up_version_object_data(full_lib_name, symbol)

        df = self._maybe_read_version_object_from_local_cache(full_lib_name, symbol, sync_info)
        return filter_df_by_t_and_cols(df, None, None, cols)

    # region TS by Symbol 接口
    def equity_quotation_daily(self, symbol: str, start: Optional[Union[date, datetime]] = None,
                               end: Optional[Union[date, datetime]] = None,
                               cols: Optional[List[str]] = None, re_init: bool = False) -> pd.DataFrame:
        """
        see https://tushare.pro/document/2?doc_id=27
        """
        # 数据接口相关的内容
        sync_info = self.get_recommend_sync_info(self.ts_pro.daily, symbol)
        sync_info.f_original_df_process = lambda x: convert_column_as_datetime(x, "trade_date", "date").drop(
            columns=["ts_code", "trade_date"]).set_index("date")

        return self._run_get_data_and_return("daily_per_symbol", symbol, start, end, sync_info, cols, re_init)

    def equity_basic_daily(self, symbol: str, start: Optional[Union[date, datetime]] = None,
                           end: Optional[Union[date, datetime]] = None,
                           cols: Optional[List[str]] = None,
                           re_init: bool = False) -> pd.DataFrame:
        """
        see https://tushare.pro/document/2?doc_id=32
        """
        # 数据接口相关的内容
        sync_info = self.get_recommend_sync_info(self.ts_pro.daily_basic, symbol)
        sync_info.f_original_df_process = lambda x: convert_column_as_datetime(x, "trade_date", "date").drop(
            columns=["ts_code", "trade_date"]).set_index("date")

        return self._run_get_data_and_return("basic_daily_per_symbol", symbol, start, end, sync_info, cols, re_init)

    def equity_backward_adjust_daily(self, symbol: str, start: Optional[Union[date, datetime]] = None,
                                     end: Optional[Union[date, datetime]] = None,
                                     cols: Optional[List[str]] = None,
                                     re_init: bool = False) -> pd.DataFrame:
        """
        see https://tushare.pro/document/2?doc_id=32
        """
        f = lambda ts_code, start_date, end_date='': ts.pro_bar(ts_code=ts_code, api=self.ts_pro, asset="E", adj="hfq",
                                                             freq="D", start_date=start_date, end_date=end_date)
        # 数据接口相关的内容
        sync_info = self.get_recommend_sync_info(f, symbol)
        sync_info.f_original_df_process = lambda x: convert_column_as_datetime(x, "trade_date", "date").drop(
            columns=["ts_code", "trade_date"]).set_index("date")

        return self._run_get_data_and_return("backward_adjust_daily_per_symbol", symbol, start, end, sync_info, cols, re_init)

    def _equity_adj_factor_all(self, symbol: str, re_init: bool = False) -> pd.DataFrame:
        sync_info = self.get_recommend_sync_info(self.ts_pro.adj_factor, symbol)
        sync_info.f_original_df_process = lambda x: convert_column_as_datetime(x, "trade_date", "date").drop(
            columns=["ts_code", "trade_date"]).set_index("date")
        return self._run_get_data_and_return("adj_factor_per_symbol", symbol, None, None, sync_info, None, re_init)

    def equity_adj_factor_daily(self, symbol: str, start: Optional[Union[date, datetime]] = None,
                                     end: Optional[Union[date, datetime]] = None,
                                     cols: Optional[List[str]] = None,
                                     re_init: bool = False) -> pd.DataFrame:
        """ 复权因子 https://tushare.pro/document/2?doc_id=28 """
        # 先得到所有的数据
        df = self._equity_adj_factor_all(symbol, re_init)
        # 需要对数据今天填值
        df = df.fillna(method="ffill").fillna(1.)
        return filter_df_by_t_and_cols(df, start, end, cols)


    def equity_moneyflow_daily(self, symbol: str, start: Optional[Union[date, datetime]] = None,
                               end: Optional[Union[date, datetime]] = None,
                               cols: Optional[List[str]] = None,
                               re_init: bool = False) -> pd.DataFrame:
        """https://tushare.pro/document/2?doc_id=170"""
        sync_info = self.get_recommend_sync_info(self.ts_pro.moneyflow, symbol)
        sync_info.f_original_df_process = lambda x: convert_column_as_datetime(x, "trade_date", "date").drop(
            columns=["ts_code", "trade_date"]).set_index("date").fillna(0.0)

        return self._run_get_data_and_return("equity_moneyflow_daily_per_symbol", symbol, start, end, sync_info, cols,
                                             re_init)

    def index_quotation_daily(self, symbol: str, start: Optional[Union[date, datetime]] = None,
                              end: Optional[Union[date, datetime]] = None,
                              cols: Optional[List[str]] = None,
                              re_init: bool = False) -> pd.DataFrame:
        """
        see https://tushare.pro/document/2?doc_id=95
        """
        # 数据接口相关的内容
        sync_info = self.get_recommend_sync_info(self.ts_pro.index_daily, symbol)
        sync_info.f_original_df_process = lambda x: convert_column_as_datetime(x, "trade_date", "date").drop(
            columns=["ts_code", "trade_date"]).set_index("date")

        return self._run_get_data_and_return("index_daily_per_symbol", symbol, start, end, sync_info, cols,
                                             re_init)

    def margin(self, exchange_id: str, start: Optional[Union[date, datetime]] = None,
               end: Optional[Union[date, datetime]] = None,
               cols: Optional[List[str]] = None,
               re_init: bool = False) -> pd.DataFrame:
        # 用一个函数，改变第一个参数名为 ts_code
        f = lambda ts_code, start_date, end_date=None: self.ts_pro.margin(exchange_id=ts_code, start_date=start_date,
                                                                     end_date=end_date)
        sync_info = self.get_recommend_sync_info(f, exchange_id)
        sync_info.f_original_df_process = lambda x: convert_column_as_datetime(x, "trade_date", "date").drop(
            columns=["exchange_id", "trade_date"]).set_index("date")

        return self._run_get_data_and_return("margin_per_exchange", exchange_id, start, end, sync_info, cols,
                                             re_init)

    def index_weight(self, symbol: str, start: Optional[Union[date, datetime]] = None,
                     end: Optional[Union[date, datetime]] = None,
                     cols: Optional[List[str]] = None,
                     re_init: bool = False) -> pd.DataFrame:
        """
        see https://tushare.pro/document/2?doc_id=96
        """
        # 数据接口相关的内容
        # 因为这里用的参数名是 index_code ， 所以用一个 lambda 的函数调整参数名

        f = lambda ts_code, start_date, end_date='': self.ts_pro.index_weight(index_code=ts_code, start_date=start_date,
                                                                              end_date=end_date)
        ls_init_query_period = list()

        # 这里不清楚单期是否会超过最多 4000条记录的  tushare 请求限制，所有都改为按照月度获取数据，并且获取的数据从 2000年开始
        ls_init_query_period = get_month_periods(datetime(2000, 1, 1), 1)

        # 2020.01.30 废弃原先 hardcode 的分批次策略
        # 这里做一个 hardcode，tushare接口限制了一次性只能拿到 4000条记录，
        #  为了避免市场指数的数据拿不全，这里对全市场指数一次只拿 1M 的数据
        # if symbol in set(["000001.SH", "399001.SZ"]):
        #     ls_init_query_period = get_month_periods(datetime(1990, 1, 1), 1)
        # else:  # 其他的先假定每个月的平均成分股不超过 2000 条
        #     ls_init_query_period = get_month_periods(datetime(1990, 1, 1), 2)

        sync_info = self.get_recommend_sync_info(f, symbol, ls_init_query_period)
        sync_info.f_original_df_process = lambda x: convert_column_as_datetime(x, "trade_date", "date").drop(
            columns=["index_code", "trade_date"]).set_index("date")

        return self._run_get_data_and_return("index_weight_per_symbol", symbol, start, end, sync_info, cols,
                                             re_init)

    @staticmethod
    def _convert_enddate_index_and_accumulate_to_single_period(df: pd.DataFrame, quarterly_cols: List[str] = [],
                                                               semi_yearly_cols: List[str] = []) -> pd.DataFrame:
        assert len(set(quarterly_cols).intersection(set(semi_yearly_cols))) == 0
        df = df.drop_duplicates(subset="end_date", keep="last")
        df = convert_columns_as_datetime(df, ["end_date", "f_ann_date"])
        df = df.reset_index(drop=True).set_index("end_date", drop=False)
        fix_column_to_drop = ["comp_type", "report_type", "end_date", "f_ann_date"]
        if quarterly_cols:
            for col in quarterly_cols:
                col_prev = f"prev_{col}"
                col_single_period = f"_{col}"
                df.loc[:, col_prev] = df[col].shift(1)
                df.loc[:, col_single_period] = df.apply(
                    lambda row: row[col] - row[col_prev] if row["end_date"].month in (6, 9, 12) else row[col], axis=1)
            df.drop(columns=quarterly_cols + ["prev_" + col for col in quarterly_cols],
                    inplace=True)
            df.rename(columns={"_" + col: col for col in quarterly_cols}, inplace=True)

        if semi_yearly_cols:
            for col in semi_yearly_cols:
                col_prev = f"prev_{col}"
                col_single_period = f"_{col}"
                df.loc[:, col_prev] = df[col].shift(2)
                df.loc[:, col_single_period] = df.apply(
                    lambda row: row[col] - row[col_prev] if row["end_date"].month == 12 else row[col], axis=1)
            df.drop(columns=semi_yearly_cols + ["prev_" + col for col in semi_yearly_cols],
                    inplace=True)
            df.rename(columns={"_" + col: col for col in semi_yearly_cols}, inplace=True)

        df.drop(columns=fix_column_to_drop, inplace=True)
        return df

    _income_cols: List[str] = ["basic_eps", "diluted_eps", "total_revenue", "revenue", "int_income",
                                          "prem_earned",
                                          "comm_income", "n_commis_income", "n_oth_income", "n_oth_b_income",
                                          "prem_income",
                                          "out_prem",
                                          "une_prem_reser", "reins_income", "n_sec_tb_income", "n_sec_uw_income",
                                          "n_asset_mg_income",
                                          "oth_b_income", "fv_value_chg_gain", "invest_income", "ass_invest_income",
                                          "forex_gain",
                                          "total_cogs", "oper_cost", "int_exp", "comm_exp", "biz_tax_surchg",
                                          "sell_exp",
                               "admin_exp",
                               "fin_exp", "assets_impair_loss", "prem_refund", "compens_payout",
                               "reser_insur_liab",
                               "div_payt", "reins_exp", "oper_exp", "compens_payout_refu",
                               "insur_reser_refu",
                               "reins_cost_refund", "other_bus_cost", "operate_profit", "non_oper_income",
                               "non_oper_exp",
                               "nca_disploss", "total_profit", "income_tax", "n_income", "n_income_attr_p",
                               "minority_gain",
                               "oth_compr_income", "t_compr_income", "compr_inc_attr_p",
                               "compr_inc_attr_m_s", "ebit",
                               "ebitda", "insurance_exp", "undist_profit", "distable_profit"]
    """利润表中累积类型的字段"""

    _income_semi_yearly_report_cols: List[str] = ['ebitda']

    def income(self, symbol: str, report_type: int = 1, comp_type: Optional[int] = None,
               start: Optional[Union[date, datetime]] = None,
               end: Optional[Union[date, datetime]] = None,
               cols: Optional[List[str]] = None, re_init: bool = False) -> pd.DataFrame:
        """
        see https://tushare.pro/document/2?doc_id=33
        """
        # 数据接口相关的内容
        f = lambda ts_code, start_date, end_date=None: self.ts_pro.income(ts_code=ts_code, report_type=report_type,
                                                                          comp_type=comp_type, start_date=start_date,
                                                                          end_date=end_date)
        sync_info = self.get_recommend_sync_info(f, symbol)

        sync_info.f_original_df_process = lambda x: convert_column_as_datetime(x, "ann_date", "date").drop(
            columns=["ts_code", "ann_date"]).set_index("date").astype({k: "float64" for k in TuShareProData._income_cols})

        return self._run_get_data_and_return(f"income_{report_type}_{comp_type}_per_symbol", symbol, start, end,
                                             sync_info, cols, re_init)

    def income_by_enddate(self, symbol: str, to_single_period_val: bool = False,
                          start: Optional[Union[date, datetime]] = None,
                          end: Optional[Union[date, datetime]] = None,
                          cols: Optional[List[str]] = None, re_init: bool = False) -> pd.DataFrame:
        """提供以enddate作为index 的现金流量表，提供参数 to_single_period_val 可以将输入转成单期值"""
        df = self.income(symbol=symbol, report_type=1, re_init=re_init)

        df = TuShareProData._convert_enddate_index_and_accumulate_to_single_period(df, list(
            set(TuShareProData._income_cols) - set(
                TuShareProData._income_semi_yearly_report_cols)) if to_single_period_val else [],
                                                                                   TuShareProData._income_semi_yearly_report_cols if to_single_period_val else [])

        return filter_df_by_t_and_cols(df, start, end, cols)

    _balancesheet_cols: List[str] = ['total_share', 'cap_rese', 'undistr_porfit', 'surplus_rese', 'special_rese',
                                     'money_cap',
                                     'trad_asset', 'notes_receiv', 'accounts_receiv', 'oth_receiv', 'prepayment',
                                     'div_receiv',
                                     'int_receiv', 'inventories', 'amor_exp', 'nca_within_1y', 'sett_rsrv',
                                     'loanto_oth_bank_fi',
                                     'premium_receiv', 'reinsur_receiv', 'reinsur_res_receiv', 'pur_resale_fa',
                                     'oth_cur_assets',
                                     'total_cur_assets', 'fa_avail_for_sale', 'htm_invest', 'lt_eqt_invest',
                                     'invest_real_estate',
                                     'time_deposits', 'oth_assets', 'lt_rec', 'fix_assets', 'cip', 'const_materials',
                                     'fixed_assets_disp', 'produc_bio_assets', 'oil_and_gas_assets', 'intan_assets',
                                     'r_and_d',
                                     'goodwill', 'lt_amor_exp', 'defer_tax_assets', 'decr_in_disbur', 'oth_nca',
                                     'total_nca',
                                     'cash_reser_cb', 'depos_in_oth_bfi', 'prec_metals', 'deriv_assets',
                                     'rr_reins_une_prem',
                                     'rr_reins_outstd_cla', 'rr_reins_lins_liab', 'rr_reins_lthins_liab',
                                     'refund_depos',
                                     'ph_pledge_loans', 'refund_cap_depos', 'indep_acct_assets', 'client_depos',
                                     'client_prov',
                                     'transac_seat_fee', 'invest_as_receiv', 'total_assets', 'lt_borr', 'st_borr',
                                     'cb_borr',
                                     'depos_ib_deposits', 'loan_oth_bank', 'trading_fl', 'notes_payable',
                                     'acct_payable',
                                     'adv_receipts', 'sold_for_repur_fa', 'comm_payable', 'payroll_payable',
                                     'taxes_payable',
                                     'int_payable', 'div_payable', 'oth_payable', 'acc_exp', 'deferred_inc',
                                     'st_bonds_payable',
                                     'payable_to_reinsurer', 'rsrv_insur_cont', 'acting_trading_sec', 'acting_uw_sec',
                                     'non_cur_liab_due_1y', 'oth_cur_liab', 'total_cur_liab', 'bond_payable',
                                     'lt_payable',
                                     'specific_payables', 'estimated_liab', 'defer_tax_liab', 'defer_inc_non_cur_liab',
                                     'oth_ncl',
                                     'total_ncl', 'depos_oth_bfi', 'deriv_liab', 'depos', 'agency_bus_liab', 'oth_liab',
                                     'prem_receiv_adva', 'depos_received', 'ph_invest', 'reser_une_prem',
                                     'reser_outstd_claims',
                                     'reser_lins_liab', 'reser_lthins_liab', 'indept_acc_liab', 'pledge_borr',
                                     'indem_payable',
                                     'policy_div_payable', 'total_liab', 'treasury_share', 'ordin_risk_reser',
                                     'forex_differ',
                                     'invest_loss_unconf', 'minority_int', 'total_hldr_eqy_exc_min_int',
                                     'total_hldr_eqy_inc_min_int', 'total_liab_hldr_eqy', 'lt_payroll_payable',
                                     'oth_comp_income',
                                     'oth_eqt_tools', 'oth_eqt_tools_p_shr', 'lending_funds', 'acc_receivable',
                                     'st_fin_payable',
                                     'payables', 'hfs_assets', 'hfs_sales']
    _balancesheet_semi_yearly_report_cols: List[str] = ['oth_cur_assets', 'fa_avail_for_sale', 'oth_nca',
                                                        'bond_payable', 'lt_payable', 'defer_inc_non_cur_liab',
                                                        'oth_ncl']

    def balancesheet(self, symbol: str, report_type: int = 1, comp_type: Optional[int] = None,
                     start: Optional[Union[date, datetime]] = None,
                     end: Optional[Union[date, datetime]] = None,
                     cols: Optional[List[str]] = None, re_init: bool = False) -> pd.DataFrame:
        """see https://tushare.pro/document/2?doc_id=36"""
        # 数据接口相关的内容
        f = lambda ts_code, start_date, end_date=None: self.ts_pro.balancesheet(ts_code=ts_code,
                                                                                report_type=report_type,
                                                                                comp_type=comp_type,
                                                                                start_date=start_date,
                                                                                end_date=end_date)
        sync_info = self.get_recommend_sync_info(f, symbol)

        sync_info.f_original_df_process = lambda x: convert_column_as_datetime(x, "ann_date", "date").drop(
            columns=["ts_code", "ann_date"]).set_index("date").astype({k: "float64" for k in TuShareProData._balancesheet_cols})

        return self._run_get_data_and_return(f"balancesheet_{report_type}_{comp_type}_per_symbol", symbol, start, end,
                                             sync_info, cols, re_init)

    def balancesheet_by_enddate(self, symbol: str,
                                start: Optional[Union[date, datetime]] = None,
                                end: Optional[Union[date, datetime]] = None,
                                cols: Optional[List[str]] = None, re_init: bool = False) -> pd.DataFrame:
        """提供以enddate作为index 的现金流量表，提供参数 to_single_period_val 可以将输入转成单期值"""
        df = self.balancesheet(symbol=symbol, report_type=1, re_init=re_init)
        df = TuShareProData._convert_enddate_index_and_accumulate_to_single_period(df, [],[])
        return filter_df_by_t_and_cols(df, start, end, cols)

    _cashflow_cols: List[str] = ['net_profit', 'finan_exp', 'c_fr_sale_sg', 'recp_tax_rends', 'n_depos_incr_fi',
                                 'n_incr_loans_cb', 'n_inc_borr_oth_fi', 'prem_fr_orig_contr', 'n_incr_insured_dep',
                                 'n_reinsur_prem', 'n_incr_disp_tfa', 'ifc_cash_incr', 'n_incr_disp_faas',
                                 'n_incr_loans_oth_bank', 'n_cap_incr_repur', 'c_fr_oth_operate_a',
                                 'c_inf_fr_operate_a',
                                 'c_paid_goods_s', 'c_paid_to_for_empl', 'c_paid_for_taxes', 'n_incr_clt_loan_adv',
                                 'n_incr_dep_cbob', 'c_pay_claims_orig_inco', 'pay_handling_chrg',
                                 'pay_comm_insur_plcy',
                                 'oth_cash_pay_oper_act', 'st_cash_out_act', 'n_cashflow_act', 'oth_recp_ral_inv_act',
                                 'c_disp_withdrwl_invest', 'c_recp_return_invest', 'n_recp_disp_fiolta',
                                 'n_recp_disp_sobu',
                                 'stot_inflows_inv_act', 'c_pay_acq_const_fiolta', 'c_paid_invest',
                                 'n_disp_subs_oth_biz',
                                 'oth_pay_ral_inv_act', 'n_incr_pledge_loan', 'stot_out_inv_act', 'n_cashflow_inv_act',
                                 'c_recp_borrow', 'proc_issue_bonds', 'oth_cash_recp_ral_fnc_act',
                                 'stot_cash_in_fnc_act',
                                 'free_cashflow', 'c_prepay_amt_borr', 'c_pay_dist_dpcp_int_exp',
                                 'incl_dvd_profit_paid_sc_ms',
                                 'oth_cashpay_ral_fnc_act', 'stot_cashout_fnc_act', 'n_cash_flows_fnc_act',
                                 'eff_fx_flu_cash',
                                 'n_incr_cash_cash_equ', 'c_cash_equ_beg_period', 'c_cash_equ_end_period',
                                 'c_recp_cap_contrib',
                                 'incl_cash_rec_saims', 'uncon_invest_loss', 'prov_depr_assets', 'depr_fa_coga_dpba',
                                 'amort_intang_assets', 'lt_amort_deferred_exp', 'decr_deferred_exp', 'incr_acc_exp',
                                 'loss_disp_fiolta', 'loss_scr_fa', 'loss_fv_chg', 'invest_loss',
                                 'decr_def_inc_tax_assets',
                                 'incr_def_inc_tax_liab', 'decr_inventories', 'decr_oper_payable', 'incr_oper_payable',
                                 'others', 'im_net_cashflow_oper_act', 'conv_debt_into_cap',
                                 'conv_copbonds_due_within_1y',
                                 'fa_fnc_leases', 'end_bal_cash', 'beg_bal_cash', 'end_bal_cash_equ',
                                 'beg_bal_cash_equ',
                                 'im_n_incr_cash_equ']
    _cashflow_semi_yearly_report_cols: List[str] = ['net_profit', 'finan_exp', 'c_recp_return_invest', 'c_paid_invest',
                                                    'oth_cash_recp_ral_fnc_act', 'incl_dvd_profit_paid_sc_ms',
                                                    'c_recp_cap_contrib', 'incl_cash_rec_saims', 'prov_depr_assets',
                                                    'depr_fa_coga_dpba', 'amort_intang_assets', 'lt_amort_deferred_exp',
                                                    'loss_disp_fiolta', 'loss_scr_fa', 'invest_loss',
                                                    'decr_def_inc_tax_assets', 'incr_def_inc_tax_liab',
                                                    'decr_inventories', 'decr_oper_payable', 'incr_oper_payable',
                                                    'im_net_cashflow_oper_act', 'end_bal_cash', 'beg_bal_cash',
                                                    'im_n_incr_cash_equ']
    """半年频公布的列"""

    def cashflow(self, symbol: str, report_type: int = 1, comp_type: Optional[int] = None,
                 start: Optional[Union[date, datetime]] = None,
                 end: Optional[Union[date, datetime]] = None,
                 cols: Optional[List[str]] = None, re_init: bool = False) -> pd.DataFrame:
        """see https://tushare.pro/document/2?doc_id=44"""
        # 数据接口相关的内容
        f = lambda ts_code, start_date, end_date=None: self.ts_pro.cashflow(ts_code=ts_code,
                                                                            report_type=report_type,
                                                                            comp_type=comp_type,
                                                                            start_date=start_date,
                                                                            end_date=end_date)
        sync_info = self.get_recommend_sync_info(f, symbol)

        sync_info.f_original_df_process = lambda x: convert_column_as_datetime(x, "ann_date", "date").drop(
            columns=["ts_code", "ann_date"]).set_index("date").astype(
            {k: "float64" for k in TuShareProData._cashflow_cols})

        return self._run_get_data_and_return(f"cashflow_{report_type}_{comp_type}_per_symbol", symbol, start, end,
                                             sync_info, cols, re_init)

    def cashflow_by_enddate(self, symbol: str, to_single_period_val: bool = False,
                          start: Optional[Union[date, datetime]] = None,
                          end: Optional[Union[date, datetime]] = None,
                          cols: Optional[List[str]] = None, re_init: bool = False) -> pd.DataFrame:
        """提供以enddate作为index 的现金流量表，提供参数 to_single_period_val 可以将输入转成单期值"""
        df = self.cashflow(symbol=symbol, report_type=1, re_init=re_init)
        df = TuShareProData._convert_enddate_index_and_accumulate_to_single_period(df,
                                                                                   list(set(TuShareProData._cashflow_cols) - set(TuShareProData._cashflow_semi_yearly_report_cols)) if to_single_period_val else [],
                                                                                   TuShareProData._cashflow_semi_yearly_report_cols if to_single_period_val else [])
        return filter_df_by_t_and_cols(df, start, end, cols)

    def _ts_func_start_end_wrapper(self, f: Callable, ts_code: str, start_date: str,
                                   end_date: str = "") -> pd.DataFrame:
        """基金净值数据等接口，不支持按照时间段的增量获取，这里只能做一层封装，以适应与 equity 相同的增量数据接口"""
        df = f(ts_code=ts_code)
        # 以 end_date 作为 日期的 PK 值
        if end_date:
            return df[(df["end_date"] >= start_date) & (df["end_date"] <= end_date)]
        else:
            return df[df["end_date"] >= start_date]

    def fund_nav(self, symbol: str, start: Optional[Union[date, datetime]] = None,
                 end: Optional[Union[date, datetime]] = None,
                 cols: Optional[List[str]] = None,
                 re_init: bool = False) -> pd.DataFrame:
        """
        see https://tushare.pro/document/2?doc_id=119
        """
        # 数据接口相关的内容

        sync_info = self.get_recommend_sync_info(partial(self._ts_func_start_end_wrapper, self.ts_pro.fund_nav), symbol)
        sync_info.f_original_df_process = lambda x: convert_column_as_datetime(x, "end_date", "date").drop(
            columns=["ts_code", "end_date"]).set_index("date")

        return self._run_get_data_and_return("fund_nav_per_symbol", symbol, start, end, sync_info, cols,
                                             re_init)

    def fund_portfolio(self, symbol: str, start: Optional[Union[date, datetime]] = None,
                       end: Optional[Union[date, datetime]] = None,
                       cols: Optional[List[str]] = None,
                       re_init: bool = False) -> pd.DataFrame:
        """
        see https://tushare.pro/document/2?doc_id=121
        """
        # 数据接口相关的内容
        # 因为这里用的参数名是 index_code ， 所以用一个 lambda 的函数调整参数名

        f = partial(self._ts_func_start_end_wrapper, self.ts_pro.fund_portfolio)
        ls_init_query_period = list()

        # 因为是一次性获取所有的数据，所以可以把这个 period 设置的非常大，目前设置为20年
        ls_init_query_period = get_month_periods(datetime(2000, 1, 1), 12*20)

        sync_info = self.get_recommend_sync_info(f, symbol, ls_init_query_period)
        sync_info.f_original_df_process = lambda x: convert_column_as_datetime(x, "end_date", "date").drop(
            columns=["ts_code", "end_date"]).set_index("date")

        return self._run_get_data_and_return("fund_portfolio_per_symbol", symbol, start, end, sync_info, cols,
                                             re_init)

    def fx_daily(self, ts_code: str, start: Optional[Union[date, datetime]] = None,
                 end: Optional[Union[date, datetime]] = None,
                 cols: Optional[List[str]] = None,
                 re_init: bool = False) -> pd.DataFrame:
        """
        see https://tushare.pro/document/2?doc_id=175
        外汇数据，经过时间调整，从 格林威治时间改为北京时间
        """
        # 固定 exchange参数，并且 state_date , end_date 都按照北京时间做修改
        # 注意：这里 start end 是 date 对象
        f = lambda ts_code, start_date=None, end_date=None: self.ts_pro.fx_daily(ts_code=ts_code,
                                                                                 start_date=(datetime.strptime(
                                                                                     start_date,
                                                                                     _DATE_STRFTIME) + timedelta(
                                                                                     days=1)).strftime(
                                                                                     _DATE_STRFTIME) if start_date else None,
                                                                                 end_date=(datetime.strptime(end_date,
                                                                                                             _DATE_STRFTIME) + timedelta(
                                                                                     days=1)).strftime(
                                                                                     _DATE_STRFTIME) if end_date else None,
                                                                                 exchange="FXCM")
        # 接口单次最大取1000条数据，这里按照四年计算
        sync_info = self.get_recommend_sync_info(f, ts_code,
                                                 init_query_paras=get_month_periods(datetime(2000, 1, 1), 36))
        # 拿到的数据减一天修改成北京时间
        sync_info.f_original_df_process = \
            lambda x: convert_column_as_datetime_minus_one_day(x, "trade_date", "date").drop(
                columns=["ts_code", "trade_date"]).set_index("date")

        return self._run_get_data_and_return("fx_daily_per_symbol", ts_code, start, end, sync_info, cols,
                                             re_init)

    def shibor(self, start: Optional[Union[date, datetime]] = None,
               end: Optional[Union[date, datetime]] = None,
               cols: Optional[List[str]] = None,
               re_init: bool = False) -> pd.DataFrame:
        # 用一个函数，改变第一个参数名为 ts_code
        f = lambda ts_code, start_date, end_date=None: self.ts_pro.shibor(start_date=start_date,
                                                                          end_date=end_date)
        sync_info = self.get_recommend_sync_info(f, "shibor",  # 这里的 symbol 是假的，只是为了接口能够统一
                                                 init_query_paras=get_month_periods(datetime(2000, 1, 1),
                                                                                    48))  # 单次最多2000条
        sync_info.f_original_df_process = lambda x: convert_column_as_datetime(x, "date", "date").set_index("date")

        return self._run_get_data_and_return("shibor", "shibor", start, end, sync_info, cols,
                                             re_init)

    def wz_index(self, start: Optional[Union[date, datetime]] = None,
               end: Optional[Union[date, datetime]] = None,
               cols: Optional[List[str]] = None,
               re_init: bool = False) -> pd.DataFrame:
        # 用一个函数，改变第一个参数名为 ts_code
        f = lambda ts_code, start_date, end_date=None: self.ts_pro.wz_index(start_date=start_date,
                                                                     end_date=end_date)
        sync_info = self.get_recommend_sync_info(f, "wz_index",  # 这里的 symbol 是假的，只是为了接口能够统一
                                                 init_query_paras=get_month_periods(datetime(2000, 1, 1),
                                                                                    48))  # 单次最多2000条
        sync_info.f_original_df_process = lambda x: convert_column_as_datetime(x, "date", "date").set_index("date")

        return self._run_get_data_and_return("wz_index", "wz_index", start, end, sync_info, cols,
                                             re_init)

    # endregion

    # region cs 类接口

    def chn_equity_business_daily_freq(self):
        """中国股市的business daily 的基准值"""

        # 用上证综指的数据作为 freq 的基准
        df = self.index_quotation_daily(symbol="000001.SH", cols=["close"])
        return df.index

    def _cs_query_period_to_absolute_date_list(self, start: Optional[Union[date, datetime]] = None,
                                               end: Optional[Union[date, datetime]] = None,
                                               look_period: Optional[int] = None, market="chn_equity") -> List[date]:
        import functools
        not_none_count = functools.reduce(lambda a, b: a + b,
                                          [1 if x is not None else 0 for x in [start, end, look_period]])
        assert not_none_count == 2, f"start:{start},end:{end},look_period:{look_period} only 2 of these can have value"
        dt_index = None
        if market == "chn_equity":
            dt_index = self.chn_equity_business_daily_freq()
        else:
            raise RuntimeError(f"Not supported market:{market}")

        if start:
            if isinstance(start, date):
                start = datetime.combine(start, datetime.min.time())
            dt_index = dt_index[dt_index >= start]
        if end:
            if isinstance(end, date):
                end = datetime.combine(end, datetime.max.time())
            dt_index = dt_index[dt_index <= end]
        ls_date = [t.date() for t in dt_index.to_list()]
        if look_period and look_period > 0:
            if start:
                ls_date = ls_date[:min(len(ls_date), look_period)]
            else:
                ls_date = ls_date[-1 * min(len(ls_date), look_period):]
        return ls_date

    def _get_recommend_cs_query_info(self, f_query, t_para_name: str,
                                     t_col_name: str = "trade_date") -> CSApiRemoteSyncToArcticInfo:
        """提供一个适合于大多数情况的 sync_info 的数据内容，各接口可根据具体情况，进行细项目的调整
        NOTE: 这里假定 init_query_paras 是升序排列的，逆序调用接口时，只要找到第一条不符合内容的信息，则不再向前追溯
        """
        query_info = CSApiRemoteSyncToArcticInfo()
        query_info.f_query_by_t = lambda t: f_query(**{t_para_name: t.strftime("%Y%m%d")})
        query_info.f_original_df_process = lambda x: convert_column_as_datetime(x, t_col_name, "date").drop(
            columns=[t_col_name]).rename(columns={"ts_code": "symbol"}).set_index(["date", "symbol"])
        return query_info

    def _cs_run_get_data_and_return(self, lib_name: str, api_name: str,
                                    query_info: CSApiRemoteSyncToArcticInfo,
                                    start: Optional[Union[date, datetime]],
                                    end: Optional[Union[date, datetime]],
                                    look_period: Optional[int],
                                    by_dates: Optional[List[date]] = None,
                                    market: str = "chn_equity",
                                    cols: Optional[List[str]] = None,
                                    re_init: bool = False) -> pd.DataFrame:
        full_lib_name = self.lib_prefix + lib_name

        if re_init:
            self.cs_clean_up_data(full_lib_name, api_name)

        if by_dates is None:
            ls_date = self._cs_query_period_to_absolute_date_list(start, end, look_period, market)
        else:
            ls_date = by_dates
        ls_all_df = [self._cs_maybe_read_from_local_cache(full_lib_name, api_name, t, query_info) for t in ls_date]
        df_all = None
        for df in ls_all_df:
            if df_all is None:
                df_all = df
            else:
                df_all = df_all.append(df)
        df_all = filter_df_by_t_and_cols(df_all, None, None, cols)
        return df_all

    def cs_equity_quotation_daily(self, start: Optional[Union[date, datetime]] = None,
                                  end: Optional[Union[date, datetime]] = None,
                                  look_period: Optional[int] = None,
                                  by_dates: Optional[List[date]] = None,
                                  cols: Optional[List[str]] = None, re_init: bool = False) -> pd.DataFrame:
        """ 日线行情 see https://tushare.pro/document/2?doc_id=27
        start , end , look_period 三个值不能同时为 Not None , 要求必须有两项为 非 None
        """
        # 数据接口相关的内容
        query_info = self._get_recommend_cs_query_info(self.pro_api.daily, "trade_date")
        return self._cs_run_get_data_and_return(TuShareProData.CS_LIB_NAME, self.cs_equity_quotation_daily.__name__,
                                                query_info, start, end, look_period, by_dates, cols=cols,
                                                re_init=re_init)

    def cs_equity_basic_daily(self, start: Optional[Union[date, datetime]] = None,
                              end: Optional[Union[date, datetime]] = None,
                              look_period: Optional[int] = None,
                              by_dates: Optional[List[date]] = None,
                              cols: Optional[List[str]] = None, re_init: bool = False) -> pd.DataFrame:
        """个股每日指标 see https://tushare.pro/document/2?doc_id=32 """
        # 数据接口相关的内容
        query_info = self._get_recommend_cs_query_info(self.pro_api.daily_basic, "trade_date")
        return self._cs_run_get_data_and_return(TuShareProData.CS_LIB_NAME, self.cs_equity_basic_daily.__name__,
                                                query_info, start, end, look_period, by_dates, cols=cols,
                                                re_init=re_init)

    def cs_equity_moneyflow(self, start: Optional[Union[date, datetime]] = None,
                            end: Optional[Union[date, datetime]] = None,
                            look_period: Optional[int] = None,
                            by_dates: Optional[List[date]] = None,
                            cols: Optional[List[str]] = None, re_init: bool = False) -> pd.DataFrame:
        """个股资金流向 see https://tushare.pro/document/2?doc_id=170"""
        # 数据接口相关的内容
        query_info = self._get_recommend_cs_query_info(self.pro_api.moneyflow, "trade_date")
        return self._cs_run_get_data_and_return(TuShareProData.CS_LIB_NAME, self.cs_equity_moneyflow.__name__,
                                                query_info, start, end, look_period, by_dates, cols=cols,
                                                re_init=re_init)

    def cs_equity_margin_detail(self, start: Optional[Union[date, datetime]] = None,
                                end: Optional[Union[date, datetime]] = None,
                                look_period: Optional[int] = None,
                                by_dates: Optional[List[date]] = None,
                                cols: Optional[List[str]] = None, re_init: bool = False) -> pd.DataFrame:
        """融资融券交易明细 see https://tushare.pro/document/2?doc_id=59"""
        # 数据接口相关的内容
        query_info = self._get_recommend_cs_query_info(self.pro_api.margin_detail, "trade_date")
        return self._cs_run_get_data_and_return(TuShareProData.CS_LIB_NAME, self.cs_equity_margin_detail.__name__,
                                                query_info, start, end, look_period, by_dates, cols=cols,
                                                re_init=re_init)

    def cs_equity_block_trade(self, start: Optional[Union[date, datetime]] = None,
                              end: Optional[Union[date, datetime]] = None,
                              look_period: Optional[int] = None,
                              by_dates: Optional[List[date]] = None,
                              cols: Optional[List[str]] = None, re_init: bool = False) -> pd.DataFrame:
        """大宗交易 see https://tushare.pro/document/2?doc_id=161 """
        # 数据接口相关的内容
        query_info = self._get_recommend_cs_query_info(self.pro_api.block_trade, "trade_date")
        return self._cs_run_get_data_and_return(TuShareProData.CS_LIB_NAME, self.cs_equity_block_trade.__name__,
                                                query_info, start, end, look_period, by_dates, cols=cols,
                                                re_init=re_init)

    def cs_equity_top_inst(self, start: Optional[Union[date, datetime]] = None,
                           end: Optional[Union[date, datetime]] = None,
                           look_period: Optional[int] = None,
                           by_dates: Optional[List[date]] = None,
                           cols: Optional[List[str]] = None, re_init: bool = False) -> pd.DataFrame:
        """ 龙虎榜机构成交明细 see https://tushare.pro/document/2?doc_id=107 """
        # 数据接口相关的内容
        query_info = self._get_recommend_cs_query_info(self.pro_api.top_inst, "trade_date")
        return self._cs_run_get_data_and_return(TuShareProData.CS_LIB_NAME, self.cs_equity_top_inst.__name__,
                                                query_info, start, end, look_period, by_dates, cols=cols,
                                                re_init=re_init)

    def cs_equity_adj_factor(self, start: Optional[Union[date, datetime]] = None,
                             end: Optional[Union[date, datetime]] = None,
                             look_period: Optional[int] = None,
                             by_dates: Optional[List[date]] = None,
                             cols: Optional[List[str]] = None, re_init: bool = False) -> pd.DataFrame:
        """ 复权因子 see https://tushare.pro/document/2?doc_id=28 """
        # 数据接口相关的内容
        query_info = self._get_recommend_cs_query_info(self.pro_api.adj_factor, "trade_date")
        return self._cs_run_get_data_and_return(TuShareProData.CS_LIB_NAME, self.cs_equity_adj_factor.__name__,
                                                query_info, start, end, look_period, by_dates, cols=cols,
                                                re_init=re_init)

    def cs_equity_backward_adjust_daily(self, start: Optional[Union[date, datetime]] = None,
                                        end: Optional[Union[date, datetime]] = None,
                                        look_period: Optional[int] = None,
                                        by_dates: Optional[List[date]] = None,
                                        cols: Optional[List[str]] = None, re_init: bool = False) -> pd.DataFrame:
        """cs 的后复权市场数据，这里为了方便调用，进行 derived 计算"""
        df_mkt_data = self.cs_equity_quotation_daily(start, end, look_period,by_dates, None, re_init)
        df_adj = self.cs_equity_adj_factor(start, end, look_period, by_dates, None, re_init)
        df_rlt = pd.DataFrame({"open": df_mkt_data["open"] * df_adj["adj_factor"],
                               "high": df_mkt_data["high"] * df_adj["adj_factor"],
                               "low": df_mkt_data["low"] * df_adj["adj_factor"],
                               "close": df_mkt_data["close"] * df_adj["adj_factor"]
                               })
        return df_rlt

    def cs_fund_nav(self, start: Optional[Union[date, datetime]] = None,
                    end: Optional[Union[date, datetime]] = None,
                    look_period: Optional[int] = None,
                    by_dates: Optional[List[date]] = None,
                    cols: Optional[List[str]] = None, re_init: bool = False) -> pd.DataFrame:
        query_info = self._get_recommend_cs_query_info(self.pro_api.fund_nav, "end_date", t_col_name="end_date")
        return self._cs_run_get_data_and_return(TuShareProData.CS_LIB_NAME, self.cs_fund_nav.__name__,
                                                query_info, start, end, look_period, by_dates, cols=cols,
                                                re_init=re_init)
    # endregion

    # region derived calculation 接口

    def period_index_member(self, index_code: str, start: Optional[Union[date, datetime]] = None,
                            end: Optional[Union[date, datetime]] = None,
                            resample_freq: str = "BM",
                            cols: Optional[List[str]] = None,
                            re_init: bool = False) -> pd.DataFrame:
        """
        得到一个时间段范围内的行业的成分股票数据，这是 tushare 接口计算的衍生数据，为了使得其入参与输出行为与 index_membership 一致
        """
        # 将历史的和当期的 index member 数据进行 union
        df_history = self.index_member(index_code=index_code, is_new="N", cols=["in_date", "con_code", "out_date"],
                                       re_init=re_init)
        df_history = convert_column_as_datetime(df_history, "in_date", "date").drop(columns=["in_date"])
        df_history = convert_column_as_datetime(df_history, "out_date", "t_out_date").drop(columns=["out_date"])
        df_history.rename(columns={"con_code": "symbol"}, inplace=True)

        df_new = self.index_member(index_code=index_code, is_new="Y", cols=["in_date", "con_code", "out_date"],
                                   re_init=re_init)
        df_new = convert_column_as_datetime(df_new, "in_date", "date").drop(columns=["in_date"])
        df_new.rename(columns={"out_date": "t_out_date", "con_code": "symbol"}, inplace=True)
        # out_date 为 None 必须标记成 today ， 否则在矩阵转换的时候，会额外补充出 None 来
        df_new = df_new.fillna(value=datetime.today().date())
        df_all = pd.concat([df_new, df_history])

        # 把 symbol 变成 column ,这样可以 resample 并对齐时间
        min_t = df_all["date"].min()
        df_all = df_all.pivot(values="t_out_date", index="date", columns="symbol")

        df_time_align = self.index_quotation_daily(symbol="000001.SH", cols=["close"])
        df_time_align = df_time_align[df_time_align.index >= min_t]
        # df_time_align = filter_df_by_t_and_cols(df_time_align, start, end, None)
        df_all = df_time_align.join(df_all)
        df_all = df_all.fillna(method="ffill")
        df_all = df_all[df_all.columns[1:]]

        # NOTE:根据 t 过滤需要在 join 完成之后，否则 fillna 会没有合适数据
        df_all = filter_df_by_t_and_cols(df_all, start, end, None)
        # 数据太早，没有可以返回的内容
        if df_all.shape[0] == 0:
            return None

        # resample ，以去掉太多的数据列内容
        df_all = df_all.asfreq(freq=resample_freq)

        # 将 symbol 变为一列，并删除 out_date 大于 in_date 的记录
        df_all = pd.DataFrame(df_all.stack(level=-1)).reset_index()
        df_all.rename(columns={df_all.columns[1]: "symbol", df_all.columns[2]: "out_date"}, inplace=True)
        df_all = df_all[df_all["date"] <= df_all["out_date"]]
        df_all = df_all.set_index("date")

        df_rlt = df_all[["symbol"]].sort_index(axis=0, ascending=True)
        if cols:
            df_rlt = df_rlt[cols]
        return df_rlt

    # endregion

    # region 非时间序列类，一般是一些名称代码表类的数据
    NON_TS_LIBNAME = "non_ts_version"

    def stock_basic(self, is_hs: Optional[str] = None, list_status: str = "L", exchange: str = "SSE",
                    cols: Optional[List[str]] = None, re_init: bool = False) -> pd.DataFrame:
        """https://tushare.pro/document/2?doc_id=25"""
        sync_info = self.get_non_ts_sync_info(self.ts_pro.stock_basic, is_hs=is_hs, list_status=list_status,
                                              exchange=exchange)
        obj_uuid = "stock_basic_" + md5_str(f"{is_hs}-{list_status}-{exchange}")
        return self._run_non_ts_get_data_and_return(self.NON_TS_LIBNAME, obj_uuid, sync_info, cols, re_init)

    def index_classify(self, index_code: Optional[str] = None, level: Optional[str] = None, src: Optional[str] = None,
                       cols: Optional[List[str]] = None, re_init: bool = False) -> pd.DataFrame:
        """ https://tushare.pro/document/2?doc_id=181 """
        sync_info = self.get_non_ts_sync_info(self.ts_pro.index_classify, index_code=index_code, level=level,
                                              src=src)
        obj_uuid = "index_classify_" + md5_str(f"{index_code}-{level}-{src}")
        return self._run_non_ts_get_data_and_return(self.NON_TS_LIBNAME, obj_uuid, sync_info, cols, re_init)

    def index_basic(self, market: str, publisher: Optional[str] = None, category: Optional[str] = None,
                    cols: Optional[List[str]] = None, re_init: bool = False) -> pd.DataFrame:
        """ https://tushare.pro/document/2?doc_id=94 指数基本信息"""
        sync_info = self.get_non_ts_sync_info(self.ts_pro.index_basic, market=market, publisher=publisher,
                                              category=category)
        sync_info.f_check_arctic_need_update = arctic_non_ts_data_expired_month_end  # 基于月度的超时策略
        obj_uuid = "index_basic_" + md5_str(f"{market}-{publisher}-{category}")
        return self._run_non_ts_get_data_and_return(self.NON_TS_LIBNAME, obj_uuid, sync_info, cols, re_init)

    def index_member(self, index_code: Optional[str] = None, ts_code: Optional[str] = None,
                     is_new: Optional[str] = None, cols: Optional[List[str]] = None,
                     re_init: bool = False) -> pd.DataFrame:
        """https://tushare.pro/document/2?doc_id=182
            申万行业成分
            Note:该接口不提供根据时间进行增量的请求，所以使用 version store 的方式进行操作
        """
        sync_info = self.get_non_ts_sync_info(self.ts_pro.index_member, index_code=index_code, ts_code=ts_code,
                                              is_new=is_new)
        sync_info.f_check_arctic_need_update = arctic_non_ts_data_expired_month_end  # 基于月度的超时策略
        obj_uuid = "index_member_" + md5_str(f"{index_code}-{ts_code}-{is_new}")
        return self._run_non_ts_get_data_and_return(self.NON_TS_LIBNAME, obj_uuid, sync_info, cols, re_init)

    def fund_basic(self, market: str = "E",
                   cols: Optional[List[str]] = None, re_init: bool = False) -> pd.DataFrame:
        """
        获取公募基金数据列表，包括场内和场外基金, https://tushare.pro/document/2?doc_id=19
        Parameters
        ----------
        market
            交易市场: E场内 O场外（默认E）
        cols
        re_init

        Returns
        -------

        """
        """"""
        sync_info = self.get_non_ts_sync_info(self.ts_pro.fund_basic, market=market)
        obj_uuid = "fund_basic_" + md5_str(f"{market}")
        return self._run_non_ts_get_data_and_return(self.NON_TS_LIBNAME, obj_uuid, sync_info, cols, re_init)

    def concept(self, src: str = "ts", cols: Optional[List[str]] = None, re_init: bool = False) -> pd.DataFrame:
        """ concept概念列表  see https://tushare.pro/document/2?doc_id=125 """
        sync_info = self.get_non_ts_sync_info(self.ts_pro.concept, src=src)
        obj_uuid = "stock_concept_" + md5_str(f"{src}")
        return self._run_non_ts_get_data_and_return(self.NON_TS_LIBNAME, obj_uuid, sync_info, cols, re_init)

    def concept_detail(self, concept_id: str, cols: Optional[List[str]] = None, re_init: bool = False) -> pd.DataFrame:
        """ see https://tushare.pro/document/2?doc_id=126 """

        sync_info = self.get_non_ts_sync_info(self.ts_pro.concept_detail, id=concept_id)

        obj_uuid = "concept_detail_" + md5_str(f"{concept_id}")
        return self._run_non_ts_get_data_and_return(self.NON_TS_LIBNAME, obj_uuid, sync_info, cols, re_init)


    # endregion

    # region derived ts 读取接口

    def read_derived_ts(self, lib_name: str, symbol: str, start: Optional[Union[date, datetime]] = None,
                        end: Optional[Union[date, datetime]] = None,
                        cols: Optional[List[str]] = None,
                        re_init: bool = False) -> pd.DataFrame:
        if re_init:
            self.clean_up_symbol_data(lib_name, symbol)
        df = self._read_ts_without_vendor_source(lib_name, symbol)
        return filter_df_by_t_and_cols(df, start, end, cols)

    # 一些维护的 derived_ts lib name
    DERIVED_TS_EQUITY_SW_INDUSTRY_L1: str = "sw_industry_l1"
    DERIVED_TS_EQUITY_SW_INDUSTRY_L2: str = "sw_industry_l2"
    DERIVED_TS_EQUITY_SW_INDUSTRY_L3: str = "sw_industry_l3"
    DERIVED_TS_INDUSTRY_INDEX: str = "industry_index"
    """各种行业数据的行业指数内容"""
    # endregion


# deleted since 2020.01.08
# # ---- 以下是一些直接调用 tushare 的 api 封装，没有两级 cache -----
#
# def get_category_symbols(tushare: TuShareProData, ls_category: List[str]) -> Tuple[
#     List[Tuple[str, str]], Set[str]]:
#     """
#
#     Parameters
#     ----------
#     tushare
#     ls_category
#
#     Returns
#     -------
#     ls_category
#
#     symbols
#
#     """
#     symbols_with_category = list()
#     for category in ls_category:
#         df = tushare.concept_detail(category)
#         ls_category_symbols = [(df.iloc[i]["ts_code"], category) for i in range(len(df))]
#         symbols_with_category += ls_category_symbols
#     all_symbols_with_category = set([symbol for symbol, category in symbols_with_category])
#     return symbols_with_category, all_symbols_with_category
#
#
# def get_all_market_symbols(tushare: TuShareProData) -> Set[str]:
#     sh_stocks = tushare.stock_basic(exchange="SSE")
#     sz_stocks = tushare.stock_basic(exchange="SZSE")
#     all_stock_symbols = set(
#         [sh_stocks.iloc[i]["ts_code"] for i in range(len(sh_stocks))] + [sz_stocks.iloc[i]["ts_code"] for i in
#                                                                          range(len(sz_stocks))])
#     return all_stock_symbols
#
#
# def get_all_symbol_basic(tushare: TuShareProData) -> Dict[str, Dict]:
#     # todo : 这个接口增加 arctic 的 cache 能力
#     sh_stocks = tushare.stock_basic(exchange="SSE")
#     sz_stocks = tushare.stock_basic(exchange="SZSE")
#     dict_all_symbol = sh_stocks.set_index("ts_code").to_dict("index")
#     dict_all_symbol.update(sz_stocks.set_index("ts_code").to_dict("index"))
#     return dict_all_symbol
