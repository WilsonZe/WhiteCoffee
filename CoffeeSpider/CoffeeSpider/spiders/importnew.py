# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse

class ImportnewSpider(scrapy.Spider):
    name = 'importnew'
    allowed_domains = ['importnew.com']
    start_urls = ['http://www.importnew.com/all-posts']

    def parse(self, response):
        post_nodes = response.css('.grid-8 .post.floated-thumb')
        for post_node in post_nodes:
            post_url = post_node.css('.post-thumb a::attr(href)')
            post_img = post_node.css('.post-thumb img::attr(src)')
            yield Request(url=parse.urljoin(response.url, post_url),
                          meta={"post_img": post_img},
                          callback=self.parse_post_detail)

        # post_nodes = response.css('.grid-8 .post-meta .meta-title::attr(href)')

        next_page_url = response.css('.next.page-numbers::attr(href)').extract_first("")
        if next_page_url:
            yield Request(url=parse.urljoin(response.url, next_page_url), callback=self.parse)
        pass

    def parse_post_detail(self, response):
        pass
