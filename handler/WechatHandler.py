#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 微信处理器

from handler import BaseHandler
from module import WechatModule

class WechatHandler(BaseHandler):

    async def get(self):
        shop = self._shop
        wechat_module = WechatModule()
        uri = wechat_module.getAuthUri(shop, shop.get('code'))
        self.success_ret(uri)

    async def post(self):
        param = self.get_param()
        self.get_current_user()

class WechatVerifyHandler(BaseHandler):

    async def get(self):
        param = self.get_param()
        echostr = param.get('echostr')
        self.finish(echostr)

class WechatMenuHandler(BaseHandler):

    async def get(self):
        shop = self._shop
        wechat_module = WechatModule()
        ret = await wechat_module.setMenu(shop)
        self.finish(ret)
