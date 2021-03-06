#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 路由文件，遵守restful规范
# 格式 : (路径, 处理器, 构造函数参数, 名称)
# 注意:名称不可重复

from handler import *

route = [
    (r"/", TestHandler, None, '检测入口'),
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
    (r"/shoppingmallMaterialDetail", ShoppingMallHandelr.ShoppingMallMaterialDetailHandler, None, '商城食材详情'),
    (r"/shoppingmallRecipeDetail", ShoppingMallHandelr.ShoppingMallRecipeDetailHandler, None, '商城菜谱详情'),
    #订单
    (r"/orderQueryAllOrders", OrderHandler.OrderQueryAllOrdersByUserHandler, None, '查询所有订单'),
    (r"/orderQueryWaitPayOrders", OrderHandler.OrderQueryWaitPayOrdersByUserHandler, None, '查询待付款订单'),
    (r"/orderQueryWaitSendOrders", OrderHandler.OrderQueryWaitSendOrdersByUserHandler, None, '查询待发货订单'),
    (r"/orderQueryWaitMakeSureOrders", OrderHandler.OrderQueryWaitMakeSureOrdersByUserHandler, None, '查询待确认订单'),
    (r"/orderQueryFinishOrders", OrderHandler.OrderQueryFinishOrdersByUserHandler, None, '查询完成订单'),
    (r"/orderPlaceOrders", OrderHandler.OrderPlaceOrdersHandler, None, '下单'),
    (r"/orderSendOrder", OrderHandler.OrderSendOrderHandler, None, '发货'),
    (r"/orderMakeSureOrder", OrderHandler.OrderMakesureOrderHandler, None, '确认收货'),
    (r"/orderDrawbackOrder", OrderHandler.OrderDrawbackOrderHandler, None, '退款'),
    (r"/orderCancelOrder", OrderHandler.OrderCancelOrderHandler, None, '取消'),
    (r"/orderPayOrder", OrderHandler.OrderPayOrderHandler, None, '付款'),
    # 商店
    (r"/shops/([0-9]+)", ShopHandler, None, '获取商店，上线屏蔽'),
    # 微信
    (r"/wechatOauthUrl", WechatHandler, None, '获取微信授权地址'),
    (r"/wechatVerify", WechatVerifyHandler, None, '微信接入验证'),
    (r"/wechatMenu", WechatMenuHandler, None, '微信公众号菜单设置'),
    (r"/wechatAuthCallback", WechatCallbackHandler, None, '微信授权回调'),
    (r"/wechatPush", WechatHandler, None, '模板推送,测试'),
]