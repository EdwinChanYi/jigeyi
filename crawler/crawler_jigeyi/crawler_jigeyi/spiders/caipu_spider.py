#coding:utf-8
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
import time
import json
import sys
from crawler_jigeyi.items import CrawlerJigeyiItem
from crawler_jigeyi.items import CrawlerJigeyiRecipeItem
from crawler_jigeyi.items import CrawlerJigeyiMaterialToRecipeItem
optional_features.remove('boto')
class CaipuSpider(scrapy.spiders.Spider):
	name="caipu"
	allowed_domains = ["haodou.com"]
	start_urls = [
	        "http://www.haodou.com/recipe/food/",
			    ]
	#all cai
	def parse(self, response):
		print response.url
		items_para = response.xpath('''//div[@class="warpb clearfix"]/div[@class="auto"]/div[@class="fl area_gp"]
								/div[@class="auto pdt20"]''') 
		print("hello world")
		print items_para
		url = items_para.xpath('./a[@class="fr more"]/@href').extract()
		print url		
		for tmp in url:
			material = "http:"+tmp.encode("utf-8")
			print material
			yield Request(material, callback=self.material_parse)
			time.sleep(1)
	#cai
	def material_parse(self, response):
		print response.url
		items_para = response.xpath('//div[@class="warpb clearfix"]/div[@class="auto pdt10 fs"]') 
		print("hello world")
		print items_para
		src = items_para.xpath('.//div[@class="auto mgt5"]/h2/text()').extract()
		name = items_para.xpath('.//div[@class="recipe_makings_more"]/h3/text()').extract() 
		print name				
		for j in range(len(name)):
			print name[j].encode("utf-8")
				
		caiName = items_para.xpath('.//div[@class="recipe_makings_more"]/ul/li/a/@title').extract()
		caiImage = items_para.xpath('.//div[@class="recipe_makings_more"]/ul/li/a/img/@src').extract()
		caiLinkVec = items_para.xpath('.//div[@class="recipe_makings_more"]/ul/li/a/@href').extract()
		caiImage2 = items_para.xpath('.//div[@class="recipe_makings_more"]/ul/li/a/img/@original').extract()
		l = 0
		for k in range(len(caiName)):
			caiLinkTmp = caiLinkVec[k].encode("utf-8")
			image = caiImage[k]
			if image=="http://www.haodou.com/public/images/blank.gif":
				image = caiImage2[l]
				l = l+1
			print caiName[k].encode("utf-8")
			print caiImage[k].encode("utf-8")
			print image.encode("utf-8")
			print caiLinkTmp[2:]
			caiLink = "http:"+caiLinkTmp
			file_name = "%s.jpg" % (caiName[k].encode('utf-8'))
			file_path = os.path.join("/home/chenyiwei/jigeyi/jigeyi/crawler/cai", file_name)
			#urllib.urlretrieve(image.encode("utf-8"), file_path)
			yield Request(caiLink, callback=self.cai_parse)
			time.sleep(1)
		
	def cai_parse(self,response):
		print response.url
		items_para = response.xpath('//div[@class="box"]')
		#get cai image
		material_image = response.xpath('//div[@id="leftTopFloat"]/img/@src').extract()
		#get cai name
		material_name = items_para.xpath('./h1[@id="food_title"]/text()').extract()
		#get material big id
		material_big_id_tmp = response.xpath('''//div[@class="warpb clearfix"]
										/div[@class="auto pdt20 fs"]/a[contains(./@href,
										'www.haodou.com/recipe/food/cate/')]/@href''').extract()

		material_big_name_tmp = response.xpath('''//div[@class="warpb clearfix"]
										/div[@class="auto pdt20 fs"]/a[contains(./@href,
										'www.haodou.com/recipe/food/cate/')]/@title''').extract()
		material_big_name = material_big_name_tmp[0].encode("utf-8")
		print "here is :",__file__,sys._getframe().f_lineno,material_big_id_tmp[0].encode("utf-8")
		material_link = material_big_id_tmp[0].encode("utf-8")
		material_big_id = material_link[34::].encode("utf-8")
		print material_big_id,material_big_name
		#get cai small id
		material_small_id = items_para.xpath('./h1[@id="food_title"]/@data').extract()
		file_name = "mat_img_%s.jpg" % (material_small_id[0].encode('utf-8'))
		file_path = os.path.join("/home/chenyiwei/jigeyi/jigeyi/crawler/cai", file_name)
		print file_path
		urllib.urlretrieve(material_image[0].encode("utf-8"), file_path)
		print material_image
		print items_para
		intro_items_para = items_para.xpath('./p[@class="mgt20"]')
		#cai introduction
		introdution_detail = {}
		for tmp in intro_items_para:
			key = tmp.xpath('./b/text()').extract()
			value = tmp.xpath('./text()').extract()
			if value:
				print value[0].encode("utf-8")
				introdution_detail[key[0].encode("utf-8")] = value[0].encode("utf-8")
		introdution_json = json.dumps(introdution_detail)
		make_items_para = items_para.xpath('./div[@class="auto mgt20"]')
		#get recipe link
		make_method = make_items_para.xpath('./a[@class="fr more"]/@href').extract()
		recipe_big_id = material_big_id
		print "recipe_big_id:",recipe_big_id
		recipe_link = "http:"+make_method[0]
		print recipe_link
		#material detail
		matetial_detil_dict = {}
		#cai effect
		effect_key_items_para = items_para.xpath('''./a[@name="effect"]/following-sibling::
									div[@class="auto mgt20"]/h2/text()''').extract()
		effect_value_items_para = items_para.xpath('''./a[@name="effect"]/following-sibling::div[@class="auto mgt20"]/
									following-sibling::p[@class="mgt10"][1]/text()''').extract()
		print effect_key_items_para[0].encode("utf-8")
		effect_value_list = []
		for effect_item_tmp in effect_value_items_para:
			print effect_item_tmp.encode("utf-8")
			effect_value_list.append(effect_item_tmp.encode("utf-8"))
		matetial_detil_dict[effect_key_items_para[0].encode("utf-8")] = effect_value_list
		#cai shuxing excepct effect
		shuxing_items_para = items_para.xpath('./a/@name').extract()
		for shuxing_tmp in shuxing_items_para:
			if shuxing_tmp=="effect":
				continue
			go_pick_key_items_para = items_para.xpath('''./a[@name="%s"]/
							following-sibling::h2[@class="mgt20"][1]/text()''' % shuxing_tmp).extract()
			g_pick_value_items_para = items_para.xpath('''./a[@name="%s"]/following-sibling::
									p[@class="mgt10"][1]/text()'''%shuxing_tmp).extract()
			if go_pick_key_items_para:
				print go_pick_key_items_para[0].encode("utf-8")
				g_pick_value_list = []
				for tmp in g_pick_value_items_para:
					print tmp.encode("utf-8")
					g_pick_value_list.append(tmp.encode("utf-8"))
				matetial_detil_dict[go_pick_key_items_para[0].encode("utf-8")] = g_pick_value_list
		material_dict = {}
		material_dict["introduct"] = introdution_detail
		material_dict["detial"] = matetial_detil_dict
		material_json = json.dumps(material_dict)
		print material_json
		material_all_file_path = "material_%s.json"%(material_small_id[0].encode('utf-8'))
		#get tuijian recipe id
		tuijian_items_para = items_para.xpath('''./div[@class="rc_igd_im_list mgt10"]/ul/li/a/@href''').extract()	
		for tmp in tuijian_items_para:
			print tmp[24:]
		Item=CrawlerJigeyiItem()
		Item['materialBigId'] = material_big_id
		Item['materialSmallId'] = material_small_id[0].encode("utf-8")
		Item['materialName'] = material_name[0].encode("utf-8")
		Item['materialPic'] = file_name
		Item['matRecipeBigId'] = recipe_big_id.encode("utf-8")
		Item['materialIntroduct'] = material_all_file_path
		Item['materialBigName'] = material_big_name
		Item['itemType'] = "1"
		yield Item
		yield Request(recipe_link, callback=self.kind_recipe_parse)
	#recipe 
	def kind_recipe_parse(self,response):
		print response.url
		items_para = response.xpath('''//div[@class="recipe_all_list clearfix mgt20"]/
							ul/li/div[@class="picList"]/p[@class="bigimg"]
							/a[@target="_blank"]/@href''').extract()
		print "recipe:"
		#Item = 
		print items_para
		for recipe in items_para:
			recipe_link = "http://www.haodou.com"+recipe.encode("utf-8")
			print recipe_link
			yield Request(recipe_link, callback=self.recipe_parse)
			time.sleep(1)
		
	def recipe_parse(self, response):
		print response.url
		items_para = response.xpath('''//div[@class="warpb clearfix pdt20"]
								/div[contains(@class,"fl area")]''')
		itemid = items_para.xpath('''./@itemid''').extract()
		print itemid[0].encode("utf-8")
		recipe_small_id = itemid[0].encode("utf-8")
		recipe_name = items_para.xpath('''./div[@class="concrete"]
						/div[@class="box"]
						/h1[@id="stitle"]/a[@target="_blank"]/text()''').extract()
		recipe_img = items_para.xpath('''./div[@class="concrete"]
		                         /div[@class="listRol"]
		                         /div[@class="ulCon  ulCont-video"]
								 /img[@class="recipe_cover"]/@src''').extract()
		if len(recipe_name)==0:
			recipe_name = items_para.xpath('''./div[@class="rec_con_lar"]
			                         /div[@class="large"]
			                         /img[@id="showcover"]/@alt''').extract()
			recipe_img = items_para.xpath('''./div[@class="rec_con_lar"]
			                         /div[@class="large"]
			                         /img[@id="showcover"]/@src''').extract()
		intro_items_para = items_para.xpath('''./div[@class="concrete"]/div[@class="intro"]
									/dl[@class="des"]''')
		if intro_items_para:
			jianjie = intro_items_para.xpath('''./dt/text()''').extract()
			xiangqing = intro_items_para.xpath('''./dd/span/@data''').extract()
		
		print recipe_img[0].encode("utf-8")
		print recipe_name[0].encode("utf-8")
		recipe_name_str = recipe_name[0].encode("utf-8")
		recipe_img_str = recipe_img[0].encode("utf-8")
		#TODO
		recipe_imge_file_name = "recipe_img_%s.jpg"%recipe_small_id
		introduction = {}
		if jianjie:
			print jianjie[0].encode("utf-8")
			introduction['jianjie'] = jianjie[0].encode("utf-8")
		if xiangqing:
			print xiangqing[0].encode("utf-8")
			introduction['xiangqing'] = xiangqing[0].encode("utf-8")
		#TODO
		introduct_file_name = "recipe_intr_%s.json"%recipe_small_id
		material_items_para = items_para.xpath('''./div[@class="concrete"]/div[@class="intro"]
									/div[@class="material"]''')
		shicai_items_para = material_items_para.xpath('''./h2/text()''').extract()
		if shicai_items_para:
			print shicai_items_para[0].encode("utf-8")
		liao_items_para = material_items_para.xpath('''./ul/li[@class="imit_h2"]/text()''').extract()
		print liao_items_para
		zhuliao_list = []
		fuliao_list = []
		for liao_tmp in liao_items_para:
			if liao_tmp.encode("utf-8")=="主料":
				zhuliao_dict = {}
				intmgr_items_para = material_items_para.xpath('''./ul/li[@class="ingtmgr"]''')
				_zhuliao_name = intmgr_items_para.xpath('''./p/a/text()''').extract()
				zhuliao_amount = intmgr_items_para.xpath('''./span/text()''').extract()
				print liao_tmp.encode("utf-8")
				for i in range(len(_zhuliao_name)):
					print _zhuliao_name[i].encode("utf-8")
					print zhuliao_amount[i].encode("utf-8")
					zhuliao_dict['name'] = _zhuliao_name[i].encode('utf-8')
					zhuliao_dict['amount'] = zhuliao_amount[i].encode('utf-8')
					zhuliao_list.append(zhuliao_dict)
			if liao_tmp.encode("utf-8")=="辅料":
				fuliao_dict = {}
				intmgr_items_para = material_items_para.xpath('''./ul/li[@class="ingtbur"]''')
				fuliao_name = intmgr_items_para.xpath('''./p/text()''').extract()
				fuliao_amount = intmgr_items_para.xpath('''./span/text()''').extract()
				print liao_tmp.encode("utf-8")
				for i in range(len(fuliao_name)):
					print fuliao_name[i].encode("utf-8")
					print fuliao_amount[i].encode("utf-8")
					fuliao_dict['name'] = fuliao_name[i].encode("utf-8")
					fuliao_dict['amount'] = fuliao_amount[i].encode("utf-8")
					fuliao_list.append(fuliao_dict)

		step_items_para = items_para.xpath('''./div[@class="concrete"]/div[@class="intro"]
									/dl[@class="step"]''')
		buzhou_items_para = step_items_para.xpath('''./dt/text()''').extract()
		print buzhou_items_para
		num_items_para = step_items_para.xpath('''./dd/input/@itemnum''').extract()
		img_items_para = step_items_para.xpath('''./dd/div/img/@src''').extract()
		p_itmes = step_items_para.xpath('''./dd/p/text()''').extract()
		step_list = []
		for i in range(len(num_items_para)):
			print num_items_para[i]
			print img_items_para[i]
			print p_itmes[i]
			step_num = num_items_para[i].encode('utf-8')
			step_image_file_name = "step_image_%s_%s.jpg"%(recipe_small_id,step_num)
			step_intro = p_itmes[i].encode('utf-8')
			step_dict = {}
			step_dict['step_num'] = step_num
			step_dict['step_image'] = step_image_file_name
			step_dict['step_intro'] = step_intro
			step_list.append(step_dict)
		step_detail_dict = {}
		step_detail_dict['main_food'] = zhuliao_list
		step_detail_dict['assisted_food'] = fuliao_list
		step_detail_dict['step'] = step_list
		print step_detail_dict
		#TODO
		step_file_name = "recipe_step_%s.json"%recipe_small_id
		Item = CrawlerJigeyiRecipeItem()
		Item['recipeId'] = recipe_small_id
		Item['recipeName'] = recipe_name_str
		Item['recipeIntroduct'] = introduct_file_name
		Item['recipeStep'] = step_file_name
		Item['recipeImage'] = recipe_imge_file_name
		Item['itemType'] = "2"
		yield Item
