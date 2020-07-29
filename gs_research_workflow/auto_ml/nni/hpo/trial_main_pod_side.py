# -*- coding: utf-8 -*-

"""
pod 端的一个 trial 统一的 文件，主要包含的功能：
"""
import argparse
import asyncio
import logging
import tempfile
from datetime import datetime
from enum import IntEnum
from typing import Mapping

import nni
import pytz
from gs_framework.activatable_stateful_service import Env
from gs_framework.instance_hash_calculation import HashCalculation
from gs_framework.object_reference import ObjectRef
from gs_framework.timer_handler import timer
from gs_framework.utilities import md5_str, generate_uuid, get_random_int

from gs_research_workflow.auto_ml.nni.hpo.arctic_metrics_reporter import TrailMetricsArcticReporter
from gs_research_workflow.auto_ml.nni.hpo.trial_stream import topic_gs_nni_trial, \
    ENV_KEY_TRIAL_IN_NNI, LocalRunGSWorkflowEnv
from gs_research_workflow.auto_ml.notebook.colab_notebook_generator import notebook_by_replace_one_cell
from gs_research_workflow.common.google_drive import GoogleDriveWrapper, MIME_FOLDER, MIME_COLAB
from gs_research_workflow.common.google_oauth import get_google_token
from gs_research_workflow.common.path_utilities import get_hpo_trial_cfg_path, get_hpo_notebook_path
from gs_research_workflow.common.serialization_utilities import load_mapping_from_file, str_to_cls, \
    unescape_nni_choice_item, save_mapping_to_file_or_stream
from gs_research_workflow.core.gs_step import upsert_step_cfg_para, create_step_by_dict

logger = logging.getLogger(__name__)


class ExecTrialMachineType(IntEnum):
    Colab = 1
    Local = 2


