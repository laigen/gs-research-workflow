# -*- coding: UTF-8 -*-
from datetime import date
from typing import List, Type, Any, Callable, Set, Mapping, Tuple

from dataclasses import dataclass, field, Field
import pandas as pd
import tensorflow as tf
from gs_research_workflow.core.gs_step import GSStep, PropFieldMapping

from gs_research_workflow.time_series.data.tushare_wrapper import TuShareProData

from gs_research_workflow.core.dataclass_utilities import find_field_in_dataclass


def register_field_property_mapping(from_cls, to_cls, same_name_mapping: Set[Field],
                                    prop_field_mapping: Mapping[Callable, Field]):
    """
    注册两个 dataclass 之间的映射关系
    """
    pass


def init_fields_from_dataclass(inst, to_cls) -> Mapping: ...


@dataclass
class TSDataFromTushare(GSStep):
    func_name: str
    symbol: str
    start_t: date = None
    end_t: date = None
    cols: List[str] = None

    def __post_init__(self):
        # todo: init tushare query object
        self._tushare = TuShareProData()

    @property
    def ts_data(self) -> pd.DataFrame:
        return getattr(self._tushare, self.func_name)(self.symbol, self.start_t, self.end_t, self.cols)


@dataclass
class TrainValSplit(GSStep):
    data: pd.DataFrame = field(init=True)
    split_ratio: float = 0.9

    def __post_init__(self):
        # TODO: shuffle self.data
        pass

    @property
    def training_set(self):
        return self.data.iloc[0:self.split_ratio * len(self.data)]

    @property
    def val_set(self):
        return self.data.iloc[self.split_ratio * len(self.data):]

# 参数关系绑定


class DataClassesFieldPropertyMapping:
    # all_mapping_data: Mapping[Tuple[Type, Type], PropFieldMapping]

    class DataContainer:
        data = Mapping[Tuple[Type, Type], PropFieldMapping]
    _data = DataContainer()

    @classmethod
    def register(cls, from_cls: Type, to_cls: Type, same_name_prop_field_mapping: Set[Field],
                 different_name_prop_field_mapping: Mapping[Callable, Field]):
        ...



DataClassesFieldPropertyMapping.register(from_cls=TSDataFromTushare, to_cls=TrainValSplit, same_name_mapping=None,
                                         prop_field_mapping={TSDataFromTushare.ts_data: TrainValSplit.data})



# NOTE: TrainValSplit.split_ratio 需要另外传入，不在 pipline 上

@dataclass
class TrainValDatasetPipline(GSStep):
    ori_training_set: pd.DataFrame
    ori_val_set: pd.DataFrame
    f_data_preprocess: Callable[[tf.data.Dataset], tf.data.Dataset]
    training_batch_size: int = 10
    val_batch_size: int = 10

    def __post_init__(self):
        # todo , tf.data.from_tensor_slices 得到 dataset 对象
        pass

    @property
    def training_set(self): ...

    @property
    def val_set(self): ...


DataClassesFieldPropertyMapping.register(from_cls=TrainValSplit, to_cls=TrainValDatasetPipline, same_name_mapping=None,
                                         prop_field_mapping={
                                             TrainValDatasetPipline.ori_training_set: TrainValSplit.training_set,
                                             TrainValDatasetPipline.ori_val_set: TrainValSplit.val_set})

# 以下的实例化方法，将能够被 json 化
# 虽然看上去复杂，但是 recursive 的
TrainValDatasetPipline(
    **dict(
        init_fields_from_dataclass(TrainValSplit(
            **dict(
                init_fields_from_dataclass(TSDataFromTushare(**dict(
                    func_name="index_quotation_daily",
                    symbol="000001.SH",
                )), TrainValSplit),
                **dict(
                    split_ratio=0.85,
                )
            )
        ), TrainValDatasetPipline),
        **dict(
            f_data_preprocess=lambda ds: ds.repeat(),
            training_batch_size=10,
            val_batch_size=10,
        )
    )
)

# NOTE: dictionary concatenate 的简化版写法 dict( dict_a , **dict_b , **dict_c)

