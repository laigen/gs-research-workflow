# -*- coding: utf-8 -*-

"""
NNI Local Experiment
see : https://github.com/microsoft/nni/blob/master/docs/en_US/TrainingService/LocalMode.md
see : https://nni.readthedocs.io/en/latest/TrainingService/LocalMode.html
"""
import os

import yaml
from dataclasses import dataclass, field, asdict
from typing import Optional, Dict, List

from gs_research_workflow.common.google_drive import GoogleDriveWrapper, MIME_FOLDER

from gs_research_workflow.common.google_oauth import get_google_token

from gs_research_workflow.common.serialization_utilities import cls_to_str, load_mapping_from_file

from gs_research_workflow.auto_ml.nni.hpo.trial_main_pod_side import HPOTrialPodSideEnv, ExecTrialMachineType

from gs_research_workflow.core.gs_step import GSStep, lookup_step_cfg_para

from gs_research_workflow.auto_ml.nni.hpo.search_space import SearchSpace, Choice
import gs_research_workflow


# class FieldsToDictMixin:
#     def get_fields_dict(self) -> Dict:
#         return None
from gs_research_workflow.auto_ml.loc_alias.step_cfg_loc_alias import InceptionCategoryDefaultAlias, \
    InceptionWithAttentionDefaultAlias, TSBertForMaskedCSDefaultAlias

# venv_path = "/root/.pyenv/gs-laigen/"
venv_path = ""  # 直接使用系统的 python ， 不用 venv 中的


def _remove_none_val_in_dict(dict_obj: Dict):
    items_need_remove = list()
    for k, v in dict_obj.items():
        if isinstance(v, dict):
            _remove_none_val_in_dict(v)
        elif v is None:
            items_need_remove.append(k)
        else:
            continue
    if items_need_remove:
        for k in items_need_remove:
            dict_obj.pop(k)


@dataclass(frozen=True)
class TunerArgs(GSStep):
    optimize_mode: str = "maximize"


@dataclass(frozen=True)
class Tuner(GSStep):
    builtinTunerName: str
    """eg:TPE """
    classArgs: Optional[TunerArgs] = None


@dataclass(frozen=True)
class Trial(GSStep):
    command: str
    """eg: 'python mnist.py' """
    codeDir: str
    """eg: '~/nni/examples/trials/mnist-annotation' """
    gpuNum: int = 0


@dataclass
class LocalExperiment(GSStep):
    authorName: str
    """your_name"""

    experimentName: str
    """eg:auto_mnist"""

    trialConcurrency: int
    """how many trials could be concurrently running, eg: 1"""

    maxExecDuration: str
    """maximum experiment running duration , eg : '3H' """

    trainingServicePlatform: str = field(default="local", init=False, repr=False)
    """固定为 local，不能被修改"""

    searchSpacePath: str = field(init=False, repr=False)
    """ SearchSpace 由系统负责填入
    eg: search_space.json"""

    useAnnotation: bool = field(default=False, init=False, repr=False)
    """在GS的应用场景中，不使用 annotation 的方式定义 trial"""

    tuner: Tuner

    trial: Trial = field(init=False, repr=False)
    """trial的参数"""

    maxTrialNum: Optional[int] = None
    """empty means never stop , eg: 100"""

    def set_search_space(self, search_space: SearchSpace):
        """设置 search space 的内容，系统将指定 json 文件的保存位置"""
        self._search_space = search_space
        # Search Space 文件路径是有系统确定，用户不应该在外部进行设置
        self.searchSpacePath = os.path.join(f"{os.path.sep}tmp", "nni", "experiment", self.experimentName, "search_space.json")

    def set_trial_module_and_args(self, trial_module, **kwargs):
        """设置 trial.py 文件的 module , 可用于生成 trial 部分的代码"""
        # python_cmd = "python"
        # if os.getenv("VIRTUAL_ENV", None):
        if venv_path:
            python_cmd = f"""{venv_path}bin/python3"""
        else:
            python_cmd = "python3"
        command = f"""{python_cmd} {trial_module.__file__} {" ".join(['--' + k + ' ' + str(v) for k, v in kwargs.items()])}"""
        self.trial = Trial(command=command, codeDir=f"{os.path.dirname(trial_module.__file__)}", gpuNum=0)

    def to_yml(self) -> str:  # 该接口仅为调试用途
        assert hasattr(self, "_search_space"), '`search_space` should be set first !!!'
        v = self.to_dict()
        print(self.to_dict())
        return yaml.dump(self.to_dict())

    def to_dict(self):
        dict_v = asdict(self)
        _remove_none_val_in_dict(dict_v)
        return dict_v

    def run(self, nnictl_folder: str = "", port: int = 8080):
        """生成 experiment 的 yml 文件，然后调用 nnictl 将 experiment 运行起来
        nnictl_folder 是为了在有 venv 的场景下，能够指定具体的  venv 的 命令行
        """
        # step 1: save search space json file
        import json
        assert hasattr(self, "_search_space"), '`search_space` should be set first !!!'
        experiment_path = os.path.dirname(self.searchSpacePath)
        if not os.path.exists(experiment_path):
            os.makedirs(experiment_path)
        with open(self.searchSpacePath, "w") as json_file:
            json.dump(self._search_space.dict_val, json_file)
        # step 2: save experiment yml file

        # tutorial 中都推荐使用 config.yml。 我们可以用不同的folder 代表不同的 experiment
        experiment_config_file = os.path.join(experiment_path, "config.yml")
        import yaml
        with open(experiment_config_file, "w") as yaml_file:
            yaml.dump(self.to_dict(), yaml_file)
        # run experiment use `nnictl`
        import subprocess
        # eg: nnictl create --config ~/nni/examples/trials/mnist-annotation/config.yml
        # subprocess.run([f"{nnictl_folder}nnictl", "create", "--config", f"{experiment_config_file}"])
        ls_cmd_run = [f"{nnictl_folder}nnictl", "create", "--config", f"{experiment_config_file}", "--debug", "--port",
                      str(port)]
        print(f"cmd: {' '.join(ls_cmd_run)}")
        subprocess.run(ls_cmd_run)


