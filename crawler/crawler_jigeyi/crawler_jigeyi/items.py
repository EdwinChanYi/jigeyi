# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerJigeyiItem(scrapy.Item):
    # define the fields for your item here like:
	materialBigId = scrapy.Field()
	materialSmallId = scrapy.Field()
	materialSmallType = scrapy.Field()
	materialName = scrapy.Field()
	materialBigName = scrapy.Field()
	materialPic = scrapy.Field()
	matRecipeBigId = scrapy.Field()
	materialIntroduct = scrapy.Field()
	itemType = scrapy.Field()
class CrawlerJigeyiRecipeItem(scrapy.Item):
	recipeId = scrapy.Field()
	recipeName = scrapy.Field()
	recipeIntroduct =  scrapy.Field()
	recipeStep =  scrapy.Field()
	recipeImage = scrapy.Field()
	itemType = scrapy.Field()
class CrawlerJigeyiMaterialToRecipeItem(scrapy.Item):
	matSmallId = scrapy.Field()
	recSmallId = scrapy.Field()


