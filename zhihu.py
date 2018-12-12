from selenium import webdriver
import time



def start_chrome():
    driver = webdriver.Chrome(executable_path='./chromedriver.exe')  # 实例化浏览器驱动实例
    driver.start_client()  # 打开客户端
    return driver
driver = start_chrome()

def find_strangers(driver):

    btn_sel = ''
    elems = driver.find_elements_by_css_selector(btn_sel)
    return  elems

def add_fren():
    pass

