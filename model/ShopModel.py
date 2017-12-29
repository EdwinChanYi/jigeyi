#!/usr/bin/env python
#-*- coding: utf-8 -*-

from model import BaseModel

class ShopModel(BaseModel):

    __table = 'shop'

    async def findByHost(self, host):
        sql = 'select * from shop where host = %s limit 1'
        row = await self.one(sql, (host), 'jigeyi')
        return row