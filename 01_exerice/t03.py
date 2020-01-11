'''
目标 : 动态获取浏览器启动参数
原因 : 不同浏览器,启动参数有差异,由于不适合记忆,可以参考复制
'''
from selenium.webdriver import  DesiredCapabilities
#调用copy方法复制字典
ff = DesiredCapabilities.FIREFOX.copy()
#修改默认平台名为ANY
ff['platform'] = "WINDOWS"
print(ff)





