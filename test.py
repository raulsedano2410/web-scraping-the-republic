import scrapy
from scrapy import signals


class BlogSpider(scrapy.Spider):
    name = "blogspider"
    start_urls = ["https://www.zyte.com/blog/"]

    def __init__(self, *args, **kwargs):
      super(BlogSpider, self).__init__(*args, **kwargs)
      self.results = []

    def parse(self, response):
        for title in response.css(".z-text-blog-title"):
            yield {"title": title.css("::text").get()}

    def closed(self, reason):
        # Se emite la señal 'spider_closed' cuando el spider ha terminado
        self.crawler.signals.send_catch_log(
            signal=signals.spider_closed, spider=self, reason=reason
        )
    def parse_item(self, response):
        self.results.append({"title": response.css(".z-text-blog-title::text").get()})

    def get_results(self):
        return self.results

# rules:
# pip install scrapy

# command to create csv:
#  scrapy runspider test.py -o scraped_data.csv
