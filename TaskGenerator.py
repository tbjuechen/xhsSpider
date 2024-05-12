from DrissionPage import ChromiumPage
import config

class TaskGenerator(object):
    def __init__(self) -> None:
        self.start_page = config.STARTPAGE
        self.broswer = ChromiumPage()
    
    def head_page_init(self):
        self.broswer.get(self.start_page)
        self.close_login_box()

    def close_login_box(self):
        # 查找 .login—container 元素
        login_container_ele = self.broswer.ele('.login-container', timeout= 2)
        # 存在登录框则关闭
        if login_container_ele:
            login_container_close_button_ele = login_container_ele.child('tag:div')
            login_container_close_button_ele.click()


# 测试
if __name__=='__main__':
    tg = TaskGenerator()
    tg.head_page_init()
    tg.close_login_box()