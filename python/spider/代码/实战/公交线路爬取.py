#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-09 22:37:51
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

import requests
from lxml import etree
import time

# 用来保存所有线路信息
items = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
    'Connection': 'close',
}


# https://wuhan.8684.cn/
def parse_navigation():
    url = 'https://wuhan.8684.cn/'
    r = requests.get(url=url, headers=headers)
    # 解析内容获取所有的导航链接
    tree = etree.HTML(r.text)
    # 查找以数字开头的链接
    number_list = tree.xpath('//div[@class="bus_kt_r1"]/a/@href')
    # 查找以字母开头的所有链接
    word_list = tree.xpath('//div[@class="bus_kt_r2"]/a/@href')
    return number_list + word_list


def parse_datials(content):
    tree = etree.HTML(content)
    # 依次获取内容
    bus_number = tree.xpath('//div[@class="bus_i_t1"]/h1/text()')[0]
    bus_number = bus_number.replace('路线&nbsp', '')
    # 获取运行时间
    run_time = tree.xpath('//p[@class="bus_i_t4"][1]/text()')[0]
    # 获取票价信息
    ticket_price = tree.xpath('//p[@class="bus_i_t4"][2]/text()')[0]
    # 获取更新时间
    update_time = tree.xpath('//p[@class="bus_i_t4"][4]/text()')[0]
    # 获取上行总战数
    total_list = tree.xpath('//span[@class="bus_line_no"]/text()')
    up_total = total_list[0]
    # 去除乱码
    up_total = up_total.replace('\xa0', '')
    # 获取上行所有站名
    up_site_list = tree.xpath(
        '//div[@class="bus_line_site "][1]/div/div/a/text()')
    try:
        # 获取下行总站数
        down_total = total_list[1]
        down_total = down_total.replace('\xa0', '')
        # 获取下行所有站名
        down_site_list = tree.xpath(
            '//div[@class="bus_line_site "][2]/div/div/a/text()')
    except Exception as e:
        down_total = ''
        down_site_list = []
    item = {
        '线路名': bus_number,
        '运行时间': run_time,
        '票价信息': ticket_price,
        '更新时间': update_time,
        '上行站数': up_total,
        '上行站点': up_site_list,
        '下行站数': down_total,
        '下行站点': down_site_list,
    }
    items.append(item)


def parse_second_route(content):
    tree = etree.HTML(content)
    # xpath解析每个路线url
    route_list = tree.xpath('//div[@id="con_site_1"]/a/@href')
    route_name = tree.xpath('//div[@id="con_site_1"]/a/text()')
    i = 0
    # 遍历上述列表获取详细信息
    for route in route_list:
        print('开始爬取%s线路' % route_name[i])
        route = 'https://wuhan.8684.cn/' + route
        r = requests.get(url=route, headers=headers)
        # 解析内容，获取详细信息
        parse_datials(r.text)
        time.sleep(2)
        print('成功爬取%s线路' % route_name[i])
        i += 1


def parse_second(navi_list):
    # 遍历传入的列表发送请求，解析内容，获取每个页面所有的url
    for url in navi_list:
        url = 'https://wuhan.8684.cn/' + url
        print('爬取%s所有的公交信息' % url)
        r = requests.get(url=url, headers=headers)
        time.sleep(1)
        # 解析内容，获取详细url
        parse_second_route(r.text)


def main():
    # 爬取第一页所有导航链接
    navi_list = parse_navigation()
    time.sleep(1)
    # 爬取二级页面需要找到所有以1开头的公交线路
    parse_second(navi_list)
    # 爬取完毕
    fp = open('wuhanbus.txt', 'w', encoding='utf8')
    for item in items:
        fp.write(str(item) + '\n')
    print('文件写入完成...........')
    fp.close()


if __name__ == '__main__':
    main()
