#!/usr/bin/env python
#-*- coding: utf-8 -*-
# redis管理

import sys
sys.path.append('../')
import redis
from conf import redis_config
import threading
from common import Redis
class RedisMgr:
	__instane = None
	@classmethod
	def getInstance(cls):
		if not cls.__instance:
			cls.__instance = cls()
		return cls.__instance

	async def hget(self, str_key, filed, mod = 'redis'):
		conn = Redis.conn(str_key,mod)
		return conn.hget(str_key, filed)

	async def hgetall(self, str_key, mod = 'reids'):
		conn = Redis.conn(str_key,mod)
		return conn.hgetall(str_key)

	async def hset(self, str_key, filed, value, mod='redis'):
		conn = Redis.conn(str_key, mod)
		return conn.hset(str_key, filed, value)

	async def hscan(self, str_key, cursor = 0, match = None, count = None, mod = 'redis'):
		conn = Redis.conn(str_key,mod)
		return conn.hscan(str_key,cursor, match, count)

	async def hmset(self, str_key, mapping, mod = 'redis'):
		conn = Redis.conn(str_key,mod)
		return conn.hmset(str_key,mapping)

	async def hmget(self, str_key, fields, mapping, mod = 'redis'):
		conn = Redis.conn(str_key, mod)
		return conn.hmget(str_key, fields, mapping)

	async def get(self, str_key, mod='redis'):
		conn = Redis.conn(str_key,mod)
		return conn.get(str_key)

	async def set(self, str_key, value, ex=None, px=None, nx=False, xx=False, mod='redis'):
		conn = Redis.conn(str_key, mod)
		return conn.set(str_key, value, ex, px, nx, xx)

	async def expire(self, str_key, expire, mod = 'redis'):
		conn = Redis.conn(str_key, mod)
		return conn.expire(str_key, expire)

	async def zset(self, str_key, mod = 'redis', *argvs, **kwargs):
		conn = Redis.conn(str_key, mod)
		return conn.zadd(str_key, *argvs, **kwargs)

	async def zincry(self, str_key, field, add, mod='redis'):
		conn = Redis.conn(str_key, mod)
		return conn.zincrby(str_key, field, add)

	async def zrevrange(self, str_key, begin, end, withscore = False, score_cast_func=float, mod = 'redis'):
		conn = Redis.conn(str_key, mod)
		return conn.zrevrange(str_key, begin, end, withscore,score_cast_func)

	async def zrange(self, str_key, begin, end, withscore = False, score_cast_func=float, mod = 'redis'):
		conn = Redis.conn(str_key, mod)
		return conn.zrange(str_key, begin, end, withscore,score_cast_func)

	async def sadd(self, str_key, field, mod = 'redis'):
		conn = Redis.conn(str_key, mod)
		return conn.sadd(str_key, field)

	async def sismember(self, str_key, field, mod = 'redis'):
		conn = Redis.conn(str_key, mod)
		return conn.sismember(str_key, field)

	async def smembers(self, str_key, mod = 'redis'):
		conn = Redis.conn(str_key, mod)
		return conn.smembers(str_key)

	async def srem(self, str_key, *values, mod = 'redis'):
		conn = Redis.conn(str_key, mod)
		return conn.srem(str_key, *values)


