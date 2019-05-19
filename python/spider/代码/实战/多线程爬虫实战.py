#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-12 16:04:17
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$
'''
未能完美控制解析进程结束时间，导致爬取页数比输入页数少两页，有影响，但影响比较小
'''


import threading
import time
import requests
import json
from queue import Queue
from lxml import etree

# 用来存放采集线程
g_crawl_list = []
# 用来存放解析线程
g_parse_list = []


class CrawlThread(threading.Thread):
    """docstring for CrawThre"""

    def __init__(self, name, page_queue, data_queue):
        super(CrawlThread, self).__init__()
        self.name = name
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.url = 'http://www.fanjian.net/jiantu-{}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
        }

    def run(self):
        print('%s---线程启动' % self.name)
        while 1:
            if self.page_queue.empty():
                break
            # 从队列中取出页码
            page = self.page_queue.get()
            # 拼接url，发送请求
            url = self.url.format(page)
            r = requests.get(url, headers=self.headers)
            # 将响应保存到data_queue中
            self.data_queue.put(r.text)
        print('%s---线程结束' % self.name)


class ParseThread(threading.Thread):
    """docstring for CrawThre"""

    def __init__(self, name, page_queue, data_queue, fp, lock):
        super(ParseThread, self).__init__()
        self.name = name
        self.data_queue = data_queue
        self.page_queue = page_queue
        self.fp = fp
        self.lock = lock

    def run(self):
        print('%s---线程启动' % self.name)
        while 1:
            if self.data_queue.empty() and self.page_queue.empty():
                break
            # 从data_queue中取出数据
            data = self.data_queue.get()
            # 解析内容
            self.parse_content(data)
        print('%s---线程结束' % self.name)

    def parse_content(self, data):
        tree = etree.HTML(data)
        # 先查出来所有的li，再从li里面找自己的标题和url
        li_list = tree.xpath('//li[@class="cont-item"]')
        items = []
        for info in li_list:
            # 获取图片标题
            title = info.xpath('.//h2/a/text()')[0]
            # 获取图片url
            image_url = info.xpath('.//div/p/img/@data-src')
            item = {
                '标题': title,
                '链接': image_url,
            }
            items.append(item)
        # 写到文件中
        self.lock.acquire()
        self.fp.write(json.dumps(items, ensure_ascii=False) + '\n')
        self.lock.release()


def creat_queue():
    # 创建页码队列
    page_queue = Queue()
    for page in range(1, 10):
        page_queue.put(page)
    # 创建内容队列
    data_queue = Queue()
    return page_queue, data_queue


# 创建采集线程
def creat_crawl_thread(page_queue, data_queue):
    crawl_name = ['crawl_no1', 'crawl_no2', 'crawl_no3']
    for name in crawl_name:
        tcrawl = CrawlThread(name, page_queue, data_queue)
        # 保存到列表
        g_crawl_list.append(tcrawl)


# 创建解析线程
def creat_parse_thread(page_queue, data_queue, fp, lock):
    parse_name = ['parse_no1', 'parse_no2', 'parse_no3']
    for name in parse_name:
        tparse = ParseThread(name, page_queue, data_queue, fp, lock)
        # 保存到列表
        g_parse_list.append(tparse)


def main():
    # 创建队列函数
    page_queue, data_queue = creat_queue()
    # 保存文件
    fp = open('jian.json', 'a', encoding='utf8')
    # 创建锁
    lock = threading.Lock()
    # 创建采集线程
    creat_crawl_thread(page_queue, data_queue)
    time.sleep(3)
    # 创建解析线程
    creat_parse_thread(page_queue, data_queue, fp, lock)

    # 启动所有线程
    for tcrawl in g_crawl_list:
        tcrawl.start()
    for tparse in g_parse_list:
        tparse.start()

    # 主线程等待子线程结束
    for tcrawl in g_crawl_list:
        tcrawl.join()
    for tparse in g_parse_list:
        tparse.join()

    fp.close()
    print('主线程子线程全部结束')


if __name__ == '__main__':
    main()
