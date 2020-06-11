import scrapy
from scrapy import Request
from ..items import PhimmoiItem

class PhimmoiSpider(scrapy.Spider):

	name = "phimmoi"
	allowed_domains = ["phimmoi.net"]
	count = 0
	MAX_FILMS = 15000

	def start_requests(self):
		urls = ["http://www.phimmoi.net/phim-bo/", "http://www.phimmoi.net/phim-le/"]
		for url in urls:
			for i in range(1, 170):
				if self.count < self.MAX_FILMS:
					connect_url = url + "page-{}.html".format(str(i))
					yield Request(url=connect_url, callback=self.parse)

	def parse(self, response):
		urls = response.css(".movie-list-index .list-movie .movie-item .block-wrapper ::attr(href)").getall()
		for url in urls:
			if self.count < self.MAX_FILMS:
				self.count += 1
				connect_to_url = response.urljoin(url)
				yield Request(connect_to_url, self.parse_item)
			else:
				break

	def parse_item(self, response):
		item = PhimmoiItem()
		item["name_vi"] = response.xpath("/html/body/div[3]/div[5]/div[1]/div[1]/div[1]/div[1]/div/div[1]/h1/span[1]/a/text()").get().strip()
		item["name_en"] = response.xpath("/html/body/div[3]/div[5]/div[1]/div[1]/div[1]/div[1]/div/div[1]/h1/span[2]/text()").get().strip()
		item["status"] = response.css(".movie-meta-info .movie-dl .movie-dd.status::text").get().strip()
		# item["director"] = response.css("movie-meta-info .movie-dl .movie-dd.dd-director .director::attr(title)").get()
		# item["country"] = response.css("movie-meta-info .movie-dl .movie-dd.dd-country .country::attr(title)").get()
		# item["director"] = response.selector.xpath("/html/body/div[3]/div[5]/div[1]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div[1]/dl/dd[2]")
		# item["country"] = response.xpath("/html/body/div[3]/div[5]/div[1]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div[1]/dl/dd[3]")
		item["year"] = response.xpath('//dd[@class="movie-dd"]/a/text()').get()
		actors = response.xpath('//a[@class="actor-profile-item"]/div[2]/span[1]/text()').getall()
		directors = response.xpath('//a[@class="director"]/text()').getall()
		countries = response.xpath('//dd[@class="movie-dd dd-country"]/a/text()').getall()
		kind = response.css(".movie-meta-info .movie-dl .movie-dd.dd-cat a::text").getall()
		item["actors"] = ", ".join(x.strip() for x in actors)
		item["director"] = ", ".join(x.strip() for x in directors)
		item["country"] = ", ".join(x.strip() for x in countries)
		item["kind"] = ", ".join(x.strip() for x in kind)
		# flag = True
		# for key in item:
		# 	if item[key] is None:
		# 		flag = False
		# 		break
		# if flag is True:
		# 	yield item
		yield item