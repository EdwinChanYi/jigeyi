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
        if cls.__ins is None:
            cls.__ins = cls()
            cls.__ins.init()
        return cls.__ins

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
                cls.__pool[key] = PooledDB(pymysql, num, host=host, user=user, password=password, db=db, port=port, charset=charset, blocking=True, autocommit=True)

    # 获取连接
    def conn(self, mod):
        pool = self.__pool.get(mod)
        if not pool:
            raise Exception('db pool no this mod:',mod)
        return pool.connection()

if (__name__ == '__main__'):
    a = Db.instance()
    con1 = a.conn('clwa')
    # con1.begin() con1.commit() con1.rollback()
    cursor1 = con1.cursor(pymysql.cursors.DictCursor)
    # ret = cursor1.execute('set autocommit = 1')
    # print(ret)
    ret = cursor1.execute('update user set age = 7')
    print(ret)
    cursor1.close()
    con1.close()

    # con2 = a.conn('clw')
    # cursor2 = con2.cursor(pymysql.cursors.DictCursor)
    # con2.commit()
    # cursor2.close()
    # con2.close()
    # con1.commit()
    # print(con1)
    # print(con2)
    # print(con1 == con2)
    # b = Db.instance()
    # con = a.conn('jigeyi')
    # print(con)
    # print(a == b)