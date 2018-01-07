#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 模块基类，所有模块必须继承

class BaseModule(object):

    __ins = None

    _db = None

    def __init__(self, db):
        self._db = db

    @classmethod
    def instance(cls):
        if cls.__ins is None:
            cls.__ins = cls()
        return cls.__ins


class BaseObj(object):

    def __init__(self):
        pass

    def __init__(self, row):
        if row:
            for i in row:
                if hasattr(self, i):
                    setattr(self, i, row.get(i))
