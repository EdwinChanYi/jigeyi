
from handler import BaseHandler
import tornado.web
from voluptuous import *
from common.Decorate import apiCounter,redisGet
import time
from json import loads,dumps
from module.ShopModule import ShopModule
from model.ShopModel import ShopModel
from model.UserModel import UserModel

from common import Db

class TestHandler(BaseHandler):

    def param_filter(self):
        return {
        }

    async def get(self):
        param = self.get_param()
        host = param['host']
        shop_module = ShopModule(ShopModel(await self.get_db_by_host()))
        shop = await shop_module.findValidShopByHost(host)
        self.success_ret(shop)

    # @redisGet('a', (), True, True)
    async def post(self, a='abc'):
        model = ShopModel(await self.get_db_by_host())
        res = await model.all('select id from user')
        self.success_ret(res)

