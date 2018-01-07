#!/usr/bin/env python
#-*- coding: utf-8 -*-

from model import BaseModel
from conf import constant
import sys
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

        print(self.__shop_db,sql)

        rows = await self.all(sql, (),self.__shop_db)
        return rows

    async def findMaterialsByCodeAndMaterialKind(self, kind_id, begin, limit):
        sql = 'SELECT material_id,material_name,iamge,common_price,' \
              'discount_price,description,repertory FROM '+\
              self.__material_table%self.__shop_code+\
              ' WHERE kind_id = %d limit %d,%d'
        rows = await self.all(sql, (kind_id, begin, limit), self.__shop_db)
        return rows


    async def findKindsInfoByKindId(self, kinds):
        sql = 'SELECT kind_id,kind_name,image FROM '+self.__kind_table+' kind_id IN('+",".join(kinds)+')'
        print(sql)
        rows = await self.all(sql, self.__db)
        return rows