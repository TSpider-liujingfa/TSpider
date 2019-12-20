# !/usr/bin/python3
# -*- coding: utf-8 -*-

from queue import Queue
from collections import abc
from src.items import Task
from src.controller import BaseController
from src.exceptions import EmptyError

class QueueController(BaseController):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.count = 0
        self.pre_tasks = [] # 预备任务
        self.tasks = Queue() # 准备要进行的任务

    def result_handler(self, pre_result, result):
        if isinstance(result, Task):
            pre_result.append(result)
        elif isinstance(result, abc.Iterator):
            pre_result += list(result)
        else:
            print(result)
        return pre_result

    def _get(self):
        if self.empty():
            raise EmptyError()

        if self.tasks.empty():
            tasks = self.pipeline(self.pre_tasks, default_result=[])
            if len(tasks) == 0:
                self.tasks.put(self.pre_tasks.pop(0))
            else:
                for task in tasks:
                    self.tasks.put(task)
                    self.pre_tasks.remove(task)
            return self._get()
        else:
            return self.tasks.get()

    # 队列是否为空
    def empty(self):
        return self.count == 0

    # 获取一个任务
    def get(self):
        task = self._get()
        self.count -= 1
        return task

    # 添加一个任务
    def put(self, task):
        self.pre_tasks.append(task)
        self.count += 1