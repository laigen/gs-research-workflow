# -*- coding: UTF-8 -*-
from gs_research_workflow.time_series.tf_data_generators.discarded_index_prediction import SampleTushareDataGenerator, \
    SamplePricePrediction


def price_prediction():
    sample_pipline = SamplePricePrediction()
    sample_pipline.run_pipline()


if __name__ == "__main__":
    price_prediction()
