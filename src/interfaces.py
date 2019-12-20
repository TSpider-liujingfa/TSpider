# !/usr/bin/python3
# -*- coding: utf-8 -*-

from abc import abstractclassmethod, ABCMeta

# 基础组件接口
class ComponentInterface(metaclass=ABCMeta):
    def __init__(self):
        print('初始化组件：' + self.__class__.__name__)

    # 处理数据并返回
    @abstractclassmethod
    def handler(self, item, controller):
        return item

class ProcessComponentInterface(ComponentInterface):
    pass

class ParserComponentInterface(ComponentInterface):
    pass

class QueueComponentInterface(ComponentInterface):
    pass