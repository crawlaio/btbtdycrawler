# -*- coding: utf-8 -*-
from pymongo import MongoClient


class MongoDBPipeline(object):
    def __init__(self, mongodb_uri, mongodb_db):
        self.mongodb_uri = mongodb_uri
        self.mongodb_db = mongodb_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongodb_uri=crawler.settings.get(
                "MONGODB_URI",
                "mongodb://172.25.2.31:27017,172.25.2.32:27017,172.25.2.33:27017"
            ),
            mongodb_db=crawler.settings.get("MONGODB_DATABASE", "items")
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongodb_uri)
        self.db = self.client[self.mongodb_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        """
        :param item: 传入的item数据
        :param spider: spider相关信息
        :return item:
        """
        self.db[spider.name].update_one(
            filter={"page_url": item["page_url"]},
            update={"$setOnInsert": dict(item)},
            upsert=True
        )
        return item
