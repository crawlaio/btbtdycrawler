# -*- coding: utf-8 -*-
# ------------------------------项目配置----------------------------------------
BOT_NAME = 'btbtdy'

SPIDER_MODULES = ['btbtdy.spiders']
NEWSPIDER_MODULE = 'btbtdy.spiders'

MONGODB_URI = "mongodb://localhost:27017"
MONGODB_DATABASE = "movie"

# # -----------------------------Redis 单机模式----------------------------------------
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = None
# REDIS 单机模式配置参数
REDIS_PARAMS = {
    "db": REDIS_DB,
    "password": REDIS_PASSWORD,
}

# DUPEFILTER_CLASS = "scrapy_redis_sentinel.dupefilter.RedisDupeFilter"
DUPEFILTER_CLASS = "scrapy_redis_sentinel.dupefilter.RedisBloomFilter"
SCHEDULER = "scrapy_redis_sentinel.scheduler.Scheduler"
STATS_CLASS = "scrapy_redis_sentinel.stats.RedisStatsCollector"

ROBOTSTXT_OBEY = False

RETRY_ENABLED = True

DOWNLOAD_TIMEOUT = 30

LOG_LEVEL = "DEBUG"

COOKIES_ENABLED = False

ITEM_PIPELINES = {
    "btbtdy.pipelines.MongoDBPipeline": None,
}
