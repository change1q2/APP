"""
============================
Author:柠檬班-木森
Time:2019/11/29
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import requests

header = {
    "X-Lemonban-Media-Type": "lemonban.v1",
    "Content-Type": "application/json"
}
data = {
    "member_id": 45504,
    "reg_name": "小柠檬888"
}

res = requests.patch(url="http://api.lemonban.com/futureloan/member/update", json=data, headers=header)
print(res.json())
