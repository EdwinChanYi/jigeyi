#!/usr/bin/env python
# -*-  coding:utf-8 -*-
# 日志公共类

import time
import os
import logging
import logging.handlers

class Logger(object):

    @staticmethod
    def get_log(filename='main.log', divide=False):

        if divide:
            ymd = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            filename = filename + '-' + ymd
        filename = os.path.abspath(os.path.join(os.getcwd())) + '/data/' + filename

        handler = logging.handlers.RotatingFileHandler(filename)
        fmt = '%(asctime)s - %(filename)s:%(lineno)s - [thread:%(thread)s] - [process:%(process)s] - %(message)s'
        formatter = logging.Formatter(fmt)
        handler.setFormatter(formatter)

        logger = logging.getLogger('tst')
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)

        return logger

if __name__ == "__main__":
    # a = os.getcwd()
    # print(a)
    # b = os.path.join(a, 'log.txt')
    # print(b)
    # Logger.get_log('1.log')
    # print(os.path.abspath(os.path.join(os.getcwd(), "..")))

    log = Logger.get_log('abc.log')
    log.info('hello123')