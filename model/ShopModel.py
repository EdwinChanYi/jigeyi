#!/usr/bin/env python
#-*- coding: utf-8 -*-

from model import BaseModel
from time import time
from conf import constant

class ShopModel(BaseModel):

    async def findByHost(self, host):
        sql = 'select * from ' + constant.MYSQL_SHOP_TABLE + ' where host = %s limit 1'
        row = await self.one(sql, (host), constant.MYSQL_JIGEYI_DB)
        return row

    async def findValidByHost(self, host):
        now = int(time())
        sql = 'select * from ' + constant.MYSQL_SHOP_TABLE + ' where host = %s and status = 1 and %s >= start_time and %s <= end_time limit 1'
        row = await self.one(sql, (host, now, now), constant.MYSQL_JIGEYI_DB)
        return row