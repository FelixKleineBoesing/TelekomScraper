import scrapy
from scrapy.crawler import CrawlerProcess
from telekom.spiders.pdftelekom import PDFSpider

process = CrawlerProcess(
    settings={}
)

process.crawl(PDFSpider)
process.start()
