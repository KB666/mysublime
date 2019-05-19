#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-24 14:48:22
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Version : $Id$

import urllib.request
import urllib.parse

url = 'https://movie.douban.com/top250'

page = int(input('请输入您要查询的页码数'))

data = {
    'start': (page - 1) * 25,
}

query_string = urllib.parse.urlencode(data)

url = url + '?' + query_string

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

print(response.read().decode())
