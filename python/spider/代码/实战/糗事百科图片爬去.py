#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-28 13:54:40
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

import urllib.request
import urllib.parse
import re
import os
import time


def handler_request(url, page):
    url = url + str(page) + '/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request

# <div class="thumb">
# <a href="/article/121478398" target="_blank">
# <img alt="image" src="//pic.qiushibaike.com/system/pictures/12147/121478398/medium/Q2J2YTYO24O0O7O5.jpg">
# </a>
# </div>


def download_image(content):
    pattern = re.compile(
        r'<div class="thumb">.*?<img src="(.*?)" .*?>.*?</div>', re.S)
    lt = pattern.findall(content)
    # print(lt)
    # 遍历列表依次下载图片
    for image_src in lt:
        # 先处理一下链接
        image_src = 'https:' + image_src
        # 发送请求下载图片
        # 创建文件夹
        dirname = 'qiutu'
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        # 图片名字
        filename = image_src.split('/')[-1]
        filepath = dirname + '/' + filename
        print('%s图片正在下载......' % filename)
        urllib.request.urlretrieve(image_src, filepath)
        print('%s图片下载完成......' % filename)
        time.sleep(1)


def main():
    url = 'https://www.qiushibaike.com/pic/page/'
    start_page = int(input('请输入起始页码:'))
    end_page = int(input('请输入结束页码:'))
    for page in range(start_page, end_page + 1):
        print('第%s页开始下载......' % page)
        # 生成请求对象
        request = handler_request(url, page)
        # 发送请求对象，获取响应内容
        content = urllib.request.urlopen(request).read().decode()
        # 解析内容提取所有的图片链接，下载图片
        download_image(content)
        print('第%s页下载完成......' % page)
        print('*'*20)
        time.sleep(2)


if __name__ == '__main__':
    main()

