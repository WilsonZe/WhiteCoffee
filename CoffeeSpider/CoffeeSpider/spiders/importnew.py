# -*- coding: utf-8 -*-
import scrapy


class ImportnewSpider(scrapy.Spider):
    name = 'importnew'
    allowed_domains = ['importnew.com']
    start_urls = ['http://importnew.com/']

    def parse(self, response):
        pass
