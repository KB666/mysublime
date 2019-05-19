#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-10 20:04:08
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

import requests
from lxml import etree

items = []


def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134', }
    url = 'https://www.gushiwen.org/'
    r = requests.get(url=url, headers=headers)
    tree = etree.HTML(r.text)
    tree_list = tree.xpath('//div[@class="left"]/div[@class="sons"]')
    for tree in tree_list:
        # 名字
        title = tree.xpath('./div[@class="cont"]/p/a/b/text()')[0]
        # 朝代
        time = tree.xpath(
            './div[@class="cont"]/p[@class="source"]/a/text()')[0]
        # 作者
        author = tree.xpath(
            './div[@class="cont"]/p[@class="source"]/a/text()')[1]
        # 文章
        text = tree.xpath(
            './div[@class="cont"]/div[@class="contson"]/text()')
        # text.replace('\n','').replace('\r','').replace('\t','')
        # # 标签
        tag = tree.xpath('./div[@class="tag"]/a/text()')
        item = str(title)+str(time)+str(author)+str(text)+str(tag)
        # item = {
        #     '标题': title,
        #     '朝代': time,
        #     '作者': author,
        #     '文章': text,
        #     '标签': tag,
        # }
        items.append(item)
    with open('gushi.txt', 'w', encoding='utf8') as fp:
        fp.write(str(items))


if __name__ == '__main__':
    main()
