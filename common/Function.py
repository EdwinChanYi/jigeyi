#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 通用方法

import datetime
import json

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

#获取n天前时间，n>0获取过去时间，n<0获取未来时间
def get_days_before(n=0, format="%Y-%m-%d %H:%M:%S"):
    now = datetime.datetime.now()
    days_before = now - datetime.timedelta(days=n)
    ret_time = datetime.datetime(days_before.year, days_before.month, days_before.day, days_before.hour, days_before.minute, days_before.second)
    return ret_time.strftime(format)

if __name__ == "__main__":
    ret = get_days_before(1)
    print(ret)
    ret = json_encode({'a':12, 'b':34})
    print(ret)
    ret = json_decode(ret)
    print(ret)
    pass