
from controller import BaseHandler
import tornado.web
from voluptuous import *
from common.Decorate import apiCounter,redisGet
import time
from json import loads,dumps
from model import ShopModel

class TestHandler(BaseHandler):

    def param_filter(self):
        return {
            'GET': Schema({
                Required('a'): str,
                'page': str
            })
        }

    @apiCounter(max=10)
    @tornado.web.authenticated
    async def get(self):
        param = self.get_param()
        print(param)
        time.sleep(1)
        pass;

    @redisGet('a', (), True, True)
    async def post(self, a='abc'):
        print(1)
        param = self.get_param()
        print(param)
        print(2)
        return 'hahaha'

    @apiCounter(max=1000)
    async def put(self):
        param = self.get_param()
        a = ShopModel()
        # time.sleep(2)
        res = await a.oneByHost(param.get('host'))
        self.json_ret(res)