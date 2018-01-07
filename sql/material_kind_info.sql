CREATE TABLE `material_kind_info` (
  `kind_id` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '食材类id',
  `kind_name` VARCHAR(255) NOT NULL DEFAULT '' COMMENT '食材类名',
  `image` VARCHAR(255) DEFAULT '' COMMENT '图片 ps:json格式存储',
  `description` VARCHAR(255) DEFAULT '' COMMENT '描述 ps:json格式存储',
  `status` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '数据状态 -1表示删除 0表示使用 1表示屏蔽',
  `create_time` int(11) NOT NULL DEFAULT '0' COMMENT '创建时间',
  `update_time` int(11) DEFAULT NULL COMMENT '最近更新时间',
  PRIMARY KEY (`kind_id`),
  KEY (`kind_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='商店食材表'