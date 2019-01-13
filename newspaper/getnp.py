from datetime import date
from bs4 import BeautifulSoup
import requests
import re


#获取当前日期，格式化为日报地址模式year-month/day
tdate = date.today()
datetmp = str(tdate).rsplit("-",1)

#url-address
hurl="http://epaper.wxrb.com/paper/wxrb/html/"+datetmp[0]+"/"+datetmp[1]+"/node_2.htm"
hheads={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
r_url=requests.get(hurl,headers=hheads)
print('获取地址状态：{}'.format(r_url.status_code))
soup = BeautifulSoup(r_url.content,'lxml')
get_soup=soup.find('div',class_="liebiao").select('a[href^="node"]')
#获取当日所有版面和地址
boarddict={}
for gs in get_soup:
    #版名
#    boardname = gs.text
    #地址
    boardaddr = gs.get("href")
    boarddict[gs.text]=boardaddr

#获取每版标题和地址
for key in boarddict.keys():
    board_url="http://epaper.wxrb.com/paper/wxrb/html/"+datetmp[0]+"/"+datetmp[1]+"/"+boarddict[key]
    print("{}:{}".format(key,board_url))