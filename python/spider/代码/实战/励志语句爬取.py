#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-28 15:29:00
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

import urllib.request
import urllib.parse
import re
import time


def handle_request(url, page=None):
    # 拼接出来指定的url
    if page != None:
        url = url + str(page) + '.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_text(href):
    # 调用函数构建请求对象
    request = handle_request(href)
    # 发送请求获取响应
    content = urllib.request.urlopen(request).read().decode()
    # 解析内容
    pattern = re.compile(r'<div class="neirong">(.*?)</div>', re.S)
    lt = pattern.findall(content)
    text = lt[0]
    # print(lt)
    # exit()
    # 写个正则清除图片标签
    pat = re.compile(r'<img .*?>')
    text = pat.sub('', text)
    return text


def parse_content(content):
    # <h3><a href="/lizhi/qianming/20190141219.html"><b>你的努力永远不会背叛你——句句戳心</b></a></h3>
    # 写正则
    pattern = re.compile(
        r'<h3><a href="(.*?)"><b>(.*?)</b></a></h3>')
    lt = pattern.findall(content)
    # 返回的lt是一个列表，每个列表里都有多个元组远足中有两个分别是url和标题
    # 遍历列表
    for href_title in lt:
        # 获取标题
        title = href_title[-1]
        # 获取链接
        href = 'http://www.yikexun.cn' + href_title[0]
        # 向链接发送请求，获取响应内容
        text = get_text(href)
        print('《%s》开始下载...' % title)
        time.sleep(0.5)
        # 写文件
        string = '<h1>%s</h1>%s' % (title, text)
        with open('lizhi.html', 'a') as fp:
            fp.write(string)


def main():
    url = 'http://www.yikexun.cn/lizhi/qianming/list_50_'
    start_page = int(input('请输入起始页码:'))
    end_page = int(input('请输入结束页码:'))
    for page in range(start_page, end_page + 1):
        print('第%s页开始下载......' % page)
        # 根据指定的url和page去生成指定的request
        request = handle_request(url, page)
        # 发送请求
        content = urllib.request.urlopen(request).read().decode()
        # 解析内容
        parse_content(content)
        print('第%s页下载完成......' % page)
        time.sleep(2)


if __name__ == '__main__':
    main()
