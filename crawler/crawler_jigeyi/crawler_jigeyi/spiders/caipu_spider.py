import scrapy
from scrapy.selector import Selector
from scrapy.selector import HtmlXPathSelector
from scrapy.http import HtmlResponse
import re
from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy import optional_features
import os
import urllib
optional_features.remove('boto')
class CaipuSpider(scrapy.spiders.Spider):
	name="caipu"
	allowed_domains = ["haodou.com"]
	start_urls = [
	        "http://www.haodou.com/recipe/food/cate/25/",
			    ]
	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		print response.url
		if re.match('http://www.haodou.com/recipe/food/cate/25/', response.url): 
			items = hxs.select('//div[@class="warpb clearfix"]/div') 
			print("hello world")
			print items
			for i in range(len(items)):
				src = hxs.select('//div[@class="warpb clearfix"]/div[@class="auto pdt10 fs"]/div["%d"]/div[@class="auto mgt5"]/h2/text()' % i).extract()
				name = hxs.select('//div[@class="warpb clearfix"]/div[@class="auto pdt10 fs"]/div["%d"]/div[@class="recipe_makings_more"]/h3/text()' % i).extract() 
				print name				
				for j in range(len(name)):
					print name[j].encode("utf-8")
				
				caiName = hxs.select('//div[@class="warpb clearfix"]/div[@class="auto pdt10 fs"]/div["%d"]/div[@class="recipe_makings_more"]/ul/li/a/@title' % i).extract()
				caiImage = hxs.select('//div[@class="warpb clearfix"]/div[@class="auto pdt10 fs"]/div["%d"]/div[@class="recipe_makings_more"]/ul/li/a/img/@src' % i).extract()
				caiLink = hxs.select('//div[@class="warpb clearfix"]/div[@class="auto pdt10 fs"]/div["%d"]/div[@class="recipe_makings_more"]/ul/li/a/@href' % i).extract()

				for k in range(len(caiName)):
					caiLinkTmp = caiLink[k].encode("utf-8")
					print caiName[k].encode("utf-8")
					print caiImage[k].encode("utf-8")
					print caiLinkTmp[2:]
					file_name = "%s.jpg" % (caiName[k].encode('utf-8'))
					file_path = os.path.join("/home/chenyiwei/jigeyi/jigeyi/crawler/cai", file_name)
					urllib.urlretrieve(caiImage[k].encode("utf-8"), file_path)

