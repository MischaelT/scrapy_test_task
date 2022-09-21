import os
import random

from scrapy import signals
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import (DNSLookupError, TCPTimedOutError,
                                    TimeoutError)

from films_scraper.settings import DEFAULT_USER_AGENT, PATH_TO_USER_AGENTS


class FilmsScraperSpiderMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        return None

    def process_spider_output(self, response, result, spider):
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        if type(exception) == IndexError:
            spider.logger.error(f'Field on page was not found on responce: {response}')

    def process_start_requests(self, start_requests, spider):
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class FilmsScraperDownloaderMiddleware:

    def __init__(self) -> None:

        if os.path.exists(PATH_TO_USER_AGENTS):
            with open(PATH_TO_USER_AGENTS) as f:
                self.user_agents_list = f.read().split('\n')
        else:
            self.user_agents_list = [DEFAULT_USER_AGENT]

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        user_agent = random.choice(self.user_agents_list)
        request.headers['User-Agent'] = user_agent
        return None

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        if type(exception) == HttpError:
            spider.logger.error("HttpError occurred")
        elif type(exception) == DNSLookupError:
            spider.logger.error("DNSLookupError occurred")
        elif type(exception) in [TimeoutError, TCPTimedOutError]:
            spider.logger.error("TimeoutError occurred")

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
