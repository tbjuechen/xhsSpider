# from DrissionPage import ChromiumPage
import sqlite3

# 创建页面对象，并启动或接管浏览器
page = ChromiumPage()
# 跳转到登录页面
page.get('https://www.xiaohongshu.com/explore')

# 定位到账号文本框，获取文本框元素
ele = page.ele('#user_login')
# 输入对文本框输入账号
ele.input('您的账号')
# 定位到密码文本框并输入密码
page.ele('#user_password').input('您的密码')
# 点击登录按钮
page.ele('@value=登 录').click()
