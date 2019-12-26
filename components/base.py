# !/usr/bin/python3
# -*- coding: utf-8 -*-

# 仅用作参考

import random
import asyncio
from src.item import Task
from src.component import Component, AsyncComponent

class BaseProcessorComponent(AsyncComponent):
    async def handler(self, task, result, controller):
        print('[+] %d号任务开始执行' % task.id)
        await asyncio.sleep(random.random() + 1)
        print('[+] %d号任务执行结束' % task.id)

class BaseParserComponent(Component):
    def handler(self, result, new_tasks, controller):
        print('[+] %d号任务结果开始解析' % result.task.id)
        if result.task.id < result.task._id + 9:
            yield Task(id=result.task.id+1, _id=result.task._id)
        print('[+] %d号任务结果解析结束' % result.task.id)