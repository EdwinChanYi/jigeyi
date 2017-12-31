#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 常用装饰器

from common import Redis
import time
from common.Log import Logger
from json import dumps,loads
from common.Function import json_encode,json_decode

import datetime
import json

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


# redis key decorator
# key:redis key
# param:key中的参数,字典类型
# json:取到redis的数据是否进行解json
# write:若redis不存在,是否写回redis
# expire:过期时间,不传则永久
# 若空返回(),只能执行redis->get操作,无法执行pop之类操作
def redisGet(key, param=[], json=True, write=True, expire=False):
    def wrapper(func):
        async def cache(*args, **kwargs):
            redis_param = []
            if param:
                for i,val in enumerate(param):
                    if val.isdigit():
                        redis_param.append(args[int(val)])
                    else:
                        if kwargs.get(val) is None:
                            raise Exception('decorate param not exit,',val)
                        redis_param.append(kwargs.get(val))
                redis_key = key % tuple(param)
            else :
                redis_key = key

            conn = Redis.conn()
            res = conn.get(redis_key)
            if res:
                if json:
                    res = json_decode(res)
            else:
                res = await func(*args, **kwargs)
                if res and write:
                    redis_val = res
                    if json:
                        redis_val = json_encode(res, cls=DateEncoder)
                    conn.set(redis_key, redis_val)
                    if expire:
                        conn.expire(redis_key, expire)
            return res
        return cache
    return wrapper

# redis hash decorator
# key:redis key
# field:redis field
# param:key中的参数
# json:取到redis的数据是否进行解json
# write:若redis不存在,是否写回redis
# expire:过期时间,不传则永久
# 若空返回(),只能执行redis->get操作,无法执行pop之类操作
def redisHget(key, field, param=[], json=True, write=True, expire=False):
    def wrapper(func):
        async def cache(*args, **kwargs):
            redis_param = []
            if param:
                for i,val in enumerate(param):
                    if val.isdigit():
                        redis_param.append(args[int(val)])
                    else:
                        if kwargs.get(val) is None:
                            raise Exception('decorate param not exit,',val)
                        redis_param.append(kwargs.get(val))
                redis_key = key % tuple(redis_param)
            else :
                redis_key = key

            conn = Redis.conn()
            res = conn.hget(redis_key, field)
            if res:
                if json:
                    res = loads(res)
            else:
                res = await func(*args, **kwargs)
                if res and write:
                    res = dumps(res, cls=DateEncoder)
                    conn.hset(redis_key, field, res)
                    if expire:
                        conn.expire(redis_key, expire)
            return res
        return cache
    return wrapper

# redis hash obj decorator
# key:redis key
# field:redis field
# param:key中的参数
# write:若redis不存在,是否写回redis
# expire:过期时间,不传则永久
# 将对象进行hash存储,若空返回{},包装的db方法必须返回对象,只有需要的所有属性都存在于redis的时候才会不走db
def redisHashObj(key, field=[], param=[], write=True, expire=False):
    def wrapper(func):
        async def cache(*args, **kwargs):
            redis_param = []
            if param:
                for i,val in enumerate(param):
                    if val.isdigit():
                        redis_param.append(args[int(val)])
                    else:
                        if kwargs.get(val) is None:
                            raise Exception('decorate param not exit,',val)
                        redis_param.append(kwargs.get(val))
                redis_key = key % tuple(redis_param)
            else :
                redis_key = key

            from_redis = True   #是否成功从redis获取所有属性标志
            if field:
                conn = Redis.conn()
                redis_val = {}
                for f in field:
                    val = conn.hget(redis_key, f)
                    if val:
                        redis_val[f] = val
                    else:
                        from_redis = False
                        break

            if from_redis:
                res = redis_val
            else:
                res = await func(*args, **kwargs)
                if res and write:
                    for r in res.__dict__:
                        conn.hset(redis_key, r, getattr(res, r))
                    if expire:
                        conn.expire(redis_key, expire)
            return res
        return cache
    return wrapper


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

