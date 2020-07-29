# -*- coding: UTF-8 -*-

import datetime


def local_timezone() -> datetime.tzinfo:
    import datetime
    return datetime.datetime.now(datetime.timezone(datetime.timedelta(0))).astimezone().tzinfo


def local_now() -> datetime.datetime:
    return datetime.datetime.now(local_timezone())
