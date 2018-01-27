#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 通用方法

import datetime
import json
import time
from binascii import b2a_hex, a2b_hex
from Crypto.Cipher import AES

#json加密兼容datetime
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

# json加密
def json_encode(data):
    return json.dumps(data, cls=DateEncoder)

# json解密
def json_decode(json_data):
    return json.loads(json_data)

# 获取n天前时间，n>0获取过去时间，n<0获取未来时间
def get_days_before(n=0, format="%Y-%m-%d %H:%M:%S"):
    now = datetime.datetime.now()
    days_before = now - datetime.timedelta(days=n)
    ret_time = datetime.datetime(days_before.year, days_before.month, days_before.day, days_before.hour, days_before.minute, days_before.second)
    return ret_time.strftime(format)

# 获取n小时前时间，n>0获取过去时间，n<0获取未来时间
def get_time_before_hour(hours, is_format=True, format='%Y-%m-%d %H:%M:%S'):
    hours = int(hours)
    t = time.time() - hours*60*60
    if is_format:
        t = time.strftime(format, time.localtime(t))
    return t


def aes_encrypt(val, key, mode=AES.MODE_CBC):
    cryptor = AES.new(key, mode, key)
    length = 16
    count = len(val)
    if (count % length != 0):
        add = length - (count % length)
    else:
        add = 0
    val = val + ('\0' * add)
    ret = cryptor.encrypt(val)
    return b2a_hex(ret).decode('utf-8')

def aes_decrypt(val, key, mode=AES.MODE_CBC):
    cryptor = AES.new(key, mode, key)
    val = cryptor.decrypt(a2b_hex(val))
    return val.decode('utf-8').rstrip('\0')

if __name__ == "__main__":
    r = []
    r.append('a')
    r.append('e')
    print(','.join(r))