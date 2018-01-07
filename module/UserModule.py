#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 用户模块

from module.BaseModule import BaseModule,BaseObj
from model.UserModel import UserModel
from common.Decorate import redisHashObj
from conf.constant import REDIS_USER_ID

class UserModule(BaseModule):

    # @redisHashObj(REDIS_USER_ID, ['nickname'], ['1'])
    async def getUserInfo(self, id):
        user_model = UserModel(self._db)
        row = await user_model.findById(id)
        if not row:
            return User()
        user = User(row)
        return user

    async def updateUserInfo(self, id, nickname):
        user_model = UserModel(self._db)
        ret = await user_model.updateUserNickname(id, nickname)
        if ret > 0:
            return True
        else:
            return False

class User(BaseObj):

    # 自增id,即uid,int
    id = None

    # 商店代码,string
    code = None

    # 密码,string
    password = None

    # 昵称,string
    nickname = None

    # 年龄,int
    age = 0

    # 性别,1:男,2:女,int
    sex = 0

    # 注册时间,int
    register_time = 0

    # 邮箱,string
    email = None

    # 手机号,string
    phone = None

    # 微信open_id,string
    open_id = None

    # 微信union_id,string
    union_id = None

    # 省份,string
    province = None

    # 城市,string
    city = None

    # 状态,-1:禁用,1:正常,int
    status = 1

    # 创建时间,int
    create_time = 0

    # 最近更新时间,int
    undate_time = 0

    def isValid(self):
        return self.status == 1

    # def __init__(self, row):
    #     BaseObj.__init__(row)

    # def __init__(self, row):
    #     self.id = row.get('id')
    #     self.code = row.get('code')
    #     self.password = row.get('password')
    #     self.nickname = row.get('nickname')
    #     self.age = row.get('age')
    #     self.sex = row.get('sex')
    #     self.register_time = row.get('register_time')
    #     self.email = row.get('email')
    #     self.phone = row.get('phone')
    #     self.open_id = row.get('open_id')
    #     self.union_id = row.get('union_id')
    #     self.province = row.get('province')
    #     self.city = row.get('city')
    #     self.status = row.get('status')
    #     self.create_time = row.get('create_time')
    #     self.update_time = row.get('update_time')
