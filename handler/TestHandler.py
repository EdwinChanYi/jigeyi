
from handler import BaseHandler
import tornado.web
from voluptuous import *
from common.Decorate import apiCounter,redisGet
import time
from json import loads,dumps
from model import BaseModel

from common import Db

class TestHandler(BaseHandler):

    def param_filter(self):
        return {
            'GET': Schema({
                Required('a'): str,
                'page': str
            })
        }

    async def get(self):
        a = BaseModel.instance()
        b = BaseModel.instance()
        print(a == b)
        a.setDefaultMod('hhh')
        pass;

    # @redisGet('a', (), True, True)
    async def post(self, a='abc'):
        print(1)
        param = self.get_param()
        print(param)
        print(2)
        self.json_ret(200, 'ok')
