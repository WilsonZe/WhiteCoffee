# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

import datetime
import re

from w3lib.html import remove_tags

from utils.commonUtils import date_convert, extract_num, extract_date

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

    def get_insert_sql(self):
        sql = """
            INSERT INTO `coffee_spider`.`t_post`
                (`url`,
                `url_object_id`,
                `title`,
                `date`,
                `post_type`,
                `comments_num`,
                `tag`,
                `original_url`,
                `img_url`,
                `content`)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        url = self["url"][0]
        url_object_id = self["url_object_id"][0]
        title = "".join(self["title"])
        date = date_convert(extract_date(self["date"][0]))
        post_type = "".join(self["post_type"])
        comments_num = extract_num(self["comments_num"][0])
        tag = "".join(self["tag"])
        original_url = self["original_url"][0]
        img_url = self["img_url"][0]
        content = "".join(self["content"])

        params = (url, url_object_id, title, date, post_type, comments_num, tag, original_url, img_url, content)

        return sql, params


