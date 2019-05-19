#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-24 14:47:34
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

import urllib.request

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
}


url = 'https://www.lagou.com/jobs/list_python?px=default&gm=%E5%B0%91%E4%BA%8E15%E4%BA%BA&city=%E5%85%A8%E5%9B%BD'
request = urllib.request.Request(url=url, headers=headers)
res = urllib.request.urlopen(request)
print(res.read())
