#--------------------- NOT WORKING YET -------------------------#
# import scrapy
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule


# class BestMoviesSpider(CrawlSpider):
#     name = 'best_movies'
#     allowed_domains = ['imdb.com']
#     # start_urls = ['http://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc']
    
#     user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    
#     def start_requests(self):
#         yield scrapy.Request(url = 'https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc',
#                                   headers = {'User-Agent' : self.user_agent})  

#     rules = (
#             Rule(LinkExtractor(restrict_xpaths="//h3[@class='lister-item-header']/a"),callback = "parse_item", follow=True,process_request='set_user_agent'),
#             Rule(LinkExtractor(restrict_xpaths="(//a[@class='lister-page-next next-page'])[2]") ,process_request ='set_user_agent')
#     )
    
#     def set_user_agent(self,request):
#         request.headers['User-Agent'] = self.user_agent
#         return request

#     def parse_item(self, response):
#         # pass
#         # print(response.url)
#         yield {
#             'title': response.xpath("//div[@class='title_wrapper']/h1/text()").get(),
#             'year': response.xpath("//div[@class='title_wrapper']/h1/span/a/text()").get(),
#             'duration': response.xpath("normalize-space(//div[@class='title_wrapper']/div/time/text())").get(),
#             'genre': response.xpath("//div[@class='title_wrapper']/div/a/text()").get(),
#             'rating': response.xpath("//div[@class='ratingValue']/strong/span/text()").get(),
#             'movie_url': response.url,
#             'user-agent' : response.request.headers['User-Agent'],
#         }
        

#------------------------ WORKING CODE ------------------------#
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']
    start_urls = ['http://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc']
    
    # user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    
    # def start_requests(self):
    #     yield scrapy.Request(url = 'https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc',
    #                               headers = {'User-Agent' : self.user_agent})

    rules = (
            Rule(LinkExtractor(restrict_xpaths="//h3[@class='lister-item-header']/a"),callback = "parse_item", follow=True),#process_request='set_user_agent'),
            Rule(LinkExtractor(restrict_xpaths="(//a[@class='lister-page-next next-page'])[2]") #,process_request ='set_user_agent')
    ))
    
    # def set_user_agent(self,request):
    #     request.headers['User-Agent'] = self.user_agent
    #     return request
    def parse_item(self, response):
        # pass
        # print(response.url)
        yield {
            'title': response.xpath("//div[@class='title_wrapper']/h1/text()").get(),
            'year': response.xpath("//div[@class='title_wrapper']/h1/span/a/text()").get(),
            'duration': response.xpath("normalize-space(//div[@class='title_wrapper']/div/time/text())").get(),
            'genre': response.xpath("//div[@class='title_wrapper']/div/a/text()").get(),
            'rating': response.xpath("//div[@class='ratingValue']/strong/span/text()").get(),
            'movie_url': response.url,
            # 'user-agent' : response.request.headers['User-Agent'],
        }
        
        
# ---------------------- SOLVED BY TEACHER---------------------------#
# -*- coding: utf-8 -*-
# import scrapy
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule


# class BestMoviesSpider(CrawlSpider):
#     name = 'best_movies'
#     allowed_domains = ['imdb.com']

#     user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'

#     def start_requests(self):
#         yield scrapy.Request(url='https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc', headers={
#             'User-Agent': self.user_agent
#         })

#     rules = (
#         Rule(LinkExtractor(restrict_xpaths="//h3[@class='lister-item-header']/a"), callback='parse_item', follow=True, process_request='set_user_agent'),
#         Rule(LinkExtractor(restrict_xpaths="(//a[@class='lister-page-next next-page'])[2]"), process_request='set_user_agent')
#     )

#     def set_user_agent(self, request):
#         request.headers['User-Agent'] = self.user_agent
#         return request

#     def parse_item(self, response):
#         yield {
#             'title': response.xpath("//div[@class='title_wrapper']/h1/text()").get(),
#             'year': response.xpath("//span[@id='titleYear']/a/text()").get(),
#             'duration': response.xpath("normalize-space((//time)[1]/text())").get(),
#             'genre': response.xpath("//div[@class='subtext']/a[1]/text()").get(),
#             'rating': response.xpath("//span[@itemprop='ratingValue']/text()").get(),
#             'movie_url': response.url
#         }
