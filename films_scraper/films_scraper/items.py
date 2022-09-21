import scrapy


class FilmsScraperItem(scrapy.Item):

    film_name = scrapy.Field()
    film_name_eng = scrapy.Field()
    film_rating = scrapy.Field()
    film_country = scrapy.Field()
    film_length = scrapy.Field()
    film_description = scrapy.Field()
