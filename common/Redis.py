#!/usr/bin/env python
#-*- coding: utf-8 -*-
# redis工厂，维护redis连接

import sys
sys.path.append('../')
import redis
from conf import redis_config

class Redis(object):

    __pool = {}

    @classmethod
    def init(cls):
        if not cls.__pool:
            for key in redis_config:
                config = redis_config.get(key)
                host = config.get('host')
                password = config.get('password')
                db = config.get('db')
                port = config.get('port')
                cls.__pool[key] = redis.ConnectionPool(host=host, password=password, db=db, port=port)

    @classmethod
    def get_pool(cls, mod='redis'):
        if not cls.__pool:
            cls.init()
        return cls.__pool.get(mod)


    @classmethod
    def conn(cls, mod='redis'):
        pool = cls.get_pool(mod)
        return redis.Redis(connection_pool=pool)

if (__name__ == '__main__'):
    conn = Redis.conn()
    conn.set('a', 123)
    a = conn.get('a')
    conn.close()