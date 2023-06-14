from pathlib import Path
import uuid
import scrapy
from csv import writer

from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from telekom.misc import CommonSpider


class SupportSpider(CommonSpider):
    name = "support"
    start_urls = [
        'https://www.telekom.de/hilfe',
    ]
    page_url_file = "page_urls.csv"
    allowed_domains = ["telekom.de", "www.telekom.de"]
    rules = [
        Rule(LinkExtractor(allow=("/hilfe/.*")), follow=True, callback="parse")
    ]

    def parse(self, response):
        page = response.url
        id_ = uuid.uuid1()
        filename = f"data/{id_}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
        with open(self.page_url_file, "a") as f:
            writer_object = writer(f)
            writer_object.writerow([id_, page])
            f.close()
