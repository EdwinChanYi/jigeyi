#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
sys.path.append('../')
from model import BaseModel

class TestModel(BaseModel):
    pass

if (__name__ == '__main__'):
    a = TestModel.instance()
    b = TestModel.instance()
    print(a == b)
    print(a)
    print(b)
    c = TestModel()
    d = TestModel()
    print(c)
    print(d)
    print(c == d)