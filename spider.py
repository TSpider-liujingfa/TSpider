# !/usr/bin/python3
# -*- coding: utf-8 -*-

from src.ProcessorController import ProcessorController
from src.ParserController import ParserController
from src.QueueController import QueueController
from settings import PROCESSOR_COMPONENTS, PARSER_COMPONENTS, QUEUE_COMPONENTS

class TSpider:
    def __init__(self, start_task):
        self.start_task = start_task
        self.processor = ProcessorController(self, PROCESSOR_COMPONENTS)
        self.parser = ParserController(self, PARSER_COMPONENTS)
        self.queue = QueueController(self, QUEUE_COMPONENTS)

    def start(self):
        self.queue.put(self.start_task)
        while not self.queue.empty():
            self.processor.process(self.parser, self.queue)