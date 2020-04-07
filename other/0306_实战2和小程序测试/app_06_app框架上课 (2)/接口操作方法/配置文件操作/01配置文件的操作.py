"""
============================
作者:seak
时间:
邮件:274882401@qq.com
作用：
题目：使用配置文件
============================
"""
#导包
from configparser import ConfigParser

#步骤：
#1.创建一个操作配置文件的对象(文件解析对象)
conf = ConfigParser()

#2 读取配置文件中的内容
conf.read("conf.ini", encoding="utf8")

# get方法：读取出来的内容，都是字符串
# res1 = conf.get("logging", "level")
# print(res1, type(res1))
# res2 = conf.get("seak",'name')
# print(res2,type(res2))

# getint:读取整数类型的数据，读取出来是int类型
# res3 = conf.getint("musen","age")
# print(res3,type(res3))

# getfloat:读取浮点数
# res4 = conf.getfloat("musen", "money")
# print(res4)

# getboolean:读取布尔值
# res5 = conf.getboolean("musen", "switch")
# print(res5, type(res5))


# 配置数据的写入
conf.set("seak", "hai", "python24")
conf.write(open("conf.ini", "w",encoding="utf-8"))#要用w写入，a的话会重叠