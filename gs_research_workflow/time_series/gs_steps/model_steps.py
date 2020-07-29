# -*- coding: UTF-8 -*-

"""
Model inst 的创建
"""
import json
import os
from typing import Union, Any, Optional, List, Mapping, Type, Set, Dict, NamedTuple

from dataclasses import dataclass, fields, field

from gs_research_workflow.core.gs_step_mapping import GlobalGSStepMapping

from gs_research_workflow.common.path_utilities import get_model_checkpoint_path

from gs_research_workflow.common.serialization_utilities import str_to_cls, cls_to_str, save_mapping_to_file_or_stream

from gs_research_workflow.core.gs_step import GSStep, create_step_by_dict
from tensorflow import keras
import tensorflow as tf
import numpy as np
import pandas as pd

from gs_research_workflow.time_series.gs_steps.tf_dataset_step import TFDSSpecDataCodingType, \
    tf_tensor_spec_type_encoding_decoding


class AdditionalColumnInDS(NamedTuple):
    idx: int
    label: str
    spec_dtype: Optional[TFDSSpecDataCodingType] = None


def predict_category(model: tf.keras.Model, ds_to_pred: tf.data.Dataset, y_true_col_index: Optional[int] = None,
                     additional_cols: Optional[List[AdditionalColumnInDS]] = None) -> pd.DataFrame:
    """
            使用 model 遍历 ds_to_pred 做一次 predict，结果输出为 dataframe

            Parameters
            ----------
            ds_to_pred : tf.data.Dataset
                该dataset 有几个 assumption
                a) dataset 一定是带有 batch 的，哪怕 batch size = 1
                b) col_index = 0 的列，必须是 x
                c) input parameter y_true_col_index is not None 的时候，表示 ds_to_pred 中带有 y_true 的信息
                    含有 y_true 时，会额外输出 y_true 的值，以及 y_true 与 y _pred 是否相等的判定

            y_true_col_index: Optional[int]
                含有 y_true 的列序号，None 表示不含有 y_true 列

            additional_cols: Optional[List[Tuple[int, str, int]]]
                ds 中额外的数据列的信息，数据结构为：Tuple[ColIndex,Label,DType]

            Returns
            -------
                prediction 的结果集

            """
    df_data = {}
    if additional_cols is not None:
        for col in additional_cols:
            df_data[col.label] = list()
    if y_true_col_index is not None:
        df_data["y_true"] = list()
        df_data["is_correct"] = list()

    df_data["y_pred"] = list()
    df_data["y_pred_percentage"] = list()
    df_data["y_pred_distribute"] = list()

    for row_num, value in enumerate(ds_to_pred.take(-1)):
        x = value[0]
        y_pred = model.predict(x)
        y_pred_category_num = tf.math.argmax(y_pred, axis=1)
        y_pred_max_v = tf.math.reduce_max(y_pred, axis=1)
        y_true = None
        y_true_category_num = None
        if y_true_col_index is not None:
            y_true = value[y_true_col_index]
            y_true_category_num = tf.math.argmax(y_true, axis=1)
        df_data["y_pred_distribute"].extend([",".join(["%.4f" % y for y in x.tolist()]) for x in y_pred])
        df_data["y_pred_percentage"].extend(y_pred_max_v.numpy())
        df_data["y_pred"].extend(y_pred_category_num.numpy())
        if y_true_col_index is not None:
            df_data["y_true"].extend(y_true_category_num.numpy())
            df_data["is_correct"].extend((y_pred_category_num == y_true_category_num).numpy())

        if additional_cols is not None:
            for col in additional_cols:
                values = tf_tensor_spec_type_encoding_decoding(col.spec_dtype, value[col.idx], is_encoding=False)
                df_data[col.label].extend(values)

    return pd.DataFrame(data=df_data)


@dataclass
class TFModelStep(GSStep):
    model_cls_str: str
    model_hp: GSStep

    # TODO model 必须放在 train step 进行实例化，这样才能用到 train strategy 的内容
    def __post_init__(self):
        assert self.model_hp is not None
        self._model_cls = str_to_cls(self.model_cls_str)
        assert self.model_hp.__class__ is getattr(self._model_cls, "HP")

        # self._model = model_cls(self.model_hp)

    @property
    def model_cls(self) -> Type:
        return self._model_cls

    @property
    def model_init_hp(self) -> GSStep:  # field 和 property 不能重名，所以这里起一个新的 Property Name
        return self.model_hp

    @property
    def check_point_path(self) -> str:
        model_name = self.model_cls.__name__
        return get_model_checkpoint_path(model_name, self.model_init_hp.get_hash_str())

    # @property
    # def model(self) -> keras.Model:
    #     return self._model


