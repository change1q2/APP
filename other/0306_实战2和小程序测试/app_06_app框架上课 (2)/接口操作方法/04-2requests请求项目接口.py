"""
============================
Author:柠檬班-木森
Time:2019/11/29
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import requests

register_url = "http://api.lemonban.com/futureloan/member/register"

data = {
    "mobile_phone": "15867859876",
    "pwd": "123456qwe",
    "reg_name": "木森",
    "type": 0
}

header = {
    "X-Lemonban-Media-Type": "lemonban.v1",
    "Content-Type": "application/json"
}

# 发送post请求
# json类型的参数，一定要使用json去传递
response = requests.post(url=register_url, json=data, headers=header)

# 表单类型的参数Content-Type: application/x-www-form-urlencoded; charset=UTF-8
# 使用data进行传递
# response = requests.post(url=register_url, data=data, headers=header)

# post请求上传文件: 使用files来上传文件
# res = requests.post(url=register_url,files=None)


# print(type(response.text))

# print(type(response.content.decode("utf8")))

# json方法可以将json字符串转换成对应的python类型的数据
# print(type(response.json()))
print(response.json())
# 需要做自动化的（http/https协议）接口返回的数据99%是json类型的


