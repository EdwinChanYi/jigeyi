#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 模块基类，所有模块必须继承

class BaseModule(object):

    __ins = None

    @classmethod
    def instance(cls):
        if cls.__ins is None:
            cls.__ins = cls()
        return cls.__ins
