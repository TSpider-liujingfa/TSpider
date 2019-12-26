# !/usr/bin/python3
# -*- coding: utf-8 -*-

__all__ = (
    'Component',
    'AsyncComponent'
)

from abc import abstractclassmethod, ABCMeta

class BaseComponent(metaclass=ABCMeta):
    def __init__(self):
        print('[+] init component:', self.__class__.__name__)

# 同步组件
class Component(BaseComponent, metaclass=ABCMeta):
    @abstractclassmethod
    def handler(self, item, result, controller):
        return item

# 异步组件
class AsyncComponent(BaseComponent, metaclass=ABCMeta):
    @abstractclassmethod
    async def handler(self, item, result, controller):
        return item