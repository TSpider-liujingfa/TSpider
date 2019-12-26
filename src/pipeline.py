# !/usr/bin/python3
# -*- coding: utf-8 -*-

__all__ = ('Pipeline')

import types
from abc import ABCMeta

# 管道处理
class Pipeline(metaclass=ABCMeta):
    def __init__(self, components):
        self.components = [i() for i in components]

    # 组件管道
    async def pipeline(self, item, default_result=None):
        result = default_result
        for component in self.components:
            _result = component.handler(item, result, self)
            result = await self._result_handler(result, _result)
        return result

    # 结果处理（内部）
    async def _result_handler(self, pre_result, result):
        if isinstance(result, types.AsyncGeneratorType): # 异步生成器
            async for _result in result:
                pre_result = await self._result_handler(pre_result, _result)
        elif isinstance(result, types.CoroutineType): # 异步函数
            pre_result = await self._result_handler(pre_result, await result)
        elif isinstance(result, types.GeneratorType): # 生成器
            for _result in result:
                pre_result = await self._result_handler(pre_result, _result)
        elif isinstance(result, str):
            print(result)
        elif result is not None:
            pre_result = self.result_handler(pre_result, result)
        return pre_result

    # 结果处理
    def result_handler(self, pre_result, result):
        return pre_result