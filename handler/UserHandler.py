#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 用户控制器

from handler import BaseHandler
from voluptuous import *
from module import UserModule

class UserHandler(BaseHandler):

    def param_filter(self):
        return {
            'get' : Schema({
                # Required('id'): int,
                extra: PREVENT_EXTRA
            }),
            'post' : Schema({
                Required('code'): str,
                Required('nickname'): str,
                Required('password'): str,
            }),
            'put': Schema({
                Required('nickname'): str,
                extra: PREVENT_EXTRA
            }),
            'delete': Schema({
                Required('id'): int
            }),
        }

    async def get(self, id):
        db = self._shop.get('db')
        user_module = UserModule(db)
        uid = self.get_current_user()
        row = await user_module.getUserInfo(uid)
        self.success_ret(row)

    # async def post(self):
    #     param = self.get_param()
    #     user_model = UserModel(await self.get_db_by_host())
    #     ret = await user_model.createUser(param['code'], param['nickname'], param['password'])
    #     if ret:
    #         self.success_ret()
    #     else:
    #         self.fail_ret()

    async def put(self, id):
        param = self.get_param()
        db = self._shop.get('db')
        user_module = UserModule(db)
        ret = await user_module.updateUserInfo(id, param['nickname'])
        if ret:
            self.success_ret()
        else:
            self.fail_ret()

    # async def delete(self):
    #     param = self.get_param()
    #     user_model = UserModel(await self.get_db_by_host())
    #     ret = await user_model.deleteUser(param['id'])
    #     if ret:
    #         self.success_ret()
    #     else:
    #         self.fail_ret()
