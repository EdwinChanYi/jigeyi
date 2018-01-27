#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 微信模块

from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from six.moves.urllib.parse import urlencode
from tornado.gen import Return
from common.Function import json_decode

class WechatModule(object):

    timeout = 5; #请求微信超时时间

    #  微信授权地址
    AUTH_URI = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=%s&redirect_uri=%s&response_type=code&scope=%s&state=%s#wechat_redirect'
    # 微信授权回调地址,code和state会带回到这个地址
    AUTH_REDIRECT_URI = '/auth_callback'
    # 根据code获取openid或access_token
    GET_OPENID_URI = 'https://api.weixin.qq.com/sns/oauth2/access_token?'

    async def _request(self):
        pass;

    # 获取授权uri,此uri用于获取code
    def getAuthUri(self, shop, state, scope='snsapi_base'):
        app_id = shop.get('app_id')
        auth_uri = self.AUTH_URI % (app_id, self.AUTH_REDIRECT_URI, scope, state)
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

        res = await self._request_get(uri, params)
        return res['open_id']


    # get请求
    async def _request_get(self, url, params):
        http_client = AsyncHTTPClient()

        params = urlencode(dict((k, v) for k, v in params.items()))
        _url = '{0}?{1}'.format(url, params)

        req = HTTPRequest(
            url=_url,
            method="GET",
            request_timeout=self.timeout
        )
        res = await http_client.fetch(req)
        if res.error is not None:
            raise Exception('wechat error')

        result = self._decode_result(res)

        if 'errcode' in result and result['errcode'] != 0:
            raise Exception('wechat error')

        raise Return(result)

    def _decode_result(self, res):
        try:
            result = json_decode(res.body)
        except (TypeError, ValueError):
            return res
        return result