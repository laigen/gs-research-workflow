# -*- coding: UTF-8 -*-
"""
提供  category 相关的一些 steps generator 对象
"""

from gs_research_workflow.time_series.models.inception_time import InceptionBlock, \
    InceptionTimeForClassification, InceptionTimeBlock

from gs_research_workflow.common.serialization_utilities import cls_to_str

from gs_research_workflow.time_series.gs_steps.model_steps import TFModelStep
from gs_research_workflow.time_series.models.inception_time_with_attention import \
    InceptionTimeWithAttentionForWeightPrediction, InceptionTimeWithAttentionBlock
from gs_research_workflow.time_series.models.ts_bert import TSBertForWeightPrediction


def get_default_inception_model_classification_task_step(nb_classes: int) -> TFModelStep:
    model_step = TFModelStep(model_cls_str=cls_to_str(InceptionTimeForClassification),
                             model_hp=InceptionTimeForClassification.HP(nb_classes=nb_classes,
                                                                        inception_time_hp=InceptionTimeBlock.HP(
                                                                            depth=6, use_residual=True,
                                                                            inception_block_hp=InceptionBlock.HP(
                                                                                stride=1,
                                                                                use_bottleneck=True))))
    return model_step


def get_default_inception_with_attention_model_weight_prediction_task_step() -> TFModelStep:
    model_step = TFModelStep(model_cls_str=cls_to_str(InceptionTimeWithAttentionForWeightPrediction),
                             model_hp=InceptionTimeWithAttentionForWeightPrediction.HP(
                                 inception_attention_hp=InceptionTimeWithAttentionBlock.HP(
                                     depth=6, use_residual=True,
                                     use_attention_at_input=True,
                                     use_attention_at_each_inception=True,
                                     use_attention_after_residual=True,
                                     inception_block_hp=InceptionBlock.HP(stride=1, use_bottleneck=True)
                                 )
                             ))
    return model_step


def get_default_ts_bert_for_weight_prediction_task_step() -> TFModelStep:
    model_step = TFModelStep(model_cls_str=cls_to_str(TSBertForWeightPrediction),
                             model_hp=TSBertForWeightPrediction.HP(hidden_size=72)) # hidden_size 必须与 lookback_period 相同
    return model_step


# 这些 model 的 HP 都需要重新调整一下，先都注释掉
# def get_default_inception_with_attention_model_step(nb_classes: int) -> TFModelStep:
#     # TODO：根据数据结构，还需要进行调整
#     model_step = TFModelStep(model_cls_str=cls_to_str(InceptionTimeWithAttention),
#                              model_hp=InceptionTimeWithAttention.HP(nb_classes=nb_classes,
#                                                                     depth=6,
#                                                                     use_attention_at_input=True,
#                                                                     use_attention_at_each_inception=True,
#                                                                     use_attention_after_residual=True,
#                                                                     inception_block_hp=InceptionBlock.HP(stride=1)))
#     return model_step
#
#
# def get_default_simple_lstm_model_step(nb_classes: int) -> TFModelStep:
#     model_step = TFModelStep(model_cls_str=cls_to_str(SimpleLSTM),
#                              model_hp=SimpleLSTM.HP(nb_classes=nb_classes, lstm_units=8, l1_factor=0.01,
#                                                     l2_factor=0.01))
#     return model_step


