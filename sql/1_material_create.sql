CREATE TABLE `material_kind_` (
  `material_id` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '食材id',
  `kind_id` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '食材类id',
  `material_name` VARCHAR(255) NOT NULL DEFAULT '' COMMIT '食材名'
  `kind_name` VARCHAR(255) NOT NULL DEFAULT '' COMMIT '食材类名'
  `price` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '食材价格',
  `image` VARCHAR(255) DEFAULT '' COMMIT '图片 ps:json格式存储'
  `description` VARCHAR(255) DEFAULT '' COMMIT '描述 ps:json格式存储'
  `create_time` int(11) NOT NULL DEFAULT '0' COMMENT '创建时间',
  `update_time` int(11) DEFAULT NULL COMMENT '最近更新时间',
  PRIMARY KEY (`material_id`,`kind_id`),
  KEY (`material_name`,`kind_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户表'