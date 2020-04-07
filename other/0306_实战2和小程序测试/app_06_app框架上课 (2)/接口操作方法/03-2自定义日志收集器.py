"""
============================
Author:柠檬班-木森
Time:2019/11/22
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import logging

# 一、创建一个名为：python24的日志收集器
my_log = logging.getLogger("python24")

# 二、设置日志收集器的等级
my_log.setLevel("DEBUG")

# 三、添加输出渠道（输出到控制台）
# 1、创建一个输出到控制台的输出渠道
sh = logging.StreamHandler()
# 2、设置输出等级
sh.setLevel("ERROR")
# 3、将输出渠道绑定到日志收集器上
my_log.addHandler(sh)

# 四、添加输出渠道（输出到文件）
fh = logging.FileHandler("log.log",encoding="utf8")
fh.setLevel("DEBUG")
my_log.addHandler(fh)

# 五、设置日志输出的格式
# 创建一个日志输出格式
formatter = logging.Formatter('%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s')
# 将输出格式和输出渠道进行绑定
sh.setFormatter(formatter)
fh.setFormatter(formatter)


my_log.debug("这个是自己记录了的debug等级的日志")
my_log.info("这个是自己记录了的info等级的日志")
my_log.warning("这个是自己记录了的warning等级的日志")
my_log.error("这个是自己记录了的error等级的日志")
my_log.critical("这个是自己记录了的critical等级的日志")
