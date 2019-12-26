# !/usr/bin/python3
# -*- coding: utf-8 -*-

import asyncio
import settings
import src.settings as default_settings
from src.queue import TaskQueue, ResultQueue
from src.controller import ProcessorController, ParserController

# 配置文件处理
class Setting:
    def __init__(self, _settings, _default_settings):
        self._settings = _settings
        self._default_settings = _default_settings
    
    def __getattr__(self, attr):
        default = getattr(self._default_settings, attr)
        return getattr(self._settings, attr, default)

# 主控对象
class TSpider:
    _settings = Setting(settings, default_settings)

    def __init__(self):
        self.task_queue = TaskQueue(self, self._settings.TASK_QUEUE_COMPONENT)
        self.result_queue = ResultQueue(self, self._settings.RESULT_QUEUE_COMPONENT)
        self.processor = ProcessorController(self, self.task_queue, self.result_queue, self._settings.PROCESSOR_COMPONENT)
        self.parser = ParserController(self, self.result_queue, self.task_queue, self._settings.PARSER_COMPONENT)

    # 开始任务
    # start_task(Task or list(Task))
    def start(self, start_task):
        self.task_queue.put(start_task)
        coroutine = [self.processor.run() for i in range(self._settings.PROCESSOR_COUNT)]
        coroutine += [self.parser.run() for i in range(self._settings.PARSER_COUNT)]
        asyncio.run(asyncio.wait(coroutine))