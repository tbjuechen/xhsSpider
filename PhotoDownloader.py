import time
import os


import config

from DrissionPage import ChromiumPage
from DrissionPage._elements.chromium_element import ChromiumElement


class PhotoDownloader():
    def __init__(self) -> None:
        self.down_path = config.DOWNPATH
        # 初始化下载文件夹
        if os.path.exists(self.down_path):
            pass
        else:
            os.makedirs(self.down_path)

        self.timeout = config.INTIMEOUT
        self.broswer = ChromiumPage()
    

    def wait(self):
        '''
        等待
        '''
        time.sleep(self.timeout)

    def turn_to_target_page(self, target_page:str):
        '''
        跳转到指定页面
        '''
        self.broswer.get(target_page)
        self.wait()
    
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

    def is_video(self)-> bool:
        '''
        判断是否为视频笔记
        '''
        video_ele = self.broswer.ele('tag:video', timeout=1)
        if video_ele:
            return True
        else:
            return False

    def collect_photo_srcs(self)->list[str]:
        '''
        获取图片列表
        '''
        photo_container_ele = self.broswer.ele('.swiper-wrapper',timeout=2)
        if photo_container_ele:
            photo_eles = photo_container_ele.children('tag:div')[1:-1]
            srcs = [item.style('background-image')[5:-2] for item in photo_eles]
        return srcs
    
    def down_photo(self, photo_url):
        self.broswer.get(photo_url)
        img = self.broswer.ele('tag:img')
        img.save(path=self.down_path)

    def new_task(self, task_url):
        '''
        下载任务
        '''
        self.turn_to_target_page(task_url)
        self.close_login_box()
        if self.is_video():
            # 视频笔记 跳过
            pass
        else:
            photo_srcs = self.collect_photo_srcs()
            for item in photo_srcs:
                self.down_photo(item)

# 测试
if __name__ == '__main__':
    pd = PhotoDownloader()
    pd.new_task('https://www.xiaohongshu.com/explore/645782e80000000027001d5d')

