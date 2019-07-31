import scrapy

from ..items import WebScraperItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        "http://quotes.toscrape.com/"
    ]

    def parse(self,response):
        for quotes in response.css('div.quote'):
            item = WebScraperItem()
            item['title'] = quotes.css('span.text::text').extract()
            item['author'] = quotes.css('.author::text').extract()
            # item['tag'] = quotes.css('.tag::text').extract()
            item.save()
            yield item