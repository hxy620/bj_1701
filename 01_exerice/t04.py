#导包
import threading
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

#打开 百度封装
def get_baidu(driver):
    driver.get("http://baidu.com")
    driver.find_element_by_id("kw").send_keys("python")
    driver.find_element_by_id("su").click()
    driver.quit()

#获取 driver 封装
def get_driver(browserName):   #浏览器名称
    cap = None
    if browserName=="chrome":
        cap = DesiredCapabilities.CHROME.copy()
        #修改默认平台  名称
        cap['platform'] = "WINDOWS"
    elif browserName == "firefox":
        cap = DesiredCapabilities.FIREFOX.copy()
        cap['platform'] = "WINDOWS"

    return webdriver.Remote("http://127.0.0.1:4444/wd/hub",cap)

#多线程  遍历调用
browsers = ['chrome','firefox']
# browsers = ['chrome']
for browser in browsers:
    #获取driver
    driver = get_driver(browser)
    #实例多线程  并 启动
    threading.Thread(target=get_baidu,args=(driver,)).start()
