# -*- coding: utf-8 -*-
from urllib import parse

from scrapy import Request
from scrapy_redis_sentinel.spiders import RedisSpider

from btbtdy.items import BtbtdyMovieItem


class BtbtdyMovieSpider(RedisSpider):
    name = "btbtdy_movie"
    redis_key = "start_urls:{0}".format(name)

    def make_request_from_data(self, data):
        values = eval(data).get("values")
        return Request(
            url=eval(data).get("baseUrl"),
            dont_filter=True,
            meta={"data": values}
        )

    def parse(self, response):
        items = BtbtdyMovieItem()
        movie_list = response.xpath("//div[@class='cts_ms']")
        for movie in movie_list:
            items["name"] = movie.xpath("./p[@class='title']/a/@title").extract_first()
            items["url"] = parse.urljoin(
                response.url, movie.xpath("./p[@class='title']/a/@href").extract_first()
            )
            items["score"] = movie.xpath(
                "./p[@class='title']/span/text()"
            ).extract_first()
            items["des"] = movie.xpath("string(./p[@class='des'])").extract_first()
            yield items
