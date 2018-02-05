#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 微信公众号模型

from model import BaseModel
from conf import constant

class WechatModel(BaseModel):

    async def findByCode(self, code):
        sql = 'select * from wechat where code = %s limit 1'
        row = await self.one(sql, (code), constant.MYSQL_JIGEYI_DB)
        return row

    async def findByAppidAppsecret(self, appid, appsecret):
        sql = 'select * from wechat where appid = %s and appsecret = %s limit 1'
        row = await self.one(sql, (appid, appsecret), constant.MYSQL_JIGEYI_DB)
        return row

    async def updateToken(self, id, access_token, expire):
        sql = 'update wechat set access_token = %s, expire = %s where id = %s limit 1'
        ret = await self.update(sql, (access_token, expire, id), constant.MYSQL_JIGEYI_DB)
        return ret