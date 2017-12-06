#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 数据库工厂，维护数据库连接

import pymysql
import sys
sys.path.append('../')
from conf import db_config
from DBUtils.PooledDB import PooledDB

class Db(object):
    __ins = None
    __pool = {}

    # 统一使用此方式实例话
    @classmethod
    def instance(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = cls()
        return cls._instance

    # 初始化连接池
    @classmethod
    def init(cls):
        if not cls.__pool:
            for key in db_config:
                config = db_config.get(key)
                host = config.get('host')
                user = config.get('user')
                password = config.get('password')
                db = config.get('db')
                port = config.get('port')
                charset = config.get('charset')
                num = config.get('num')
                cls.__pool[key] = PooledDB(pymysql, num, host=host, user=user, password=password, db=db, port=port, charset=charset)

    @classmethod
    async def conn(cls, mod='master'):
        return cls.__pool.get(mod).connection()

if (__name__ == '__main__'):
    a = Db()
    # conn = a.conn()
    # cur = conn.cursor()
    # r = cur.execute('select * from test')
    # res = cur.fetchall()
    # print(res)
    # cur.close()
    # conn.close()
    # time.sleep(10)
