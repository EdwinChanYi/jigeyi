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
            for key,configs in redis_config.items():
                connections = []
                for config in configs:
                    host = config.get('host')
                    password = config.get('password')
                    db = config.get('db')
                    port = config.get('port')
                    connection = redis.ConnectionPool(host=host,
                                password=password, db=db, port=port, decode_responses=True)
                    connections.append(connection)
                cls.__pool[key] = connections
    @classmethod
    def get_pool(cls, mod='redis'):
        if not cls.__pool:
            cls.init()
        return cls.__pool.get(mod)


    @classmethod
    def conn(cls, hash_str, mod='redis'):
        connections = cls.get_pool(mod)
        connection = connections[cls.hashPool(connections.size(), hash_str)]
        return redis.Redis(connection_pool=connection)

    def hashPool(self, pool_num, hash_str='redis'):
        hash_num = 0
        for i in hash_str:
            hash_num += ord(i)
        return hash_num%pool_num

if (__name__ == '__main__'):
    conn = Redis.conn()
    conn.set('a', 123)
    a = conn.get('a')
    conn.close()