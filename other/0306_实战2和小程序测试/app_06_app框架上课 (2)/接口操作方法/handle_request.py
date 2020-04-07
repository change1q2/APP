"""
============================
Author:柠檬班-木森
Time:2019/12/2
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
封装的目的：
1.提高代码的复用性



封装的需求：
    发送post请求，，发送get请求，发送patch请求，
    代码中如何做到不同请求方式的接口去发送不同的请求
    加判断
    
    





"""

import requests


class HandleRequest:
    def send(self, url, method, params=None, data=None, json=None, headers=None):
        # 将请求的方法转换为小写
        method = method.lower()
        if method == "post":
            return requests.post(url=url, json=json, data=data, headers=headers)
        elif method == "patch":
            return requests.patch(url=url, json=json, data=data, headers=headers)
        elif method == "get":
            return requests.get(url=url, params=params)


class HandleSessionRequest:
    """使用session鉴权的接口，使用这个类类发送请求"""

    def __init__(self):
        self.se = requests.session()

    def send(self, url, method, params=None, data=None, json=None, headers=None):
        # 将请求的方法转换为小写
        method = method.lower()
        if method == "post":
            return self.se.post(url=url, json=json, data=data, headers=headers)
        elif method == "patch":
            return self.se.patch(url=url, json=json, data=data, headers=headers)
        elif method == "get":
            return self.se.get(url=url, params=params)


if __name__ == '__main__':
    # 登录接口地址
    login_url = "http://api.lemonban.com/futureloan/member/login"

    # 登录的参数
    login_data = {
        "mobile_phone": "15867554893",
        "pwd": "123456qwe",
    }
    # 登录的请求头
    header = {
        "X-Lemonban-Media-Type": "lemonban.v2",
        "Content-Type": "application/json"
    }

    http = HandleRequest()
    res = http.send(url=login_url, method="post", json=login_data, headers=header)
    print(res.json())
