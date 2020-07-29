# -*- coding: UTF-8 -*-

"""
使用 Arctic 来存储 metrics 数据，具体的存储结构为：
    > 所有的 nni experiment 用同一个 chunk library（library 过多会造成 mongo collection 较多的问题） ， chunk_size 为 "D"
    > 每个 trial uuid 是一个 symbol (symbol 多一些问题并不大， 方便以 trial 为最小颗粒的数据更新)
    > 每个 epoch 是一天的数据 (intermediate metrics)， 固定从 2000-01-01 的 days 数表示第几个 epoch
        > 每个 metrics 数据都会变成一列数据
    > final result 固定记录在 2010-01-01 这一天
    > experiment name 和 experiment uuid 作为 meta 保存
"""
from datetime import datetime, timedelta
from typing import Mapping, Any, Optional, Tuple, Dict, List

from arctic import Arctic, CHUNK_STORE
from gs_framework.gs_resource import set_http_proxy

from gs_research_workflow.external_data.db_server_resource.mongo import get_google_mongo_conn_str
import pandas as pd


class TrailMetricsArcticReporter:
    NNI_EXPERIMENT_LIB = "NNI_EXPERIMENT_METRICS"
    COL_FINAL_RESULT = "final_result"
    INTERMEDIATE_START_DATE = datetime(2000, 1, 1)
    FINAL_METRICS_DATE = datetime(2010, 1, 1)

    def __init__(self, experiment_name: str, experiment_uuid: str, trial_uuid: str):
        set_http_proxy()
        self.experiment_name = experiment_name
        self.experiment_uuid = experiment_uuid
        self.trial_uuid = trial_uuid
        # 不论程序跑在哪里，都使用 google 上的 arctic 进行沟通
        self.arctic_store = Arctic(get_google_mongo_conn_str(), connectTimeoutMS=600 * 1000,
                                   serverSelectionTimeoutMS=600 * 1000)
        if not self.arctic_store.library_exists(TrailMetricsArcticReporter.NNI_EXPERIMENT_LIB):
            self.arctic_store.initialize_library(TrailMetricsArcticReporter.NNI_EXPERIMENT_LIB, lib_type=CHUNK_STORE)
        self.arctic_lib = self.arctic_store[TrailMetricsArcticReporter.NNI_EXPERIMENT_LIB]

        self._curr_write_epoch_id: int = 0

    def _write_arctic(self, df: pd.DataFrame):
        if not self.arctic_lib.has_symbol(self.trial_uuid):
            self.arctic_lib.write(self.trial_uuid, df, chunk_size="D", upsert=True)
            self.arctic_lib.write_metadata(self.trial_uuid, {"experiment_name": self.experiment_name,
                                                             "experiment_uuid": self.experiment_uuid})
        else:
            self.arctic_lib.update(self.trial_uuid, df, upsert=True)

    def report_intermediate_result(self, epoch: int, metrics: Mapping[str, Any]):
        df = pd.DataFrame(data=metrics, index=pd.DatetimeIndex(
            [TrailMetricsArcticReporter.INTERMEDIATE_START_DATE + timedelta(days=epoch)], name="date"))
        self._write_arctic(df)

    def report_final_result(self, val: float):
        df = pd.DataFrame(data={TrailMetricsArcticReporter.COL_FINAL_RESULT: val},
                          index=pd.DatetimeIndex([TrailMetricsArcticReporter.FINAL_METRICS_DATE], name="date"))
        self._write_arctic(df)

    def query_metrics(self, latest_epoch: Optional[int]) -> Tuple[
        Optional[int], Optional[List[Dict[str, float]]], Optional[float]]:
        """
        查询 metrics 内容

        Parameters
        ----------
        latest_epoch : int
            从 epoch（不包含） 开始增量查询，不填表示从第一期开始查询

        Returns
        -------
            latest epoch : optional[int]
                最新一个 epoch

            intermediate metrics : Optional[List[Dict[str,float]]]
                从 input latest_epoch 之后的 intermediate metrics 内容

            final result : Optional[float]
                如果已经得到 final result 则提供该数值
        """
        if not self.arctic_lib.has_symbol(self.trial_uuid):
            return None, None, None
        start_t = TrailMetricsArcticReporter.INTERMEDIATE_START_DATE
        if latest_epoch is not None:
            start_t = TrailMetricsArcticReporter.INTERMEDIATE_START_DATE + timedelta(days=latest_epoch + 1)
        end_t = TrailMetricsArcticReporter.FINAL_METRICS_DATE
        df = self.arctic_lib.read(self.trial_uuid, chunk_range=pd.date_range(start_t, end_t), filter_data=True)
        if df is None or df.shape[0] == 0:
            return latest_epoch, None, None
        metrics_cols = df.columns.to_list()
        if TrailMetricsArcticReporter.COL_FINAL_RESULT in metrics_cols:
            metrics_cols.remove(TrailMetricsArcticReporter.COL_FINAL_RESULT)
        final_result = None
        ls_intermediate_metrics = []
        rlt_latest_epoch = latest_epoch
        for row_index, row in df.iterrows():
            if row_index < TrailMetricsArcticReporter.FINAL_METRICS_DATE:
                curr_epoch_id = (row_index - TrailMetricsArcticReporter.INTERMEDIATE_START_DATE).days
                if rlt_latest_epoch is None or curr_epoch_id > rlt_latest_epoch:
                    rlt_latest_epoch = curr_epoch_id
                ls_intermediate_metrics.append({k: row[k] for k in metrics_cols})
            elif row_index == TrailMetricsArcticReporter.FINAL_METRICS_DATE:
                final_result = row[TrailMetricsArcticReporter.COL_FINAL_RESULT]
            else:
                raise RuntimeError(f"invalid date {row_index} in trail {self.trial_uuid} metrics")
        return rlt_latest_epoch, ls_intermediate_metrics if len(ls_intermediate_metrics) > 0 else None, final_result


if __name__ == "__main__":
    import random
    reporter = TrailMetricsArcticReporter("EquityDailyReturnCSBert_ChnV1", "dN5PBxRz", "mOB53")
    # for i in range(10):
    #     reporter.report_intermediate_result(i, {"mae": random.random(), "mse": random.random()})
    # reporter.report_final_result(random.random())
    rlt = reporter.query_metrics(None)
    print(rlt)
