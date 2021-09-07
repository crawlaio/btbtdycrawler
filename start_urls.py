# -*- coding: utf-8 -*-
import json

from redis import StrictRedis

from btbtdy.settings import REDIS_DB, REDIS_HOST, REDIS_PASSWORD, REDIS_PORT


class StartUrls:
    def __init__(self):
        self.redis = StrictRedis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            password=REDIS_PASSWORD,
            db=REDIS_DB,
            decode_responses=True,
        )

    def main(self, spider_name: str):
        item_list = [json.dumps({"url": f"http://ldytt.com/List/1-pg-{one}.html"}) for one in range(2, 10)]
        self.redis.rpush(f"{spider_name}:start_urls", *item_list)
        return len(item_list)


if __name__ == "__main__":
    StartUrls().main("btbtdy")
