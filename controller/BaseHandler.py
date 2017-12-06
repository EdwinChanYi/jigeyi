#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 控制器基类，所有控制器必须继承

import tornado.web
from voluptuous import *
import sys
sys.path.append('../')
from model import BaseModel
from conf import constant
from common import Logger

class BaseHandler(tornado.web.RequestHandler):
    __param = None

    # 参数过滤器
    # @https://pypi.python.org/pypi/voluptuous/0.10.5
    def param_filter(self):
        return {
            'GET' : Schema({
                Required('q') : str,
                'page' : int
            }),
            'POST': Schema({
                Required('q'): str,
                'page': int
            })
        }

    # 获取参数
    def get_param(self):
        if self.__param is None:
            param = {}  # 所有参数字典
            args = self.request.arguments
            for key in args:
                param[key] = self.get_argument(key)
            schema = self.param_filter().get(self.request.method)
            if schema is not None:
                try:
                    schema(param)
                except MultipleInvalid as e:
                    print('eee')
                    self.json_ret(201, str(e))
            self.__param = param

        return self.__param

    # 登录验证,暂时写死
    def get_current_user(self):
        return 1

    # 初始化
    def prepare(self):
        params = self.get_param()
        uid = self.get_current_user()
        uri = self.request.uri
        remote_ip = self.request.remote_ip
        method = self.request.method
        msg = "uid[%s],method[%s],remote_ip[%s],uri[%s],param[%s]" % (uid, method, remote_ip, uri, params)
        log = Logger.get_log('main.log', True)
        log.info(msg)
        # TODO
        host = 'aa.com'
        a = 'aa'


    # 清理和日志
    def on_finish(self):
        BaseModel.close()
        print('on_finish')

    # 返回json
    def json_ret(self, code=200, msg='', data={}):
        ret = {'code': code, 'msg': msg, 'data': data}
        self.finish(ret)

    # 非业务异常统一处理，TODO 加告警
    def write_error(self, status_code, **kwargs):
        self.json_ret(status_code, 'internal error')

    @tornado.web.authenticated
    async def get(self):
        # self.get_param()
        # self.finish({'message': 'ok'})
        # raise tornado.web.HTTPError('test')
        # ret = await self.sleep(
        user_id = self.current_user
        # gen.Return(ret)
        self.json_ret(200, user_id, {'a': 2})

    async def sleep(self):
        await tornado.gen.sleep(2)
        return 'hello'

    async def post(self):
        base_model = BaseModel.instance()
        res = await base_model.insert('insert into test(name) values(%s)', ('zhou12'))
        await base_model.commit()
        print(res)

    def __del__(self):
        print('over')


    # 抛出业务异常并结束请求
    def bus_exce_ret(self, e):
        if constant.bus_e.get(e) is not None:
            e = constant.bus_e.get(e)
            self.json_ret(e.get('code'), e.get('msg'))
        else:
            self.json_ret(500, 'undefined err')


if __name__ == "__main__":
    pass