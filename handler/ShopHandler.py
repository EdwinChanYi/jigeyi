#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 商店处理器

from handler import BaseHandler
from module import ShopModule

class ShopHandler(BaseHandler):

    # 测试商店权限
    async def get(self, id):
        shop = self._shop
        shop_module = ShopModule()
        is_auth = shop_module.isAuth(shop, ShopModule.AUTH_MENU)
        if is_auth:
            self.success_ret()
        else:
            self.fail_ret()

