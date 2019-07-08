#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-23 20:19:47
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disadle-gpu')
# 路径
path = r'D:\chromedriver\chromedriver.exe'
# 创建浏览器对象
browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)


def handle_request(page):
    if page == 1:
        url = 'http://www.moa.gov.cn/gk/yjgl_1/yqfb/index.htm'
    else:
        url = 'http://www.moa.gov.cn/gk/yjgl_1/yqfb/index_{}.htm'.format(
            str(page - 1))
    browser.get(url)
    time.sleep(2)
    return browser.page_source


def main():
    for page in range(1, 2):
        content = handle_request(page)
        print(content)


if __name__ == '__main__':
    main()
