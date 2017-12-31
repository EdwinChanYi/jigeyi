#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 商店模块

from module import BaseModule
from module import ShopModule

class ShoppingMallModule(BaseModule):

    async def getAllKindOfMaterialByShop(self, host):
        shop_info = await ShopModule.findShopByHost(host)