def cfg_value_to_choice(workflow_cfg: Dict, context_cfg: Dict, alias_cls, loc_or_alias: str) -> Choice:
    return Choice(name=loc_or_alias,
                  options=[lookup_step_cfg_para(workflow_cfg, context_cfg, alias_cls.get_cfg_loc(loc_or_alias))])


def prepare_gdrive_folder(experiment_name: str):
    token = get_google_token()
    gdrive = GoogleDriveWrapper(token)

    exp_folder_obj = gdrive.create_or_update_file(experiment_name, MIME_FOLDER, "GS/NNI_EXPERIMENTS/HPO")
    nb_folder_obj = gdrive.create_or_update_file("notebooks", MIME_FOLDER, exp_folder_obj)
    cfg_folder_obj = gdrive.create_or_update_file("trial_cfg", MIME_FOLDER, exp_folder_obj)

    # NOTE: http proxy 必须在这里去掉，否则 启动 nni experiment 的时候会出现错误
    del os.environ["http_proxy"]
    del os.environ["https_proxy"]


def run_colab_experiment(template_file_name: str, experiment_name: str,
                         trial_concurrency: int, max_trial_num: int,
                         tuner: Tuner, cls_hp_alias, hps_to_display: List[str], search_space: List[Choice],
                         vm=ExecTrialMachineType.Colab.value,
                         port: int = 8080):
    import os
    cfg_path = f"samples/workflow_cfg/{template_file_name}"  # 从 project root 开始算起的目录
    yml_abs_path = os.path.join(os.path.dirname(__file__), "../../..", cfg_path)
    workflow_cfg, workflow_context = load_mapping_from_file(yml_abs_path)

    experiment = LocalExperiment(authorName="GS_GROUP",
                                 experimentName=experiment_name,
                                 trialConcurrency=trial_concurrency,
                                 maxExecDuration="168h",
                                 tuner=tuner,
                                 maxTrialNum=max_trial_num
                                 )
    experiment.set_trial_module_and_args(gs_research_workflow.auto_ml.nni.hpo.trial_main_pod_side,
                                         cfg=cfg_path,
                                         pool="gs_google_acct_pool_1",
                                         name=experiment_name,
                                         vm=vm,
                                         cfg_alias=cls_to_str(cls_hp_alias))

    if vm == ExecTrialMachineType.Colab.value:
        prepare_gdrive_folder(experiment_name)

    ls_tune_paras = []
    # 以下是一些用于显示的重要 hp 的内容，不参与 tuning ，只保留一个 Choice 项
    # 不参与 tuning 的超参项放在靠前的位置，可以让 nni 的 展示图形更好看一些
    if hps_to_display:
        ls_tune_paras += [cfg_value_to_choice(workflow_cfg, workflow_context, cls_hp_alias, p) for p in
                          hps_to_display]
    if search_space:
        ls_tune_paras += search_space

    exp_search_space = SearchSpace(parameters=ls_tune_paras)
    experiment.set_search_space(exp_search_space)

    print("-" * 50)
    # NOTE: 必须设置 VIRTUAL_ENV 的环境变量，以使得 nnictl 能够正常在 venv 中运行

    nnictl_folder = ""
    if venv_path:
        os.environ["VIRTUAL_ENV"] = venv_path
        nnictl_folder = f"{venv_path}bin/"
    experiment.run(nnictl_folder=nnictl_folder, port=port)


