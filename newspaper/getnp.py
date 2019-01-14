'''
@Description: 
@Author: kinston.ding
@Date: 2018-12-24 21:55:09
@LastEditors: kinston.ding
@LastEditTime: 2019-01-14 22:16:48
'''
from datetime import date
from bs4 import BeautifulSoup
import requests
import re


#func:get_board  返回dict{版名：地址}
def get_board(surl,sclass,shref):
    hheads={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    r_url = requests.get(surl,headers=hheads)
    if r_url.status_code == 200:
        soup = BeautifulSoup(r_url.content,'lxml')
        get_soup = soup.find('div',class_=sclass).select(shref)
        # print("get_soup:",get_soup)
    else:
        print("网址不可访问！")

        
        #字典boarddict保存board_name:board_addr
    boarddict = {}
    for gs in get_soup:
        boarddict_name = gs.text
        boarddict_addr = gs.get("href")
        boarddict[boarddict_name]=boarddict_addr
    return boarddict

    
#获取当前日期，格式化为日报地址模式year-month/day
tdate = date.today()
datetmp = str(tdate).rsplit("-",1)

#url-address
hurl="http://epaper.wxrb.com/paper/wxrb/html/"+datetmp[0]+"/"+datetmp[1]+"/node_2.htm"
#获取当日所有版面和地址
day_class = "liebiao"
day_href = 'a[href^="node"]'
day_board = get_board(hurl,day_class,day_href)
#获取每版标题和地址
for key in day_board.keys():
    sboard_url="http://epaper.wxrb.com/paper/wxrb/html/"+datetmp[0]+"/"+datetmp[1]+"/"+day_board[key]
    sboard_class = 'liebiaoA'
    sboard_href = 'a[href^="content"]'
    sboarddict = get_board(sboard_url,sboard_class,sboard_href)
    for sd in sboarddict.keys():
    #     print("{}:{}".format(sd,sboarddict[sd]))
        paper_url = "http://epaper.wxrb.com/paper/wxrb/html/"+datetmp[0]+"/"+datetmp[1]+"/"+sboarddict[sd]
        paper_title = "title1"  #class = "title1" 文章标题
        paper_content = "content" #class = "content" 文章内容
        hheads={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
        r_purl = requests.get(paper_url,headers=hheads)
        if r_purl.status_code == 200:
            soup = BeautifulSoup(r_purl.content,'lxml')
            get_soup_title = soup.find('div',class_=paper_title)
            get_soup_content = soup.find('div',class_=paper_content)
            for linebreak in get_soup_content.find_all('br'):
                linebreak.extract()
            # print("{}/n{}".format(get_soup_title.text,get_soup_content.get_text()))
            paper_name=str(tdate)+'.txt'
            with open(paper_name,'a') as ne:
                print("write in...")
                ne.writelines(get_soup_title.get_text())
                ne.writelines(get_soup_content.get_text())
                print("write done!")
            break
        break
    break