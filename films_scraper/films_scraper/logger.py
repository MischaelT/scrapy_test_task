import logging

from films_scraper.settings import PATH_TO_LOGS

logging.basicConfig(format=u'%(asctime)s - %(levelname)s - %(module)s %(funcName)s - %(message)s',
                    level=logging.DEBUG,
                    filename=PATH_TO_LOGS,
                    filemode='w')
logger = logging.getLogger()
