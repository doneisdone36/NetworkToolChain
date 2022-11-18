import scrapy


class SecuritySpider(scrapy.Spider):
    name = 'security'
    allowed_domains = ['https://www.naver.com']
    start_urls = ['http://www.naver.com']

    def parse(self, response):
        print(response.text)
       
