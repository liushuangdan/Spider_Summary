# -*- coding: utf-8 -*-
import scrapy
import json
import re,time
from w3lib.html import remove_tags
from projects.items import LiepinItem

class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'
    allowed_domains = ['zhilian.com','zhaopin.com']
    # start_urls = ['http://zhilian.com/']
    #给spider一个起始的url
    def start_requests(self):
        base_url = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=4&lastUrlQuery=%7B%22p%22:2,%22pageSize%22:%2260%22,%22jl%22:%22530%22,%22kw%22:%22Python%22,%22kt%22:%224%22%7D'
        #给这个url 数据，做一个拼接，页码数的变化
        for i in range(1,500):
            print('--------------------------------第',i,"页------------------------------------------------")
            url = base_url.format(i*60)
            req = scrapy.Request(url=url, callback=self.parse)
            #加一个请求头
            req.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
            yield  req

    def parse(self, response):
        # 将获取到的内容做一个编码，得到json格式
        res_dict = json.loads(response.body.decode('utf-8'))
        #遍历获取到的内容的results
        for i in res_dict['data']['results']:
            #在这个里面获取我们想要得到工作详情页的url
            href = i['positionURL']
            #请求这个url 获取详情页
            req = scrapy.Request(url=href, callback=self.parse_detailed)
            yield req

    def parse_detailed(self,response):
        # with open('zhilian.html','wb') as f:
        #     f.write(response.body)
        #来捕捉异常的
        try:
            #将html 编码 utf-8 来获取信息
            html = response.body.decode('utf-8')
            #正则匹配 获取标题
            title_re = re.compile(r'<h1>(.*?)</h1>',re.S)
            title = re.search(title_re,html).group(1)
            #正则匹配获取工资
            salary = re.search('<strong>(.*?)<a href="http://www.zhaopin.com/\w.*/".*?>',html).group(1)
            salary = salary.split('&')[0]
            #因为这里的 经验 学历要求，工作地点，招聘人数，
            # 以及发布时间没有专门的类或者id，所以需要获取所有的一起获得，然后来切分
            #取出所有的 ul 内的内容，然后来切分取值
            ul_re = re.compile('<ul class="terminal-ul clearfix">(.*?)</ul>',re.S)
            ul = re.search(ul_re,html).group(1)
            info_li = remove_tags(ul)
            info = info_li.split('\n')
            # print(info)
            experince = ""
            number = ""
            education = ""
            time_show = ""
            position=""
            for i in info:
                if i == "":
                    info.remove(i)
                if "工作地点" in i:
                    i = i.split('：')
                    # print(i)
                    position += i[-1]
                    # print(position)
                if "工作经验" in i:
                    i = i.split('：')
                    # print(i)
                    experince += i[-1]
                    # print(experience)
                if "最低学历" in i :
                    i=i.split('：')
                    education += i[-1]
                    # print(education)
                if "招聘人数" in i :
                    i = i.split('：')
                    number += i[-1]
                if "发布日期" in i :
                    i = i.split('：')
                    time_show += i[-1]
            #获取工作职位的描述
            description = re.search(r'<div class="tab-inner-cont">(.*?)<b>',html,re.S).group(1)
            description = remove_tags(description)
            description = ''.join(description)
            # print(description)
            #获取公司名称
            com_name_re = re.compile('target="_blank">(.*?)<img class="icon_vip"')
            com_name =re.search(com_name_re,html).group(1)
            #爬虫的添加时间
            add_time = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
            #来自于哪个网站
            from_web = "智联招聘 zhaopin.com"
            data = (title, salary, position, experince, education, number, time_show, description, com_name, add_time, from_web)
            # print(data)
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
            yield item
        except:
            pass




