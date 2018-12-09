from selenium import webdriver
import time

def start_chrome():
    driver = webdriver.Chrome(executable_path='./chromedriver.exe') #实例化浏览器驱动实例
    driver.start_client() #打开客户端
    return driver