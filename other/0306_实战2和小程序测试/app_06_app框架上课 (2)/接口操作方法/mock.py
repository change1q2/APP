'''
作者：seak
时间：
项目：
题目：
作用：
备注：
'''
from flask import Flask,jsonify,request
import flask,json
#1.导入flask中的Flask,jsonify,requewst

#2.创建flask对象，使用该对象进行配置与运行


#name是python中的特殊变量，如果文件作为主程序执行，
# __name__变量的值就是__main__,如果是被其他模块引入，那么__name__的值就是模块名称

server = flask.Flask(__name__) #把app.python当作一个server

#装饰器，将get_all_user()函数变为一个接口127.0.0.1：9000、get_user
@server.route('/get_user',methods=['get','post'])#参数路劲和请求方法
def get_all_user():
    all_user = [
        {'id':1,'sex':1,'real_name':'小花'},
        {'id': 2, 'sex': 0, 'real_name': '小明'},
        {'id': 1, 'sex': 1, 'real_name': '小黑'},
    ]
    res = json.dumps(all_user,ensure_ascii=False)#ensure_ascii为False时，可以包含non-ASCII字符
    return res

# 启动服务，debug=True表示修改代码后自动重启；
# 启动服务后接口才能访问，端口号为9000，默认ip地址为127.0.0.1
server.run(port=9000, debug=True)

#只在本页运行
if __name__ == '__main__':
    get_all_user()