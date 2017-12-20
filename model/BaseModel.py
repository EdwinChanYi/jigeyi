#!/usr/bin/env python
#-*- coding: utf-8 -*-
# model基类，所有Model必须继承

import sys
sys.path.append('../')
from common import Db
import pymysql

class BaseModel(object):

    __instance = None

    # 存放连接字典
    conn = {}

    # 默认数据库,次于mod参数
    __default_mod = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance

    # 统一使用此方式实例话
    # @classmethod
    # def instance(cls):
    #     if not hasattr(cls, '_instance'):
    #         cls._instance = cls()
    #     return cls._instance

    # 设置默认使用的库
    def setDefaultMod(self, mod):
        if mod:
            self.__default_mod = mod

    # 获取连接
    async def getConn(self, mod):
        if not mod and self.__default_mod:
            mod = self.__default_mod
        if self.conn.get(mod) is None:
            self.conn[mod] = await Db.conn(mod)
        return self.conn[mod]

    # 获取游标
    async def getCursor(self, mod, cursor_type=pymysql.cursors.DictCursor):
        if not mod and self.__default_mod:
            mod = self.__default_mod
        if not mod:
            raise Exception('no mod to get cursor');
        conn = await self.getConn(mod)
        return conn.cursor(cursor_type)

    async def one(self, sql, param, mod):
        if not mod and self.__default_mod:
            mod = self.__default_mod
        cursor = await self.getCursor(mod)
        cursor.execute(sql, param)
        res = cursor.fetchone()
        cursor.close()
        return res

    async def all(self, sql, param, mod):
        if not mod and self.__default_mod:
            mod = self.__default_mod
        cursor = await self.getCursor(mod)
        cursor.execute(sql, param)
        res = cursor.fetchall()
        cursor.close()
        return res

    async def insert(self, sql, param, mod):
        if not mod and self.__default_mod:
            mod = self.__default_mod
        cursor = await self.getCursor(mod)
        row = cursor.execute(sql, param)
        if row != 1:
            return False
        cursor.close()
        insert_id = cursor.lastrowid
        return insert_id

    async def update(self, sql, param, mod):
        if not mod and self.__default_mod:
            mod = self.__default_mod
        cursor = await self.getCursor(mod)
        row = cursor.execute(sql, param)
        cursor.close()
        if not row or row <= 0:
            return False
        return True

    async def delete(self, sql, param=()):
        cursor = await self.get_cursor(self.__master_mod)
        row = cursor.execute(sql, param)
        cursor.close()
        if not row or row <= 0:
            return False
        return True

    async def commit(self):
        conn = await self.get_conn(self.__master_mod)
        conn.commit()

    async def rollback(self):
        conn = await self.get_conn(self.__master_mod)
        conn.rollback()

    @classmethod
    def close(self):
        for mod in self.conn:
            self.conn.get(mod).close()


if (__name__ == '__main__'):
    a = BaseModel.instance()
    res = a.insert('insert into test(id,name) values(%s, %s)', (10, 'zhou'))
    res = a.one('select * from test')
    print(res)