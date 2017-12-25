#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 商店模块

from module import BaseModule
from model.ShopModel import *

class ShopModule(BaseModule):

    async def findShopByHost(self, host):
        shop = Shop.instance()
        return await shop.findByHost(host)
