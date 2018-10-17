# -*- coding: utf-8 -*-
import scrapy,json
from w3lib.html import remove_tags
from projects.items import WeiboItem
import time

class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['weibo.com']
    # start_urls = ['https://m.weibo.cn/u/1195230310?uid=1195230310&luicode=10000011&lfid=100103type%3D1%26q%3D%E4%BD%95%E7%82%85']

    def start_requests(self):
        #央视新闻
        base_url = 'https://m.weibo.cn/api/container/getIndex?uid=2656274875&luicode=10000011&lfid=100103type%3D1%26q%3D%E5%A4%AE%E8%A7%86%E6%96%B0%E9%97%BB&type=uid&value=1664971205&containerid=1076032656274875&page={}'

        for i in range(4360, 10146):
            url = base_url.format(i)
            print("第",i,"页")
            req = scrapy.Request(url=url, callback=self.parse)
            req.headers['User-Agent']='Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Mobile Safari/537.36'
            yield req


    def parse(self, response):
        res_dict = json.loads(response.body.decode('utf-8'))
        cards_list = res_dict['data']['cards']
        for card in cards_list:
            if 'mblog' not in card:
                continue
            try:
                username = card['mblog']['user']['screen_name']
                created_at = card['mblog']['created_at']
                text = remove_tags(card['mblog']['text'])
                attitudes_count = card['mblog']['attitudes_count']
                comments_count = card['mblog']['comments_count']
                reposts_count = card['mblog']['reposts_count']
                add_time =  time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
                item = WeiboItem()
                item['username'] = username
                item['created_at'] = created_at
                item['text'] = text
                item['attitudes_count'] = attitudes_count
                item['reposts_count'] = reposts_count
                item['comments_count'] = comments_count
                item['add_time']=add_time
                # print(created_at)
                # print(text)
                # print(username)
                # print(attitudes_count)
                # print(comments_count)
                # print(reposts_count)
                # print(add_time)
                yield  item
            except:
                pass