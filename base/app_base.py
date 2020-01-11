from time import sleep

from selenium.webdriver.common.by import By

from base.base import Base


class AppBase(Base):
    """存储 app应用专属方法"""

    def base_app_right_to_left(self, area_loc, find_text):
        # 获取区域元素
        el = self.base_find(area_loc)
        #获取区域 位置
        location = el.location
        y = location.get("y")

        # 获取元素宽高
        size = el.size
        # 宽
        width = size.get("width")
        # 高
        height = size.get("height")

        # 计算 start_x  start_y end_x end_y
        start_x = width * 0.8
        start_y = y + height * 0.5
        end_x = width * 0.2
        end_y = y + height * 0.5

        # 组合 find_text包含的元素定位信息
        loc = By.XPATH, "//android.widget.HorizontalScrollView//*[contains(@text,'{}')]".format(find_text)

        # 获取当前页面结构
        page_soure = self.driver.page_source

        while True:
            # 首先  查找一次当前页面是否存在 要找的元素
            try:
                el = self.base_find(loc,timeout=2)
                print("找到指定频道了!")
                el.click()
                # 跳出循环
                break
            except:
                print("当前页面没有找到指定的频道元素!")
                # 滑动屏幕
                self.driver.swipe(start_x, start_y, end_x, end_y, 2000)

            if page_soure == self.driver.page_source:
                print("滑不动了")
                raise Exception("异常啦!,滑到最后一屏幕也没找到!")
            else:
                #更新
                page_soure = self.driver.page_source

    # # 滑动屏幕操作
    # def swipe_screen(self, tag=1):
    #     # 获取屏幕分辨率
    #     size = self.driver.get_window_size()
    #     # 宽
    #     width = size.get("width")
    #     # 高
    #     height = size.get("height")
    #
    #     # 滑动前等待
    #     sleep(2)
    #     '''滑动'''
    #     # 向上      宽*0.5 高*0.5 宽0.5 高*0.2
    #     if tag == 1:
    #         self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2, 2000)
    #
    #     # 向下      宽*0.5 高*0.2 宽0.5 高*0.8
    #     if tag == 2:
    #         self.driver.swipe(width * 0.5, height * 0.2, width * 0.5, height * 0.8, 2000)
    #
    #     # 向左      宽*0.8 高*0.5 宽0.2 高*0.5
    #     if tag == 3:
    #         self.driver.swipe(width * 0.8, height * 0.5, width * 0.2, height * 0.5, 2000)
    #
    #     # 向右      宽*0.2 高*0.5 宽0.8 高*0.5
    #     if tag == 4:
    #         self.driver.swipe(width * 0.2, height * 0.5, width * 0.8, height * 0.5, 2000)

    def base_app_down_to_up(self,area_loc,find_text):
        # size = self.driver.get_window_size()
        el = self.base_find(area_loc)
        size = el.size
        # 宽
        width = size.get("width")
        # 高
        height = size.get("height")

        # 计算 start_x  start_y end_x end_y
        start_x = width * 0.5
        start_y = height * 0.8
        end_x = width * 0.5
        end_y = height * 0.2

        # 组合 find_text包含的元素定位信息
        loc = By.XPATH, "//*[@bounds='[0,390][1080,1716]']//*[contains(@text,'{}')]".format(find_text)

        # 获取当前页面结构
        page_soure = self.driver.page_source

        while True:
            # 首先  查找一次当前页面是否存在 要找的元素
            try:
                print("正在查找包含文章标题:{}".format(find_text))
                el = self.base_find(loc, timeout=2)
                print("找到 包含 {} 文章的标题！ ->文章标题为:{}".format(find_text, el.text))
                el.click()
                # 跳出循环
                break
            except:
                print("当前页面没有找到指定的文章标题!")
                # 滑动屏幕
                self.driver.swipe(start_x, start_y, end_x, end_y, 2000)

            if page_soure == self.driver.page_source:
                print("滑不动了")
                raise Exception("异常啦!,滑到最后一屏幕也没找到!")
            else:
                # 更新
                page_soure = self.driver.page_source
