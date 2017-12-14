#!/usr/bin/env python
#-*- coding: utf-8 -*-
# redis缓存装饰器

from common import Redis
import time
from common.Log import Logger

# key:redis key
# param:key中的参数,字典类型
# json:取到redis的数据是否进行解json
# write:若redis不存在,是否写回redis
# expire:过期时间,不传则永久
# 若空返回(),只能执行redis->get操作,无法执行pop之类操作
def redis(key, param=(), json=True, write=False, expire=False):
    async def cache(func):
        conn = await Redis.conn()
        if (conn):
            redis_key = key % param
            redis_val = await conn.get(redis_key)
            if json:
                pass
                # redis_val = json.loads(redis_val)
                # if redis_val and write:
                #     conn.set(redis_key, json.dumps())
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return res
        return wrapper
    return cache


# 函数计数装饰器，计数单位是毫秒
# max:可接受最大毫秒数，若0则必写进文件，若不为0则函数消耗时间大于此值才写入文件
# file:写入的日志文件
# 示例:@apiCounter(max=1000, file='test.log')
def apiCounter(max=0, file='api_timer.log'):
    def wrapper(func):
        async def count(*args, **kwargs):
            t = time.time()
            start = int(round(t * 1000))
            res = await func(*args, **kwargs)
            t = time.time()
            end = int(round(t * 1000))
            time_length = end - start   #函数消耗时间
            print('length',time_length)
            if max <= 0 or time_length > max:
                log = Logger.get_log(file)
                log.info('function['+func.__name__+'],time['+str(time_length)+']')
            return res
        return count
    return wrapper

