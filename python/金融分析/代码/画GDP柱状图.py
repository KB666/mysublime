#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-13 21:45:24
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

'''
数据来自国家统计局官网
'''


# 导入python画图库
import matplotlib.pyplot as plt

list_year = [2006, 2007, 2008, 2009, 2010,
             2011, 2012, 2013, 2014, 2015, 2016, 2017]
list_gdp = [219000, 270000, 319000, 349000, 413000, 489000,
            540000, 595000, 643000, 689000, 744000, 827000]


# 画柱状图
plt.bar(list_year, list_gdp)

# 标识标题及坐标轴信息
plt.title('ddp amount from 2006 to 2017')
plt.xlabel('year')
plt.ylabel('gdp amount')

# 显示画图结果
plt.show()
