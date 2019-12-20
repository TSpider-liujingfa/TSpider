# !/usr/bin/python3
# -*- coding: utf-8 -*-

from spider import TSpider
from src.items import Task

if __name__ == '__main__':
    start_task = Task(number=1)
    TSpider(start_task).start()