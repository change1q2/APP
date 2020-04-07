"""
============================
Author:柠檬班-木森
Time:2019/11/22
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import logging

"""
logging模块默认收集的日志是warning以上等级的

"""
# 获取默认的日志收集器root
my_log = logging.getLogger()
# 设置默认的日志收集器登录
my_log.setLevel("DEBUG")

a = 100
logging.debug(a)
logging.info('这是INFO等级的信息')
logging.warning('这是WARNING等级的信息')
logging.error('这是ERROR等级的信息')
logging.critical('这是CRITICAL等级的信息')
