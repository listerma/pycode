'''
@Description: 测试用文件
@Author: kinston.ding
@Date: 2019-01-14 19:32:49
@LastEditors: kinston.ding
@LastEditTime: 2019-01-14 20:40:49
'''
from bs4 import BeautifulSoup
import requests

def get_board(surl,sclass,shref):
    hheads={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    r_url = requests.get(surl,headers=hheads)
    if r_url.status_code == 200:
        soup = BeautifulSoup(r_url.content,'lxml')
        get_soup = soup.find('div',class_=sclass).select(shref)
        print("get_soup:",get_soup)
    else:
        print("网址不可访问！")

        
        #字典boarddict保存board_name:board_addr
    boarddict = {}
    for gs in get_soup:
        boarddict_name = gs.text
        boarddict_addr = gs.get("href")
        boarddict[boarddict_name]=boarddict_addr
    return boarddict

surl = 'http://epaper.wxrb.com/paper/wxrb/html/2019-01/13/node_2.htm'
sclass = 'liebiaoA'
shref = 'a[href^="content"]'
mydict = get_board(surl,sclass,shref)
for item in mydict.keys():
        print('{}:{}'.format(item,mydict[item]))