with InitParaFlowTape() as flow_tape:
    ts_training_data = TSDataFromTushare(func_name="index_quotation_daily", symbol="000001.SH")
    train_val_split = TrainValSplit(split_ratio=0.85, **ts_training_data.map_to_kwargs(TrainValSplit))
    train_val_tf_ds = TrainValDatasetPipline(f_data_preprocess=lambda ds: ds.repeat(),
                                             training_batch_size=10,
                                             val_batch_size=10, **train_val_split.map_to_kwargs(TrainValDatasetPipline))

    # ts_training_data = TSDataFromTushare, func_name="index_quotation_daily", symbol="000001.SH")
    # ts_training_data = create_inst(TSDataFromTushare,func_name="index_quotation_daily", symbol="000001.SH")
    # train_val_split = create_inst(TrainValSplit,ts_training_data,split_ratio=0.85)
    # train_val_tf_ds = create_inst(TrainValDatasetPipline,train_val_split,f_data_preprocess=lambda ds: ds.repeat(),
    #                                          training_batch_size=10,
    #                                          val_batch_size=10)

calc_flow_dict = flow_tape.as_dict()

# calc_flow_dict 的内容形如：
{
    "module:TrainValDatasetPipline": {
        "module:TrainValSplit": {
            "module:TSDataFromTushare": {"func_name": "index_quotation_daily", "symbol": "000001.SH"},
            "split_ratio": 0.85
        },
        "f_data_preprocess": "binary(lambda ds: ds.repeat())",
        "training_batch_size": 10,
        "val_batch_size": 10
    }
}




# ----- 以下部分先不要看 -----------



# NOTE: 基类是否是一个 dataclass 需要考虑一下（可能是以 Mixin 的方式整合）
class DataclassInitFieldsGenerator:
    """
    生成某一个 dataclass init fields 的 generator。

    Features include：
    基本功能：
    1) target fields (dictionary) generate.
        Eg:
        @dataclass
        class A:
            hp1:Any
            hp2:Any

        @dataclass
        AInitFieldsGenerator:
            @property
            def target_init_fields(self):
                return {"hp1":some_value,"hp2":some_value}

    2) fields transform
        Eg:
        @dataclass
        AInitFieldsGenerator:
            hp3:Any

            @property
            def target_init_fields(self):
                # means : {hp1,hp2} = some_deterministic_func({hp3})
                return {"hp1":func1(self.hp3),"hp2":func2(self.hp3)}

    additional feature：
    1) (在提供了 target dataclass 的情况下 )，检查 init_fields 是否与 target dataclass 匹配
        NOTE：在 target dataclass 修改了 init features 的时候，可以在 generator class 中就抛出错误。
                好处是，容易定位到不一致的环节，进行修改。一般是修改 InitFieldsGenerator.target_init_fields 的 key

    ----------- 以下部分不属于该类 class 的 feature ， 但可以用到该信息完成的功能 --------
    1) dataclass initial pipline (flow)
    2) (UI) recommend initial fields generator
    3) pre-define workflow 可以用 多个 DataclassInitFieldsGenerator(以 tree 型结构) 搭建
    """

    # dataclass 的基类不适合定义 required fields ， 所以在 field需要在派生类中定义，基类中做检查
    # target_cls: Type = None
    """ 目标生成的 dataclass 的类型 """

    # ls_init_fields_to_be_created: List[str] = []
    """ 会输出哪些 fields """

    def check_assumptions(self):
        """
        将做以下的一些检查:
        1) fields 中 'target_cls' 和 'ls_init_fields_to_be_created' 有值，将检查 这些 fields name 是否都在 target_cls 中，并且是 init 参数项
        """
        target_cls = getattr(self, "target_cls", None)
        init_fields_in_target = getattr(self, "ls_init_fields_to_be_created", None)
        if target_cls is not None and init_fields_in_target is not None and len(init_fields_in_target) > 0 :
            for field_name in init_fields_in_target:
                curr_field = find_field_in_dataclass(field_name, target_cls)
                assert curr_field is not None, f"{field_name} is not a field in {target_cls}"
                assert curr_field.init , f"{field_name} should be a init field in {target_cls}"

    # @property
    # def target_init_fields(self):
    #     raise NotImplementedError
