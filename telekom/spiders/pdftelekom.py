from pathlib import Path
import uuid
import scrapy
from csv import writer

from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from telekom.misc import CommonSpider


class PDFSpider(CommonSpider):
    name = "pdftelekom"
    start_urls = [
        'https://www.telekom.de/hilfe',
    ]
    allowed_domains = ["telekom.de", "www.telekom.de"]
    rules = [
        Rule(LinkExtractor(allow=("/hilfe/.*")), follow=True, callback="parse")
    ]

    def parse(self, response):
        page = response.url
        if isinstance(response.body, bytes):
            if page.endswith(".pdf") or b"PDF-" in response.body[:1025]:
                name = page.split("/")[-1]
                filename = f"data/pdfs/{name}.pdf"
                if Path(filename).exists():
                    self.log(f"File {filename} already exists")
                    filename = f"data/pdfs/{name}-1.pdf"
                Path(filename).write_bytes(response.body)
                self.log(f"Saved file {filename}")
