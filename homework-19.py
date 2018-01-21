# -*- coding: utf-8 -*-
# @Date    : 2018-01-09 18:12:59
# @Author  : brkstone
import requests
import os
from lxml import etree
import time
from random import randint
# 存放位置


def savepath():
    curpath = os.path.realpath('.')
    try:
        os.mkdir('doubanmovie')
    except Exception as e:
        print('file exsit')
    filepath = curpath + '/doubanmovie'
    return filepath


def transchar(instr):
    '''
    转换 / . 为空格
    '''
    intab = '/.'
    outtab = '  '
    outstr = instr.translate(str.maketrans(intab, outtab))
    return outstr


def dealmv(originfile):
    '''
    originfile : 存储文件位置
    获取序号 电影名 导演 平均评分
    '''
    os.chdir(originfile)
    for i in range(0, 226, 25):  # 226
        url = 'https://movie.douban.com/top250?start=' + str(i) + '&filter='
        # print(url)
        try:
            req = requests.get(url, headers=myhead, timeout=0.2)
            chooser = etree.HTML(req.text)
            lis = chooser.xpath('//li/div[@class="item"]')  # 获取所有li结点
            for x in lis:
                mvseal = x.xpath('div//em/text()')[0]
                mvname = x.xpath('div//span[@class="title"]/text()')[0]
                director = x.xpath('div//div[@class="bd"]/p/text()')[0]  # 导演
                director = transchar(director).strip()
                rating = x.xpath('div//div[@class="bd"]//span[@property="v:average"]/text()')[0]  # 平均评分
                # print(mvseal, mvname, director, 'OOOP', rating)
                singlemv = mvseal + ' ' + mvname + ' ' + director + ' ' + rating + '\n'
                # print(singlemv)
                with open('mv-list.txt', 'a', encoding='utf-8') as ftem:
                    ftem.write(singlemv)
        except Exception as e:
            # print('bad apple：', e)  # 不成功的暂不处理
            print('{}至{}获取失败！'.format(i + 1, i + 25))
        time.sleep(randint(1, 3))


def main():
    movefile = savepath()  # 存放文件夹
    dealmv(movefile)
    print('抓取结束')


if __name__ == '__main__':
    myhead = {
        'User-Agent': 'Mozilla / 5.0 (Windows NT 6.1) AppleWebKit / 537.36 (KHTML,\
         like Gecko) Chrome / 37.0.2062.124 Safari / 537.36',
        'Connection': 'Keep-Alive',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Accept-Encoding': 'gzip,deflate,sdch',
        'Accept': '*/*',
        'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
        'Cache-Control': 'max-age=0'}
    main()
