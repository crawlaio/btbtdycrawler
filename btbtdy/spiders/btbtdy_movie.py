# -*- coding: utf-8 -*-
from urllib import parse

from scrapy import Request
from scrapy_redis_sentinel.spiders import RedisSpider

from btbtdy.items import BtbtdyMovieItem


class BtbtdySpider(RedisSpider):
    name = "btbtdy"
    redis_key = f"{name}:start_urls"

    def make_request_from_data(self, data):
        data = eval(data)
        return Request(
            url=data.get("url"),
            dont_filter=False,
        )

    def parse(self, response, **kwargs):
        items = BtbtdyMovieItem()
        movie_list = response.xpath("//div[@class='cts_ms']")
        for movie in movie_list:
            items["name"] = movie.xpath("./p[@class='title']/a/@title").get()
            items["url"] = parse.urljoin(
                response.url, movie.xpath("./p[@class='title']/a/@href").get()
            )
            items["score"] = movie.xpath(
                "./p[@class='title']/span/text()"
            ).get()
            items["des"] = movie.xpath("string(./p[@class='des'])").get()
            yield items
