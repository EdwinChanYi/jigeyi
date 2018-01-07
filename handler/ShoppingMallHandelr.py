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
		        Required('kindId'): int,
		        Required('type'): int,
		        }),
        }

    async def get(self):
        print("shoppingMallMaterialKinds")
        param = self.get_param()
        shop_info = await self.get_db_by_host()
        print(param, shop_info)
        if not shop_info:
            return self.fail_ret(data={'para':'error'})
        shopping_mall_module = ShoppingMallModule.ShoppingMallModule(shop_info,'1234')
        begin = 0
        limit = 50

        shopping_mall_module.getKindsByShop()
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
