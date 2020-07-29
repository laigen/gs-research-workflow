# -*- coding: utf-8 -*-

import tensorflow as tf

from gs_research_workflow.samples.time_series_prediction.weather_data_envs import WeatherDataEnv
import logging
import os
from gs_research_workflow.samples.time_series_prediction.weather_data_predictor import WeatherDataPredictor

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [%(name)s,line:%(lineno)d] - %(levelname)s - %(message)s')

os.environ["http_proxy"] = "http://proxy.graphstrategist.com:8000/"
os.environ["https_proxy"] = "http://proxy.graphstrategist.com:8000/"


def test_tf():
    print(tf.__version__)


def test_env():
    env = WeatherDataEnv()
    env._read_data_from_original_source()
    env._prepare_xy()


def test_agent():
    agent = WeatherDataPredictor(predict_mode=False)
    agent.train_flow()


if __name__ == "__main__":
    # test_tf()
    # test_env()
    test_agent()
