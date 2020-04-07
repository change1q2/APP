



## 环境依赖

- 1，appium
  - 依赖 nodejs
  - net4.5.1.exe
  - [appium](<http://appium.io/>) 桌面程序。 下载 1.13 版本。
  - 安装给用户，而不是所有用户
- 2， java jdk1.8+  64位
- 3，android 环境 [adt-bundle](http://tools.android-studio.org/index.php/adt-bundle-plugin)， 
- 4,  手机。 模拟器或者真机, 雷电模拟器。genymotion. 
  - 开发者模式
  - USB 调试模式
- 5，Appium-Python-Client





## appium 安装注意事项

- 依赖 nodejs
- net4.5.1.exe
- [appium](<http://appium.io/>) 桌面程序。 ， 下载 1.13 版本。
- 安装给用户，而不是所有用户（记住安装位置）
- 确认安装成功。能够正常启动。





## java jdk 安装注意事项， java8

- 1.8 以上
- 64位
- 尽量下载高版本
- 下载慢，使用 [华为镜像](https://mirrors.huaweicloud.com/java/jdk/)
- 确认安装成功
  - 配置 JAVA_HOME 和 PATH 路径
  - cmd 命令行输入：`java -version`





## android sdk 环境安装注意事项

- 安卓开发新手集成包 [adt-bundle](http://tools.android-studio.org/index.php/adt-bundle-plugin) ;  

- 双击解压;

- 配置 ANDROID_HOME 变量;
- 确认安装成功：
  - 配置 adb 环境变量;
  - 配置 aapt 环境变量；
  - cmd 命令输入 `adb` 和 `aapt`。









## 更新 sdk tools

- 手机系统版本高，会报错；
- 安卓 api 向下兼容，下载新版本，低版本也能用。



![1564553653156](D:\data\雨泽\typora图片\1564553653156.png)



如果不能立即刷新，需要点击 tools -> option, 添加镜像：

![1564553752008](D:\data\雨泽\typora图片\1564553752008.png)



可以用的镜像地址：

1、中科院开源协会镜像站地址:

IPV4/IPV6 : http://mirrors.opencas.ac.cn 端口：80

2、北京化工大学镜像服务器地址：

IPv4: http://ubuntu.buct.edu.cn/  端口：80

IPv4: http://ubuntu.buct.cn/  端口：80

IPv6: http://ubuntu.buct6.edu.cn/  端口：80

3、大连东软信息学院镜像服务器地址:

http://mirrors.neusoft.edu.cn  端口：80





## 使用夜神模拟器要额外注意

参看夜神模拟器安装文件夹，里面有安装步骤和说明。

记得把 带有环境变量的 adb 命令命名到 夜神模拟器的 adb_nox



更新夜神手机系统版本

夜神多开形式进行修改：

![1564553917165](D:\data\雨泽\typora图片\1564553917165.png)









## appium 测试流程和原理



![1558276381905](D:\data\雨泽\typora图片\1558276381905.png)





## appium vs  selenium



![1558276288864](D:\data\雨泽\typora图片\1558276288864.png)





## Appium 为什么要采用这套架构

安卓，自己的自动化测试框架：uiautomator

苹果：xcui,  python



![1564558845920](D:\data\雨泽\typora图片\1564558845920.png)



Appium 旨在满足移动端自动化需求的理念，概述为以下四个原则：


- 你没有必要为了自动化而重新编译你的应用或者以任何方式修改它。
      Android/IOS系统自带框架
- 你不应该被限制在特定的语言或框架上来编写运行测试。
      WebDriver API
       客户端-服务器协议（称为 JSON Wire Protocol）
-  移动端自动化框架在自动化接口方面不应该重造轮子。
      WebDriver  - Web 浏览器自动化的标准
       附加可用于移动端自动化的 API 方法
- 移动端自动化框架应该开源，不但在名义上而且在精神和实践上都要实至名归。
      Appium开源
- 可以做混合应用，可以同时做原生应用和 H5, app嵌套 html
- html --> 嵌套，iframe  webview



### 系统官方的自动化框架

iOS 9.3 及以上：苹果的 XCUITest,    swift
iOS 9.3 及以下：苹果的 UIAutomation , object-c, 版本
Android 4.2+: 谷歌的 UiAutomator,   kotlin , pycharm ==> JVM, 安卓开发
Android 2.3+: 谷歌的 Instrumentation（通过绑定另外的项目—— Selendroid 提供 Instrumentation 的支持）    java， oracle


