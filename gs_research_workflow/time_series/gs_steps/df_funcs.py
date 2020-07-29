# -*- coding: UTF-8 -*-
"""
ts workflow 中用到的一些dataframe 处理工具类的函数
"""

import pandas as pd
from typing import Dict


def dfs_concat(dfs: Dict[str, pd.DataFrame], key_col_name: str = "category") -> pd.DataFrame:
    """
    将 Category 类型的 dataframe dictionary 合并成一个 dataframe 对象，第一列为 key 的值

    Parameters
    ----------
    dfs
    key_col_name :
        新生成的key 这一列的名称
    """
    df = pd.concat(dfs, keys=sorted(list(dfs.keys()))).reset_index()
    df.rename(columns={df.columns[0]: key_col_name},inplace=True)
    return df
