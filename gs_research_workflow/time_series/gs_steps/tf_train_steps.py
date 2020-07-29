# -*- coding: UTF-8 -*-
"""
一个典型的 tf training 的 workflow step 对象

定义 Training Workflow 相关的内容

适用于 数据源头是一个 tf.data.Dataset 的对象
    Step 1: 通过 Hyper Parameter 生成 Dataset 对象 (两个数据，分别为 TrainSet 和 ValidationSet)
    Step 2: Dataset Pipline 的函数 (TrainSet 和 ValidationSet 的 Pipline 函数可能不同)
                    Batch 为这一步的参数。
            这一步骤不太容易做成 Scalar 的 Dict ， 是 Function + input 的形式
    Step 3: 创建 Model By Hyper Parameters
        可以拿到上一步的两个对象，也作为 hyper parameter 的一部分
    Step 4: Model Compile , 确定 Loss 和 Optimizer 和 Metrics 等 Hyper Parameters
    Step 5: Fit 主要确定 Epoch , Step , Validation Step 等 Hyper Parameters
"""
import asyncio
import logging
import os
from typing import Callable, Mapping, Any, Optional, Type

import tensorflow as tf
from dataclasses import dataclass

from gs_research_workflow.auto_ml.nni.hpo.arctic_metrics_reporter import TrailMetricsArcticReporter
from gs_research_workflow.auto_ml.nni.tfv2.callbacks import ReportIntermediates
from gs_research_workflow.common.serialization_utilities import cls_to_str, save_mapping_to_file_or_stream, str_to_cls
from gs_research_workflow.core.gs_step import GSStep, create_step_by_dict
from gs_research_workflow.core.gs_step_mapping import GlobalGSStepMapping
from gs_research_workflow.time_series.gs_steps.data_preprocess_steps import TrainValSpiltStep
from gs_research_workflow.time_series.gs_steps.func_steps import FuncStrStep
from gs_research_workflow.time_series.gs_steps.model_steps import TFModelStep, CompileStep, FitStep, \
    ModelCheckPointStep, TensorBoardStep, EarlyStoppingStep, ModelPredictionMixin
from gs_research_workflow.time_series.gs_steps.tf_dataset_step import TSCategoryDatasetPreparingStep
from gs_research_workflow.time_series.gs_steps.tf_dataset_steps.equity_daily_data_mask_ds import EquityPoolTSDatasetStep
from gs_research_workflow.time_series.gs_steps.tf_ds_for_financial_statement import \
    FinancialStatementCSMaskedTFDatasetStep
from gs_research_workflow.time_series.gs_steps.ts_data_steps import SymbolTSStep
from gs_research_workflow.time_series.gs_steps.ts_portfolio_ds_steps import TSPortfolioWeightTFDSStep
from gs_research_workflow.time_series.models.gs_loss_functions import process_compile_loss_kwargs

logger = logging.getLogger(__name__)

CallableDSPipline = Callable[[tf.data.Dataset], tf.data.Dataset]


class WithModelMixIn:
    """有 Model 对象的 MixIn,提供一些基础的 api 服务
        MixIn 假定有 model_cls,  model_init_hp , compile_kwargs 这几个成员变量，这些成员变量可以不是 __init__ 的参数
        
    """

    def load_model_with_compiled(self, model_full_cfg_file_path: str) -> tf.keras.Model:
        with open(model_full_cfg_file_path, "r") as f:
            architecture_obj = json.load(f)
        model_cls_str, model_init_hp, compile_kwargs = architecture_obj
        model_cls = str_to_cls(model_cls_str)
        model = model_cls(create_step_by_dict(model_init_hp))
        model.compile(**process_compile_loss_kwargs(compile_kwargs))
        return model

    def save_compiled_model_args(self, model_full_cfg_file_path: str):
        # NOTE:compile_kwargs 里的 metrics 如果是 Metrics Class 的话，无法序列化成 json 和 pickles
        #  所以这里先暂时假定 compile_kwargs 里面的 metrics 都是 string 类型
        obj_to_dump = (cls_to_str(self.model_cls), self.model_init_hp.get_init_value_dict(True), self.compile_kwargs)
        with open(model_full_cfg_file_path, "w") as f:
            json.dump(obj_to_dump, f)


