#!/usr/bin/env python
#-*- coding: utf-8 -*-

from model import BaseModel
from time import time
from conf.constant import MASTER_DB

class ShopModel(BaseModel):

    __table = 'shop'

    async def findByHost(self, host):
        sql = 'select * from shop where host = %s limit 1'
        row = await self.one(sql, (host), MASTER_DB)
        return row

    async def findValidByHost(self, host):
        now = int(time())
        sql = 'select * from shop where host = %s and status = 1 and %s >= start_time and %s <= end_time limit 1'
        row = await self.one(sql, (host, now, now), MASTER_DB)
        return row