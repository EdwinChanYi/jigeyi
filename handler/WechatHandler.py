#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 微信处理器

from handler import BaseHandler
from module import WechatModule

class WechatHandler(BaseHandler):

    async def get(self):
        shop = self._shop
        wechat_module = WechatModule()
        uri = wechat_module.getAuthUri(shop, 'test_state')
        self.success_ret(uri)

class WechatVerifyHandler(BaseHandler):

    async def get(self):
        return True;