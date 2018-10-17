
爬取前程无忧的数据
===

```python

import requests
from lxml import etree
from spider_projects.mysqlhelper import MysqlHelper
from urllib import parse
import time
import re

#封装一个函数，用来获取数据，判断数据是否存在
def Decide(element):
    if element:
        element=element[0]
    else:
        element = " "
    return element

helper = MysqlHelper()
base_url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,java,2,{}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
#请求头
headers ={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'guid=5e80d2479dd198d859c503e40a9bb4aa; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; adv=adsnew%3D1%26%7C%26adsresume%3D1%26%7C%26adsfrom%3Dhttps%253A%252F%252Fwww.baidu.com%252Fbaidu.php%253Fsc.0s0000KlmKuCTsdU2Ie5cilLfWfMcG39IbDBuBRmslDhKajt6Pm5oVUB1Ia9033A5pXt9nRrTgkwp7zGOCKF2kdJaUGKRm49shunfiu72wdpjZgt_0KeNOvYBbGRCryT1Od126mgTluhnUIYPYJu1fRZk46fKXbx2GwPI0nh2EoerGRzAf.7Y_NR2Ar5Od66CHnsGtVdXNdlc2D1n2xx81IZ76Y_NtX5W3eS1J1-k_nOEOlecxLO3MHSEwECntx135zOCxgvg45E6OeAHxfOgkOdkxo3O-CLOWEWEzgxwOsr5Oml5dlpoQOvSajSw7OVxwxS9yOO_xVYXveqElqEgVmvfdG_H3en-dvHFIjxvuQVOB-MFb8lRq5uEtN2s1f_IhOF_L2.U1Yk0ZDqkea11neXYtxPS0KspynqnfKY5TXs_t1rLV5Z1x60pyYqnW0Y0ATqmhNsT100Iybqmh7GuZR0TA-b5HD0mv-b5H00UgfqnH0krNtknjDLg1c4rH-xn1msnfKopHYs0ZFY5HmvPsK-pyfqnWmdnWwxnHfzndtzPWbvP7tznHDsn7tkrjRvn7tzPWndn7tznWDdrfKBpHYznjf0UynqnH0snNtLrjm3nH6zPjNxn10vnWnLnHfsP7ts0Z7spyfqn0Kkmv-b5H00ThIYmyTqn0K9mWYsg100ugFM5H00TZ0qn0K8IM0qna3snj0snj0sn0KVIZ0qn0KbuAqs5H00ThCqnfKbugmqTAn0uMfqn0KspjYs0Aq15H00mMTqnH00UMfqn0K1XWY0IZN15HD1n161nj61PWcdn1n3rjcvPWmz0ZF-TgfqnHR1P1f3rHcYrj6dP6K1pyfqmHN-PANbmH6snj04nAN9n6KWTvYqnRRsnWIKfHPKP16knYcdnfK9m1Yk0ZK85H00TydY5H00Tyd15H00XMfqn0KVmdqhThqV5HKxn7tsg100uA78IyF-gLK_my4GuZnqn7tsg1Kxn0Ksmgwxuhk9u1Ys0AwWpyfqn0K-IA-b5iYk0A71TAPW5H00IgKGUhPW5H00Tydh5H00uhPdIjYs0AulpjYs0Au9IjYs0ZGsUZN15H00mywhUA7M5HD0UAuW5H00mLFW5HfdP1m3%2526ck%253D1583.4.110.165.538.610.616.297%2526shh%253Dwww.baidu.com%2526sht%253Dbaidu%2526us%253D1.0.1.0.1.303.0%2526ie%253Dutf-8%2526f%253D8%2526tn%253Dbaidu%2526wd%253D%2525E5%252589%25258D%2525E7%2525A8%25258B%2525E6%252597%2525A0%2525E5%2525BF%2525A7%2525E7%2525BD%252591%2526rqlang%253Dcn%2526inputT%253D4178%2526bc%253D110101%26%7C%26adsnum%3D1337794; partner=www_baidu_com; 51job=cenglish%3D0%26%7C%26; search=jobarea%7E%60010000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%601%A1%FB%A1%FA010000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FAJava+%BF%AA%B7%A2%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1537489571%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch1%7E%601%A1%FB%A1%FA010000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FAjava%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1537455456%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21',
    'Host': 'search.51job.com',
    'Referer': 'https://www.51job.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
}
#269  1-269
#对于页码的获取
for i in range(1,266):
    url = base_url.format(i)
    print("----------------------------第",i,"页------------------------------------")
    response = requests.get(url,headers=headers)
    html_ele = etree.HTML(response.text)
    a_eles_list = html_ele.xpath('//div[@class="dw_table"]/div[position()>3]/p/span/a/@href')
    # 循环访问这些a标签
    for href in a_eles_list:
        response = requests.get(href,headers=headers)
        # 利用xpath获取数据
        html_ele = etree.HTML(response.text)
        try:
            # 用xpath 找到详情页里的 title
            title = html_ele.xpath('//h1/@title')
            title = Decide(title)
            # 职位工资的获取
            salary = html_ele.xpath('//div[@class="cn"]/strong/text()')
            salary = Decide(salary)
            #获取页面里关于工作地点，经验要求，学历要求，招聘人数，招聘时间的列表
            info = html_ele.xpath('//div[@class="cn"]/p[2]/text()')
            #前程无忧是两个模板，所以需要做个处理判断。
            count = len(info)
            #如果获取的信息长度是大于四的 做个获取，否则做另一种方法获取
            if count > 4 :
                #获取工作地点
                position = html_ele.xpath('//div[@class="cn"]/p[2]/text()')
                position = Decide(position).strip()
                #获取经验要求
                experince = html_ele.xpath('//div[@class="cn"]/p[2]/text()')
                if experince:
                    experince = experince[1].strip()
                else:
                    experince=" "
                #获取学历要求
                education = html_ele.xpath('//div[@class="cn"]/p[2]/text()')
                if education:
                    education = education[2].strip()
                else:
                    education=" "
                #获取招聘人数
                number = html_ele.xpath('//div[@class="cn"]/p[2]/text()')
                if number:
                    number = number[3].strip()
                else:
                    number=" "
                #获取招聘时间的显示
                time_show = html_ele.xpath('//div[@class="cn"]/p[2]/text()')
                if time_show:
                    time_show = time_show[4].strip()
                else:
                    time_show=" "
            else:
                #工作地点的获取
                position = html_ele.xpath('//div[@class="cn"]/p[2]/text()')
                position = Decide(position).strip()
                #工作经验的获取
                experince = html_ele.xpath('//div[@class="cn"]/p[2]/text()')
                if experince:
                    experince = experince[1].strip()
                else:
                    experince = " "
                #对于低于长度等于4 的 没有学历的要求，所以要做个单独的处理
                education = " "
                #招聘人数的获取
                number = html_ele.xpath('//div[@class="cn"]/p[2]/text()')
                if number:
                    number = number[2].strip()
                else:
                    number = " "
                #招聘时间的显示
                time_show = html_ele.xpath('//div[@class="cn"]/p[2]/text()')
                if time_show:
                    time_show = time_show[3].strip()
                else:
                    time_show = " "
            # print(title,salary,position,experince,education,num,time_show)
            #获取工作的的岗位职责的标题
            job_title = html_ele.xpath('//div[@class="bmsg job_msg inbox"]/p/strong//text()')
            job_title = Decide(job_title).strip()
            #获取岗位信息
            job_info =html_ele.xpath('//div[@class="bmsg job_msg inbox"]/p//text()')
            #前程无忧关于页面的岗位信息显示，是两个模板，所以这个时候要做个判断，
            # 如果一个模板能获取成功的话就获取信息，如果不成功，就是另个模板，来获取信息
            if job_info:
                job_info = ''.join(job_info)
                job_info = re.findall('\S', job_info)
                job_info = ''.join(job_info)
                description= job_title+job_info
                # print(description)
            else:
                job_title = html_ele.xpath('//h2/span[@class="bname"]/text()')
                job_title = Decide(job_title).strip()
                job_info = html_ele.xpath('//div[@class="bmsg job_msg inbox"]//text()')
                job_info = ''.join(job_info)
                job_info = re.findall('\S',job_info)
                job_info = ''.join(job_info)
                description = job_title + job_info
                # print(description)

                # 公司名称
                com_name = html_ele.xpath('//div[@class ="com_msg"]/a/p/text()')[0]

                # print(com_name)
            #我的添加时间
            add_time = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
            #来自于哪个网站
            from_web = "jobs.51job.com前程无忧"
            data = (title, salary, position,experince,education,number,time_show, description,com_name,add_time,from_web)
            print(data)
            print("****"*30)
            # 存储数据到mysql
            insert_sql = 'INSERT INTO job_zhaopin(title, salary, position,experince,education,number,time_show, description,com_name,add_time,from_web) VALUES (%s, %s, %s, %s,%s,%s, %s, %s, %s,%s, %s)'
            helper.execute_modify_sql(insert_sql, data)
        except:
            pass

```

