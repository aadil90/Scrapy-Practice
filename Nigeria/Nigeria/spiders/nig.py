# -*- coding: utf-8 -*-
import scrapy


class NigSpider(scrapy.Spider):
    name = 'nig'
    allowed_domains = ['https://www.businesslist.com.ng/location/lagos?fbclid=IwAR1k64ADD-Y6m4YYvJbcddVWE935N_0NphTOJ0MCngl0I6iRPvi8Nav6Jzg']
    start_urls = ['https://www.businesslist.com.ng/location/lagos?fbclid=IwAR1k64ADD-Y6m4YYvJbcddVWE935N_0NphTOJ0MCngl0I6iRPvi8Nav6Jzg/']

    def parse(self, response):
        pass
