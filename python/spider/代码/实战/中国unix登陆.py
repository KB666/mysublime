#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-07 10:31:25
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

import requests
import json
from bs4 import BeautifulSoup
import time
# 创建会话
s = requests.session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
}
# 对第一个url发送post请求
url_1 = 'http://account.chinaunix.net/login/login'

data = {
    '_t': '1549506591876',
    '_token': '3nKKjeI2jhF5AQieJsNrliQJHamFtJlQnLGgzUhV',
    'password':	'888888KB',
    'username':	'13525186763',
}

r_1 = s.post(url=url_1, headers=headers, data=data)
# 解析返回的json数据
dic = json.loads(r_1.text)
url_2 = 'http://www.chinaunix.net' + dic['data']['url']
# 对第二个url发送post请求
r_2 = s.get(url=url_2, headers=headers)
# 注意编码格式
r_2.encoding = 'gbk'
# 用bs解析第二个url的数据，bs没xpath好用
soup = BeautifulSoup(r_2.text, 'lxml')
url_3 = soup.select('.box > .login > a')[1]['href']
r_3 = s.get(url=url_3, headers=headers)
# 等待浏览器自动跳转
time.sleep(6)
print(r_3.text)
