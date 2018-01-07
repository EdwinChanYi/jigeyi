#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 商店处理器

from handler import BaseHandler
from module import ShopModule
from common.Decorate import auth

class ShopHandler(BaseHandler):

    # 测试商店权限
    @auth(ShopModule.AUTH_MENU)
    async def get(self, id):
        self.success_ret(id)

