#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 微信处理器

from handler import BaseHandler
from module import WechatModule,CookieModule,UserModule,ShopModule,WechatPushModule
import time
from tornado.web import authenticated

class WechatHandler(BaseHandler):

    async def get(self):
        shop = self._shop
        wechat_module = WechatModule()
        uri = await wechat_module.getAuthUri(shop.get('code'))
        self.success_ret(uri)

    @authenticated
    async def post(self):
        uid = self.current_user
        print('template push uid:'+uid)
        module = WechatPushModule()
        param = {
            'menu' : "牛肉三百斤",
            'address' : 'yy',
            'link' : 'http://www.baidu.com'
        }
        shop = self._shop
        user_module = UserModule(shop.get('db'))
        user = await user_module.getUserInfo(uid)
        if not user:
            self.json_ret(201, 'user not exits')
        res = await module.template_push('clw', user.open_id, WechatPushModule.TEMPLATE_TYPE_ORDER, param)
        self.success_ret(res)

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

class WechatCallbackHandler(BaseHandler):
    _init_shop = False

    async def get(self):
        print('oauth callback start')
        param = self.get_param()
        code = param.get('code')
        shop_code = param.get('state')

        wechat_module = WechatModule()
        shop = await wechat_module.getInfoByCode(shop_code)
        if not shop:
            raise Exception('no wechat config about '+shop_code)
        openid = await wechat_module.getOpenIdByCode(shop.get('appid'), shop.get('appsecret'), code)
        if not openid:
            raise Exception('get openid error')

        shop_module = ShopModule()
        row = await shop_module.findByCode(shop_code)
        if not row:
            raise Exception('shop not exit')
        user_module = UserModule(row.db)
        user = await user_module.getUserByOpenid(openid)
        if user:
            uid = user.id
        else:
            uid = await user_module.createByOpenid(shop_code, openid)
            if not uid:
                raise Exception('create user error')

        cookie_modle = CookieModule()
        cookie = cookie_modle.cookie_encrypt(uid, time.time() + 86500)#一天多一百秒，保证cookie有效期内有效
        self.set_secure_cookie('token', cookie, 1)
        self.redirect('/index.html')