class OutKwargsPropMixin:
    def _field_to_kwargs(self, ignore_fields: Optional[Set[str]] = None) -> Mapping[str, Any]:
        dict_rlt = {}
        for fld in fields(self):
            if ignore_fields and fld.name in ignore_fields:
                continue
            if getattr(self, fld.name, None):
                dict_rlt[fld.name] = getattr(self, fld.name)
        return dict_rlt


@dataclass
class CompileStep(OutKwargsPropMixin, GSStep):
    """
    wrapper model.compile 的参数项
    see https://www.tensorflow.org/api_docs/python/tf/keras/Model#compile
    """

    # region fields

    optimizer: Union[str, Any] = 'rmsprop'
    """ String (name of optimizer) or optimizer instance. See tf.keras.optimizers."""

    loss: Optional[Union[str, Any]] = None
    """String (name of objective function), objective function or tf.losses.Loss instance. See tf.losses. If the model has multiple outputs, you can use a different loss on each output by passing a dictionary or a list of losses. The loss value that will be minimized by the model will then be the sum of all individual losses."""

    str_metrics: Optional[List[Union[str, List[str]]]] = None
    """ List of metrics to be evaluated by the model during training and testing. Typically you will use metrics=['accuracy']. To specify different metrics for different outputs of a multi-output model, you could also pass a dictionary, such as metrics={'output_a': 'accuracy', 'output_b': ['accuracy', 'mse']}. You can also pass a list (len = len(outputs)) of lists of metrics such as metrics=[['accuracy'], ['accuracy', 'mse']] or metrics=['accuracy', ['accuracy', 'mse']]."""

    loss_weights: Optional[Union[List[float], Mapping]] = None
    """ Optional list or dictionary specifying scalar coefficients (Python floats) to weight the loss contributions of different model outputs. The loss value that will be minimized by the model will then be the weighted sum of all individual losses, weighted by the loss_weights coefficients. If a list, it is expected to have a 1:1 mapping to the model's outputs. If a tensor, it is expected to map output names (strings) to scalar coefficients."""

    sample_weight_mode: Optional[str] = None
    """If you need to do timestep-wise sample weighting (2D weights), set this to "temporal". None defaults to sample-wise weights (1D). If the model has multiple outputs, you can use a different sample_weight_mode on each output by passing a dictionary or a list of modes."""

    weighted_metrics: Optional[List[Union[str, List[str]]]] = None
    """List of metrics to be evaluated and weighted by sample_weight or class_weight during training and testing."""

    target_tensors: Any = None
    """By default, Keras will create placeholders for the model's target, which will be fed with the target data during training. If instead you would like to use your own target tensors (in turn, Keras will not expect external Numpy data for these targets at training time), you can specify them via the target_tensors argument. It can be a single tensor (for a single-output model), a list of tensors, or a dict mapping output names to target tensors."""

    metrics: Optional[List[Union[str, Any, List[Any]]]] = field(init=False)

    # endregion

    def __post_init__(self):
        # 调整 metrics 允许支持class类型的对象
        if self.str_metrics and isinstance(self.str_metrics, list):
            tmp_metrics = list()
            for m in self.str_metrics:
                if isinstance(m, list):
                    sub_m_list = list()
                    for sub_m in m:
                        assert isinstance(sub_m, str)
                        if sub_m.find(":") > 0:
                            sub_m_list.append(str_to_cls(m)())
                        else:
                            sub_m_list.append(sub_m)
                    tmp_metrics.append(sub_m_list)
                elif isinstance(m, str):
                    if m.find(":") > 0:  # a class define，create a default instance
                        tmp_metrics.append(str_to_cls(m)())
                    else:
                        tmp_metrics.append(m)
                else:
                    raise RuntimeError(f"Invalid metrics {m}")
            self.metrics = tmp_metrics

    # NOTE: property 在 register 的时候，会有 owner_cls 的检查，所以不能放到 mixin 基类中定义
    @property
    def out_kwargs(self) -> Mapping[str, Any]:
        return self._field_to_kwargs(ignore_fields={"str_metrics"})


