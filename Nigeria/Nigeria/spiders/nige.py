# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class NigeSpider(CrawlSpider):
    name = 'nige'
    allowed_domains = ['www.youtube.com']
    start_urls = ['https://www.youtube.com/watch?v=5I4bc-njfmE']

    # rules = (
    #     Rule(LinkExtractor(restrict_xpaths=r'//a[@id="video-title"]'), callback='parse_item', follow=True),
    # )

    def parse_item(self, response):
        
        # City = response.xpath('//div[@class="text location"]/text()').get()
        # City = City.split()[-1:-3]
        item = {
            'Date' : response.xpath("(//yt-formatted-string[@class='style-scope ytd-video-primary-info-renderer'])[2]/text()").get(),
            # 'Address': response.xpath('//div[@class="text location"]/text()').get(),
            # 'Phone': response.xpath('//div[@class="text phone"]/text()').get(),
            # 'Email': response.xpath('//a[contains(@href,"mailto:")]/text()').get(),
            # 'About':response.xpath('//div[@class="text desc"]/text()').get(),
            # 'City':'Lagos',
            # 'Map': response.xpath('//a[@id="map_dir_button"]/@href').get(),
            # 'Website': response.xpath('//div[@class="text weblinks"]//a/text()').get(),
            # 'Opening': response.xpath('//div[@class="info oh r_3px"]/text()').get()
        }
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
