#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 路由文件，遵守restful规范
# 格式 : (路径, 处理器, 构造函数参数, 名称)
# 注意:名称不可重复

from handler import *

route = [
    # 测试
    (r"/test", TestHandler, None, '新增测试'),
    (r"/test/([0-9]+)", TestHandler, None, '删改查测试'),
    # 用户
    (r"/users", UserHandler, None, '新增用户，上线屏蔽'),
    (r"/users/([0-9]+)", UserHandler, None, '删改查用户'),
    #商城
    (r"/shoppingmallKinds", ShoppingMallHandelr.ShoppingMallMaterialKindsHandler, None, '商城食材类列表'),
    (r"/shoppingmallMaterials", ShoppingMallHandelr.ShoppingMallMaterialsHandler, None, '商城食材列表'),
    (r"/shoppingmallRecipeDaily", ShoppingMallHandelr.ShoppingMallRecipeDailyHandler, None, '商城每日菜谱'),
    (r"/shoppingmallRecipeDaily", ShoppingMallHandelr.ShoppingMallMaterialDetailHandler, None, '商城食材详情'),
    (r"/shoppingmallRecipeDaily", ShoppingMallHandelr.ShoppingMallRecipeDetailHandler, None, '商城菜谱详情'),
    # 商店
    (r"/shops/([0-9]+)", ShopHandler, None, '获取商店，上线屏蔽'),
]