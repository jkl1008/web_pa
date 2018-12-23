#用requests的方法添加cookies
import requests
from bs4 import BeautifulSoup
'''
url = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'
web_data = requests.get(url)
soup = BeautifulSoup(web_data.text,'lxml')
titles = soup.select('a.poiTitle')
imgs = soup.select('div.centering_wrapper img.photo_image') # 方括号中间为标签的属性值
cates = soup.select('div.detail > div:nth-of-type(4)') # Soup 里 nth-child 要改为nth-of-type
for title,img,cate in zip(titles,imgs,cates): #将三组数据装入字典
    data = {
        'title':title.get_text(),
        'img':img.get('src'),
        'cate':cate.get_text()
    }
    print(data)
'''
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Cookie':'TASSK=enc%3AAP14r4WR%2Blx8HIg7GJ6iqqBnDkExUAWJOuVecLlqV1HHuvvOGywYqjtGMgE67X6NUeC%2FIRfv3wNKdGfxynSvUyNI4Tdds8TtWjbCAOeB5lINflF%2FvYpJkPFG4g77s5A5qQ%3D%3D; ServerPool=A; TART=%1%enc%3AMePodR6gFlmC7Sd5yUEFvrCLQ%2BYU1KTuE8D%2FFFxtbB%2F2lrBvQTfgYnDljqs1D5qphOAaWX%2FoYRI%3D; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RS.1; CM=%1%PremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CRestAds%2FRPers%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CRestPartSess%2C%2C-1%7CUVOwnersSess%2C%2C-1%7CCCUVOwnPers%2C%2C-1%7CRestPremRSess%2C%2C-1%7CCCSess%2C%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CTADORSess%2C%2C-1%7CAdsRetPers%2C%2C-1%7CTARSWBPers%2C%2C-1%7CSPMCSess%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CSPMCWBPers%2C%2C-1%7CRBAPers%2C%2C-1%7CRestAds%2FRSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7CRestPartPers%2C%2C-1%7CRestPremRPers%2C%2C-1%7CCCUVOwnSess%2C%2C-1%7CUVOwnersPers%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCCPers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CSPMCPers%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CAdsRetSess%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CTADORPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CTARSWBSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7CSPORPers%2C%2C-1%7Cperssticker%2C%2C-1%7CSPMCWBSess%2C%2C-1%7C; TAUnique=%1%enc%3ApVZSfiziNCBqwGglQJMmUjqGX0tLcYRZX8rSwAIpd5bLH0eO5X1%2BTQ%3D%3D; _ga=GA1.2.2012206963.1545568094; _gid=GA1.2.1168308404.1545568094; Hm_lvt_cdce8cda34e84469b1c8015204129522=1545568094,1545571647; SecureLogin2=3.4%3AAMtSAQq4sAsHRDDyAKTH%2FUeb6wKk%2FH3TM08xHpH41Iz7CgRmnL2D9d6hPEOnjnbt1Ay0rlOqemNt77knoZdtDrL%2BziroPK8lwZmt21ldgFvWLxsnQYuHl0YMYwb6tMZk9lLK9VvMOJsAf%2FuxaTdULrFBQi7zPE8WmU9wQel8HI%2FMwp3TE4NfsANL7%2FB5gVnMcB4N0Uwj86Y6G1Y%2Fyho3jnU%3D; TAAuth3=3%3Adeb98e92b47aff16b4a55a3db0461207%3AAFayhkF1ZGPEYMCA9T7yWE85dheT7mtQGo9uaSmWUTrcOlWE3dKcI0G78t4Ndmmfvq2hQ0u5LkwVpADxSo8HDLD55rNr6lLWkXJEPwDSHoFbrxrgb0QrAjDoIY2cLCgtB1FxTz6aouCjtatkUAdd4okVnZKODOlLCakzhZhMIIwvsEQXsndiYB%2FfhHLyBBf%2B6A%3D%3D; TAReturnTo=%1%%2FAttraction_Review-g60763-d587661-Reviews-Top_of_the_Rock-New_York_City_New_York.html; roybatty=TNI1625!AEL7hsAndCS5bmHO6uLQAXonq7uTAxFY5sSKqZ9fFhtEKEYG6mbWhfvgKv4%2BDgX0qBYwhgkjGFDXwYskWE7b2Glaw59QxK1eGvjtM5e3v4htrxvXamWxTww4%2BJl0pJcr5aMVtLmn53gNMd2f%2Bh4tm9NLblbK6tKPZ799kSTWnCsW%2C1; _gat_UA-79743238-4=1; Hm_lpvt_cdce8cda34e84469b1c8015204129522=1545571676; TASession=%1%V2ID.9C63B008C81DA598F40A3833A1DE34FC*SQ.25*LP.%2FAttractions-g60763-Activities-New_York_City_New_York%5C.html*PR.39766%7C*LS.DemandLoadAjax*GR.84*TCPAR.68*TBR.84*EXEX.64*ABTR.40*PHTB.62*FS.47*CPU.55*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.64B712FB9B75C7DEE2C055283C4D19F3*LF.zhCN*FA.1*DF.0*MS.-1*RMS.-1*FLO.60763*TRA.false*LD.587661; TAUD=LA-1545568101433-1*RDD-1-2018_12_23*LG-3588701-2.1.F.*LD-3588702-.....'
}
url_saves = 'https://www.tripadvisor.cn/Saves/1463691'
wb_data = requests.get(url_saves,headers=headers) #将headers信息传递给 requests.get 的参数，模拟带cookie登录
soup = BeautifulSoup(wb_data.text,'lxml')
print(soup)