@dataclass
class FitStep(OutKwargsPropMixin, GSStep):
    """fit 步骤的参数
    see : https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit
    """

    # region fields

    batch_size: Optional[int] = None
    """Integer or None. Number of samples per gradient update. If unspecified, batch_size will default to 32. Do not specify the batch_size if your data is in the form of symbolic tensors, datasets, generators, or keras.utils.Sequence instances (since they generate batches)."""

    epochs: Optional[int] = None
    """Integer. Number of epochs to train the model. An epoch is an iteration over the entire x and y data provided. Note that in conjunction with initial_epoch, epochs is to be understood as "final epoch". The model is not trained for a number of iterations given by epochs, but merely until the epoch of index epochs is reached."""

    verbose: Optional[int] = None
    """Integer. Number of epochs to train the model. An epoch is an iteration over the entire x and y data provided. Note that in conjunction with initial_epoch, epochs is to be understood as "final epoch". The model is not trained for a number of iterations given by epochs, but merely until the epoch of index epochs is reached."""

    callbacks: Optional[List[Any]] = None
    """
    List of keras.callbacks.Callback instances. List of callbacks to apply during training. See tf.keras.callbacks.
    如果没有特别指定，则workflow将约定用于 save model 和 tensorboard 的 callback
    """

    validation_split: Optional[float] = None
    """Float between 0 and 1. Fraction of the training data to be used as validation data. The model will set apart this fraction of the training data, will not train on it, and will evaluate the loss and any model metrics on this data at the end of each epoch. The validation data is selected from the last samples in the x and y data provided, before shuffling. This argument is not supported when x is a dataset, generator or keras.utils.Sequence instance."""

    # validation_data = None # 由 train workflow 指定

    shuffle: Optional[bool] = None
    """Boolean (whether to shuffle the training data before each epoch) or str (for 'batch'). 'batch' is a special option for dealing with the limitations of HDF5 data; it shuffles in batch-sized chunks. Has no effect when steps_per_epoch is not None."""

    class_weight: Optional[Mapping] = None
    """Optional dictionary mapping class indices (integers) to a weight (float) value, used for weighting the loss function (during training only). This can be useful to tell the model to "pay more attention" to samples from an under-represented class."""

    sample_weight: Optional[np.ndarray] = None
    """Optional Numpy array of weights for the training samples, used for weighting the loss function (during training only). You can either pass a flat (1D) Numpy array with the same length as the input samples (1:1 mapping between weights and samples), or in the case of temporal data, you can pass a 2D array with shape (samples, sequence_length), to apply a different weight to every timestep of every sample. In this case you should make sure to specify sample_weight_mode="temporal" in compile(). This argument is not supported when x is a dataset, generator, or keras.utils.Sequence instance, instead provide the sample_weights as the third element of x."""

    initial_epoch: Optional[int] = None
    """Integer. Epoch at which to start training (useful for resuming a previous training run)."""

    steps_per_epoch: Optional[int] = None
    """  Integer or None. Total number of steps (batches of samples) before declaring one epoch finished and starting the next epoch. When training with input tensors such as TensorFlow data tensors, the default None is equal to the number of samples in your dataset divided by the batch size, or 1 if that cannot be determined. If x is a tf.data dataset, and 'steps_per_epoch' is None, the epoch will run until the input dataset is exhausted. This argument is not supported with array inputs. """

    validation_steps: Optional[int] = None
    """Only relevant if validation_data is provided and is a tf.data dataset. Total number of steps (batches of samples) to draw before stopping when performing validation at the end of every epoch. If validation_data is a tf.data dataset and 'validation_steps' is None, validation will run until the validation_data dataset is exhausted."""

    validation_freq: Optional[int] = None
    """Only relevant if validation data is provided. Integer or collections_abc.Container instance (e.g. list, tuple, etc.). If an integer, specifies how many training epochs to run before a new validation run is performed, e.g. validation_freq=2 runs validation every 2 epochs. If a Container, specifies the epochs on which to run validation, e.g. validation_freq=[1, 2, 10] runs validation at the end of the 1st, 2nd, and 10th epochs."""

    max_queue_size: Optional[int] = None
    """Integer. Used for generator or keras.utils.Sequence input only. Maximum size for the generator queue. If unspecified, max_queue_size will default to 10."""

    workers: Optional[int] = None
    """Integer. Used for generator or keras.utils.Sequence input only. Maximum number of processes to spin up when using process-based threading. If unspecified, workers will default to 1. If 0, will execute the generator on the main thread."""

    use_multiprocessing: Optional[bool] = None
    """Boolean. Used for generator or keras.utils.Sequence input only. If True, use process-based threading. If unspecified, use_multiprocessing will default to False. Note that because this implementation relies on multiprocessing, you should not pass non-picklable arguments to the generator as they can't be passed easily to children processes."""

    # endregion

    @property
    def out_kwargs(self) -> Mapping[str, Any]:
        return self._field_to_kwargs()


