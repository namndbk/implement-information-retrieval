# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PhimmoiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name_vi = scrapy.Field()
    name_en = scrapy.Field()
    status = scrapy.Field()
    director = scrapy.Field()
    country = scrapy.Field()
    kind = scrapy.Field()
    actors = scrapy.Field()
    year = scrapy.Field()


