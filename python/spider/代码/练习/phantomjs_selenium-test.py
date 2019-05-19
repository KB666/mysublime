#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-05 20:04:54
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

from selenium import webdriver
import time

# 模拟创建一个浏览器对象，然后通过对象去操作浏览器
path = 'D:\\phantomjs\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe'

browser = webdriver.PhantomJS(path)

url = 'http://www.baidu.com/'
browser.get(url)
# print(browser)
time.sleep(2)

# 查找输入框
my_input = browser.find_element_by_id('kw')
# 往框里面写文字
my_input.send_keys('汽车')
time.sleep(2)
# 保存当前页面的图片
browser.save_screenshot('111.png')
# 查找搜索框
button = browser.find_element_by_class_name('s_btn')
button.click()
time.sleep(2)

browser.quit()
