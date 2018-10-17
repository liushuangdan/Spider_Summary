

线程和线程池
===

## 线程编程

1. 导入线程和进程的包
2. 新建进程或者线程的类t
3. 函数启动线程/进程 t.start()
4. 主线程或者主进程 t.join()
5. 限制进程和线程的个数， Pool
6. 进程池和线程池的作用就是
    a) 限制进程或者线程的个数 
    b) 重用进程和线程


```python
import threading
from time import ctime,sleep


def music(func):
    for i in range(2):
        print("I was listening to %s. %s" %(func,ctime()))
        sleep(1)

def move(func):
    for i in range(2):
        print("I was at the %s! %s" %(func,ctime()))
        sleep(5)

if __name__ == '__main__':
    threads = []
    # 首先需要生成一个Thread的类， 第一个参数是targe， 执行的函数是什么
    t1 = threading.Thread(target=music, args=('爱情买卖',))
    threads.append(t1)
    t2 = threading.Thread(target=move, args=('阿凡达',))
    threads.append(t2)
    for t in threads:
        # 开始这个线程
        t.start()
    for t in threads:
        # 等待所有的线程结束
        t.join()
    print("all over %s" %ctime())
```
### 执行结果：
```python
I was listening to 爱情买卖. Wed Oct 17 20:53:02 2018
I was at the 阿凡达! Wed Oct 17 20:53:02 2018
I was listening to 爱情买卖. Wed Oct 17 20:53:03 2018
I was at the 阿凡达! Wed Oct 17 20:53:07 2018
all over Wed Oct 17 20:53:12 2018
```
----

## 线程池的代码：

```python 
import time
import threadpool

def sayhello(str):
    print("Hello ",str)
    if str == 'aa':
        time.sleep(8)
    time.sleep(2)

name_list =['xiaozi','aa','bb','cc']
start_time = time.time()
# 初始化线程池， 线程池内部的线程的个数那就是10
pool = threadpool.ThreadPool(8)
# makeRquests的作用是生成很多的requests，
# 它的参数就是1， 需要执行的函数， 执行的所有参数的列表
requests = threadpool.makeRequests(sayhello, name_list)
print(len(requests))
# 将request放入到pool里面. putRequest 的意思是将requests放入到线程池中去执行
[pool.putRequest(req) for req in requests]
pool.wait()
print('%d second'% (time.time()-start_time))
```

### 执行结果：

```python
4
Hello  xiaozi
Hello  aa
Hello  bb
Hello  cc
10 second

```

---

## 进程池的使用例子：爬取喜马拉雅。

```python
import requests
import os
from lxml import etree
import multiprocessing

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}
def download_one_page():
    url_list = []
    url = 'https://www.ximalaya.com/lishi/4164479/'
    base_m4a_url = 'https://www.ximalaya.com/revision/play/tracks?trackIds={}'
    response = requests.get(url, headers=headers)
    html_ele = etree.HTML(response.text)
    href_list = html_ele.xpath('//div[@class="dOi2 text"]/a/@href')
    for href in href_list:
        # 我们只去获取trackID， trackID 就是href的最后的数字
        trackID = href.split('/')[-1]
        m4a_url = base_m4a_url.format(trackID)
        url_list.append(m4a_url)
        #print('download... url=' + m4a_url)
        #download_m4a_from_url(m4a_url)
    return url_list

# with open('ximalaya.html', 'wb') as f:
#     f.write(response.content)

#url = 'https://www.ximalaya.com/revision/play/tracks?trackIds=32176227'

def download_m4a_from_url(m4a_url):
    print('downloading .... url=' + m4a_url)
    response = requests.get(m4a_url, headers=headers)
    # 获取json内的src的内容
    res_dict = response.json()
    src = res_dict['data']['tracksForAudioPlay'][0]['src']
    name = res_dict['data']['tracksForAudioPlay'][0]['trackName']
    dictionary = 'download'
    filename = dictionary + '/' + name + '.m4a'
    response = requests.get(src)


    if not os.path.exists(dictionary):
        os.mkdir(dictionary)

    with open(filename, 'wb') as f:
        f.write(response.content)

if __name__ == '__main__':
    import time
    start_time = time.time()
    # 首先需要生成一个pool， 用于存放进程
    pool = multiprocessing.Pool(processes=4)
    url_list = download_one_page()
    for m4a_url in url_list:
        # 需要将函数放入到pool中进行执行
        pool.apply_async(download_m4a_from_url, (m4a_url, ))

    pool.close()
    pool.join()

    end_time = time.time()
    print('执行的时间是：', end_time-start_time)
    # 163.06532669067383
```





