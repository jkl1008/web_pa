from selenium.webdriver import Chrome # 从selenium.webdriver 导入 Chrome 类
import time
import pyautogui #导入桌面提醒的类
import webbrowser

class PageObserver:  # 定义一个监测网页内容变化的类
    def __init__(self,url,target_sel): # 定义类的属性
        self.driver = Chrome(executable_path='./chromedriver.exe')  # 自动化浏览器对象变成类的属性， self 是类里面的属性或行为
        self.url = url # url是从外界获得的属性，url 是爬取的网址
        self.target_sel = target_sel # target_sel 是页面定位元素
        self.request_time = 10 # 一开始初始化遵循一个默认值

    def is_changed(self):
        self.driver.get(self.url)
        time.sleep(self.request_time) # 避免频繁地访问网站被视为攻击性行为
        oos_sel = self.driver.find_elements_by_css_selector(self.target_sel) # elements 即使没有找到，也是一个空列表,找 OOS的对象
        buy_button = self.driver.find_elements_by_css_selector('button.single_add_to_cart_button.button.alt')
        print(oos_sel)
        print(buy_button)
        if not oos_sel and buy_button:
            return True
def alert():
    pyautogui.alert('The bag is available')


target_sel = 'a.oos div.swatch-container.swatch-1-colours div.swatch-column.colour-burgundy'
url = 'https://strathberry.cn/products/the-strathberry-nano-tote-burgundy-silver-hardware/'
target = PageObserver(url=url,target_sel=target_sel) #  实例化一个对象，对象首字母一般是大写,括号中第一个url 是类的属性名

while True:
    if target.is_changed(): # 调用类的函数
        alert()
        webbrowser.open(url) # 浏览器打开这个网站
        target.driver.close() #关闭之前的驱动浏览器
    else:
        print('None!')