#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-27 18:27:06
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

import urllib.request
import urllib.parse
import re

url = 'https://www.kuaidaili.com/free/inha/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request).read().decode(
    'utf-8', 'ignore').replace(u'\xa9', u'')


pattern1 = re.compile(r'<td data-title="IP">(.*?)</td>')
pattern2 = re.compile(r'<td data-title="PORT">(.*?)</td>')

lt1 = pattern1.findall(response)
lt2 = pattern2.findall(response)

filename = 'proxy.txt'

with open(filename, 'a') as fp:
    for i in range(0, len(lt1)):
        fp.write(lt1[i] + ':' + lt2[i] + '\n')
