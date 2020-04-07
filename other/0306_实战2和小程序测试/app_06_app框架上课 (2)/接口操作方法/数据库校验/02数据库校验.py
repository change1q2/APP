'''
作者：seak
时间：
项目：
题目：
作用：
备注：
'''
import decimal

from common.handle_db import HandleDB
from common.myconfig import conf


#调用数据库控制类
db = HandleDB()
#输入查询语句
sql = 'SELECT leave_amount FROM futureloan.member WHERE mobile_phone="{}"'
#调用配置文件中user的手机号码
phone = conf.get_str("test_data",'user')

#获取这个电话号码所拥有的金额，格式化sql语句
s_amount = db.get_one(sql.format(phone))[0]
print(s_amount,type(s_amount))

#decimal的类型不能与float相加，所以要进行转化,将其他数据转化为decimal问题，转化之前线转化成字符串否者会有精度问题
amount =100.1
amount = decimal.Decimal(str(amount))
all_amount = s_amount + amount
print(all_amount)