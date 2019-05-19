#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-27 17:33:43
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

import re

#  first
# string = '<p><div><span>猪八戒</span></div></p>'
# pattern = re.compile(r'<(\w+)><(\w+)>\w+</\2></\1>')
# ret = pattern.search(string)
# print(ret)

# second
# string = '''hate is a beautiful feel
# love you very much
# love me
# love her
# love your family
# '''
# # pattern = re.compile(r'love', re.M)
# # pattern = re.compile(r'love')
# # ret = pattern.search(string)
# ret = re.sub(r'love', 'hate', string)
# print(ret)

# third

# def fn(a):
#     ret = int(a.group())
#     return str(ret - 10)
# string = '我喜欢身高为170的女孩'

# pattern = re.compile(r'\d+')
# ret = pattern.sub(fn, string)

# print(ret)
