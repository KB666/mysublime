#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-28 13:01:09
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

import urllib.request
import urllib.parse

handler = urllib.request.ProxyHandler({'http': 'xxx.xxx.xxx.xxx:xxxx'})

# 创建哦opener
opener = urllib.request.build_opener(handler)
url = ''

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
}

request = urllib.request.Request(url=url,headers=headers)

response = opener.open(request)

print(response.read().decode())
