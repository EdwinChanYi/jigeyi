#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 微信模块

from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from six.moves.urllib.parse import urlencode
from tornado.gen import Return
from common.Function import json_decode,async_get,async_post
from model import WechatModel
import time

class WechatModule(object):

    timeout = 5; #请求微信超时时间

    #  微信授权地址
    AUTH_URI = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=%s&redirect_uri=%s&response_type=code&scope=%s&state=%s#wechat_redirect'
    # 微信授权回调地址,code和state会带回到这个地址
    AUTH_REDIRECT_URI = 'http://clw.jigeyi.xyz/api/wechatAuthCallback'
    # 根据code获取openid或access_token
    GET_OPENID_URI = 'https://api.weixin.qq.com/sns/oauth2/access_token?'

    async def _request(self):
        pass;

    # 获取授权uri,此uri用于获取code
    async def getAuthUri(self, code, scope='snsapi_base'):
        model = WechatModel()
        shop_info = await model.findByCode(code)
        if not shop_info:
            raise Exception('no wuchat config with '+code)
        auth_uri = self.AUTH_URI % (shop_info.get('appid'), urlencode(self.AUTH_REDIRECT_URI), scope, code)
        return auth_uri

    # 根据code拿openid
    async def getOpenIdByCode(self, app_id, app_secret, code):
        uri = self.GET_OPENID_URI
        params = {
            'appid' : app_id,
            'secret' : app_secret,
            'code' : code,
            'grant_type' : 'authorization_code'
        }
        print('get openid param'+params)
        res = await async_get(uri, params)
        print('get opendi res:'+res)
        return res['open_id']

    async def getShopAccessToken(self, code):
        wechat_model = WechatModel()
        wechat_info = await wechat_model.findByCode(code)
        if not wechat_info:
            return None
        else:
            if wechat_info.get('access_token') and wechat_info.get('expire') and wechat_info.get('expire') > time.time():
                return wechat_info.get('access_token')
            else:
                if not wechat_info.get('appid') or not wechat_info.get('appsecret'):
                    return None
                param = {
                    'grant_type' : 'client_credential',
                    'appid' : wechat_info.get('appid'),
                    'secret' : wechat_info.get('appsecret')
                }
                uri = 'https://api.weixin.qq.com/cgi-bin/token'
                res = await async_get(uri, param)
                if not res:
                    raise Exception('get access token from wechat error')
                access_token = res.get('access_token')
                if not access_token:
                    raise Exception('get access token error')
                else:
                    await wechat_model.updateToken(wechat_info.get('id'), access_token, res.get('expires_in')+time.time())
                return access_token


    async def setMenu(self, shop):
        code = shop.get('code')
        access_token = await self.getShopAccessToken(code)
        uri = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s' % (access_token)
        param = {
             "button":[
             {
                  "type":"view",
                  "name":"首页",
                  "url":"http://clw.jigeyi.xyz/index.html"
             }]
        }
        res = await async_post(uri, param)
        return res







