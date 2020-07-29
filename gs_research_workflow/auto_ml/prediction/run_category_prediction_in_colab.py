# -*- coding: UTF-8 -*-

"""
    启动在colab上运行prediction的过程
"""


import logging
from typing import Mapping

import tempfile
from gs_framework.instance_hash_calculation import HashCalculation
from gs_framework.utilities import md5_str

from gs_research_workflow.common.path_utilities import get_prediction_cfg_path
from gs_research_workflow.core.gs_step import upsert_step_cfg_para

from gs_research_workflow.auto_ml.notebook.colab_notebook_generator import notebook_by_replace_one_cell

from gs_research_workflow.common.serialization_utilities import save_mapping_to_file_or_stream, load_mapping_from_file

from gs_research_workflow.common.google_drive import GoogleDriveWrapper, MIME_FOLDER, MIME_COLAB

from gs_research_workflow.common.google_oauth import get_google_token

logger = logging.getLogger(__name__)


# NOTE:是否要变成一个 Env 暂时还未确定
class RunPredictionInColab:

    def __init__(self, model_name: str, model_inst_gid: str, template_workflow_yml_file: str, changed_params: Mapping,
                 pred_name: str):
        super().__init__()
        self._model_name = model_name
        self._model_inst_gid = model_inst_gid
        self._pred_name = pred_name
        self.workflow_cfg, self.workflow_context = load_mapping_from_file(template_workflow_yml_file)

        for k, v in changed_params.items():
            changed_items = upsert_step_cfg_para(self.workflow_cfg, self.workflow_context, k, v)
            if changed_items == 0:
                logger.error(f"'{k}' is not available in config setting , should check changed_params file")
        self.cfg_hash = md5_str(HashCalculation.value_to_hash_str(self.workflow_cfg))

    CELL_CODE_RUN_PRED = """# GS --max-run-seconds=36000
from gs_research_workflow.auto_ml.prediction.run_category_prediction import run_category_prediction
import logging
logging.getLogger('').addHandler(logging.FileHandler('/tmp/colab_prediction.log'))
df = run_category_prediction("{model_name}", "{model_inst_gid}", "{workflow_cfg_path}", "{pred_name}")
print(df)"""

    def _run_pred_cell_code(self, cfg_file: str) -> str:
        return RunPredictionInColab.CELL_CODE_RUN_PRED.format(model_name=self._model_name,
                                                              model_inst_gid=self._model_inst_gid,
                                                              workflow_cfg_path=cfg_file,
                                                              pred_name=self._pred_name)

    def _prepare_colab_resource(self):
        # 检查路径
        # Google Drive Location
        # GS/SYS_MODEL_PREDICTION/[MODEL_NAME]/notebooks/[model_inst_gid]_[pred_name].ipynb
        # GS/SYS_MODEL_PREDICTION/[MODEL_NAME]/workflow_cfg/[cfg_hash].yml

        token = get_google_token()
        gdrive = GoogleDriveWrapper(token)

        pred_folder_obj = gdrive.create_or_update_file(self._model_name, MIME_FOLDER, "GS/SYS_MODEL_PREDICTION")
        nb_folder_obj = gdrive.create_or_update_file("notebooks", MIME_FOLDER, pred_folder_obj)
        cfg_folder_obj = gdrive.create_or_update_file("workflow_cfg", MIME_FOLDER, pred_folder_obj)

        with tempfile.NamedTemporaryFile("w", suffix=".yml", delete=False) as f:
            save_mapping_to_file_or_stream(f, self.workflow_cfg, self.workflow_context)
            yaml_path = f.name
        yml_gfile = gdrive.create_or_update_file(f"{self.cfg_hash}.yml", None, cfg_folder_obj, yaml_path)
        logger.info(f"yml file is created on google drive {yml_gfile}")

        colab_file_path = notebook_by_replace_one_cell(template_file_name='colab_template', cell_idx=4,
                                                       new_code=self._run_pred_cell_code(
                                                           cfg_file=get_prediction_cfg_path(self._model_name,
                                                                                            self.cfg_hash)),
                                                       new_nb_name=f"{self._model_inst_gid}_{self._pred_name}.ipynb")

        colab_gfile = gdrive.create_or_update_file(f"{self._model_inst_gid}_{self._pred_name}.ipynb", MIME_COLAB,
                                                   nb_folder_obj, colab_file_path)
        logger.info(f"colab notebook file is created on google drive {colab_gfile}")
        self.notebook_file_id = colab_gfile.id

    def _exec_pred_in_colab(self):
        # TODO:调用 google account pool 的 rpc 接口，将 colab 跑起来
        logger.info(
            f"Open web browser and run notebook in url: https://colab.research.google.com/drive/{self.notebook_file_id}")

    def run(self):
        self._prepare_colab_resource()
        self._exec_pred_in_colab()


if __name__ == "__main__":
    import os
    cfg_path = os.path.join(os.path.dirname(__file__), "../..",
                            "samples/workflow_cfg/category_prediction_ds_workflow_v1.yml")

    do_pred = RunPredictionInColab("InceptionTime", "AD7616E186C84B233972DBF509AEA638", cfg_path, {}, "SSHMarketCap")
    do_pred.run()

