
from handler import BaseHandler
import tornado.web
from voluptuous import *
from common.Decorate import apiCounter,redisGet
import time
from json import loads,dumps
from module.ShopModule import ShopModule
from model.ShopModel import ShopModel
from model.UserModel import UserModel
from module.WechatModule import *

from module.TestModule import TestModule

from common import Db

class TestHandler(BaseHandler):

    def param_filter(self):
        return {
        }

    async def get(self):
        db = self._shop.get('db')
        test_module = TestModule(db)
        res = await test_module.getUserInfo(1)
        self.success_ret(res)

    async def post(self):
        module = WechatModule()
        res = await module.getShopAccessToken('clw')
        self.success_ret(res)

