# !/usr/bin/python3
# -*- coding: utf-8 -*-

from spider import TSpider
from src.item import Task

if __name__ == '__main__':
    tasks = [Task(id=i*10, _id=i*10) for i in range(3)]
    TSpider().start(tasks)