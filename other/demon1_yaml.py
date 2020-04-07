'''
作者：seak
时间：
项目：
题目：
作用：
备注：
'''
import yaml

f = open('demo.yaml')

data = yaml.load(f, Loader=yaml.FullLoader)
print(data)

#username = data['person1']["data"]["username"]
# jsonpath,   $..username