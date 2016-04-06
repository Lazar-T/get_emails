# -*- coding: utf-8 -*-
import re
import csv

import scrapy
from scrapy.loader import ItemLoader
from w3lib.html import replace_escape_chars
from scrapy.loader.processors import MapCompose
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from get_emails.items import GetEmailsItem


class EmailsSpider(CrawlSpider):
    name = 'emails'
    start_urls = []

    with open('emails.csv', 'rb') as f:
        reader = csv.reader(f)
        for line in reader:
            start_urls.append(line[0])

    rules = (Rule(LinkExtractor(), callback='parse_item'),)

    def parse_item(self, response):
        l = ItemLoader(item=GetEmailsItem(), response=response)
        l.default_output_processor = MapCompose(lambda v: v.strip(), replace_escape_chars)

        emails = response.xpath('//text()').re(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}")

        l.add_value('email', emails)
        l.add_value('url', response.url)

        return l.load_item()
