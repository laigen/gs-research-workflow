# -*- coding: utf-8 -*-

"""
copy from https://github.com/algrebe/python-tee/blob/master/tee/tee.py

改动的部分：
1) 输出的日志，加上了时间戳(支持时区)
"""

import os
import sys
from abc import ABCMeta, abstractmethod
from datetime import datetime

import pytz


class Tee(object):
    """
    duplicates streams to a file.
    credits : http://stackoverflow.com/q/616645
    """

    def __init__(self, filename, mode="a", buff=1, timezone="Asia/Shanghai", file_filters=None, stream_filters=None):
        """
        writes both to stream and to file.
        file_filters is a list of callables that processes a string just before being written
        to the file.
        stream_filters is a list of callables that processes a string just before being written
        to the stream.
        both stream & filefilters must return a string or None.
        """
        self.filename = filename
        self.mode = mode
        self.buff = buff
        self.file_filters = file_filters or []
        self.stream_filters = stream_filters or []
        self.tz = pytz.timezone(timezone)

        self.stream = None
        self.fp = None

    @abstractmethod
    def set_stream(self, stream):
        """
        assigns "stream" to some global variable e.g. sys.stdout
        """
        pass

    @abstractmethod
    def get_stream(self):
        """
        returns the original stream e.g. sys.stdout
        """
        pass

    def write(self, message):
        stream_message = message
        for f in self.stream_filters:
            stream_message = f(stream_message)
            if stream_message is None:
                break

        file_message = message
        for f in self.file_filters:
            file_message = f(file_message)
            if file_message is None:
                break

        if stream_message is not None:
            self.stream.write(stream_message)

        if file_message is not None:
            now_t = datetime.now(tz=self.tz).strftime('%Y%m%d_%H%M%S')
            self.fp.write(f"[{now_t}]" + file_message)

    def flush(self):
        self.stream.flush()
        self.fp.flush()
        os.fsync(self.fp.fileno())

    def __enter__(self):
        self.stream = self.get_stream()
        self.fp = open(self.filename, self.mode, self.buff)
        self.set_stream(self)

    def __exit__(self, *args):
        self.close()

    def __del__(self):
        self.close()

    def close(self):
        if self.stream is not None:
            self.set_stream(self.stream)
            self.stream = None

        if self.fp is not None:
            self.fp.close()
            self.fp = None

    def isatty(self):
        return self.stream.isatty()

    def __repr__(self):
        return "<%s: %s>" % (self.__class__.__name__, self.filename)

    __str__ = __repr__
    __unicode__ = __repr__


class StdoutTee(Tee):
    def set_stream(self, stream):
        sys.stdout = stream

    def get_stream(self):
        return sys.stdout


class StderrTee(Tee):
    def set_stream(self, stream):
        sys.stderr = stream

    def get_stream(self):
        return sys.stderr
