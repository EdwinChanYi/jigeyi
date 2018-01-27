#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 客户端cookie模块

import time
from module import BaseModule
from common.Function import aes_encrypt, aes_decrypt

class CookieModule(BaseModule):

    COOKIE_PRE = 'JiGeJi'   #cookie前缀
    KEY = 'A7dM0o1.s*s-!d8p'#cookie加密秘钥
    SEPARATOR = ' '         #加密内容间隔符

    # 加密uid和有效结束时间
    def cookie_encrypt(self, uid, expire_time):
        val = []
        val.append(self.COOKIE_PRE)
        val.append(uid)
        val.append(expire_time)
        val = self.SEPARATOR.join(val)
        return aes_encrypt(val, self.KEY)

    # 解密cookie,返回uid或False
    def cookie_decrypt(self, val):
        if not val:
            return False
        val = aes_decrypt(val, self.KEY)
        if not val:
            return False
        val = val.split(self.SEPARATOR)
        if val.length != 3 or val[0] != self.COOKIE_PRE or not val[1].isdigit() or not val[2].isdigit() or int(val[2]) < time.time():
            return False
        return val[1]

