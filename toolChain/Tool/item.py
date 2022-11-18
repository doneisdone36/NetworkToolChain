import scrapy

class GetNaverMovieItem(scrapy.Item):
    title = scrapy.Field()
    score = scrapy.Field()
    reservation = scrapy.Field()

