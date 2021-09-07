# -*- coding: utf-8 -*-
import scrapy


class BtbtdyMovieItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    score = scrapy.Field()
    des = scrapy.Field()
