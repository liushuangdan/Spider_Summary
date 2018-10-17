
Xpath的代码例子
===

喜马拉雅

```python
from lxml import etree
from urllib import request
import requests
import os
import json


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
}

fetch_audio_base_url = 'https://www.ximalaya.com/revision/play/tracks?trackIds=%s'

def get_one_page_links(page_url):

    response = requests.get(page_url, headers = headers)
    html_ele = etree.HTML(response.text)

    forder_name = html_ele.xpath('//h1[@class="e-630486218 title"]')[0].text
    if os.path.exists(forder_name) is False:
        os.mkdir(forder_name)

    li_ele_list = html_ele.xpath('//li[@class="e-2304105070"]')

    for li_ele in li_ele_list:
        detailed_url = li_ele.xpath('./div[@class="e-2304105070 text"]/a/@href')[0]
        audio_num = detailed_url.split('/')[-1]
        title = li_ele.xpath('./div[@class="e-2304105070 text"]/a/@title')[0]
        file_name = forder_name + '/' + title + '.m4a'
        fetch_audio_url = fetch_audio_base_url % audio_num
        parse_detailed_url(fetch_audio_url, file_name)

    # with open('yishuo.html', 'wb') as f:
    #     f.write(response.content)

def parse_detailed_url(fetch_audio_url, file_name):
    response = requests.get(fetch_audio_url, headers=headers)
    audio_json = json.loads(response.text)

    src = audio_json['data']['tracksForAudioPlay'][0]['src']
    print("start to download " + file_name + " .....")
    request.urlretrieve(src, file_name)


if __name__ == '__main__':
    page_url = 'https://www.ximalaya.com/lishi/4164479/p1/'
    get_one_page_links(page_url)
```


