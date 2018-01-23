# -*- coding: utf-8 -*-
# @Date    : 2018-01-23 19:22:23
# @Author  : brkstone
import requests


url = 'https://www.toutiao.com/api/pc/feed/?category=news_sports&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A185CA7675BF630&cp=5A65DF1623B0FE1&_signature=GBSXdQAAQnUpAGXIDraHoBgUl2'

headers = {"User-Agent":
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/63.0.3239.132 Safari/537.36"}
rqd = requests.get(url, headers=headers)
print(rqd.json())
print(type(rqd.json()))
