# -*- coding: UTF-8 -*-
from datetime import date, datetime
from typing import NamedTuple, Callable, Union, List, Optional

import pandas as pd
from dataclasses import dataclass
from datetime import date, datetime

SymbolPeriodTSCallable = Callable[[str, Union[date, datetime], Union[date, datetime], List[str]], pd.DataFrame]
""" 取某一个Symbol的一段时间跨度数据的 function ， 参数含义(symbol,start_t,end_t) """


@dataclass
class TSCallableData:
    f_get_ts_data: SymbolPeriodTSCallable
    """
        取数据的 function
        Examples
        --------
            TuShareProData().equity_quotation_daily
    """

    column_prefix_format: str = "{symbol}_"
    """
    """


@dataclass
class MultiTSData:

    def _loop_get_data_and_join(self, symbol: str, ls_get_data_objs: List[SymbolPeriodTSCallable],
                                start_t: Union[datetime, date], end_t: Union[datetime, date],
                                col_rename_format: str = "{symbol}_") -> pd.DataFrame:
        """

        Parameters
        ----------
        symbol
        ls_get_data_objs
        start_t
        end_t
        col_rename_format : -
            多个x将会join到一张表，为了避免列名的冲突，可以约定Column Name 的 prefix
            支持 {symbol} 的表达，将替换成具体的 symbol 内容
            Examples
            --------
                "{symbol}_" 会替换成 "600000.SH_"

        Returns
        -------

        """
        df_curr = None
        for call_obj in ls_get_data_objs:
            df = call_obj(symbol, start_t, end_t)
            if df is None or df.empty:
                continue
            if col_rename_format:
                rename_cols = {col: col_rename_format.format(symbol=symbol) + col for col in df.columns}
                df.rename(columns=rename_cols, inplace=True)
            # 多个 相同 symbol 的 x table join 到一起
            if df_curr is None:
                df_curr = df
            else:
                df_curr = df_curr.join(df)
        return df_curr


NONE_CATEGORY_STR = "NONE"