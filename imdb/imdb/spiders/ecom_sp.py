# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class EcomSpSpider(scrapy.Spider):
    name = 'ecom_sp'
    allowed_domains = ['alcampo.es']
    start_urls = ['http://www.alcampo.es/compra-online/']

    rules = (
        Rule(
            LinkExtractor(restrict_xpaths=r'//a[@data-idcomponent="comp_8IBT"]'),callback='parse_item',follow=True),     
        )
    def start_requests(self):
        yield scrapy.Request(url='http://www.alcampo.es/compra-online/')

    def parse_item(self, response):
        yield {
            'Title': response.xpath('//h1').get(),
            'Price':response.xpath('(//span[@class="big-price price right precio precio38"])[1]').get()
        }
        
