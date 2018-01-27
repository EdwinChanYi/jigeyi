#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 订单模块

from module import BaseModule,BaseObj
from model import OrderModel
import json
import time
from common import RedisMgr
class OrderModule(BaseModule):
	def __init__(self, shop_db, shop_code):
		self.__shop_db = shop_db
		self.__shop_code = shop_code

	#获取所有订单
	async def getAllOrders(self, uid, begin, limit):
		if begin<0 or limit<0 or limit>100 or uid<0:
			return
		order_modle = OrderModel.OrderModel(self.__shop_db, self.__shop_code)
		all_orders = await order_modle.findAllOrdersByUid(uid, begin, limit)
		return all_orders
	#获取待付款订单
	async def getWaitPayOrders(self, uid, begin, limit):
		if begin<0 or limit<0 or limit>100 or uid<0:
			return
		order_modle = OrderModel.OrderModel(self.__shop_db, self.__shop_code)
		all_orders = await order_modle.findWaitPayOrdersByUid(uid, begin, limit)
		return all_orders
	#获取待发货订单
	async def getWaitSendOrders(self, uid, begin, limit):
		if begin<0 or limit<0 or limit>100 or uid<0:
			return
		order_modle = OrderModel.OrderModel(self.__shop_db, self.__shop_code)
		all_orders = await order_modle.findWaitSendOrdersByUid(uid, begin, limit)
		return all_orders
	#获取待收货订单
	async def getWaitMakeSureOrders(self, uid, begin, limit):
		if begin<0 or limit<0 or limit>100 or uid<0:
			return
		order_modle = OrderModel.OrderModel(self.__shop_db, self.__shop_code)
		all_orders = await order_modle.findWaitMakeSureOrdersByUid(uid, begin, limit)
		return all_orders
	#获取已完成订单
	async def getFinishOrders(self, uid, begin, limit):
		if begin<0 or limit<0 or limit>100 or uid<0:
			return
		order_modle = OrderModel.OrderModel(self.__shop_db, self.__shop_code)
		all_orders = await order_modle.findFinishOrdersByUid(uid, begin, limit)
		return all_orders

	# 获取订单详情
	async def getOneOrderDetail(self, order_id):
		order_modle = OrderModel.OrderModel(self.__shop_db, self.__shop_code)
		all_orders = await order_modle.findOneOrderDetailByUid(order_id)
		return all_orders

	#下单
	async def placeOneOrder(self, uid, infos):
		if infos.empty():
			return
		order_id = self.__shop_code + str(uid)+str(time.time())
		order_modle = OrderModel.OrderModel(self.__shop_db, self.__shop_code)
		status = await order_modle.insertOrder(uid, order_id, infos)
		return status

	#付款
	async def payOneOrder(self, uid, infos):
		if infos.empty():
			return
		order_id = self.__shop_code + str(uid)+str(time.time())
		order_modle = OrderModel.OrderModel(self.__shop_db, self.__shop_code)
		status = await order_modle.updateOrderToHavePayed(uid, order_id)
		return status
	#发货
	async def SendOrder(self, order_id):
		order_modle = OrderModel.OrderModel(self.__shop_db, self.__shop_code)
		status = await order_modle.updateOrderToHaveSend(order_id)
		return status
	#收货
	async def MakesureOrder(self, uid, order_id):
		order_modle = OrderModel.OrderModel(self.__shop_db, self.__shop_code)
		status = await order_modle.updateOrderToFinish(uid, order_id)
		return status

	#取消订单
	async def CancelOrder(self, uid, order_id):
		order_modle = OrderModel.OrderModel(self.__shop_db, self.__shop_code)
		status = await order_modle.updateOrderToCancel(uid, order_id)
		return status

	#退款
	async def DrawbackOrder(self, uid, order_id):
		order_modle = OrderModel.OrderModel(self.__shop_db, self.__shop_code)
		status = await order_modle.updateOrderToDrawback(uid, order_id)
		return status

