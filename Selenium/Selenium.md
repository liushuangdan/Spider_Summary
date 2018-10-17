
Selenium
====

---
Selenium是一个Web的自动化测试工具，最初是为网站自动化测试而开发的，类型像我们玩游戏用的按键精灵，可以按指定的命令自动操作，不同是Selenium 可以直接运行在浏览器上，它支持所有主流的浏览器（包括PhantomJS这些无界面的浏览器）。

Selenium 可以根据我们的指令，让浏览器自动加载页面，获取需要的数据，甚至页面截屏，或者判断网站上某些动作是否发生。


可以从 PyPI 网站下载 Selenium库https://pypi.python.org/simple/selenium ，也可以用 第三方管理器 pip用命令安装：`pip install selenium`

Selenium 官方参考文档：http://selenium-python.readthedocs.io/index.html

chromedriver 驱动下载

https://npm.taobao.org/mirrors/chromedriver/

----

 当页面中有需要javascript 去动态加载的内容的时候，
 我们又不好模拟这个javascript，这个时候

----
例如：百度上搜索什么是建设性问题
===
```python
from selenium import webdriver

#这个驱动要添加到环境变量中，如果没有添加到环境变量中，那么我们可以使用它的路径。
driver = webdriver.Chrome()

driver.get('http://www.baidu.com')

driver.find_element_by_id('kw').send_keys('建设性问题是什么')
driver.find_element_by_id('su').click()

```
---
栗子：京东上搜索奶瓶消毒器
===
```python
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.jd.com')

driver.find_element_by_id('key').send_keys('奶瓶消毒器')
driver.find_element_by_class_name('button').click()
```

----

Selenium 自己不带浏览器，不支持浏览器的功能，它需要与第三方浏览器结合在一起才能使用。但是我们有时候需要让它内嵌在代码中运行，所以我们可以用一个叫 PhantomJS 的工具代替真实的浏览器。

---

PhantomJS
===


PhantomJS 是一个基于Webkit的“无界面”(headless)浏览器，它会把网站加载到内存并执行页面上的 JavaScript，因为不会展示图形界面，所以运行起来比完整的浏览器要高效。

如果我们把 Selenium 和 PhantomJS 结合在一起，就可以运行一个非常强大的网络爬虫了，这个爬虫可以处理 JavaScrip、Cookie、headers，以及任何我们真实用户需要做的事情。

注意：PhantomJS 只能从它的官方网站http://phantomjs.org/download.html) 下载。 因为 PhantomJS 是一个功能完善(虽然无界面)的浏览器而非一个 Python 库，所以它不需要像 Python 的其他库一样安装，但我们可以通过Selenium调用PhantomJS来直接使用。

PhantomJS 官方参考文档：http://phantomjs.org/documentation

---

### selenium + phantomJS
### selenium + Chrome headless 模式

但是现在都不用`selenium + phantomJS`,一般使用`selenium + Chrome headless 模式`


### 栗子：爬取豆瓣，需要登录验证进入后爬取信息。
```python

#无界面模式 selenium 的另一个模式
from selenium import webdriver
from lxml import etree
import requests
import base64


option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument('--disable-gpu')

driver = webdriver.Chrome(chrome_options=option)
driver.get('https://accounts.douban.com/login?alias=&redir=https%3A%2F%2Fwww.douban.com%2F&source=index_nav&error=1016')
driver.find_element_by_id('email').send_keys('18510556963')
driver.find_element_by_id('password').send_keys('yaoqinglin2011')

#page_source 是这个页面的html 代码
html_str = driver.page_source
html_ele = etree.HTML(html_str)
image_url = html_ele.xpath('//img[@id="captcha_image"]/@src')[0]
response = requests.get(image_url)

# @获取到图片的base64的编码
v_pic = base64.b64encode(response.content)
#需要获取我们验证码的类型
v_type = 'cn'

#生成form 表单
form_data = {
    'v_pic':v_pic,
    'v_type':v_type
}

#需要在headers 中增加授权
headers = {
    'Authorization': 'APPCODE ' + 'eab23fa1d03f40d48b43c826c57bd284'
}
dama_url = 'http://yzmplus.market.alicloudapi.com/fzyzm'
response = requests.post(dama_url,data=form_data,headers=headers)
print(response.text)
res_dict = response.json()
valid_image = res_dict['v_code']
driver.find_element_by_id('captcha_field').send_keys(valid_image)
driver.find_element_by_class_name('btn-submit').click()

cookie_list = []
for cookie in driver.get_cookies():
    cookie_item = cookie['name'] + '=' + cookie['value']
    cookie_list.append(cookie_item)
cookies = '; '.join(cookie_list)
print(cookies)

url = 'https://www.douban.com/mine/wallet/#/all-spending?page=1'
headers = {
    'Cookie': cookies,
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}
response = requests.get(url,headers=headers)
print(response.status_code)
with open('douban_money1.html','wb') as f:
    f.write(response.content)

```
---

### 对比：下面是有界面模式

```python

#有界面模式 selenium 的另一个模式
from selenium import webdriver
from lxml import etree
import requests
import base64

# selenium + phantomJS
# selenium + Chrome headless 模式 无界面模式

# option = webdriver.ChromeOptions()
# option.add_argument('--headless')
# option.add_argument('--disable-gpu')

driver = webdriver.Chrome()
driver.get('https://accounts.douban.com/login?alias=&redir=https%3A%2F%2Fwww.douban.com%2F&source=index_nav&error=1016')
driver.find_element_by_id('email').send_keys('18510556963')
driver.find_element_by_id('password').send_keys('yaoqinglin2011')

#page_source 是这个页面的html 代码
html_str = driver.page_source
html_ele = etree.HTML(html_str)
image_url = html_ele.xpath('//img[@id="captcha_image"]/@src')[0]
response = requests.get(image_url)

# @获取到图片的base64的编码
v_pic = base64.b64encode(response.content)
#需要获取我们验证码的类型
v_type = 'cn'

#生成form 表单
form_data = {
    'v_pic':v_pic,
    'v_type':v_type
}

#需要在headers 中增加授权
headers = {
    'Authorization': 'APPCODE ' + 'eab23fa1d03f40d48b43c826c57bd284'
}

dama_url = 'http://yzmplus.market.alicloudapi.com/fzyzm'

response = requests.post(dama_url,data=form_data,headers=headers)
print(response.text)
res_dict = response.json()
valid_image = res_dict['v_code']
driver.find_element_by_id('captcha_field').send_keys(valid_image)
driver.find_element_by_class_name('btn-submit').click()

cookie_list = []
for cookie in driver.get_cookies():
    cookie_item = cookie['name'] + '=' + cookie['value']
    cookie_list.append(cookie_item)

cookies = '; '.join(cookie_list)

url = 'https://www.douban.com/mine/wallet/#/all-spending?page=1'
headers = {
    'Cookie':cookies,
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}
response = requests.get(url,headers=headers)

with open('douban_money2.html','wb') as f:
    f.write(response.content)

```
---

Selenium 的用处
===


当页面中有需要javascript去动态加载的内容的时候， 我们又不好模拟这个javascript， 那么我们可以通过selenium进行获取页面。

1. 如果页面需要动态加载数据， 这些数据又包含在javascript中， 我们不容易获取到，就可以应用selenium进行获取html， 这事的html是已经经过浏览器渲染后的页面了。

2. 很多时候，在登录时需要有加密，所以我们可以通过selenium登录，获取cookie，设置cookie后就可以任意的访问页面了。

---
