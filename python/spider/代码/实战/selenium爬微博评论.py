#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-14 10:41:12
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disadle-gpu')
# 路径
path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
# 创建浏览器对象
browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)

url = 'https://www.thepaper.cn/searchResult.jsp?inpsearch=%E9%9D%9E%E6%B4%B2%E7%8C%AA%E7%98%9F'
browser.get(url)
# print(browser)
time.sleep(5)

browser.save_screenshot('weibo.png')
# 模拟滚动条滚动
js = "var q=document.documentElement.scrollTop=10000"
browser.execute_script(js)

time.sleep(5)
browser.save_screenshot('weibo2.png')
html = browser.page_source
print(html)

browser.quit()
