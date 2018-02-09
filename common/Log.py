#!/usr/bin/env python
# -*-  coding:utf-8 -*-
# 日志公共类

import time
import os
import logging
import logging.handlers
from conf.constant import *

class Logger(object):

    # 日志通用函数
    # file:写入的文件名，多个单词建议用-隔开，如，access-log
    # message:写入的内容
    # divide:是否按月拆分，是的话文件名后面会加上日期，如main-2018-02-09.log
    @staticmethod
    def log(file, message, divide=False, level='info'):
        if not file or not message:
            return
        if divide:
            ymd = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            file = file + '-' + ymd
        file = DOCUMENT_ROOT + '/' + file + '.log'
        LOG_FORMAT = "%(asctime)s [%(levelname)s] %(message)s"
        DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
        logging.basicConfig(filename=file, level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
        if level == 'debug':
            logging.debug(message)
        elif level == 'warning':
            logging.warning(message)
        elif level == 'error':
            logging.error(message)
        else:
            logging.info(message)

if __name__ == "__main__":
    Logger.log('main', 'test', True, 'error')