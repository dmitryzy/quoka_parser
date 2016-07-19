# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader.processors import TakeFirst
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Compose
from scrapy.contrib.loader.processor import MapCompose
# from scrapy.loader import ItemLoader
from scrapy.selector import HtmlXPathSelector
from quoka.items import QuokaItem


class QuokaLoader(XPathItemLoader):
    default_input_processor = MapCompose(lambda s: re.sub('\s+', ' ', s.strip()))
    default_output_processor = TakeFirst()

class QuokaSpider(CrawlSpider):

    name = "quoka"
    allowed_domains = ["quoka.de"]
    start_urls = ["http://www.quoka.de/immobilien/bueros-gewerbeflaechen/"]

    rules = (
            #правила обработки url
             Rule(LinkExtractor(allow=('kleinanzeigen/cat_27_2710_ct_0_page_')), follow=True),
             Rule(LinkExtractor(allow=('immobilien/bueros-gewerbeflaechen/')), callback='parse_item'),
             )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        l = QuokaLoader(QuokaItem(), hxs)
        #собираем данные
        l.add_xpath('OBID',response.xpath("html/body/div[3]/div[2]/div[1]/main/div[8]/div/div[3]/div[2]/div[2]/strong[1]/text()").extract())
        l.add_xpath('Stadt',response.xpath("html/body/div[3]/div[2]/div[1]/main/div[8]/div/div[3]/div[2]/div[1]/strong/span/a/span/text()").extract())
        l.add_xpath('PLZ',response.xpath("html/body/div[3]/div[2]/div[1]/main/div[8]/div/div[3]/div[2]/div[1]/strong/span/span/span[2]/text()").extract())
        l.add_xpath('Uberschrift',response.xpath("html/body/div[3]/div[2]/div[1]/main/div[8]/div/div[1]/h1/text()").extract())
        l.add_xpath('Beschreibung',response.xpath("html/body/div[3]/div[2]/div[1]/main/div[8]/div/div[3]/div[3]/div/text()[12]").extract())
        l.add_xpath('Kaufpreis',response.xpath("html/body/div[3]/div[2]/div[1]/main/div[8]/div/div[2]/strong/span").extract())
        l.add_xpath('Erstellungsdatum',response.xpath("html/body/div[3]/div[2]/div[1]/main/div[8]/div/div[3]/div[2]/div[2]/text()[7]").extract())
        return l.load_item()
