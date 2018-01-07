#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 商店模块

from module import BaseModule,BaseObj
from model.ShopModel import ShopModel

class ShopModule(BaseModule):

    # 根据域名获取商店
    async def findShopByHost(self, host):
        shop_model = ShopModel()
        row = await shop_model.findByHost(host)
        shop = Shop(row)
        return shop

    # 根据域名获取有效的商店
    async def findValidShopByHost(self, host):
        shop_model = ShopModel()
        row = await shop_model.findValidByHost(host)
        shop = Shop(row)
        return shop

class Shop(BaseObj):

    # 自增id,int
    id = 0

    # 商店代码,按照店名拼音大写,也用作登录账号,string
    code = None

    # 密码,string
    password = None

    # 地址,string
    address = None

    # 店名,string
    name = None

    # 联系方式,string
    contact = None

    # 备用联系方式,string
    contact_bak = None

    # 邮箱,string
    email = None

    # 手机号,string
    phone = None

    # 对应的数据库,为小写字母,string
    db = None

    # 域名,string
    host = None

    # 合作开始时间，即有效开始时间,int
    start_time = 0

    # 合作结束时间，即失效开始时间,int
    end_time = 0

    # 备注
    mark = None

    # 状态,-1:删除,0:停用,1:启用
    status = 0

    # 创建时间,int
    create_time = 0

    # 更新时间,int
    update_time = 0