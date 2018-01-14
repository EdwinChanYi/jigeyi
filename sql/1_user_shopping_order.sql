CREATE TABLE `order_user_shopping_order` (
  `ordei_id` VARCHAR(1000) NOT NULL DEFAULT '0' COMMENT '订单号',
  `material_id` int(64) unsigned NOT NULL DEFAULT '' COMMENT '食材ID',
   `material_name` VARCHAR(255) NOT NULL DEFAULT '' COMMENT '食材名',
  `image` VARCHAR(255) NOT NULL DEFAULT '' COMMENT '图片 ps:json格式存储',
  `description` VARCHAR(50000) DEFAULT '' COMMENT '描述 ps:json格式存储',
  `material_list` VARCHAR(50000) DEFAULT '' COMMENT '食材列表 ps:json格式存储',
  `step` VARCHAR(50000) NOT NULL DEFAULT '' COMMENT '步骤 ps:json格式存储',
  `tips` VARCHAR(50000) DEFAULT '' COMMENT '小贴士 ps:json格式存储',
  `create_time` TIMESTAMP NOT NULL COMMENT '创建时间',
  `update_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最近更新时间',
  PRIMARY KEY (`ordei_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户表'