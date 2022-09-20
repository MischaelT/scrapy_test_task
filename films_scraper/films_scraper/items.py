# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FilmsScraperItem(scrapy.Item):

    film_name = scrapy.Field()
    film_name_eng = scrapy.Field()
    film_rating = scrapy.Field()
    film_country = scrapy.Field()
    film_length = scrapy.Field()
    film_description = scrapy.Field()