@dataclass
class TFTrainStep(ModelPredictionMixin, GSStep):
    """一种用 tensorflow 进行 training 的典型 workflow"""
    train_ds: tf.data.Dataset
    """NOTE: ds_pip 在该 step 之外进行"""
    val_ds: tf.data.Dataset
    test_ds: tf.data.Dataset

    model_cls: Type
    model_init_hp: GSStep

    compile_kwargs: Mapping[str, Any]

    fit_kwargs: Mapping[str, Any]

    checkpoint_kwargs: Mapping[str, Any]

    tensor_board_kwargs: Mapping[str, Any]

    early_stopping_kwargs: Optional[Mapping[str, Any]] = None

    def __post_init__(self):
        self._have_gpu = False
        self._tf_cb_report_metrics: Optional[ReportIntermediates] = None
        # ---- [laigen 2020.02.29] colab train 不再通过 kafka 进行，这里先去掉。  ----
        # self._metrics_env: Optional[TrialColabSideEnv] = None
        # ----

        gpus = tf.config.experimental.list_physical_devices('GPU')
        if gpus:
            try:
                tf.config.experimental.set_visible_devices(gpus[0], 'GPU')
                self._have_gpu = True
                logical_gpus = tf.config.experimental.list_logical_devices('GPU')
                logger.debug(f"{len(gpus)} Physical GPU , {len(logical_gpus)} Logical GPUs")
            except RuntimeError as e:
                # Virtual devices must be set before GPUs have been initialized
                logger.error(e)
        logger.debug(f"GPU resource is {self._have_gpu}")

    @property
    def model_check_point_path(self) -> str:
        return self.model_cls.model_checkpoint_path(self.model_init_hp)

    @property
    def tensorboard_path(self) -> str:
        return self.model_cls.model_tensorboard_path(self.model_init_hp)

    # ---- [laigen 2020.02.29] colab train 不再通过 kafka 进行，这里先去掉。  ----
    # async def prepare_metrics_callback(self, trial_hash_gid: str, one_trial_spec_val: str, tp: faust.types.TP):
    #     self._metrics_env = TrialColabSideEnv(trial_hash_gid, one_trial_spec_val)
    #     self._metrics_env.bind(topic_define=tp)
    #     await self._metrics_env.start()
    #     self._tf_cb_report_metrics = ReportIntermediates(self._metrics_env)
    # -------

    # 因为 colab 连 kafka 时间稍长一些，就会中断。所以这里改为通过 google mongo 的方式，交互 model 的 metrics 数据
    def prepare_metrics_recorder(self, experiment_name: str, experiment_id: str, trial_id: str):
        self.metrics_reporter = TrailMetricsArcticReporter(experiment_name, experiment_id, trial_id)
        self._tf_cb_report_metrics = ReportIntermediates(self.metrics_reporter)

    async def stop_env(self):
        # ---- [laigen 2020.02.29] colab train 不再通过 kafka 进行，这里先去掉。  ----
        # await self._metrics_env.stop()
        # ----
        pass

    async def report_final_result(self, val: float):
        self.metrics_reporter.report_final_result(val)
        # ---- [laigen 2020.02.29] colab train 不再通过 kafka 进行，这里先去掉。  ----
        # self._metrics_env.final_metrics.VALUE = val
        # self._metrics_env.commit_state_var_changes()
        # ----

    # ---- [laigen 2020.02.29] colab train 不再通过 kafka 进行，这里先去掉。  ----
    # def set_metrics_callback(self, trial_hash_gid: str, one_trial_spec_val: str, tp: faust.types.TP):
    #     """提供给 colab cell 中调用的，提交中间的部分结果内容，必须在 fit 之前调用"""
    #     loop = asyncio.get_event_loop()
    #     loop.run_until_complete(self.prepare_metrics_callback(trial_hash_gid, one_trial_spec_val, tp))
    # ----

    async def fit(self):
        checkpoint_path = self.model_cls.model_checkpoint_path(self.model_init_hp)
        logger.debug(f"Model checkpoint path '{checkpoint_path}'")
        # 保存一份 model(和workflow) 的 hyper parameter 到 model 所在的目录，以提供 human 查看

        # save model architecture
        # NOTE:compile_kwargs 里的 metrics 如果是 Metrics Class 的话，无法序列化成 json 和 pickles ， 所以这里先暂时假定 compile_kwargs 里面的 metrics 都是 string 类型
        self.model_cls.save_model_full_cfg(checkpoint_path, self.model_init_hp, self.compile_kwargs)

        # Create a callback that saves the model's weights

        # checkpoint 的 其他参数，是 step 的 field 进行控制，而 checkpoint_path 则由 Platform 进行统一的管理
        # NOTE:暂时先去掉 save check point 的 callback
        # cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=self.model_cls.model_checkpoint_file(checkpoint_path),
        #                                                  **self.checkpoint_kwargs)

        # tensorboard_callback = tf.keras.callbacks.TensorBoard(
        #     log_dir=self.model_cls.model_tensorboard_path(self.model_init_hp), **self.tensor_board_kwargs)

        # tensorboard 的 callback 也会发生错误，暂时先去掉 tensorboard 的 callback 内容
        # fit_callback = [cp_callback, tensorboard_callback] # NOTE:暂时先去掉 save check point 的 callback
        # fit_callback = [tensorboard_callback]
        fit_callback = []
        if self.early_stopping_kwargs is not None:
            fit_callback.append(tf.keras.callbacks.EarlyStopping(**self.early_stopping_kwargs))

        if self._tf_cb_report_metrics:
            fit_callback.append(self._tf_cb_report_metrics)

        if self._have_gpu:
            strategy = tf.distribute.MirroredStrategy()
            with strategy.scope():
                logger.info("Training with GPU !!!")
                _model = self.model_cls.from_pre_saved(checkpoint_path)
                if _model is None:
                    logger.info(f"Model {self.model_cls.__name__} train from scratch.")
                    _model = self.model_cls.from_init_hp_compile(self.model_init_hp, self.compile_kwargs)
                else:
                    logger.info(f"Model {self.model_cls.__name__} loaded from pre saved weights.")

                _model.fit(self.train_ds, validation_data=self.val_ds, callbacks=fit_callback,
                           **self.fit_kwargs)
                _model.save_model_and_weights(checkpoint_path)
        else:
            _model = self.model_cls.from_pre_saved(checkpoint_path)
            if _model is None:
                logger.info(f"Model {self.model_cls.__name__} train from scratch.")
                _model = self.model_cls.from_init_hp_compile(self.model_init_hp, self.compile_kwargs)
            else:
                logger.info(f"Model {self.model_cls.__name__} loaded from pre saved weights.")
            _model.fit(self.train_ds, validation_data=self.val_ds, callbacks=fit_callback,
                       **self.fit_kwargs)
            _model.save_model_and_weights(checkpoint_path)
        await asyncio.sleep(60.)

    async def eval_model(self):
        # 这里因为可能是在 strategy.scope() 中 compile 的 model，是没有 evaluate 的方法，所以重新 load 一次整个 model 进行 eval
        # TODO: 这个改成从 ModelWithWeightLoadingStep 的内容
        checkpoint_path = self.model_cls.model_checkpoint_path(self.model_init_hp)
        eval_model = self.model_cls.from_pre_saved(checkpoint_path)
        eval_result = eval_model.evaluate(self.test_ds)
        logger.info(f"eval result : {eval_result}")
        loss, default_metrics, *_ = eval_result

        if getattr(self, "metrics_reporter", None) is not None:
            logger.info(f"report model final result {default_metrics}")
            await self.report_final_result(default_metrics)
            await asyncio.sleep(60.)


