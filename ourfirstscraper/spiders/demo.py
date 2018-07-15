

import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):

        yield {'title':response.css('div.blog-title > a > h1').extract()}

