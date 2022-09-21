import os


BOT_NAME = 'films_scraper'

SPIDER_MODULES = ['films_scraper.spiders']
NEWSPIDER_MODULE = 'films_scraper.spiders'

ROBOTSTXT_OBEY = True

COOKIES_ENABLED = False

ITEM_PIPELINES = {
   'films_scraper.pipelines.FilmsScraperPipeline': 300,
}

ROTATING_PROXY_LIST_PATH = os.path.join(os.getcwd(), 'films_scraper', 'mics', 'proxies.txt')

DOWNLOADER_MIDDLEWARES = {
   'films_scraper.middlewares.FilmsScraperDownloaderMiddleware': 543,
   'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
   'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
}

DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}

SPIDER_MIDDLEWARES = {
   'films_scraper.middlewares.FilmsScraperSpiderMiddleware': 543,
}

DEFAULT_USER_AGENT = 'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4'

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
AUTOTHROTTLE_DEBUG = False

HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

PATH_TO_DATA = os.path.join(os.getcwd(), 'downloaded_data', 'films.csv')
PATH_TO_USER_AGENTS = os.path.join(os.getcwd(),'films_scraper', 'mics' ,'user-agents.txt')
PATH_TO_LOGS = os.path.join(os.getcwd(), 'logs', 'app.log')
PATH_TO_RESOURSES = os.path.join(os.getcwd(), 'pages_to_parse.txt')