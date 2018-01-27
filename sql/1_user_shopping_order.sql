CREATE TABLE `order_user_shopping_order` (
  `ordei_id` VARCHAR(1000) NOT NULL DEFAULT '' COMMENT '订单号',
  `wetchat_order_id` VARCHAR(1000) NOT NULL DEFAULT '' COMMENT '微信订单号',
  `status` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '订单状态 0表示无效 1表示未付款 2表示已发收货 3表示待收货 4表示已完成 5表示退款 6表示取消订单',
  `uid` int(64) unsigned NOT NULL DEFAULT '0' COMMENT '用户ID',
  `shop_code` VARCHAR(1000) NOT NULL DEFAULT '' COMMENT '商店标识',
  `material_infos` VARCHAR(1000) NOT NULL DEFAULT '' COMMENT
    '购买物品列表 json格式 [{"material_id":11,"price":1.2,"num":10,"discount_ammount":1}]',
  `contract` VARCHAR(1000) NOT NULL DEFAULT '' COMMENT '联系方式 {"phone":"13570432443","address":"世世代代"}',
  `create_time` DATETIME NOT NULL COMMENT '创建时间',
  `pay_time` DATETIME NULL COMMENT '付款时间',
  `send_time` DATETIME NULL COMMENT '发货时间',
  `finish_time` DATETIME NULL COMMENT '成交时间',
  `drawback_time` DATETIME NULL COMMENT '退款时间',
  `cancel_time` DATETIME NULL COMMENT '取消时间',
  `update_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最近更新时间',
  PRIMARY KEY (`ordei_id`),
  INDEX(`uid`),
  INDEX(`shop_code`),
  INDEX(`status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='订单表'