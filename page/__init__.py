from selenium.webdriver.common.by import By
from tools.read_yaml import read_yaml

'''一下为黑马头条项目url'''
#自媒体
url_mp = "http://ttmp.research.itcast.cn/#/login"
#h后台管理
url_mis =  "http://ttmis.research.itcast.cn/#/"

'''APP包名启动名'''
appPackage ="com.itcast.toutiaoApp"
appActivity =".MainActivity"



"""以下为文章配置数据"""
article_title = read_yaml("mp_article.yaml")[0][0]
article_channel = "数据库"


''' 以下为自媒体配置数据'''
#手机号
mp_phone = By.CSS_SELECTOR,"[placeholder ='请输入手机号']"

#验证码
mp_code = By.CSS_SELECTOR,"[placeholder='验证码']"

#登陆el-button el-button--primary
my_login = By.CSS_SELECTOR,".el-button--primary"

#昵称
my_name = By.CSS_SELECTOR,".user-name"


'''发表文章'''
# 点击内容管理
mp_content_manage = By.XPATH, "//div[@class='menu-wrapper']//*[text()='内容管理']"
# 点击发布文章
mp_publish_article = By.XPATH, "//*[contains(text(),'发布文章')]"
# 输入标题
mp_title = By.CSS_SELECTOR, "[placeholder='文章名称']"
# 输入内容之前要切换iframe
mp_iframe = By.CSS_SELECTOR, "#publishTinymce_ifr"
# 输入内容
mp_content = By.CSS_SELECTOR, "#tinymce"
# 选择封面
mp_cover = By.XPATH, "//*[text()='自动']"
# 选择点击请选
mp_select = By.CSS_SELECTOR, "[placeholder='请选择']"
# 点击具体频道
mp_select_database = By.XPATH, "//*[text()='{}']".format(article_channel)
# 点击发表
mp_commit = By.CSS_SELECTOR, ".el-button.filter-item.el-button--primary"
# 获取发表结果
mp_commit_result = By.XPATH, "//*[contains(text(),'成功')]"


'''以下为后台管理页面配置数据'''
#用户名
mis_username = By.CSS_SELECTOR, '[placeholder="用户名"]'

#密码
mis_pwd = By.CSS_SELECTOR, "[placeholder='密码']"

#登录按钮
mis_login_btn = By.CSS_SELECTOR, "#inp1"

#昵称
mis_nickname = By.CSS_SELECTOR, ".user_info>span"


'''信息管理'''
#信息管理
mis_info_manage = By.XPATH,'//*[@class="menu"]//*[text()="信息管理"]'
#内容审核
mis_content_audit = By.XPATH,'//*[@class="menu"]//*[text()="内容审核"]'
#标题
mis_title = By.CSS_SELECTOR,'[placeholder="请输入: 文章名称"]'
#频道
mis_channel = By.CSS_SELECTOR,'[placeholder="请输入: 频道"]'
#查询
mis_search = By.CSS_SELECTOR,".find"
#通过
mis_pass_btn = By.XPATH,"//*[text()='通过']/.."
#确认通过
mis_confirm_pass = By.CSS_SELECTOR,".el-button--primary"

#文章id
mis_article_id = By.CSS_SELECTOR,".cell>span"




'''以下为APP应用配置数据'''
# 用户名
app_username = By.XPATH, "//*[@index='1' and @class='android.widget.EditText']"
# 密码
app_pwd = By.XPATH, "//*[@index='2' and @class='android.widget.EditText']"
# 登录按钮
app_login_btn = By.XPATH, "//*[@index='4' and @class='android.widget.Button']"
# 判断登录成功
app_me = By.XPATH, "//*[@index='3' and contains(@text,'我的')]"
#频道
app_area = By.XPATH, "//*[@class='android.widget.HorizontalScrollView']"
#文章区域
app_article_area = By.XPATH,"//*[@bounds='[0,390][1080,1716]']"



