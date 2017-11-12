# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse
from scrapy.loader import ItemLoader
from items import ImportnewPostItem

from utils.commonUtils import get_md5

class ImportnewSpider(scrapy.Spider):
    name = 'importnew'
    allowed_domains = ['importnew.com']
    start_urls = ['http://www.importnew.com/all-posts']

    def parse(self, response):
        post_nodes = response.css('.grid-8 .post.floated-thumb')
        for post_node in post_nodes:
            post_url = post_node.css('.post-thumb a::attr(href)').extract_first("")
            post_img = post_node.css('.post-thumb img::attr(src)').extract_first("")
            yield Request(url=parse.urljoin(response.url, post_url),
                          meta={"post_img": post_img},
                          callback=self.parse_post_detail)

        # post_nodes = response.css('.grid-8 .post-meta .meta-title::attr(href)')

        # next_page_url = response.css('.next.page-numbers::attr(href)').extract_first("")
        # if next_page_url:
        #     yield Request(url=parse.urljoin(response.url, next_page_url), callback=self.parse)
        # pass

    def parse_post_detail(self, response):
        item_loader = ItemLoader(item=ImportnewPostItem(), response=response)

        item_loader.add_value("url", response.url)
        item_loader.add_value("url_object_id", get_md5(response.url))
        item_loader.add_css("title", ".entry-header h1::text")
        item_loader.add_css("date", ".entry-meta-hide-on-mobile::text")
        item_loader.add_css("post_type", ".entry-meta-hide-on-mobile a:nth-child(1)::text")
        item_loader.add_css("comments_num", ".entry-meta-hide-on-mobile a:nth-child(2)::text")
        item_loader.add_css("tag", ".entry-meta-hide-on-mobile a:nth-child(3)::text")
        item_loader.add_css("original_url", ".copyright-area a::attr(href)")
        item_loader.add_value("img_url", response.meta.get("post_img", ""))
        item_loader.add_css("content", "div.entry")

        item = item_loader.load_item()

        yield item