class HPOTrialPodSideEnv(Env):

    CELL_CODE_RUN_TRIAL = """# GS --max-run-seconds=36000
# trial params to be check
{trial_params_comment}
from gs_research_workflow.common.serialization_utilities import load_mapping_from_file
from gs_research_workflow.core.gs_step import create_step_by_dict
from gs_research_workflow.auto_ml.nni.hpo.trial_stream import topic_gs_nni_trial
import asyncio
import logging
from gs_research_workflow.common.tee import StdoutTee, StderrTee

logging.getLogger('').addHandler(logging.FileHandler('{nb_path}/{nb_filename}_logger.txt'))

workflow_cfg, workflow_context = load_mapping_from_file("{yml_path}")
# trial_hash_id = "{trail_hash_id}"
experiment_name = "{experiment_name}"
experiment_uuid = "{experiment_uuid}"
trial_uuid = "{trial_uuid}"
one_trial_spec_val = "{one_trial_spec_val}"
loop = asyncio.get_event_loop()

with StdoutTee("{nb_path}/{nb_filename}_stdout.txt",buff=1), StderrTee("{nb_path}/{nb_filename}_stderr.txt",buff=1):
    workflow_inst = create_step_by_dict(workflow_cfg, workflow_context)
    workflow_inst.prepare_metrics_recorder(experiment_name, experiment_uuid, trial_uuid)
    # loop.run_until_complete(workflow_inst.prepare_metrics_callback(trial_hash_id,one_trial_spec_val,topic_gs_nni_trial))
    loop.run_until_complete(workflow_inst.fit())
    loop.run_until_complete(workflow_inst.eval_model())
    loop.run_until_complete(workflow_inst.stop_env())"""


    CELL_CODE_TENSORBOARD = """# GS --max-run-seconds=1200
# trial params to be check
{trial_params_comment}
%load_ext tensorboard
%tensorboard --logdir {tensor_board_path}"""

    TRIAL_MAX_TIMEOUT_SECS = 3600.0 * 24

    SAFETY_SECONDS_4_ASYNC_OPERATIONS_TO_FINISH: int = 60

    # ---- [laigen 2020.02.29] colab train 不再通过 kafka 进行，这里先去掉。  ----
    # trial_colab_env = ObjectRef.bind_at_runtime()
    # ----

    def __init__(self, experiment_name: str, template_workflow_yml_file: str, trial_params: Mapping, trial_uuid: str,
                 experiment_uuid: str):
        super().__init__()
        self.workflow_cfg, self.workflow_context = load_mapping_from_file(template_workflow_yml_file)
        self.trial_params = trial_params
        for k, v in trial_params.items():
            changed_items = upsert_step_cfg_para(self.workflow_cfg, self.workflow_context, k, v)
            if changed_items == 0:
                logger.error(f"'{k}' is not available in config setting , should check search space file")
        self.experiment_name = experiment_name
        self.trial_uuid = trial_uuid
        self.experiment_uuid = experiment_uuid

        self.is_trial_finished = False
        self.cfg_hash = md5_str(HashCalculation.value_to_hash_str(self.workflow_cfg))

        self._trial_finished_future = asyncio.get_event_loop().create_future()

        # ---- [laigen 2020.02.29] colab train 不再通过 kafka 进行，这里先去掉。  ----
        # colab_side_env = TrialColabSideEnv(self.cfg_hash, self.trial_uuid)
        # self._colab_side_env_pk = colab_side_env.pk
        # ---- end ----
        self.metrics_reporter = TrailMetricsArcticReporter(self.experiment_name, self.experiment_uuid, self.trial_uuid)
        self.latest_epoch = None
        self.final_val = None

    @staticmethod
    def get_trial_max_timeout_secs(machine_type: ExecTrialMachineType = ExecTrialMachineType.Colab) -> float:
        if machine_type == ExecTrialMachineType.Colab:
            return 3600.0 * 12
        elif machine_type == ExecTrialMachineType.Local:
            return 3600.0 * 24
        else:
            raise RuntimeError(f"not supported machine_type:{machine_type}")

    # ---- [laigen 2020.02.29] colab train 不再通过 kafka 进行，这里先去掉。  ----
    # @property
    # def colab_side_env_pk(self) -> str:
    #     return self._colab_side_env_pk
    # ---- end ----

    async def run_in_local_smoke_test(self):
        """用于测试，在本地直接run这个 trail 的 workflow"""
        workflow_inst = create_step_by_dict(self.workflow_cfg, self.workflow_context)
        # ---- [laigen 2020.02.29] colab train 不再通过 kafka 进行，这里先去掉。  ----
        # await workflow_inst.prepare_metrics_callback(self.cfg_hash, self.trial_uuid)
        # ---- end ----
        workflow_inst.prepare_metrics_recorder(self.experiment_name, self.experiment_uuid, self.trial_uuid)
        await workflow_inst.fit()
        await workflow_inst.eval_model()

    def _trial_run_cell_code(self) -> str:
        trial_params_comment = "\r\n".join([f"#{k} <= {v}" for k, v in self.trial_params.items()])
        return HPOTrialPodSideEnv.CELL_CODE_RUN_TRIAL.format(trial_params_comment=trial_params_comment,
                                                             yml_path=get_hpo_trial_cfg_path(self.experiment_name,
                                                                                                 self.cfg_hash),
                                                             trail_hash_id=self.cfg_hash,
                                                             experiment_name=self.experiment_name,
                                                             experiment_uuid=self.experiment_uuid,
                                                             trial_uuid=self.trial_uuid,
                                                             one_trial_spec_val=self.trial_uuid,
                                                             nb_path=get_hpo_notebook_path(self.experiment_name),
                                                             nb_filename=self.nb_file_prefix)

    def _trial_tensor_board_cell_code(self) -> str:
        trial_params_comment = "\r\n".join([f"#{k} <====> {v}" for k, v in self.trial_params.items()])
        workflow_inst = create_step_by_dict(self.workflow_cfg, self.workflow_context)

        return HPOTrialPodSideEnv.CELL_CODE_TENSORBOARD.format(trial_params_comment=trial_params_comment,
                                                               tensor_board_path=workflow_inst.tensorboard_path.replace(
                                                                   " ", "\\ ")
                                                               )

    async def _prepare_colab_resource(self):
        # 检查路径
        # Google Drive Location
        # GS/NNI_EXPERIMENTS/HPO/[ExperimentName]/notebooks/yyyyMMdd_hhmmss_[experiment_uuid]_[trial_uuid].ipynb
        # GS/NNI_EXPERIMENTS/HPO/[ExperimentName]/notebooks/[cfg_hash]_[trial_id]_tensorboard.ipynb
        # GS/NNI_EXPERIMENTS/HPO/[ExperimentName]/trial_cfg/[cfg_hash].yml

        token = get_google_token()
        gdrive = GoogleDriveWrapper(token)

        # 随机等待一段时间，避免在同一个时间点上创建了多份相同的目录(挪到 local_experiment.py 之后，sleep 可以不再需要)
        await asyncio.sleep(get_random_int(1, 30))

        # 检查路径同时获取 FileID , 创建的逻辑已经挪到的 experiment 中，这里仅为获取
        exp_folder_obj = gdrive.create_or_update_file(self.experiment_name, MIME_FOLDER, "GS/NNI_EXPERIMENTS/HPO",
                                                      get_only=True)
        logger.debug(f"exp_folder_obj:{exp_folder_obj}")
        nb_folder_obj = gdrive.create_or_update_file("notebooks", MIME_FOLDER, exp_folder_obj, get_only=True)
        cfg_folder_obj = gdrive.create_or_update_file("trial_cfg", MIME_FOLDER, exp_folder_obj, get_only=True)

        with tempfile.NamedTemporaryFile("w", suffix=".yml", delete=False) as f:
            save_mapping_to_file_or_stream(f, self.workflow_cfg, self.workflow_context)
            yaml_path = f.name
        yml_gfile = gdrive.create_or_update_file(f"{self.cfg_hash}.yml", None, cfg_folder_obj, yaml_path)
        logger.info(f"yml file is created on google drive {yml_gfile}")
        t = datetime.now(tz=pytz.timezone("Asia/Shanghai"))
        # NOTE: 该命名规则方便排序找到相应的 notebook
        self.nb_file_prefix = f"{t.strftime('%Y%m%d_%H%M%S')}_{self.experiment_uuid}_{self.trial_uuid}"
        nb_filename = self.nb_file_prefix + ".ipynb"
        colab_file_path = notebook_by_replace_one_cell(template_file_name='colab_template', cell_idx=3,
                                                       new_code=self._trial_run_cell_code(),
                                                       new_nb_name=nb_filename)
        colab_gfile = gdrive.create_or_update_file(nb_filename, MIME_COLAB, nb_folder_obj, colab_file_path)
        logger.info(f"colab notebook file is created on google drive {colab_gfile}")
        self.notebook_file_id = colab_gfile.id

        # 暂时先不支持 tensorboard 的功能
        # colab_tensorboard_path = notebook_by_replace_one_cell(template_file_name="colab_tensorboard", cell_idx=1,
        #                                                       new_code=self._trial_tensor_board_cell_code(),
        #                                                       new_nb_name=f"{self.cfg_hash}_{self.trial_uuid}_tensorboard.ipynb")
        # colab_tensorboard_gfile = gdrive.create_or_update_file(f"{self.cfg_hash}_{self.trial_uuid}_tensorboard.ipynb",
        #                                                        MIME_COLAB,
        #                                                        nb_folder_obj, colab_tensorboard_path)
        # logger.info(f"colab tensorboard notebook file is created on google drive {colab_tensorboard_gfile}")

    async def _exec_trial_in_colab(self):
        # TODO:调用 google account pool 的 rpc 接口，将 colab 跑起来
        logger.info(f"One trial spec value: {self.trial_uuid}")
        logger.info(
            f"Open web browser and run notebook in url: https://colab.research.google.com/drive/{self.notebook_file_id}")

        # call colab pool and run colab use rpc call
        from gs_framework.service import StatelessService
        from gs_framework.colab.colab_pool_client import ColabPoolClient
        from gs_framework.colab.colab_pool_0_constants import Configuration as colab_config
        from gs_framework.activatable_stateful_service import Env
        import faust.types

        class _ColabPoolService(StatelessService):
            def __init__(self, pool_client: ColabPoolClient, _):
                super().__init__()
                self._pool_client: ColabPoolClient = pool_client
                self.add_service_units(pool_client)

            async def start(self):
                await super().start()
                await self._pool_client.get_ready()

        class _ColabPoolCallEnv(Env):
            def __init__(self, trial_uuid: str):
                super().__init__()
                self.trial_uuid = trial_uuid

            async def run_colab(self, notebook_file_id: str, task_group_name: str):
                pool_client = ColabPoolClient(colab_config.pool_name, colab_config.pool_env_rpc_callee_topic)
                pool_client.pool_env_status_stream.bind(topic_define=colab_config.pool_env_status_topic)
                pool_client.rpc_caller_stream.bind(topic_define=colab_config.pool_client_rpc_caller_topic)

                pool_test_service = _ColabPoolService(pool_client, self.trial_uuid)
                await pool_test_service.start()
                logger.info(f"_ColabPoolService service started")

                task_id = await pool_client.submit(notebook_file_id, task_group_name)
                logger.info(f"after submit({notebook_file_id} - {task_group_name} ): {task_id}")

        self.colab_caller_env = _ColabPoolCallEnv(self.trial_uuid)
        self.colab_caller_env.bind(topic_define=faust.types.TP(topic="nni_colab_pool_0", partition=1))
        await self.colab_caller_env.start()
        await self.colab_caller_env.run_colab(self.notebook_file_id, self.experiment_name)
        await asyncio.sleep(60)  # 因为是 submit ，这里为了安全，只 sleep 1min

    async def _stop_trial_in_colab(self):
        if getattr(self, "colab_caller_env", None) is not None:
            await self.colab_caller_env.stop()

    async def _prepare_trial_local_resource(self):
        with tempfile.NamedTemporaryFile("w", suffix=".yml", delete=False) as f:
            save_mapping_to_file_or_stream(f, self.workflow_cfg, self.workflow_context)
            yaml_path = f.name
        self.local_trial_exec_env = LocalRunGSWorkflowEnv(self.cfg_hash, self.experiment_name, self.experiment_uuid,
                                                          self.trial_uuid)
        self.local_trial_exec_env.set_workflow_data(yaml_path)

    async def _exec_trial_in_local(self):
        self.local_trial_exec_env.bind(topic_define=topic_gs_nni_trial)
        await self.local_trial_exec_env.start()
        self.local_trial_exec_env.need_to_run_flag.VALUE = 1
        self.local_trial_exec_env.commit_state_var_changes()

    async def _stop_trial_in_local(self):
        await self.local_trial_exec_env.stop()

    async def start_trial(self, machine_type: ExecTrialMachineType = ExecTrialMachineType.Colab):
        self._trial_start_time = datetime.now()

        if machine_type == ExecTrialMachineType.Colab:
            await self._prepare_colab_resource()
            await self._exec_trial_in_colab()
        elif machine_type == ExecTrialMachineType.Local:
            await self._prepare_trial_local_resource()
            await self._exec_trial_in_local()
        else:
            raise NotImplementedError

        b_trial_timeout = False
        try:
            await asyncio.wait_for(self._trial_finished_future, HPOTrialPodSideEnv.get_trial_max_timeout_secs(machine_type))
        except asyncio.TimeoutError as err:
            b_trial_timeout = True

        if machine_type == ExecTrialMachineType.Local:
            await self._stop_trial_in_local()
        elif machine_type == ExecTrialMachineType.Colab:
            await self._stop_trial_in_colab()

        logger.info(
            f"Trial({self.cfg_hash}) finished , now sleep {HPOTrialPodSideEnv.SAFETY_SECONDS_4_ASYNC_OPERATIONS_TO_FINISH} secs")
        await asyncio.sleep(HPOTrialPodSideEnv.SAFETY_SECONDS_4_ASYNC_OPERATIONS_TO_FINISH)
        logger.info(f"after sleep for safety. trial {self.trial_uuid} finished!")

        # 超时以后，直接抛出异常，以便于下一个 trial 能够发出去
        if b_trial_timeout:
            run_secs = 0.0
            start_t = getattr(self, "_trial_start_time", None)
            if start_t is not None:
                run_secs = (datetime.now() - start_t).total_seconds()
            err_msg = f"Trial '{self.trial_uuid}' is timeout , has run {run_secs} secs "
            logger.error(err_msg)
            raise RuntimeError(err_msg)

    # ---- [laigen 2020.02.29] colab train 不再通过 kafka 进行，这里先去掉。  ----
    # @state_var_change_handler(state_vars=TrialColabSideEnv.intermediate_metrics, state_var_source=trial_colab_env)
    # @pick_one_change
    # async def on_intermediate_metrics(self, state_var_owner_pk: Any, state_var_name: str, metrics: Mapping[str, Any]):
    #     logger.info(f"report_intermediate_result:{metrics}")
    #     if os.getenv(ENV_KEY_TRIAL_IN_NNI, None):
    #         nni.report_intermediate_result(metrics)  # 目前测试阶段，还不能调用 nni 的接口
    #
    # @state_var_change_handler(state_vars=TrialColabSideEnv.final_metrics, state_var_source=trial_colab_env)
    # @pick_one_change
    # async def on_final_metrics(self, state_var_owner_pk: Any, state_var_name: str, metrics: Mapping[str, Any]):
    #     logger.info(f"report_final_result:{metrics}")
    #     if os.getenv(ENV_KEY_TRIAL_IN_NNI, None):
    #         nni.report_final_result(metrics)
    #     self._trial_finished_future.set_result(metrics)
    # ---- end ----

    # @timer(interval=10.)
    # async def print_running_log(self):
    #     start_t = getattr(self, "_trial_start_time", None)
    #     if start_t is None:
    #         logger.info(f"Trial({self.cfg_hash}) is not started!")
    #     else:
    #         logger.info(f"Trial({self.cfg_hash}) has started {(datetime.now() - start_t).total_seconds()} secs")

    @timer(interval=300.)
    async def query_trial_metrics(self):
        start_t = getattr(self, "_trial_start_time", None)
        if start_t is None:
            logger.info(f"Trial({self.cfg_hash}) is not started!")
        else:
            logger.info(f"Trial({self.cfg_hash}) has started {(datetime.now() - start_t).total_seconds()} secs")

        curr_latest_epoch, intermediate_metrics, final_val = self.metrics_reporter.query_metrics(self.latest_epoch)
        if curr_latest_epoch is None:
            return
        if curr_latest_epoch is not None and intermediate_metrics is not None:
            for metrics in intermediate_metrics:
                logger.info(f"report_intermediate_result:{metrics}")
                if os.getenv(ENV_KEY_TRIAL_IN_NNI, None):
                    nni.report_intermediate_result(metrics)  # 目前测试阶段，还不能调用 nni 的接口
            self.latest_epoch = curr_latest_epoch
        if final_val is not None and self.final_val is None:  # 第一次读取到 final val
            self.final_val = final_val
            logger.info(f"report_final_result:{self.final_val}")
            if os.getenv(ENV_KEY_TRIAL_IN_NNI, None):
                nni.report_final_result(self.final_val)
            self._trial_finished_future.set_result(self.final_val)


