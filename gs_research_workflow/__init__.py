# -*- coding: UTF-8 -*-

# 暂时为了方便，将 loging 的输出级别写在了 __init__ 中
# !!! 在 __init__ 中写 logging 的输出方式并不规范，应该是在后续具体的应用模块中设定。这里只是为了全局调试方便的一种临时方案
import logging

import os

_log_level = logging.INFO
_log_format = '%(asctime)s - [%(name)s,line:%(lineno)d] - %(levelname)s - %(message)s'

# 如果没有创建过 root logger 时， basicConfig 会起作用
logging.basicConfig(level=_log_level, format=_log_format)

# 创建了 root logger 时，需要进行修改
logging.getLogger('').setLevel(_log_level)  # 似乎 NNI 会创建一个 root logger ， 这里修改 root logger 的 level

# NNI 起作用时，还是需要注释掉，否则可能会出现错误
# formatter = logging.Formatter(_log_format)
# for handler in logging.getLogger('').handlers:
#     handler.setFormatter(formatter)

__all__ = ["browser_workflow_common", "common", "external_data", "time_series"]

# debug_level_modules = []
debug_level_modules = ["gs_research_workflow.time_series.data.arctic_and_local_cache", "__main__"]
for n in debug_level_modules:
    logging.getLogger(n).setLevel(logging.DEBUG)

os.environ["local_cache_expire_hours"] = str(24 * 7)  # 假定 training code 一周才更新一次数据

import pandas as pd
# 一些 列赋值写法会触发 false warning，这里暂时先关闭
pd.set_option('mode.chained_assignment', None)

# 系统缺少了时区的设置，这里补充一下时区为 东八区
import os
os.environ["TZ"] = "Asia/Shanghai"

