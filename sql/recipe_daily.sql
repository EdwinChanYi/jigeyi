CREATE TABLE `recipe_daily` (
  `serial` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '序号',
  `recipe_id` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '菜谱id',
  `recipe_name` VARCHAR(255) NOT NULL DEFAULT '' COMMENT '菜谱名',
  `image` VARCHAR(255) NOT NULL DEFAULT '' COMMENT '图片 ps:json格式存储',
  `description` VARCHAR(50000) DEFAULT '' COMMENT '描述 ps:json格式存储',
  `create_time` TIMESTAMP NOT NULL COMMENT '创建时间',
  `update_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最近更新时间',
  PRIMARY KEY (`serial`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户表'