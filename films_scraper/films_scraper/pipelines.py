# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from csv import writer
import os


class FilmsScraperPipeline:

    def open_spider(self, spider):

        if not os.path.exists(os.path.join(os.getcwd(), 'items.csv')):
            self.file = open('items.csv', 'w')
            writer(self.file).writerow(['film_name', 'film_name_eng', 'film_rating', 'film_country', 'film_length', 'film_description',])
        else:
            self.file = open('items.csv', 'a')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        
        writer(self.file).writerow(ItemAdapter(item).asdict().values())

        return item

