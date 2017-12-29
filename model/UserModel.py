#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 用户模型

from model import BaseModel

class UserModel(BaseModel):

    async def findById(self, id):
        sql = 'select * from user where id = %s limit 1'
        row = await self.one(sql, (id), self.get_db())
        return row

    async def createUser(self, code, nickname, password):
        sql = 'insert into user (code, nickname, password) values (%s, %s, %s)'
        ret = await self.insert(sql, (code, nickname, password), self.get_db())
        return ret

    async def updateUserNickname(self, id, nickname):
        sql = 'update user set nickname = %s where id = %s limit 1'
        ret = await self.update(sql, (nickname, id), self.get_db())
        return ret

    async def deleteUser(self, id):
        sql = 'delete from user where id = %s limit 1'
        ret = await self.update(sql, (id), self.get_db())
        return ret