GlobalGSStepMapping.register(FuncStrStep, TFTrainStep, rule_name="train_ds",
                             diff_name={FuncStrStep.func_result: TFTrainStep.train_ds})

GlobalGSStepMapping.register(FuncStrStep, TFTrainStep, rule_name="val_ds",
                             diff_name={FuncStrStep.func_result: TFTrainStep.val_ds})

GlobalGSStepMapping.register(FuncStrStep, TFTrainStep, rule_name="test_ds",
                             diff_name={FuncStrStep.func_result: TFTrainStep.test_ds})


GlobalGSStepMapping.register(TSCategoryDatasetPreparingStep, TFTrainStep, rule_name="train_ds",
                             diff_name={TSCategoryDatasetPreparingStep.tf_ds: TFTrainStep.train_ds})

GlobalGSStepMapping.register(TSCategoryDatasetPreparingStep, TFTrainStep, rule_name="val_ds",
                             diff_name={TSCategoryDatasetPreparingStep.tf_ds: TFTrainStep.val_ds})

GlobalGSStepMapping.register(TSCategoryDatasetPreparingStep, TFTrainStep, rule_name="test_ds",
                             diff_name={TSCategoryDatasetPreparingStep.tf_ds: TFTrainStep.test_ds})

GlobalGSStepMapping.register(TSPortfolioWeightTFDSStep, TFTrainStep, rule_name="train_ds",
                             diff_name={TSPortfolioWeightTFDSStep.tf_ds: TFTrainStep.train_ds})

GlobalGSStepMapping.register(TSPortfolioWeightTFDSStep, TFTrainStep, rule_name="val_ds",
                             diff_name={TSPortfolioWeightTFDSStep.tf_ds: TFTrainStep.val_ds})

GlobalGSStepMapping.register(TSPortfolioWeightTFDSStep, TFTrainStep, rule_name="test_ds",
                             diff_name={TSPortfolioWeightTFDSStep.tf_ds: TFTrainStep.test_ds})

GlobalGSStepMapping.register(FinancialStatementCSMaskedTFDatasetStep, TFTrainStep, rule_name="train_ds",
                             diff_name={FinancialStatementCSMaskedTFDatasetStep.tf_ds: TFTrainStep.train_ds})

