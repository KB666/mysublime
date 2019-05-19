#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-24 15:08:10
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

import urllib.request
import urllib.parse

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

city = input('请输入你要查询的城市')

formdata = {
    'cname': city,
    'pid': '',
    'pageIndex': '1',
    'pageSize': '10',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
}
request = urllib.request.Request(url=url, headers=headers)

formdata = urllib.parse.urlencode(formdata).encode()

response = urllib.request.urlopen(request, data=formdata)

print(response.read().decode())
