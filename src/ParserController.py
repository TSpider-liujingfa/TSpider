# !/usr/bin/python3
# -*- coding: utf-8 -*-

from collections import abc
from src.items import Task
from src.controller import BaseController

class ParserController(BaseController):
    def result_handler(self, pre_result, result):
        if isinstance(result, Task):
            pre_result.append(result)
        elif isinstance(result, abc.Iterator):
            for task in result:
                self.result_handler(pre_result, task)
        else:
            print(result)
        return pre_result

    # 解析结果
    def parse(self, result, queue=None):
        if queue is None:
            queue = self.spider.queue
        new_tasks = self.pipeline(result, default_result=[])
        for task in new_tasks:
            queue.put(task)