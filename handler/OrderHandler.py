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

# 获取待付款订单
class OrderQueryWaitSendOrdersByUserHandler(BaseHandler):
	def param_filter(self):
		return {
			'get': Schema({
				Required('begin'): int,
				Required('limit'): int,
			}),
		}

	async def get(self, *args, **kwargs):
		print("OrderQueryHaveSendOrdersByUserHandler")
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
		out_data = await order_module.getWaitSendOrders(uid, begin, limit)
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
class OrderPlaceOrdersHandler(BaseHandler):
	def param_filter(self):
		return {
			'get': Schema({
				Required('orders_data'):str
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
		orders_data = param.get('orders_data')
		out_data = await order_module.placeOneOrder(uid, orders_data)
		self.success_ret(out_data)

# 下单
class OrderPayOrderHandler(BaseHandler):
	def param_filter(self):
		return {
			'get': Schema({
				Required('order_id'): str
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
		order_id = param.get('order_id')
		out_data = await order_module.payOneOrder(uid, order_id)
		self.success_ret(out_data)
#发货
class OrderSendOrderHandler(BaseHandler):
	def param_filter(self):
		return {
			'get': Schema({
				Required('order_id'):str
			}),
		}

	async def get(self, *args, **kwargs):
		print("OderSendOrderHandler")
		param = self.get_param()
		print(param, self._shop)
		if not self._shop:
			return self.fail_ret(data={'para': 'error'})
		shop_code = self._shop.get('code')
		shop_db = self._shop.get('db')
		order_module = OrderModule.OrderModule(shop_db, shop_code)
		uid = self.get_current_user()
		order_id = param.get('order_id')
		out_data = await order_module.SendOrder(order_id)
		self.success_ret(out_data)
#收货
class OrderMakesureOrderHandler(BaseHandler):
	def param_filter(self):
		return {
			'get': Schema({
				Required('order_id'):str
			}),
		}

	async def get(self, *args, **kwargs):
		print("OderMakesureOrderHandler")
		param = self.get_param()
		print(param, self._shop)
		if not self._shop:
			return self.fail_ret(data={'para': 'error'})
		shop_code = self._shop.get('code')
		shop_db = self._shop.get('db')
		order_module = OrderModule.OrderModule(shop_db, shop_code)
		uid = self.get_current_user()
		order_id = param.get('order_id')
		out_data = await order_module.MakesureOrder(uid, order_id)
		self.success_ret(out_data)

#取消订单
class OrderCancelOrderHandler(BaseHandler):
	def param_filter(self):
		return {
			'get': Schema({
				Required('order_id'):str
			}),
		}

	async def get(self, *args, **kwargs):
		print("OderMakesureOrderHandler")
		param = self.get_param()
		print(param, self._shop)
		if not self._shop:
			return self.fail_ret(data={'para': 'error'})
		shop_code = self._shop.get('code')
		shop_db = self._shop.get('db')
		order_module = OrderModule.OrderModule(shop_db, shop_code)
		uid = self.get_current_user()
		order_id = param.get('order_id')
		out_data = await order_module.CancelOrder(uid, order_id)
		self.success_ret(out_data)

#退款
class OrderDrawbackOrderHandler(BaseHandler):
	def param_filter(self):
		return {
			'get': Schema({
				Required('order_id'):str
			}),
		}

	async def get(self, *args, **kwargs):
		print("OderDrawbackOrderHandler")
		param = self.get_param()
		print(param, self._shop)
		if not self._shop:
			return self.fail_ret(data={'para': 'error'})
		shop_code = self._shop.get('code')
		shop_db = self._shop.get('db')
		order_module = OrderModule.OrderModule(shop_db, shop_code)
		uid = self.get_current_user()
		order_id = param.get('order_id')
		out_data = await order_module.DrawbackOrder(uid, order_id)
		self.success_ret(out_data)
