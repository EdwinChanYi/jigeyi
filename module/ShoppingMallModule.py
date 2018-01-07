#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 商店模块

from module import BaseModule,BaseObj
from module import ShopModule
from model import ShoppingMallModel
import json
class Material(BaseObj):
    #食材ID
    material_id = 0
    #食材类ID
    kind_id = 0
    #食材名
    material_name = ''
    #食材类名
    kind_name = ''
    #食材普通价格
    common_price = 0
    #食材优惠价格
    discount_price = 0
    #食材图片
    image = ''
    #食材描述
    description = ''
    #数据状态
    status = 0
    #库存量
    repertory = 0

class Recipe(BaseObj):
    #食材ID
    material_id = 0
    #菜谱ID
    recipe_id = 0
    #菜谱名
    recipe_name = ''
    #食材名
    material_name = ''
    #食材图片
    image = ''
    #食材描述
    description = ''
    #数据状态
    status = 0
class ShoppingMallModule(BaseModule):

    def __init__(self, shop_db, shop_code):
        self.__shop_db = shop_db
        self.__shop_code = shop_code

    #根据店铺获取店铺食材类型
    async def getKindsByShop(self, begin, limit):
        shopping_mall = ShoppingMallModel.ShoppingMallModel(self.__shop_db, self.__shop_code)
        shop_kinds = await shopping_mall.findMaterialKindsByCode(begin, limit)
        print(shop_kinds)
        common_kinds = []
        [common_kinds.append(shop_kind.get('kind_id')) for shop_kind in shop_kinds]
        print(common_kinds)
        if common_kinds:
            kinds_info = await shopping_mall.findKindsInfoByKindId(common_kinds)
            return kinds_info


    #根据店铺和食材类型获取食材列表
    async def getMaterialsByShopAndKind(self, kind_id, begin, limit):
        shopping_mall = ShoppingMallModel.ShoppingMallModel(self.__shop_db, self.__shop_code)
        shop_material_rows = await shopping_mall.findMaterialsByCodeAndMaterialKind(kind_id, begin, limit)
        for show_mateial_row in shop_material_rows:
            shop_material = Material(show_mateial_row)

