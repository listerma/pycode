# -*- coding: utf-8 -*-
# @Date    : 2018-01-20 19:04:55
# @Author  : brkstone
from bs4 import BeautifulSoup
import requests
import re
import time
'''爬取8hr 13页所有段子，包括段子内容、段子作者、作者性别和年龄、”好笑” 数、评论数。
将以上信息存入 txt 文件。'''


def write_data(name, sex, age, gut, stats, stats_cmt):
    brk = ' ' * 5
    text1 = name
    text1 += sex + brk + age + '\n'
    text1 += gut + '\n'
    text1 += '笑脸：' + stats + brk + '评论：' + stats_cmt + '\n'
    with open('段子.txt', 'a', encoding='utf-8') as file:
        file.write(text1)
        # 分隔
        file.write('==' * 20 + '\n')


def dealwreq(req):
    data = BeautifulSoup(req.text, 'lxml')
    # rule_1 = re.compile('qiushi_tag\w*\d')
    # 每页段子块
    data_find = data.find_all("div", id=re.compile('qiushi_tag\w*\d'))
    # print(type(data_find))
    # print(len(data_find))
    for one in data_find:
        # print(data_find[i])
        tem = BeautifulSoup(str(one), 'lxml')
        # 返回作者名字
        name = tem.find("h2").string
        sex_tem = tem.find_all("div", class_=re.compile('article.*?con'))
        # 返回作者性别sex，年龄age
        # print(sex_tem)
        if len(sex_tem) == 0:
            # 如果匿名用户，age&sex为空
            age = ''
            sex = ''
        else:
            age = sex_tem[0].string
        # get()返回list
            if re.match('man', sex_tem[0].get('class')[0]) is None:
                sex = '女'
            else:
                sex = '男'
        # 返回段子内容
        fruit = tem.find("div", class_="content")
        gut = fruit.find("span").get_text()
        stats = tem.find("span", class_="stats-vote").find("i").get_text()
        stats_cmt = tem.find(
            "span", class_="stats-comments").find("i").get_text()
        write_data(name, sex, age, gut, stats, stats_cmt)
        # print(gut)
        # print(name)
        # print(sex)
        # print(age)
        # print('laugh face:', stats)
        # print('comments:', stats_cmt)
        # print('==' * 20)


# 每页地址
for i in range(1, 14):
    url = 'https://www.qiushibaike.com/8hr/page/i/'
    try:
        req = requests.get(url)
    except Exception as e:
        for _ in range(1, 4):
            req = requests.get(url)
            if req.status_code is 200:
                break
            time.sleep(2)
    dealwreq(req)
print('抓取结束！')
