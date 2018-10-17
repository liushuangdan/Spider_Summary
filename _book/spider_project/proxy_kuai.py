

import requests

class MyProxy(object):
    # 1. 存储一个proxy， 需要的是重复使用， 这个变量就放到这个类中，
    # 每次获取proxy的时候，只需要获取已经存在的proxy就可以了，不需要每次都重新获取proxy
    # 如果出错的情况，我们需要重新获取一遍proxy，后面使用
    def __init__(self):
        self.form_proxy = {}
        self.need_change_proxy = True

    def change_proxy(self):
        self.need_change_proxy = True
    # 需要有一个函数， 获取当前可用的代理
    def get_one_proxy(self):
        # 如果need_change_proxy == True, 就说明需要新的proxy做替换
        if self.need_change_proxy:
            self.form_proxy = self.new_proxy()#需要处理
            self.need_change_proxy = False

        return self.form_proxy

    def new_proxy(self):
        url = 'http://dps.kdlapi.com/api/getdps/?orderid=923732543439561&num=1&pt=1&ut=1&dedup=1&sep=1'
        response = requests.get(url)
        myformproxy = {
            'http': 'http://'+ response.text,
            'https': 'http://' + response.text,
        }

        return myformproxy












