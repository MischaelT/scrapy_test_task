import scrapy
from bs4 import BeautifulSoup
from films_scraper.settings import PATH_TO_RESOURSES
from films_scraper.items import FilmsScraperItem
from films_scraper.logger import logger

from scrapy.exceptions import CloseSpider


class FilmSpider(scrapy.Spider):

    name = 'film'
    allowed_domains = ['rezka.ag']

    def start_requests(self):

        try:
            with open(PATH_TO_RESOURSES) as file:
                file_contents = file.read()
        except FileNotFoundError:
            logger.error('File pages_to_parse.txt was not provided')
            raise CloseSpider(reason='File pages_to_parse.txt should be provided')

        contents_split = file_contents.splitlines()

        for url in contents_split:
            yield scrapy.Request(url)

    custom_settings = {
        'xpaths': {'parse_film_name': '//div[@class="b-post__title"]/h1/text()',
                   'parse_film_name_english': '//div[@class="b-post__origtitle"]/text()',
                   'parse_film_rating': '//span[@class="b-post__info_rates imdb"]/span/text()',
                   'parse_film_length': '//td[@itemprop="duration"]/text()',
                   'parse_description': '//div[@class="b-post__description_text"]/text()', }
    }

    def parse(self, response):

        film_name = response.xpath(self.get_xpath('parse_film_name')).extract()[0]
        film_name_eng = response.xpath(self.get_xpath('parse_film_name_english')).extract()[0]
        film_rating = response.xpath(self.get_xpath('parse_film_rating')).extract()[0]
        film_length = response.xpath(self.get_xpath('parse_film_length')).extract()[0]
        film_description = response.xpath(self.get_xpath('parse_description')).extract()[0]

        # Since there is no class tied to TD tag in table, using the absolute xpath is useless, because it will not work at some pages,
        # where it located on another place. For example: https://rezka.ag/series/adventures/42638-vokrug-sveta-za-80-dney-2021.html
        # That it why it will be better to parse content directly, looking for a tag with needed content
        film_country = self.parse_country(response=response)

        yield FilmsScraperItem({'film_name': film_name, 'film_name_eng': film_name_eng, 'film_rating': film_rating,
                                'film_country': film_country, 'film_length': film_length, 'film_description': film_description})

    def parse_country(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')

        table = soup.find('table', {"class": "b-post__info"})
        table_datas = table.find_all('td')

        for table_data in table_datas:

            if table_data.get_text() == 'Страна:':
                film_country = table_data.findNext('td').get_text()

        return film_country

    def get_xpath(self, key_to_xpath):
        return self.custom_settings['xpaths'][key_to_xpath]
