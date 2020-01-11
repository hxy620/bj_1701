from page.page_in import PageIn
from tools.get_driver import GetDriver


class TestAppArticle:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_app_driver()
        # 通过统一入口类获取 PageAppLogin对象
        self.page_in = PageIn(driver)

        # 调用登录业务成功方法（需要在PageAppLogin新增）
        self.page_in.page_get_PageAppLogin().page_app_login_success()

        # 获取pageapparticle对象
        self.article = self.page_in.page_get_PageAppArticle()

    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_app_driver()

    # 查找文章测试方法
    def test_app_article(self):
        # 调用查找文章方法
        self.article.page_app_article(find_text="python", title_text="python")
