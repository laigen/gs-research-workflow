# -*- coding: utf-8 -*-

"""
与路径有关的一些功能内容

当前 Project 会在 WSL / Docker / Colab 这几种场景中使用，本 Module 所提供的 function , 能够使得在这三种应用场景都有一致性的存储路径规则

说明：
    Google Drive 在 Colab 中能够访问的路径， Mount 代码为 drive.mount("/gdriver")
        [DATA_ROOT] := /gdrive/My Drive/GS
        含义为： /用户Mount指定位置/colab.drive代码中固定加上/多账户共同的Share Folder

各部分的数据文件位置：
> 数据文件（training dataset）： [DATA_ROOT]/TrainingData/[DATA_SOURCE_NAME]/[DATA_NAME]/[element.pkl]
    如：tushare 的 股票市场日数据：  [DATA_ROOT]/TrainingData/tushare_pro/tushare_daily_per_symbol/600000.SH.pkl

> Model Checkpoint : [DATA_ROOT]/ModelData/[ModelName]/[HyperParametersHash]/CheckPointFiles
                注：该目录下有一个 model_hp.yml 文件，描述了 model 的 hyper parameter 信息
                    该目录下也会保存一个 workflow_hp.yml 文件，描述了整个 train workflow 的所有参数情况

> Training TensorBoard : [DATA_ROOT]/TensorBoard/[ModelName]/[HyperParametersHash]/YYYMMDD-HHmmSS
                注：一个 model 可能会 training 多次，tensorboard 的文件路径应该分开，这也是标准做法


> Workflow Config File : [DATA_ROOT]/workflow/[ModelName]/[cfg_hash].yml
        说明： (1) 通常这个 cfg 文件是由代码产生的，所以文件名只要不冲撞就可以了。如果人为的修改产生这个 yml 文件，可以起一个易于识别的名字

        
> Workflow hyper-parameter dict : [DATA_ROOT]/ModelData/[ModelName]/[HyperParametersHash]/hp.json
        注：这里 hp.json 是整个 workflow 的参数。 在 workflow 内，可以单独将 model 的参数分支取出来后保存为  model.json
        
> HPO Experiment:
    Google Drive Location
        GS/NNI_EXPERIMENTS/HPO/[ExperimentName]/notebooks/[cfg_hash].ipynb
        GS/NNI_EXPERIMENTS/HPO/[ExperimentName]/trial_cfg/[cfg_hash].yml

"""

import os
from datetime import datetime
from typing import Mapping

_DATA_ROOT: str = os.path.join("/gdrive", "My Drive", "GS")
"""数据的根路径"""


def _is_colab_env() -> bool:
    """当前的环境是否为 colab 
        NOTE: 通过观察，发现 Colab VM 会有一个环境变量 COLAB_GPU 记录是否含有 GPU 资源，以此为特征信息判断执行环境是否为 Colab
    """
    return "COLAB_GPU" in os.environ


def _check_data_root():
    """
    检查数据根路径是否存在
        Colab 场景下，如果不存在则抛出异常，用户尚未进行绑定
        非 Colab 场景下，如果不存在则创建该 folder
    """
    if not os.path.exists(_DATA_ROOT):
        if _is_colab_env():
            raise RuntimeError("""Should mount google drive first! use code
            from google.colab import drive
            drive.mount('/gdriver')""")
        else:
            os.makedirs(_DATA_ROOT)


def get_training_data_file_path(data_source: str, data_name: str) -> str:
    _check_data_root()
    file_path = os.path.join(_DATA_ROOT, "TrainingData", data_source, data_name)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    return file_path


def get_workflow_file_path(model_name: str) -> str:
    _check_data_root()
    file_path = os.path.join(_DATA_ROOT, "workflow", model_name)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    return file_path


def get_model_checkpoint_path(model_name: str, hash_str: str) -> str:
    _check_data_root()
    file_path = os.path.join(_DATA_ROOT, "ModelData", model_name, hash_str)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    return file_path


def get_tensor_board_path(model_name: str, hash_str: str) -> str:
    _check_data_root()
    file_path = os.path.join(_DATA_ROOT, "TensorBoard", model_name, hash_str)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    return file_path


def get_prediction_output_path(model_name: str, prediction_name: str) -> str:
    """prediction 结果的 csv 输出"""
    _check_data_root()
    file_path = os.path.join(_DATA_ROOT, "ModelPrediction", model_name, prediction_name)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    return file_path


def get_hpo_trial_cfg_path(experiment_name: str, hash_str: str) -> str:
    # NOTE: 这里不需要对路径进行Exist检查
    # NNI_EXPERIMENTS/HPO/[ExperimentName]/trial_cfg/[cfg_hash].yml
    return os.path.join(_DATA_ROOT, "NNI_EXPERIMENTS", "HPO", experiment_name, "trial_cfg", f"{hash_str}.yml")


def get_hpo_notebook_path(experiment_name: str) -> str:
    return os.path.join(_DATA_ROOT, "NNI_EXPERIMENTS", "HPO", experiment_name, "notebooks")


def get_prediction_cfg_path(model_name: str, cfg_hash: str) -> str:
    # GS/SYS_MODEL_PREDICTION/[MODEL_NAME]/workflow_cfg/[cfg_hash].yml
    return os.path.join(_DATA_ROOT, "SYS_MODEL_PREDICTION", model_name, "workflow_cfg", f"{cfg_hash}.yml")


if __name__ == "__main__":
    get_training_data_file_path("tushare_pro", "tushare_daily_per_symbol")