if __name__ == "__main__":
    experiment_kwargs = {
        "template_file_name": "inception_for_classification_index_cap_membership_category_workflow_v1.yml",
        "experiment_name": "InceptionTimeModelHPTuningLocalExecV8",
        "trial_concurrency": 4,
        "max_trial_num": 12,
        "tuner": Tuner(builtinTunerName="GridSearch"),
        "cls_hp_alias": InceptionCategoryDefaultAlias,
        # 一些用于显示的重要 hp 的内容，不参与 tuning ，只保留一个 Choice 项
        "hps_to_display": ["data.y_categories", "data.x_features", "data.x_api"],
        "search_space": [
            Choice(name="model.depth", options=[4, 5, 6]),
            Choice(name="model.use_residual", options=[True, False]),
            Choice(name="model.use_bottleneck", options=[True, False]),
        ],
        "vm": ExecTrialMachineType.Colab.value,
        "port": 8081,
    }

    # inception_attention_kwargs
    # experiment_kwargs.update({
    #     "template_file_name": "InceptionTimeWithAttentionForWeightPrediction_workflow_v1.yml",
    #     "experiment_name": "InceptionTimeWithAttentionForWeightPredictionV2",
    #     "cls_hp_alias": InceptionWithAttentionDefaultAlias,
    #     "trial_concurrency": 48,
    #     "max_trial_num": 96,
    #     "hps_to_display": None,
    #     "search_space": [
    #         Choice(name="model.depth", options=[6, 10, 14]),
    #         Choice(name="model.use_residual", options=[True, False]),
    #         Choice(name="model.use_bottleneck", options=[True, False]),
    #         Choice(name="model.attention_after_residual", options=[True, False]),
    #         Choice(name="model.attention_at_each_inception", options=[True, False]),
    #         Choice(name="model.attention_at_input", options=[True, False])
    #     ],
    # })

    # ---- Financial Statement CS Bert -------
    # experiment_kwargs.update({
    #     "template_file_name": "TSBertForMaskedCS_workflow_v1.yml",
    #     "experiment_name": "FinancialStatementCSBert",
    #     "cls_hp_alias": TSBertForMaskedCSDefaultAlias,
    #     "trial_concurrency": 8,
    #     "max_trial_num": 8,
    #     "hps_to_display": ["model.hidden_size"],
    #     "search_space": [
    #         Choice(name="model.num_attention_heads", options=[6, 12]),  # 必须是能被整除 model.hidden_size 的数字，且不宜过大
    #         Choice(name="model.num_hidden_layers", options=[8, 12, 16, 20]),
    #     ],
    #     "vm": ExecTrialMachineType.Colab.value,
    # })

    # ----- equity daily return bert ------

    experiment_kwargs.update({
        "template_file_name": "chn_equity_daily_return_less_indicators_workflow_v1.yml",
        "experiment_name": "EquityDailyReturnCSBert_ChnV2",
        "cls_hp_alias": TSBertForMaskedCSDefaultAlias,
        "trial_concurrency": 3,
        "max_trial_num": 8,
        "hps_to_display": ["model.hidden_size"],
        "search_space": [
            Choice(name="model.num_attention_heads", options=[6, 7, 8, 12]),  # 必须是能被整除 model.hidden_size 的数字，且不宜过大
            Choice(name="model.num_hidden_layers", options=[10, 12]),  # 最好不要超过 12 ，否则 Colab GPU 会溢出，或者运行时间过长
        ],
        "vm": ExecTrialMachineType.Colab.value,
    })

    run_colab_experiment(**experiment_kwargs)
