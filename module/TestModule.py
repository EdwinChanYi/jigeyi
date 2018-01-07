#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 测试模块

from module import BaseModule
from model import UserModel
from common.Decorate import redisHget

class TestModule(BaseModule):

    @redisHget('a_%s', 'b', ['1'], True, True, 3600)
    async def getUserInfo(self, id):
        user_model = UserModel(self._db)
        user = await user_model.findById(id)
        return user
