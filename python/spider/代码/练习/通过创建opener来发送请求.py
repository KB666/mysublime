#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-28 12:52:33
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

import urllib.request
import urllib.parse

url = ''

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
}

# 创建一个handler
handler = urllib.request.HTTPHandler()


# 通过hnadler创建一个opener
# opener就是一个对象，发送请求时可以直接用opener里的open方法
opener = urllib.request.build_opener(handler)

request = urllib.request.Request(url, headers=headers)

response = opener.open(request)

print(response.read().decode())
