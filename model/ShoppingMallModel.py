#!/usr/bin/env python
#-*- coding: utf-8 -*-

from model import BaseModel
from conf import constant
import sys
class ShoppingMallModel(BaseModel):
    super.__db = constant.MYSQL_JIGEYI_DB #公共数据库
    __material_table = constant.MYSQL_SHOPPING_MALL_MATERIAL_TABLE #商城食材表
    __recipe_table = constant.MYSQL_SHOPPING_MALL_RECIPE_TABLE#商城食谱表
    __kind_table = constant.MYSQL_SHOPPING_MALL_KIND_TABLE#商城食材类型表
    def __init__(self, db, code):
        __shop_db = db #店铺数据库
        __code = code
    @classmethod
    async def findMaterialKindsByCode(self, code, begin, limit):
        sql = 'SELECT kind_id FROM '+self.__material_table%code+' GROUP BY kind_id limit %d,%d'
        rows = await self.all(sql, (begin, limit),self.__shop_db)
        return rows
    @classmethod
    async def findMaterialsByCodeAndMaterialKind(self, code, kind_id, begin, limit):
        sql = 'SELECT material_id,material_name,iamge,common_price,' \
              'discount_price,description,repertory FROM '+\
              self.__material_table%code+\
              ' WHERE kind_id = %d limit %d,%d'
        rows = await self.all(sql, (kind_id, begin, limit), self.__shop_db)
        return rows

    @classmethod
    async def findKindsInfoByKindId(self, kinds):
        sql = 'SELECT kind_id,kind_name,image FROM '+self.__kind_table+' kind_id IN('+",".join(kinds)+')'
        rows = await self.all(sql, self.__db)
        return rows