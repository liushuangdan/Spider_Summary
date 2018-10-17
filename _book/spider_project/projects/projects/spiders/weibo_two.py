# -*- coding: utf-8 -*-
import scrapy,json
from w3lib.html import remove_tags
from projects.items import Weibo_twoItem
import time


#首先 需求是 获取移动端微博里面的，明星 那个话题的 所有发布微博的 明星，然后获取这些明星的 微博id 来获取该微博用户的所有的微博。


class WeiboTwoSpider(scrapy.Spider):
    name = 'weibo_two'
    allowed_domains = ['m.weibo.cn']
    # start_urls = ['https://m.weibo.cn/api/container/getIndex?containerid=102803_ctg1_4288_-_ctg1_4288&openApp=0&since_id={}']

    def start_requests(self):
        #首先给了一个微博明星专栏 的 url 来获取 用户的id ，要给它添加一个页码。
        base_url = 'https://m.weibo.cn/api/container/getIndex?containerid=102803_ctg1_4288_-_ctg1_4288&openApp=0&since_id={}'
        for i in range(600,700):
            url_list = base_url.format(i)
            req = scrapy.Request(url=url_list, callback=self.parse)
            yield req


    def parse(self, response):
        #将获取到的内容做一个编码，得到json格式
        res_dict = json.loads(response.body.decode('utf-8'))
        #获取json中的每一个cards来获取数据
        cards_list = res_dict['data']['cards']
        #遍历cards_list中的cards
        for cards in cards_list:
            #获取这个里面的用户id
            mblog = cards['mblog']
            user_id = mblog['user']['id']
            #来遍历用户id 所对应的 用户的微博的url
            port_url = 'https://m.weibo.cn/api/container/getIndex?containerid=230413{}_-_WEIBO_SECOND_PROFILE_WEIBO&page_type=03&page='
            url_original = port_url.format(user_id)
            #对每个url做一个页码的拼接
            for i in (100,400):
                url = url_original+str(i)
                req = scrapy.Request(url=url,callback=self.parse_ports)
                yield req

    def parse_ports(self,response):
        # 将获取到的内容做一个编码，得到json格式
        res_dict = json.loads(response.body.decode('utf-8'))
        # 获取json中的每一个cards来获取数据
        list_info = res_dict['data']['cards']
        # 遍历cards_list中的cards
        for cards in list_info:
            #判断如果 scheme存在的话。，那么我们就可以的到我们想要的信息
            if cards['scheme']:
                try:
                    #微博名的获取
                    username = cards['mblog']['user']['screen_name']
                    #微博发布的时间
                    created_at = cards['mblog']['created_at']
                    #微博的内容
                    text = remove_tags(cards['mblog']['text'])
                    #点赞数
                    attitudes_count = cards['mblog']['attitudes_count']
                    #评论数
                    comments_count = cards['mblog']['comments_count']
                    #转发数
                    reposts_count = cards['mblog']['reposts_count']
                    #数据爬取的添加时间
                    add_time = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
                    #实例化 Weibo_twoItem
                    item = Weibo_twoItem()
                    item['username'] = username
                    item['created_at'] = created_at
                    item['text'] = text
                    item['attitudes_count'] = attitudes_count
                    item['reposts_count'] = reposts_count
                    item['comments_count'] = comments_count
                    item['add_time'] = add_time
                    # print(created_at)
                    # print(text)
                    # print(username)
                    # print(attitudes_count)
                    # print(comments_count)
                    # print(reposts_count)
                    # print(add_time)
                    yield item

                except:
                    pass




