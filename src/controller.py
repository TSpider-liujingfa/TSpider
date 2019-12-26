# !/usr/bin/python3
# -*- coding: utf-8 -*-

__all__ = (
    'ProcessorController',
    'ParserController'
)

import random
import asyncio
from abc import ABCMeta
from collections import abc
from src.item import Task, Result
from src.pipeline import Pipeline

# 基础控制器
class BaseController(Pipeline, metaclass=ABCMeta):
    def __init__(self, spider, input_queue, output_queue, components):
        self.spider = spider
        self.input_queue = input_queue
        self.output_queue = output_queue
        super().__init__(components)

    # 执行任务
    async def run(self):
        while not self.input_queue.done() or not self.output_queue.done():
            while not self.input_queue.empty():
                item = await self.input_queue.get()
                default_result = self.get_default_result(item)
                result = await self.pipeline(item, default_result)
                self.output_queue.put(result)
                self.input_queue.done(item)
            await asyncio.sleep(random.random())

    # 获取默认结果
    def get_default_result(self, item):
        return item

# 处理控制器
class ProcessorController(BaseController):
    def get_default_result(self, task):
        return Result(task)

    # 控制结果必为Result对象
    def result_handler(self, pre_result, result):
        if isinstance(result, Result):
            pre_result = result
        return pre_result

# 解析控制器 
class ParserController(BaseController):
    def get_default_result(self, result):
        return []

    # 控制结果必为Task列表
    def result_handler(self, pre_result, result):
        if isinstance(result, Task):
            pre_result.append(result)
        elif isinstance(result, abc.Iterable):
            for task in result:
                pre_result = self.result_handler(pre_result, task)
        return pre_result