
XPATH的爬虫练习
===

```python
#导包
import requests
from lxml import etree

#下载页面
url = 'http://python.jobbole.com/all-posts/'

#下载页面
response = requests.get(url)
html_str = response.text

#获取页面内的内容，
html_ele = etree.HTML(html_str)

#[]的意思是里面可以写下标
# xpath_str = '/html/body/div[1]/div[3]/div[1]/div[2]/p/a[1]/text()'

#//a 可以看做是findall re.findall
#[] 中括号的意思是选择，内部的@class就是属性，最后属性的值等于'archive-title'

#下面小path的异地就是找到左右的a标签，过滤class = archive-title的情况
#xpath_str ='//a[@class='archive-title']/text()'

#xpath 的使用
#xpath 返回的是列表
# xpath 每次访问可以返回多个标签
# a_ele = html_ele.xpath(xpath_str)

# span_ele = html_ele.xpath('//span[@class="excerpt"]/p/text()')
# print(span_ele)
# print(a_ele[0])
#
# print(a_ele)

#获取到了需要的信息的先辈级节点，然后遍历这个先辈级节点，找到每个DIV。
div_eles_list = html_ele.xpath('//div[@class="post floated-thumb"]')

for div_ele in div_eles_list:
    #需要加. 。 .的作用是获取的那个玩的位置继续寻找，与文件系统类似
    title = div_ele.xpath('.//a[@class="archive-title"]/text()')[0]
    excerpt = div_ele.xpath('.//span[@class="excerpt"]/p/text()')[0]
    href = div_ele.xpath('.//a[@class="archive-title"]/@href')[0]
    print(title)
    print(excerpt)
    print(href)
    print('---' * 50)

```














