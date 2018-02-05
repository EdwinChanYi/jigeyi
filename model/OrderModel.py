#!/usr/bin/env python
#-*- coding: utf-8 -*-

from model import BaseModel
from conf import constant
import sys
import time
from common import Function
import datetime
class OrderModel(BaseModel):

	def __init__(self, shop_db, shop_code):
		self.__shop_db = shop_db
		self.__shop_code = shop_code

	#获取用户所有订单
	async def findAllOrdersByUid(self, uid, begin, limit):
		sql = 'SELECT order_id,wetchat_order_id,status,uid,material_infos,contract,CAST(create_time AS CHAR) AS create_time FROM ' + ( constant.MYSQL_ORDER_USER_SHOPPING_ORDER_TABLE) \
		      + ' WHERE uid=' + str(uid) + ' ORDER BY create_time desc LIMIT ' + str(begin)+ ','+str(limit)
		print(self.__shop_db, sql)
		rows = await self.all(sql, (), self.__shop_db)
		print(self.__shop_db, sql)
		return rows

	#获取待付款订单
	async def findWaitPayOrdersByUid(self, uid, begin, limit):
		sql = 'SELECT order_id,wetchat_order_id,status,uid,material_infos,contract,CAST(create_time AS CHAR) AS create_time FROM ' + ( constant.MYSQL_ORDER_USER_SHOPPING_ORDER_TABLE) \
		      + ' WHERE uid=' + str(uid) + ' AND status=1 ORDER BY create_time desc LIMIT ' + str(begin)+ ','+str(limit)
		print(self.__shop_db, sql)
		rows = await self.all(sql, (), self.__shop_db)
		return rows
	#获取已发货订单
	async def findWaitSendOrdersByUid(self, uid, begin, limit):
		sql = 'SELECT order_id,wetchat_order_id,status,uid,material_infos,contract,CAST(create_time AS CHAR) AS create_time FROM ' + ( constant.MYSQL_ORDER_USER_SHOPPING_ORDER_TABLE) \
		      + ' WHERE uid=' + str(uid) + ' AND status=2 ORDER BY create_time desc LIMIT ' + str(begin)+ ','+str(limit)
		print(self.__shop_db, sql)
		rows = await self.all(sql, (), self.__shop_db)
		return rows
	#获取待收货订单
	async def findWaitMakeSureOrdersByUid(self, uid, begin, limit):
		sql = 'SELECT order_id,wetchat_order_id,status,uid,material_infos,contract,CAST(create_time AS CHAR) AS create_time FROM ' + ( constant.MYSQL_ORDER_USER_SHOPPING_ORDER_TABLE) \
		      + ' WHERE uid=' + str(uid) + ' AND status=3 ORDER BY create_time desc LIMIT ' + str(begin)+ ','+str(limit)
		print(self.__shop_db, sql)
		rows = await self.all(sql, (), self.__shop_db)
		return rows
	#获取已完成订单
	async def findFinishOrdersByUid(self, uid, begin, limit):
		sql = 'SELECT order_id,wetchat_order_id,status,uid,material_infos,contract,CAST(create_time AS CHAR) AS create_time FROM ' + ( constant.MYSQL_ORDER_USER_SHOPPING_ORDER_TABLE) \
		      + ' WHERE uid=' + str(uid) + ' AND status=4 ORDER BY create_time desc LIMIT ' + str(begin)+ ','+str(limit)
		print(self.__shop_db, sql)
		rows = await self.all(sql, (), self.__shop_db)
		return rows

	# 获取退款订单
	async def findDrawbackOrdersByUid(self, uid, begin, limit):
		sql = 'SELECT order_id,wetchat_order_id,status,uid,material_infos,contract,CAST(create_time AS CHAR) AS create_time FROM ' + (constant.MYSQL_ORDER_USER_SHOPPING_ORDER_TABLE) \
		      + ' WHERE uid=' + str(uid) + ' AND status=5 ORDER BY create_time desc LIMIT ' + str(begin) + ',' + str(limit)
		print(self.__shop_db, sql)
		rows = await self.all(sql, (), self.__shop_db)
		return rows

	# 获取退款订单
	async def findOneOrderDetailByUid(self, order_id):
		sql = 'SELECT ordei_id,wetchat_order_id,status,uid,material_infos,contract,CAST(create_time AS CHAR) AS create_time FROM ' + (constant.MYSQL_ORDER_USER_SHOPPING_ORDER_TABLE) \
		      + ' WHERE order_id=' + order_id
		print(self.__shop_db, sql)
		rows = await self.all(sql, (), self.__shop_db)
		return rows

	#提交订单
	async def insertOrder(self, uid, order_id, infos):
		sql = 'INSERT INTO ' + (constant.MYSQL_ORDER_USER_SHOPPING_ORDER_TABLE) \
		      + '(order_id, status, uid, shop_code, material_infos, create_time) VALUES'
		# begin = 0
		# materials = ''
		# print(order_id)
		# for which in range(begin, len(infos)):
		# 	one_material = infos[which]
		# 	materials = '(\''+order_id+'\','+one_material.get('material_id')+',1,'+str(uid)+','+self.__shop_code\
		# 	            +','+(one_material.get('price'))+',' \
		# 				+(one_material.get('num'))+','+ (one_material.get('discount_ammount'))+','+str(time.time())+')'
		# 	if which+1<len(infos)-1:
		# 		materials += ','
		materials = '(%s,%s,%s,%s,%s,%s)'
		dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		print(self.__shop_db, sql+materials)
		rows = await self.insert(sql+materials, (order_id,1,uid,self.__shop_code,Function.json_encode(infos),dt), self.__shop_db)
		return rows
	#已付款
	async def updateOrderToHavePayed(self, uid, order_id):
		dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		sql = 'UPDATE ' + (constant.MYSQL_ORDER_USER_SHOPPING_ORDER_TABLE) \
		      + ' set status=2,pay_time=%s WHERE order_id=%s AND uid=%s'
		print(uid,order_id)
		print(self.__shop_db, sql)
		rows = await self.update(sql, (dt,order_id,uid), self.__shop_db)
		return rows
	#已发货
	async def updateOrderToHaveSend(self, order_id):
		dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		sql = 'UPDATE ' + (constant.MYSQL_ORDER_USER_SHOPPING_ORDER_TABLE) \
		      + ' set status=3,send_time=%s WHERE order_id=%s'
		print(order_id)
		print(self.__shop_db, sql)
		rows = await self.update(sql, (dt,order_id), self.__shop_db)
		return rows
	#已完成
	async def updateOrderToFinish(self, uid, order_id):
		dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		sql = 'UPDATE ' + (constant.MYSQL_ORDER_USER_SHOPPING_ORDER_TABLE) \
		      + ' set status=4,finish_time=%s WHERE order_id=%s AND uid=%s'
		print(order_id)
		print(self.__shop_db, sql)
		rows = await self.update(sql, (dt,order_id,uid), self.__shop_db)
		return rows
	#退款
	async def updateOrderToDrawback(self, uid, order_id):
		dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		sql = 'UPDATE ' + (constant.MYSQL_ORDER_USER_SHOPPING_ORDER_TABLE) \
		      + ' set status=5,drawback_time=%s WHERE order_id=%s AND uid=%s'
		print(order_id)
		print(self.__shop_db, sql)
		rows = await self.update(sql, (dt,order_id,uid), self.__shop_db)
		return rows
	#取消订单
	async def updateOrderToCancel(self, uid, order_id):
		dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		sql = 'UPDATE ' + (constant.MYSQL_ORDER_USER_SHOPPING_ORDER_TABLE) \
		      + ' set status=6,cancel_time=%s WHERE order_id=%s AND uid=%s'
		print(order_id)
		print(self.__shop_db, sql)
		rows = await self.update(sql, (dt,order_id,uid), self.__shop_db)
		return rows