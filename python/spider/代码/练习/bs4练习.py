#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-29 13:08:05
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

from bs4 import BeautifulSoup

# 生成对象
soup = BeautifulSoup(open('bs.html', encoding='utf8'), 'lxml')

# print(soup)
# print(type(soup))
# print(soup.div)
# print(soup.a['href'])
# print(soup.a.attrs)
# print(soup.a.text)
# print(soup.find('a', title ='qin'))
# print(soup.find_all('a'))
# print(soup.find_all(['a','b']))
# print(soup.select('.tang > li > a'))