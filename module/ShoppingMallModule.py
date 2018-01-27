#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 商店模块

from module import BaseModule,BaseObj
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
        common_kinds = []
        [common_kinds.append(str(shop_kind.get('kind_id'))) for shop_kind in shop_kinds]
        if common_kinds:
            kinds_info = await shopping_mall.findKindsInfoByKindId(common_kinds)
            return kinds_info


    #根据店铺和食材类型获取食材列表
    async def getMaterialsByShopAndKind(self, kind_id, begin, limit):
        shopping_mall = ShoppingMallModel.ShoppingMallModel(self.__shop_db, self.__shop_code)
        shop_material_rows = await shopping_mall.findMaterialsByCodeAndMaterialKind(kind_id, begin, limit)
        return shop_material_rows

    #获取每日菜谱
    async def getDailyRecipeByShop(self, is_own, begin, limit):
        shopping_mall_model = ShoppingMallModel.ShoppingMallModel(self.__shop_db, self.__shop_code)
        shopping_mall_recipes = await shopping_mall_model.findDailyRecipeList(is_own, begin, limit)
        return shopping_mall_recipes

    #获取食材详情
    async def getMaterialDetailByMaterialId(self, material_id):
        shopping_mall_model = ShoppingMallModel.ShoppingMallModel(self.__shop_db, self.__shop_code)
        shopping_mall_material = await shopping_mall_model.findMaterialDetail(material_id)
        return shopping_mall_material
    #获取菜谱详情
    async def getRecipeDetailByRecipeId(self, is_own, recipe_id):
        shopping_mall_model = ShoppingMallModel.ShoppingMallModel(self.__shop_db, self.__shop_code)
        shopping_mall_recipe = await shopping_mall_model.findRecipeDetail(is_own, recipe_id)
        return shopping_mall_recipe

    #获取关联菜谱
    async def getRecipesRelatedMaterial(self, is_own, material_id):
        shopping_mall_model = ShoppingMallModel.ShoppingMallModel(self.__shop_db, self.__shop_code)
        shopping_mall_recipes = await shopping_mall_model.findRecipeRelatedMaterial(is_own, material_id)
        return shopping_mall_recipes

    #获取用户购物车列表
    async def getUserShopCar(self, uid, begin, limit):
        shopping_mall_model = ShoppingMallModel.ShoppingMallModel(self.__shop_db, self.__shop_code)
        shopping_mall_materials = await shopping_mall_model.findUserShopCarByUid(uid, begin, limit)
        return shopping_mall_materials

    #添加用户购物车
    async def addUserShopCar(self, uid, material_info):
        shopping_mall_model = ShoppingMallModel.ShoppingMallModel(self.__shop_db, self.__shop_code)
        res = await shopping_mall_model.insertAddUserShopCarToUid(uid, material_info)
        return res

    #修改用户购物车
    async def motifyUserShopCar(self, uid, material_info):
        shopping_mall_model = ShoppingMallModel.ShoppingMallModel(self.__shop_db, self.__shop_code)
        res = await shopping_mall_model.updateUserShopCarToUid(uid, material_info)
        return res

    #删除用户购物车
    async def deleteUserShopCar(self, uid, materials):
        shopping_mall_model = ShoppingMallModel.ShoppingMallModel(self.__shop_db, self.__shop_code)
        res = await shopping_mall_model.deleteUserShopCarOfUid(uid, materials)
        return res

    #