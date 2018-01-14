CREATE TABLE `material_recipe` (
  `material_id` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '食材id',
  `recipe_id` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '菜谱id',
  `create_time` TIMESTAMP NOT NULL COMMENT '创建时间',
  `update_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最近更新时间',
  PRIMARY KEY (`material_id`,`recipe_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户表'