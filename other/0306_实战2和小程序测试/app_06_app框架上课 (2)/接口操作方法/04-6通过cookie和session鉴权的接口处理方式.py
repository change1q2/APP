"""
============================
Author:柠檬班-木森
Time:2019/12/2
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import requests
"""
使用cookie和session鉴权的接口处理


使用requests模块中的session对象来发请求


"""

#  -----------------使用requests直接发送请求，无法通过session鉴权-------

# # 老版的前程贷登录接口
# login_url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
#
# login_data = {
#     "mobilephone": "13367899876",
#     "pwd": "lemonban"
# }
# res = requests.post(url=login_url, data=login_data)
# print(res.cookies)
#
#
# # 老版的前程贷充值接口
# recharge_url = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
# recharge_data = {
#     "mobilephone": "13367899876",
#     "amount": 200000
# }
# res2 = requests.post(url=recharge_url, data=recharge_data)
# print(res2.json())


#-----------------使用requests模块中的session对象来发请求---------------

# 创建一个session对象:se对象能够自动记录上一次请求中的cookie信息
se = requests.session()

# 老版的前程贷登录接口
login_url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
login_data = {
    "mobilephone": "13367899876",
    "pwd": "lemonban"
}
res = se.post(url=login_url, data=login_data)



# 老版的前程贷充值接口
recharge_url = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
recharge_data = {
    "mobilephone": "13367899876",
    "amount": 200000
}
res2 = se.post(url=recharge_url, data=recharge_data)
print(res2.json())