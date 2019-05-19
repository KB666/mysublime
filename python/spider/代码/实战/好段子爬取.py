#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-01 18:11:25
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

import urllib.request
import urllib.parse
from lxml import etree
import time
import json

item_list = []


def handler_request(url, page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
    }
    # 处理python爬虫中有中文的url
    word = urllib.parse.quote('经典段子')
    url = url % (word, page)
    request = urllib.request.Request(url=url, headers=headers)
    return request


def parse_content(content):
    tree = etree.HTML(content)
    ret_list = tree.xpath('//article[@class="post"]')
    for ret in ret_list:
        # 获取标题
        title = ret.xpath('.//div[@class="post-head"]/h1/a/text()')[0]
        # 获取内容
        text_lt = ret.xpath('.//div[@class="post-content"]/p/text()')
        text = ''.join(text_lt)
        item = {
            '标题': title,
            '内容': text,
        }
        # 将内容添加到列表中
        item_list.append(item)


def main():
    url = 'http://duanziwang.com/category/%s/%s/'
    start_page = int(input('请输入起始页码:'))
    end_page = int(input('请输入结束页码:'))
    for page in range(start_page, end_page + 1):
        print('开始爬取%s页' % page)
        request = handler_request(url, page)
        content = urllib.request.urlopen(request).read().decode()
        # 解析内容
        parse_content(content)
        print('第%s页爬取成功' % page)
        time.sleep(2)
    string = json.dumps(item_list, ensure_ascii=False)
    with open('段子.txt', 'w', encoding='utf8') as fp:
        fp.write(string)


if __name__ == '__main__':
    main()
