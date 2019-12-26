# !/usr/bin/python3
# -*- coding: utf-8 -*-

__all__ = (
    'TaskQueue',
    'ResultQueue'
)

import queue
from abc import ABCMeta
from collections import abc
from src.item import BaseItem
from src.pipeline import Pipeline
from src.exception import QueueEmptyError, QueueNoneExtractItemsError, QueueUnexpectedItemError

class BaseQueue(Pipeline, metaclass=ABCMeta):
    def __init__(self, spider, components=[]):
        self.spider = spider
        self.queue = queue.Queue()
        self.pre_items = []
        self.going_items = []
        self.count = 0
        self.going_count = 0
        super().__init__(components)

    def result_handler(self, pre_result, result):
        if isinstance(result, abc.Iterable) and len(result) > 0:
            for i in result:
                if not isinstance(i, BaseItem):
                    raise QueueNoneExtractItemsError()
            return result
        else:
            raise QueueNoneExtractItemsError()
    
    # 判断队列是否为空
    def empty(self):
        return self.count == 0

    # 获取一个Item
    async def get(self):
        if self.empty():
            raise QueueEmptyError()
        if self.queue.empty():
            items = await self.pipeline(self.pre_items.copy(), default_result=[self.pre_items[0]])
            for item in items:
                self.queue.put(item)
                self.pre_items.remove(item)
                self.going_items.append(item)
        self.count -= 1
        return self.queue.get()

    # 添加Item或list(Item)
    def put(self, item):
        if isinstance(item, BaseItem):
            self.pre_items.append(item)
            self.count += 1
            self.going_count += 1
        elif isinstance(item, abc.Iterable):
            for _item in item:
                self.put(_item)
        else:
            raise QueueUnexpectedItemError()

    # 任务已完成
    # item=None时检测当前队列所有任务是否已完成
    def done(self, item=None):
        if item is None:
            return self.going_count == 0
        else:
            try:
                self.going_items.remove(item)
                self.going_count -= 1
            except ValueError:
                raise QueueUnexpectedItemError()

class TaskQueue(BaseQueue):
    pass

class ResultQueue(BaseQueue):
    pass