@dataclass
class ModelCheckPointStep(OutKwargsPropMixin, GSStep):
    """有关 Model check point 有关的内容
    see https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint
    """

    # region fields

    monitor: Optional[str] = None
    """quantity to monitor. default value is ''val_loss """

    verbose: Optional[int] = None
    """ verbosity mode, 0 or 1. default value is 0 """

    save_best_only: Optional[bool] = None
    """if save_best_only=True, the latest best model according to the quantity monitored will not be overwritten.
    default value is False
    """

    save_weights_only: Optional[bool] = None
    """
    if True, then only the model's weights will be saved (model.save_weights(filepath)), else the full model is saved (model.save(filepath)).
    default value is False
    """
    mode: Optional[str] = None
    """
    one of {auto, min, max}. If save_best_only=True, the decision to overwrite the current save file is made based on either the maximization or the minimization of the monitored quantity. For val_acc, this should be max, for val_loss this should be min, etc. In auto mode, the direction is automatically inferred from the name of the monitored quantity.
    default value is 'auto' 
    """
    save_freq: Optional[Union[str, int]] = None
    """'epoch' or integer. When using 'epoch', the callback saves the model after each epoch. When using integer, the callback saves the model at end of a batch at which this many samples have been seen since last saving. Note that if the saving isn't aligned to epochs, the monitored metric may potentially be less reliable (it could reflect as little as 1 batch, since the metrics get reset every epoch). Defaults to 'epoch'
    """

    # endregion

    @property
    def out_kwargs(self) -> Mapping[str, Any]:
        return self._field_to_kwargs()


@dataclass
class TensorBoardStep(OutKwargsPropMixin, GSStep):
    """保存 tensorboard 信息的详细参数内容
    SEE https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TensorBoard
    """

    # region fields

    histogram_freq: Optional[int] = None
    """frequency (in epochs) at which to compute activation and weight histograms for the layers of the model. If set to 0, histograms won't be computed. Validation data (or split) must be specified for histogram visualizations."""

    write_graph: Optional[bool] = None
    """whether to visualize the graph in TensorBoard. The log file can become quite large when write_graph is set to True.
    Default Value is True
    """

    write_images: Optional[bool] = None
    """ whether to write model weights to visualize as image in TensorBoard.
     Default value is False"""

    update_freq: Optional[Union[str, int]] = None
    """
    'batch' or 'epoch' or integer. When using 'batch', writes the losses and metrics to TensorBoard after each batch. The same applies for 'epoch'. If using an integer, let's say 1000, the callback will write the metrics and losses to TensorBoard every 1000 samples. Note that writing too frequently to TensorBoard can slow down your training.
    default value is 'epoch'
    """

    profile_batch: Optional[int] = None
    """ Profile the batch to sample compute characteristics. By default, it will profile the second batch. Set profile_batch=0 to disable profiling. Must run in TensorFlow eager mode.
    default value is 2"""

    embeddings_freq: Optional[int] = None
    """
    frequency (in epochs) at which embedding layers will be visualized. If set to 0, embeddings won't be visualized.
    default value is 0
    """

    embeddings_metadata: Optional[Mapping] = None
    """a dictionary which maps layer name to a file name in which metadata for this embedding layer is saved. See the details about metadata files format. In case if the same metadata file is used for all embedding layers, string can be passed.
    default value is None"""

    # endregion

    @property
    def out_kwargs(self) -> Mapping[str, Any]:
        return self._field_to_kwargs()


@dataclass
class EarlyStoppingStep(OutKwargsPropMixin, GSStep):
    """
    see https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/EarlyStopping
    """

    # region fields

    monitor: Optional[str] = None
    """ Quantity to be monitored
            default value is 'val_loss'
    """
    min_delta: Optional[int] = None
    """
    Minimum change in the monitored quantity to qualify as an improvement, i.e. an absolute change of less than min_delta, will count as no improvement.
            default value is 0
    """

    patience: Optional[int] = None
    """Number of epochs with no improvement after which training will be stopped.
    default value is 0"""

    verbose: Optional[int] = None
    """verbosity mode.
        Default value is 0
    """

    mode: Optional[str] = None
    """One of {"auto", "min", "max"}. In min mode, training will stop when the quantity monitored has stopped decreasing; in max mode it will stop when the quantity monitored has stopped increasing; in auto mode, the direction is automatically inferred from the name of the monitored quantity.
    default value is 'auto'
    """
    baseline: Optional[float] = None
    """ Baseline value for the monitored quantity. Training will stop if the model doesn't show improvement over the baseline"""

    restore_best_weights: Optional[bool] = None
    """
     Whether to restore model weights from the epoch with the best value of the monitored quantity. If False, the model weights obtained at the last step of training are used
     default value is false
    """

    # endregion

    @property
    def out_kwargs(self) -> Mapping[str, Any]:
        return self._field_to_kwargs()


