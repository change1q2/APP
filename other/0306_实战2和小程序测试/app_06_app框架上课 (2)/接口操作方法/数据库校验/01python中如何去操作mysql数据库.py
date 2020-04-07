"""
============================
Author:柠檬班-木森
Time:2019/12/6
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
python操作mysql需要使用pymysql这个模块，

主机：120.78.128.25
port：3306
用户：future
密码：123456


"""

import pymysql

# 第一步：连接到mysql数据库
con = pymysql.connect(host="120.78.128.25",
                      user="future",
                      password="123456",
                      port=3306,
                      charset="utf8"
                      )

# 第二步：创建一个游标对象
cur = con.cursor()

# 第三步：执行sql语句
# 1、准备sql语句
# sql = "SELECT * FROM futureloan.member WHERE mobile_phone ='15512345678'"
# sql = "SELECT id,mobile_phone FROM futureloan.member LIMIT 20"
# 2、执行sql语句
# res = cur.execute(sql)

# print(res)
# 第四步：提取sql语句查找的内容
# fetchall:返回的是一个查询集(元祖的形式，查询到到的每一条数据为这个元祖中的一个元素)
# datas = cur.fetchall()
# print(datas)
# for i in datas:
#     print(i)

# fatchone：获取查询到的数据中的第一条
# data = cur.fetchone()
# print(data)


# 增删改
# sql = ""
# # 执行sql
# cur.execute(sql)
#
# # 执行完增删改的sql语句之后，需要进行commit提交
# con.commit()

