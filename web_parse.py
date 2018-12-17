from bs4 import BeautifulSoup

with open('./new_index.html','r')as wb_data:
    soup = BeautifulSoup(wb_data,'lxml')
    images = soup.select('body > div.main-content > ul > li > img')
    titles = soup.select('body > div.main-content > ul > li > div.article-info > h3 > a')
    descs = soup.select('body > div.main-content > ul > li > div.article-info > p.description')
    rates = soup.select('body > div.main-content > ul > li > div.rate > span')
    cates = soup.select('body > div.main-content > ul > li > div.article-info > p.meta-info')

info = [] #把多个字典装入一个列表
for title,image,desc,rate,cate in zip(titles,images,descs,rates,cates):
    data = {
        'title':title.text,
        'desc':desc.text,
        'rate':rate.text,
        'cate':list(cate.stripped_strings), # stripped_strings 获得该标签下所有子节点的文本，生成一个列表
        'image':image.get('src') # 获得标签中的每个属性，用get方法
    }
    info.append(data)

#打印出大于3分的内容
for i in info:
    if float(i['rate'] )>3:
        print(i['title'],i['cate'])