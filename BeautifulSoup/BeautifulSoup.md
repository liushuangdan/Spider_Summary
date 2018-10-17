
BeautifulSoup
===

我们到网站上爬取数据，需要知道什么样的数据是我们想要爬取的，什么样的数据是网页上不会变化的。

Beautiful Soup提供一些简单的、python式的函数用来处理导航、搜索、修改分析树等功能。它是一个工具箱，通过解析文档为用户提供需要抓取的数据，因为简单，所以不需要多少代码就可以写出一个完整的应用程序。<br>

Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码。你不需要考虑编码方式，除非文档没有指定一个编码方式，这时，Beautiful Soup就不能自动识别编码方式了。然后，你仅仅需要说明一下原始编码方式就可以了。

三种类型：bs4.BeautifulSoup， bs4.element.Tag, NavigableString

## 安装

```bash
pip install bs4
```

## bs4.BeautifulSoup（美味汤）

bs4.BeautifulSoup, 继承自 Tag。
也就是说，Tag中的函数，变量，大多都能在 bs4.BeautifulSoup 中使用。

```

html_str = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc)
type(soup)
```

## element.Tag(标签)

### name, attributes（名字和属性）
将 Tag 中的方法同样放在 BeautifulSoup 的类中，试下什么情况。

```
# 通过标签名字获取标签
p = soup.p
# 标签的类型是什么
type(p)
# 标签的名字是什么
p.name
# 这个标签的属性
p.attrs
# 通过属性的名字获取属性信息
p['class']
# 通过属性的名字设置属性信息
p['id'] = 1
```

### multi-valued attributes（多值属性）

```
css_soup = BeautifulSoup('<p class="body"></p>')
css_soup.p['class']

css_soup = BeautifulSoup('<p class="body strikeout"></p>')
css_soup.p['class']

id_soup = BeautifulSoup('<p id="my id"></p>')
id_soup.p['id']
```

## NavigableString （一种类似string的类型）

```
p.string
type(p.string)
p.string.parent

str(p.string)
type(str(p.string))
```

## Going down(查找文档中的标签)

### using tag name（通过标签名字获取）

```
soup.head
soup.title
soup.body.b
```

### using .contents and .children

contents 返回的是 list
children 返回的是 list_iterator

```
soup.body.contents
soup.body.children

for child in soup.body:
    print(child)
```

## Filters （过滤器）

a string, a regular expression, a list, a function, or the value True.  

```
soup.find_all('b')
import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
for tag in soup.find_all(re.compile("t")):
    print(tag.name)

```


Definitions:  
```
find_all(name, attrs, recursive, string, limit, **kwargs)
```

### name

tag name:   
```
soup.find_all("title")
```

### keyword arguments

kwargs

```
soup.find_all(id='link2')
soup.find_all(href=re.compile("elsie"), id='link1')
soup.find_all(id=True)
soup.find_all(href=re.compile("elsie"))

data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
data_soup.find_all(data-foo="value")
data_soup.find_all(attrs={"data-foo": "value"})

```

special

```
soup.find_all("a", class_="sister")
soup.find_all("a", attrs={"class": "sister"})
```

### string

```
soup.find_all(string="Elsie")
soup.find_all(string=["Tillie", "Elsie", "Lacie"])
soup.find_all(string=re.compile("Dormouse"))
def is_the_only_string_within_a_tag(s):
    return (s == s.parent.string)

soup.find_all(string=is_the_only_string_within_a_tag)
soup.find_all("a", string="Elsie")
```

### limit

```
soup.find_all("a", limit=2)
```

### recursive

```
soup.html.find_all("title")
soup.html.find_all("title", recursive=False)
```

### Calling a tag like a function

```
soup.find_all("a")
soup("a")

soup.title.find_all(string=True)
soup.title(string=True)
```

### find

```
soup.find_all('title', limit=1)
# [<title>The Dormouse's story</title>]

soup.find('title')
# <title>The Dormouse's story</title>
```

### css selector

Tags find 

```
soup.select("title")
soup.select("p:nth-of-type(3)")
```

class

```
soup.select(".sister")
```

attribute

```
soup.select('a[href]')
soup.select('a[href="http://example.com/elsie"]')

soup.select('a[href^="http://example.com/"]')

soup.select('a[href$="tillie"]')

soup.select('a[href*=".com/el"]')
```

## 注意事项

格式编码问题

```
BeautifulSoup(page, from_encoding='gb2312')
```

如果在某个ul下，有多个li，一半是有样式，一半是没有的，而刚好他们是两个类别，你也恰好需要这两个，例如：
```
html = '''
    <ul>
        <li>hello world!</li>
        <li class="hh">hello world!</li>
    </ul>
'''
```

```
from bs4 import BeautifulSoup

soup = BeautifulSoup(html,'lxml')

no_tag = soup.find('li',{'class':False})
```














