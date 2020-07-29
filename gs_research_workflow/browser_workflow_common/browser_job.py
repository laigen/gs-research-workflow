# -*- coding: utf-8 -*-

"""
平台指派给 Desktop Browser Env 的各类 job
"""
from datetime import datetime
from enum import Enum
from typing import NamedTuple, List, Tuple


class BrowserVisitUrlsJob(NamedTuple):
    """需要ChromeDesktopEnv将网页分别打开一次，dom load 完成之后即可关闭"""
    id: str = None
    """该 job 的唯一 id，用于状态沟通"""
    runner_env_id: str = None
    """执行这项 job 的 env 的 id"""
    urls_to_navi: List[Tuple[str, str]] = None
    """触发的url(比如：google scholar search 页面) 以及需要访问的 url (author detail) 列表"""
    new_window: bool = True
    """在新的window中完成该任务，目前只支持这一选项"""
    assigned_time: datetime = None
    """assign 任务的时间，避免历史的消息记录还在起作用"""


class ReOrganizeBrowserWindowJob(NamedTuple):
    """重新调整 window 和 tab 的排布任务"""
    # NOTE : 内容暂略，用于示意有多个 Job
    ...


class JobStatus(Enum):
    not_assigned = 0  # 任务还在 非 Chrome Desktop Env 一端，未分配出来
    waiting = 1
    processing = 2
    abort = 3
    pause = 4
    finish = 5


class BrowserJobStatus(NamedTuple):
    """Job的执行状态"""
    job_id: str = None
    """link to BrowserVisitUrlJob.id"""
    job_type: str = None
    """任务的类型，即 BrowserVisitUrlJob.module + BrowserVisitUrlJob.__qualname__ ，用于表示任务的类型"""
    status: JobStatus = None
    success_count: int = None
    fail_count: int = None
    remaining_count: int = None
    status_description: str = None
    """状态的描述，给人看的内容"""


class JobHeartBeats(NamedTuple):
    """任务的心跳包"""
    remain_jobs: List[str] = None
    """还有多少待处理的任务，job 的 id"""
    beats_ts: datetime = None
    """心跳的时间戳"""
    can_assign_jobs: bool = False
    """是否能够接受任务的指派"""
