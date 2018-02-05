CREATE TABLE `sm_shop_car` (
  `uid` int(64) unsigned NOT NULL DEFAULT '0' COMMENT '用户ID',
  `shop_code` VARCHAR(1000) NOT NULL DEFAULT '' COMMENT '商店标识',
  `material_id` int(64) unsigned NOT NULL DEFAULT '0' COMMENT '食材ID',
  `num` int(64) unsigned NOT NULL DEFAULT '0' COMMENT '食材ID',
  `create_time` DATETIME NOT NULL COMMENT '创建时间',
  `update_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最近更新时间',
  PRIMARY KEY (`uid`,`material_id`),
  INDEX(`create_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='订单表'