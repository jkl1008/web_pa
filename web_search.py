# start_chrome → input_date → scroll_down → find_card_info → save → find_next(goto)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,os,csv

def start_chrome():
    driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    driver.start_client()
    return driver

def q(st,et):  # 定义查询日期函数
    return f'?is_ori=1&is_forward=1&is_text=1&is_pic=1&is_video=1&is_music=1&is_article=1&key_word=&start_time={st}&end_time={et}&is_search=1&is_searchadv=1#_0'

def scroll_down():
    html_page = driver.find_element_by_tag_name('html')  #找到页面
    for i in range(15):  # 重复往下翻滚动条
        html_page.send_keys(Keys.SPACE)
        time.sleep(0.6)  # 模拟停顿

def find_card_info():
    pass


driver = start_chrome()
driver.get('https://www.qq.com')
scroll_down()