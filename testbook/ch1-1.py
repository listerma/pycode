#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-13 23:13:28
# @Author  : brkstone (mc0909dz@hotmail.com)
# @Link    : https://github.com/listerma/pycode
# @notes   : 鸡汤+1


import matplotlib as mpl
import matplotlib.pyplot as plt


myfont = mpl.font_manager.FontProperties(
    fname='/Users/yuan/pycode/font/simhei.ttf')
plt.plot([727, 641, 678, 714, 628], 'r', label='20180927')
plt.plot([725, 636, 678, 714, 627], 'g', label='20180928')
plt.plot([0, 0, 0, 0, 0], 'b', label='第二条曲线')
plt.legend()
plt.grid(True)
plt.axis([0, 5, 0, 1000])
plt.xlabel('X-轴坐标', FontProperties=myfont)
plt.ylabel('Y-轴坐标', FontProperties=myfont)
plt.title('百分比演化图', FontProperties=myfont)
plt.show()
