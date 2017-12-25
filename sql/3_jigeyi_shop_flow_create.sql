CREATE TABLE `shop_flow` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `code` varchar(20) NOT NULL DEFAULT '' COMMENT '商店代码',
  `amount` decimal(20,2) NOT NULL DEFAULT '0.00' COMMENT '金额',
  `mark` varchar(255) NOT NULL DEFAULT '' COMMENT '备注',
  `operator` int(11) NOT NULL DEFAULT '0' COMMENT '操作人',
  `create_time` datetime NOT NULL DEFAULT '' COMMENT '最近更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='商店流水表'