'''
作者：seak
时间：
项目：
题目：
作用：
备注：
用正则表达式进行替换
'''
import re

from common.myconfig import conf

# data = '{"mobile_phone":"#phone#","pwd":"#pwd#"}'
# #data = '{"member_id": #member_id#,"amount":600}'
# #----未使用正则之前的参数替换方法-------
# if "#phone#" in data:
#     data = data.replace("#phone#",conf.get_str("test_data","user"))
#
# if "#pwd#" in data:
#     data = data.replace("#pwd#",conf.get_str("test_data","pwd"))
# print(data)

# ------------使用正则进行替换----方式不通用----------
# data = '{"mobile_phone":"#phone#","pwd":"#pwd#"}'
# #  # #两个#号之间可以表示要替换的数据，.+表示1个字符以上,?关闭贪婪模式
# r = "#.+?#"
# res2 = re.findall(r,data)
# print(res2)
#
# #使用search方法，只找第一个
# res3 = re.search(r,data)
# print(res3)
# data = data.replace(res3.group(),conf.get_str("test_data","user"))
# print(data)

#使用通用的方法
data = '{"mobile_phone":"#phone#","pwd":"#pwd#"}'
r = "#(.+?)#"
res = re.search(r,data)
#判断结果是否为None
if res:
    item = res.group()#获取全部数据
    key = res.group(1)#获取（）组中的数据
    print(item)
    print(key)
    #进行替换，item替换成配置文件conf中test_data,通用key(因为key在前面()组中获取的是phone所以key会替换成phone号码)
    data = data.replace(item,conf.get_str("test_data",key))

print(data)