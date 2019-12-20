# !/usr/bin/python3
# -*- coding: utf-8 -*-

from collections import abc
from src.items import Result
from src.controller import BaseController

class ProcessorController(BaseController):
    def result_handler(self, pre_result, result):
        if isinstance(result, Result):
            return result
        else:
            return pre_result

    def process(self, parser=None, queue=None):
        if parser is None:
            parser = self.spider.parser
        if queue is None:
            queue = self.spider.queue
        task = queue.get()
        result = self.pipeline(task, default_result=Result())
        result.setTask(task)
        parser.parse(result, queue)