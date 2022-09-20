import scrapy
from    films_scraper.items import FilmsScraperItem

from films_scraper.logger import logger
from bs4 import BeautifulSoup
import os

class FilmSpider(scrapy.Spider):

    name = 'film'
    allowed_domains = ['rezka.ag']

    def start_requests(self):

        try:
            with open(os.path.join(os.getcwd(), 'inputs.txt')) as file:
                file_contents = file.read()
        except FileNotFoundError as error:
            logger.error('File inputs.txt should be provided')
        
        contents_split = file_contents.splitlines()

        for url in contents_split:
            yield scrapy.Request(url)

    custom_settings = {
        'xpaths' : {'parse_film_name': '//div[@class="b-post__title"]/h1/text()',
                    'parse_film_name_english': '//div[@class="b-post__origtitle"]/text()',
                    'parse_film_rating': '//span[@class="b-post__info_rates imdb"]/span/text()',
                    'parse_film_length': '//td[@itemprop="duration"]/text()',
                    'parse_description': '//div[@class="b-post__description_text"]/text()',}
    }

    def parse(self, response):

        film_name = response.xpath(self.custom_settings['xpaths']['parse_film_name']).extract()[0]
        film_name_eng = response.xpath(self.custom_settings['xpaths']['parse_film_name_english']).extract()[0]
        film_rating= response.xpath(self.custom_settings['xpaths']['parse_film_rating']).extract()[0]
        film_length = response.xpath(self.custom_settings['xpaths']['parse_film_length']).extract()[0]
        film_description = response.xpath(self.custom_settings['xpaths']['parse_description']).extract()[0]

        film_country = self.parse_country(response=response)

        yield FilmsScraperItem({'film_name': film_name, 'film_name_eng': film_name_eng, 'film_rating':film_rating,
               'film_country':film_country, 'film_length':film_length, 'film_description':film_description})


    def parse_country(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')

        table = soup.find('table', {"class": "b-post__info"})
        table_datas = table.find_all('td')

        for table_data in table_datas:  

            if table_data.get_text() == 'Страна:':
                film_country = table_data.findNext('td').get_text()

        return film_country