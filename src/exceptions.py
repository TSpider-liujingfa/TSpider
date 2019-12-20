# !/usr/bin/python3
# -*- coding: utf-8 -*-

class TSpiderError(Exception):
    pass

class EmptyError(TSpiderError):
    def __init__(self):
        super().__init__('队列为空')