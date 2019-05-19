#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-09 22:06:19
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disadle-gpu')
# 路径
path = r'D:\google\Google\Chrome\Application\chromedriver.exe'
# 创建浏览器对象
browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
print(browser)
# 其实用法与phantomjs大抵相同，
