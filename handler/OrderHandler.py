#!/usr/bin/env python
#-*- coding: utf-8 -*-
#订单控制器
from voluptuous import *
from module import OrderModule
from handler import BaseHandler

#获取所有订单
class OrderQueryAllOrdersByUserHandler(BaseHandler):
	def param_filter(self):
		return {
			    'get': Schema({
		        Required('begin'): int,
                Required('limit'): int,
		        }),
        }

	async def get(self, *args, **kwargs):
		print("shoppingMallMaterialKinds")
		param = self.get_param()
		print(param, self._shop)
		if not self._shop:
			return self.fail_ret(data={'para': 'error'})
		shop_code = self._shop.get('code')
		shop_db = self._shop.get('db')
		order_module = OrderModule.OrderModule(shop_db, shop_code)
		uid = self.get_current_user()
		begin = param.get('begin')
		limit = param.get('limit')
		if begin is None or limit is None:
			begin = 0
			limit = 50
		out_data = await order_module.getAllOrders(uid, begin, limit)
		self.success_ret(out_data)

#获取待付款订单
class OrderQueryWaitPayOrdersByUserHandler(BaseHandler):
	def param_filter(self):
		return {
			    'get': Schema({
		        Required('begin'): int,
                Required('limit'): int,
		        }),
        }

	async def get(self, *args, **kwargs):
		print("OrderQueryWaitPayOrdersByUserHandler")
		param = self.get_param()
		print(param, self._shop)
		if not self._shop:
			return self.fail_ret(data={'para': 'error'})
		shop_code = self._shop.get('code')
		shop_db = self._shop.get('db')
		order_module = OrderModule.OrderModule(shop_db, shop_code)
		uid = self.get_current_user()
		begin = param.get('begin')
		limit = param.get('limit')
		if begin is None or limit is None:
			begin = 0
			limit = 50
		out_data = await order_module.getWaitPayOrders(uid, begin, limit)
		self.success_ret(out_data)

#获取待收货订单
class OrderQueryWaitMakeSureOrdersByUserHandler(BaseHandler):
	def param_filter(self):
		return {
			    'get': Schema({
		        Required('begin'): int,
                Required('limit'): int,
		        }),
        }

	async def get(self, *args, **kwargs):
		print("OrderQueryWaitPayOrdersByUserHandler")
		param = self.get_param()
		print(param, self._shop)
		if not self._shop:
			return self.fail_ret(data={'para': 'error'})
		shop_code = self._shop.get('code')
		shop_db = self._shop.get('db')
		order_module = OrderModule.OrderModule(shop_db, shop_code)
		uid = self.get_current_user()
		begin = param.get('begin')
		limit = param.get('limit')
		if begin is None or limit is None:
			begin = 0
			limit = 50
		out_data = await order_module.getWaitMakeSureOrders(uid, begin, limit)
		self.success_ret(out_data)

#获取已完成订单
class OrderQueryFinishOrdersByUserHandler(BaseHandler):
	def param_filter(self):
		return {
			    'get': Schema({
		        Required('begin'): int,
                Required('limit'): int,
		        }),
        }

	async def get(self, *args, **kwargs):
		print("OrderQueryFinishOrdersByUserHandler")
		param = self.get_param()
		print(param, self._shop)
		if not self._shop:
			return self.fail_ret(data={'para': 'error'})
		shop_code = self._shop.get('code')
		shop_db = self._shop.get('db')
		order_module = OrderModule.OrderModule(shop_db, shop_code)
		uid = self.get_current_user()
		begin = param.get('begin')
		limit = param.get('limit')
		if begin is None or limit is None:
			begin = 0
			limit = 50
		out_data = await order_module.getFinishOrders(uid, begin, limit)
		self.success_ret(out_data)

#下单
class PlaceOrdersHandler(BaseHandler):
	def param_filter(self):
		return {
			'get': Schema({
				Required('begin'): int,
				Required('limit'): int,
			}),
		}

	async def get(self, *args, **kwargs):
		print("PlaceOrdersHandler")
		param = self.get_param()
		print(param, self._shop)
		if not self._shop:
			return self.fail_ret(data={'para': 'error'})
		shop_code = self._shop.get('code')
		shop_db = self._shop.get('db')
		order_module = OrderModule.OrderModule(shop_db, shop_code)
		uid = self.get_current_user()
		begin = param.get('begin')
		limit = param.get('limit')
		if begin is None or limit is None:
			begin = 0
			limit = 50
		out_data = await order_module.getFinishOrders(uid, begin, limit)
		self.success_ret(out_data)