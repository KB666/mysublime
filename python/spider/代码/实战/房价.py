#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-03 22:05:07
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

"""
防爬虫做的不错
"""

# 'url = 'http://m.jiwu.com/fangjia/''
import requests
from lxml import etree
import time

items = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
    'Connection': 'close',
}


def geturl():
    url = 'http://m.jiwu.com/fangjia/'
    r = requests.get(url=url, headers=headers)
    tree = etree.HTML(r.text)
    lis = tree.xpath('//table[@class="zmtable"]/tr/td/a/@href')
    return lis


def handel_request(url):
    r = requests.get(url=url, headers=headers)
    a = '阿布' in r.text
    if a:
        print('此城市无数据')
    else:
        tree = etree.HTML(r.text)
        loc_tim = tree.xpath('//div[@class="content"]/div/h1/text()')[0]
        new_price = str(tree.xpath(
            '//div[@class="inbox"][1]/div[1]/div/span/text()')[0]) + '元/㎡'
        new_price_rate = tree.xpath(
            '//div[@class="inbox"][1]/div[1]/div[2]/span/span/text()')[0].replace(' ', '').replace('\r', '').replace('\n', '')
        secondhand_price = str(tree.xpath(
            '//div[@class="inbox"][2]/div[1]/div[1]/span/text()')[0]) + '元/㎡'
        secondhand_rate = tree.xpath(
            '//div[@class="inbox"][2]/div[1]/div[2]/span/text()')[0]
        item = {
            '时间和地区': loc_tim,
            '新房价格': new_price,
            '新房价格浮动比率': new_price_rate,
            '二手房价格': secondhand_price,
            '二手房价格浮动比率': secondhand_rate,
        }
        items.append(item)


def main():
    # 获取表中对应地区的链接
    url_list = geturl()
    time.sleep(2)
    print('已获取地区链接')
    for url in url_list:
        handel_request(url)
        print('一个城市已经获取')
    fp = open('房价信息.txt', 'w', encoding='utf8')
    for item in items:
        fp.write(str(item) + '\n')
    print('文件写入完成...........')
    fp.close()


if __name__ == '__main__':
    main()
