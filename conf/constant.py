DOCUMENT_ROOT = '/data/jigeyi'
# 业务异常
bus_e = {
    # 同一业务业务异常编号相邻
    # 异常名称              编号              msg
    'TEST_ERROE' : {'code' : 10000, 'msg' : 'test err'},
}

# redis key
REDIS_SHOP_DETAIL_HOST = 'shop_detail_host_%s'      #商店根据域名获取详情
REDIS_USER_ID = 'user_detail_id_%s'                 #用户根据id获取详情

#mysql key
MYSQL_JIGEYI_DB = 'jigeyi'
#商城数据库表名
MYSQL_SHOPPING_MALL_MATERIAL_TABLE = 'sm_material_kind_%s'
MYSQL_SHOPPING_MALL_RECIPE_TABLE = 'sm_recipe_%s'
MYSQL_SHOP_TABLE = 'shop'
MYSQL_SHOPPING_MALL_KIND_TABLE = 'sm_material_kind_info'
MYSQL_SHOPPING_MALL_MATERIAL_RELATE_RECIPE_TABLE = 'sm_material_relate_recipe'
MYSQL_SHOPPING_MALL_RECIPE_DAILY_TABLE = 'sm_recipe_daily'
MYSQL_SHOPPING_MALL_SHOP_CAR_TABLE = 'sm_shop_car'
MYSQL_ORDER_USER_SHOPPING_ORDER_TABLE = 'order_user_shopping_order'