import scrapy


class FilmSpider(scrapy.Spider):
    name = 'film'
    allowed_domains = ['rezka.ag']
    start_urls = ['http://rezka.ag/']

    def parse(self, response):
        pass
