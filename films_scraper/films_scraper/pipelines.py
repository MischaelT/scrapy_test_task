import os
from csv import writer

from itemadapter import ItemAdapter

from films_scraper.settings import PATH_TO_DATA


class FilmsScraperPipeline:

    def open_spider(self, spider):

        if not os.path.exists(PATH_TO_DATA):
            self.file = open(PATH_TO_DATA, 'w')
            writer(self.file).writerow(['film_name', 'film_name_eng', 'film_rating', 'film_country', 'film_length', 'film_description', ])
        else:
            self.file = open(PATH_TO_DATA, 'a')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        writer(self.file).writerow(ItemAdapter(item).asdict().values())
        return item
