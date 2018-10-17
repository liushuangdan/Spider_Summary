
Requests库
===

### Get 方法

首先安装我们的**requests 库**

`pip install requests`  

```python
导入库：
import requests

r = requests.get('http://httpbin.org/get?key2=value2&key1=value1')
#请求的状态码
r.status_code
#请求头
r.headers
#请求的url
r.url
#请求的编码格式
r.encoding
#请求的文本内容
r.text

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get',params=payload)

""" 这里可行么，为什么，出错之后可以根据代码发现问题 """

r = requests.get('http://httpbin.org/get', payload)
```
上面我们传入的参数 payload 是一个字典传参。

---

\*\*kwargs 是一个字典，dict。

## 那么 dict 背后的实现方式是什么?

Dict的对象在使用到了所谓的关联关系的时候，就是通过key-value的形式，能够通过key值快速定位到某个value值；

### Dict的存储实现原理

python中的dict对象也即PyDictObject对象，因为对搜索的效率要求很高，所以选择了哈希表（hash table），因为在最优情况下，哈希表能够提供O(1)的搜索效率

因此：这里就能想到在leetcode上面刷的题目中，很多通过list形式可以实现的，为了降低时间复杂度，可以用hash的方式，选择dict对象存储（当然具体问题要具体分析）

哈希表的基本思想是：通过一定的函数将需要搜索的键值映射为一个整数，根据这个整数作为索引去访问某片连续的内存区域。用于映射的函数称为哈希函数，映射所产生的值称为哈希值（hash value）。哈希函数对搜索效率有直接的决定性作用。在使用哈希函数将不同的值可能映射到相同的哈希值，这个时候就需要冲突解决（装载率大于2/3时，冲突的概率就会大大增加）

冲突解决在python中使用的是开放定址法，就是通过一个二次探测函数f，计算下一个位置，一直到找到下一个可用的位置为止，在这个过程中会到达多个位置，这些位置就形成了一个“冲突探测链”，这个冲突探测链在查找某个元素的时候起到重要作用，所以在删除某个位置上的元素，不能直接将这个位置的内容删除，如果删除的话，则导致后续依赖于这个位置的其他值就都无法寻找到了，所以只能进行“伪删除”（通过给元素设置状态，dummy态，表示没有存储具体的值但是还会用到的废弃态）

---

那么以上就是python字典中的实现原理，具体的PyDictObject对象中，会存在每一个元素，元素的定义什么等等之类的解释，我会在python总结中的数据类型中的dict字典的总结中详细讲解。

---

### Post 方法

~~~python
r = requests.post('http://httpbin.org/post', data = {'key':'value'})
~~~

### 更复杂的 Post
~~~python

payload = {'key1': 'value1', 'key2': 'value2'}

payload = {'key1': ('value1', 'value2')}

数据在 form 里面 

r = requests.post('http://httpbin.org/post', data=payload)

数据在data 里面

import json

r = requests.post('http://httpbin.org/post', data=json.dumps(payload))
~~~

---

### 文件上传

~~~python
当我们用一个请求地址，请求到数据以后，需要把请求回来的数据保存下来

url = 'http://httpbin.org/post'
这种方法就是用字典的形式，来把参数传到下面的请求方法中去，请求完以后，直接保存下来。
files = {'file': open('report.xls', 'rb')}

r = requests.post(url, files=files)
r.text

files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}
r = requests.post(url, files=files)
r.text
~~~

---

### Cookies 

设置cookie，当我们遇到反爬机制的时候，需要添加cookies值来继续我们的数据爬取。

```python
url = 'http://httpbin.org/cookies'

cookies = dict(cookies_are='working')

r = requests.get(url, cookies=cookies)
r.text
```

---

### Redirect

重定向 在网络中，有些网站在直到你是网络爬虫以后，不会让你爬取到它网站的数据，那么你如何判断呢？这个时候就需要接收一下状态码来判断是不是给了重定向。

~~~python
r = requests.get('http://github.com')
r.url
根据状态码来确定是不是重定向，那么我们重定向的状态码是：
3xx：重定向--要完成请求必须进行更进一步的操作

r.status_code
r.history

r = requests.get('http://github.com', allow_redirects=False)
r.status_code
r.history
~~~

---

### Timeout

请求超时的设置，来设置爬取这个网站，在0.001内没有请求到，那么就做超时处理。

~~~python
requests.get('http://github.com', timeout=0.001)
~~~

---

### Requests 的乱码问题

~~~python
import requests
 
response = requests.get('http://www.dytt8.net/index.htm')
print(response.text)

response.encoding

 比较慢
response.apparent_encoding

requests.utils.get_encodings_from_headers(response.text)
requests.utils.get_encodings_from_content(response.text)
response.encoding = 'gb2312'

~~~

---

## Requests 的项目实践

1. 百度首页爬取下载
2. 西刺代理网页爬取
3. 百度翻译_post
4. 人人网登录
5. 暴力破解登录的方法
6. 有道翻译
7. 百思不得姐
8. 雪球网
8. 微博的方法
9. 微信的方法
10. 知乎的方法

----

后面会附上 我 爬虫的项目内容。
---













