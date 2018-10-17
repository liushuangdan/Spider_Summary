
BeautifulSoup4的各种例子
===

### 链家网的网页信息爬取 

https://bj.lianjia.com/ershoufang/c1111027378138/?sug=%E6%B5%81%E6%98%9F%E8%8A%B1%E5%9B%AD%E4%B8%89%E5%8C%BA

```python
from bs4 import BeautifulSoup
import requests

url = 'https://bj.lianjia.com/ershoufang/c1111027378138/?sug=%E6%B5%81%E6%98%9F%E8%8A%B1%E5%9B%AD%E4%B8%89%E5%8C%BA'

response = requests.get(url)

# with open('lianjia.html', 'wb') as f:
#     f.write(response.content)

soup = BeautifulSoup(response.text, 'lxml')

li_tag_list = soup.select('li[class="clear LOGCLICKDATA"]')

for li_tag in li_tag_list:
    #css 子选择器，喧杂额父元素下的一个div并且这个div里面有一个类是title，下面的同理。
    title_name = li_tag.select('div[class="info clear"] > div.title')[0].text
    address = li_tag.select('div[class="info clear"] > div.address')[0].text
    flood = li_tag.select('div[class="info clear"] > div.flood')[0].text
    followInfo = li_tag.select('div[class="info clear"] > div.followInfo')[0].text

    print(title_name)
    print(address)
    print(flood)
    print(followInfo)
```

### 雪球网 

https://xueqiu.com/ask/square

```python
from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
}

url = 'https://xueqiu.com/ask/square'
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')
div_ask_items = soup.find_all('div', class_="ask-item")

for div_ask_item in div_ask_items:
    ask_text = div_ask_item.p.text
    answer_text = div_ask_item.select('div.ask-item-comment > div.aks-item-comment-bd > p')[0].text
    print('问问问问: ' + ask_text)
    print('答答答答: ' + answer_text)
    print('-------------' * 5)
    


# with open('xueqiu.html', 'wb') as f:
#     f.write(response.content)
```

### 豆瓣的活动页面 

https://beijing.douban.com/events/week-party

```python
from bs4 import BeautifulSoup
import requests

url = 'https://beijing.douban.com/events/week-party'
response = requests.get(url)


# with open('douban_party.html', 'wb') as f:
#     f.write(response.content)

soup = BeautifulSoup(response.text, 'lxml')

# li_tag_list = soup.find_all('li', class_="list-entry")
li_tag_list = soup.select('ul.events-list.events-list-pic100.events-list-psmall > li.list-entry')

for li_tag in li_tag_list:
    #summary = li_tag.find('span', itemprop="summary").text
    summary = li_tag.select('span[itemprop="summary"]')[0].text
    #event_time = li_tag.find('li', class_="event-time").text.strip()
    event_time = li_tag.select('li.event-time')[0].text
    fee = li_tag.find('li', class_="fee").text
    host_info = li_tag.select('ul.event-meta > li:nth-of-type(4)')[0].text

    print(summary)
    print(event_time)
    print(fee)
    print(host_info)
    print('-----------------------------------------------------')
```

### 链家

```python

from bs4 import BeautifulSoup
import requests

url = 'https://bj.lianjia.com/zufang/c1111027378138/?sug=%E6%B5%81%E6%98%9F%E8%8A%B1%E5%9B%AD%E4%B8%89%E5%8C%BA'

response = requests.get(url)

#所有的获取具体内容信息的类都是一个用法，输入是html_str,输出是一个类 ，用个这个类获取信息

soup = BeautifulSoup(response.text,'lxml')

#find-all 的用法就是 第一个输入是标签，第二个输入是属性过滤器

a_tag = soup.find_all('a',target='_blank')
print(a_tag)

ul_tag = soup.find_all('ul', id="house-lst")[0]
a_tag = ul_tag.find_all('a',target="_blank")
print(len(ul_tag))
print(a_tag)

a_tag = soup.select('ul#house-lst a[target="_blank"]')
print(a_tag)

```





