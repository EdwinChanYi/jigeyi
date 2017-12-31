#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 用户模块

from module.BaseModule import BaseObj

class UserModule(object):

    _user_model = None

    def __init__(self, user_model):
        self._user_model = user_model

    async def getUserInfo(self, id):
        row = await self._user_model.findById(id)
        if not row:
            return User()
        user = User(row)
        print(user)
        return user

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
