# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from twisted.enterprise import adbapi
import MySQLdb.cursors
import re
import types
import sys
from crawler_jigeyi.items import CrawlerJigeyiItem
class CrawlerJigeyiPipeline(object):
	def __init__(self, dbpool):
		self.dbpool = dbpool
		
	@classmethod
	def from_settings(cls, settings):
		dbparams = dict(
				host=settings['MYSQL_HOST'],  
				db=settings['MYSQL_DBNAME'],
				user=settings['MYSQL_USER'],
				passwd=settings['MYSQL_PASSWD'],
				charset='utf8', 
				cursorclass=MySQLdb.cursors.DictCursor,
				use_unicode=False,
				)
		dbpool = adbapi.ConnectionPool('MySQLdb', **dbparams)
		return cls(dbpool)

	def process_item(self, item, spider):
		if item['itemType']=="1":
			if type(item['materialBigId']) is types.IntType:
				print "type is int"
			print __file__,sys._getframe().f_lineno,item['materialBigId']
			query = self.dbpool.runInteraction(self.material_insert, item)
			query.addErrback(self.handle_error, item, spider)
		elif item['itemType']=="2":
			query = self.dbpool.runInteraction(self.recipe_insert, item)
			query.addErrback(self.handle_error, item, spider)

		return item

	def material_insert(self, tx, item):
		sql = '''replace into jgy_material(big_id,small_id,big_name,name,image,recipe_big_id,introduct) 
					values('''+item['materialBigId']+","+item['materialSmallId']+",'"\
					+item['materialBigName']+"','"+item['materialName']+"','"+item['materialPic']+"',"\
					+item['matRecipeBigId']+",'"+item['materialIntroduct']+"');"
		tx.execute(sql)
	def recipe_insert(self, tx, item):
		sql = '''replace into jgy_recipe(recipe_id,name,image,introduct,step) 
				values('''+item['recipeId']\
				+",'"+item['recipeName']+"','"+item['recipeImage']+"','"\
				+item['recipeIntroduct']+"','"+item['recipeStep']+"')"
		tx.execute(sql)
	def material_create_table(self, tx, item):
		sql = '''CREATE TABLE IF NOT EXISTS jgy_material(big_id bigint(20) NOT NULL,
													small_id bigint(20) NOT NULL,
													name varchar(100) DEFAULT '',
													image varchar(100) DEFAULT '',
													recipe_big_id bigint(20) NOT NULL,
													introduct varchar(100) DEFAULT '',
													PRIMARY KEY(big_id,small_id),
													INDEX(small_id,recipe_big_id))ENGINE=InnoDB DEFAULT CHARSET=utf8;
				'''
		tx.execute(sql)
	def recipe_create_table(self, tx, item):
		sql = '''CREATE TABLE IF NOT EXISTS jgy_recipe(recipe_id bigint(20) NOT NULL,
														name varchar(100) DEFAULT '',
														image varchar(100) DEFAULT '',
														introduct varchar(100) DEFAULT '',
														step varchar(100) DEFAULT '',
														PRIMARY KEY(recipe_id),
														INDEX(name))ENGINE=InnoDB DEFAULT CHARSET=utf8;
														'''
		tx.execute(sql)
	def handle_error(self, failue, item, spider):
		if item['itemType']=="1":
			self.dbpool.runInteraction(self.material_create_table, item)
			self.dbpool.runInteraction(self.material_insert, item)
			print item['materialBigId']
			print '''handel_error'''
		elif item['itemType']=="2":
			self.dbpool.runInteraction(self.recipe_create_table, item)
			self.dbpool.runInteraction(self.recipe_insert, item)


