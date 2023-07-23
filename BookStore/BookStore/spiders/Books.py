#------------ NOT WORKING ------
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BooksSpider(CrawlSpider):
    name = 'Books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/index.html']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//ul[@class='nav nav-list']/li/ul/li/a"), \
            callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//article[@class='product_pod']/h3/a")),
        Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a")),
        
    )
    # def parse(self,response):
        
    #     Books = response.xpath("//article[@class='product_pod']/h3/a")
    #     Num_of_Books = ['']
    #     for Book in Books:
    #         Book = int(response.xpath(".//form[@class='form-horizontal']/strong/text()").get())
    #         Num_of_Books.append(Book)
    #     print(Num_of_Books + 'THe NUmber of BOOKS .............')

    def parse_item(self, response):
        # Num_of_Books = ['']
        # for Book in response.xpath("//article[@class='product_pod']/h3/a"):
        #     Book = int(response.xpath("//form[@class='form-horizontal']/strong/text()").get())
        #     Num_of_Books.append(Book)
        # print(Num_of_Books + 'THe NUmber of BOOKS .............')
        
        yield {
            
             
            
        
            'BookName': response.xpath("//h1/text()").get(),
            'BookPrice': response.xpath("//p[@class='price_color']/text()").get()
                
            }
            
# ------------- TYPE A ------- WORKING ---------
        
# import scrapy
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule


# class BooksSpider(CrawlSpider):
#     name = 'Books'
#     allowed_domains = ['books.toscrape.com']
#     start_urls = ['http://books.toscrape.com/index.html']

#     rules = (
#         Rule(LinkExtractor(restrict_xpaths="//div[@class='image_container']/a"), callback='parse_item', follow=True),
#         Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a")),
#     )

#     def parse_item(self, response):
#         yield {
#             'BookName': response.xpath("//h1/text()").get(),
#             'BookPrice': response.xpath("//p[@class='price_color']/text()").get()
                
#             }
            
       