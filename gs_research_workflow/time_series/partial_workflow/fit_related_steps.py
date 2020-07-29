# -*- coding: UTF-8 -*-

"""与fit有关的step对象"""
from typing import List

from gs_research_workflow.time_series.gs_steps.model_steps import FitStep, ModelCheckPointStep, TensorBoardStep, \
    EarlyStoppingStep, CompileStep

from gs_research_workflow.core.gs_step import GSStep


def get_category_compile_step(optimizer: str = "Adam") -> CompileStep:
    compile_step = CompileStep(loss="categorical_crossentropy", optimizer=optimizer,
                               # 注意:第一位的是作为 eval step 进行 final report 的 metrics
                               str_metrics=["categorical_accuracy",
                                            # for cls_to_str(tf.keras.metrics.CategoricalAccuracy),
                                            # "accuracy",  # for cls_to_str(tf.keras.metrics.Accuracy), Note :accuracy 在这里就是 categorical_accuracy
                                            "categorical_crossentropy",
                                            # for cls_to_str(tf.keras.metrics.CategoricalCrossentropy),
                                            "categorical_hinge"  # for cls_to_str(tf.keras.metrics.CategoricalHinge),
                                            ])
    return compile_step


def get_compile_step(loss: str = "mae", optimizer: str = "Adam", metrics: List[str] = ["mae", "mse"]) -> CompileStep:
    compile_step = CompileStep(loss=loss, optimizer=optimizer,
                               # 注意:第一位的是作为 eval step 进行 final report 的 metrics
                               str_metrics=metrics)
    return compile_step


def get_recommend_fit_with_callback_steps(epochs: int = 10, steps_per_epoch: int = 1000, validation_steps: int = 300) \
        -> List[GSStep]:
    fit_step = FitStep(epochs=epochs, steps_per_epoch=steps_per_epoch, validation_steps=validation_steps)
    checkpoint_step = ModelCheckPointStep(save_best_only=True, verbose=1, save_weights_only=False)
    tensor_board_step = TensorBoardStep(write_graph=False)
    early_stop_step = EarlyStoppingStep(monitor="val_loss", patience=3)
    return [fit_step, checkpoint_step, tensor_board_step, early_stop_step]
