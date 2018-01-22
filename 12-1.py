# -*- coding: utf-8 -*-
# @Date    : 2017-12-17 17:46:29
# @Author  : brkstone
import requests
import threading
import os
import re
from bs4 import BeautifulSoup
import progressbar

# 根据地址下载图片
'''糗事百科热图下载'''


def download(url):
    # print('DOWNLOAD BEGIN')
    name = re.search('(app)\S+(jpg)', url)
    req = requests.get(url, headers=myhead)
    # 以二进制读取并写入
    with open(name.group(), 'wb') as f:
        f.write(req.content)
        f.flush()
# 从每一页下载


def page_down(url, num):
    new_url = url.format(num)
    newreq = requests.get(new_url, headers=myhead)
    newsoup = BeautifulSoup(newreq.text, 'lxml')
    hufu = r'src="(\S*(jpg))"'
    imgre = re.compile(hufu)
    pic_list = imgre.findall(str(newsoup))
    widgets = ['Progress:', progressbar.Percentage(), ' ',
               progressbar.Bar(marker='#', left='[', right=']'),
               ' ', progressbar.ETA(), ' ', progressbar.FileTransferSpeed()]
    with progressbar.ProgressBar(min_value=0, max_value=len(pic_list), widgets=widgets) as pbar:
        for each_pic in pic_list:
            dl_url = 'https:' + each_pic[0]
            pbar.update(pic_list.index(each_pic) + 1)
            download(dl_url)
        pbar.finish()
        print('完成一页。')


# 获得下载初始结束页，每页一个线程


def piclist(url, myhead):
    startpage = eval(input('请输入起始页:'))
    endpage = eval(input('请输入结束页:'))
    print('起始页{}：：结束页{}'.format(startpage, endpage))

    # 获取页的图片列表
    i = 0
    for num in range(startpage, endpage + 1):
        thread_name = 'new_down' + str(i)
        new_thread = threading.Thread(page_down(url, num), name=thread_name)
        new_thread.start()
        new_thread.join()
        i += 1


# 全部完成后判断是否成功，没有下载则报告失败并删除新建的文件夹picsave


def beforefinish(path):
    print(path)
    try:
        os.rmdir(path)
        print('下载未完成！')
    except OSError:
        print('下载完成!')


myhead = {"User-Agent":
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) /AppleWebKit/537.36 ( /KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
picurl = 'https://www.qiushibaike.com/imgrank/page/{}/'
# 在当前位置新建一个picsave文件夹用于存放下载的图片
f_curdir = os.getcwd()
filename = 'picsave'
try:
    os.makedirs(filename)
except FileExistsError:
    filename = input('请输入文件夹名:')
    os.makedirs(filename)
curdir = f_curdir + '\\{}'.format(filename)
os.chdir(curdir)  # 进入创建的文件夹
piclist(picurl, myhead)
# 退出并检测下载文件夹
os.chdir(f_curdir)
beforefinish(curdir)
