# -*- coding: utf-8 -*-

"""
因为 step config 的 location 定义的名称包含有层级的定位关系，所以比较长。在 nni 的 ui 界面中，
    不容易看懂这个名称，所以用 static alias 的方式，将这个名称变得可读性更好一些

格式的规则为： Dict[str,str] ,
"""
from typing import Dict


class GSStepConfigAlias:
    """每个派生类都需要定义该对象，key = alias , value = location str in cfg file
        注意：Alias 中尽量不要出现 '>' 以免 location 的字符串与 alias 的字符串发生名称通途
    """
    alias_mapping: Dict[str, str] = None

    @classmethod
    def get_cfg_loc(cls, alias_or_loc: str):
        if alias_or_loc in cls.alias_mapping:
            return cls.alias_mapping[alias_or_loc]
        else:
            return alias_or_loc


class InceptionCategoryDefaultAlias(GSStepConfigAlias):
    alias_mapping = {
        "model.depth": "gs_research_workflow.time_series.models.inception_time:InceptionTimeBlock.HP > depth",
        "model.use_residual": "gs_research_workflow.time_series.models.inception_time:InceptionTimeBlock.HP > use_residual",
        "model.use_bottleneck": "inception_block_hp > gs_research_workflow.time_series.models.inception_time:InceptionBlock.HP > use_bottleneck",
        "data.y_categories": "LOCAL > category_labels",
        "data.x_features": "LOCAL > x_feature_columns",
        "data.x_api": "LOCAL > x_feature_from_api"
    }


class InceptionWithAttentionDefaultAlias(GSStepConfigAlias):
    alias_mapping = {
        "model.depth": "gs_research_workflow.time_series.models.inception_time_with_attention:InceptionTimeWithAttentionBlock.HP > depth",
        "model.use_residual": "gs_research_workflow.time_series.models.inception_time_with_attention:InceptionTimeWithAttentionBlock.HP > use_residual",
        "model.use_bottleneck": "inception_block_hp > gs_research_workflow.time_series.models.inception_time:InceptionBlock.HP > use_bottleneck",
        "model.attention_after_residual": "inception_attention_hp > gs_research_workflow.time_series.models.inception_time_with_attention:InceptionTimeWithAttentionBlock.HP > use_attention_after_residual",
        "model.attention_at_each_inception": "inception_attention_hp > gs_research_workflow.time_series.models.inception_time_with_attention:InceptionTimeWithAttentionBlock.HP > use_attention_at_each_inception",
        "model.attention_at_input": "inception_attention_hp > gs_research_workflow.time_series.models.inception_time_with_attention:InceptionTimeWithAttentionBlock.HP > use_attention_at_input",
    }


class TSBertForMaskedCSDefaultAlias(GSStepConfigAlias):
    alias_mapping = {
        "model.hidden_size": "model_hp > gs_research_workflow.time_series.models.ts_bert:TSBertForMaskedCS.HP > hidden_size",
        "model.num_attention_heads": "model_hp > gs_research_workflow.time_series.models.ts_bert:TSBertForMaskedCS.HP > num_attention_heads",
        "model.num_hidden_layers": "model_hp > gs_research_workflow.time_series.models.ts_bert:TSBertForMaskedCS.HP > num_hidden_layers",
    }