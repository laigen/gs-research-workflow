# -*- coding: UTF-8 -*-
from typing import List

from gs_research_workflow.time_series.envs.jy_data_extract_env import JYDBManipulationEnv, TestTSDataGenerator, \
    TestTFDatePipline
import tensorflow as tf


def test_convert_to_arctic():
    env = JYDBManipulationEnv()
    # env.convert_a_share_mkt_history_data()
    # env.load_all_close_price()
    # env.save_to_arctic()
    # env.read_all_data_from_arctic()
    # env.save_to_arctic_v2()
    # env.read_all_data_from_arctic_v2()
    # env.save_to_arctic_tickstore()
    # env.save_to_chunkstore()
    # env.save_to_chunkstore_per_symbol()
    # env.read_from_chunkstore()
    # env.show_chunk_store_info()
    # env.convert_period_equity_mkt_data_to_arctic()
    # env.convert_mkt_history_data()
    env.test_tf_data()


def test_tf_data_pipline():
    test_pipline = TestTFDatePipline()
    test_pipline.ds_pipline()

if __name__ == "__main__":
    # test_convert_to_arctic()
    test_tf_data_pipline()
