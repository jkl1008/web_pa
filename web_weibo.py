from selenium import webdriver
import time

url = 'https://weibo.com/bgsxy?from=feed&loc=at&nick=%E5%8A%9E%E5%85%AC%E5%AE%A4%E5%B0%8F%E9%87%8E&is_hot=1#1544192932058'
def start_chrome():
    driver = webdriver.Chrome(executable_path='./chromedriver.exe') #实例化浏览器驱动实例
    driver.start_client() #打开客户端
    return driver

def find_info(): #找到浏览器对应的元素
    sel = '#Pl_Official_MyProfileFeed__21 > div > div:nth-child(2) > div.WB_feed_handle > div > ul > li > a > span > span > span > em:nth-child(2)'
    elems = driver.find_elements_by_css_selector(sel)
    return [int(el.text) for el in elems[1:]]

while True:
    driver = start_chrome() # 调用 start_chrome 函数
    driver.get(url)  # 打开网站
    time.sleep(8) # 等待页面加载
    info = find_info() #找到元素
    print(info)
    rep,com,like = info
    if rep > 70000:
        print(f'你关注的微博转发已经过{rep}') #f-string
        break
    else:
        print('Not happening')
    time.sleep(1200)
print('好了')
