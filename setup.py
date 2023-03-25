# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages

setup(name='gs-research-workflow',
      version='0.1',
      description='GS Research Workflow',
      author='GS',
      packages=find_packages(exclude=['test', "test.*"]),
      install_requires=[
            'gs_framework',
            'dataset',
            'furl',
            'pyquery',
            'pymongo',
            'numpy',
            'pandas',
            'tensorflow==2.11.1',
            # "tf-nightly",
            # 'tf-nightly-2.0-preview',
            # "tf-nightly-gpu-2.0-preview", # 似乎不能用 gpu 版本的 tf-nightly
            # 'tensorflow-gpu',
            'sklearn',
            'matplotlib',
            'tensorflow_hub',
            'mysql-connector-python-rf',
            'tushare==1.2.51',  # ALERT tushare 1.2.52 版本会有错误，这里先固定在这个版本上
            'BeautifulSoup4',
            # 'zipline',
            # 'yfinance',
            'html5lib',
            'quandl',
            'alpha_vantage',
            'dataclasses',
            'pyyaml',
            "arctic",
            "diskcache",
            "nni",
            "nbformat",
            "google-api-python-client",
            "google-auth-httplib2",
            "google-auth-oauthlib",
            "transformers",  # huggingface transformers
            "mongoengine",  # 一些 nlp project 中，需要直接操作 Mongo ，用该 package 来提供 highlevel 的 mongo operation
            'dash==1.12.0',
            'plotly==4.6.0',
            'akshare',  # 品类数据非常全的财经数据数据库
            'dateparser',
            'pycld3',  # for language detection
            # ta-lib 暂不加入到 setup.py ， 可以在用到的地方单独进行 pip ， colab 中对于该项内容也是单独的 pip , 以便于在不需要 ta 的场景中也能使用 gs-research-workflow
            # "ta-lib", # 需按照链接先装 talib 的 库 https://medium.com/@artiya4u/installing-ta-lib-on-ubuntu-944d8ca24eae
            # allen NLP 的 依赖包比较大，这里手工部署环境的时候再安装，避免安装 desktop-env 的时候，会有太对的依赖项产生
            # 'allennlp==1.0.0', # pip install allennlp==1.0.0 -i https://mirrors.aliyun.com/pypi/simple/ --cache-dir '/gdrive/My Drive/GS/cache'
            # 'allennlp-models==1.0.0', # pip install allennlp-models==1.0.0 -i https://mirrors.aliyun.com/pypi/simple/ --cache-dir '/gdrive/My Drive/GS/cache'
      ],
      dependency_links=[
            #"git+https://github.com/keras-team/keras-tuner.git",
            #"git+https://github.com/gftgpu/yfinance.git",
            "https://github.com/manahl/arctic.git",
      ]
      )
