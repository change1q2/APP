#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

import yaml

f = open('demo.yaml')

data = yaml.load(f, Loader=yaml.FullLoader)
print(data)

username = data['person1']["data"]["username"]
# jsonpath,   $..username