# -*- coding: utf-8 -*-
from urllib import parse

import scrapy

from btbtdy.items import BtbtdyMovieItem


class BtbtdyMovieSpider(scrapy.Spider):
    name = 'btbtdy_movie'
    allowed_domains = ['btbtdy.me']
    start_urls = ['http://www.btbtdy.me/btfl/dy1.html']

    def parse(self, response):
        items = BtbtdyMovieItem()
        movie_list = response.xpath("//div[@class='cts_ms']")
        for movie in movie_list:
            items['name'] = movie.xpath("./p[@class='title']/a/@title").extract_first()
            items['url'] = parse.urljoin(response.url, movie.xpath("./p[@class='title']/a/@href").extract_first())
            items['score'] = movie.xpath("./p[@class='title']/span/text()").extract_first()
            items['des'] = movie.xpath("string(./p[@class='des'])").extract_first()
            yield items
