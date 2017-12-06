#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 控制器基类，所有Model必须继承

import sys
sys.path.append('../')
from common import Db
import pymysql

class BaseModel(object):

    # 存放连接字典
    conn = {}

    # 默认数据库,优先于参数
    __default_mod = ''

    # 主库
    __master_mod = 'master'

    # 统一使用此方式实例话
    @classmethod
    def instance(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = cls()
        return cls._instance

    # 设置默认使用的库
    def set_default_mod(self, mod):
        if mod:
            self.__default_mod = mod

    # 获取连接
    async def get_conn(self, mod='master'):
        if self.conn.get(mod) is None:
            self.conn[mod] = await Db.conn(mod)
        return self.conn[mod]

    # 获取游标
    async def get_cursor(self, mod='master', cursor_type=pymysql.cursors.DictCursor):
        conn = await self.get_conn(mod)
        return conn.cursor(cursor_type)

    async def one(self, sql, param=(), mod='slave'):
        if self.__default_mod:
            mod = self.__default_mod
        cursor = self.get_cursor(mod)
        cursor.execute(sql, param)
        res = cursor.fetchone()
        cursor.close()
        return res

    async def all(self, sql, param=(), mod='slave'):
        if self.__default_mod:
            mod = self.__default_mod
        cursor = self.get_cursor(mod)
        cursor.execute(sql, param)
        res = cursor.fetchall()
        cursor.close()
        return res

    async def insert(self, sql, param=()):
        cursor = await self.get_cursor(self.__master_mod)
        row = cursor.execute(sql, param)
        if row != 1:
            return False
        cursor.close()
        insert_id = cursor.lastrowid
        return insert_id

    async def update(self, sql, param=()):
        cursor = await self.get_cursor(self.__master_mod)
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
    # res = a.one('select * from test')
    print(res)