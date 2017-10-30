# -*- coding: utf-8 -*-
import scrapy


class ImportnewSpider(scrapy.Spider):
    name = 'importnew'
    allowed_domains = ['importnew.com']
    start_urls = ['http://www.importnew.com/all-posts']

    def parse(self, response):
        pass
