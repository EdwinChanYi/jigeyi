#!/usr/bin/env python
#-*- coding: utf-8 -*-
#商城控制器

from handler import BaseHandler
from voluptuous import *

class ShoppingMallHandler(BaseHandler):
	def param_filter(self):
		return {
			'get': Schema({
				Required('host'): int,
				Required('type'): int,
			}),
		}
	def get(self):
		param = self.get_param()
		shop = param.get('host')
		if not self.adjust(shop):
			return self.fail_ret(data={'para':'error'})

	@classmethod
	def adjust(self, host):
		return False