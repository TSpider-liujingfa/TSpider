# !/usr/bin/python3
# -*- coding: utf-8 -*-

class BaseItem:
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

    def copy(self):
        return self.__class__(self.data.copy(), self.meta.copy())

class Task(BaseItem):
    pass

class Result(BaseItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setTask(self, task):
        self.task = task