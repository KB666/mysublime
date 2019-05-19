#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-14 16:20:52
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

import requests
from lxml import etree
import time

# 'http://www.ygdy8.net/html/gndy/dyzz/list_23_2.html'
headers = {
    'Host': 'www.ygdy8.net',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://www.ygdy8.net/html/gndy/dyzz/index.html',
}


def make_url(url, url_lis):
    for page in range(1, 11):
        url_lis.append(url % page)
    return(url_lis)


def parse_navigation(url):
    r = requests.get(url=url, headers=headers)
    tree = etree.HTML(r.text)
    navi_list = tree.xpath('//table/tr[2]/td[2]/b/a/@href')
    return(navi_list)


def main():
    url = 'http://www.ygdy8.net/html/gndy/dyzz/list_23_%s.html'
    # 先做出要爬的url
    start_url_lis = []
    start_url_lis = make_url(url, start_url_lis)
    for url in start_url_lis:
        navi_url_lis = parse_navigation(url)
        for url in navi_url_lis:
            url = 'http://www.ygdy8.net' + url
            print(url)
            exit()
            r = requests.get(url=url, headers=headers)
            tree = etree.HTML(r.text)


if __name__ == '__main__':
    main()
