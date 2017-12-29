#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 商店处理器

from handler import BaseHandler
from module import ShopModule

class ShopHandler(BaseHandler):

    async def get(self):
        param = self.get_param()
        host = param.get('host')
        shop_module = ShopModule.instance()
        res = await shop_module.findShopByHost(host)
        self.success_ret(res)

