#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-23 19:43:27
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

import requests
from lxml import etree
import time


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}


def handle_request(page):
    if page == 1:
        url = 'http://www.moa.gov.cn/gk/yjgl_1/yqfb/index.htm'
    else:
        url = 'http://www.moa.gov.cn/gk/yjgl_1/yqfb/index_{}.htm'.format(
            str(page - 1))
    r = requests.get(url=url, headers=headers)
    return r.text


def main():
    for page in range(1, 2):
        content = handle_request(page)
        print(content)


if __name__ == '__main__':
    main()
