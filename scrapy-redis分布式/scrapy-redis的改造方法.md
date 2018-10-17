scrapy-redis 的改造方法
===

---

要将一个`Scrapy`项目变成一个`Scrapy-redis`项目只需修改以下三点就可以了：

1. 将爬虫的类从`scrapy.Spider`变成`scrapy_redis.spiders.RedisSpider`；或者是从`scrapy.CrawlSpider`变成`scrapy_redis.spiders.RedisCrawlSpider`。
2. 将爬虫中的`start_urls`删掉。增加一个`redis_key="xxx"`。这个`redis_key`是为了以后在`redis`中控制爬虫启动的。爬虫的第一个url，就是在redis中通过这个发送出去的。
3. 在配置文件中增加如下配置：

---
    #  Scrapy-Redis相关配置
    # 确保request存储到redis中
    SCHEDULER = "scrapy_redis.scheduler.Scheduler"

    # 确保所有爬虫共享相同的去重指纹
    DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

    # 设置redis为item pipeline
    ITEM_PIPELINES = {
        'scrapy_redis.pipelines.RedisPipeline': 300
    }

    # 在redis中保持scrapy-redis用到的队列，不会清理redis中的队列，从而可以实现暂停和恢复的功能。
    SCHEDULER_PERSIST = True

    # 设置连接redis信息
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    REDIS_PASSWORD = 123456

---

## 运行爬虫：

1. 在爬虫服务器上。进入爬虫文件所在的路径，然后输入命令：`scrapy runspider [爬虫名字]`。
2. 在`Redis`服务器上，推入一个开始的url链接：`redis-cli> lpush [redis_key] start_url`开始爬取。



