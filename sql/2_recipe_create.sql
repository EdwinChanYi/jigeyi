CREATE TABLE `recipe_%s` (
  `recipe_id` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '菜谱id',
  `recipe_name` VARCHAR(255) NOT NULL DEFAULT '' COMMENT '菜谱名',
  `recipe_video` VARCHAR(255) DEFAULT '' COMMENT '视频',
  `image` VARCHAR(255) NOT NULL DEFAULT '' COMMENT '图片 ps:json格式存储',
  `description` VARCHAR(50000) DEFAULT '' COMMENT '描述 ps:json格式存储',
  `material_list` VARCHAR(50000) DEFAULT '' COMMENT '食材列表 ps:json格式存储',
  `step` VARCHAR(50000) NOT NULL DEFAULT '' COMMENT '步骤 ps:json格式存储',
  `tips` VARCHAR(50000) DEFAULT '' COMMENT '小贴士 ps:json格式存储',
  `create_time` TIMESTAMP NOT NULL COMMENT '创建时间',
  `update_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最近更新时间',
  PRIMARY KEY (`recipe_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户表'