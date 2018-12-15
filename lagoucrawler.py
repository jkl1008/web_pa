#coding=utf-8
'''
#以下是面向过程的写法，可复用性不强
#get_page → parse_page → filter_job → send（）
raw_html = []
for i in range(30):
    page = get_page()
    raw_html.append(page)

all_jobs = []
for html in raw_html:
    jobs = parse(html)
    all_jobs.append(jobs)

for job in all_jobs:
    result = filter_job(job)
    if result:
        send(job)
'''
#以下是面向对象的写法，按照职责划分
'''
#Spider → Parser（解析器） → Job（类自身提供可过滤的方法）
s = Spider()
raw_pages = s.crawl(url) #后面带点的是类，
p = Parser(raw_pages)
jobs = p.get_jobs()
for j in jobs:
    if j.is_today():
        j.send_to_me()
'''
# -*- encoding = UTF-8 -*-
from selenium.webdriver import Chrome
import time
from bs4 import BeautifulSoup

#url = 'https://www.lagou.com/zhaopin/qukuailian/12/'
class Spider:
    def __init__(self,index_url): # 初始化的时候创建浏览器并启动,__init__ 相当于一个公共空间
        self.page_range = 30
        self.index_url = index_url
        self.boot() #为了__init__ 看着整洁，包装一个boot 方法
        self.raw_pages = [] # 存放爬好的页

    #建立一个浏览器启动方法
    def boot(self):
        self.chrome = Chrome(executable_path='./chromedriver.exe')  # 创建浏览器对象
        self.chrome.start_client()# 启动浏览器

    def crawl(self):
        for num in range(self.page_range):
            full_url = f'{self.index_url}{str(num+1)}/'
            self.chrome.get(full_url)
            print(f'waiting for loading {str(num+1)} page')
            time.sleep(2)
            single_html = self.chrome.page_source # 获得每页的源代码
            self.raw_pages.append(single_html)
            print(f'{str(num+1)} page done')
        return self.raw_pages

class Parser:
    def __init__(self,raw_pages):
        self.raw_pages = raw_pages
        self.jobs = []
        self.parse() # 保证初始化时已经爬取好信息
    def parse(self):
        for html in self.raw_pages:
            soup = BeautifulSoup(html,'html.parser') # html.parser为解析器，构建soup 对象
            time_sel = 'span.format-time'
            link_sel = 'div.p_top a'
            comp_sel = 'div.company_name a'

            time_els = soup.select(time_sel) #选取所有时间的元素列表
            link_els = soup.select(link_sel)
            comp_els = soup.select(comp_sel)

            for t,l,c in zip(time_els,link_els,comp_els):
                cell =  {
                        'time':t.text,
                        'link':l.get('href'),
                        'comp':c.text,
                    }
                self.jobs.append(cell)
    def get_jobs(self): # 将爬取到的每条job信息带入判断job的实例中
        return [Job(j) for j in self.jobs]

class Job(): #判断job 的性质，对job 数据进行保存、发送等工作
    def __init__(self,data):
        self.time = data.get('time')
        self.link = data.get('link')
        self.comp = data.get('comp')

    def is_today(self):
        return ':' in self.time

    def send(self):
        pass

    def save_into_csv(self):
        pass

s = Spider(index_url= 'https://www.lagou.com/zhaopin/qukuailian/')
s.page_range = 3
s.crawl() #开始爬取网页
p = Parser(s.raw_pages)
jobs = p.get_jobs()

for j in jobs:
    if j.is_today():
        print(j.comp,j.link)
