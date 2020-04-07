"""
============================
Author:柠檬班-木森
Time:2019/11/20
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
再去封装两个读取数据的方法，一个写入数据的方法





"""

#读取excle中的数据，并将它们转化成需要使用的使用，列表嵌套字典形式

import openpyxl

# 打开工作簿
workbook = openpyxl.load_workbook("cases.xlsx")

# 选中表单
sheet = workbook["register"]

# 按行获取所有格子对象,转换为列表，每一行的格子作为一个元祖放在这个列表中
rows = list(sheet.rows)

# 获取第一的表头
title = []
for r in rows[0]:
    title.append(r.value)
# 创建一个空列表 用来存放所有的用例数据
cases = []
# 遍历除了表头剩余的行
for row in rows[1:]:
    # print(row)
    # 创建一个空列表，用来存储该行的数据
    data = []
    # 再次遍历该行的每一个格子
    for r in row:
        # print(r.value)
        # 将格子中的数据，添加到data中
        data.append(r.value)
    # print(data)
    case = dict(zip(title, data))
    # print(case)
    cases.append(case)
print(cases)

