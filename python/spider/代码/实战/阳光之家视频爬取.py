#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-11 15:46:02
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

# http://365yg.com/
'''
先向365.yg.com发送请求
获取响应解析响应获取标题和视频链接
以此向每个连接发送请求
获取响应，获取video标签的src属性
向src发送请求获取响应，保存内容到本地
'''
# 西瓜视频旗下太难爬了
import requests
from bs4 import BeautifulSoup
import time
from lxml import etree
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disadle-gpu')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
}


def handle_tite(widen):
    # 接口捕获
    url = 'http://365yg.com/api/pc/feed/?min_behot_time=0&category=video_new&utm_source=toutiao&widen={}&tadrequire=true&as=A1D51C860174C39&cp=5C6194AC83F9EE1&_signature=CXdPUhAXVRsjuKbsp3I57Ql3T0'
    # 拼成完整的url
    url = url.format(widen)
    r = requests.get(url=url, headers=headers)
    # 解析内容,内容为json数据
    # 通过分析发现要data里面的 title\source_url
    # 将json数据转化为python对象
    obj = json.loads(r.text)
    data = obj['data']
    for video_data in data:
        title = video_data['title']
        a_href = 'http://365yg.com' + video_data['source_url']
        # 发送请求，获取内容，解析内容,获取src
        handle_href(a_href, title)
        break


def handle_href(a_href, title):
    # 通过phantomjs来解决
    path = r'D:\google\Google\Chrome\Application\chromedriver.exe'
    browser = webdriver.Chrome(
        executable_path=path, chrome_options=chrome_options)
    browser.get(a_href)
    time.sleep(3)
    with open('qq.html', 'w', encoding='utf8') as fp:
        fp.write(browser.page_source)
    # 获取源码生成tree对象，让或查找video里面的src属性
    tree = etree.HTML(browser.page_source)
    video_src = tree.xpath(
        '//xg-poster[@class="xgplayer-poster"]/@style')[0]
    pattern = re.compile(r'background-image: url\("(.*?)"\);')
    video_src = pattern.findall(video_src)[0]
    filepath = 'shipin/' + title + '.mp4'
    r = requests.get(video_src, headers=headers)
    with open(filepath, 'wb') as fp:
        fp.write(r.content)


def main():
    # 解析首页返回所有的标题连接
    for widen in range(1, 2):
        pass
    handle_tite(widen)


if __name__ == '__main__':
    main()
