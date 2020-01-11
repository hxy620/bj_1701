from time import sleep

from selenium.webdriver.common.by import By

from base.base import Base


class webBase(Base):
    # 选择状态  ul---li
    def web_base_click_ul_li(self, placeholder_text,click_text):
        # 组合placeholder 文本元素定位信息
        loc = By.XPATH, "//*[@placeholder='{}']".format(placeholder_text)
        # 查找元素并点击
        self.base_click(loc)
        sleep(2)
        # 定位 ul>li  -- 列表
        loc1 = By.CSS_SELECTOR, "ul>li"

#运用遍历的原因是如果内部是滚动条 是无法加载出内容的
        # 遍历text 内容等于click_text 条件成立 :click()
        for el in self.base_finds(loc1):
            if el.text == click_text:
                el.click()
                break


    #判断元素是否存在
    def web_base_element_exists(self,text):
        loc = By.XPATH,"//*[contains(text(),'{}')]".format(text)
        try:
            self.base_find(loc,timeout=3)
            print("找到元素")
            return True  #说明页面存在元素
        except:
            print("没有找到元素")
            return False  #页面元素不存在