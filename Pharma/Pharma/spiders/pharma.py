# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class PharmaSpider(CrawlSpider):
    name = 'pharma'
    allowed_domains = ['192.140.149.168']
    start_urls = ['https://peshawar.infoisinfo.com.pk/search/pharmaceutical']
    Link_Xpath =  r'//a[@class="view-company"]'
    rules = (
        Rule(LinkExtractor(restrict_xpaths=Link_Xpath), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        Address = response.xpath('//div[@class="address_com address.address mid-wrapper"]/span/text()')
        Full_Address = []
        for addr in Address:
            Full_Address.append(addr)

        item = {
        'Company Name' : '//h1[@class="title_com name"]/text()',
        'Phone Number' : '(//div[@id="phone-wrapper"]/span/text())[2]',
        'Address'      : Full_Address,
        }
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        yield item
