#!/usr/bin/env python
#-*- coding: utf-8 -*-

from model import BaseModel
from conf import constant
import sys

class OrderModel(BaseModel):

	def __init__(self, shop_db, shop_code):
		self.__shop_db = shop_db
		self.__shop_code = shop_code

	#获取用户所有订单
	async def findAllOrdersByUid(self, uid, begin, limit):
		return

	#获取待付款订单
	async def findWaitPayOrdersByUid(self, uid, begin, limit):
		return
	#获取待收货订单
	async def findWaitMakeSureOrdersByUid(self, uid, begin, limit):
		return
	#获取已完成订单
	async def findFinishOrdersByUid(self, uid, begin, limit):
		return

	#下单
	async def insertOrders(self, infos):
		return