async def start_trial_env(env, vm_type: int):
    await env.start()
    await env.start_trial(vm_type)
    logger.info(f"after env.start_trial(vm_type)")
    await env.stop()
    logger.info(f"after env.stop")
    # await asyncio.sleep(30.)  # 留给 env stop 的处理
    # logger.info(f"after sleep in start_trial_env")
    # import sys
    # sys.exit(0)  # 不知道为什么 colab 的 trial 一直无法退出，这里强制结束
    # logger.info(f"after sys.exit(0)")


if __name__ == '__main__':
    import sys
    import os

    parser = argparse.ArgumentParser(prog="nni_trial")
    parser.add_argument("-c", "--cfg", nargs=None, type=str, required=True,
                        help="default workflow yml file of trial, file name in '[proj]/samples/wrokflow_cfg/xxx.yml file' , start from proj root")

    parser.add_argument("-p", "--pool", nargs=None, type=str, required=True, help="used google account pool name")
    parser.add_argument("-n", "--name", nargs=None, type=str, default="smoke_test", required=False, help="experiment name")
    parser.add_argument("-t", "--test", nargs=None, type=int, default=0, required=False, help="is smoke test")
    parser.add_argument("-m", "--vm", nargs=None, type=int, default=ExecTrialMachineType.Local.value, required=False,
                        help="vm type")
    parser.add_argument("-a", "--cfg_alias", nargs=None, type=str, default="", required=False,
                        help="step config alias class")
    args = parser.parse_args(sys.argv[1:])
    smoke_test = True
    params = dict()
    trial_uuid = ""
    experiment_id = ""
    cfg_alias_cls = None
    if args.cfg_alias:  # 有 alias 定义的 trial，对 cfg 的内容做一个映射
        cfg_alias_cls = str_to_cls(args.cfg_alias)

    if args.test:
        params["model.depth"] = 4
        # params["gs_research_workflow.time_series.gs_steps.model_steps:FitStep > epochs "] = 1
        # params["gs_research_workflow.time_series.gs_steps.model_steps:FitStep > steps_per_epoch "] = 1
        # params["gs_research_workflow.time_series.gs_steps.model_steps:FitStep > validation_steps "] = 1
        # params["gs_research_workflow.time_series.models.inception_time:InceptionTime.HP > depth"] = 5
        # params["gs_research_workflow.time_series.models.inception_time:InceptionTime.HP > use_residual"] = True
        if cfg_alias_cls:
            params = {cfg_alias_cls.get_cfg_loc(k): v for k, v in params.items()}
        trial_uuid = generate_uuid()
        experiment_id = generate_uuid()
    else:
        os.environ[ENV_KEY_TRIAL_IN_NNI] = "1"
        params = nni.get_next_parameter()
        experiment_id = nni.get_experiment_id()
        trial_uuid = nni.get_trial_id()
        if cfg_alias_cls:
            params = {cfg_alias_cls.get_cfg_loc(k): v for k, v in params.items()}
    # 对 item 进行 unescape
    params = {k: unescape_nni_choice_item(v) for k, v in params.items()}

    yml_path = os.path.join(os.path.dirname(__file__), "../../..", args.cfg)
    if not os.path.isfile(yml_path):
        logger.error(f"Default cfg file {yml_path} is not existed!")
        sys.exit(0)

    trial_task = HPOTrialPodSideEnv(args.name, yml_path, params, trial_uuid, experiment_id)
    trial_task.bind(topic_define=topic_gs_nni_trial)

    # ---- [laigen 2020.02.29] colab train 不再通过 kafka 进行，这里先去掉。  ----
    # trial_task.trial_colab_env.bind(trial_task.colab_side_env_pk, topic_define=topic_gs_nni_trial)
    # ----
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_trial_env(trial_task, args.vm))
    logger.info("after loop.run_until_complete")
    # sys.exit(0)