@dataclass
class ModelPathGeneratorStep(GSStep):
    """Model 路径的生成规则"""
    model_name: str
    """model class name"""
    hp_hash_str: str
    """参数的hash值"""

    @property
    def model_path(self) -> str:
        return get_model_checkpoint_path(self.model_name, self.hp_hash_str)


class ModelPredictionMixin:

    def predict(self, ds_to_pred: tf.data.Dataset, y_true_col_index: Optional[int] = None,
                additional_cols: Optional[List[AdditionalColumnInDS]] = None) -> pd.DataFrame:
        return predict_category(self.model, ds_to_pred, y_true_col_index, additional_cols)


@dataclass
class ModelWithWeightSaveLoadStep(ModelPredictionMixin, GSStep):
    """已经训练好的 model 装载到内存的 Step"""
    model_saved_path: str

    MODEL_FULL_CFG_FILE_NAME = "model_reinit.js"

    def __post_init__(self):
        assert os.path.exists(self.model_saved_path)

    def _model_full_cfg_file(self) -> str:
        return os.path.join(self.model_saved_path, ModelWithWeightSaveLoadStep.MODEL_FULL_CFG_FILE_NAME)

    def _load_model(self):
        assert os.path.isfile(self._model_full_cfg_file())
        with open(self._model_full_cfg_file(), "r") as f:
            architecture_obj = json.load(f)
        model_cls_str, model_init_hp, compile_kwargs = architecture_obj
        model_cls = str_to_cls(model_cls_str)
        model = model_cls(create_step_by_dict(model_init_hp))
        model.compile(**compile_kwargs)
        latest_cp_path = tf.train.latest_checkpoint(self.model_saved_path)
        # NOTE: 这里的 load 的 check_point 是不包含 Optimizer 的 state , tensorflow 会有 warning 出现
        model.load_weights(latest_cp_path)
        self._model = model

    @property
    def model(self) -> keras.Model:
        # NOTE: model 的 loading 过程 lazy 化，而不是在 __post_init__ 中进行 model 的 loading
        if not hasattr(self, "_model"):
            self._load_model()
        return self._model

    def save_model(self, model_cls, model_init_hp: GSStep, compile_kwargs: Dict[str, Any]):
        obj_to_dump = (cls_to_str(model_cls), model_init_hp.get_init_value_dict(True), compile_kwargs)
        with open(self._model_full_cfg_file(), "w") as f:
            json.dump(obj_to_dump, f)
        # 存一份单独的 model_hp 数据，已提供给 human 查看用，所以推荐使用 yml 的格式
        save_mapping_to_file_or_stream(os.path.join(self.model_saved_path, "model_hp.yml"),
                                       model_init_hp.get_init_value_dict(True))


GlobalGSStepMapping.register(ModelPathGeneratorStep, ModelWithWeightSaveLoadStep,
                             diff_name={
                                 ModelPathGeneratorStep.model_path: ModelWithWeightSaveLoadStep.model_saved_path})

if __name__ == "__main__":
    # from gs_research_workflow.time_series.models.inception_time import InceptionTime, InceptionBlock
    # import tensorflow as tf
    #
    # model_step = TFModelStep(model_cls_str=cls_to_str(InceptionTime),
    #                          model_hp=InceptionTime.HP(nb_classes=3))
    # model_step.model.build(input_shape=tf.TensorShape([None] + [128, 9]))
    # model_step.model.compile(loss='categorical_crossentropy',
    #                          optimizer="Adam",
    #                          metrics=['accuracy'])
    # print(model_step.model.summary())

    # compile_step = CompileStep(loss="categorical_crossentropy", optimizer="Adam", metrics=['accuracy'])
    # print(compile_step.out_kwargs)

    fit_step = FitStep(epochs=10, steps_per_epoch=4500, validation_steps=110)
    print(fit_step.out_kwargs)


    # import yaml
    # print(yaml.dump(model_step.get_init_value_dict(True)))


