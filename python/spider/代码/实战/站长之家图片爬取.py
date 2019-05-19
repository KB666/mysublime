#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-02 12:46:43
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

import urllib.request
import urllib.parse
from lxml import etree
import time
import os


def handle_request(url, page):
    # 由于第一页和后边的url类型不同，所以要先判断一下
    if page == 1:
        url = url.format('')
    else:
        url = url.format('_' + str(page))
    # print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def parse_content(content):
    tree = etree.HTML(content)
    # 图片懒加载
    image_list = tree.xpath('//div[@id="container"]/div/div/a/img/@src2')
    # print(image_list)
    # print(len(image_list))
    for image_src in image_list:
        print('...正在此页下载图片...')
        download_image(image_src)
        time.sleep(1)


def download_image(image_src):
    # 创建一个文件夹
    dirpath = 'pic'
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    # 文件名
    filename = os.path.basename(image_src)
    filepath = os.path.join(dirpath, filename)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
    }
    request = urllib.request.Request(url=image_src, headers=headers)
    response = urllib.request.urlopen(request)
    with open(filepath, 'wb') as fp:
        fp.write(response.read())


def main():
    url = 'http://sc.chinaz.com/tupian/wenzitupian{}.html'
    start_page = int(input('请输入起始页码:'))
    end_page = int(input('请输入结束页码:'))
    for page in range(start_page, end_page + 1):
        print('第%s页开始下载..........' % page)
        request = handle_request(url, page)
        content = urllib.request.urlopen(request).read().decode()
        parse_content(content)
        print('第%s页下载成功..........' % page)
        time.sleep(1)


if __name__ == '__main__':
    main()
