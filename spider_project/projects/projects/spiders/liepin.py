# -*- coding: utf-8 -*-
import scrapy,time,re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from projects.items import LiepinItem

class LiepinCrawlSpider(CrawlSpider):
    name = 'liepin'
    allowed_domains = ['liepin.com']
    start_urls = ['https://www.liepin.com/zhaopin/']

    #匹配规则 找到这里的所有的 工作职位的详情页
    rules = (
        Rule(LinkExtractor(allow=r'https://www.liepin.com/job/\d*.*'), callback='parse_item', follow=True),
    )


    def parse_item(self, response):
        # 用xpath 找到详情页里的 title
        title = response.xpath('//div[@class="title-info"]/h1/text()').extract_first()
        #公司的名字的获取
        com_name = response.xpath('//div[@class="title-info"]/h3/a/text()').extract_first()
        #职位工资的获取
        salary = response.xpath('//div[@class="job-title-left"]//p[@class="job-item-title"]//text()').extract_first()
        #对工资的一个去掉空格的操作
        if salary:
            salary =salary.strip()
        #公司位置的获取
        position = response.xpath('//p[@class="basic-infor"]/span/a/text()').extract_first()
        #工作经验的要求
        experince= response.xpath('//div[@class="job-qualifications"]/span[2]/text()').extract_first()
        #学历的要求
        education= response.xpath('//div[@class="job-qualifications"]/span[1]/text()').extract_first()
        #由于没有人数显示在页面中，所以添加一个 人数不限
        number= "人数不限"
        #职位招聘的时间显示
        time_show= response.xpath('//p[@class="basic-infor"]/time/text()').extract_first().strip()
        #关于职位的职责的描述
        description= response.xpath('//div[@class="content content-word"]/text()').extract()
        description = ''.join(description).strip()
        #添加的时间，我操作的时间
        add_time= time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
        #来自哪个网站
        from_web= "liepin.com猎聘直聘"
        data = (title, salary, position, experince, education, number, time_show, description, com_name, add_time, from_web)
        # print(title)
        # print(com_name)
        # print(salary)
        # print(position)
        # print(experince)
        # print(education)
        # print(number)
        # print(time_show)
        # print(description)
        # print(add_time)
        print('__'*30)
        item = LiepinItem()
        item['title'] = title
        item['salary'] = salary
        item['position'] = position
        item['experince'] = experince
        item['education'] = education
        item['number'] = number
        item['time_show'] = time_show
        item['description'] = description
        item['com_name'] = com_name
        item['add_time'] = add_time
        item['from_web'] = from_web
        yield  item


