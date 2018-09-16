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
plt.plot([-2, 2, 3, 4, 5], 'r', label='第一条曲线')
plt.plot([3, 4, 5, 8, 9], 'b', label='第二条曲线')
plt.legend()
plt.grid(True)
plt.axis([0, 5, -3, 9])
plt.xlabel('X-轴坐标', FontProperties=myfont)
plt.ylabel('Y-轴坐标', FontProperties=myfont)
plt.title('matplotlib 演示图', FontProperties=myfont)
plt.show()
