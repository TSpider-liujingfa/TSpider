# !/usr/bin/python3
# -*- coding: utf-8 -*-

import json
from abc import ABCMeta

class BaseItem(metaclass=ABCMeta):
    def __init__(self, data=None, meta=None, **kwargs):
        if data is None:
            data = {}
        if meta is None:
            meta = {}
        data.update(kwargs)
        self.data = data
        self.meta = meta

    def __getattr__(self, attr):
        return self.data[attr]

    def __str__(self):
        msg = self.__class__.__name__ + '('
        msg += ', '.join([key + '=' + str(value) for key, value in self.data.items()])
        return msg + ')'

    def copy(self):
        return self.__class__(self.data.copy(), self.meta.copy())

# 任务
class Task(BaseItem):
    pass

# 结果
class Result(BaseItem):
    def __init__(self, task, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.task = task