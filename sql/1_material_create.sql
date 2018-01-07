CREATE TABLE `material_kind_` (
  `material_id` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '食材id',
  `kind_id` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '食材类id',
  `material_name` VARCHAR(255) NOT NULL DEFAULT '' COMMIT '食材名',
  `kind_name` VARCHAR(255) NOT NULL DEFAULT '' COMMIT '食材类名',
  `repertory` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '库存量',
  `common_price` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '食材普通价格',
  `discount_price` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '食材优惠价格',
  `unit` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '食材单位 跟价格共用',
  `material_image` VARCHAR(255) DEFAULT '' COMMIT '图片 ps:json格式存储',
  `area` VARCHAR(255) DEFAULT '' COMMIT '产地',
  `storage_condition` VARCHAR(255) DEFAULT '' COMMIT '存储条件',
  `introduction` VARCHAR(5000) DEFAULT '' COMMIT '食材介绍',
  `status` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '数据状态 -1表示删除 0表示使用 1表示屏蔽',
  `create_time` int(11) NOT NULL DEFAULT '0' COMMENT '创建时间',
  `update_time` int(11) DEFAULT NULL COMMENT '最近更新时间',
  PRIMARY KEY (`material_id`,`kind_id`),
  KEY (`material_name`,`kind_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='商店食材表'