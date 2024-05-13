from DrissionPage import ChromiumPage
import config

class ElementNotFound(Exception):...

class TaskGenerator(object):
    def __init__(self) -> None:
        self.start_page = config.STARTPAGE
        self.max_task = config.MAXTASK
        self.broswer = ChromiumPage()
    
    def head_page_init(self):
        self.broswer.get(self.start_page)
        self.close_login_box()
        self.turn_to_dressing_category()

    def close_login_box(self):
        '''
        关闭登录框
        '''
        # 查找 .login—container
        login_container_ele = self.broswer.ele('.login-container', timeout=2)
        # 存在登录框则关闭
        if login_container_ele:
            login_container_close_button_ele = login_container_ele.child('tag:div')
            login_container_close_button_ele.click()
    
    def turn_to_dressing_category(self):
        '''
        切换到穿搭分区
        '''
        # 查找 .content-container
        navigation_bar = self.broswer.ele('.content-container', timeout=2)
        if navigation_bar:
            dressing_button_ele = navigation_bar.child('tag:div', index=3)
            dressing_button_ele.click()
        else:
            raise ElementNotFound('navidation bar not found')
    
    def generate_task_url(self)-> set[str]:
        '''
        生成图片下载路径
        '''
        task_url_set = set()  # url集
        while(len(task_url_set) < self.max_task):
            content_node_eles = self.broswer.eles('.note-item',timeout=1)
            # print(content_node_eles)
            for node in content_node_eles:
                link_info_ele = node.ele('tag:a')
                task_url_set.add(link_info_ele.link)
            self.broswer.scroll.to_bottom()  # 滚动到底部 触发ajax加载
        return task_url_set                 

# 测试
if __name__=='__main__':
    tg = TaskGenerator()
    tg.head_page_init()
    tg.generate_task_url()