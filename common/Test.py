#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
import json

if __name__ == '__main__':
    a = {
        'AUTH_MENU' : 1
    }
    b = json.dumps(a)
    print(b)


