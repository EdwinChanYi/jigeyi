
from handler import BaseHandler
import tornado.web
from voluptuous import *
from common.Decorate import apiCounter,redisGet
import time
from json import loads,dumps
from module.ShopModule import ShopModule
from model.ShopModel import ShopModel
from model.UserModel import UserModel
from module.TestModule import TestModule

from common import Db

class TestHandler(BaseHandler):

    def param_filter(self):
        return {
        }

    async def get(self):
        test_module = TestModule(await self.get_db_by_host())
        res = await test_module.getUserInfo(1)
        self.success_ret(res)

    # @redisGet('a', (), True, True)
    async def post(self, a='abc'):
        model = ShopModel(await self.get_db_by_host())
        res = await model.all('select id from user')
        self.success_ret(res)

