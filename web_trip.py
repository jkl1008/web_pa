import requests
from bs4 import BeautifulSoup

url = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'
web_data = requests.get(url)
soup = BeautifulSoup(web_data.text,'lxml')
titles = soup.select('div.item.name > a')
for title in titles:
    print(title.get_text())
