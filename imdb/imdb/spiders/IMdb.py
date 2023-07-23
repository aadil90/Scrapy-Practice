import scrapy 
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re

class ImdbSpider(CrawlSpider):
    name = 'IMdb'
    allowed_domains = ['facebook.com']
    # start_urls = ['https://www.imdb.com/name/nm2789448/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p']/@href"),\
             callback = 'parse_item', follow = True), 
        # Rule(LinkExtractor(restrict_xpaths = "//div[@class='azpagelinks']/span[13]"))
        # #( //ul[@class='pagination']/li)[12]
        ) 
    def start_requests(self):
        yield scrapy.Request(url = 'https://www.facebook.com/groups/1377040672306168/members'
        # headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}, 
        )

    def parse_item(self, response):
            # Email = response.xpath("//span[@class= 'subhead']/span[contains(text(),'E-Mail:')]/a/text()").get()   #.replace('E-Mail','')
            # Web = response.xpath("//span[@class= 'subhead']/span[contains(text(),'Web')]/a/text()").get()     #.replace('Web','')
            # # print('Email',Email)
            # # print('Web',Web)
            # if Email is None:
            #     Email = Email
            # else: 
            #     Email = Email.replace('E-Mail:','')
            # if Web is None:
            #     Web = Web
            # else:
            #     Web = Web.replace('Web:','')
            yield {
                'Name': response.xpath("//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql gk29lw5a a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb h6olsfn3 m6dqt4wy h7mekvxk hnhda86s oo9gr5id hzawbc8m']/text()").get(),
                'Telephone' : response.xpath("//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql gk29lw5a jq4qci2q a3bd9o3v knj5qynh oo9gr5id']/text()").get(),
                # 'Email' : Email,#i.xpath(".//span[contains(text(),'E-Mail:')]/text()").get().replace('E-Mail',''),
                # 'Web': Web#i.xpath(".//span[contains(text(),'Web')]/text()").get().replace('Web','')
            }



#//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql gk29lw5a jq4qci2q a3bd9o3v knj5qynh oo9gr5id']/text()
#//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p']/@href