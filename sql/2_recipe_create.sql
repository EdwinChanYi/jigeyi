CREATE TABLE `recipe_%s` (
  `material_id` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '食材id',
  `recipe_id` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '菜谱id',
  `recipe_name` VARCHAR(255) NOT NULL DEFAULT '' COMMENT '菜谱名',
  `material_name` VARCHAR(255) NOT NULL DEFAULT '' COMMENT '食材名',
  `image` VARCHAR(255) DEFAULT '' COMMENT '图片 ps:json格式存储',
  `description` VARCHAR(255) DEFAULT '' COMMENT '描述 ps:json格式存储',
  `create_time` int(11) NOT NULL DEFAULT '0' COMMENT '创建时间',
  `update_time` int(11) DEFAULT NULL COMMENT '最近更新时间',
  PRIMARY KEY (`material_id`,`recipe_id`),
  KEY (`material_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户表'