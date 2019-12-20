# !/usr/bin/python3
# -*- coding: utf-8 -*-

from src.items import Result

class BaseController:
    def __init__(self, spider, components):
        self.spider = spider
        self.components = [i() for i in components]

    def pipeline(self, item, default_result=None):
        result = default_result
        for component in self.components:
            _result = component.handler(item, result, self)
            result = self.result_handler(result, _result)
        return result

    def result_handler(self, pre_result, result):
        return result