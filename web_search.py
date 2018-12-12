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
    for i in range(20):  # 重复往下翻滚动条
        html_page.send_keys(Keys.SPACE)
        time.sleep(0.6)  # 模拟停顿

def find_card_info():
    cards_sel = 'div.WB_feed_detail' #每条微博的Card
    cards = driver.find_elements_by_css_selector(cards_sel) #找到所有微博Card,生成一个列表
    info_list = []
    for card in cards:
        content_sel = 'div.WB_text.W_f14' #每条微博的内容
        time_sel = 'div.WB_from.S_txt2' #每条微博的发布时间
        link_sel = 'div.WB_from.S_txt2 > a:nth-child(1)' #每条微博的链接
        content =  card.find_element_by_css_selector(content_sel).text #获得对应元素的内容
        time = card.find_element_by_css_selector(time_sel).text #获得对应元素的内容
        link = card.find_element_by_css_selector(link_sel).get_attribute('href') #获得每条微博的链接
        info_list.append([content,time,link]) #类似这样的结构[[1,2,3],[4,5,6]
    return info_list

def find_next():
    next_sel = 'a.page.next'
    next_page = driver.find_elements_by_css_selector(next_sel)
    if next_page: #如果next_page是一个列表
        return next_page[0].get_attribute('href') #url
def save(info_list,name): # 定义一个保存信息成csv 格式的函数
    full_path = './' + name + '.csv'
    if os.path.exists(full_path): #如果已经存在文件，以追加的方式写入
        with open(full_path, 'a') as f:
            writer = csv.writer(f)  # 实例化一个csv的写入对象
            writer.writerows(info_list)# 将info_list写入csv
            print("done")
    else:
        with open(full_path,'w+') as f:
            writer = csv.writer(f) # 实例化一个csv的写入对象
            writer.writerows(info_list) #将info_list写入csv
            print("done")

def run_crawler(base,duration):
    #2018-01-01~2018-12-12
    if not base.endswith('feedtop'):
        st,et = duration.split('~') # 将日期段拆开成字符串
        driver.get(base + q(st,et))
    else:
        driver.get(base)# 打开微博查询页面
    time.sleep(5) # 设置下等待时间
    scroll_down()
    time.sleep(5) #网络可能没那么快，设置下等待
    info_list = find_card_info()
    save(info_list,duration)
    next_page = find_next()
    if next_page:
        run_crawler(next_page,duration)
base = 'https://weibo.com/p/1004061195242865/home' # 设定基本url
driver = start_chrome() # 打开浏览器
driver.get('https://weibo.com')
time.sleep(18)
run_crawler(base,'2018-08-01~2018-12-12')