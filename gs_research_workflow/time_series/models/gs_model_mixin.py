# -*- coding: UTF-8 -*-
import json
from typing import Dict, Optional

import os
import tensorflow as tf
from gs_research_workflow.common.serialization_utilities import cls_to_str

from gs_research_workflow.core.gs_step import GSStep, create_step_by_dict

from gs_research_workflow.common.path_utilities import get_model_checkpoint_path, get_tensor_board_path
from gs_research_workflow.time_series.models.gs_loss_functions import process_compile_loss_kwargs


class GSModelMixin:
    _MODEL_FULL_CFG_FILE_NAME: str = "model_full_cfg.js"
    MODEL_CHECKPOINT_FILE_NAME: str = "cp.ckpt"
    TF2_WEIGHTS_NAME: str = "tf_model.h5"

    @property
    def dummy_inputs(self):
        """ Dummy inputs to build the network.

        Returns:
            tf.Tensor with dummy inputs
        """
        return tf.constant(1., shape=self._dummy_input_shape, dtype=tf.float32)  # 每个 派生类需要定义自己的 dummy input shape 的数据

    @classmethod
    def model_checkpoint_path(cls, init_hp: GSStep) -> str:
        model_name = cls.__name__
        return get_model_checkpoint_path(model_name, init_hp.get_hash_str())

    @classmethod
    def model_checkpoint_file(cls, pre_saved_checkpoint_path: str) -> str:
        return os.path.join(pre_saved_checkpoint_path, GSModelMixin.MODEL_CHECKPOINT_FILE_NAME)

    @classmethod
    def model_tensorboard_path(cls, init_hp: GSStep) -> str:
        model_name = cls.__name__
        return get_tensor_board_path(model_name, init_hp.get_hash_str())

    @classmethod
    def save_model_full_cfg(cls, model_full_cfg_file_path: str, init_hp: GSStep, compile_kwargs: Dict):
        # NOTE:compile_kwargs 里的 metrics 如果是 Metrics Class 的话，无法序列化成 json 和 pickles
        #  所以这里先暂时假定 compile_kwargs 里面的 metrics 都是 string 类型
        model_full_cfg_file = os.path.join(model_full_cfg_file_path, GSModelMixin._MODEL_FULL_CFG_FILE_NAME)
        obj_to_dump = (cls_to_str(cls), init_hp.get_init_value_dict(True), compile_kwargs)
        with open(model_full_cfg_file, "w") as f:
            json.dump(obj_to_dump, f)

    def save_model_and_weights(self, model_full_cfg_file_path: str):
        assert isinstance(self, tf.keras.Model)
        output_model_file = os.path.join(model_full_cfg_file_path, GSModelMixin.TF2_WEIGHTS_NAME)
        self.save_weights(output_model_file)

    @classmethod
    def from_pre_saved(cls, pre_saved_checkpoint_path: str) -> Optional[tf.keras.Model]:
        model_full_cfg_file = os.path.join(pre_saved_checkpoint_path, GSModelMixin._MODEL_FULL_CFG_FILE_NAME)
        if not os.path.isfile(model_full_cfg_file):
            return None
        model_weight_file = os.path.join(pre_saved_checkpoint_path, GSModelMixin.TF2_WEIGHTS_NAME)
        if not os.path.isfile(model_weight_file):
            return None

        with open(model_full_cfg_file, "r") as f:
            architecture_obj = json.load(f)
        model_cls_str, model_init_hp, compile_kwargs = architecture_obj
        model = cls(create_step_by_dict(model_init_hp))

        # model 先运行一次可能会有问题，因为输入有可能不是一个简单的 tensor
        model(model.dummy_inputs, training=False)  # build the network with dummy inputs
        model.compile(**process_compile_loss_kwargs(compile_kwargs))
        model.load_weights(model_weight_file, by_name=True)  # by_name = True for transfer learning
        model(model.dummy_inputs, training=False)  # Make sure restore ops are run
        return model

    @classmethod
    def from_init_hp_compile(cls, init_hp: GSStep, compile_kwargs: Dict) -> Optional[tf.keras.Model]:
        model = cls(init_hp)
        model.compile(**process_compile_loss_kwargs(compile_kwargs))
        return model