GlobalGSStepMapping.register(FinancialStatementCSMaskedTFDatasetStep, TFTrainStep, rule_name="val_ds",
                             diff_name={FinancialStatementCSMaskedTFDatasetStep.tf_ds: TFTrainStep.val_ds})

GlobalGSStepMapping.register(FinancialStatementCSMaskedTFDatasetStep, TFTrainStep, rule_name="test_ds",
                             diff_name={FinancialStatementCSMaskedTFDatasetStep.tf_ds: TFTrainStep.test_ds})

GlobalGSStepMapping.register(EquityPoolTSDatasetStep, TFTrainStep, rule_name="train_ds",
                             diff_name={EquityPoolTSDatasetStep.tf_ds: TFTrainStep.train_ds})

GlobalGSStepMapping.register(EquityPoolTSDatasetStep, TFTrainStep, rule_name="val_ds",
                             diff_name={EquityPoolTSDatasetStep.tf_ds: TFTrainStep.val_ds})

GlobalGSStepMapping.register(EquityPoolTSDatasetStep, TFTrainStep, rule_name="test_ds",
                             diff_name={EquityPoolTSDatasetStep.tf_ds: TFTrainStep.test_ds})

GlobalGSStepMapping.register(TFModelStep, TFTrainStep, same_name={TFTrainStep.model_cls, TFTrainStep.model_init_hp})

GlobalGSStepMapping.register(CompileStep, TFTrainStep, diff_name={CompileStep.out_kwargs: TFTrainStep.compile_kwargs})

GlobalGSStepMapping.register(FitStep, TFTrainStep, diff_name={FitStep.out_kwargs: TFTrainStep.fit_kwargs})

GlobalGSStepMapping.register(ModelCheckPointStep, TFTrainStep,
                             diff_name={ModelCheckPointStep.out_kwargs: TFTrainStep.checkpoint_kwargs})

GlobalGSStepMapping.register(TensorBoardStep, TFTrainStep,
                             diff_name={TensorBoardStep.out_kwargs: TFTrainStep.tensor_board_kwargs})

GlobalGSStepMapping.register(EarlyStoppingStep, TFTrainStep,
                             diff_name={EarlyStoppingStep.out_kwargs: TFTrainStep.early_stopping_kwargs})

if __name__ == "__main__":
    # _pip_op => _input_steps
    # GSOp => GSStep
    import json

    index_membership_ts_step = SymbolTSStep(api="index_weight",
                                            symbols={"BigCap": "000043.SH", "MidCap": "000044.SH", "SmlCap": "000045.SH"},
                                            cols=["con_code"])
    f_after_split_step = FuncStrStep(
        func_body="lambda df : {t: set(df[df.index == t][df.columns[0]].tolist()) for t in df.index.unique()}")
    train_val_set = TrainValSpiltStep(_input_steps=[index_membership_ts_step, f_after_split_step], split_ratio=0.85)
    time_align_step = SymbolTSStep(api="index_quotation_daily", symbols="000001.SH", cols=["close"])
    x_ts_data_step = SymbolTSStep(api="equity_backward_adjust_daily",
                                  cols=["open", "high", "low", "close", "pre_close", "change", "pct_chg", "vol", "amount"])

    train_val_tf_ds_step = DELTSCategoryMultiPeriodDatasetStep(
        _input_steps=[train_val_set, (time_align_step, "time_align"), (x_ts_data_step, "x_data_callable")])
    train_ds_step = FuncStrStep(func_body="lambda ds: ds.repeat().batch(10)")
    val_ds_step = FuncStrStep(func_body="lambda ds: ds.repeat().batch(10)")
    model_step = TFModelStep(model_cls_str=cls_to_str(InceptionTime),
                             model_hp=InceptionTime.HP(nb_classes=3))
    compile_step = CompileStep(loss="categorical_crossentropy", optimizer="Adam", metrics=['accuracy'])
    fit_step = FitStep(epochs=10, steps_per_epoch=4500, validation_steps=110)
    checkpoint_step = ModelCheckPointStep(save_best_only=True, verbose=1)
    tensor_board_step = TensorBoardStep(write_graph=False)

    train_step = TFTrainStep(
        _input_steps=[train_val_tf_ds_step, (train_ds_step, "train_pip_line"), (val_ds_step, "val_pip_line"),
                      model_step, compile_step, fit_step, checkpoint_step, tensor_board_step])

    # train_step.fit()
    # 作为一个标准的 workflow 进行保存
    sample_file_path = os.path.join(os.path.dirname(__file__), "..", "..", "samples", "workflow_cfg",
                                    "inception_category_workflow_v1.yml")
    print(sample_file_path)
    save_mapping_to_file_or_stream(sample_file_path, train_step.get_init_value_dict(True))

