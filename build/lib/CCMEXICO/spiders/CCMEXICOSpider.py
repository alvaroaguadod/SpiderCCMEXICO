import scrapy
from scrapy.loader import ItemLoader
from scrapy import Item
from scrapy.spiders import CrawlSpider, Rule
from CCMEXICO.items import CCMEXICOItem
from CCMEXICO.parameters import SpiderParameters
from CCMEXICO.processing import ProcessingSearches


class CCMEXICOSpiderSpider(scrapy.Spider):
    name = "CCMEXICOSpider"
    download_delay = 1
    urls_list = []

    def start_requests(self):
        parameters = SpiderParameters(self)
        urls_list = ProcessingSearches(parameters).get_urls
        searchlist = parameters.searchlist
        category = parameters.category
        blog = parameters.blog

        if searchlist or category:
            for link in urls_list:
                print("Scraping page: " + link)
                yield scrapy.Request(url=link, callback=self.parse)
        elif blog:
            for link in urls_list:
                print("Scraping page: " + link)
                yield scrapy.Request(url=link, callback=self.parse_blog)

    def parse(self, response):
        # Create a new list for all the articles in the pages
        articles_list = response.xpath(
            '//div[contains(@id, "post")]//h4[contains(@class, "title")]/a/@href'
        ).getall()
        print(articles_list)
        for article in articles_list:
            print("ARTICLE: " + article)
            yield scrapy.Request(url=article, callback=self.parse_item)

    def parse_blog(self, response):
        # Create a new list for all the articles in the pages
        articles_list = response.xpath(
            '//div[contains(@class, "media-body")]//h3[contains(@class, "title")]/a/@href'
        ).getall()
        print(articles_list)
        for article in articles_list:
            print("ARTICLE: " + article)
            yield scrapy.Request(url=article, callback=self.parse_post)

    def parse_item(self, response):
        item = ItemLoader(CCMEXICOItem(), response)
        item.add_xpath(
            "title",
            '//div[contains(@id, "email-data")]/p[contains(@class, "campaignSubject")]/text()',
        )
        item.add_xpath(
            "author",
            '//div[contains(@id, "email-data")]/p[contains(@class, "campaignFrom")]/text()',
        )
        item.add_xpath(
            "context",
            ' //div[contains(@style, "text-align: right")]/span/text()',
        )
        item.add_xpath(
            "text",
            '//div[contains(@style, "text-align: justify")]/span//text()',
        )
        yield item.load_item()

    def parse_post(self, response):
        item = ItemLoader(CCMEXICOItem(), response)
        item.add_xpath(
            "title",
            '//div[contains(@class, "post-title")]/h1[contains(@class, "post-title")]//text()',
        )
        item.add_xpath(
            "text",
            '//article[contains(@class, "post-details")]/p/text()',
        )
        yield item.load_item()
