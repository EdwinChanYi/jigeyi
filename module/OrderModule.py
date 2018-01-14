#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 订单模块

from module import BaseModule,BaseObj
from model import ShoppingMallModel
import json
class OrderModule(BaseModule):
	def __init__(self, shop_db, shop_code):
		self.__shop_db = shop_db
		self.__shop_code = shop_code

	#获取所有订单
	async def getAllOrders(self, uid, begin, limit):
		if begin<0 or limit<0 or limit>100 or uid<0:
			return
	#获取待付款订单
	async def getWaitPayOrders(self, uid, begin, limit):
		if begin<0 or limit<0 or limit>100 or uid<0:
			return

	#获取待收货订单
	async def getWaitMakeSureOrders(self, uid, begin, limit):
		if begin<0 or limit<0 or limit>100 or uid<0:
			return

	#获取已完成订单
	async def getFinishOrders(self, uid, begin, limit):
		if begin<0 or limit<0 or limit>100 or uid<0:
			return

	#下单
	async def placeOrders(self, infos):
		if infos.empty():
			return
		return