"""
============================
Author:柠檬班-木森
Time:2019/11/29
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import requests

# 第一步：发送get请求

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}
#
# data = {
#     "wd":"柠檬班"
# }

# get请求传递参数使用params来进行传递

data = {
    "mobilephone": "13456785678",
    "pwd":"123qwe"
}
#response = requests.get(url="http://test.lemonban.com/futureloan/mvc/api/member/register", params=data)

response = requests.get(url="https://www.baidu.com",params=data,headers=headers)
print(response)

# 第二步：获取响应数据
# 1、text属性(自动识别文本中的编格式进行解码，有时候不准确，会出现乱码)
# print(response.text)

# 2、content(获取返回的内容，需要自己使用decode指定解码方式)
#print(response.content.decode("utf8"))

# 3、json():获取返回内容中的json数据（只能在返回数据时json的情况下使用）
# print(response.json())
