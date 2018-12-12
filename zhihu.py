from selenium import webdriver
import time

def start_chrome():
    driver = webdriver.Chrome(executable_path='./chromedriver.exe')  # 实例化浏览器驱动实例
    driver.start_client()  # 打开客户端
    return driver

def find_strangers():
    btn_sel = '#Profile-following > div:nth-child(2) > div > div > div > div.ContentItem-extra > button' #按钮的路径
    elems = driver.find_elements_by_css_selector(btn_sel) # 找到按钮元素
    return elems

def add_fren():
    pass


url = 'https://www.zhihu.com/'
follower_url = 'https://www.zhihu.com/people/mmfff/following'
driver = start_chrome() #实例化一个浏览器对象
driver.get(url) # 打开知乎网站首页
time.sleep(20) #等待登陆输入
driver.get(follower_url)
time.sleep(6) # 等待好友网站加载
strangers = find_strangers()
for s in strangers:
    s.click()
    time.sleep(3) # 防止网站封锁爬虫，每次点击后间隔3s
print('完成加好友了')
