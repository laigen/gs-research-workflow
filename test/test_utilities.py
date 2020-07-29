# -*- coding: utf-8 -*-

from gs_research_workflow.common.serialization_utilities import load_mapping_from_file, escape_nni_choice_item, \
    unescape_nni_choice_item
from gs_research_workflow.core.gs_step import upsert_step_cfg_para, lookup_step_cfg_para
from gs_research_workflow.auto_ml.loc_alias.step_cfg_loc_alias import InceptionCategoryDefaultAlias

if __name__ == "__main__":
    import os
    from gs_research_workflow.samples import workflow_cfg

    sample_file_path = os.path.join(os.path.dirname(workflow_cfg.__file__), "inception_category_workflow_v1.yml")
    workflow_cfg, step_local = load_mapping_from_file(sample_file_path)
    # print(json.dumps(workflow_cfg))
    # workflow_cfg["gs_research_workflow.time_series.gs_steps.tf_train_steps:TFTrainStep"]\
    #     ["#model_init_hp,model_cls#"]\
    #     ["gs_research_workflow.time_series.gs_steps.model_steps:TFModelStep"]\
    #     ["model_hp"]\
    #     ["gs_research_workflow.time_series.models.inception_time:InceptionTime.HP"]\
    #     ["depth"] = 6
    para_location1 = "gs_research_workflow.time_series.models.inception_time:InceptionTime.HP>nb_classes"
    para_location2 = "gs_research_workflow.time_series.models.inception_time:InceptionTime.HP>inception_block_hp>gs_research_workflow.time_series.models.inception_time:InceptionBlock.HP>stride"
    para_location3 = "gs_research_workflow.time_series.models.inception_time:InceptionTime.HP>inception_block_hp>gs_research_workflow.time_series.models.inception_time:InceptionBlock.HP"

    print(lookup_step_cfg_para(workflow_cfg,"#orig_data#>gs_research_workflow.time_series.gs_steps.ts_data_steps:SymbolTSStep>symbols"))
    print(lookup_step_cfg_para(workflow_cfg,"#x_get_data_callable#>gs_research_workflow.time_series.gs_steps.ts_data_steps:SymbolTSStep>cols"))
    print(lookup_step_cfg_para(workflow_cfg,
                               "#x_get_data_callable#>gs_research_workflow.time_series.gs_steps.ts_data_steps:SymbolTSStep>api"))
    print(lookup_step_cfg_para(workflow_cfg, InceptionCategoryDefaultAlias.get_cfg_loc("data.y_categories")))
    v = escape_nni_choice_item(lookup_step_cfg_para(workflow_cfg, InceptionCategoryDefaultAlias.get_cfg_loc("data.y_categories")))
    print(f"escape:{v}")
    print(f"unescape:{unescape_nni_choice_item(v)}")

    affected_items = upsert_step_cfg_para(workflow_cfg, para_location1, 444)
    affected_items += upsert_step_cfg_para(workflow_cfg, para_location2, 444)
    affected_items += upsert_step_cfg_para(workflow_cfg, para_location3, 444)

    para_local_location = "LOCAL>test_ds_pip"
    local_items_change = upsert_step_cfg_para(step_local, para_local_location, "8959")

    import yaml

    # print(yaml.dump(workflow_cfg))
    print(yaml.dump(step_local))
    print(f"{local_items_change} items changed")
