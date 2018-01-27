#!/usr/bin/env python
#-*- coding: utf-8 -*-

from model import BaseModel
from conf import constant
import sys
import time
from common import RedisMgr
class ShoppingMallModel(BaseModel):


    __material_table = constant.MYSQL_SHOPPING_MALL_MATERIAL_TABLE #商城食材表
    __recipe_table = constant.MYSQL_SHOPPING_MALL_RECIPE_TABLE#商城食谱表
    __kind_table = constant.MYSQL_SHOPPING_MALL_KIND_TABLE#商城食材类型表
    def __init__(self, db, code):
        self.__shop_db = db #店铺数据库
        self.__shop_code = code
        self.__db = constant.MYSQL_JIGEYI_DB
    #获取食材类
    async def findMaterialKindsByCode(self, begin, limit):
        sql = 'SELECT kind_id FROM '+(self.__material_table%self.__shop_code)\
              +' GROUP BY kind_id limit '+str(begin)+','+str(limit)
        RedisMgr.getInstance().hset()
        print(self.__shop_db,sql)

        rows = await self.all(sql, (),self.__shop_db)
        return rows
    #获取食材列表
    async def findMaterialsByCodeAndMaterialKind(self, kind_id, begin, limit):
        sql = 'SELECT material_id,material_name,iamge,common_price,' \
              'discount_price,description,repertory FROM '+\
              self.__material_table%self.__shop_code+\
              ' WHERE kind_id = %d limit %d,%d'
        rows = await self.all(sql, (kind_id, begin, limit), self.__shop_db)
        return rows

    #获取食材类信息
    async def findKindsInfoByKindId(self, kinds):
        sql = 'SELECT kind_id,kind_name,image FROM '+self.__kind_table+' WHERE kind_id IN('+",".join(kinds)+')'
        rows = await self.all(sql, (),self.__db)
        return rows

    #获取食谱列表
    async def findDailyRecipeList(self, is_own, begin, limit):
        if limit<=0 or limit>100 or begin<0:
            return
        if is_own:
            recipe_db = self.__shop_db
        else:
            recipe_db = self.__db
        sql = 'SELECT * FROM '+ constant.MYSQL_SHOPPING_MALL_RECIPE_DAILY_TABLE + ' LIMIT ' +str(begin) +','+str(limit)
        print(sql,recipe_db)
        rows = await self.all(sql, (),recipe_db)
        print(rows)
        return rows

    #获取食材详情
    async def findMaterialDetail(self, material_id):
        if material_id<=0:
            return
        material_db = self.__shop_db
        sql = 'SELECT * FROM '+ constant.MYSQL_SHOPPING_MALL_MATERIAL_TABLE%self.__shop_code \
              +'WHERE material_id='+str(material_id)+ ' LIMIT 1'
        print(sql,material_db)
        rows = await self.one(sql, (),material_db)
        print(rows)
        return rows

    #获取菜谱详情
    async def findRecipeDetail(self, is_own, recipe_id):
        if recipe_id<=0:
            return
        if is_own:
            recipe_db = self.__shop_db
        else:
            recipe_db = self.__db
        sql = 'SELECT * FROM '+ constant.MYSQL_SHOPPING_MALL_RECIPE_TABLE%self.__shop_code \
                + 'WHERE recipe_id='+ str(recipe_id) + ' LIMIT 1'
        print(sql,recipe_db)
        rows = await self.one(sql, (),recipe_db)
        print(rows)
        return rows

    #获取关联菜谱
    async def findRecipeRelatedMaterial(self,is_own, material_id):
        if material_id<=0:
            return
        if is_own:
            recipe_db = self.__shop_db
        else:
            recipe_db = self.__db
        sql = 'SELECT * FROM ' + constant.MYSQL_SHOPPING_MALL_MATERIAL_RELATE_RECIPE_TABLE \
              + 'WHERE material_id=' + str(material_id) + ' LIMIT 10'
        print(sql, recipe_db)
        rows = await self.all(sql, (), recipe_db)
        print(rows)
        return rows

    #获取用户购物车列表
    async def findUserShopCarByUid(self, uid, begin, limit):
        if uid <= 0:
            return
        sql = 'SELECT * FROM ' + constant.MYSQL_SHOPPING_MALL_SHOP_CAR_TABLE \
              + 'WHERE uid=' + str(uid) + 'ORDER BY create_time LIMIT ' + str(begin) +','+str(limit)
        shop_db = self.__shop_db
        print(sql, shop_db)
        rows = await self.all(sql, (), shop_db)
        print(rows)
        return rows

    #添加用户购物车
    async def insertAddUserShopCarToUid(self, uid, material_info):
        if uid <= 0:
            return
        sql = 'INSERT INTO ' + constant.MYSQL_SHOPPING_MALL_SHOP_CAR_TABLE \
              + '(uid,shop_code,material_id,num,create_time) VALUES(' +\
                str(uid)+',\''+self.__shop_code + '\',' + str(material_info.get('material_id'))\
                +','+str(material_info.get('num'))+','+str(time.time()) +') ON DUPLICATE KEY UPDATE num = num+'\
                +str(material_info.get('num'))
        shop_db = self.__shop_db
        print(sql, shop_db)
        rows = await self.insert(sql, (), shop_db)
        print(rows)
        return rows

    #修改用户购物车
    async def updateUserShopCarToUid(self, uid, material_info):
        if uid <= 0:
            return
        sql = 'UPDATE ' + constant.MYSQL_SHOPPING_MALL_SHOP_CAR_TABLE \
              + ' set num=' +str(material_info.get('num'))\
              +' WHERE uid='+str(uid)+' AND material_id='+material_info.get('material_id')
        shop_db = self.__shop_db
        print(sql, shop_db)
        rows = await self.insert(sql, (), shop_db)
        print(rows)
        return rows

    #删除购物车
    async def deleteUserShopCarOfUid(self, uid, materials):
        if uid <= 0:
            return
        sql = 'DELETE FROM ' + constant.MYSQL_SHOPPING_MALL_SHOP_CAR_TABLE \
              + ' WHERE uid='+str(uid)+' AND material_id IN('+','.join(materials)+')'
        shop_db = self.__shop_db
        print(sql, shop_db)
        rows = await self.delete(sql, (), shop_db)
        print(rows)
        return rows