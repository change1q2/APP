"""
============================
Author:柠檬班-木森
Time:2019/12/2
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import requests

register_url = "http://api.lemonban.com/futureloan/member/register"

data = {
    "mobile_phone": "15867554893",
    "pwd": "123456qwe",
    "reg_name": "木森",
    "type": 0
}

header = {
    "X-Lemonban-Media-Type": "lemonban.v2",
    "Content-Type": "application/json"
}

# 请求注册接口
# response = requests.post(url=register_url, json=data, headers=header)
# 重返回的结果中提取想要的数据
# json_data= response.json()
# id = json_data["data"]["id"]
# print(id)


# ----------------------登录--------------

login_url = "http://api.lemonban.com/futureloan/member/login"

login_data = {
    "mobile_phone": "15867554893",
    "pwd": "123456qwe",
}

response = requests.post(url=login_url, json=login_data, headers=header)
json_data = response.json()
# print(json_data)


# 提取登录之后的用户id
member_id = json_data["data"]["id"]

# 提取token类型
type_token = json_data["data"]["token_info"]["token_type"]

# 提取token值
token = json_data["data"]["token_info"]["token"]

token_data = type_token + " " + token

# print(type_token)
# print(token)
# token认证的请求头数据
# print(token_data)



# -----------------------充值接口-------------------------

header_token = {
    "X-Lemonban-Media-Type": "lemonban.v2",
    "Content-Type": "application/json",
    "Authorization":token_data
}

recharge_data = {
    "member_id":member_id,
    "amount":2000
}

recharge_url = "http://api.lemonban.com/futureloan/member/recharge"

response = requests.post(url=recharge_url,json=recharge_data,headers=header_token)

print(response.json())

