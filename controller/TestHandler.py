
from controller import BaseHandler
import tornado.web
from voluptuous import *

class TestHandler(BaseHandler):

    def param_filter(self):
        return {
            'GET': Schema({
                Required('a'): str,
                'page': str
            })
        }

    @tornado.web.authenticated
    async def get(self):
        param = self.get_param();
        print(param)
        print('tttt1')
        pass;
