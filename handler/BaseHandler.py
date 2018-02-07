#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 控制器基类，所有控制器必须继承

import tornado.web
from voluptuous import *
import sys
sys.path.append('../')
from conf import constant
from common import Logger
from model.ShopModel import *
from module.BaseModule import BaseObj
from common.Function import json_encode
from module import CookieModule

class BaseHandler(tornado.web.RequestHandler):

    __param = None

    # 是否获取商店信息
    _init_shop = True
    
    # 根据域名获取的商店信息
    _shop = None

    # __instance = {}
    #
    # def __call__(self, *args, **kw):
    #     if self not in self.__instance:
    #         self.__instance[self] = super(BaseHandler, self).__call__(*args, **kw)
    #     return self.__instance[self]

    # 参数过滤器
    # @https://pypi.python.org/pypi/voluptuous/0.10.5
    def param_filter(self):
        return {}

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
                    print("get parm",schema.validate(param))
                except MultipleInvalid as e:
                    self.fail_ret(201, str(e))
            self.__param = param
        return self.__param

    # @classmethod
    # def get_db_by_host(cls):
    #     print(cls.request.host)


    # 登录验证,返回用户uid,暂时写死
    def get_current_user(self):
        token = self.get_secure_cookie('token')
        if not token:
            return False
        print('cookie token:' + token)
        cookie_module = CookieModule()
        uid = cookie_module.cookie_decrypt(token)
        return uid

    # 初始化
    async def prepare(self):
        params = self.get_param()
        uid = self.get_current_user()
        uri = self.request.uri
        remote_ip = self.request.remote_ip
        method = self.request.method
        msg = "start:uid[%s],method[%s],remote_ip[%s],uri[%s],param[%s]" % (uid, method, remote_ip, uri, params)
        log = Logger.get_log('main.log', True)
        log.info(msg)
        # 初始化商店信息
        if self._init_shop:
            shop_model = ShopModel()
            self._shop = await shop_model.findByHost(host=self.request.host)

    # 清理和日志
    def on_finish(self):
        params = self.get_param()
        uid = self.get_current_user()
        uri = self.request.uri
        remote_ip = self.request.remote_ip
        method = self.request.method
        msg = "end:uid[%s],method[%s],remote_ip[%s],uri[%s],param[%s]" % (uid, method, remote_ip, uri, params)
        log = Logger.get_log('main.log', True)
        log.info(msg)

    # 返回json
    def json_ret(self, code=200, msg='', data={}):
        ret = {'code': code, 'msg': msg, 'data': data}
        self.finish(ret)

    # 成功返回
    def success_ret(self, data=''):
        if isinstance(data, BaseObj):
            data = data.__dict__
            data = json_encode(data)
        ret = {'code': 200, 'msg': 'ok', 'data': data}
        self.finish(ret)

    # 错误返回
    def fail_ret(self, code=500, msg='error', data={}):
        ret = {'code': code, 'msg': msg, 'data': {}}
        self.finish(ret)

    # 非业务异常统一处理，TODO 加告警
    def write_error(self, status_code, **kwargs):
        self.json_ret(status_code, '发生未知错误,请稍后重试')

    # 析造函数，暂不加逻辑
    def __del__(self):
        print('over')

    # 抛出业务异常并结束请求
    def bus_exce_ret(self, e):
        if constant.bus_e.get(e) is not None:
            e = constant.bus_e.get(e)
            self.json_ret(e.get('code'), e.get('msg'))
        else:
            self.json_ret(500, 'undefined err')

    # 用过域名获取db，失败抛出异常,已弃用
    async def get_db_by_host(self):
        host = self.request.host
        shop_model = ShopModel()
        row = await shop_model.findByHost(host)
        if row:
            return row.get('db')
        else:
            self.json_ret(500, 'no correct db choose')


                    # async def current_user(self):
    #     user_model = UserModel(await self.get_db_by_host())
    #     return await user_model.findById(self.get_current_user())


if __name__ == "__main__":
    pass