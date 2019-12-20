# !/usr/bin/python3
# -*- coding: utf-8 -*-

# 仅用作参考

import time
from src.interfaces import ProcessComponentInterface
from src.interfaces import ParserComponentInterface
from src.interfaces import QueueComponentInterface
from src.items import Task, Result

class BaseProcessorComponent(ProcessComponentInterface):
    def handler(self, task, result, controller):
        time.sleep(0.5)
        return Result(result=task.number+1)

class BaseParserComponent(ParserComponentInterface):
    def handler(self, result, new_tasks, controller):
        if result.result <= 10:
            yield Task(number=result.result)
        yield '任务已完成，参数number=%d，结果result=%d' % (result.task.number, result.result)

        
class BaseQueueComponent(QueueComponentInterface):
    def handler(self, pre_tasks, tasks, controller):
        return pre_tasks[-1]
