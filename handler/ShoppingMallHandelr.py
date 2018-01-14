#!/usr/bin/env python
#-*- coding: utf-8 -*-
#商城控制器

from handler import BaseHandler
from voluptuous import *
from module import ShoppingMallModule

#获取食材类列表
class ShoppingMallMaterialKindsHandler(BaseHandler):

    def param_filter(self):
        return {
			    'get': Schema({
		        Required('begin'): int,
                Required('limit'): int,
		        }),
        }

    async def get(self):
        print("shoppingMallMaterialKinds")
        param = self.get_param()
        print(param, self._shop)
        if not self._shop:
            return self.fail_ret(data={'para':'error'})
        shop_code = self._shop.get('code')
        shop_db = self._shop.get('db')
        shopping_mall_module = ShoppingMallModule.ShoppingMallModule(shop_db,shop_code)
        begin = param.get('begin')
        limit = param.get('limit')
        if begin is None or limit is None:
            begin = 0
            limit = 50
        out_data = await shopping_mall_module.getKindsByShop(begin, limit)
        self.success_ret(out_data)

#获取食材列表
class ShoppingMallMaterialsHandler(BaseHandler):
    def param_filter(self):
        return {
            	'get': Schema({
	        	Required('host'): int,
				Required('type'): int,
			}),
		}
      
    async def get(self):
        param = self.get_param()
        print(param, self._shop)
        if not self._shop:
            return self.fail_ret(data={'para':'error'})
        shop_code = self._shop.get('code')
        shop_db = self._shop.get('db')
        if not shop_db or not shop_code:
            return self.fail_ret(data={'para':'error'})
        shopping_mall_module = ShoppingMallModule.ShoppingMallModule(shop_db,shop_code)
        begin = param.get('begin')
        limit = param.get('limit')
        kind_id = param.get('kindId')
        if not begin or not limit:
            begin = 0
            limit = 50
        shopping_mall_materials = await shopping_mall_module.getMaterialsByShopAndKind(kind_id,begin,limit)
        self.success_ret(shopping_mall_materials)

#获取每日食谱列表
class ShoppingMallRecipeDailyHandler(BaseHandler):
    def param_filter(self):
        return {
            'get': Schema({
             Required('host'): int,
             Required('type'): int,
            }),
        }

    async def get(self):
        param = self.get_param()
        print(param, self._shop)
        if not self._shop:
            return self.fail_ret(data={'para':'error'})
        shop_code = self._shop.get('code')
        shop_db = self._shop.get('db')
        if not shop_db or not shop_code:
            return self.fail_ret(data={'para':'error'})
        shopping_mall_module = ShoppingMallModule.ShoppingMallModule(shop_db,shop_code)
        begin = param.get('begin')
        limit = param.get('limit')
        shopping_mall_recipes = await shopping_mall_module.getDailyRecipeByShop(False, begin, limit)
        self.success_ret(shopping_mall_recipes)

#食材详情
class ShoppingMallMaterialDetailHandler(BaseHandler):
    def param_filter(self):
        return {
            'get': Schema({
                Required('material_id'): int,
                Required('type'): int,
            }),
        }

    async def get(self):
        param = self.get_param()
        print(param, self._shop)
        if not self._shop:
            return self.fail_ret(data={'para': 'error'})
        shop_code = self._shop.get('code')
        shop_db = self._shop.get('db')
        if not shop_db or not shop_code:
            return self.fail_ret(data={'para': 'error'})
        shopping_mall_module = ShoppingMallModule.ShoppingMallModule(shop_db, shop_code)
        material_id = param.get('material_id')
        shopping_mall_recipes = await shopping_mall_module.getMaterialDetailByMaterialId(material_id)
        self.success_ret(shopping_mall_recipes)

#菜谱详情
class ShoppingMallRecipeDetailHandler(BaseHandler):
    def param_filter(self):
        return {
            'get': Schema({
                Required('recipe_id'): int,
                Required('type'): int,
            }),
        }

    async def get(self):
        param = self.get_param()
        print(param, self._shop)
        if not self._shop:
            return self.fail_ret(data={'para': 'error'})
        shop_code = self._shop.get('code')
        shop_db = self._shop.get('db')
        if not shop_db or not shop_code:
            return self.fail_ret(data={'para': 'error'})
        shopping_mall_module = ShoppingMallModule.ShoppingMallModule(shop_db, shop_code)
        recipe_id = param.get('recipe_id')
        shopping_mall_recipes = await shopping_mall_module.getRecipeDetailByRecipeId(recipe_id)
        self.success_ret(shopping_mall_recipes)

#关联菜谱
class ShoppingMallRecipesRelatedToMaterilHandler(BaseHandler):
    def param_filter(self):
        return {
            'get': Schema({
                Required('material_id'): int,
                Required('type'): int,
            }),
        }

    async def get(self):
        param = self.get_param()
        print(param, self._shop)
        if not self._shop:
            return self.fail_ret(data={'para': 'error'})
        shop_code = self._shop.get('code')
        shop_db = self._shop.get('db')
        if not shop_db or not shop_code:
            return self.fail_ret(data={'para': 'error'})
        shopping_mall_module = ShoppingMallModule.ShoppingMallModule(shop_db, shop_code)
        material_id = param.get('material_id')
        shopping_mall_recipes = await shopping_mall_module.getRecipesRelatedMaterial(material_id)
        self.success_ret(shopping_mall_recipes)

#获取用户购物车
class ShoppingMallQueryUserShopCarHandler(BaseHandler):
    def param_filter(self):
        return {
            'get': Schema({
                Required('uid'): int,
                Required('type'): int,
            }),
        }

    async def get(self):
        param = self.get_param()
        print(param, self._shop)
        if not self._shop:
            return self.fail_ret(data={'para': 'error'})
        shop_code = self._shop.get('code')
        shop_db = self._shop.get('db')
        if not shop_db or not shop_code:
            return self.fail_ret(data={'para': 'error'})
        shopping_mall_module = ShoppingMallModule.ShoppingMallModule(shop_db, shop_code)
        uid = self.get_current_user()
        begin = param.get('begin')
        limit = param.get('limit')
        shopping_mall_materials = await shopping_mall_module.getUserShopCar(uid,begin, limit)
        self.success_ret(shopping_mall_materials)
