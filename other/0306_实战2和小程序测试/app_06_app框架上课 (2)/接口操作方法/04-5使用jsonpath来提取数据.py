"""
============================
Author:柠檬班-木森
Time:2019/12/2
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import requests
import jsonpath

# ----------------------登录--------------
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
# 发送登录的请求
response = requests.post(url=login_url, json=login_data, headers=header)
# 获取返回的json数据
json_data = response.json()

# print(json_data)
# res_data = jsonpath.jsonpath(json_data,"$.data.id")

member_id = jsonpath.jsonpath(json_data, "$..id")[0]
type_token = jsonpath.jsonpath(json_data, "$..token_type")[0]
token = jsonpath.jsonpath(json_data, "$..token")[0]


# print(type_token)
# print(token)
# 拼接鉴权所以要到的token信息
token_data = type_token+" "+token


# -----------------------充值接口-------------------------
#
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
#
response = requests.post(url=recharge_url,json=recharge_data,headers=header_token)
#
print(response.json())
