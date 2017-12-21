# -*- coding: utf-8 -*-
# @Date    : 2017-12-19 21:40:30
# @Author  : brkstone
import requests
import re
from bs4 import BeautifulSoup
import lxml

homeurl = 'http://jandan.net/ooxx'
myhead = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
req = requests.get(homeurl, headers=myhead)
mysoup = BeautifulSoup(req.text, 'lxml')
li_list = mysoup.find("span", class_="current-comment-page")
page_num = re.search('\d+', str(li_list)).group()
startpage = eval(page_num) - 3
endpage = eval(page_num)
print('{}{}'.format(startpage, endpage))

# 获取页的图片列表
for i in range(startpage, endpage + 1):
    new_url = 'http://jandan.net/ooxx/page-{}#comments'.format(i)
    newreq = requests.get(new_url, headers=myhead)
    newsoup = BeautifulSoup(newreq.text, 'lxml')
    # print(newsoup.prettify())
    hufu = r'href="([.*\S]*(\.gif|\.img))"'
    imgre = re.compile(hufu)
    text_list = newsoup.find_all(imgre)
    print(text_list)
    print('+++++++++++++++++++++++++++++++++++++')
