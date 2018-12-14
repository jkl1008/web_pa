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
class Spider