#导包
from selenium import webdriver
from time import sleep

#定义启动参数
cap = { "browserName": "chrome",
        "version": "",
        "platform": "WINDOWS",
        }
#获取浏览器驱动对象
driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub",cap)
#打开百度url
driver.get("http://www.baidu.com")
#输入python
driver.find_element_by_css_selector("#kw").send_keys("python")
#点击按钮
driver.find_element_by_css_selector("#su").click()
#暂停,关闭浏览器
sleep(3)
driver.quit()