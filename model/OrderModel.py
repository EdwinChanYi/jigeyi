#!/usr/bin/env python
#-*- coding: utf-8 -*-

from model import BaseModel
from conf import constant
import sys
import time
class OrderModel(BaseModel):

	def __init__(self, shop_db, shop_code):
		self.__shop_db = shop_db
		self.__shop_code = shop_code

	#获取用户所有订单
	async def findAllOrdersByUid(self, uid, begin, limit):
		sql = 'SELECT * FROM ' + ( constant.MYSQL_ORDER_USER_SHOPPING_ORDER_TABLE) \
		      + ' WHERE uid=' + str(uid) + ' ORDER BY create_time desc LIMIT ' + str(begin)+ ','+str(limit)
		print(self.__shop_db, sql)
		rows = await self.all(sql, (), self.__shop_db)
		return rows

	#获取待付款订单
	async def findWaitPayOrdersByUid(self, uid, begin, limit):
		sql = 'SELECT * FROM ' + ( constant.MYSQL_ORDER_USER_SHOPPING_ORDER_TABLE) \
		      + ' WHERE uid=' + str(uid) + ' AND status=1 ORDER BY create_time desc LIMIT ' + str(begin)+ ','+str(limit)
		print(self.__shop_db, sql)
		rows = await self.all(sql, (), self.__shop_db)
		return rows
	#获取已发货订单
	async def findWaitSendOrdersByUid(self, uid, begin, limit):
		sql = 'SELECT * FROM ' + ( constant.MYSQL_ORDER_USER_SHOPPING_ORDER_TABLE) \
		      + ' WHERE uid=' + str(uid) + ' AND status=2 ORDER BY create_time desc LIMIT ' + str(begin)+ ','+str(limit)
		print(self.__shop_db, sql)
		rows = await self.all(sql, (), self.__shop_db)
		return rows
	#获取待收货订单
	async def findWaitMakeSureOrdersByUid(self, uid, begin, limit):
		sql = 'SELECT * FROM ' + ( constant.MYSQL_ORDER_USER_SHOPPING_ORDER_TABLE) \
		      + ' WHERE uid=' + str(uid) + ' AND status=3 ORDER BY create_time desc LIMIT ' + str(begin)+ ','+str(limit)
		print(self.__shop_db, sql)
		rows = await self.all(sql, (), self.__shop_db)
		return rows
	#获取已完成订单
	async def findFinishOrdersByUid(self, uid, begin, limit):
		sql = 'SELECT * FROM ' + ( constant.MYSQL_ORDER_USER_SHOPPING_ORDER_TABLE) \
		      + ' WHERE uid=' + str(uid) + ' AND status=4 ORDER BY create_time desc LIMIT ' + str(begin)+ ','+str(limit)
		print(self.__shop_db, sql)
		rows = await self.all(sql, (), self.__shop_db)
		return rows

	# 获取退款订单
	async def findDrawbackOrdersByUid(self, uid, begin, limit):
		sql = 'SELECT * FROM ' + (constant.MYSQL_ORDER_USER_SHOPPING_ORDER_TABLE) \
		      + ' WHERE uid=' + str(uid) + ' AND status=5 ORDER BY create_time desc LIMIT ' + str(begin) + ',' + str(limit)
		print(self.__shop_db, sql)
		rows = await self.all(sql, (), self.__shop_db)
		return rows

	# 获取退款订单
	async def findOneOrderDetailByUid(self, order_id):
		sql = 'SELECT * FROM ' + (constant.MYSQL_ORDER_USER_SHOPPING_ORDER_TABLE) \
		      + ' WHERE order_id=' + order_id
		print(self.__shop_db, sql)
		rows = await self.all(sql, (), self.__shop_db)
		return rows

	#提交订单
	async def insertOrder(self, uid, order_id, infos):
		sql = 'INSERT INTO ' + (constant.MYSQL_ORDER_USER_SHOPPING_ORDER_TABLE) \
		      + '(order_id, material_id, status, uid, shop_code, price, num, discount_ammount, create_time) VALUES'
		begin = 0
		materials = ''
		for which in range(begin, len(infos)):
			one_material = infos[which]
			materials = '('+order_id+','+one_material.get('material_id')+',1,'+str(uid)+','+self.__shop_code\
			            +','+one_material.get('price')+',' \
					+one_material.get('num')+','+one_material.get('discount_ammount')+','+time.time()+')'
			if which+1<len(infos)-1:
				materials += ','
		print(self.__shop_db, sql+materials)
		rows = await self.insert(sql+materials, (), self.__shop_db)
		return rows
	#已付款
	async def updateOrderToHavePayed(self, uid, order_id):
		sql = 'UPDATE ' + (constant.MYSQL_ORDER_USER_SHOPPING_ORDER_TABLE) \
		      + 'set status=2,pay_time='+time.time()+'WHERE order_id='+order_id+' AND uid='+str(uid)

		print(self.__shop_db, sql)
		rows = await self.insert(sql, (), self.__shop_db)
		return rows
	#已发货
	async def updateOrderToHaveSend(self, order_id):
		sql = 'UPDATE ' + (constant.MYSQL_ORDER_USER_SHOPPING_ORDER_TABLE) \
		      + 'set status=3,send_time='+time.time()+'WHERE order_id='+order_id

		print(self.__shop_db, sql)
		rows = await self.insert(sql, (), self.__shop_db)
		return rows
	#已完成
	async def updateOrderToFinish(self, uid, order_id):
		sql = 'UPDATE ' + (constant.MYSQL_ORDER_USER_SHOPPING_ORDER_TABLE) \
		      + 'set status=4,finish_time='+time.time()+'WHERE order_id='+order_id +' AND uid='+str(uid)

		print(self.__shop_db, sql)
		rows = await self.insert(sql, (), self.__shop_db)
		return rows
	#退款
	async def updateOrderToDrawback(self, uid, order_id):
		sql = 'UPDATE ' + (constant.MYSQL_ORDER_USER_SHOPPING_ORDER_TABLE) \
		      + 'set status=5,drawback_time='+time.time()+'WHERE order_id='+order_id +' AND uid='+str(uid)
		print(self.__shop_db, sql)
		rows = await self.insert(sql, (), self.__shop_db)
		return rows
	#取消订单
	async def updateOrderToCancel(self, uid, order_id):
		sql = 'UPDATE ' + (constant.MYSQL_ORDER_USER_SHOPPING_ORDER_TABLE) \
		      + 'set status=6,cancel_time='+time.time()+'WHERE order_id='+order_id +' AND uid='+str(uid)
		print(self.__shop_db, sql)
		rows = await self.insert(sql, (), self.__shop_db)
		return rows