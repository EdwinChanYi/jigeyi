CREATE TABLE `material_kind_1234` (
  `material_id` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '食材id',
  `kind_id` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '食材类id',
  `material_name` VARCHAR(255) NOT NULL DEFAULT '' COMMENT '食材名',
  `kind_name` VARCHAR(255) NOT NULL DEFAULT '' COMMENT '食材类名',
  `repertory` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '库存量',
  `common_price` DOUBLE(12,4) NOT NULL DEFAULT '0' COMMENT '食材普通价格',
  `discount_price` DOUBLE(12,4) NOT NULL DEFAULT '0' COMMENT '食材优惠价格',
  `unit` VARCHAR(100) NOT NULL DEFAULT '0' COMMENT '食材单位 跟价格共用',
  `material_image` VARCHAR(255) DEFAULT '' COMMENT '图片 ps:json格式存储',
  `area` VARCHAR(255) DEFAULT '' COMMENT '产地',
  `storage_condition` VARCHAR(255) DEFAULT '' COMMENT '存储条件',
  `introduction` VARCHAR(5000) DEFAULT '' COMMENT '食材介绍',
  `status` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '数据状态 -1表示删除 0表示使用 1表示屏蔽',
  `create_time` TIMESTAMP NOT NULL COMMENT '创建时间',
  `update_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最近更新时间',
  PRIMARY KEY (`material_id`,`kind_id`),
  KEY (`material_name`,`kind_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='商店食材表'