"""
============================
Author:柠檬班-木森
Time:2019/12/2
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""



json_data = {"count": 18, "next": "http://api.keyou.site:8000/projects/?page=2&size=10", "previous": None, "results": [
    {"id": 1, "create_time": "2019-11-06 14:21:19", "name": "自动化测试平台项目", "leader": "可可", "tester": "优优",
     "programmer": "可优", "publish_app": "自动化测试平台应用", "desc": "该平台当前主要用于接口自动化测试.", "interfaces": 4, "testsuits": 2,
     "testcases": 5, "configures": 1},
    {"id": 2, "create_time": "2019-11-06 14:22:54", "name": "前程贷P2P金融项目", "leader": "可优", "tester": "小可可",
     "programmer": "小优优", "publish_app": "前程贷P2P金融应用", "desc": "", "interfaces": 4, "testsuits": 1, "testcases": 1,
     "configures": 1},
    {"id": 3, "create_time": "2019-11-06 14:24:43", "name": "西天取经项目", "leader": "唐僧", "tester": "猪八戒",
     "programmer": "孙悟空", "publish_app": "修成正果应用", "desc": "妖怪哪里跑?", "interfaces": 0, "testsuits": 0, "testcases": 0,
     "configures": 0},
    {"id": 4, "create_time": "2019-11-06 14:27:33", "name": "红楼梦项目", "leader": "曹雪芹", "tester": "贾宝玉",
     "programmer": "王熙凤", "publish_app": "红楼梦研究应用", "desc": "如花美眷，怎敌似水流年。", "interfaces": 0, "testsuits": 0,
     "testcases": 0, "configures": 0},
    {"id": 5, "create_time": "2019-11-06 14:28:54", "name": "水浒传项目", "leader": "施耐庵", "tester": "宋江",
     "programmer": "武松", "publish_app": "水浒传研究应用", "desc": "有缘千里来相会，无缘对面不相逢。", "interfaces": 0, "testsuits": 0,
     "testcases": 0, "configures": 0},
    {"id": 6, "create_time": "2019-11-06 14:30:42", "name": "三国演义项目", "leader": "吴承恩", "tester": "刘备",
     "programmer": "关羽", "publish_app": "三国演义应用",
     "desc": "念刘备、关羽、张飞，虽然异姓，既结为兄弟，则同心协力，救困扶危；上报国家，下安黎庶。不求同年同月同日生，只愿同年同月同日死。皇天后土，实鉴此心，背义忘恩，天人共戮！", "interfaces": 0,
     "testsuits": 0, "testcases": 0, "configures": 0},
    {"id": 7, "create_time": "2019-11-06 14:33:38", "name": "金瓶梅项目", "leader": "兰陵笑笑生", "tester": "潘金莲",
     "programmer": "西门庆", "publish_app": "金瓶梅研究项目", "desc": "富贵必因奸巧得，功名全仗邓通成。", "interfaces": 0, "testsuits": 0,
     "testcases": 0, "configures": 0},
    {"id": 8, "create_time": "2019-11-06 14:41:12", "name": "项目1", "leader": "某人", "tester": "某人", "programmer": "某人",
     "publish_app": "某应用", "desc": "某某描述", "interfaces": 0, "testsuits": 0, "testcases": 0, "configures": 0},
    {"id": 9, "create_time": "2019-11-06 14:42:00", "name": "项目2", "leader": "某人", "tester": "某人", "programmer": "某人",
     "publish_app": "某应用", "desc": "某某描述", "interfaces": 0, "testsuits": 0, "testcases": 0, "configures": 0},
    {"id": 10, "create_time": "2019-11-06 14:42:19", "name": "项目3", "leader": "某人", "tester": "某人", "programmer": "某人",
     "publish_app": "某应用", "desc": "某某描述", "interfaces": 0, "testsuits": 0, "testcases": 0, "configures": 0}],
             "total_pages": 2, "current_page_num": 1}


import jsonpath

# id = jsonpath.jsonpath(json_data, "$..id")
# print(id)


# name = jsonpath.jsonpath(json_data, "$..name")
# name3 = jsonpath.jsonpath(json_data, "$.results[2].name")
# print(name[2])
#
# print(name3)

# datas = jsonpath.jsonpath(json_data,"$.*")
# print(datas)


data = {"name":"musen","id":18,"msg":None}

json_data = '{"name":"musen","id":19,"msg":null}'


# --------------------错误示范-----------------
# 不能使用dict将json字符串转换为字典
# res1 = dict(json_data)
# print(res1)

# 不能使用eval将json字符串转换为字典,json中的null在python中无法识别，会当成变量处理
# res2 = eval(json_data)
# print(res2)

# ———————————————————正确用法---------------
import json

# 将json字符串转换为python类型的，会自动将null转换为None
res4 = json.loads(json_data)
print(res4,type(res4))

# 将python类型的数据转换为json字符串，会自动将None转换为null,
# json.dumps是将一个Python数据类型列表进行json格式的编码解析，
res5 = json.dumps(data)
print(res5,type(res5))

'''
json.dumps : dict转成str     json.dump是将python数据保存成json

json.loads:str转成dict          json.load是读取json数据 

'''


