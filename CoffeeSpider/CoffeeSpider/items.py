# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CoffeespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ImportnewPostItem(scrapy.Item):

    url = scrapy.Field()
    url_object_id = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    post_type = scrapy.Field()
    comments_num = scrapy.Field()
    tag = scrapy.Field()
    original_url = scrapy.Field()
    img_url = scrapy.Field()
    content = scrapy.Field()


