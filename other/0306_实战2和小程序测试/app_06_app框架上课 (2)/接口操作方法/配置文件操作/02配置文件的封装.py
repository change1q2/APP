"""
============================
作者:seak
时间:
邮件:274882401@qq.com
作用：
题目：配置文件的封装
============================
"""

from configparser import ConfigParser

#不使用继承的方法获取所有的数据都要重写一遍获取数据不同的方法
class MyConf:
    #配置文件的文件名要从外面传过来，使用————init__初始化，并传入filename（文件名）和读取模式utf8
    def __init__(self, filename, encoding="utf8"):
        """
        :param filename: 配置文件名
        :param encoding: 文件编码方式
        """
        self.filename = filename
        self.encoding = encoding
        # 创建一个文件解析对象，设为对象的conf
        self.conf = ConfigParser()
        # 使用解析器对象，加载配置文件中的内容
        self.conf.read(filename, encoding)

    #定义一个读取方法，并把section, option（配置文件中的数据）传进去
    '''
    补充说明：
    conf文件 
    [logging]  块----》section
    level = DEBUG 配置项----》option
    f_level = DEBUG
    s_level = ERROR
    
    '''
    def get_str(self, section, option):
        """
        读取数据
        :param section: 配置块
        :param option: 配置项
        :return: 对应配置项的数据
        """
        return self.conf.get(section, option)

    def get_float(self, section, option):
        """
        读取数据
        :param section: 配置块
        :param option: 配置项
        :return: 对应配置项的数据
        """
        return self.conf.getfloat(section, option)

    def get_bool(self, section, option):
        """
        读取数据
        :param section: 配置块
        :param option: 配置项
        :return: 对应配置项的数据
        """
        return self.conf.getboolean(section, option)

    def write_data(self, section, option, value):
        """
        写入数据
        :param section: 配置块
        :param option: 配置项
        :param value:  配置项对应的值
        """
        # 写入内容
        self.conf.set(section, option, value)
        # 保存到文件
        self.conf.write(open(self.filename, "w", encoding=self.encoding))

#使用继承的方法，会方便很多，不用一个个定义
#定义一个MyConf2类继承ConfigParser方法    继承格式：  类名.(继承的类名)
class MyConf2(ConfigParser):

    def __init__(self, filename, encoding="utf8"):
        # 调用父类原来的init方法
        super().__init__()#super继承父类
        self.filename = filename
        self.encoding = encoding
        self.read(filename, encoding)

    def write_data(self, section, option, value):
        self.set(section, option, value)
        self.write(open(self.filename, "w", encoding=self.encoding))

#读取和写入数据
if __name__ == '__main__':
    # conf = MyConf("conf.ini")
    # res = conf.get_str("mysql", "host")
    # print(res)
    # conf.write_data("mysql", "database", "test_lemon")

    conf = MyConf2("conf.ini")
    # 读取数据,get由继承过来的
    res = conf.get("mysql", "database")
    print(res)
    conf.write_data("mysql", "databse2", "lemon2")