# -*- coding: utf-8 -*-

"""
适用于 nni 的一些 tfv2 callbacks
"""
import asyncio
import logging
from typing import Mapping, Any

import tensorflow as tf

from gs_research_workflow.auto_ml.nni.hpo.arctic_metrics_reporter import TrailMetricsArcticReporter

logger = logging.getLogger(__name__)


class ReportIntermediates(tf.keras.callbacks.Callback):
    """
    报告运行中间过程的 metrics ，支持两种方式：
        1) 直接调用 nni 的 report_intermediate_result 接口，适用于  local machine 或者 kubeflow 进行的 trail
        2) 将 intermediate result push 到 kafka (colab side) , 然后在 gs container 里 consume 该 msg 后推送到 nni
    """

    def __init__(self, reporter: TrailMetricsArcticReporter):
        self._reporter: TrailMetricsArcticReporter = reporter

    # ---- [laigen 2020.02.29] colab train 不再通过 kafka 进行，这里先去掉。  ----
    # async def _report_intermediate_result(self, metrics: Mapping[str, Any]):
    #     self._env.intermediate_metrics.VALUE = metrics
    #     self._env.commit_state_var_changes()
    # ----

    def on_epoch_end(self, epoch, logs=None):
        """Reports intermediate metrics to NNI framework via Env.StateVariable"""
        logger.info(f"on_epoch_end:{logs}")
        self._reporter.report_intermediate_result(epoch,logs)
        # ---- [laigen 2020.02.29] colab train 不再通过 kafka 进行，这里先去掉。  ----
        # asyncio.ensure_future(self._report_intermediate_result(logs))
        # ----
