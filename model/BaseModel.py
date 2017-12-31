#!/usr/bin/env python
#-*- coding: utf-8 -*-
# model基类，所有Model必须继承

import sys
sys.path.append('../')
from common import Db
import pymysql

class BaseModel(object):

    # 默认数据库,次于mod参数
    __db = None

    # __ins = None

    # 获取单例
    # @classmethod
    # def instance(cls):
    #     if cls.__ins is None:
    #         cls.__ins = cls()
    #     return cls.__ins

    def __init__(self, db=None):
        self.__db = db

    def get_db(self):
        return self.__db

    # 设置默认使用的库
    def setDefaultMod(self, mod):
        if mod:
            self.__db = mod

    # 获取连接
    def getConn(self, mod=None):
        if mod is None and self.__db:
            mod = self.__db
        return Db.instance().conn(mod)

    async def one(self, sql, param, mod=None):
        if mod is None and self.__db:
            mod = self.__db
        conn = self.getConn(mod)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql, param)
        res = cursor.fetchone()
        cursor.close()
        conn.close()
        return res

    async def all(self, sql, param=(), mod=None):
        if mod is None and self.__db:
            mod = self.__db
        conn = self.getConn(mod)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql, param)
        res = cursor.fetchall()
        cursor.close()
        conn.close()
        return res

    async def insert(self, sql, param, mod=None):
        if mod is None and self.__db:
            mod = self.__db
        conn = self.getConn(mod)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        row = cursor.execute(sql, param)
        if row != 1:
            return False
        cursor.close()
        conn.close()
        insert_id = cursor.lastrowid
        return insert_id

    async def update(self, sql, param, mod=None):
        if not mod and self.__db:
            mod = self.__db
        conn = self.getConn(mod)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        row = cursor.execute(sql, param)
        cursor.close()
        conn.close()
        return row

    async def delete(self, sql, param=(), mod=None):
        if not mod and self.__db:
            mod = self.__db
        conn = self.getConn(mod)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        row = cursor.execute(sql, param)
        cursor.close()
        conn.close()
        return row

if (__name__ == '__main__'):
    a = BaseModel()
    b = BaseModel()
    print(a == b)
    # res = a.insert('insert into test(id,name) values(%s, %s)', (10, 'zhou'))
    # res = a.one('select * from test')
    # print(res)