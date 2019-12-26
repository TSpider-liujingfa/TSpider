# !/usr/bin/python3
# -*- coding: utf-8 -*-

from abc import ABCMeta

class TSpiderError(Exception, metaclass=ABCMeta):
    __msg__ = 'TSpider异常基类'

    def __init__(self):
        super().__init__(self.__msg__)

class QueueError(TSpiderError):
    __msg__ = '未知队列异常'

class QueueEmptyError(QueueError):
    __msg__ = '队列为空'

class QueueUnexpectedItemError(QueueError):
    __msg__ = '未知Item对象'

class QueueNoneExtractItemsError(QueueError):
    __msg__ = '空提取Item异常'