#!/usr/bin/env python
#-*- coding: utf-8 -*-
#商城控制器

from handler import BaseHandler
from voluptuous import *
from module import ShoppingMallModule

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
        return await shopping_mall_module.getKindsByShop(begin, limit)

class ShoppingMallMaterialsHandler(BaseHandler):
    def param_filter(self):
        return {
            	'get': Schema({
	        	Required('host'): int,
				Required('type'): int,
			}),
		}
      
    def get(self):
        param = self.get_param()
        shop_db = self.get_db_by_host()

        if not shop_db:
            return self.fail_ret(data={'para':'error'})

    @classmethod
    def adjust(self, host):
        return False

class ShoppingMallHandler(BaseHandler):
    def param_filter(self):
        return {
            'get': Schema({
             Required('host'): int,
             Required('type'): int,
            }),
        }
    def get(self):
        param = self.get_param()
        shop_db = self.get_db_by_host()

        if not shop_db:
            return self.fail_ret(data={'para':'error'})

    @classmethod
    def adjust(self, host):
        return False

