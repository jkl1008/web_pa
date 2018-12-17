from selenium.webdriver import Chrome
import time
from bs4 import BeautifulSoup
import sys
class Spider:
    def __init__(self,index_url):
        self.index_url = index_url
        self.raw_htmls = []
        self.boot()

    def boot(self): # 启动浏览器&加载cookie
        self.chrome = Chrome(executable_path='./chromedriver.exe')  # 创建浏览器对象
        self.chrome.start_client()
        self.check_cookie()

    def check_cookie(self):
        from xcookie import cookie_list
        if cookie_list: #如果cookie list不为空
            self.chrome.get(self.index_url) #打开网页
            print('waiting for page loading')
            time.sleep(5)
            self.chrome.delete_all_cookies() #加载新的cookie前，清除浏览器之前的旧cookie，保证新Cookie 正确加载
            print('Clear all old cookies')
            for c in cookie_list: #加载Cookie
                self.chrome.add_cookie(c)
            print('done')
        else:
            print('pls add cookie first')
            sys.exit() #程序退出

    def crawl(self,target_url):
        self.chrome.get(target_url) # 打开网页
        print('waiting for loading page')
        time.sleep(2)
        self.raw_htmls.append(self.chrome.page_source) #获得每页的源代码

class Parser:
    def __init__(self,html_list):
        self.html_list = html_list
        self.raw_posts = []
        self.parse()

    def parse(self):
        for html in self.html_list:
            soup = BeautifulSoup(html,'html.parser')
            detail_sel = '.WB_detail' #要选择的元素
            detail_els = soup.select(detail_sel)
            for detail in detail_els:
                content = detail.get_text() #这一块里面所有文本都提取出来
                clean_text = content.replace(' ','').replace('\n','') #先把文本中的空格替换掉，再把换行符替换掉
                self.raw_posts.append(clean_text)
        print(self.raw_posts)


    def save_into_text(self):
        with open('./fav.txt','a+',encoding='utf-8') as f:
            for i in self.raw_posts:
                f.write(i)
                f.write('\n')
                f.write('---'*30)
                f.write('\n')
class Post:
    pass

s = Spider('https://weibo.com/')
s.crawl('https://weibo.com/fav')
p = Parser(s.raw_htmls)
p.save_into_text()
time.sleep(999)