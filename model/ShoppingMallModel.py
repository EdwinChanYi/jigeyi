#!/usr/bin/env python
#-*- coding: utf-8 -*-

from model import BaseModel
from conf import constant

class ShoppingMallModel(BaseModel):
    __db = constant.MYSQL_SHOPPING_MALL_DB
    __material_table = constant.MYSQL_SHOPPING_MALL_MATERIAL_TABLE
    __recipe_table = constant.MYSQL_SHOPPING_MALL_RECIPE_TABLE

    @classmethod
    async def findAllKindsOfMaterialKindByCode(self, code):
        sql = 'SELECT kind_id,kind_name FROM %s GROUP BY kind_id'
        row = await self.one(sql, (self.__material_table%code), self.__db)
        return row
    @classmethod
    async def findAllKindsOfMaterialByCode(self, code, kind_id):
	    sql = 'SELECT material_id,material_name FROM %s WHERE kind_id = %d'
	    row = await self.one(sql, (self.__recipe_table % code, kind_id), self.__db)
	    return row