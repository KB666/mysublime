#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-27 14:32:58
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

import requests
from lxml import etree

# url = 'https://www.xicidaili.com/nn/'

lis = []


def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134', }
    url = 'https://www.xicidaili.com/nn/'
    r = requests.get(url=url, headers=headers)
    tree = etree.HTML(r.text)
    tree_list = tree.xpath('//table[@id="ip_list"]/tr')
    for rtree in tree_list:
        a = rtree.xpath('.//td/text()')
        lis.append(a)
    lis.pop(0)
    filename = 'proxy.txt'

    with open(filename, 'a') as fp:
        for i in range(0, len(lis)):
            fp.write(lis[i][0] + ':' + lis[i][1] + '\n')


if __name__ == '__main__':
    main()
