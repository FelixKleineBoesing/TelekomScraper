import scrapy
from scrapy.crawler import CrawlerProcess
from telekom.spiders.support import SupportSpider

process = CrawlerProcess(
    settings={}
)

process.crawl(SupportSpider)
process.start()
